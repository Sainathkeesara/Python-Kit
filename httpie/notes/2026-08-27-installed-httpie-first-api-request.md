---
last_verified: 2026-08-27
tool_version: "3.2.4"
sources:
  - https://pypi.org/project/httpie/
  - https://httpie.io/docs/cli/usage
---

# First API request with httpie

> Install httpie, run my first request, and figure out why `name=value` and `name:=value` behave differently.

## What I did

Installed httpie with `pip install httpie` and ran a quick GET against api.example.com:

```bash
http GET https://api.example.com/users user=alice
```

That worked, but then I tried a POST with a raw number and got confused:

```bash
http POST https://api.example.com/users count:=5
```

## What tripped me up

The `=` vs `:=` difference. `name=value` sends a JSON-quoted string. `name:=value` sends the raw value without quotes. So `count:=5` becomes a number, while `count=5` becomes the string `"5"`.

I also expected fields before the URL to always be headers, but on GET requests they become query parameters instead. Headers need the `:` prefix, like `X-API-Key:abc123`.

## Tiny example that worked

```bash
http GET https://api.example.com/users user=alice status:=200
```

## What I'll cover next

I want to try sessions next so I don't re-type auth flags on every call, then move on to `--check-status` for CI gating.
