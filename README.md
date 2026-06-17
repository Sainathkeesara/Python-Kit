# Python-Kit
> A working engineer's Python reference for uv, Ruff, pytest, mypy, pre-commit, rich, pipdeptree, py-spy, tox, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-157-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), py-spy (profiler), tox (test automation), httpie (API testing), ty (alternative type checker), uv.lock, pyproject.toml conventions, and cross-tool workflow notes. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks |
|------|-------|---------|---------|----------|------|-----------|
| general | 2 | — | 1 | 1 | — | — |
| httpie | 4 | 1 | — | 1 | — | — |
| mypy | 6 | 1 | 2 | 3 | — | — |
| pip-audit | 3 | 3 | 1 | 1 | — | — |
| pipdeptree | 6 | 1 | — | 5 | — | — |
| pre-commit | 4 | 1 | 2 | 2 | — | — |
| py | 1 | 1 | — | — | — | — |
| py-spy | 7 | 3 | — | 2 | — | — |
| pyproject.toml | 3 | — | 4 | — | — | — |
| pytest | 5 | 3 | — | 2 | 1 | — |
| rich | 7 | 1 | — | 6 | — | — |
| ruff | 3 | — | 2 | 2 | 1 | — |
| tox | 5 | 1 | 2 | — | — | — |
| ty | 5 | 1 | 2 | 2 | — | — |
| typer | 3 | 2 | — | 1 | — | — |
| uv | 6 | 3 | 1 | 1 | 1 | — |
| uv.lock | 3 | 4 | — | 2 | — | 1 |

## Quick links

- [Rich Console API renderables](rich/notes/2026-06-17-explored-rich-console-api-renderables.md) — Renderables, styles, and output modes
- [Rich Console panel and table snippet](rich/snippets/tried-rich-console-panel-table.py) — Minimal Console script with text styling, panel, and table
- [Quality tools pyproject.toml config](general/configs/tried-quality-tools-pyproject.toml) — Combined ruff, mypy, pytest config in one pyproject.toml
- [Pre-commit ruff and mypy hooks](pre-commit/snippets/tried-ruff-mypy-config.yaml) — Minimal pre-commit config with ruff and mypy hooks
- [Ty vs mypy comparison](ty/snippets/tried-ty-vs-mypy.py) — Compare Ty and mypy output on the same typed code

## Layout

- `00_index/` — Navigation index: topics.md, quick-links.md, glossary.md
- `general/` — Cross-tool workflow notes and chaining scripts
- `httpie/` — HTTPie CLI notes, install scripts, snippets
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py-spy/` — Profiler notes, flamegraph scripts, CPU-bound samples
- `py/` — Ruff primer and Python tooling install script
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `rich/` — Terminal output notes, tables, panels, progress, snippets
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs
- `ty/` — Ty type checker comparison notes and configs
- `typer/` — CLIs built with Typer notes and demo scripts
- `tox/` — Tox automation notes, env configs, and CLI patterns
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lock file structure notes, generation and reproducibility scripts
- `docs/` — Project-level documentation

## Status

Building out first-contact notes across the Python toolchain. Recent additions cover rich Console renderables, a combined quality-tool pyproject.toml config, pre-commit hooks for ruff and mypy, Ty vs mypy comparisons, and uv CLI exploration. Notebooks and detailed walkthroughs are beginning to appear alongside the core notes.

---
_Last updated: 2026-06-17_
