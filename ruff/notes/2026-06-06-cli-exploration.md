# Ruff CLI exploration — flags and output formats

I ran the Ruff CLI to see what flags and output formats are available. Here's what I found.

## Main commands

Ruff has two primary commands:
- `ruff check` — runs the linter
- `ruff format` — runs the formatter

## Output formats

I tested `--output-format` with these options:
- `text` (default) — human-readable with colors
- `json` — machine-readable JSON array
- `concise` — minimal output, just file:line:col: code
- `grouped` — groups issues by file
- `junit` — JUnit XML for CI

```bash
ruff check messy_example.py --output-format json
```

This prints JSON to stdout, which I can parse if I want to build a report.

## Useful flags

- `--select E,F` — only check pycodestyle and pyflakes rules
- `--ignore N` — skip naming rules
- `--fix` — auto-fix issues (only works for safe fixes)
- `--unsafe-fixes` — apply fixes that might be unsafe
- `--diff` — show what would change without modifying files

## What tripped me up

- `--output-format` only works with `check`, not `format`
- `--fix` doesn't fix naming issues (`N` rules) — it says they're "unsafe" because renaming could break code
- `ruff format` has its own `--check` flag to show what would change

## What I'd try next

I want to wire Ruff into a pre-commit hook and try running it on a real project with many files.