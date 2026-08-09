---
last_verified: 2026-08-09
tool_version: n/a
sources: []
---

# Tried uv's script, venv, and lockfile workflow on a small CLI project

I wanted to see if uv could replace the `python -m venv` + `pip install` + `pip freeze` routine I've been using. I set up a tiny CLI tool — a script that takes a filename and prints its line count — and worked through the full uv workflow.

## What I did

Started with `uv init wordcount-cli`. It created `pyproject.toml`, a `README.md`, and a `src/wordcount_cli/` package dir. No venv was created, which surprised me at first.

I created a venv with `uv venv`. Then I added `typer` for the CLI: `uv add typer`. The dependency landed in `[project.dependencies]` in `pyproject.toml` and `uv.lock` appeared in the same command — I didn't need to run anything extra to generate the lockfile.

I wrote `src/wordcount_cli/main.py` with a `@app.command()` that reads a file and prints the count, then ran it with `uv run typer run src/wordcount_cli/main.py run myfile.txt`. It worked on the first try.

## What tripped me up

`uv init` doesn't create a venv — that's separate. I kept reaching for it before realizing the two-step pattern.

`uv add` already syncs. I ran `uv sync` immediately after `uv add` and got "nothing to do." The `add` command handles both writing the dep and resolving the lockfile in one shot.

`uv lock --frozen` validates the lockfile without changing anything. Useful when you want to confirm the lockfile matches `pyproject.toml` before committing, but I almost ran `uv lock` (without `--frozen`) by accident, which would have updated it.

## What I'd try next

I want to try `uv sync` from a fresh clone — no venv, no installed packages, just the lockfile — to confirm the environment reproduces cleanly. Also want to see `uv export` produce a `requirements.txt` for CI environments that don't have uv.
