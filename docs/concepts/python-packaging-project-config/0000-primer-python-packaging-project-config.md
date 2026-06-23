# Python Packaging & Project Config — quick primer

> First-day notes on Python Packaging & Project Config. What it is, why it matters, and the key ideas to know.

## What is it?

Python Packaging & Project Config is the system for describing a Python project so that tools know how to install it, build it, and run it. It lives mainly in a file called `pyproject.toml` (and historically `setup.py` or `setup.cfg`). This file tells the world: what the project is called, what version it is, what dependencies it needs, and how to build it into a distributable package. I think of it like a recipe card — anyone with the card can reproduce the same result.

## Why does it matter for Python?

Every Python project I work with needs some form of packaging info. When I use uv to add a dependency, it writes to pyproject.toml. When I run pytest, it reads test settings from pyproject.toml. When I install a tool with pip, it uses the packaging metadata to resolve which version to install. Without understanding packaging basics, I'd find myself guessing at what all those config fields mean and why my lockfile contains certain packages.

## Key terminology

- **pyproject.toml** — The standard config file for Python projects, defined by PEP 518 and PEP 621. Example: contains a `[project]` table with `name`, `version`, and `dependencies`
- **PEP 621** — The standard that defines how to put project metadata directly in pyproject.toml under a `[project]` table. Example: `[project] name = "my-app" version = "0.1.0"`
- **Build backend** — The library that builds your package into a distribution (setuptools, hatchling, flit_core, pdm-backend). Example: `[build-system] requires = ["hatchling"] build-backend = "hatchling.build"`
- **Dependencies** — Other packages your project needs at runtime. Example: `dependencies = ["requests>=2.28", "click>=8.0"]`
- **Lockfile** — A file that pins exact versions of every dependency and transitive dependency. Example: uv.lock records version, source URL, checksum, and Python markers for each package
- **Virtual environment** — An isolated directory with its own Python interpreter and package set. Example: `.venv/` created by `uv venv`
- **SDist (source distribution)** — A compressed archive of source code that can be built and installed. Example: `mypackage-1.0.tar.gz`
- **Wheel** — A pre-built distribution format that installs faster than SDist. Example: `mypackage-1.0-py3-none-any.whl`
- **Entry point** — A function exposed as a CLI command via the `[project.scripts]` table. Example: `cli = "my_package:main"`

## A concrete example

Here's the minimal pyproject.toml I wrote to understand packaging:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

This tells uv and pip what my project is called, what Python version it needs, what packages it depends on, and how to build it.

## How this connects to what's next

Understanding packaging is the foundation for using uv (dependency management), uv.lock (reproducible installs), and pip-audit (vulnerability scanning). Next I'll practice how these tools read and write pyproject.toml, and how the lockfile ensures everyone on my team gets identical dependencies.
