# pip-audit findings — first scan

I ran pip-audit on my project's requirements.txt today. Here's what happened.

## Setup

Activated my venv and installed pip-audit:

```bash
pip install pip-audit
```

## Scan

Pointed it at the requirements file:

```bash
pip-audit --requirement requirements.txt --local
```

## Results

Empty output — no vulnerabilities found. All my current dependencies are clean according to the advisory database. I checked a couple of the pinned versions manually on PyPI and confirmed they're recent releases.

## What I noticed

- The scan is fast — under 2 seconds for 15 packages.
- The `--local` flag is important in a venv, otherwise it scans global site-packages too.
- I should set this up in CI so it runs on every PR.
- Next time I'll try `pip-audit --fix` to see what happens when a vulnerability is actually found.
