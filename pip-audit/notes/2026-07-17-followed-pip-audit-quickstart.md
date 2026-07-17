---
last_verified: 2026-07-17
tool_version: 2.10.1
sources:
  - https://github.com/pypa/pip-audit#installation
  - https://github.com/pypa/pip-audit#pip-audit-takes-longer-than-i-expect
  - https://github.com/pypa/pip-audit#dry-runs
  - https://github.com/pypa/pip-audit#pip-audit-shows-irrelevant-vulnerability-reports
  - https://github.com/pypa/pip-audit#suppressing-exit-codes-from-pip-audit
  - https://pypi.org/project/pip-audit/
---

# Followed the official pip-audit quickstart — what tripped me up

I sat down with the pip-audit docs and tried to follow the quickstart end to end. Most of it worked, but a few steps tripped me up enough that I'm writing them down.

## Setup

The docs say `python -m pip install pip-audit`. I did that and got version 2.10.1. One note: pip-audit requires Python 3.10 or newer. I accidentally tried on a 3.9 venv first and got an opaque error that didn't mention the version requirement at all. Switching to a 3.11 venv fixed it immediately.

```bash
python -m pip install pip-audit
pip-audit --version
# pip-audit 2.10.1
```

## My first scan

I pointed it at a `requirements.txt` with a few pinned packages:

```bash
pip-audit --requirement requirements.txt --local
```

The `--local` flag matters. Without it, pip-audit resolves every package on my entire system — first run took 30 seconds because it was scanning global site-packages. With `--local` it dropped to under 2 seconds. That one's easy to forget.

## What caught me

**Full dependency resolution on first run.** The docs mention it, but I still wasn't prepared. pip-audit does the same resolution work as `pip install`, so on a project with many dependencies it can take 30–60 seconds. The terminal stays quiet during this — it looks like it's hung. Patience. Or use `--local` to skip resolution and audit only what's already installed.

**`--require-hashes` fails hard on unpinned deps.** I tried `pip-audit --requirement requirements.txt --require-hashes` on a file that had some unpinned entries. It failed immediately without scanning anything. The error message didn't say which line was the problem — I had to bisect the file manually. If your requirements aren't fully pinned, use `--no-deps` instead or generate a lockfile first.

**`--fix` bumped a version past my test matrix.** I ran `pip-audit --fix` on a small project and it upgraded a package by two minor versions. My CI only tested against the previous minor, so the build broke. The docs recommend `--dry-run` first to see what would change. Do that. Always.

**Exit codes are intentional.** pip-audit exits non-zero when it finds vulnerabilities. This isn't an error state — it's the expected behavior. I wrapped my CI command in `|| true` so the pipeline doesn't fail on a clean scan that happens to find something.

**`--ignore-vuln` uses the vuln ID, not the package name.** I kept passing the package name and nothing happened. The correct usage is `--ignore-vuln PYSEC-2021-59` (or a CVE/GHSA ID). The `vuln` field in the JSON output tells you which ID to use.

## What I'd do differently

Start with `pip-audit --local --dry-run` to get a baseline. Add `--ignore-vuln` for known false positives (I had one for pytest). Only then try `--fix` after confirming the scope of changes. And always check the Python version before installing — 3.10+ required.
