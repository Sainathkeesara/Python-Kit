# HTTPie vs curl — same API calls, different ergonomics

I ran the same JSONPlaceholder requests with both HTTPie and curl to see where the differences actually matter.

## GET request

```bash
# curl
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq .

# httpie
http GET https://jsonplaceholder.typicode.com/posts/1
```

Curl gives me raw JSON — I need `jq` to format it. HTTPie colors and indents by default. For quick inspection, HTTPie wins hands down.

## POST with JSON body

```bash
# curl
curl -s -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "foo", "body": "bar", "userId": 1}'

# httpie
http POST https://jsonplaceholder.typicode.com/posts/ title=foo body=bar userId=1
```

The curl version makes me remember flags (`-X`, `-H`, `-d`) and hand-type JSON. HTTPie's `key=value` syntax sends JSON without quotes or braces. Less mental overhead.

## Where curl still wins

- **Scripting:** curl is installed everywhere by default; HTTPie is an extra dependency.
- **Downloading files:** curl's `-O` flag is simpler than HTTPie's `--download`.
- **Complex auth flows:** curl handles raw HTTP more transparently (NTLM, digest auth, raw cookie jars).

## Verdict

For ad-hoc API testing during development, I'll reach for HTTPie first. For scripts and CI pipelines, I'll stick with curl — no extra install needed.
