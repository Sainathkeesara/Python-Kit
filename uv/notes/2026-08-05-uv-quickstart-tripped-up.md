---
last_verified: 2026-08-05
tool_version: n/a
---

# Tried the uv quickstart — what tripped me up

I followed the official uv quickstart today. I already had uv installed, so I jumped straight into project mode.

## What happened

I ran `uv init quickstart-demo` and it created a directory with `pyproject.toml`, `README.md`, and a `src/quickstart_demo/` package dir. No virtualenv yet — I had to run `uv venv` separately to get one.

Then I added deps with `uv add requests rich`. Both appeared in `[project.dependencies]` and `uv.lock` was generated automatically.

I wrote a small script that used `requests` and `rich` to fetch and pretty-print the GitHub API root. Ran it with `uv run python main.py` and it worked on the first try.

## What tripped me up

- `uv init` doesn't create a venv. I kept wondering why `uv run` wasn't available until I ran `uv venv` manually.
- After `uv add`, running `uv sync` said "nothing to do" — because `uv add` already syncs. I didn't need to run it again.
- The `src/` layout with a package dir is fine, but I had to figure out the import path for my own scripts inside it.

## What I'd try next

I want to try `uv remove`, `uv sync` from a clean clone, and `uv export` to get a `requirements.txt` for CI pipelines that don't have uv.
