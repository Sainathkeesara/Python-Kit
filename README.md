# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, pre-commit, rich, Typer, pip-audit, py-spy, tox, Ty, httpie, pyproject.toml, uv.lock, uvl, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![License](https://img.shields.io/github/license/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain — uv, Ruff, pytest, mypy, pre-commit, rich, Typer, pip-audit, py-spy, tox, Ty, httpie, pyproject.toml, uv.lock, uvl, and more. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

This kit covers package and project management (uv), linting and formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit, pau), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock, uvl), and project config conventions (pyproject.toml). It is a working reference — notes, configs, scripts, and snippets gathered in practice — not a replacement for official documentation.

## Quick links

- [pau pip-audit pyproject config](pau/configs/2026-08-09-minimal-pip-audit-pyproject.toml) — Minimal pyproject.toml with [tool.pip-audit] strict mode and timeout settings
- [pau pip-audit scan config](pau/configs/2026-08-09-pip-audit-scan-config.toml) — pip-audit scan configuration with strict mode and custom sources
- [First pre-commit hook notes](prc/notes/2026-08-09-first-pre-commit-hook.md) — Set up first pre-commit hook: install, config, first run
- [uv script, venv, and lockfile notes](uv/notes/2026-08-09-tried-uv-script-venv-lockfile.md) — Tried uv script, venv, and lockfile workflow on a small CLI project
- [First uv project snippet](uv/snippets/2026-08-08-first-uv-project.py) — Minimal example creating a first uv project with a dependency

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `.gitattributes` — Git export-ignore and line-ending rules
- `docs/` — Foundational concept primers and project-level documentation
  - `docs/concepts/<concept>/` — Primer notes, scripts, and snippets per foundational concept
- `httpie/` — HTTPie CLI notes, install scripts, request workflows
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pau/` — pip-audit quick primer and configs
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `prc/` — pre-commit first-contact notes
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Ruff first-contact primer and install/lint script
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
- `uvl/` — uv.lock quick primer and mapping docs
- `CHANGELOG.md` — Recent changes log

## Coverage

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Last verified |
|------|-------|---------|---------|----------|------|-----------|---------------|
| httpie | 5 | 2 | 1 | 1 | — | — | 2026-07-19 |
| mypy | 7 | 1 | 4 | 4 | — | — | — |
| pau | 1 | — | 2 | — | — | — | 2026-07-26 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 8 | 2 | 1 | 6 | — | — | 2026-08-06 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — |
| prc | 1 | — | — | — | — | — | 2026-08-09 |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | — | — | 2026-07-08 |
| pyproject.toml | 3 | — | 5 | — | — | — | — |
| pytest | 5 | 3 | 1 | 2 | 1 | — | — |
| rich | 8 | 3 | — | 7 | — | — | 2026-08-05 |
| ruff | 7 | 1 | 4 | 2 | 1 | — | 2026-07-21 |
| tox | 5 | 1 | 2 | — | — | — | — |
| ty | 7 | 1 | 3 | 3 | — | — | 2026-08-04 |
| typer | 3 | 2 | — | 2 | — | — | — |
| uv | 8 | 4 | 2 | 2 | 1 | — | 2026-08-05 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — |
| uvl | 2 | — | — | — | 1 | — | 2026-08-01 |

</details>

## Status

Currently adding pau configs, prc first-contact notes, uv script/venv/lockfile workflow notes, and uv project snippets. pipdeptree tutorials, Rich styled output and inspect workflows continue to grow.

---
_Last updated: 2026-08-10_
