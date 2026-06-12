# Python-Kit
> A working engineer's Python reference for uv, Ruff, pytest, mypy, pre-commit, rich, typer, tox, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-129-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), py-spy (profiler), tox (test automation), httpie (API testing), ty (alternative type checker), uv.lock, pyproject conventions, and general quality-tool workflow notes. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets | Docs |
|------|-------|---------|---------|----------|------|
| httpie | 4 | 1 | 0 | 1 | 0 |
| mypy | 6 | 1 | 2 | 2 | 0 |
| pip-audit | 3 | 3 | 1 | 0 | 0 |
| pipdeptree | 6 | 1 | 0 | 2 | 0 |
| pre-commit | 3 | 1 | 2 | 1 | 0 |
| py / Ruff tooling | 1 | 1 | 1 | 0 | 0 |
| py-spy | 5 | 2 | 0 | 1 | 0 |
| pyproject.toml | 3 | 0 | 2 | 0 | 0 |
| pytest | 5 | 2 | 0 | 2 | 1 |
| rich | 6 | 1 | 0 | 5 | 0 |
| ruff | 3 | 0 | 1 | 1 | 1 |
| tox | 5 | 0 | 1 | 0 | 0 |
| ty | 4 | 1 | 2 | 1 | 0 |
| typer | 3 | 2 | 0 | 1 | 0 |
| uv | 5 | 3 | 1 | 1 | 1 |
| uv.lock | 3 | 2 | 0 | 1 | 0 |
| general | 1 | 0 | 0 | 1 | 0 |

## Quick links

- [Followed the official mypy quickstart](mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Using gradual typing and strict mode, where I got stuck
- [Figured out which Python quality tools belong together](general/notes/2026-06-12-figured-out-quality-tool-workflow.md) — Ruff, mypy, pytest, pre-commit, and uv as a chain
- [Run Ruff, mypy, and pytest in sequence](general/snippets/tried-first-quality-chain.py) — Single script that stops on the first failure
- [Followed the tox quickstart — multi-env setup](tox/notes/2026-06-11-followed-tox-quickstart.md) — Lint and test environments, skip_install, .tox/ disk footprint
- [pipdeptree CLI patterns I keep using](pipdeptree/notes/2026-06-12-pipdeptree-cli-patterns.md) — --warn silence, --freeze, --exclude, JSON output tricks

## Layout

- `00_index/` — Navigation index: topics.md, quick-links.md, glossary.md
- `general/` — Cross-tool workflow notes and chaining scripts
- `httpie/` — HTTPie CLI notes, install scripts, snippets
- `mypy/` — mypy type-checking notes, strict config, and typed code samples
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py-spy/` — Profiler notes, flamegraph scripts, CPU-bound samples
- `py/` — Ruff and Python tooling notes, install/lint scripts, pyproject config
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `rich/` — Terminal output notes, tables, panels, progress, snippets
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs
- `ty/` — Ty type checker comparison notes and configs
- `typer/` — CLIs built with Typer notes and demo scripts
- `tox/` — Tox automation notes, env config, and CLI patterns
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lock file structure notes, generation and reproducibility scripts
- `docs/` — Project-level documentation

## Status

Building out first-contact notes across the Python toolchain. Recent additions cover pipdeptree JSON parsing, py-spy profiling snippets, mypy workflow notes, ruff CLI exploration, and general quality-tool workflow notes. Actively working through notes for uv, pytest, and rich.

---
_Last updated: 2026-06-13_