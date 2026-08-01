# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, pre-commit, rich, Typer, pip-audit, py-spy, tox, Ty, httpie, pyproject.toml, uv.lock, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![License](https://img.shields.io/github/license/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain — uv, Ruff, pytest, mypy, pre-commit, rich, Typer, pip-audit, py-spy, tox, Ty, httpie, pyproject.toml, uv.lock, and more. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

This kit covers package and project management (uv), linting and formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit, pau), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock), and project config conventions (pyproject.toml). It is a working reference — notes, configs, scripts, and snippets gathered in practice — not a replacement for official documentation.

## Quick links

- [Ruff quick primer](ruff/notes/0000-primer-ruf.md) — Ruff linter and formatter first-contact notes
- [Applying type hints practice script](docs/concepts/static-type-checking-type-hints/scripts/2026-07-27-applying-type-hints.py) — Apply type hints to a module and run mypy to check results
- [Common venv patterns snippet](docs/concepts/virtual-environment-dependency-mgmt/snippets/2026-07-27-common-venv-patterns.py) — Python helpers to create and compare virtual environments
- [First pip-audit quick primer](pau/notes/0000-primer-pip-audit.md) — What pau is, key terminology, and a tiny scan example
- [Git attributes config](.gitattributes) — Repository-level git attribute rules

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers and project-level documentation
  - `docs/concepts/<concept>/` — Primer notes, scripts, and snippets per foundational concept
- `httpie/` — HTTPie CLI notes, install scripts, request workflows
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pau/` — pip-audit quick primer
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
| mypy | 7 | 1 | 3 | 4 | — | — | — |
| pau | 1 | — | — | — | — | — | 2026-07-26 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 7 | 2 | 1 | 5 | — | — | — |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | — | — | 2026-07-19 |
| pyproject.toml | 3 | — | 5 | — | — | — | — |
| pytest | 5 | 3 | 1 | 2 | 1 | — | — |
| rich | 7 | 1 | — | 6 | — | — | — |
| ruff | 7 | 1 | 4 | 2 | 1 | — | 2026-08-01 |
| tox | 5 | 1 | 2 | — | — | — | — |
| ty | 6 | 1 | 2 | 2 | — | — | — |
| typer | 3 | 2 | — | 2 | — | — | — |
| uv | 6 | 4 | 2 | 1 | 1 | — | — |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — |

</details>

## Status

Currently working through foundational concept practice scripts and the Ruff quick primer. Pip-audit and uv workflows continue to grow.

---
_Last updated: 2026-08-01_