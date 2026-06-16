# Installed pre-commit and ran it with linting and type check

I set up a sample repo to test pre-commit with both Ruff (lint) and mypy (type check) hooks.

## What I did

Installed pre-commit with `pip install pre-commit`. Created a `.pre-commit-config.yaml` with two hooks:

- **ruff** — lints Python files
- **mypy** — type checks, with `types-requests` as an extra dep

Ran `pre-commit install` to wire it into git hooks. Then `pre-commit run --all-files` to test all files in one shot.

## What happened

Ruff caught a few unused imports and a line-too-long in my test script. mypy flagged a function call where I passed a string instead of an int. Both were fast — under a second total.

What tripped me up: `pre-commit install` by default only hooks into `git commit`. Running `pre-commit run` without `--all-files` only checks changed (unstaged) files, which is confusing the first time. `--all-files` is what I wanted.

## What I'd try next

I want to add more hooks — `end-of-file-fixer`, `trailing-whitespace`, maybe `check-yaml`. Also want to try the `--from-ref` and `--to-ref` flags for CI integration.
