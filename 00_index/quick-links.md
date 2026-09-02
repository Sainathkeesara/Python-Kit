# Quick Links

## Foundational Concepts

- [Git Version Control Primer](../docs/concepts/git-version-control/0000-primer-git-version-control.md) — What is Git? first-contact notes
- [Git workflows, branches, tags, and CI](../docs/concepts/git-version-control/git-workflows-branches-tags-ci.md) — Branch-and-PR flow, semantic release tags, and CI gates tied to a uv lockfile
- [Derive a version from git tags](../docs/concepts/git-version-control/scripts/derive-version-from-git-tags.py) — setuptools-scm-style version resolution from plain git history
- [Python Programming Fundamentals Primer](../docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md) — What are Python programming fundamentals? first-contact notes
- [Comprehensions, Generators, Error Handling](../docs/concepts/python-programming-fundamentals/snippets/2026-08-11-comprehensions-generators-error-handling.py) — Practice transforming data, lazy sequences, and try/except
- [Dataclasses, Context Managers, Decorators](../docs/concepts/python-programming-fundamentals/scripts/2026-08-27-dataclasses-context-managers-decorators.py) — Practice advanced Python fundamentals with dataclasses, context managers, and decorators
- [Python Packaging & Project Config Primer](../docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md) — What is Python packaging and project config? first-contact notes
- [Build and Verify a Wheel](../docs/concepts/python-packaging-project-config/scripts/2026-08-12-build-verify-wheel.py) — Build a minimal PEP 621 package into a wheel and inspect the manifest
- [Software Testing Principles Primer](../docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md) — What are software testing principles? first-contact notes
- [Parametrized AAA tests](../docs/concepts/software-testing-principles/snippets/2026-08-20-parametrized-aaa-tests.py) — Arrange-act-assert made explicit with `parametrize` and a fixture
- [Boundary Values and Test Doubles](../docs/concepts/software-testing-principles/snippets/2026-08-12-boundary-values-test-doubles.py) — Boundary-value cases and test doubles applied in pytest
- [Static Type Checking & Type Hints Primer](../docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md) — What are type hints and static type checkers? first-contact notes
- [Type-checking patterns: Protocol, TypedDict, generics](../docs/concepts/static-type-checking-type-hints/typing-patterns-protocol-typeddict-generics.md) — Structural typing, fixed-shape dicts, and type-preserving generics in real projects
- [CI-ready static type checking with pytest and pyproject.toml](../docs/concepts/static-type-checking-type-hints/ci-ready-static-checking-pytest-pyproject.md) — Wiring mypy into a CI pipeline with pytest and pyproject.toml
- [Virtual Environment & Dependency Mgmt Primer](../docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md) — What are virtual environments and dependency management? first-contact notes
- [Venv strategies in real projects: venv vs uv vs tox](../docs/concepts/virtual-environment-dependency-mgmt/venv-strategies-venv-uv-tox.md) — How venv, uv, and tox each solve a different layer of environment management
- [Security Best Practices Primer](../docs/concepts/security-best-practices/0000-primer-security-best-practices.md) — Dependency scanning, secrets hygiene, input validation, and least privilege
- [Secure coding patterns](../docs/concepts/security-best-practices/snippets/2026-08-27-secure-coding-patterns.py) — Common secure coding patterns and anti-patterns in Python
- [Dependency, secrets, and deserialization practice](../docs/concepts/security-best-practices/scripts/2026-08-28-dependency-secrets-scan-deserialize.py) — Three runnable security habits: scanning deps, spotting leaked secrets, and safe parsing
- [Repository Structure](../docs/repository-structure.md) — How this repo is laid out

## I need to...

