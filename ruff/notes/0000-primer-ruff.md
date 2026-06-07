# Ruff — quick primer

> First-day notes for someone who's never used Ruff. Personal voice, plain language.

## What is it?

Ruff is a Python linter and formatter written in Rust. Think of it as the tool that replaces both `flake8` (linting) and `black` (formatting), but runs 10-100x faster because it's compiled instead of interpreted. I'd compare it to ESLint in JavaScript — a single tool that finds style issues and can auto-fix them.

## What does it do?

You run `ruff check file.py` and it flags unused imports, undefined names, line-too-long, and 900+ other issues. Run `ruff format file.py` and it reformats your code to a consistent style. It integrates with `pyproject.toml` so your config lives alongside other tool settings, and it can run in pre-commit hooks to catch issues before commit.

## Why does it exist?

Before Ruff, Python linting meant chaining together flake8, isort, black, pydocstyle, and sometimes pyupgrade or autoflake. Each tool was its own slow Python script. Ruff exists to do all of this in one fast pass, making linting so quick you can run it on every save instead of just in CI. Day-to-day users are Python devs who want instant feedback on their code quality.

## Key terminology

- **Linting** — Finding code issues like bugs, style problems, or complexity. Example: `ruff check src/` finds all issues in the `src/` directory.
- **Formatting** — Reformatting code to a consistent style. Example: `ruff format src/` reformats all Python files in place.
- **Rules** — Named checks with codes like `E501` (line too long), `F401` (unused import). Example: `ruff rule F401` shows the documentation for unused imports.
- **Fix** — Automatically correcting issues. Example: `ruff check --fix .` applies safe auto-corrections.
- **pyproject.toml** — Config file where you set which rules to enable or ignore. Example: `ruff check --select E,F .` runs only pycodestyle and Pyflakes rules.

## A tiny example

```bash
ruff check --select F401 my_script.py
ruff format my_script.py
```

The first command finds unused imports in `my_script.py`, the second reformats it. If there are unused imports, Ruff leaves them — `F` rules don't auto-fix.

## What I'll cover next

I want to install Ruff with uv, run it on a real project, and compare its speed to flake8. Then I'll configure it in `pyproject.toml` and try the formatter on some badly-formatted code.