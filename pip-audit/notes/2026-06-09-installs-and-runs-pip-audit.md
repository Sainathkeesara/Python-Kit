# pip-audit install and first run — what tripped me up

I installed pip-audit today and ran it on my project's requirements file. Here's what happened.

## Setup

pipdeptree works with `pip`, but uv is how this project manages packages, so I used that:

```bash
uv tool install pip-audit
```

## Scan

Ran it on the requirements file:

```bash
pip-audit --requirement requirements.txt --local
```

## What I noticed

- The `--local` flag is actually very important — without it, pip-audit scans everything on my system, not just the venv. First run took 30 seconds because it was looking at global site-packages. With `--local` it was under 2 seconds.
- The `--format json` flag works, but the output is a list of vulnerability objects, not keyed by package name. I kept trying to look up dicts by package key and got KeyErrors. It's a list of dicts, each with `package`, `vuln`, and `fix`. Loop over it or use jq.
- Empty output is not always clean — it can also mean pip-audit couldn't parse the file or the PyPI advisory database hasn't synced yet. Check with verbose mode if you think something's wrong.
- If you're on slow internet, the first run downloads the OSV advisory database. It's ~100MB and pip-audit prints nothing during download, so it looks hung. Be patient.
- `--ignore` is per-vuln-id, not per-package. Use the `vuln` string like `PYSEC-2021-59`, not the package name.
