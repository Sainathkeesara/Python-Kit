---
last_verified: 2026-08-14
tool_version: 3.2.4
sources:
  - https://httpie.io/docs/cli/scripting
  - https://pypi.org/project/httpie/
---

# Scripting with httpie: request items, --offline, and safe status gating

I've been using httpie interactively for a while, but this doc collects what I learned about making it script-friendly. Most of it comes from the official scripting docs, and it pairs with the smoke-test script already in this kit (`httpie/scripts/ci-safe-api-smoke-test.sh`), which chains these ideas together end to end.

## The request-item parts after the URL

A call is a URL plus request items after it. Data fields go on the command line as `key=value`, and httpie turns them into the request body. The trap I keep hitting: a body fed through `stdin` **can't** be combined with data fields specified on the command line — the docs are explicit about it, and the runtime error spells the same rule out as "Request body ... and request data (key=value) cannot be mixed". So per call, pick one way to supply the body: either pipe it in, or list it as `key=value` items, never both.

## --offline: build and preview a request without sending it

`--offline` builds the request and prints it without sending anything:

```bash
http --offline POST https://example.com/api/users name=john
```

It has the side effect of automatically activating `--print=HB`, so you see the request headers and body that *would* be sent. That's useful for API-doc examples and dry runs where you don't want to actually hit the server.

## --check-status: turn non-2xx into a real exit code

On its own, httpie is happy to show you a 500 body and move on. `--check-status` changes that: it instructs HTTPie to exit with an error if the HTTP status is one of `3xx`, `4xx`, or `5xx`, and the exit status is `3` (unless `--follow` is set), `4`, or `5`, respectively. That's the difference between a script that notices a failed request and one that "succeeds" against an error body. Pair it with `-qq` to silence warnings while keeping error exits.

## --ignore-stdin: the hang every script hits

This one cost me a CI run. Outside an interactive session (cron, CI, GitHub Actions), `stdin` is not a terminal, so httpie assumes the input will contain the request body and waits for it — and since there is neither any input data nor an end-of-file signal, httpie gets stuck. The fix is to always pass `--ignore-stdin` in scripts unless you're actually piping a body.

## Verify

```bash
http --offline GET https://example.com/api                   # preview, nothing sent
http --check-status --ignore-stdin GET https://example.com/api  # exit 0 on 200
http --check-status GET https://example.com/api/definitely-nope  # exit 4 on 404
```

The third one is the one that surprised me: a plain call exits 0, `--check-status` turns it into a gated failure.

## What I'd verify next

Persistent session reuse across repeated calls (so auth and cookies don't have to be re-sent on every request in a batch) is the piece I haven't sorted out yet. I don't want to write those specifics up until I've verified them against the docs, so that's next on the list.