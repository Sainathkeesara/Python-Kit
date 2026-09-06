# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, Ty, pyright, bandit, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, httpie, pdt, and the project config that holds them together.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

---

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Notes, configs, scripts, and snippets organised per tool, covering the day-to-day Python workflow: package and project management (uv), linting and formatting (Ruff), testing (pytest), static type checking (mypy, Ty, pyright), security linting (bandit), hook management (pre-commit), terminal output (rich), CLI building (typer), dependency auditing (pip-audit), dependency trees (pipdeptree), dependency hygiene (pdt), profiling (py-spy), multi-environment test automation (tox), API testing (httpie), and lockfile analysis (uv.lock, uvl). A `docs/concepts/` tree carries the foundational primers — Git, Python fundamentals, packaging, testing principles, type hints, virtual environments, and security — that the tool notes build on.

## Quick links

- [pyproject.toml tool tables](docs/concepts/python-packaging-project-config/pyproject-toml-tool-tables.md) — Mapping of pyproject.toml tables to the tools that consume them
- [AAA, parametrize, fixtures, coverage, and static typing](docs/concepts/software-testing-principles/aaa-parametrize-fixtures-coverage-static-typing-ci.md) — How pytest fixtures, parametrize, coverage, and type checking compose in a real test suite
- [First pyright type check](pyright/notes/2026-09-05-first-pyright-type-check.md) — First-contact notes from running pyright on a typed codebase
- [Integrating pipdeptree, pip-audit, and uv in a dependency-health loop](pdt/docs/integrating-pipdeptree-pip-audit-uv-dependency-health-loop.md) — A single CI job that runs pipdeptree, pip-audit, and a drift check in sequence
- [Skip specific bandit tests](bandit/snippets/2026-09-04-skip-specific-bandit-tests.sh) — Skip B101 and B105 for test files without losing the rest of the scan

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers, practice scripts, and snippets per concept; plus project-level docs like repository-structure.md
- `CHANGELOG.md` — Project changelog tracking kit additions
- `.gitattributes` — Git merge-strategy config (union merge for CHANGELOG.md)
- `bandit/` — Security linter first-contact primer and snippets
- `httpie/` — HTTPie CLI notes, install scripts, request workflows, configs, notebooks, CI docs, and an httpie+pytest scaffold template
- `mypy/` — mypy type-checking notes, strict configs, typed samples, CI manifests, and a type-safe package template
- `pau/` — pip-audit short-alias configs and primer
- `pdt/` — Dependency-hygiene scaffold template, CI manifests, and integration docs
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, health-report scripts, JSON parsing, reverse-dep snippets
- `prc/` — pre-commit first-contact hook notes, configs, and scripts
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — General Python launcher notes and lint scripts
- `py-spy/` — Profiler notes, flamegraph scripts, profiling-mode guide, CPU-bound samples
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `pyright/` — Pyright type-checking primer and notes
- `rich/` — Terminal output notes, tables, panels, progress, snippets, and a status-dashboard doc
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs, format-vs-black notebook
- `tox/` — Tox automation notes, env config, and CLI patterns
- `ty/` — Ty type checker notes, configs, and comparisons with mypy
- `typer/` — CLIs built with Typer, notes and demo scripts
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lockfile structure notes, generation and reproducibility scripts
- `uvl/` — uv.lock mapping primer and dependency docs

---

## Coverage

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Manifests | Templates | Last verified |
|------|-------|---------|---------|----------|------|-----------|-----------|-----------|---------------|
| bandit | 1 | — | — | 1 | — | — | — | — | 2026-08-29 |
| httpie | 6 | 5 | 2 | 2 | 3 | 2 | — | 8 | 2026-09-04 |
| mypy | 7 | 2 | 5 | 4 | 2 | 2 | 1 | 5 | 2026-09-02 |
| pau | 1 | 1 | 2 | — | — | — | — | — | 2026-07-26 |
| pdt | — | — | — | — | 1 | — | 1 | 9 | 2026-09-05 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | — | — | 2026-07-17 |
| pipdeptree | 8 | 4 | 1 | 6 | — | — | — | — | 2026-08-06 |
| prc | 2 | 2 | 2 | — | 1 | — | — | — | 2026-09-02 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — | — | — |
| py | 1 | 1 | — | — | — | — | — | — | — |
| py-spy | 10 | 10 | — | 2 | 2 | 1 | — | — | 2026-08-17 |
| pyproject.toml | 4 | 1 | 7 | — | — | — | — | — | 2026-08-22 |
| pyright | 2 | — | — | — | — | — | — | — | 2026-09-05 |
| pytest | 5 | 4 | 1 | 2 | 2 | 1 | — | — | 2026-08-22 |
| rich | 8 | 4 | — | 8 | 1 | 1 | — | — | 2026-09-02 |
| ruff | 6 | 2 | 5 | 2 | 2 | 1 | — | — | 2026-09-03 |
| tox | 5 | 2 | 4 | — | — | — | — | — | — |
| ty | 7 | 1 | 3 | 6 | — | — | — | — | 2026-08-04 |
| typer | 4 | 4 | — | 3 | — | — | — | — | 2026-08-18 |
| uv | 8 | 5 | 3 | 2 | 2 | — | — | — | 2026-08-22 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — | — | — |
| uvl | 2 | 1 | — | — | 2 | 1 | — | — | 2026-08-23 |

</details>

## Status

Expanding pyright first-contact notes, adding the pipdeptree dependency-health scaffold template and integration docs, and filling in bandit skip-pattern snippets. The foundational concepts tree now includes pyproject.toml tool-table mapping and AAA/parametrize testing patterns.

---

_Last updated: 2026-09-05_