### Set up a Python project
- [uv Primer](../uv/notes/0000-primer-uv.md) — What is uv? first-contact notes
- [Install uv Script](../uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [End-to-end uv Workflow Script](../uv/scripts/2026-07-19-uv-workflow.sh) — Create project, add deps, sync, run, and lock with uv
- [Bootstrap + lockcheck script](../uv/scripts/bootstrap-project-lockcheck.sh) — Scaffold a uv project, sync every group, wipe and re-sync to prove the lockfile reproduces
- [Managed Project Config](../uv/configs/2026-07-19-uv-managed-project.toml) — Scaffolded uv-managed project with pyproject.toml, build-system, and dependencies
- [uv dependency groups pyproject](../uv/configs/uv-dependency-groups-pyproject.toml) — Runtime deps in `[project]`, dev-only deps in `[dependency-groups]`
- [uv script, venv, and lockfile workflow notes](../uv/notes/2026-08-09-tried-uv-script-venv-lockfile.md) — Tried uv script, venv, and lockfile workflow on a small CLI project
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first-contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project

### Lint and format code
- [Ruff Primer](../ruff/notes/0000-primer-ruff.md) — What is Ruff? first-contact notes
- [Ruff select, ignore, extend-safe, and per-directory overrides](../ruff/notes/2026-07-21-ruff-select-ignore-extend-safe-overrides.md) — `select` as a filter, safe fixes only, and per-directory rule exceptions
- [Pinned Ruff rule set](../ruff/configs/2026-08-18-pinned-rule-set.toml) — Explicit rule selections, ignores, and per-rule settings for a settled linter config
- [Ruff End-to-End Lint-and-Format Workflow](../ruff/scripts/end-to-end-ruff-lint-format.sh) — Install Ruff, lint a project, auto-fix, format, and verify end to end
- [Ruff Linter Config](../ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [Messy Example Snippet](../ruff/snippets/messy_example.py) — Deliberately broken code to test the linter
- [Ruff Install Script](../py/scripts/install-and-lint.sh) — Install Ruff and lint a Python file

### Write and run tests
- [pytest Primer](../pytest/notes/0000-primer-pytest.md) — What is pytest? first-contact notes
- [pytest vs unittest Docs](../pytest/docs/pytest-vs-unittest-mapping.md) — API mapping and migration patterns from unittest
- [Run pytest with CLI Flags Script](../pytest/scripts/run-pytest-with-cli-flags.sh) — Create a test file and run with -v, -k, -x, --tb=short
- [Fixtures with conftest Notes](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md) — conftest.py with shared setup/teardown using yield fixtures
- [Minimal pytest Config](../pytest/configs/2026-07-19-minimal-pytest-config.toml) — Minimal pytest configuration in pyproject.toml format
- [Fixtures, conftest, and scoping patterns](../pytest/docs/fixtures-conftest-scoping.md) — Fixtures, conftest, and scoping patterns explained
- [red-green-refactor notebook](../pytest/notebooks/red-green-refactor-loop.ipynb) — Interactive TDD workflow with pytest

### Type-check code
- [mypy Primer](../mypy/notes/0000-primer-mypy.md) — What is mypy? first-contact notes
- [Followed mypy Quickstart Notes](../mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Gradual typing, strict mode, what tripped me up
- [Selective mypy strictness config](../mypy/configs/2026-08-04-selective-mypy-strictness.ini) — Minimal mypy.ini with strict mode and per-directory rule overrides
- [Incremental mypy CI workflow](../mypy/manifests/ci-incremental-mypy-workflow.yaml) — A fail-fast, cache-warm type-check job keyed by lockfile and interpreter version
- [Ty Primer](../ty/notes/0000-primer-ty.md) — What is Ty? first-contact notes
- [Followed Ty quickstart notes](../ty/notes/2026-08-04-followed-ty-quickstart.md) — Following the Ty quickstart, first type check, what tripped me up
- [Minimal annotated module](../ty/snippets/2026-08-18-minimal-annotated-module.py) — A minimal fully-annotated module to run Ty's type checker against
- [Minimal annotated Ty module](../ty/snippets/2026-08-29-ty-minimal-module.py) — Minimal fully-annotated module with generics, TypeVar, and reveal_type for Ty exploration
- [Pyright Primer](../pyright/notes/0000-primer-pyright.md) — Microsoft's fast static type checker for Python
- [Type-safe Python package template](../mypy/templates/type-safe-python-package/) — A minimal src-layout package wired for mypy strict checking from the first commit

### Manage pre-commit hooks
- [pre-commit Primer](../pre-commit/notes/0000-primer-pre-commit.md) — What is pre-commit? first-contact notes
- [First pre-commit hook notes](../prc/notes/2026-08-09-first-pre-commit-hook.md) — Set up first pre-commit hook: install, config, first run
- [pre-commit quickstart gotchas](../prc/notes/2026-08-30-pre-commit-quickstart-gotchas.md) — Local hooks, --hook-stage, and pass_args — the three things that kept tripping me up
- [pre-commit bootstrap script](../prc/scripts/pre-commit-bootstrap.sh) — Bootstrap pre-commit on a fresh repo: ensure the config exists, install the git hook, and run --all-files
- [First real pre-commit config](../prc/configs/2026-08-17-pre-commit-config.yaml) — Pinned ruff + pre-commit-hooks set for day-to-day commits
- [CI parity check script](../prc/scripts/2026-08-17-ci-parity-check.sh) — Automate pre-commit install and repo-wide hook runs that match CI behaviour
- [Run Ruff + Trailing-Whitespace Hooks Script](../pre-commit/scripts/run-pre-commit-ruff-trailing-ws.sh) — Configure a sample project with ruff and trailing-whitespace hooks, run them once

### Scan for security issues
- [bandit Primer](../bandit/notes/0000-primer-bandit.md) — What is bandit? first-contact notes for the AST-based security linter

### Audit and understand dependencies
- [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first-contact notes
- [Scan Project Script](../pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [Parse pip-audit JSON CVEs](../pip-audit/snippets/2026-07-13-parse-pip-audit-json-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [pau scan config](../pau/configs/2026-08-09-pip-audit-scan-config.toml) — pip-audit scan configuration with strict mode and custom sources
- [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first-contact notes
- [Dependency-health report](../pipdeptree/scripts/dependency-health-report.sh) — Turn `--warn`, `--reverse`, and `--json` output into one health summary
- [Reverse Dependency Snippet](../pipdeptree/snippets/find-reverse-deps.py) — Use `--reverse` to find which packages depend on a given package

### Manage lockfiles
- [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) — What is uv.lock? first-contact notes
- [uv.lock mapping to pyproject](../uvl/notes/2026-08-04-uv-lock-mapping-to-pyproject.md) — Map uv.lock sections to pyproject.toml tables
- [Generate uv.lock Script](../uv.lock/scripts/generate-uv-lock.sh) — Generate a uv.lock with uv sync
- [Reproducibility Test Script](../uv.lock/scripts/tried-uv-lock-reproducibility.sh) — Test that uv.lock checksums are stable across lock commands
- [Exploring uv.lock Structure Notebook](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb) — Walk through uv.lock sections, hashes, and reproducibility mechanisms

### Configure pyproject.toml
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first-contact notes
- [Multi-tool pyproject.toml Config](../pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config
- [First PEP 621 Config](../pyproject.toml/configs/first-pep621-config.toml) — PEP 621 build-system and project metadata with hatchling
- [pyproject.toml Settings Notes](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md) — Key pyproject.toml settings explained
- [Validate pyproject.toml with tomllib](../pyproject.toml/scripts/2026-08-22-validate-pyproject-tomllib.py) — Validate pyproject.toml structure with tomllib

### Build a CLI
- [Typer Primer](../typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [What tripped me up in the typer quickstart](../typer/notes/2026-08-18-tripped-up-typer-quickstart.md) — Positional args, the free `--no-` pair, and docstring-driven `--help`
- [Typer quickstart CLI](../typer/scripts/2026-08-18-quickstart-args-options-help.py) — Arguments, options, and generated help in one small script
- [Typer TODO CLI](../typer/scripts/2026-08-20-todo-cli.py) — A small persists-to-disk todo list with `add` / `list` / `done` subcommands
- [Minimal CLI Demo](../typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Typer CLI Option + Subcommand Snippet](../typer/snippets/2026-07-05-typer-cli-option-and-subcommand.py) — Typer CLI with one option and two subcommands

### Profile performance
- [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first-contact notes
- [When to use top vs record/flamegraph vs dump](../py-spy/docs/when-to-use-py-spy-top-vs-record-flamegraph-vs-dump.md) — Choosing the right py-spy mode for the question you're asking
- [py-spy modes comparison notebook](../py-spy/notebooks/compare-py-spy-top-vs-record-vs-dump.ipynb) — Side-by-side top vs record/flamegraph vs dump on the same CPU-bound target
- [Profiling mode guide](../py-spy/docs/when-to-use-py-spy-modes.md) — Short-alias-guide to choosing the right py-spy mode
- [Profile Running Process End-to-End](../py-spy/scripts/profile-running-process-end-to-end.sh) — End-to-end script: start a process, profile it, read the flamegraph
- [Profile Tiny Loop Script](../py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh) — Minimal CPU-bound loop for profiling practice with py-spy
- [CPU Speedscope Record Script](../py-spy/scripts/2026-07-10-cpu-speedscope-record.py) — Self-profiling CPU-bound workload with py-spy record and speedscope export
- [Record Output Formats Compared (July 10)](../py-spy/notes/2026-07-10-compared-py-spy-record-output-formats.md) — flamegraph, speedscope, and raw JSON compared

### Automate test environments
- [tox Primer](../tox/notes/0000-primer-tox.md) — What is tox? first-contact notes
- [Minimal tox Config](../tox/configs/tox.ini) — Single env with pytest deps
- [Lint and Test Env Config](../tox/configs/tried-lint-and-test-env.ini) — tox.ini with lint (ruff) and test (pytest) environments
- [tox env matrix](../tox/configs/2026-08-22-tox-env-matrix.toml) — tox envlist matrix with Python version constraints
- [Install tox and first env script](../tox/scripts/2026-08-05-install-tox-and-first-env.sh) — Install tox, write a minimal tox.ini, and run a first test environment

### Test APIs
- [httpie Primer](../httpie/notes/0000-primer-httpie.md) — What is HTTPie? first-contact notes
- [Installed httpie — first API request](../httpie/notes/2026-08-27-installed-httpie-first-api-request.md) — First request and why `name=value` and `name:=value` behave differently
- [httpie core syntax](../httpie/snippets/2026-08-27-httpie-core-syntax.sh) — GET/POST with query params, JSON bodies, headers, and auth in one shell snippet
- [httpie dev session config](../httpie/configs/2026-08-27-httpie-session-dev.json) — A reusable session carrying auth and headers for repeated API calls
- [Integrating httpie with jq and shell pipelines](../httpie/docs/integrating-httpie-jq-shell-pipelines.md) — Composable httpie stages: piping, field extraction, and chained API calls
- [CI-safe API smoke test](../httpie/scripts/ci-safe-api-smoke-test.sh) — httpie requests that never hang on a closed stdin, with `--check-status` failing on non-2xx
- [CI httpie wrapper](../httpie/scripts/ci-httpie-wrapper.sh) — A safe httpie wrapper for CI with `--ignore-stdin` and `--check-status`
- [Session vs Inline Auth Notebook](../httpie/notebooks/compare-session-vs-inline-auth.ipynb) — Compare session auth vs inline auth for repeated API calls
- [httpie + pytest API scaffold template](../httpie/templates/httpie-pytest-api-scaffold/) — A ready-to-fork project skeleton pairing httpie for API calls with pytest for test discovery

### Make terminal output nice
- [Rich Primer](../rich/notes/0000-primer-rich.md) — What is Rich? first-contact notes
- [Wiring Rich into a CLI status dashboard](../rich/docs/wiring-rich-into-a-cli-status-dashboard.md) — Console + Panel + Layout + Live for an updating CLI dashboard
- [First rich output snippet](../rich/snippets/2026-08-18-first-rich-output.py) — Minimal example showing Rich markup, tables, and live display in one script
- [Rich inspect live pipeline snippet](../rich/snippets/2026-08-06-rich-inspect-live-pipeline.py) — What I learned using Rich's inspect() and live display on a sample data pipeline
- [Table, Panel, Progress Script](../rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Live log tailer](../rich/scripts/live-log-tailer.py) — A live-updating log viewer that colour-codes INFO/WARN/ERROR lines using Rich panels and a rolling deque buffer
