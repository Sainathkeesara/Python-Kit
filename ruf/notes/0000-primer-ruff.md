---
last_verified: 2026-08-03
tool_version: n/a
---

# Ruff — quick primer

> First-day notes for someone who's never used Ruff. Personal voice, plain language.

## What is it?

I just learned about Ruff, and it's already the Python linting tool everyone keeps recommending. Ruff is an extremely fast Python linter and code formatter written in Rust by Astral — the same company behind uv and Ty. It replaces a pile of older Python tools with a single binary that runs noticeably faster. If you've ever used `flake8`, `pylint`, `isort`, `pydocstyle`, or even `Black`, Ruff covers most of what those do, all in one command.

Comparing it to something I already know: Ruff is to Python linting what `cargo check` is to Rust — a single, fast tool that surfaces problems before they bite you in CI.

## What does it do?

Ruff has two main jobs. First, it lints your code: runs a huge set of rules to catch unused imports, undefined names, unused variables, bad naming conventions, and potential bugs. Second, it formats your code: applies consistent quoting, sorts imports, and wraps long lines — similar to what `Black` does. You can use either mode alone or both together.

The big selling point is speed. Because it's compiled to native code instead of being a Python script, `ruff check` and `ruff format` complete in milliseconds even on large codebases.

## Why does it exist?

Before Ruff, Python linting was a patchwork of slow, separate tools. `flake8` handled style and error checks, `isort` sorted your imports, `pydocstyle` enforced docstring conventions, and `Black` formatted code. Each tool had its own config format, its own install time, and its own warm-up cost. Running all of them in a pre-commit hook could take 10+ seconds for a small change. Ruff exists to collapse all that into one tool with one config file and a single invocation. Day to day, it's used by Python devs who want fast feedback in their editor and CI without managing seven different dependencies.

## Key terminology

- **Lint rule** — an individual check Ruff runs against your code. Each rule has a code like `F401` (unused import) or `E501` (line too long). Example: running `ruff check` on a file with an unused `import os` triggers rule `F401`.
- **ruff (the binary)** — the compiled Rust executable you invoke from the terminal. Example: `ruff check myfile.py`.
- **ruff check** — the subcommand that runs lint rules and reports violations. Example: `ruff check .` scans every Python file in the current directory.
- **ruff format** — the subcommand that automatically reformats code for consistent style. Example: `ruff format src/` reformats all files in `src/`.
- **ruff.toml** — the configuration file where you enable/disable rules, set line length, and list files to ignore. Example: a `ruff.toml` with `line-length = 100` and `select = ["E", "F"]`.
- **select** — a flag that picks which rule categories or codes to run. Example: `ruff check --select F` runs only the PyFlakes rules.
- **fix** — a flag that tells Ruff to automatically correct simple violations. Example: `ruff check --fix` removes unused imports without manual editing.

## A tiny example

```bash
# Install Ruff
pip install ruff

# Check a file for issues
ruff check my_script.py

# Auto-fix what it can (like unused imports)
ruff check --fix my_script.py

# Format code in-place
ruff format my_script.py
```

This scans `my_script.py` for lint violations, fixes the ones Ruff knows how to handle automatically, then reformats the file to match the default style.

## What I'll cover next

After this primer, I want to create a `ruff.toml` with a small set of rules I actually care about, then figure out how to wire Ruff into a pre-commit hook so it runs before every commit. I'd also like to explore the difference between `ruff check` and `ruff format` so I know when to use which.
