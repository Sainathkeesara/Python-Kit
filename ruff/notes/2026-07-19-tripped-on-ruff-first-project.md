---
last_verified: 2026-07-19
tool_version: n/a
sources: []
---

# What tripped me up applying Ruff to my first project

I already ran the quickstart (single-file linting) but today I tried Ruff on an actual project with multiple files, a virtualenv, and existing code. Different world.

## Config location confusion

I created a `ruff.toml` in my project root and also had Ruff settings under `[tool.ruff]` in `pyproject.toml`. Ruff reads both, but I didn't know which one won. Turns out: `ruff.toml` is standalone, `[tool.ruff]` in pyproject.toml is inline — they don't merge the way I expected. I kept editing the wrong one.

## Running on a real project

`ruff check .` was overwhelming — hundreds of warnings from test directories, generated files, vendored libs. The quickstart used `ruff check single_file.py`, so I wasn't ready for the noise.

I added `exclude = [".venv", "build", "tests/fixtures"]` and used `--select E,F` to narrow down issues I actually wanted to fix first.

## Select vs Ignore — not what I expected

I set `select = ["E", "F"]` and `ignore = ["E501"]` thinking ignore would override. It doesn't — `select` defines the full rule set, and `ignore` only filters within it. `ignore = ["E501"]` worked because E501 is in the E group, but if I'd set `select = ["F"]`, no E or N rules would run at all. Took me a minute to figure out.

## Check then format, not the other way

I ran `ruff format` first, then `ruff check`. The formatter moved things around but left lint issues. I had to run `ruff check --fix` again afterward. The recommended order is check-first-then-format, but backwards felt natural.

## What I'd try next

Add Ruff to a pre-commit hook so I catch issues before committing, and try `--add-noqa` to baseline existing warnings in a legacy codebase.
