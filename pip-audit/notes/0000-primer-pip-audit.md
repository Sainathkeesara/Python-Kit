# pip-audit — quick primer

> First-day notes for someone who's never used pip-audit. Personal voice, plain language.

## What is it?

pip-audit is a CLI tool that scans Python dependencies for known security vulnerabilities. Think of it like `npm audit` for the Python ecosystem — it looks at your installed packages or a requirements file, checks each one against the Python Vulnerability Database (PyPI's advisory DB and the OSV database), and reports anything with a known CVE.

## What does it do?

It runs across your environment and tells you which packages have vulnerabilities, what the CVE IDs are, and what versions fix them. You can point it at a virtual environment, a `requirements.txt`, or even a pip-compile output. It exits with a non-zero code if it finds anything, so you can drop it in CI.

## Why does it exist?

Before pip-audit, checking Python dependencies for CVEs meant either using a SaaS platform like Snyk or Dependabot, or manually cross-referencing package versions against advisory databases. Neither scales to local development or offline use. pip-audit is free, works offline (with a local cache), and fits into a pre-commit hook or CI pipeline with one line.

## Key terminology

- **CVE** — A publicly disclosed security vulnerability with an ID like `CVE-2023-12345`. Example: pip-audit reports `CVE-2023-12345` for a package you have installed.
- **OSV** — Open Source Vulnerabilities database, the engine pip-audit uses under the hood. Example: pip-audit queries `osv.dev` for each package.
- **PYSEC** — The PyPI-specific advisory ID format, like `PYSEC-2023-100`. Example: shown alongside CVEs in pip-audit output.
- **`--requirement`** — Flag to point pip-audit at a file instead of scanning the current environment. Example: `pip-audit --requirement requirements.txt`.
- **`--local`** — Only scan the local environment, skip the global site-packages. Example: `pip-audit --local`.
- **`--fix`** — Experimental flag that can auto-upgrade vulnerable packages. Example: `pip-audit --fix`.

## A tiny example

```bash
pip install pip-audit
pip-audit
```

This installs pip-audit, then scans every package in the current Python environment and prints a table of any known vulnerabilities. If you run this in a fresh environment, the output is just an empty table — no news is good news.

## What I'll cover next

I want to run pip-audit against a real project with dependencies, see what a CVE report actually looks like, and try the `--fix` flag. Then I'll set it up in a pre-commit hook so every commit scans for vulnerabilities before it goes in.
