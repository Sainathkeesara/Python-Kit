---
last_verified: 2026-09-05
tool_version: n/a
---

# pyproject.toml tool tables for uv, Ruff, pytest, and mypy

> Pattern reference for consolidating per-tool configuration into pyproject.toml within a src-layout package.

## Purpose

In a src-layout Python package, configuration tends to scatter across `.coveragerc`, `mypy.ini`, `ruff.toml`, `pytest.ini`, and `tox.ini`. pyproject.toml centralizes these under `[tool.*]` tables, giving you one file that editors, CI, and contributors can discover. This note documents the pattern for uv, Ruff, pytest, and mypy.

## When to use

- You are migrating from a flat layout or a setup.cfg-based project.
- You want a single config file that tools like uv, ruff, and mypy can all read.
- Your package uses a `src/` directory (e.g., `src/my_package/`).

## Prerequisites

- A Python package with a `src/<package>/` layout.
- pyproject.toml already contains `[build-system]` and `[project]` tables.
- uv, ruff, pytest, and mypy installed in your environment.

## Steps

1. **Add `[tool.uv]`.** Declare the package and any development dependencies so `uv sync` installs the full dev set.

2. **Add `[tool.ruff]`.** Place lint and format rules here. Include `line-length`, `select`, and `ignore` lists.

3. **Add `[tool.pytest.ini_options]`.** Point `testpaths` at `tests/` and set `pythonpath` to include `src/`.

4. **Add `[tool.mypy]`.** Set `python_version`, `strict`, and `files` or `exclude` patterns to match the src layout.

5. **Verify each tool reads the table.** Run `uv run ruff check .`, `uv run pytest`, and `uv run mypy src/`. If a tool ignores pyproject.toml, check that it is installed at a version that supports the table layout.

## Example

```toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "A src-layout package with unified tool config"
requires-python = ">=3.11"
dependencies = []

[tool.uv]
package = true
dev-dependencies = ["pytest", "ruff"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
target-version = "py311"
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
ignore = ["E501"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.mypy]
python_version = "3.11"
strict = true
warn_unused_configs = true
files = ["src/my_package"]
```

## Verify

- `uv run ruff check .` reports zero violations.
- `uv run pytest` discovers and runs tests from `tests/`.
- `uv run mypy src/` reports zero type errors (or only expected ones from untyped dependencies).
- `uv sync` installs the dev dependencies declared in `[tool.uv]`.
- Running `cat pyproject.toml | grep '\[tool\.'` shows tables for uv, ruff, pytest, and mypy.

## Common errors

- **Mypy ignores pyproject.toml.** Older mypy versions read `mypy.ini` or `setup.cfg` exclusively. Upgrade to a version that supports `[tool.mypy]`.
- **Pytest does not find tests.** Without `pythonpath = ["src"]`, pytest may fail to import the package under test.
- **Ruff reports "unknown key".** The `[tool.ruff]` schema evolves. If you see unknown-key warnings, pin Ruff to a recent version.
