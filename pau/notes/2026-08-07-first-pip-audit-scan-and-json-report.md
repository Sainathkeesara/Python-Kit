---
last_verified: 2026-08-07
tool_version: n/a
---
# First pip-audit scan — what the JSON report looks like

I made a tiny requirements.txt with two packages and pointed pip-audit at it just to see what the output looks like.

## The scan

```text
requests==2.31.0
flask==3.0.0
```

Ran:

```bash
pip-audit --requirement requirements.txt --local --format json
```

## What the JSON report looks like

The `--format json` flag outputs a list of objects. Each object has `package` (name and version), `vuln` (the advisory ID), and `fix` (the patched version). If there are no vulnerabilities, the list is empty.

The structure surprised me — I expected a dict keyed by package name, but it's a flat list. To look up a specific package, I have to loop through and match on `package.name`.

## What I'll try next

I want to pass the JSON through `jq` to filter by severity, then try parsing it in Python to build a small report script.
