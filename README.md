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

199 files across 16 tool directories plus 6 foundational concept primers and a repository-structure doc. Covers package and project management (uv), linting and formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock), and project config conventions (pyproject.toml).

## Quick links

- [Ruff select, ignore, extend-safe, and per-directory overrides](ruff/notes/2026-07-21-ruff-select-ignore-extend-safe-overrides.md) — Walked through Ruff's rule configuration and the distinction between `select` as a filter vs a toggle
- [Fresh standalone ruff.toml with select/ignore rules](ruff/configs/2026-07-21-minimal-standalone-ruff.toml) — Ready-to-use standalone Ruff config for a new Python project
- [Profile a tiny loop with py-spy](py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh) — Install py-spy, profile a CPU-bound loop, and export a flamegraph
- [First Ruff project: what tripped me up](ruff/notes/2026-07-19-tripped-on-ruff-first-project.md) — Initial Ruff setup, CLI exploration, and the gotchas that caught me
- [Followed the official httpie quickstart](httpie/notes/2026-07-19-followed-httpie-quickstart.md) — Sessions, headers, and JSON handling gotchas from a fresh install

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers and project-level documentation
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
| pre-commit | 5 | 2 | 2 | 2 | — | — | 2026-07-17 |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | — | — | 2026-07-20 |
| pyproject.toml | 3 | — | 5 | — | — | — | 2026-07-05 |
| pytest | 5 | 3 | 1 | 2 | 1 | — | 2026-07-19 |
| rich | 7 | 1 | — | 6 | — | — | — |
| ruff | 6 | — | 4 | 2 | 1 | — | 2026-07-21 |
| tox | 5 | 1 | 2 | — | — | — | — |
| ty | 6 | 1 | 2 | 2 | — | — | — |
| typer | 3 | 2 | — | 2 | — | — | 2026-07-05 |
| uv | 6 | 4 | 2 | 1 | 1 | — | 2026-07-19 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — |

</details>

## Status

Notes and snippets continue to expand across ruff, httpie, uv, py-spy, and pip-audit. Ruff gained expanded select/ignore/extend-safe notes and a fresh standalone config (2026-07-21), and py-spy added a streamlined profile loop script (2026-07-20). The concept primer library covers all six foundational areas for the Python toolchain.

---
_Last updated: 2026-07-22_
