# Learning Path — Python

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

These concepts have no prerequisites and are the starting point for Python tooling.

- **Python Programming Fundamentals** — Understanding basic Python syntax, functions, modules, and error handling. Everything in this kit depends on this. Primer: [Python Programming Fundamentals primer](../docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md).
- **Git Version Control** — Tracking changes, committing, branching. Required for pre-commit hooks. Primer: [Git Version Control primer](../docs/concepts/git-version-control/0000-primer-git-version-control.md).
- **Software Testing Principles** — What makes a good test, test discovery, assertions. Unlocks pytest and tox. Primer: [Software Testing Principles primer](../docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md).
- **Static Type Checking & Type Hints** — Type annotations (`str`, `int`, `Optional`, `Union`). Unlocks mypy, Ty, and typer. Primer: [Static Type Checking & Type Hints primer](../docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md).
- **Virtual Environment & Dependency Management** — Isolated Python environments, installing packages. Unlocks uv and pip-audit. Primer: [Virtual Environment & Dependency Mgmt primer](../docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md).
- **Python Packaging & Project Config** — pyproject.toml, build backends, project metadata. Unlocks pyproject.toml configs and uv.lock. Primer: [Python Packaging & Project Config primer](../docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md).

## Stage 2: Core Tools

These tools are unlocked from the start and form the day-to-day workflow.

- **uv** — Fast package and project manager. Install packages, manage environments, run scripts. Start with the [uv Primer](../uv/notes/0000-primer-uv.md) and [install script](../uv/scripts/install-and-first-command.sh).
- **Ruff** — Linter and formatter. Catches bugs and enforces style. Start with the [Ruff Primer](../ruff/notes/0000-primer-ruff.md) and [quickstart notes](../ruff/notes/2026-06-03-tried-ruff-quickstart.md).
- **pytest** — Test runner with fixtures and parametrization. Start with the [pytest Primer](../pytest/notes/0000-primer-pytest.md) and [first test suite notes](../pytest/notes/2026-06-08-installed-pytest-first-suite.md).
- **pre-commit** — Hook framework that runs linters and type checkers before each commit. Start with the [pre-commit Primer](../pre-commit/notes/0000-primer-pre-commit.md) and [install/run script](../pre-commit/scripts/install-and-run.sh).
- **pyproject.toml** — Central config file for all modern Python tools. Start with the [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) and [minimal config](../pyproject.toml/configs/minimal-pyproject.toml).

## Stage 3: Building Skills

Intermediate tools and patterns that extend the core workflow.

- **Type checking (mypy)** — Static analysis for type safety. Start with the [mypy Primer](../mypy/notes/0000-primer-mypy.md) and [CLI flags notes](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md).
- **Type checking (Ty)** — An alternative type checker with a focus on ergonomics. Start with the [Ty Primer](../ty/notes/0000-primer-ty.md) and [quickstart notes](../ty/notes/2026-06-05-tried-ty-quickstart.md).
- **Vulnerability scanning (pip-audit)** — Audit dependencies for known CVEs. Start with the [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) and [scan script](../pip-audit/scripts/scan-project.sh).
- **Dependency trees (pipdeptree)** — Visualize and analyze package dependency graphs. Start with the [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) and [JSON parsing snippet](../pipdeptree/snippets/parse-pipdeptree-json.py).
- **Lock files (uv.lock)** — Reproducible dependency resolution. Start with the [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) and [generation script](../uv.lock/scripts/generate-uv-lock.sh).

## Stage 4: Advanced Tools

Tools that depend on foundational concepts being complete.

- **Terminal output (rich)** — Beautiful terminal formatting with tables, panels, progress bars. Start with the [rich Primer](../rich/notes/0000-primer-rich.md) and [first script](../rich/scripts/first-table-panel-progress.py).
- **CLI framework (typer)** — Build command-line interfaces with type hints. Start with the [typer Primer](../typer/notes/0000-primer-typer.md) and [hello-world notes](../typer/notes/2026-06-10-first-typer-hello-world.md).
- **Profiling (py-spy)** — Sampling profiler for running Python processes. Start with the [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) and [flamegraph script](../py-spy/scripts/tried-install-and-record-flamegraph.sh).
- **API testing (httpie)** — User-friendly HTTP client for REST APIs. Start with the [httpie Primer](../httpie/notes/0000-primer-httpie.md) and [install/test script](../httpie/scripts/install_and_test_httpie.sh).
- **Test automation (tox)** — Multi-environment test runner. Start with the [tox Primer](../tox/notes/0000-primer-tox.md) and [minimal config](../tox/configs/tox.ini).
- **uv vs pip cheat sheet** — Quick reference for migrating from pip to uv: [cheat sheet](../uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md).

## Stage 5: Mastery

Advanced patterns and integrated workflows.

- **Multi-tool pyproject.toml** — Combine ruff, pytest, and mypy config in one file: [multi-tool config](../pyproject.toml/configs/multi-tool-pyproject.toml).
- **Full pre-commit pipeline** — Chain Ruff, mypy, and pytest hooks: [multi-hook config](../pre-commit/configs/tried-multi-hook-config.yaml).
- **Cross-tool quality workflow** — How Ruff, mypy, pytest, pre-commit, and uv fit together in practice.
- **Profiling advanced output formats** — Compare flamegraph SVG, speedscope JSON, and raw JSON: [output formats notes (June)](../py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md) and [output formats notes (July)](../py-spy/notes/2026-07-08-compared-py-spy-record-output-formats.md).
- **CVE parsing from pip-audit** — Parse vulnerability scan output programmatically: [CVE snippet](../pip-audit/snippets/tried-list-cves.py).
- **Speedscope profiling workflow** — Record and export speedscope JSON from CPU-bound workloads: [speedscope script](../py-spy/scripts/tried-cpu-speedscope-record.py) and [July speedscope script](../py-spy/scripts/2026-07-08-cpu-speedscope-record.py).
- **Reproducible lock files** — Test uv.lock checksum stability across lock commands: [reproducibility script](../uv.lock/scripts/tried-uv-lock-reproducibility.sh).

## Progression Map

```
Python Programming Fundamentals
├── Git Version Control ──────► pre-commit
├── Software Testing Principles ─► pytest ──► tox
├── Static Type Checking ──────► mypy, Ty, typer
├── Virtual Environment Mgmt ──► uv ──► uv.lock, pip-audit, pipdeptree
└── Python Packaging Config ───► pyproject.toml
                                     │
                                     ├── Ruff (linter config)
                                     ├── pytest (test config)
                                     └── mypy (type check config)
```
