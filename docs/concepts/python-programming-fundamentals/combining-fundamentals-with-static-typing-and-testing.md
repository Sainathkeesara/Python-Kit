---
last_verified: 2026-08-14
tool_version: n/a
sources:
  - https://mypy.readthedocs.io/en/stable/common_issues.html
  - https://calpaterson.com/mypy-hints.html
  - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
  - https://til.simonwillison.net/python/pyproject
---

# Combining Python fundamentals with static typing and tests

## Purpose

This is the integration point between three things the kit teaches separately: core Python (functions, data structures, exceptions), static typing with mypy, and testing with pytest. Rather than learning them in isolation, it shows how a small real project holds all three in one place — the type hints annotate the functions, the tests pin the behavior the type checker cannot see, and mypy is configured so adding a function without annotations stops being silent.

## When to use

- A script has grown past a single file and changing a function signature should not silently break a caller.
- The project is small enough that a separate `mypy.ini`, `setup.cfg`, and `pytest.ini` is heavier than a `[tool.*]` block in `pyproject.toml`.
- CI needs to run both gates (type check and tests) from one entry point before code lands.

## Prerequisites

- A Python 3.10+ interpreter — the lowercase generics and `X | Y` union syntax need it; on 3.8–3.9 use the `typing` module spellings.
- A `pyproject.toml` with `[project]` metadata and a `dev` dependency group that declares `mypy` and `pytest`.
- `uv sync` (or an equivalent install) that resolves the `dev` group into an environment.

## Steps

1. **Write the fundamentals first, untyped.** Get the shape of the module down as plain Python before the type checker enters the picture: a custom exception for a guard condition, and a function that folds a list of dictionaries into a lookup.

   ```python
   class ConfigError(Exception):
       """Raised when package config is malformed."""


   def load_packages(packages):
       if not packages:
           raise ConfigError("no packages listed")
       return {p["name"]: p.get("version", "unknown") for p in packages}
   ```

2. **Add type hints where the checker can see them.** Annotate the public signature. This is where the gap appears: functions without annotations are not checked by mypy, so a `def` that returns the wrong type passes with zero errors. Annotate the public surface, or turn on `check_untyped_defs` so the bodies of unannotated functions still get checked.

   ```python
   from typing import TypedDict


   class Package(TypedDict):
       name: str
       version: str


   def load_packages(packages: list[Package]) -> dict[str, str]:
       if not packages:
           raise ConfigError("no packages listed")
       return {p["name"]: p.get("version", "unknown") for p in packages}
   ```

3. **Probe inference with `reveal_type`.** When a type does not resolve as expected, `reveal_type(expr)` prints what mypy actually inferred — it is a mypy-only magic function and is not valid at runtime. A minimal `[tool.mypy]` block with `check_untyped_defs = true` makes the untyped-function gap loud the moment it lands.

   ```toml
   [tool.mypy]
   check_untyped_defs = true
   ```

4. **Write tests for the branches the checker cannot see.** The type checker cannot prove `load_packages([])` raises, so a `pytest.raises` test guards that path. Parametrize the edge cases (missing `version` key, empty list) so each branch that type narrowing cannot fully cover is pinned by a test that would otherwise fail.

   ```python
   import pytest


   def test_load_packages_missing_version_defaults_unknown():
       pkgs = [{"name": "mypy", "version": ""}]
       assert load_packages(pkgs) == {"mypy": "unknown"}


   def test_load_packages_empty_raises():
       with pytest.raises(ConfigError):
           load_packages([])
   ```

5. **Converge on `pyproject.toml`.** This is the single file where metadata (`[project]`), the type-checking policy (`[tool.mypy]`), the test configuration, and the dependency groups (`[dependency-groups]`) all live together — the place where fundamentals, static typing, and dependency management stop being three separate tutorials.

   ```toml
   [tool.pytest.ini_options]
   testpaths = ["tests"]

   [dependency-groups]
   dev = ["mypy", "pytest"]
   ```

## Verify

- `mypy .` reports zero errors on the annotated module.
- `pytest -q` exits `0`, and both the empty-list and missing-version cases are covered.
- `uv run mypy . && uv run pytest` runs both gates from one command, matching what CI will do.

## Common errors

- **Annotations added, but still invisible.** A typed function called from an unannotated caller can still flow through as `Any` — the gap is the untyped caller, not the typed callee. `check_untyped_defs` closes that gap.
- **Tests that only cover the happy path.** `load_packages([])` raising `ConfigError` is a control-flow branch the type checker cannot see; without the `pytest.raises` test it rots unnoticed.

## References

- https://mypy.readthedocs.io/en/stable/common_issues.html
- https://calpaterson.com/mypy-hints.html
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- https://til.simonwillison.net/python/pyproject
