---
last_verified: 2026-07-19
tool_version: n/a
sources: []
---

# Followed the httpie quickstart — what worked and what tripped me up

I sat down with the official httpie quickstart to go beyond the basic requests I'd tried before. Here's what I did, what caught me off guard, and what I'd look into next.

## Steps I followed

### 1. Basic GET and checking status

The quickstart starts with a simple GET. I ran `http https://jsonplaceholder.typicode.com/posts/1` and saw the colored JSON output — that part was straightforward.

Then I tried `https://jsonplaceholder.typicode.com/posts` without the `/1` and the response was hundreds of lines. I realized the quickstart wasn't going to teach me about pagination, so I just noted it and moved on.

I found `--check-status` on my own reading the help output. It makes httpie exit non-zero when the server returns an error (4xx or 5xx). Without it, httpie always exits 0 and prints the error body. That matters if I ever put this in a script.

### 2. POST with JSON data

The quickstart shows `http POST https://example.com/api/users name=john email=john@example.com`. httpie turns key=value pairs into a JSON body automatically. That's convenient — no need to write `Content-Type: application/json` by hand.

I tried it against JSONPlaceholder:

```bash
http POST https://jsonplaceholder.typicode.com/posts title=foo body=bar userId=1
```

It returned the created resource with id 101. The automatic JSON encoding worked exactly as advertised.

### 3. Sending raw JSON

The quickstart also covers piping raw JSON with `--raw`:

```bash
http POST https://jsonplaceholder.typicode.com/posts --raw '{"title": "raw", "body": "test", "userId": 2}'
```

This is useful when you have JSON from another source and don't want to convert it to key=value pairs.

### 4. Custom headers

I added a custom header with `name:value` syntax:

```bash
http GET https://jsonplaceholder.typicode.com/posts/1 Authorization:token-fake-123
```

httpie strips these from the body display — they only show with `--verbose` or `-v`.

## Got stuck on

- **Scheme default got me again.** I typed `http jsonplaceholder.typicode.com/posts/1` and got a redirect because httpie defaults to `http://` not `https://`. The quickstart examples all include `https://` explicitly, but when I tried to save typing I forgot. Always include the scheme.
- **`--check-status` and piped output.** If you pipe httpie output to `jq` and use `--check-status`, a 4xx response still prints the error body (so `jq` sees invalid JSON and fails). The exit code is non-zero, but you also get a `jq` parse error. Not a bug, just confusing the first time.
- **The quickstart is short.** I finished the whole thing in about 15 minutes. It's a good orientation but doesn't cover things like file uploads, sessions, or authentication. For those I'll need the more detailed docs.

## What I'd try next

I want to explore httpie's session feature for authenticated API workflows, and try building a small script that chains several authenticated requests together. I also want to compare httpie's `--verify` option against curl's `-k` for working with self-signed certs in development.
