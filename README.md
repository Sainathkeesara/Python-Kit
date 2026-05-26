# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, pre-commit, pyproject.toml, uv.lock.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-22-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, pre-commit, pyproject.toml conventions, and uv.lock. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets |
|------|-------|---------|---------|----------|
| uv | 3 | 1 | 1 | 1 |
| uv.lock | 2 | 1 | — | — |
| py (Ruff / tooling) | 2 | 1 | 1 | — |
| pyproject.toml | 2 | — | 1 | — |
| pytest | 1 | — | — | 1 |
| pre-commit | 1 | — | — | — |

## Quick links

- [pre-commit primer](pre-commit/notes/0000-primer-pre-commit.md) — First-contact notes for pre-commit hooks
- [uv pyproject.toml config](uv/configs/2026-05-26-uv-pyproject-settings.toml) — Configure uv settings inside pyproject.toml
- [uv CLI beyond basics](uv/notes/2026-05-26-cli-commands-beyond-basics.md) — Exploring uv CLI commands beyond the basics
- [uv.lock structure](uv.lock/notes/2026-05-26-uv-lock-structure.md) — Inside the lock file — understanding its structure
- [Generate uv.lock](uv.lock/scripts/generate-uv-lock.sh) — Create a uv.lock file with uv sync

## Layout

| Directory | Contents |
|-----------|----------|
| `uv/` | Notes, scripts, configs, and snippets for Astral's uv |
| `uv.lock/` | Notes and scripts for understanding uv's lock file |
| `py/` | Ruff primer, config, and install/lint script |
| `pyproject.toml/` | Primer, minimal config, and settings notes |
| `pytest/` | CLI notes and a first test snippet |
| `pre-commit/` | Primer for pre-commit hooks |

## Status

Building out first-contact notes across the Python toolchain. Currently covering uv (most depth), then Ruff, pytest, pre-commit, pyproject.toml, and uv.lock.

---
_Last updated: 2026-05-26_
