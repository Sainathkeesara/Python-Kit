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

Personal notes, configuration files, scripts, and snippets collected while getting productive with the modern Python toolchain. Covers package & project management (uv), linting & formatting (Ruff), testing (pytest), type checking (mypy, Ty), hook management (pre-commit), terminal output (rich), CLI frameworks (typer), vulnerability scanning (pip-audit), dependency trees (pipdeptree), profiling (py-spy), test automation (tox), API testing (httpie), lock file analysis (uv.lock), and project config conventions (pyproject.toml). Six foundational concept primers underpin the whole stack.

## Quick links

- [Parse pip-audit JSON CVEs](pip-audit/snippets/2026-07-13-parse-pip-audit-json-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [Compared py-spy record output formats](py-spy/notes/2026-07-10-compared-py-spy-record-output-formats.md) — flamegraph, speedscope, and raw JSON compared
- [CPU speedscope record script](py-spy/scripts/2026-07-10-cpu-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export
- [Parse pip-audit JSON CVEs (July 10)](pip-audit/snippets/2026-07-10-parse-pip-audit-json-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [Compared py-spy record output formats (July 8)](py-spy/notes/2026-07-08-compared-py-spy-record-output-formats.md) — flamegraph, speedscope, and raw JSON compared

## Layout

- `00_index/` — Navigation index: topics.md, quick-links.md, glossary.md, learning-path.md
- `CHANGELOG.md` — Project changelog tracking additions and fixes over time
- `docs/` — Foundational concept primers and project-level documentation (10 files)
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
| httpie | 4 | 1 | — | 1 | — | — | 2026-06-10 |
| mypy | 7 | 1 | 3 | 3 | — | — | 2026-06-12 |
| pip-audit | 3 | 3 | 1 | 4 | — | — | 2026-07-13 |
| pipdeptree | 7 | 1 | — | 5 | — | — | 2026-06-17 |
| pre-commit | 5 | 1 | 2 | 2 | — | — | 2026-06-18 |
| py | 1 | 1 | — | — | — | — | 2026-06-17 |
| py-spy | 9 | 7 | — | 2 | — | — | 2026-07-10 |
| pyproject.toml | 3 | — | 5 | — | — | — | 2026-07-05 |
| pytest | 5 | 3 | — | 2 | 1 | — | 2026-06-10 |
| rich | 7 | 1 | — | 6 | — | — | 2026-06-17 |
| ruff | 4 | — | 3 | 2 | 1 | — | 2026-07-05 |
| tox | 5 | 1 | 2 | — | — | — | 2026-06-11 |
| ty | 6 | 1 | 2 | 2 | — | — | 2026-06-18 |
| typer | 3 | 2 | — | 2 | — | — | 2026-07-05 |
| uv | 6 | 3 | 1 | 1 | 1 | — | 2026-06-16 |
| uv.lock | 4 | 4 | — | 2 | — | 1 | 2026-06-18 |

</details>

## Status

Notes and snippets continue to expand across py-spy, pip-audit, ruff, and typer. Recently added a pip-audit JSON CVE parser snippet and py-spy speedscope recording scripts. Concept primer library covers all six foundational areas for the Python toolchain.

---
_Last updated: 2026-07-15_
