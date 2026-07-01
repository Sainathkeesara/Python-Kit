# Python-Kit
> A working engineer's Python reference for uv, Ruff, pytest, mypy, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, Ty, httpie, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Files](https://img.shields.io/badge/files-170-blue)](https://github.com/Sainathkeesara/Python-Kit)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell Script](https://img.shields.io/badge/Shell_Script-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![TOML](https://img.shields.io/badge/TOML-9C4221?logo=toml&logoColor=white)](https://toml.io/)

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers uv (package & project manager), Ruff (linter/formatter), pytest, mypy (type checking), pre-commit, rich (terminal output), typer (CLI builder), pip-audit (vulnerability scanning), pipdeptree (dependency trees), py-spy (profiler), tox (test automation), httpie (API testing), ty (type checker), uv.lock, pyproject.toml conventions, and foundational concept primers. Written from the perspective of a working engineer who prefers plain language over marketing.

## Coverage

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks |
|------|-------|---------|---------|----------|------|-----------|
| httpie | 4 | 1 | — | 1 | — | — |
| mypy | 7 | 1 | 3 | 3 | — | — |
| pip-audit | 3 | 3 | 1 | 2 | — | — |
| pipdeptree | 7 | 1 | — | 5 | — | — |
| pre-commit | 5 | 1 | 2 | 2 | — | — |
| py | 1 | 1 | — | — | — | — |
| py-spy | 7 | 5 | — | 2 | — | — |
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

- [pip-audit CVE snippet](pip-audit/snippets/tried-list-cves.py) — Parse pip-audit JSON and list CVE findings with severity
- [py-spy speedscope record script](py-spy/scripts/tried-cpu-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export
- [mypy strict disallow config](mypy/configs/tried-strict-disallow-ignore-config.ini) — Strict mypy config with disallow-untyped-defs and ignore-missing-imports
- [mypy official quickstart notes](mypy/notes/2026-06-08-tried-mypy-official-quickstart.md) — Following official docs with gradual typing and strict mode
- [Python packaging primer](docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md) — pyproject.toml, PEP 517/621, build backends, and entry points

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

Notes and snippets continue to expand across uv, pytest, rich, mypy, Ty, typer, pipdeptree, py-spy, tox, httpie, and pre-commit. Concept primer library covers all six foundational areas for the Python toolchain.

---
_Last updated: 2026-06-30_
