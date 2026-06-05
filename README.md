# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, mypy, pre-commit, rich, typer, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-86-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), py-spy (profiler), tox (test automation), httpie (API testing), ty (alternative type checker), uv.lock, and pyproject conventions. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets | Docs |
|------|-------|---------|---------|----------|------|
| uv | 4 | 2 | 1 | 1 | 1 |
| uv.lock | 2 | 2 | — | — | — |
| mypy | 4 | 1 | 1 | 1 | — |
| pip-audit | 2 | 2 | 1 | — | — |
| pipdeptree | 3 | 1 | — | — | — |
| pre-commit | 2 | 1 | 2 | 1 | — |
| py (Ruff tooling) | 2 | 1 | 1 | — | — |
| pyproject.toml | 2 | — | 2 | — | — |
| py-spy | 2 | 1 | — | — | — |
| pytest | 2 | 1 | — | 1 | 1 |
| rich | 5 | 1 | — | 4 | — |
| ruff | 1 | — | 1 | — | 1 |
| tox | 2 | — | 1 | — | — |
| ty | 2 | — | 2 | 1 | — |
| typer | 2 | 2 | — | — | — |
| httpie | 2 | 1 | — | — | — |

## Quick links

- [uv vs pip cheat-sheet](uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md) — Command mapping and migration cheat-sheet
- [Ruff-only pre-commit config](pre-commit/configs/tried-first-ruff-hooks-config.yaml) — Minimal pre-commit config with just the ruff hook
- [Typer calculator script](typer/scripts/tried-typer-calculator.py) — Minimal Typer CLI calculator: add, sub, mul, div
- [uv.lock reproducibility test](uv.lock/scripts/tried-uv-lock-reproducibility.sh) — Test that uv.lock checksums are stable across lock commands
- [Multi-tool pyproject.toml config](pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config

## Layout

| Directory | Contents |
|-----------|----------|
| `00_index/` | Navigation: quick-links.md, topics.md, glossary.md |
| `uv/` | Notes, scripts, configs, and snippets for Astral's uv |
| `py/` | Ruff and related Python tooling notes, scripts, configs |
| `pytest/` | pytest testing framework notes and snippets |
| `pyproject.toml/` | pyproject.toml configuration notes and examples |
| `uv.lock/` | uv.lock lock file notes and scripts |
| `pre-commit/` | Hook configs: snippets/, notes/, scripts/ |
| `pip-audit/` | Vulnerability scanning notes and scripts |
| `pipdeptree/` | Dependency tree notes and scripts |
| `mypy/` | Type checking notes and test scripts |
| `rich/` | Terminal output notes, scripts, and snippets |
| `ruff/` | Linter/formatter notes, configs, and comparisons |
| `ty/` | Type checker comparison notes and configs |
| `typer/` | CLI framework notes and demos |
| `py-spy/` | Profiler notes and scripts for py-spy |
| `httpie/` | API testing CLI notes, scripts, and configs |
| `tox/` | Test automation notes and configs for tox |
| `docs/` | Project-level documentation (repository-structure.md) |

See [docs/repository-structure.md](docs/repository-structure.md) for full details.

## Status

Building out first-contact notes across the Python toolchain. Recent additions cover ty quickstart, uv vs pip cheat-sheet, ruff-only pre-commit hook config, typer calculator demo, and uv.lock reproducibility testing. Actively working through notes for uv, pytest, and rich.

---
_Last updated: 2026-06-05_
