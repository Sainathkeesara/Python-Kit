# Exploring uv CLI commands beyond the basics

I've used `uv sync`, `uv add`, and `uv run` enough to be comfortable. Today I poked around some of the other commands.

## `uv lock`

Turns out `uv sync` calls this internally, but running `uv lock` standalone just generates/updates `uv.lock` without installing anything. Handy for CI when I only need the resolved lockfile.

## `uv export`

This one surprised me — it dumps the current lockfile as a `requirements.txt`:

```bash
uv export --format requirements-txt > requirements.txt
```

I guess this is for tools that don't read `uv.lock` yet. The output is flat, with hashes if you pass `--hashes`.

## `uv build`

Builds my project into `dist/` (sdist + wheel). I tried it on a tiny project with a `pyproject.toml` and it Just Worked. Feels like `python -m build` but faster.

## `uv cache`

- `uv cache prune` — cleans old cache entries
- `uv cache dir` — prints cache path

I ran `uv cache dir` and found it's at `~/.cache/uv/`. `prune` freed about 40 MB. Not bad.

## `uv self update`

Updates uv itself. I ran it and went from 0.5.x to 0.6.x. No manual download needed.

## What I'd try next

I want to look at `uv publish` for uploading packages, and maybe `uv tool` for managing CLI tools installed via uv. The `uv tree` command also sounds useful for seeing the actual dependency tree instead of just the flat lockfile.
