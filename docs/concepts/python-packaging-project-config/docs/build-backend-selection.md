---
last_verified: 2026-08-23
tool_version: n/a
sources:
  - https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026
  - https://docs.astral.sh/uv/concepts/build-backend/
  - https://pydevtools.com/handbook/tutorial/setting-up-testing-with-pytest-and-uv/
  - https://andrewodendaal.com/python-packaging-2026-uv-poetry-modern-ecosystem/
  - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
---

# Choosing a build backend for Python packaging

## Purpose

The `[build-system]` table in `pyproject.toml` selects the library that turns source into a distributable package (wheel or sdist). The three backends covered here — setuptools, hatchling, and uv_build — each make different trade-offs between flexibility, configuration overhead, and ecosystem integration. Choosing the right one determines how `venv`, `uv sync`, mypy, and pytest interact with the installed artifact.

## When to use each backend

**setuptools** remains the default for libraries that need namespace packages, C-extension build scripts, or backward compatibility with an existing `setup.cfg`. setuptools 77.0.3 and later read PEP 621 metadata from `[project]` natively, so a separate `setup.py` is only needed for custom build steps. The backend string is `setuptools.build_meta`.

**hatchling** is the modern alternative for pure-Python projects that want zero-config packaging. hatchling 1.26 and later require only `[build-system] requires = ["hatchling"]` plus the standard `[project]` table — no `setup.py` or `setup.cfg`. It validates metadata at build time and is the backend used by the PyPA sample project and the Prefect migration pattern documented at softaims.com.

**uv_build** is the native uv backend for pure-Python src-layout packages. It requires `requires = ["uv_build>=0.12.5,<0.13"]` with `build-backend = "uv_build"`. The upper bound is necessary because the backend follows the same versioning policy as uv. uv_build only supports pure-Python code; projects with C-extension build steps must use setuptools or hatchling. During `uv build`, the uv executable bundles a copy of uv_build automatically. Other frontends (e.g. `python -m build`) fetch the `uv_build` package from PyPI independently.

## Prerequisites

- Python 3.11 or later (matching the `requires-python` floor in `[project]`).
- The `build` package (`pip install build`) if building via `python -m build`, or uv if building via `uv build`.
- The chosen backend declared in `[build-system] requires` and `build-backend`.

## Backend wiring

Each backend is wired through the same two-field pattern in `pyproject.toml`:

```toml
[build-system]
requires = ["<backend>"]
build-backend = "<backend>.<entry-point>"
```

The `requires` list is the build isolation environment — pip and uv install these packages into a temporary environment before invoking the backend, so they do not need to be in the project's runtime dependencies. The `build-backend` string must match the entry point exported by the package named in `requires`. A mismatch (e.g. `requires = ["hatchling"]` with `build-backend = "setuptools.build_meta"`) produces a "backend not found" error at build time.

## Interaction with venv and typing configs

The backend choice does not change how the virtual environment is created, but it does affect what gets installed into it. With a src layout (`src/<package>/`), `uv sync` installs the package in editable mode, making `import mypackage` resolve to the installed artifact rather than the working directory. This catches packaging bugs — missing data files, incorrect package-data declarations — before they ship.

The src layout is especially important when running pytest: a flat layout lets `pytest` import raw source from `.`, so tests pass even if the wheel is broken. Switching to src layout closes that gap, but only if `[tool.pytest.ini_options] testpaths` and `pythonpath` match the layout.

For type checking, `[tool.mypy]` lives in the same `pyproject.toml` as the packaging metadata. The `python_version` field in `[tool.mypy]` should match the `requires-python` floor declared in `[project]` so that mypy's type narrowing matches the runtime interpreter. In CI, `uv sync --frozen` provides the exact environment mypy type-checks against — the packaging config and the type-checking config share one install step.

uv_build exposes a `[tool.uv.build-backend]` section for package discovery overrides: `module-name` and `module-root` let you relocate the package away from the default `src/<package_name>/`, and `namespace = true` disables the safety check that prevents accidental namespace collisions. These settings are uv-specific; they are ignored by hatchling and setuptools.

## Verification steps

1. **Build the wheel.** Run `uv build` or `python -m build --wheel`. A clean build with no warnings confirms the backend is wired correctly.
2. **Inspect the wheel.** Wheels are zip files. Run `python -m zipfile -l dist/*.whl` to confirm the expected package code and metadata entries are present.
3. **Smoke-install into a fresh venv.** Create a new virtual environment (`python -m venv .venv-smoke && .venv-smoke/bin/pip install dist/*.whl`), activate it, and run `python -c "import mypackage; print(mypackage.__version__)"`. If the import succeeds and the version matches, the wheel is structurally sound.
4. **Run the test suite in the smoke venv.** `python -m pytest` inside the smoke venv confirms that the installed artifact — not the raw source tree — is what pytest exercises.

## Common errors

- **Backend string mismatch.** `requires = ["hatchling"]` must pair with `build-backend = "hatchling.build"`. Mixing them produces a "backend not found" error at build isolation time.
- **Missing src/__init__.py.** All three backends expect `src/<package>/__init__.py` to exist. If the file is missing, the build succeeds but the wheel is empty or the import fails after install.
- **`requires-python` vs. venv mismatch.** If `requires-python = ">=3.11"` but the venv was created with Python 3.10, `pip install` refuses to install the wheel with a version-conflict error.
- **uv_build pure-Python limitation.** Projects with C-extension build steps fail with uv_build. Switch to hatchling or setuptools for those projects.
- **`[tool.uv.build-backend]` ignored by other frontends.** This section is read only by uv. Building the same project with `python -m build` ignores it; module discovery falls back to the backend defaults.

## References

- https://docs.astral.sh/uv/concepts/build-backend/ — uv_build configuration, module discovery, and include/exclude semantics.
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ — PEP 517/518/621 backends and version requirements.
- https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026 — pyproject.toml as the single configuration hub.
- https://pydevtools.com/handbook/tutorial/setting-up-testing-with-pytest-and-uv/ — src layout, pytest, and packaging validation.
- https://andrewodendaal.com/python-packaging-2026-uv-poetry-modern-ecosystem/ — 2026 packaging ecosystem overview.
