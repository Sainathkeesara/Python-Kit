# Explored uv CLI — subcommands, help topics, and output formats

I hadn't really looked at all of uv's subcommands — I just used `sync`, `add`, `run`. Today I ran `uv --help` to see the full picture.

## Subcommands

There are more than I expected. The main ones I hadn't tried:

- `uv lock` — just generate the lockfile without installing. I thought sync did both.
- `uv export` — dump lockfile as `requirements.txt`. Surprised this isn't more prominent.
- `uv build` — builds sdist + wheel. Worked on my test project instantly.
- `uv publish` — uploads to PyPI. Haven't tried this yet.
- `uv cache` — manage the cache. `uv cache prune` freed ~40 MB on my machine.
- `uv self update` — updates uv itself. Ran it, went from 0.5.x to 0.6.x.
- `uv tool` — manage CLI tools installed via uv. Similar to `pipx`.

## Help topics

Some subcommands have their own detailed help. `uv run --help` has more flags than I realized: `--with`, `--frozen`, `--no-sync`, `--script`. `uv add --help` shows `--dev`, `--optional`, `--rev`, `--tag`.

## Output formats

By default everything is text. `uv export` supports `--format requirements-txt`. But most commands don't have a JSON flag that I could find. `uv tree` (if it exists) would probably show the dep tree — I'll check next.

What I'd try next: test `uv publish` on TestPyPI, and explore `uv tool` for managing CLI apps.
