# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, mypy, pre-commit, rich, typer, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-51-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), ty (alternative type checker), pyproject.toml conventions, and uv.lock. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets |
|------|-------|---------|---------|----------|
| uv | 3 | 1 | 1 | 1 |
| uv.lock | 2 | 1 | — | — |
| py (Ruff / tooling) | 2 | 1 | 1 | — |
| pyproject.toml | 2 | — | 1 | — |
| pytest | 1 | — | — | 1 |
| pre-commit | 2 | 1 | — | 1 |
| pip-audit | 2 | 1 | 1 | — |
| pipdeptree | 2 | 1 | — | — |
| mypy | 3 | 1 | 1 | — |
| rich | 3 | 1 | — | 2 |
| ty | 2 | — | 1 | 1 |
| typer | 2 | 1 | — | — |
| py-spy | 2 | 1 | — | — |
| httpie | 2 | 1 | — | — |
| tox | 1 | — | 1 | — |

## Quick links

- [pipdeptree primer](pipdeptree/notes/0000-primer-pipdeptree.md) — First-contact notes for pipdeptree
- [pipdeptree JSON format](pipdeptree/notes/2026-05-29-format-json-deps.md) — Formatting output as JSON, identifying top-level vs transitive deps
- [typer primer](typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [typer quickstart notes](typer/notes/2026-05-29-typer-quickstart-notes.md) — What tripped me up following the quickstart
- [typer CLI demo](typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [rich primer](rich/notes/0000-primer-rich.md) — First-contact notes for rich (terminal output)
- [rich table/panel/progress script](rich/scripts/first-table-panel-progress.py) — Rich script with table, panel, and progress bar
- [httpie primer](httpie/notes/0000-primer-httpie.md) — First-contact notes for HTTPie
- [httpie vs curl](httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, different ergonomics

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
| `ty/` | Type checker comparison notes and configs |
| `typer/` | CLI framework notes and demos |
| `py-spy/` | Profiler notes and scripts for py-spy |
| `httpie/` | API testing CLI notes, scripts, and configs |
| `tox/` | Test automation notes and configs for tox |
| `docs/` | Project-level documentation (repository-structure.md) |

See [docs/repository-structure.md](docs/repository-structure.md) for full details.

## Status

Building out first-contact notes across the Python toolchain. Recent additions cover tox (test automation), httpie (API testing CLI) and py-spy (profiling). Currently working through L1 notes for tox.

---
_Last updated: 2026-05-31_ (added httpie, py-spy, docs, tox to layout)
