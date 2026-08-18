# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, Ty, pre-commit, rich, Typer, pip-audit, pipdeptree, py-spy, tox, httpie, and the project config that holds them together.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain — uv, Ruff, pytest, mypy, Ty, pre-commit, rich, Typer, pip-audit, pipdeptree, py-spy, tox, httpie, and more. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Notes, configs, scripts, and snippets organised per tool, covering the day-to-day Python workflow: package and project management (uv), linting and formatting (Ruff), testing (pytest), static type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI building (typer), dependency auditing (pip-audit), dependency trees (pipdeptree), profiling (py-spy), multi-environment test automation (tox), API testing (httpie), and lockfile analysis (uv.lock, uvl). A `docs/concepts/` tree carries the foundational primers — Git, Python fundamentals, packaging, testing principles, type hints, and virtual environments — that the tool notes build on.

## Quick links

- [Venv strategies in real projects: venv vs uv vs tox](docs/concepts/virtual-environment-dependency-mgmt/venv-strategies-venv-uv-tox.md) — How venv, uv, and tox each solve a different layer of environment management
- [First rich output: markup colors, a table, and a live display](rich/snippets/2026-08-18-first-rich-output.py) — Minimal example showing Rich markup, tables, and live display in one script
- [When to use py-spy top vs record/flamegraph vs dump](py-spy/docs/when-to-use-py-spy-top-vs-record-flamegraph-vs-dump.md) — Choosing the right py-spy mode for the question you're asking
- [CI parity check script](prc/scripts/2026-08-17-ci-parity-check.sh) — Automate pre-commit install and repo-wide hook runs that match CI behaviour
- [First real pre-commit config](prc/configs/2026-08-17-pre-commit-config.yaml) — Pinned ruff + pre-commit-hooks set for day-to-day commits

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers, practice scripts, and snippets per concept; plus project-level docs like repository-structure.md
- `httpie/` — HTTPie CLI notes, install scripts, request workflows, and notebooks
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pau/` — pip-audit short-alias configs and primer
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `prc/` — pre-commit first-contact hook notes, configs, and scripts
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Ruff first-contact primer and install-and-lint script
- `py-spy/` — Profiler notes, flamegraph scripts, CPU-bound samples, and docs
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `rich/` — Terminal output notes, tables, panels, progress, snippets
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs
- `tox/` — Tox automation notes, env config, and CLI patterns
- `ty/` — Ty type checker notes, configs, and comparisons with mypy
- `typer/` — CLIs built with Typer, notes and demo scripts
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lockfile structure notes, generation and reproducibility scripts
- `uvl/` — uv.lock mapping primer and dependency docs
- `CHANGELOG.md` — Recent changes log

## Coverage

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Last verified |
|------|-------|---------|---------|----------|------|-----------|---------------|
| httpie | 5 | 3 | 1 | 1 | 1 | 1 | 2026-08-15 |
| mypy | 7 | 2 | 5 | 4 | 1 | — | 2026-08-16 |
| pau | 1 | — | 2 | — | — | — | 2026-07-26 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 8 | 2 | 1 | 6 | — | — | 2026-08-06 |
| prc | 1 | 1 | 1 | — | — | — | 2026-08-17 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | 1 | — | 2026-08-17 |
| pyproject.toml | 3 | — | 5 | — | — | — | — |
| pytest | 5 | 3 | 1 | 2 | 1 | — | — |
| rich | 8 | 3 | — | 8 | — | — | 2026-08-05 |
| ruff | 6 | 1 | 4 | 2 | 1 | — | 2026-08-03 |
| tox | 5 | 2 | 2 | — | — | — | — |
| ty | 7 | 1 | 3 | 3 | — | — | 2026-08-04 |
| typer | 3 | 3 | — | 2 | — | — | — |
| uv | 8 | 4 | 2 | 2 | 1 | — | 2026-08-10 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — |
| uvl | 2 | — | — | — | 1 | — | 2026-08-08 |

</details>

## Status

Currently working through first-contact notes and configs across the toolchain, with recent additions in venv strategies (venv vs uv vs tox), py-spy output-mode selection, rich first-output snippets, and the prc tool (first real config + CI parity script).

---
_Last updated: 2026-08-18_
