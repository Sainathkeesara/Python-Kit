# uv — quick primer

> First-day notes for someone who's never used uv. Personal voice, plain language.

## What is it?

I just learned about uv, and honestly, it's the thing I wish I'd had all along. uv is a Python package and project manager written in Rust by the folks at Astral (same company that makes Ruff). If you've used `pip` + `virtualenv` + maybe `pip-tools` or `poetry`, uv replaces a bunch of those with a single binary. It's fast — like, noticeably fast — because it's compiled instead of interpreted.

Comparing it to something I already know: uv is to Python packaging what `cargo` is to Rust — a single tool that handles the virtual environment, the dependencies, and the project scaffolding.

## What does it do?

uv installs Python packages, creates virtual environments, syncs dependencies from a `pyproject.toml` or `requirements.txt`, and generates a lockfile (`uv.lock`). It can also manage Python versions themselves with `uv python install`. The CLI is designed so `pip install` becomes `uv pip install` — you don't have to learn a whole new mental model to start using it.

## Why does it exist?

Before uv, the Python packaging workflow was a pile of separate tools glued together. `pip` for installing, `virtualenv` (or `venv`) for environments, `pip-compile` for lockfiles, `pip-sync` to match environments. Each would slow down as your project grew. uv exists to bundle all that into one fast, well-tested tool and to make the "it works on my machine" problem less painful. Day to day, I'd guess it's most used by Python devs who are tired of waiting for `pip install` and want a single toolchain instead of five.

## Key terminology

- **Virtual environment** — an isolated directory that holds a specific Python interpreter and its installed packages. uv creates one with `uv venv`. Example: `uv venv .venv` creates a folder called `.venv` in your project root.
- **Lockfile** — a file (`uv.lock`) that pins exact versions of every dependency (and sub-dependency) so everyone on the team gets the same environment. Example: `uv sync` reads `pyproject.toml` and generates/updates `uv.lock`.
- **PyPI** — the Python Package Index, the default source where uv looks for packages. Example: `uv add requests` downloads `requests` from PyPI.
- **uv add** — adds a package to your `pyproject.toml` and installs it. Example: `uv add flask` adds `flask` to your project dependencies.
- **uv sync** — installs everything listed in `pyproject.toml` using the lockfile. Example: `uv sync` is the first thing I run after cloning a repo.
- **uv pip** — a compatibility interface that mimics `pip` commands. Example: `uv pip install torch` works like `pip install torch` but faster.
- **uv python** — manages Python interpreter versions. Example: `uv python install 3.12` downloads and installs Python 3.12 if it's not already on your system.
- **uv tool** — manages CLI tools installed via Python (like `black`, `ruff`, `mypy`) without polluting your global environment. Example: `uv tool install ruff` makes `ruff` available system-wide.

## A tiny example

```bash
# Create a new project directory
mkdir my_project && cd my_project

# Create a virtual environment
uv venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Add a dependency
uv add requests
```

This creates a virtual environment inside `.venv`, installs `requests` (and writes it to `pyproject.toml` + `uv.lock`), and leaves you ready to `import requests` in your code.

## What I'll cover next

After this primer, I want to actually install uv, run some real commands, and see the speed difference for myself. Then I'll try creating a virtual environment and managing dependencies with `uv add` / `uv sync` to get a feel for the workflow.
