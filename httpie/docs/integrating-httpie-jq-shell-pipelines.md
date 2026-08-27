---
last_verified: 2026-08-27
tool_version: n/a
---

# Integrating httpie with jq and shell pipelines

## Purpose

HTTPie outputs JSON by default, which makes it a natural fit for Unix pipelines. This doc covers the patterns that turn a one-off `http` call into a composable stage: feeding request bodies from pipes or files, extracting fields from responses with `jq`, and chaining multiple API calls together in a single shell expression. These patterns are useful in CI smoke tests, local debugging sessions, and any workflow where one API's output becomes the next's input.

## When to use

Use pipe-and-jq patterns when a script needs to transform an API response before passing it downstream — for example, pulling an auth token from a login endpoint and feeding it into a subsequent request. Prefer this over hardcoding values or writing a full Python script when the transformation is a simple field extraction or filter. Reach for a proper scripting language instead when the logic involves retries, complex error handling, or more than a few chained calls.

## Prerequisites

- httpie installed and available on `PATH`.
- `jq` installed for JSON parsing.
- A terminal that supports standard pipes; use `--pretty=none` or `-b` when piping httpie output to another program to avoid embedded ANSI color codes.

## Feeding request bodies from pipes

HTTPie reads a request body from `stdin` when no data items are provided on the command line. This lets another program supply the payload:

```bash
# Generate a payload with jq, pipe it into httpie
jq -n '{name: "alice", role: "admin"}' | http POST https://api.example.com/users
```

The body source is exclusive: once httpie reads from `stdin`, you cannot also pass `key=value` items on the command line. Mixing the two triggers a runtime error. Choose one input method per call.

A common variant reads the body from a file:

```bash
http PUT https://api.example.com/users/42 < updated-profile.json
```

This is useful when the payload is large or already serialized on disk.

## Parsing responses with jq

Pipe httpie's response body into `jq` to extract or transform fields:

```bash
# Extract a single field
http GET https://api.github.com/repos/httpie/cli | jq '.stargazers_count'

# Pull multiple fields
http GET https://api.github.com/repos/httpie/cli | jq '{stars: .stargazers_count, forks: .forks_count}'

# Filter a collection
http GET https://api.example.com/users | jq '.[] | select(.active == true) | .email'
```

Use `-b` (or `--pretty=none`) to suppress formatting when the output is destined for another program rather than a terminal:

```bash
http -b GET https://api.example.com/config | jq '.version'
```

## Chaining API calls

Capture an intermediate result with command substitution to feed it into the next call:

```bash
# Log in, extract the token, use it on the next request
TOKEN=$(http -b POST https://api.example.com/auth username=alice password=secret | jq -r '.token')
http GET https://api.example.com/profile "Authorization:Bearer $TOKEN"
```

The `-r` flag on `jq` outputs a raw string without quotes, which is what you want when the value becomes a header or URL segment.

## Exit codes in pipelines

By default, httpie exits `0` even on HTTP error statuses, which means a pipeline continues after a failed request. Use `--check-status` to make httpie exit non-zero on 4xx/5xx responses, so the pipeline short-circuits:

```bash
http --check-status --ignore-stdin GET https://api.example.com/health | jq '.status'
```

The `--ignore-stdin` flag prevents httpie from blocking on stdin input in non-interactive contexts like cron or CI, where no terminal is attached.

## Verify

Run the following against `https://httpbin.org` to confirm the patterns work end to end:

```bash
# 1. Feed a body from a pipe
jq -n '{hello: "world"}' | http -b POST https://httpbin.org/post | jq '.json.hello'

# 2. Chain: pull a value, use it downstream
VALUE=$(http -b GET 'https://httpbin.org/get?foo=bar' | jq -r '.args.foo')
echo "extracted: $VALUE"

# 3. Pipeline with --check-status
http --check-status --ignore-stdin -b GET https://httpbin.org/status/200 | jq -R '.'
```

The first command should print `"world"`. The second should print `extracted: bar`. The third should succeed silently; change the status to `500` and the command should exit non-zero.

## Common errors

- **Mixed body sources:** piping JSON to `stdin` while also passing `key=value` items triggers a runtime error. Choose one input method per call.
- **ANSI codes in piped output:** forgetting `-b` or `--pretty=none` embeds color escape sequences in the response body, which corrupts `jq` parsing. `jq` will report a parse error on the first line.
- **Missing `--ignore-stdin` in CI:** without it, httpie hangs waiting for body input when stdin is not a terminal. The process appears to freeze with no output.
- **Quoted strings from `jq`:** omitting `-r` on `jq` wraps string values in double quotes, which breaks header values and URL segments. The downstream call receives `"token"` instead of `token`.
