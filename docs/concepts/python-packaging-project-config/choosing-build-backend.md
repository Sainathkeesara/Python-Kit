---
last_verified: 2026-08-24
tool_version: n/a
---

# Choosing a Build Backend

## Purpose

This document compares the main build backends available for Python projects and explains how to wire the chosen backend into a `pyproject.toml` that also configures a virtual environment and static type checking.

## When to Use

- Starting a new Python project and deciding which build backend to standardize on.
- Migrating an existing project from `setup.py`/`setup.cfg` to `pyproject.toml`.
- Needing a backend that works well with modern tooling (uv, hatch, pdm) and static type checkers (mypy, pyright, ty).

## Prerequisites

- Python 3.9+ installed.
- Basic familiarity with `pyproject.toml` structure (PEP 518 / PEP 621).
- A virtual environment tool (uv, venv, or virtualenv) available.

## Backend Comparison

| Backend | Package | Best For | Trade-offs |
|---------|---------|----------|------------|
| setuptools | `setuptools.build_meta` | Maximum compatibility; legacy projects; complex extension modules | Verbose config; slower builds; dynamic metadata requires `setup.py` hooks |
| hatchling | `hatchling.build` | Modern projects; fast builds; declarative config; good uv/hatch integration | Newer, smaller community than setuptools; fewer edge-case workarounds |
| uv_build | `uv_build` | uv-native workflows; minimal config; fastest builds | Early stage; limited customization; tied to uv ecosystem |
| flit_core | `flit_core.buildapi` | Pure-Python packages; minimal config; no C extensions | No support for C extensions; less flexible for complex layouts |

## Wiring a Backend into pyproject.toml

### 1. Declare the Build System

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Replace `hatchling` with `setuptools` + `wheel`, `uv_build`, or `flit_core` as needed.

### 2. Define Project Metadata (PEP 621)

```toml
[project]
name = "my-package"
version = "0.1.0"
description = "Short description"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]
```

### 3. Configure the Virtual Environment (Tool-Specific)

For uv, the venv is managed outside `pyproject.toml` via `uv venv` and `uv sync`. For hatch/pdm, the environment is managed by the tool itself. No standard `[tool]` table exists for venv creation — use the tool's CLI.

### 4. Add Static Type Checking Config

For mypy:

```toml
[tool.mypy]
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

For pyright:

```toml
[tool.pyright]
typeCheckingMode = "basic"
```

For ty:

```toml
[tool.ty]
```

## Steps to Initialize a New Project

1. **Create the project structure** (src-layout recommended):

   ```
   my-project/
   ├── pyproject.toml
   ├── README.md
   └── src/
       └── my_package/
           └── __init__.py
   ```

2. **Write `pyproject.toml`** with the chosen backend, project metadata, and type-checker config.

3. **Create a virtual environment**:

   ```bash
   uv venv
   uv sync
   ```

   Or with the backend's native tool (e.g., `hatch env create` for hatchling).

4. **Install the package in editable mode** to verify the build works:

   ```bash
   uv pip install -e .
   ```

5. **Run the type checker** to verify typing config:

   ```bash
   uv run mypy src/
   # or: uv run pyright
   # or: uv run ty check
   ```

## Verify

- Build a wheel: `uv build --wheel` (or `python -m build --wheel`).
- Inspect the wheel contents: `unzip -l dist/*.whl`.
- Confirm the package imports in a fresh environment: `uv run python -c "import my_package"`.
- Run the type checker with no errors on the source tree.

## Common Errors

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `ModuleNotFoundError` after `pip install -e .` | Package not under `src/` or `pyproject.toml` missing `[tool.setuptools.packages.find]` | Use `src/` layout with `where = ["src"]` in `[tool.setuptools.packages.find]` |
| `mypy: Cannot find implementation or library stub` | Type checker not seeing the installed package | Run mypy from within the venv (`uv run mypy`) or set `MYPYPATH` |
| Build fails with `Backend '...' not found` | Backend package not in `build-system.requires` | Add the backend package (e.g., `hatchling`) to `requires` |
| Wheel missing entry points | `[project.scripts]` not defined or backend doesn't auto-discover | Ensure `[project.scripts]` is present; for setuptools, add `[tool.setuptools.packages.find]` |

## References

- PEP 518 — Specifying Minimum Build System Requirements for Python Projects
- PEP 621 — Storing Project Metadata in pyproject.toml
- Python Packaging User Guide: Choosing a Build Backend
