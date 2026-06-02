# Tried the uv quickstart — scaffold, deps, run

I followed the official uv quickstart today. I already had uv installed from the primer, so I jumped straight into project mode.

## Scaffolding a project

Ran `uv init quickstart-demo` — it created a directory with `pyproject.toml`, `README.md`, and `src/quickstart_demo/__init__.py`. No virtualenv yet, just a project skeleton.

I noticed it didn't create a `.venv` automatically. Had to run `uv venv` to get one. That surprised me — I expected `init` to set up the env too.

## Adding deps

`uv add requests` added the dep to `pyproject.toml` and generated `uv.lock` in one step. The output showed exactly what it was doing: resolving, downloading, installing. It was fast — under 2 seconds.

Then I added `rich` and `click` with one command: `uv add rich click`. Both appeared in the `[project.dependencies]` section of `pyproject.toml`.

## Running something

I wrote a tiny script in `src/quickstart_demo/main.py`:

```python
import requests
from rich import print

r = requests.get("https://api.github.com")
print(f"Status: [bold green]{r.status_code}[/bold green]")
```

Ran it with `uv run python src/quickstart_demo/main.py`. It worked. The `uv run` part is nice — it activates the venv implicitly so I don't have to remember to `source .venv/bin/activate`.

## What tripped me up

- `uv init` doesn't create a venv. I spent a minute wondering why `uv run` wasn't available until I ran `uv venv` separately.
- I tried `uv sync` after `uv add` and it said "nothing to do" — because `uv add` already syncs. Redundant.
- The generated `src/` layout with `src/quickstart_demo/` package dir is fine but I'd rather have a flat `main.py`. I had to figure out the import path for my own script.

## What I'd try next

I want to try `uv remove`, `uv sync` from a clean clone, and maybe `uv export` to get a `requirements.txt` for CI pipelines that don't have uv.
