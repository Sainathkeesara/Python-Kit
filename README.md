# Python-Kit
> A working engineer's Python reference for uv, Ruff, pytest, mypy, pre-commit, rich, pipdeptree, py-spy, tox, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-163-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), py-spy (profiler), tox (test automation), httpie (API testing), ty (type checker), uv.lock, pyproject.toml conventions, and cross-tool workflow notes. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks |
|------|-------|---------|---------|----------|------|-----------|
| httpie | 4 | 1 | — | 1 | — | — |
| mypy | 6 | 1 | 2 | 3 | — | — |
| pip-audit | 3 | 3 | 1 | 1 | — | — |
| pipdeptree | 7 | 1 | — | 5 | — | — |
| pre-commit | 5 | 1 | 2 | 2 | — | — |
| py | 1 | 1 | — | — | — | — |
| py-spy | 7 | 4 | — | 2 | — | — |
| pyproject.toml | 3 | — | 4 | — | — | — |
| pytest | 5 | 3 | — | 2 | 1 | — |
| rich | 7 | 1 | — | 6 | — | — |
| ruff | 4 | — | 2 | 2 | 1 | — |
| tox | 5 | 1 | 2 | — | — | — |
| ty | 6 | 1 | 2 | 2 | — | — |
| typer | 3 | 2 | — | 1 | — | — |
| uv | 6 | 3 | 1 | 1 | 1 | — |
| uv.lock | 4 | 4 | — | 2 | — | 1 |

## Quick links

- [Git Version Control primer](docs/concepts/git-version-control/0000-primer-git-version-control.md) — What is Git? Commits, branches, remotes, and how it connects to pre-commit hooks
- [Virtual Environment & Dependency Mgmt primer](docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md) — Isolated environments, lockfiles, resolution, and why they matter for Python
- [Static Type Checking & Type Hints primer](docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md) — PEP 484 type hints, gradual typing, and how mypy and Ty use them
- [py-spy flamegraph install and record script](py-spy/scripts/tried-install-and-record-flamegraph.sh) — Install py-spy and profile a CPU-bound script to flamegraph SVG
- [Ruff CLI more flags notes](ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md) — `--show-settings`, `--show-files`, `--add-noqa`, `--statistics`, and `ruff rule`

## Layout

- `00_index/` — Navigation index: topics.md, quick-links.md, glossary.md, learning-path.md
- `CHANGELOG.md` — Project changelog tracking additions and fixes over time
- `docs/` — Foundational concept primers and project-level documentation
- `httpie/` — HTTPie CLI notes, install scripts, snippets
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Ruff and Python tooling notes, install/lint scripts
- `py-spy/` — Profiler notes, flamegraph scripts, CPU-bound samples
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `rich/` — Terminal output notes, tables, panels, progress, snippets
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs
- `tox/` — Tox automation notes, env config, and CLI patterns
- `ty/` — Ty type checker comparison notes and configs
- `typer/` — CLIs built with Typer notes and demo scripts
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lock file structure notes, generation and reproducibility scripts

## Status

Building out first-contact notes across the Python toolchain. Recent additions cover Git fundamentals, virtual environments, type hints, pre-commit CLI walkthrough, Ty type checking, uv.lock package details, pipdeptree patterns, and py-spy flamegraph scripts. Actively working through notes for uv, pytest, rich, and mypy.

---
_Last updated: 2026-06-23_
