# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, Ty, pre-commit, rich, Typer, pip-audit, py-spy, tox, httpie, and the project config that holds them together.

[![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)
[![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/Python-Kit)](https://github.com/Sainathkeesara/Python-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain — uv, Ruff, pytest, mypy, Ty, pre-commit, rich, Typer, pip-audit, py-spy, tox, httpie, and more. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Notes, configs, scripts, and snippets organised per tool, covering the day-to-day Python workflow: package and project management (uv), linting and formatting (Ruff), testing (pytest), static type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI building (typer), dependency auditing (pip-audit), dependency trees (pipdeptree), profiling (py-spy), multi-environment test automation (tox), API testing (httpie), and lockfile analysis (uv.lock, uvl). A `docs/concepts/` tree carries the foundational primers — Git, Python fundamentals, packaging, testing principles, type hints, and virtual environments — that the tool notes build on.

## Quick links

- [Build and verify a wheel](docs/concepts/python-packaging-project-config/scripts/2026-08-12-build-verify-wheel.py) — Build a minimal PEP 621 package into a wheel and inspect what actually gets packaged
- [Boundary values and test doubles](docs/concepts/software-testing-principles/snippets/2026-08-12-boundary-values-test-doubles.py) — Boundary-value cases and test doubles applied in pytest
- [Git workflows, branches, tags, and CI](docs/concepts/git-version-control/git-workflows-branches-tags-ci.md) — Branch-and-PR flow, semantic release tags, and CI gates tied to a uv lockfile
- [Comprehensions, generators, error handling](docs/concepts/python-programming-fundamentals/snippets/2026-08-11-comprehensions-generators-error-handling.py) — Practice transforming data, lazy sequences, and try/except
- [pip-audit pyproject config](pau/configs/2026-08-09-minimal-pip-audit-pyproject.toml) — Minimal pyproject.toml with `[tool.pip-audit]` strict mode and timeout settings

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers, practice scripts, and snippets per concept; plus project-level docs like repository-structure.md
- `httpie/` — HTTPie CLI notes, install scripts, request workflows
- `mypy/` — mypy type-checking notes, strict configs, and typed code samples
- `pau/`, `prc/`, `uvl/` — short alias folders for pip-audit, pre-commit, and uv.lock first-contact content
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, JSON parsing, reverse-dep snippets
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Ruff first-contact primer and install-and-lint script
- `py-spy/` — Profiler notes, flamegraph scripts, CPU-bound samples
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `rich/` — Terminal output notes, tables, panels, progress, snippets
- `ruff/` — Linter/formatter notes, configs, CLI exploration, vs flake8 docs
- `tox/` — Tox automation notes, env config, and CLI patterns
- `ty/` — Ty type checker notes, configs, and comparisons with mypy
- `typer/` — CLIs built with Typer, notes and demo scripts
- `uv/` — uv package/project manager notes, scripts, and configs
- `uv.lock/` — Lockfile structure notes, generation and reproducibility scripts
- `CHANGELOG.md` — Recent changes log

## Coverage

<details>
<summary>Coverage table</summary>

| Tool | Notes | Scripts | Configs | Snippets | Docs | Notebooks | Last verified |
|------|-------|---------|---------|----------|------|-----------|---------------|
| httpie | 5 | 2 | 1 | 1 | — | — | 2026-07-19 |
| mypy | 7 | 1 | 4 | 4 | — | — | 2026-08-04 |
| pau | 1 | — | 2 | — | — | — | 2026-08-09 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | 2026-07-17 |
| pipdeptree | 8 | 2 | 1 | 6 | — | — | 2026-08-06 |
| prc | 1 | — | — | — | — | — | 2026-08-10 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | 2026-07-17 |
| py | 1 | 1 | — | — | — | — | — |
| py-spy | 10 | 9 | — | 2 | — | — | 2026-07-20 |
| pyproject.toml | 3 | — | 5 | — | — | — | 2026-07-05 |
| pytest | 5 | 3 | 1 | 2 | 1 | — | 2026-07-19 |
| rich | 8 | 3 | — | 7 | — | — | 2026-08-07 |
| ruff | 6 | 1 | 4 | 2 | 1 | — | 2026-08-03 |
| tox | 5 | 2 | 2 | — | — | — | 2026-08-05 |
| ty | 7 | 1 | 3 | 3 | — | — | 2026-08-05 |
| typer | 3 | 2 | — | 2 | — | — | 2026-07-05 |
| uv | 8 | 4 | 2 | 2 | 1 | — | 2026-08-10 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — |
| uvl | 2 | — | — | — | 1 | — | 2026-08-08 |

</details>

## Status

The docs/concepts tree is getting most of the attention right now — practice scripts and snippets for packaging (wheel builds), testing (boundary values, test doubles), Git workflows, and Python fundamentals. pip-audit configs and pipdeptree tutorials continue to grow alongside it.

---
_Last updated: 2026-08-12_
