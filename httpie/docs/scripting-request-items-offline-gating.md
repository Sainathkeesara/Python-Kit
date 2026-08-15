---
last_verified: 2026-08-15
tool_version: 3.2.4
sources:
  - https://httpie.io/docs/cli/scripting
  - https://httpie.io/docs/cli/example-use-cases
  - https://pypi.org/project/httpie/
---

# Scripting with httpie: request-item DSL, --offline, and session reuse

## Purpose
This doc covers three httpie features that make interactive and scripted API workflows reliable: the request-item DSL that follows the URL, `--offline` for request previews, and session reuse for repeated authenticated calls. These patterns are useful for CI smoke tests, batch provisioning, and any automation where auth headers must persist across multiple requests.

## When to use
Use request items when constructing non-trivial POST or PUT calls from the command line. Use `--offline` to validate request shape before sending it against a live endpoint or when writing examples for documentation. Use sessions when a script makes several calls to the same host and re-authenticating on every call is wasteful or fragile.

## Prerequisites
- httpie 3.2.4 installed (`pip install httpie`).
- A terminal that supports standard output redirection; use `--pretty=none` or `-b` when piping JSON to a file to avoid embedded ANSI color codes.

## Request-item DSL
Every httpie call is a URL followed by request items. Data fields specified as `key=value` become form fields or JSON body entries depending on the content-type header. The runtime enforces a hard rule: a body supplied through `stdin` cannot be combined with command-line data items. Attempting both produces the error "Request body ... and request data (key=value) cannot be mixed".

```bash
http POST https://example.com/api/users name=john age=30
```

## --offline
`--offline` builds the full request and prints it without sending anything. It implicitly activates `--print=HB`, so headers and body are visible. This is useful for validating a request against API docs before hitting a live endpoint, or for dry-running scripts in CI.

```bash
http --offline POST https://example.com/api/users name=john
```

## Session reuse
HTTPie persists cookies and auth headers in a session file so subsequent calls inherit them. The basic pattern is:

```bash
http --session=./session.json POST https://api.example.com/login username=alice password=secret
http --session=./session.json GET https://api.example.com/protected
```

The `./` prefix matters: without it, httpie stores the session under `~/.config/httpie/sessions/<host>/<name>.json` as a named session rather than in the working directory. Sessions are per-host; a session created for `api.example.com` does not carry cookies or auth headers to `api.test.com`.

A session file retains the exact headers and cookies from the responses it receives. After rotating an API token, the existing session file may still send the old `Authorization` header or stale cookies. In that case, delete the session JSON and re-authenticate.

## Verify
Run the following against `https://httpbin.org`:

```bash
# 1. Preview a request without sending it
http --offline GET https://httpbin.org/get

# 2. Create a session and reuse it for a second request
http --session=./demo-session.json POST https://httpbin.org/post field=value
http --session=./demo-session.json GET https://httpbin.org/get

# 3. Confirm the session file exists locally
ls -l ./demo-session.json
rm -f ./demo-session.json
```

The first command should print headers and a body but not contact the server. The second and third commands should return 200 with the session file present between them.

## Common errors
- **Mixed body sources:** piping JSON to `stdin` while also passing `key=value` items triggers a runtime error. Choose one input method per call.
- **Stale session state:** rotating an API token does not update the existing session file. The old `Authorization` header or stale cookies continue to be sent. Delete the session JSON and re-authenticate.
- **Missing `./` in session path:** omitting the relative-path prefix creates a named session under `~/.config/httpie/sessions/` instead of a local file. Cleanup becomes harder in CI.
