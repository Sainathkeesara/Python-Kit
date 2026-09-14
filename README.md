# Python-Kit
> A working Python engineer's quick-reference for uv, Ruff, pytest, mypy, Ty, pyright, bandit, pre-commit, rich, typer, pip-audit, pipdeptree, py-spy, tox, httpie, and the project config that holds them together.

---

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working Python engineer's quick-reference: first-contact notes, runnable scripts, configuration files, and snippets collected while getting productive with the modern Python toolchain. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Notes, configs, scripts, and snippets organised per tool, covering the day-to-day Python workflow: package and project management (uv), linting and formatting (Ruff), testing (pytest), static type checking (mypy, Ty, pyright), security linting (bandit), hook management (pre-commit), terminal output (rich), CLI building (typer), dependency auditing (pip-audit), dependency trees (pipdeptree), dependency hygiene (pdt), profiling (py-spy), multi-environment test automation (tox), API testing (httpie), and lockfile analysis (uv.lock, uvl). A `docs/concepts/` tree carries the foundational primers — Git, Python fundamentals, packaging, testing principles, type hints, virtual environments, and security — that the tool notes build on.

## Quick links

- [Minimal bandit scan JSON severity script](bandit/scripts/2026-09-14-minimal-scan-json-severity.sh) — Run bandit with JSON output filtered by severity level
- [pip-audit src-layout config](pau/configs/pip-audit-src-layout.toml) — pip-audit configuration tailored for src-layout projects
- [Output formats comparison notebook](rich/notebooks/output-formats-comparison.ipynb) — Compare flamegraph, speedscope, and raw JSON profiling output formats
- [Multi-bar progress tracker](rich/scripts/multi-bar-progress-tracker.py) — Demonstrates multiple concurrent progress bars with Rich
- [Source layout multi-tool tables](docs/concepts/python-packaging-project-config/src-layout-multi-tool-tables.md) — How src-layout changes pyproject.toml tool tables

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
| bandit | 2 | 2 | — | 1 | 1 | — | — | — | 2026-09-06 |
| httpie | 6 | 5 | 2 | 2 | 3 | 2 | — | 7 | 2026-08-27 |
| mypy | 7 | 2 | 5 | 4 | 2 | 2 | 1 | 5 | 2026-06-12 |
| pau | 1 | 2 | 3 | — | 1 | — | — | — | 2026-07-26 |
| pdt | — | 2 | — | — | 1 | — | 1 | 9 | — |
| pip-audit | 4 | 3 | 1 | 4 | — | — | — | — | 2026-07-17 |
| pipdeptree | 8 | 4 | 1 | 6 | — | — | — | — | 2026-08-06 |
| prc | 2 | 2 | 3 | — | 2 | 1 | — | — | 2026-08-30 |
| pre-commit | 5 | 2 | 2 | 2 | — | — | — | — | 2026-06-18 |
| py | 1 | 1 | — | — | — | — | — | — | — |
| py-spy | 10 | 10 | — | 2 | 3 | 1 | — | — | 2026-07-19 |
| pyproject.toml | 4 | 1 | 8 | — | 1 | 1 | — | — | 2026-08-22 |
| pytest | 5 | 4 | 1 | 2 | 2 | 1 | — | — | 2026-06-10 |
| pyright | 3 | — | — | 1 | — | — | — | — | 2026-09-09 |
| rich | 8 | 5 | — | 8 | 2 | 2 | — | — | 2026-08-05 |
| ruff | 6 | 2 | 5 | 2 | 2 | 1 | — | — | 2026-07-21 |
| tox | 5 | 3 | 4 | — | — | — | — | — | 2026-06-11 |
| ty | 7 | 2 | 3 | 6 | — | — | — | — | 2026-08-04 |
| typer | 4 | 5 | — | 3 | — | — | — | — | 2026-08-18 |
| uv | 8 | 5 | 3 | 2 | 2 | — | — | — | 2026-08-10 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | — | — | 2026-06-18 |
| uvl | 2 | 1 | — | — | 2 | 1 | — | — | 2026-08-04 |

</details>

---

_Last updated: 2026-09-15_
