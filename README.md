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

| Tool | Notes | Scripts | Configs | Snippets |
|------|-------|---------|---------|----------|
| uv | 4 | 2 | 1 | 1 |
| uv.lock | 2 | 1 | — | — |
| py (Ruff / tooling) | 3 | 1 | 2 | — |
| pyproject.toml | 2 | — | 1 | — |
| pytest | 1 | 1 | — | 1 |
| pre-commit | 2 | 1 | — | 1 |
| pip-audit | 2 | 2 | 1 | — |
| pipdeptree | 3 | 1 | — | — |
| mypy | 4 | 1 | 1 | 1 |
| rich | 4 | 1 | — | 2 |
| ty | 3 | — | 2 | 1 |
| typer | 2 | 1 | — | — |
| py-spy | 2 | 1 | — | — |
| httpie | 2 | 1 | — | — |
| tox | 2 | — | 1 | — |

## Quick links

- [ruff linter settings](ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [uv quickstart scaffold notes](uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow
- [mypy type error detection snippet](mypy/snippets/tried-mypy-type-errors.py) — Intentional type errors for mypy to catch
- [pytest parametrized tests script](pytest/scripts/test_parametrized.py) — Parametrized tests with @pytest.mark.parametrize
- [hello world with dependency script](uv/scripts/hello-with-dep.py) — PEP 723 inline metadata, uv run with requests

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
