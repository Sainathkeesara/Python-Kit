# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, mypy, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, Ty, httpie, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![License](https://img.shields.io/github/license/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain — uv, Ruff, pytest, mypy, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, Ty, httpie, pyproject.toml, and uv.lock. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

204 files across 16 tool directories, 6 foundational concept primers, a repository-structure doc, and a changelog. Covers package and project management (uv), linting and formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock), and project config conventions (pyproject.toml).

## Quick links

- [Ruff end-to-end lint-and-format workflow](ruff/scripts/end-to-end-ruff-lint-format.sh) — Install Ruff, lint a project, auto-fix, format, and verify with a single script
- [Virtual environment management practice](docs/concepts/virtual-environment-dependency-mgmt/scripts/2026-07-23-venv-practice.py) — Create, activate, deactivate, and delete venvs programmatically
- [Git version control practice](docs/concepts/git-version-control/scripts/2026-07-23-practice-git-version-control.py) — Reproduce common Git workflows from a Python script
- [Common Git patterns in Python projects](docs/concepts/git-version-control/snippets/2026-07-23-common-git-patterns-in-python-projects.py) — Using GitPython to clone, commit, branch, and merge
- [Common type-checking patterns](docs/concepts/static-type-checking-type-hints/snippets/2026-07-23-common-type-checking-patterns.py) — Typed dicts, callables, overloads, and Protocol patterns

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers and project-level documentation
  - `docs/concepts/<concept>/` — Primer notes, scripts, and snippets per foundational concept
- `httpie/` — HTTPie CLI notes, install scripts, request workflows
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Python launcher notes and lint scripts
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
- `CHANGELOG.md` — Recent changes log

## Coverage

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Last verified |
|------|-------|---------|---------|----------|------|-----------|---------------|
| httpie | 5 | 2 | 1 | 1 | — | — | 2026-07-19 |
| mypy | 7 | 1 | 3 | 4 | — | — | 2026-07-19 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 7 | 2 | 1 | 5 | — | — | 2026-07-19 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | 2026-06-18 |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | — | — | 2026-07-20 |
| pyproject.toml | 3 | — | 5 | — | — | — | 2026-07-05 |
| pytest | 5 | 3 | 1 | 2 | 1 | — | 2026-07-19 |
| rich | 7 | 1 | — | 6 | — | — | 2026-06-17 |
| ruff | 6 | 1 | 4 | 2 | 1 | — | 2026-07-24 |
| tox | 5 | 1 | 2 | — | — | — | 2026-06-11 |
| ty | 6 | 1 | 2 | 2 | — | — | 2026-06-18 |
| typer | 3 | 2 | — | 2 | — | — | 2026-07-05 |
| uv | 6 | 4 | 2 | 1 | 1 | — | 2026-07-19 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | 2026-06-18 |

</details>

## Status

Ruff gained an end-to-end lint-and-format workflow script (2026-07-23), and the concept primer library expanded with new practice scripts and snippets for Git version control, virtual environment management, and static type-checking patterns.

---
_Last updated: 2026-07-24_
