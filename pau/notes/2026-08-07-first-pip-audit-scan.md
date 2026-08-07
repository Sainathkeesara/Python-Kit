---
last_verified: 2026-08-07
tool_version: n/a
---

# First pip-audit scan on a tiny requirements file

> Scratch notes: installed pip-audit, scanned a one-line requirements.txt with JSON output, and learned what the report actually looks like.

## Setup

I activated a fresh venv and pulled pip-audit in:

```bash
pip install pip-audit
```

Then I made a tiny `requirements.txt` with a single pinned package and ran:

```bash
pip-audit --requirement requirements.txt --local --format json
```

The `--local` flag matters here — without it pip-audit scans the whole environment, and my first run sat there resolving global site-packages for half a minute before printing anything.

## Reading the JSON report

`--format json` prints a JSON **list**, not a map keyed by package name. Each element is a package that turned up something, and I loop over it (or pipe through `jq '.[] | select(.package==...)'`) instead of indexing by name.

Each finding bundles the package name, the installed version, and a list of advisories. The advisories each carry an id, a short description, a severity, and the version that fixes it — something like:

```json
[
  {
    "package": "<name>",
    "version": "<version>",
    "vulns": [
      {
        "id": "<advisory-id>",
        "description": "...",
        "severity": "<severity>",
        "fix": "<fixed-version>"
      }
    ]
  }
]
```

I didn't bother decoding every advisory — I just confirmed the shape, then let pip-audit's exit code do the talking.

## What caught me

pip-audit exits non-zero when it finds anything. That's the point for CI, but the first time I saw a non-zero exit on a scan that otherwise looked clean I thought the tool had errored. Here a non-zero code means "issues detected," not "it broke."

## What I'd try next

Run it without `--format json`, add `2>&1 | tee audit.log` to keep a log, and look at the ids only if I need to suppress something.
