---
last_verified: 2026-09-04
tool_version: n/a
sources: []
---

# Using HTTPie in GitHub Actions CI/CD

## Purpose

This document describes how to integrate HTTPie into GitHub Actions CI/CD pipelines with proper HTTP status-code gating, request timeouts, and secret management. It covers the workflow YAML, the flags that matter most in automated environments, and the common failure modes that cause CI jobs to pass when they should fail or hang indefinitely.

## When to use

Use HTTPie in CI/CD when:

- Running post-deployment smoke tests to confirm a service responds with expected status codes.
- Making authenticated API calls from a pipeline (e.g., triggering downstream builds, posting to Slack webhooks).
- Needing selective status-code tolerance, such as accepting a 404 during a canary rollout but rejecting any 5xx response.

HTTPie's `--check-status` provides finer-grained exit-code control than `curl -f`, and its request-item syntax makes header injection and JSON body construction more readable inside workflow files. For simple one-off checks where `curl` is already available and no selective gating is needed, `curl` remains the lighter choice.

## Prerequisites

- HTTPie installed on the runner (`pip install httpie` or via `uv`).
- `jq` for JSON response parsing (optional but recommended).
- GitHub repository secrets configured for any API tokens, passwords, or keys.
- GitHub environment variables configured for non-secret config (base URLs, endpoints).
- A `tox.ini` or equivalent configuration already present in the repository (for pipelines that combine HTTPie smoke tests with tox-based test matrices).

## Steps

### Step 1 — Install HTTPie on the runner

```yaml
- name: Install httpie
  run: pip install httpie jq
```

The default GitHub Actions runner does not ship with HTTPie. Install it explicitly in a setup step so that `http` is available to all subsequent steps. Using `pip install` places the tool in the runner's system Python path.

### Step 2 — Define secrets and environment variables

```yaml
env:
  API_BASE_URL: ${{ vars.API_BASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}
```

GitHub Actions distinguishes between two interpolation sources:

- `secrets.*` — encrypted values visible only to workflows in this repository. Use for tokens, passwords, and any credential that must not appear in logs. GitHub automatically masks exact-match strings with `***` in job output.
- `vars.*` — plaintext environment variables. Use for non-sensitive configuration like base URLs, endpoints, or feature flags.

Never hardcode secrets in workflow files or source-controlled session files. Always read them from `secrets.*`.

### Step 3 — Configure `--check-status` for CI gating

```yaml
- name: Health check
  run: http --ignore-stdin --check-status --timeout 30 GET "$API_BASE_URL/health"
  env:
    API_BASE_URL: ${{ vars.API_BASE_URL }}
```

`--check-status` makes HTTPie exit non-zero when the response status code is 4xx or 5xx. The exit code mapping is:

| Exit code | Meaning |
|-----------|---------|
| 0 | 2xx response |
| 1 | Generic failure (non-HTTP) |
| 2 | Timeout |
| 3 | Unexpected redirect (3xx without `--follow`) |
| 4 | HTTP 4xx client error |
| 5 | HTTP 5xx server error |
| 6 | Exceeded `--max-redirects` |

A non-zero exit code fails the GitHub Actions step, which fails the job. This is the core CI gating mechanism — without `--check-status`, HTTPie exits `0` even on HTTP 500 responses, causing broken services to pass CI silently.

### Step 4 — Set `--timeout` for CI reliability

```yaml
- name: API request with timeout
  run: |
    http --ignore-stdin --check-status \
      --timeout 15 \
      GET "$API_BASE_URL/api/users/1" \
      "Authorization:Bearer $API_KEY"
```

`--timeout` caps the entire request lifecycle (connection + transfer) in seconds. In CI, always set an explicit timeout to prevent jobs from hanging when a service is slow or unresponsive. A common pattern is 15–30 seconds for smoke tests; tune based on real latency data from your staging environment.

### Step 5 — Use `--ignore-stdin` to prevent CI hangs

```yaml
http --ignore-stdin --check-status --quiet GET "$API_URL/endpoint"
```

Outside an interactive terminal (cron, CI, GitHub Actions), stdin may be redirected or closed. When no data items are provided on the command line and stdin is open, HTTPie waits for a request body that never arrives, causing the job to hang indefinitely. `--ignore-stdin` tells HTTPie to skip reading from stdin, so the call completes immediately. This flag is non-optional in CI scripts.

