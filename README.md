# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, mypy, pre-commit, rich, typer, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-95-blue)](https://github.com/Sainathkeesara/Python-Kit)
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
| py | 2 | 1 | 1 | — | — |
| pyproject.toml | 2 | — | 2 | — | — |
| pytest | 2 | 1 | — | 1 | 1 |
| pre-commit | 2 | 1 | 2 | 1 | — |
| pip-audit | 2 | 2 | 1 | — | — |
| pipdeptree | 4 | 1 | — | 1 | — |
| mypy | 5 | 1 | 1 | 1 | — |
| rich | 5 | 1 | — | 4 | — |
| ty | 3 | — | 2 | 1 | — |
| typer | 2 | 2 | — | — | — |
| py-spy | 2 | 2 | — | 1 | — |
| httpie | 3 | 1 | — | — | — |
| tox | 2 | — | 1 | — | — |
| ruff | 3 | — | 1 | 1 | 1 |

## Quick links

- [pipdeptree filtering notes](pipdeptree/notes/2026-06-07-tripped-on-pipdeptree-filtering.md) — What tripped me up: filter by package, JSON format quirks, and handling missing deps
- [pipdeptree JSON parser snippet](pipdeptree/snippets/parse-pipdeptree-json.py) — Parse pipdeptree JSON output and list leaf packages
- [py-spy CPU-bound simulation](py-spy/snippets/tried-cpu-bound-simulation.py) — Minimal script simulating CPU-bound work for py-spy to sample
- [mypy first check tripped me up](mypy/notes/2026-06-05-mypy-first-check-tripped-me-up.md) — What caught me off guard on my first mypy check
- [Ruff CLI exploration notes](ruff/notes/2026-06-06-cli-exploration.md) — CLI flags, output formats for check and format commands

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

Building out first-contact notes across the Python toolchain. Recent additions cover pipdeptree JSON parsing, py-spy profiling snippets, mypy workflow notes, and Ruff CLI exploration. Actively working through notes for uv, pytest, and rich.

---
_Last updated: 2026-06-07_
