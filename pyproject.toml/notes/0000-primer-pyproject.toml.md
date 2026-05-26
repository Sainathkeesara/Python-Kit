# pyproject.toml — quick primer

> First-day notes for someone who's never used `pyproject.toml`. Personal voice, plain language.

## What is it?

`pyproject.toml` is a configuration file format for Python projects. It's a replacement for the old way of doing things — `setup.py`, `setup.cfg`, `requirements.txt`, `MANIFEST.in`, and sometimes even `tox.ini` or `.pylintrc` — all rolled into one TOML file that sits at the root of your project.

Think of it like `package.json` in the JavaScript world: one file that tells tools what your project is, what it depends on, and how it should be built or checked. Python's equivalent was scattered across half a dozen files; `pyproject.toml` consolidates them.

## What does it do?

It declares your project metadata (name, version, author), defines dependencies (both runtime and dev), configures build tools (like setuptools or hatchling), and stores settings for linters, formatters, type checkers, and test runners — all under standardized `[tool.*]` sections. Instead of one tool owning a custom config file, every tool reads from `pyproject.toml`.

## Why does it exist?

Before PEP 518 (2016) and PEP 621 (2020), Python packaging was messy. You'd write a `setup.py` (a Python file, not a declarative format), a `setup.cfg` (INI-style), a `requirements.txt` for pip, and separate configs for each tool. Each tool invented its own config file format and location. `pyproject.toml` standardised the entry point: one file, TOML syntax, and a `[tool.*]` namespace so every tool can coexist without naming conflicts.

Tools like `uv`, `Ruff`, `pytest`, `mypy`, and `black` all now allow (or require) configuration via `pyproject.toml`. It's become the single source of truth for a Python project's structure and tooling.

## Key terminology

- **`[build-system]`** — Declares what build backend (e.g. `setuptools`, `hatchling`, `flit_core`) and build requirements your project needs. Example: `requires = ["hatchling"]; build-backend = "hatchling.build"`.
- **`[project]`** — The core metadata: `name`, `version`, `description`, `authors`, `dependencies`, `optional-dependencies`. This is the PEP 621 standard. Example: `name = "my-cli"; version = "0.1.0"`.
- **`[tool.*]`** — Namespace sections for individual tools. Ruff reads `[tool.ruff]`, pytest reads `[tool.pytest.ini_options]`, mypy reads `[tool.mypy]`. Each tool owns its own section. Example: `[tool.ruff]; line-length = 88`.
- **`[dependency-groups]`** — uv-specific grouping for dev/optional dependencies. Like `[project.optional-dependencies]` but with a different namespace.
- **TOML** — "Tom's Obvious, Minimal Language". A config format with key-value pairs, tables (`[section]`), arrays, and inline tables. Designed to be easy to read and unambiguous to parse.

## A tiny example

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "hello-pyproject"
version = "0.1.0"
description = "A minimal Python project"
requires-python = ">=3.10"
dependencies = []

[tool.ruff]
line-length = 88
target-version = "py310"
```

This is a minimal config that tells Python: use hatchling to build this project, call it "hello-pyproject", target Python 3.10+, and configure Ruff to lint with an 88-character line limit. With this file in the project root, `uv sync`, `ruff check`, and `pip install -e .` all work without extra flags.

## What I'll cover next

I want to try adding optional dependency groups (dev tools like pytest), configuring pytest's CLI options under `[tool.pytest.ini_options]`, and experimenting with workspace-style configs when a repo has multiple packages. I also need to understand the difference between `[project.dependencies]` and uv's `[dependency-groups]` — the naming overlap has tripped me up.
