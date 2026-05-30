# HTTPie — quick primer

> First-day notes for someone who's never used HTTPie. Personal voice, plain language.

## What is it?

HTTPie (pronounced "aitch-tee-tee-pie") is a CLI HTTP client that makes API requests readable. Think `curl` but with syntax highlighting, structured JSON output, and a command syntax that reads more like natural language. It's what you reach for when you want to test an API endpoint without mentally parsing a wall of curl flags.

I'd compare it to curl the way I'd compare a GUI file manager to `ls`: both do the same thing, but one is optimized for humans to read and write on the fly.

## What does it do?

You type `http GET https://api.example.com/users` and it prints the response headers and body with syntax-colored JSON, formatted indentation, and response status in color (green for 2xx, yellow for 3xx, red for 4xx/5xx). It also handles POST/PUT/PATCH bodies gracefully — just pass key=value pairs on the command line and it auto-sends them as JSON.

## Why does it exist?

Curl is powerful but its ergonomics are from the late 90s. Every time I needed to test a JSON API with curl, I'd end up googling the exact `-H` `-d` `-X` incantation. HTTPie was built by Jakob Schnitzer in 2012 specifically because curl's API testing workflow was painful. The tagline says it all: "A CLI, cURL-like tool for humans."

People who reach for HTTPie day-to-day are backend developers, API designers, DevOps engineers, and anyone who frequently tests REST endpoints from the terminal.

## Key terminology

- **`http` command** — The main CLI entry point. Example: `http GET httpbin.org/json` sends a GET request.
- **Key=value syntax** — HTTPie's way of setting JSON body fields. Example: `http POST httpbin.org/post name=Jane age=30` sends `{"name": "Jane", "age": 30}`.
- **`--pretty`** — Controls output formatting (all, colors, format, none). Example: `http --pretty=format GET httpbin.org/json` strips colors but keeps indented JSON.
- **`--json` / `-j`** — Explicitly set `Accept` and `Content-Type` to `application/json`. Example: `http -j PUT httpbin.org/put name=Jane` (default for key=value, but explicit is clearer).
- **`--form` / `-f`** — Send data as form-encoded instead of JSON. Example: `http -f POST httpbin.org/post name=Jane`.
- **`--follow`** — Follow redirects. Example: `http --follow GET httpbit.ly/short-url`.
- **Session** — Persistent cookies and auth across requests. Example: `http --session=logged-in POST httpbin.org/post name=Jane`.
- **Download mode** — Stream response body to file with a progress bar. Example: `http --download GET example.com/file.zip`.

## A tiny example

```bash
http GET https://api.github.com/repos/httpie/httpie
```

This returns the HTTPie repo metadata as syntax-highlighted JSON. Headers appear first (colored by type), then the pretty-printed JSON body. One command, zero flags.

## What I'll cover next

I want to install HTTPie, run actual GET and POST requests against JSONPlaceholder, and then compare the same API call side-by-side with curl to see where the ergonomic win actually lands. After that I'll look at sessions and authentication patterns for working with real-world APIs.
