---
last_verified: 2026-07-26
tool_version: "2.10.1"
sources:
  - https://pypi.org/project/pip-audit/
---

# pip-audit — quick primer

> First-day notes for someone who's never used pip-audit. Personal voice, plain language.

## What is it?

pip-audit is a command-line tool from the Python Packaging Authority (PyPA) that scans the Python packages installed in your environment for known security vulnerabilities. When I first heard the name, I assumed it was some kind of audit log for pip commands, but it's actually much more concrete: it checks your dependency tree against the Python Packaging Advisory Database and tells you if any installed version has a published flaw.

## What does it do?

You run `pip-audit` in a project directory (or point it at a requirements file with `-r`) and it prints out every package that has a known vulnerability, along with the advisory identifier and the version where it was fixed. If everything is clean, it exits silently. You can also pass `--fix` to let it upgrade those packages in place, or `--ignore-vuln <id>` to silence a specific advisory you've already accepted.

## Why does it exist?

Before pip-audit, the main way to check for vulnerable packages was to manually search CVE databases or hope your CI happened to catch it. pip-audit automates that cross-reference and ties it directly to the environment your code actually runs in. It exists because "it works on my machine" is not a security posture — a transitive dependency can have a disclosed advisory and you'd never notice unless something specifically flagged it. It's the kind of check I wish I'd run before I deployed that tiny internal script.

The tool also nudges me toward better dependency hygiene. When it flags something, I'm forced to look at my pinned versions and think about whether I need a lockfile. That conversation doesn't happen if there's no scanner in the loop.

## Key terminology

- **Vulnerability** — A known security flaw in a specific package version. Advisory databases assign identifiers like PYSEC, CVE, or GHSA. Example: an older version of a common library with a disclosed flaw.
- **Advisory** — The published record of a vulnerability, usually with a recommended fixed version. Example: pip-audit reports an advisory and suggests upgrading to a patched version.
- **`--fix`** — Automatically upgrades vulnerable packages in place without prompting. Example: `pip-audit --fix` bumps packages to patched versions.
- **`--locked`** — Audits a `pyproject.toml` or `pylock.toml` lockfile directly without needing a live environment. Added in version 2.7.
- **`--ignore-vuln <id>`** — Skips a specific advisory by identifier. Example: `pip-audit --ignore-vuln <advisory-id>` silences a known false-positive for one package.
- **`pip list`** — Flat list of installed packages and versions, with no security context. Example: `pip list` tells you what you have; pip-audit tells you whether any of it is rotten.

## A tiny example

```bash
pip install pip-audit
pip-audit
```

This installs pip-audit and scans the current environment. If there are no vulnerabilities, it exits with no output. If it finds one, it prints the package name, installed version, advisory ID, and the version that fixes it.

## What I'll cover next

I want to run pip-audit on an actual project and see what it reports, then try the `--locked` flag against a `pyproject.toml` to understand the offline workflow. After that I'll figure out how to add it to a pre-commit or CI step so it runs automatically before I merge.
