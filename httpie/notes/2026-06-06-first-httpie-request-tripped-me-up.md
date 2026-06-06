# First httpie request — what tripped me up

I installed httpie with pipx, then tried my first request:

```bash
http https://jsonplaceholder.typicode.com/posts/1
```

It worked but I kept tripping on little things:

- I typed `http get https://...` — nope. `http` is already GET by default. You only write the verb when it's not GET (like `http POST`).
- `http -h` only shows headers in the response, not the body. I wanted `-v` / `--verbose` to see both request and response headers.
- If you leave off the scheme, httpie adds `http://`, not `https://`. I typed `http jsonplaceholder.typicode.com/posts/1` and got a 301 redirect before I noticed.
- The colored JSON output is nice but I kept thinking it was a pager (like `less`). It's not — it just prints with syntax highlighting and exits.

Also tried `http https://jsonplaceholder.typicode.com/posts` — the list output was truncated. Found `--pretty=all` forces full pretty-print even on long responses.

`http --offline POST https://example.com/api hello=world` was useful for building requests without actually sending them.
