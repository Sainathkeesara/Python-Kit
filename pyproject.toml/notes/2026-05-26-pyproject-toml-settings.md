# pyproject.toml settings I've learned about

I made a minimal pyproject.toml today. Here's what the key sections do:

## `[build-system]`

This tells pip/uv what build backend to use. `requires` lists packages needed to build, `build-backend` is the actual builder. For a simple project, setuptools works fine.

## `[project]`

Core metadata — name, version, Python version requirement. I set `requires-python = ">=3.11"` to keep things modern. The name has to be valid for PyPI if I ever publish.

## Tool config sections (`[tool.*]`)

Haven't added these yet, but I know Ruff, mypy, and pytest all have their settings here under `[tool.ruff]`, `[tool.mypy]`, `[tool.pytest.ini_options]`. That's the nice thing about pyproject.toml — one file for everything instead of a dozen dotfiles.

Next I want to try adding `[tool.ruff]` config and see how it interacts with the rest of the project setup.
