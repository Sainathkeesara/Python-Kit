---
last_verified: 2026-08-22
tool_version: n/a
sources:
  - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
---

# What tripped me up writing pyproject.toml

I spent way too long mixing up which section of pyproject.toml does what. Here's what caught me out, so you don't repeat my mistakes.

## build-system vs [project] — they're not the same thing

The first thing I got wrong: I thought `[build-system]` and `[project]` were redundant. They're not.

`[build-system]` tells the build tool (pip, uv, whatever) *how* to build your package. It lists the build backend and its requirements. `[project]` tells the build tool *what* you're building — the name, version, description, dependencies.

You need both for a publishable package. But here's the gotcha: `[build-system]` alone with a `setup.cfg` is enough for a local editable install. So if you see a project without `[project]`, it doesn't mean it's broken — it might just be using the older setup.cfg path.

## The build-backend string is easy to get wrong

I copy-pasted `build-backend = "hatchling.build"` into a project that was using `setuptools`. The error message was cryptic — something about the backend not being found. The fix: if your `requires` lists `hatchling`, your `build-backend` must be `"hatchling.build"`. If it lists `setuptools`, it's `"setuptools.build_meta"`. Don't mix them.

## requires-python is stricter than I expected

I wrote `requires-python = ">=3.10"` thinking it was just metadata. It's not — pip and uv actually enforce it. If someone on Python 3.9 tries to install your package, it fails. That's the point, but I didn't realize it was enforced at install time, not just advisory.

## optional-dependencies vs dependency-groups

I kept reaching for `[project.optional-dependencies]` for dev tools, which works but has a specific semantic: those extras are *optional for the user*. `[dependency-groups]` (a uv-specific extension) is for tools *you* use during development. The distinction matters if you publish — extras show up in `pip install myproject[dev]`, dependency groups don't.

## Tool sections are just namespaces

`[tool.ruff]`, `[tool.mypy]`, `[tool.pytest.ini_options]` — these are all just TOML namespaces. The tool reads its own section and ignores the rest. The gotcha is that some tools use nested keys (`[tool.ruff.lint]`) while others use flat keys (`[tool.mypy]`). There's no universal pattern — you have to check each tool's docs.

## What I'd do differently

Start with a minimal `[build-system]` + `[project]` and add `[tool]` sections one at a time as you actually configure each tool. Don't try to set up everything at once — that's how you end up with a 200-line pyproject.toml where half the config is wrong.
