---
last_verified: 2026-08-29
tool_version: "1.9.4"
sources:
  - https://pypi.org/project/bandit/
  - https://bandit.readthedocs.io/en/latest/start.html
---

# bandit — quick primer

> First-day notes for someone who's never used bandit. Personal voice, plain language.

## What is it?

bandit is a Python tool that scans your source code for common security issues — things like hardcoded passwords, SQL injection risks, use of insecure functions like `exec()`, and weak cryptographic configurations. It's basically a static analysis linter, but specifically tuned for security instead of style. If you've ever run `ruff` or `flake8` and gotten style warnings, bandit does the same thing but for vulnerability patterns. It reads your `.py` files, parses the AST, and flags anything that matches known bad patterns.

## What does it do?

bandit runs a suite of built-in "tests" (security checks) against your Python codebase. Each test looks for a specific anti-pattern — for example, B101 catches `assert` statements (stripped under `-O`), B102 catches `exec()` usage, B601 catches shell injection via `os.system()` with formatted strings. You point it at a directory, it scans, and it spits out a report with test IDs, severity, confidence, and the offending line. You can filter by test ID, exclude directories, output as JSON or text, and compare against a baseline to track new findings over time.

## Why does it exist?

Before bandit, Python teams doing security reviews had to either manually audit code or cobble together custom AST scripts to catch dangerous patterns. That's slow, error-prone, and doesn't scale. bandit gives you a repeatable, automated first pass. It's especially useful in CI pipelines — run it on every PR, fail if new high-severity issues pop up. The tool was originally developed by OpenStack's security team and is now maintained by PyCQA. Day to day, I'd use it alongside `ruff` (for style) and `mypy` (for types) as part of a three-linter stack that catches different categories of problems.

## Key terminology

- **Test ID** — A unique identifier for each security check, like B101 (assert), B102 (exec), B601 (shell injection). Example: `bandit -s B101` skips the assert check.
- **Profile** — A named group of tests organized by category, like `ShellInjection` or `Crypto`. Example: `bandit -p ShellInjection` runs only shell-injection-related tests.
- **Severity** — How bad the finding is: LOW, MEDIUM, or HIGH. Example: hardcoded password = HIGH severity.
- **Confidence** — How sure bandit is that this is a real issue: LOW, MEDIUM, or HIGH. Example: `os.system()` with a format string = HIGH confidence shell injection.
- **Baseline** — A JSON file capturing known findings so subsequent runs only report new issues. Example: `bandit -b baseline.json -r .` shows only findings not in the baseline.
- **Exclude paths** — Directories or files to skip during scanning, passed with `-x`. Example: `bandit -r . -x tests,build`.
- **Output format** — How results are rendered: `txt` (default), `json`, `csv`, `html`, `sarif`. Example: `bandit -f json -o report.json -r .`.

## A tiny example

```bash
# Scan the current directory, skip tests
bandit -r . -x tests

# Scan and output JSON
bandit -r . -f json -o report.json

# Skip a specific test
bandit -r . -s B101

# Generate a baseline
bandit -f json -o baseline.json -r .

# Compare against baseline
bandit -b baseline.json -r .
```

The first command scans everything under the current directory except `tests/`, printing any findings to stdout. The `-r` flag means recursive. I ran it on a small Flask app and it immediately caught an `os.system()` call I'd forgotten about.

## What I'll cover next

Next I want to try running bandit against a deliberately vulnerable file to see the different test IDs in action — maybe a script with `exec()`, hardcoded secrets, and a shell injection. After that I'll look at integrating it into a pre-commit hook and a CI workflow.
