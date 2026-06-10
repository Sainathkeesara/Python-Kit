# 2026-06-10-first-httpie-request

First day with HTTPie. Installed it with `brew install httpie` (wasn't sure if uv could install CLI tools directly, so I just used brew honestly). Ran `http --version` to make sure it was there.

## GET with JSON

Ran `http GET https://jsonplaceholder.typicode.com/posts/1` and the output was colored with green status, headers in cyan, and pretty indented JSON. Way easier to read than curl. I tried piping to `jq` but I didn't even need to — the default formatting is solid.

## POST with form data

For a POST with form data I used `http --form POST https://jsonplaceholder.typicode.com/posts title=hello body=world`. The `--form` flag made it send as `application/x-www-form-urlencoded`. I got back a JSON response with an id of 101, which I assume means it was stored somewhere temporarily even though JSONPlaceholder doesn't actually persist.

## What tripped me up

I tried `http POST https://jsonplaceholder.typicode.com/posts title=hello body=world` without `--form` first, and HTTPie auto-sent it as JSON instead. Took me a minute to realize the content-type mismatch was on me, not the server. Also `--form` is abbreviated as `-f` but I kept accidentally thinking "force" like curl's `-f`.

## Next

I want to try sessions next — keeping cookies around instead of passing headers every time. And headers. I forgot those entirely on my first run.
