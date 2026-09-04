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

- [Dependency health helper](pipdeptree/scripts/dependency-health-helper.py) — pipdeptree + warnings + reverse deps in one script for a project overview
- [Ruff format vs black notebook](ruff/notebooks/compare-ruff-format-vs-black.ipynb) — Side-by-side Ruff format and black on a shared sample to compare diffs
- [Ty quickstart loop snippet](ty/snippets/2026-09-02-followed-ty-quickstart-loop.py) — Minimal annotated loop module for a Ty first type-check pass
- [Integrating mypy and Ruff in CI](mypy/docs/integrating-mypy-ruff-ci.md) — Sequencing Ruff then mypy so the type check runs on a clean tree
- [Mypy incremental cache and follow-imports notebook](mypy/notebooks/explore-incremental-cache-and-follow-imports.ipynb) — How the `.mypy_cache` interacts with `--follow-imports` across runs

## Layout

- `00_index/` — Navigation: topics.md, quick-links.md, glossary.md, learning-path.md
- `docs/` — Foundational concept primers, practice scripts, and snippets per concept; plus project-level docs like repository-structure.md
- `CHANGELOG.md` — Project changelog tracking kit additions
- `.gitattributes` — Git merge-strategy config (union merge for CHANGELOG.md)
- `bandit/` — Security linter first-contact primer and snippets
- `httpie/` — HTTPie CLI notes, install scripts, request workflows, configs, notebooks, CI docs, and an httpie+pytest scaffold template
- `mypy/` — mypy type-checking notes, strict configs, typed samples, CI manifests, and a type-safe package template
- `pau/` — pip-audit short-alias configs and primer
- `pdt/` — pipdeptree manifests and a dependency-hygiene scaffold template
- `pip-audit/` — Vulnerability scanning notes, JSON parsing scripts, ignore config
- `pipdeptree/` — Dependency tree notes, health-report scripts, JSON parsing, reverse-dep snippets
- `prc/` — pre-commit first-contact hook notes, configs, and scripts
- `pre-commit/` — Hook configs, install/run scripts, snippets
- `py/` — Ruff first-contact primer and install-and-lint script
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
| httpie | 6 | 5 | 2 | 2 | 3 | 2 | — | 7 | 2026-09-04 |
| mypy | 7 | 2 | 5 | 4 | 2 | 2 | 1 | 5 | 2026-09-02 |
| pau | 1 | 1 | 2 | — | — | — | — | — | 2026-07-26 |
| pdt | — | — | — | — | — | — | 1 | 9 | — |
| pip-audit | 4 | 3 | 1 | 4 | — | — | — | — | 2026-07-17 |
| pipdeptree | 8 | 4 | 1 | 6 | — | — | — | — | 2026-08-06 |
| prc | 2 | 2 | 2 | — | 1 | — | — | — | 2026-09-02 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — | — | — |
| py | 1 | 1 | — | — | — | — | — | — | — |
| py-spy | 10 | 10 | — | 2 | 2 | 1 | — | — | 2026-08-17 |
| pyproject.toml | 4 | 1 | 7 | — | — | — | — | — | 2026-08-22 |
| pytest | 5 | 4 | 1 | 2 | 2 | 1 | — | — | 2026-08-22 |
| pyright | 1 | — | — | — | — | — | — | — | 2026-08-24 |
| rich | 8 | 4 | — | 8 | 1 | 1 | — | — | 2026-09-02 |
| ruff | 6 | 2 | 5 | 2 | 1 | 1 | — | — | 2026-09-03 |
| tox | 5 | 2 | 4 | — | — | — | — | — | — |
| ty | 7 | 1 | 3 | 6 | — | — | — | — | 2026-08-04 |
| typer | 4 | 4 | — | 3 | — | — | — | — | 2026-08-18 |
| uv | 8 | 5 | 3 | 2 | 2 | — | — | — | 2026-08-22 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — | — | — |
| uvl | 2 | 1 | — | — | 2 | 1 | — | — | 2026-08-23 |

</details>

## Status

Currently adding the pipdeptree dependency-health scaffold template, the HTTPie CI/CD GitHub Actions doc, and the bandit skip-specific-tests snippet. The pre-commit under-the-hood doc and the rich status-dashboard notebook are next in the queue.

---

_Last updated: 2026-09-04_
