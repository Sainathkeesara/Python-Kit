# Glossary

## pre-commit
- **Hook** — A script or command that runs before a commit is finalized, defined in `.pre-commit-config.yaml`.
- **Repo** — In pre-commit, a source repository that provides hooks (e.g. `https://github.com/pre-commit/pre-commit-hooks`).
- **rev** — The tag or commit to pin a pre-commit hook source to.
- **ID** — The identifier of a specific hook within a pre-commit source repo.

## py (Ruff)
- **Linter** — Ruff's lint rules that detect code issues; configured under `[tool.ruff.lint]`.
- **Formatter** — Ruff's code formatter that rewrites files to a consistent style; configured under `[tool.ruff.format]`.
- **AST (Abstract Syntax Tree)** — The tree representation of source code that Ruff parses to apply lint and format rules.

## pyproject.toml
- **pyproject.toml** — The Python project configuration file (PEP 518 / PEP 621), used to declare build system, project metadata, and tool settings.
- **`[build-system]`** — Section declaring the build backend (e.g. setuptools, hatchling) and its requirements.
- **`[project]`** — Section for project metadata (name, version, dependencies, Python version requirement).

## pytest
- **assert** — Python's built-in assertion statement; pytest rewrites it to provide detailed failure messages.
- **fixture** — A pytest function that provides setup/teardown or test data, injected into test functions by parameter name.
- **parametrize** — A pytest decorator (`@pytest.mark.parametrize`) that runs a test function against multiple sets of arguments.
- **test discovery** — pytest's automatic collection of test functions (files matching `test_*.py`, functions named `test_*`).
- **xunit-style setup** — Module/class-level `setup_method` / `teardown_method` functions, inherited from the xUnit tradition.

## uv
- **uv** — A fast Python package and project manager (by Astral).
- **Virtual environment** — An isolated Python environment; uv can create and manage these without a separate `virtualenv` tool.
- **`uv sync`** — Command that synchronises the project environment with the lock file.
- **`uv add`** — Command that adds a dependency to `pyproject.toml` and updates the lock file.
- **`uv lock`** — Command that generates or updates the lock file without installing packages.
- **`uv run`** — Command that runs a script or command in the project's virtual environment.
- **`uv tool`** — Command for managing globally installed tools (equivalent to `pipx`).
- **`uv pip`** — Pip-compatible interface for users migrating from pip.
- **`uv python`** — Command for managing Python versions.
- **dev-dependencies** — Dependencies marked for development only; they are installed but not included in the published package metadata.

## uv.lock
- **Lockfile** — A file that pins exact versions of every direct and transitive dependency, ensuring reproducible installs.
- **Resolution** — The process of selecting compatible versions of all dependencies that satisfy the project's requirements.
- **Transitive dependency** — A dependency of a direct dependency (indirect dependency).
- **`[[package]]` section** — TOML array entry in `uv.lock` describing a single resolved package.
- **`[metadata]` section** — The top-level metadata block in `uv.lock` containing the resolver version and install strategy.
