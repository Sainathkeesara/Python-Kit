# Python-Kit
> A working engineer's Python reference — uv, Ruff, pytest, mypy, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, Ty, httpie, and more.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable snippets, and configs for the modern Python toolchain — uv, Ruff, pytest, mypy, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, Ty, httpie, pyproject.toml, and uv.lock. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers package & project management (uv), linting & formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock), and project config conventions (pyproject.toml). Includes six foundational concept primers that underpin the whole stack.

## Quick links

- [Managed project config for uv](uv/configs/2026-07-19-uv-managed-project.toml) — Scaffolded uv-managed project with pyproject.toml, build-system, and dependencies
- [End-to-end uv workflow](uv/scripts/2026-07-19-uv-workflow.sh) — Create project, add deps, sync, run, and lock with uv
- [HTTPie defaults config](httpie/configs/2026-07-19-httpie-defaults.json) — Default request options for HTTPie CLI sessions
- [Dev dependencies for pipdeptree](pipdeptree/configs/2026-07-19-dev-dependencies-pipdeptree.toml) — pyproject.toml excerpt declaring dev dependencies for dependency analysis
- [Minimal pytest config](pytest/configs/2026-07-19-minimal-pytest-config.toml) — Minimal pytest configuration in pyproject.toml format

## Layout

- `00_index/` — Navigation index: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers and project-level documentation
- `httpie/` — HTTPie CLI notes, install scripts, snippets
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

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Last verified |
|------|-------|---------|---------|----------|------|-----------|---------------|
| httpie | 4 | 1 | 1 | 1 | — | — | 2026-06-10 |
| mypy | 7 | 1 | 3 | 4 | — | — | 2026-06-12 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 7 | 2 | 1 | 5 | — | — | 2026-06-17 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | 2026-06-18 |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 8 | — | 2 | — | — | 2026-07-19 |
| pyproject.toml | 3 | — | 5 | — | — | — | 2026-06-05 |
| pytest | 5 | 3 | 1 | 2 | 1 | — | 2026-06-10 |
| rich | 7 | 1 | — | 6 | — | — | 2026-06-17 |
| ruff | 4 | — | 3 | 2 | 1 | — | 2026-06-17 |
| tox | 5 | 1 | 2 | — | — | — | 2026-06-11 |
| ty | 6 | 1 | 2 | 2 | — | — | 2026-06-18 |
| typer | 3 | 2 | — | 2 | — | — | 2026-06-10 |
| uv | 6 | 4 | 2 | 1 | 1 | — | 2026-06-16 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | 2026-06-18 |

</details>

## Status

Notes and configs continue to expand — new additions this cycle include a uv managed-project config and workflow script, HTTPie defaults, pipdeptree dev-dependencies config, and a minimal pytest config. The concept primer library covers all six foundational areas for the Python toolchain.

---
_Last updated: 2026-07-19_
