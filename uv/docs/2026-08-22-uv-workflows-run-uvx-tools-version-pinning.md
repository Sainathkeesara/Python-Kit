---
last_verified: 2026-08-22
tool_version: n/a
sources:
  - https://docs.astral.sh/uv/guides/tools/
  - https://docs.astral.sh/uv/guides/projects/
---

# uv workflows: uv run, uvx, tool management, and Python version pinning

This doc covers the day-to-day uv workflows I use most: running code in a managed environment, running CLI tools without installing them, and pinning Python versions for reproducibility.

## uv run — running commands in the project environment

`uv run` executes a command inside the project's virtual environment without requiring manual activation. It creates the venv if it doesn't exist, installs dependencies from `pyproject.toml` + `uv.lock`, and then runs the command.

```bash
# Run a Python script in the project environment
uv run python my_script.py

# Run a module
uv run python -m pytest

# Run a CLI tool installed as a project dependency
uv run ruff check .
```

The key behavior: `uv run` always ensures the environment is synced before executing. This means you don't need to remember `uv sync` first — if the lockfile or pyproject.toml changed, `uv run` handles it. It's the closest thing to "just run the code" in a managed Python project.

One thing to watch: `uv run` looks for a `pyproject.toml` in the current directory or parents. If you're in a subdirectory without one, it won't find the project environment. Run from the project root.

## uvx — running tools without installing

`uvx` runs a Python CLI tool in an isolated temporary environment. Think of it as `npx` for Python — useful when you want to try a tool or run it once without adding it to your project.

```bash
# Run ruff without installing it in the project
uvx ruff check .

# Run a specific version of a tool
uvx httpie@3.2.4 GET https://httpbin.org/get

# Run a tool that's already installed as a project dep — uvx still works
uvx pytest --co -q
```

`uvx` caches tool installations, so subsequent runs are fast. The tool runs in isolation from your project's dependencies, which prevents version conflicts. This is especially handy for linting or auditing tools you don't want polluting your dependency tree.

The difference between `uvx` and `uv run`:
- `uvx` = isolated tool, no project context
- `uv run` = project environment, synced dependencies

Use `uvx` for one-off tools. Use `uv run` for project scripts and tools declared in `pyproject.toml`.

## Tool management — uv tool install/upgrade/list

For tools you use regularly across projects, `uv tool install` makes them available system-wide (or user-wide) without polluting any project's virtual environment.

```bash
# Install a tool globally
uv tool install ruff

# Install a specific version
uv tool install mypy@2.3.1

# List installed tools
uv tool list

# Upgrade a tool
uv tool upgrade ruff

# Uninstall
uv tool uninstall ruff
```

Tool installations live in `~/.local/share/uv/tools/` (on Linux) and are completely separate from any project's `.venv`. This is the recommended way to install CLI tools like `ruff`, `mypy`, `black`, or `httpie` — they don't interfere with project dependencies.

A practical pattern: install your core linting/checking tools with `uv tool install`, then use `uv run` for project-specific tools declared in `pyproject.toml`. This keeps your global tools consistent while letting each project pin its own versions.

## Python version pinning

uv offers three layers of Python version control, from most to least specific:

**1. `requires-python` in pyproject.toml** — declares the minimum Python version for the project. This is enforced at install time.

```toml
[project]
requires-python = ">=3.11"
```

**2. `.python-version` file** — tells uv which Python version to use when creating venvs or running tools. Put this in your project root.

```
3.11
```

**3. `uv python pin`** — pins a Python version for the current directory, creating or updating `.python-version`.

```bash
# Pin Python 3.11 for this project
uv python pin 3.11

# Check what's pinned
cat .python-version
```

The interaction: when you run `uv venv` or `uv run`, uv looks for `.python-version` first, then falls back to the Python available on PATH. `requires-python` is a constraint (what versions are allowed); `.python-version` is a preference (which specific version to use).

```bash
# Install a specific Python version if not already available
uv python install 3.11

# Then pin it for the project
uv python pin 3.11

# Now uv venv and uv run will use 3.11
uv venv .venv
uv run python --version  # Python 3.11.x
```

For CI, the most reliable pattern is: install the exact Python version with `uv python install`, then let `uv run` pick it up from `.python-version` or the default. This avoids depending on whatever Python version the CI image happens to ship.

## How these pieces fit together

A typical project workflow:

```bash
# 1. Clone and enter the repo
git clone https://github.com/user/project && cd project

# 2. Pin Python (if not already in .python-version)
uv python pin 3.11

# 3. Install Python if needed
uv python install 3.11

# 4. Create venv and install deps
uv sync

# 5. Run project scripts
uv run python -m mypackage.cli

# 6. Run tools declared in pyproject.toml
uv run ruff check .
uv run pytest

# 7. Run tools not in pyproject.toml
uvx pip-audit -r requirements.txt
```

The core idea: `uv run` is your default way to execute anything in the project. `uvx` is for tools outside the project. `uv tool install` is for tools you want globally. And `.python-version` + `requires-python` handle version pinning at different granularities.
