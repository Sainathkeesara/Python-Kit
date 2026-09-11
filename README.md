# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, Ty, pyright, bandit, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, httpie, and the project config that holds them together.

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

- [Hook debugging trace notebook](prc/notebooks/2026-09-10-hook-debugging-trace.ipynb) — Interactive notebook for debugging pre-commit hook execution
- [Multi-language pre-commit config](prc/configs/multi-language-pre-commit-config.yaml) — Pre-commit config spanning Python, JS, and YAML hooks
- [Writing custom pre-commit hook](prc/docs/writing-custom-pre-commit-hook.md) — How to write and test your own pre-commit hook from scratch
- [Minimal typed module (pyright)](pyright/snippets/2026-09-09-minimal-typed-module.py) — A minimal fully-annotated module for pyright type checking
- [Bandit severity & confidence debrief](bandit/docs/2026-09-09-bandit-severity-confidence-debrief.md) — Understanding severity levels and confidence scores in bandit output

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers, practice scripts, and snippets per concept; plus project-level docs like repository-structure.md
- `bandit/` — Security linter notes, scan scripts, and skip-tests snippets
- `httpie/` — HTTPie CLI notes, install scripts, request workflows, configs, notebooks, CI docs, and an httpie+pytest scaffold template
- `mypy/` — mypy type-checking notes, strict configs, typed samples, CI manifests, and a type-safe package template
- `pau/` — pip-audit short-alias configs, integration docs, and primer
- `pdt/` — pipdeptree manifests, dependency-health loop docs, and a scaffold template
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, health-report scripts, JSON parsing, reverse-dep snippets
- `prc/` — pre-commit first-contact hook notes, configs, and scripts
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — General Python launcher notes and lint scripts
- `py-spy/` — Profiler notes, flamegraph scripts, profiling-mode guide, production runbook, CPU-bound samples
- `pyproject.toml/` — pyproject.toml settings, minimal and multi-tool configs
- `pytest/` — pytest notes, fixtures, CLI flags, test scripts
- `pyright/` — Pyright type-checking primer and first-run notes
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
| bandit | 2 | 1 | — | 1 | 1 | — | — | — | 2026-09-09 |
| httpie | 6 | 5 | 2 | 2 | 3 | 2 | — | 8 | 2026-08-27 |
| mypy | 7 | 2 | 5 | 4 | 2 | 2 | 1 | 5 | 2026-08-04 |
| pau | 1 | 1 | 2 | — | 1 | — | — | — | 2026-08-21 |
| pdt | — | — | — | — | 1 | — | 1 | 9 | 2026-09-05 |
| pip-audit | 4 | 3 | 1 | 4 | — | — | — | — | 2026-07-17 |
| pipdeptree | 8 | 4 | 1 | 6 | — | — | — | — | 2026-08-06 |
| prc | 2 | 2 | 3 | — | 2 | 1 | — | — | 2026-09-10 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — | — | — |
| py | 1 | 1 | — | — | — | — | — | — | — |
| py-spy | 10 | 10 | — | 2 | 3 | 1 | — | — | 2026-07-19 |
| pyproject.toml | 4 | 1 | 7 | — | 1 | 1 | — | — | 2026-08-22 |
| pytest | 5 | 4 | 1 | 2 | 2 | 1 | — | — | 2026-07-19 |
| pyright | 3 | — | — | 1 | — | — | — | — | 2026-09-09 |
| rich | 8 | 4 | — | 8 | 1 | 1 | — | — | 2026-08-05 |
| ruff | 6 | 2 | 5 | 2 | 2 | 1 | — | — | 2026-08-18 |
| tox | 5 | 3 | 4 | — | — | — | — | — | 2026-08-26 |
| ty | 7 | 1 | 3 | 6 | — | — | — | — | 2026-08-04 |
| typer | 4 | 5 | — | 3 | — | — | — | — | 2026-08-20 |
| uv | 8 | 5 | 3 | 2 | 2 | — | — | — | 2026-08-22 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — | — | 2026-06-18 |
| uvl | 2 | 1 | — | — | 2 | 1 | — | — | 2026-08-08 |

</details>

## Status

Currently adding prc pre-commit hook debugging notebooks, writing custom hook docs, and pyright type-checking snippets. The bandit severity & confidence debrief and multi-language pre-commit config are the most recent additions.

---

_Last updated: 2026-09-10_