### Step 6 — Manage authentication with sessions

```yaml
- name: Authenticated smoke test with session
  run: |
    http --session=./ci-session.json \
      --ignore-stdin --check-status --timeout 10 \
      POST "$API_BASE_URL/auth/login" \
      "Authorization:Bearer $API_KEY"
    http --session=./ci-session.json \
      --ignore-stdin --check-status --timeout 10 \
      GET "$API_BASE_URL/api/protected"
  env:
    API_BASE_URL: ${{ vars.API_BASE_URL }}
    API_KEY: ${{ secrets.API_KEY }}
- name: Cleanup session
  if: always()
  run: rm -f ./ci-session.json
```

Session files persist cookies and auth headers between requests. In CI, write the session to the working directory (use the `./` prefix) so it does not pollute `~/.config/httpie/`. Always delete the session file in a cleanup step — after an API token is rotated, a stale session may still send the old `Authorization` header.

For a reusable wrapper that bundles `--ignore-stdin`, `--check-status`, `--timeout`, and exit-code message mapping, see the existing [ci-httpie-wrapper.sh](../scripts/ci-httpie-wrapper.sh). A complete smoke-test script example is in [ci-safe-api-smoke-test.sh](../scripts/ci-safe-api-smoke-test.sh).

## Verify

1. Trigger a workflow run against a known-good endpoint — the step should succeed (exit 0).
2. Point a step at an endpoint that returns 404 — the step should fail with exit code 4.
3. Temporarily set `--timeout 1` against a slow endpoint — the step should fail with exit code 2.
4. Confirm that `$API_KEY` does not appear in the job log (GitHub masks secrets automatically; verify masking works for your token format).

A complete workflow file that combines all of the above patterns:

```yaml
name: API Smoke Tests
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 6 * * *'
jobs:
  smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install httpie
        run: pip install httpie jq
      - name: Health check
        run: http --ignore-stdin --check-status --timeout 30 GET "$API_BASE_URL/health"
        env:
          API_BASE_URL: ${{ vars.API_BASE_URL }}
      - name: Authenticated request
        run: |
          http --ignore-stdin --check-status --timeout 15 \
            --session=./ci-session.json \
            GET "$API_BASE_URL/api/users/1" \
            "Authorization:Bearer $API_KEY"
        env:
          API_BASE_URL: ${{ vars.API_BASE_URL }}
          API_KEY: ${{ secrets.API_KEY }}
      - name: Cleanup
        if: always()
        run: rm -f ./ci-session.json
```

## Common errors

- **Job hangs on stdin:** HTTPie blocks waiting for a request body when stdin is not a terminal. Always pass `--ignore-stdin` in CI scripts.
- **Secrets not propagated:** `secrets.*` values are only available inside the `run:` block where they are declared in `env:`. Declaring them at `jobs:` or `steps:` level does not automatically pass them into the shell.
- **Stale session sends old token:** After rotating an API key, the session file from a previous run may still carry the old `Authorization` header. Delete the session file or run `rm -f` in a cleanup step with `if: always()`.
- **Missing HTTPie on runner:** The `http` command is not pre-installed on GitHub Actions runners. Install it explicitly; a missing command produces a cryptic `command not found` error.
- **Timeout too short:** Setting `--timeout` below the expected response time causes intermittent failures. Start with 30 seconds for smoke tests and tune downward based on real latency data.
- **Exit-code masking:** `--check-status` alone does not guarantee the job logs show *why* it failed. The raw response body is printed to stderr by default; pipe through `jq` or redirect to inspect the failure payload.

## References

- [CI smoke test script](../scripts/ci-safe-api-smoke-test.sh) — working example of `--check-status` and `--ignore-stdin`
- [ci-httpie-wrapper.sh](../scripts/ci-httpie-wrapper.sh) — reusable bash library wrapping `http` with CI-safe defaults and exit-code message mapping
- [Session reuse patterns](../docs/scripting-request-items-offline-gating.md) — using `--session` for authenticated multi-request workflows
- [CI gating comparison notebook](../notebooks/compare-httpie-curl-ci-gating.ipynb) — `--check-status` vs `curl -f` exit-code semantics
