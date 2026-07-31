---
last_verified: 2026-07-31
tool_version: n/a
---
# Ruff — quick primer

> First-day notes for someone who's never used Ruff. Personal voice, plain language.

## What is it?

I just started looking at Ruff. It's a Python linter and formatter written in Rust that replaces older tools like Flake8, Black, and isort. Where I used to chain each one separately, Ruff bundles checks into a single fast binary. It's my first stop in Python projects because it feels like upgrading from a pocket knife to a multi-tool.

## What does it do?

I run `ruff check` to scan for style issues and undefined names. `ruff format` rewrites files to match a consistent style. It can also sort imports and fix issues. Config lives in `pyproject.toml` under `[tool.ruff]` or a standalone `ruff.toml`.

## Why does it exist?

Python linting used to mean stacking tools with their own config files. I'd wait for Flake8, then isort. Ruff compiles rules into native code, so scans finish instantly. The appeal is collapsing setup into something I can run without noticing the lag.

## Key terminology

- **rule** — one specific check, like "no trailing whitespace"
- **select / ignore** — choose which rules to enable or disable
- **lint** — report issues without changing files
- **format** — rewrite files to match style rules
- **fix** — auto-correct an issue in place
- **config** — settings for rules and behavior

## A tiny example

```toml
[tool.ruff.lint]
select = ["E", "F", "I"]
ignore = ["E501"]
```

I put that in `pyproject.toml` and ran `ruff check .`. It flagged an unused import and a missing newline. `ruff check --fix .` cleaned both up without touching the source.

## What I'll cover next

I want to learn custom rules, pre-commit hooks, and migrating from Black + isort.
