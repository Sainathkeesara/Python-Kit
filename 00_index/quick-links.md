# Quick Links

## Foundational Concepts
- [Git Version Control Primer](../docs/concepts/git-version-control/0000-primer-git-version-control.md) — What is Git? first contact notes
- [Python Programming Fundamentals Primer](../docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md) — What are Python programming fundamentals? first contact notes
- [Python Packaging & Project Config Primer](../docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md) — What is Python packaging and project config? first contact notes
- [Software Testing Principles Primer](../docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md) — What are software testing principles? first contact notes
- [Static Type Checking & Type Hints Primer](../docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md) — What are type hints and static type checkers? first contact notes
- [Virtual Environment & Dependency Mgmt Primer](../docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md) — What are virtual environments and dependency management? first contact notes
- [Python Fundamentals Practice Script](../docs/concepts/python-programming-fundamentals/scripts/2026-07-05-practicing-fundamentals.py) — Practicing data types, control flow, functions, and comprehensions
- [Python Packaging Patterns Snippet](../docs/concepts/python-packaging-project-config/snippets/2026-07-05-packaging-patterns.py) — Reading pyproject.toml metadata and discovering packages
- [Testing Principles Practice Script](../docs/concepts/software-testing-principles/scripts/2026-07-05-testing-principles.py) — Writing isolated, parametrized tests with fixtures

## I need to...

### Set up a Python project
- [uv Primer](../uv/notes/0000-primer-uv.md) — What is uv? first contact notes
- [Install uv Script](../uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [Virtual Env Notes](../uv/notes/2026-05-24-virtual-env-uv.md) — Creating and exploring a virtual environment with uv
- [Quickstart Scaffold Notes](../uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow
- [Managed Project Config](../uv/configs/2026-07-19-uv-managed-project.toml) — Scaffolded uv-managed project with pyproject.toml, build-system, and dependencies
- [End-to-end uv Workflow Script](../uv/scripts/2026-07-19-uv-workflow.sh) — Create project, add deps, sync, run, and lock with uv
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project

### Lint and format code
- [Ruff Primer](../ruff/notes/0000-primer-ruff.md) — What is Ruff? first contact notes
- [More Ruff CLI Flags](../ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md) — Tried --show-settings, --show-files, --add-noqa, --statistics, ruff rule
- [Ruff Install Script](../py/scripts/install-and-lint.sh) — Install Ruff and lint a Python file
- [Ruff Config in pyproject.toml](../ruff/configs/ruff-pyproject.toml) — Configure Ruff inside pyproject.toml
- [Ruff Linter Config](../ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [Ruff Quickstart Notes](../ruff/notes/2026-06-03-tried-ruff-quickstart.md) — Lint, auto-fix, explore rules
- [Ruff CLI Notes](../ruff/notes/2026-06-06-cli-exploration.md) — CLI flags and output formats
- [Ruff vs Flake8 Docs](../ruff/docs/ruff-vs-flake8-comparison.md) — Rule coverage, migration gotchas, auto-fix comparison
- [First Ruff Project: What Tripped Me Up](../ruff/notes/2026-07-19-tripped-on-ruff-first-project.md) — Initial Ruff setup, CLI exploration, and the gotchas that caught me
- [Messy Example Snippet](../ruff/snippets/messy_example.py) — Deliberately broken code to test linter
- [Tried Messy Example Snippet](../ruff/snippets/tried-messy-example.py) — Another deliberately messy file with different violations
- [Minimal Standalone Ruff Config (July 5)](../ruff/configs/2026-07-05-minimal-standalone-ruff.toml) — Minimal standalone ruff.toml with select/ignore rules
- [Minimal Standalone Ruff Config (July 21)](../ruff/configs/2026-07-21-minimal-standalone-ruff.toml) — Fresh ruff.toml with select/ignore rules for a new project

### pytest
- [pytest Primer](../pytest/notes/0000-primer-pytest.md) — What is pytest? first contact notes
- [First Test Suite Notes](../pytest/notes/2026-06-08-installed-pytest-first-suite.md) — Installed pytest, ran first test suite, what tripped me up
- [pytest CLI Notes](../pytest/notes/2026-05-26-tried-pytest-cli.md) — Exploring CLI flags and output formats
- [Fixtures with conftest Notes](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md) — conftest.py with shared setup/teardown using yield fixtures
- [pytest vs unittest Docs](../pytest/docs/pytest-vs-unittest-mapping.md) — API mapping and migration patterns from unittest
- [pytest CLI Advanced Flags Notes](../pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md) — Exploring `--collect-only`, `--fixtures`, and `--co` flags
- [Run pytest with CLI Flags Script](../pytest/scripts/run-pytest-with-cli-flags.sh) — Create test file and run with -v, -k, -x, --tb=short
- [Install and Run First pytest Script](../pytest/scripts/install-and-run-first-pytest.sh) — Install pytest and run first passing test
- [Minimal pytest Config](../pytest/configs/2026-07-19-minimal-pytest-config.toml) — Minimal pytest configuration in pyproject.toml format

### pyproject.toml
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project
- [Multi-tool pyproject.toml Config](../pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config
- [First PEP 621 Config](../pyproject.toml/configs/first-pep621-config.toml) — PEP 621 build-system and project metadata with hatchling
- [First PEP 621 pyproject.toml](../pyproject.toml/configs/first-pep621-pyproject.toml) — PEP 621 pyproject.toml with hatchling build backend
- [pyproject.toml Settings Notes](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md) — Key pyproject.toml settings explained
- [Build-System Config Notes](../pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md) — Exploring the [build-system] table and how it connects to PEP 517/621
- [Minimal No Build-System Config](../pyproject.toml/configs/2026-07-05-minimal-no-build-system.toml) — Minimal pyproject.toml with project metadata and no [build-system] section

### uv.lock
- [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) — What is uv.lock? first contact notes
- [Generate First uv.lock Notes](../uv.lock/notes/2026-06-11-generated-first-uv-lock.md) — Install uv and generate first uv.lock, what's inside it
- [uv.lock Structure Notes](../uv.lock/notes/2026-05-26-uv-lock-structure.md) — Reading and understanding uv.lock internals
- [uv.lock Packages Checksums Markers Notes](../uv.lock/notes/2026-06-18-uv-lock-packages-checksums-markers.md) — Explored uv.lock: package versions, checksums, and dependency markers
- [Generate uv.lock Script](../uv.lock/scripts/generate-uv-lock.sh) — Generate a uv.lock with uv sync
- [Reproducibility Test Script](../uv.lock/scripts/tried-uv-lock-reproducibility.sh) — Test that uv.lock checksums are stable across lock commands
- [Generate from pyproject.toml Script](../uv.lock/scripts/tried-generate-from-pyproject-toml.sh) — Create pyproject.toml by hand, generate uv.lock, and inspect the output
- [Extract Direct Dependencies Script](../uv.lock/scripts/tried-extract-direct-deps.py) — Parse uv.lock and list all direct dependency entries with versions
- [Read uv.lock Snippet](../uv.lock/snippets/tried-reading-uv-lock.py) — Parse uv.lock with Python and list package names
- [Detect Conflicting Constraints Snippet](../uv.lock/snippets/tried-detect-conflicting-constraints.py) — Parse uv.lock and flag packages with conflicting version constraints
- [Exploring uv.lock Structure Notebook](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb) — Walk through uv.lock sections, hashes, and reproducibility mechanisms

### pre-commit
- [pre-commit Primer](../pre-commit/notes/0000-primer-pre-commit.md) — What is pre-commit? first contact notes
- [pre-commit config](../pre-commit/snippets/first-pre-commit-config.yaml) — My first pre-commit hook config
- [Pre-commit Multi-Hook Config](../pre-commit/configs/tried-multi-hook-config.yaml) — Ruff + mypy + trailing-whitespace hooks
- [Ruff + Mypy Hooks Config](../pre-commit/snippets/tried-ruff-mypy-config.yaml) — Minimal pre-commit config with ruff and mypy hooks
- [Install and Run Script](../pre-commit/scripts/install-and-run.sh) — Install pre-commit and run on my repo
- [Run Ruff + Trailing-Whitespace Hooks Script](../pre-commit/scripts/run-pre-commit-ruff-trailing-ws.sh) — Configure a sample project with ruff and trailing-whitespace hooks, run them once
- [Run Pre-commit on /work Notes](../pre-commit/notes/2026-05-28-run-pre-commit-on-work.md) — Running pre-commit across /work and interpreting results
- [Ruff-Only Hook Config](../pre-commit/configs/tried-first-ruff-hooks-config.yaml) — Minimal pre-commit config with just the ruff hook
- [Pre-commit CLI Exploration Notes](../pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md) — Install pre-commit, explore CLI subcommands and flags
- [Pre-commit CLI Walkthrough Notes](../pre-commit/notes/2026-06-18-pre-commit-cli-walkthrough.md) — Installed pre-commit, walked through install/run/sample-config/validate-config/autoupdate
- [Install and Run Lint + Typecheck Notes](../pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md) — Install pre-commit, run with ruff linting and mypy type check on a sample repo

### Audit dependencies
- [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first contact notes
- [Followed pip-audit Quickstart Notes](../pip-audit/notes/2026-07-17-followed-pip-audit-quickstart.md) — Quickstart walkthrough: exit codes, dry runs, and irrelevant-report gotchas
- [Scan Project Script](../pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [Parse pip-audit JSON CVEs (July 13)](../pip-audit/snippets/2026-07-13-parse-pip-audit-json-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [Parse pip-audit JSON CVEs (July 10)](../pip-audit/snippets/2026-07-10-parse-pip-audit-json-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [CVE Findings Snippet](../pip-audit/snippets/list-cve-findings.py) — Parse pip-audit JSON and list CVE findings with severity
- [pip-audit Ignore Config](../pip-audit/configs/pip-audit-ignore.toml) — Configure pip-audit ignore list for reviewed CVEs
- [Parse CVE Findings Snippet](../pip-audit/snippets/tried-list-cves.py) — Parse pip-audit JSON and list CVE findings with severity and package info
- [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first contact notes
- [Pipdeptree Patterns I Use](../pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md) — --warn silence, --freeze, --exclude, JSON output tricks
- [Parse JSON Snippet](../pipdeptree/snippets/parse-pipdeptree-json.py) — Parse pipdeptree JSON output and list leaf packages
- [Reverse Dependency Snippet](../pipdeptree/snippets/find-reverse-deps.py) — Use `--reverse` to find which packages depend on a given package
- [List Package Dependencies Script](../pipdeptree/scripts/list-package-deps.py) — Use pipdeptree as a library to list all deps of a named package
- [Dev Dependencies Config](../pipdeptree/configs/2026-07-19-dev-dependencies-pipdeptree.toml) — pyproject.toml excerpt declaring dev dependencies for dependency analysis

### rich
- [Rich Primer](../rich/notes/0000-primer-rich.md) — What is Rich? first contact notes
- [Console API Notes](../rich/notes/2026-06-04-tried-rich-console-api.md) — Trying print, print_json, rule, log
- [Console API Renderables Notes](../rich/notes/2026-06-17-explored-rich-console-api-renderables.md) — Renderables, styles, and output modes
- [Table, Panel, Progress Script](../rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Styled Output Snippet](../rich/snippets/tried-rich-styled-output.py) — First styled terminal output with rich print

### mypy
- [mypy Primer](../mypy/notes/0000-primer-mypy.md) — What is mypy? first contact notes
- [First mypy Run Notes](../mypy/notes/2026-06-04-first-mypy-run.md) — Annotated a function, fixed type errors, tried reveal_type
- [First Type Check Script](../mypy/scripts/tried-mypy-first-check.py) — Intentionally broken file to run mypy against
- [CLI Flags Notes](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md) — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [Quickstart for Existing Projects](../mypy/notes/2026-05-29-tried-mypy-quickstart.md) — Running mypy on an existing codebase, what tripped me out
- [Strict Mode Config](../mypy/configs/tried-strict-mypy-config.toml) — Minimal mypy config with incremental strict mode and stub setup
- [Type Error Detection Snippet](../mypy/snippets/tried-mypy-type-errors.py) — Intentional type errors for mypy to catch
- [Typed Functions Validate Snippet](../mypy/snippets/typed-functions-validate.py) — Small typed Python module with annotated functions
- [Validating Typed Function Snippet](../mypy/snippets/tried-validating-typed-function.py) — Small typed function with annotations to validate with mypy
- [Typed Small Module Snippet](../mypy/snippets/2026-07-19-typed-small-module.py) — Small typed Python module with annotated functions and classes
- [Followed mypy Quickstart Notes](../mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Gradual typing, strict mode, what tripped me up
- [Official mypy Quickstart Notes](../mypy/notes/2026-06-08-tried-mypy-official-quickstart.md) — Followed official docs: gradual typing, strict mode, reveal_type, what tripped me up
- [Minimal mypy.ini Config](../mypy/configs/tried-minimal-mypy-config.ini) — Strict, disallow-untyped-defs, ignore-missing-imports
- [Strict Disallow Ignore Config](../mypy/configs/tried-strict-disallow-ignore-config.ini) — Minimal mypy.ini with strict mode, type annotation enforcement, and import allowance

### Ty
- [Ty Primer](../ty/notes/0000-primer-ty.md) — What is Ty? first contact notes
- [Ty Quickstart Notes](../ty/notes/2026-06-05-tried-ty-quickstart.md) — Following the official quickstart, first check, what tripped me up
- [First Ty Markdown Render](../ty/notes/2026-06-10-first-ty-markdown-render.md) — Install Ty and render my first markdown file in the terminal
- [Run Ty on a Codebase Snippet](../ty/snippets/run-ty-on-codebase.py) — Minimal example running Ty on a Python module
- [Compare Ty vs Mypy Notes](../ty/notes/2026-05-27-compare-ty-vs-mypy.md) — Comparing ty vs mypy output on the same codebase
- [Ty Config](../ty/configs/tried-ty-config.toml) — Ty configuration file with enabled error codes
- [Ty Markdown CSS](../ty/configs/tried-ty-markdown-css.css) — Custom CSS styling for Ty markdown rendering
- [Ty Pipeline Script](../ty/scripts/tried-ty-pipeline.sh) — Pipe markdown through ty and capture formatted output
- [CLI Flags and Formats Notes](../ty/notes/2026-06-16-explored-ty-cli-flags.md) — Explored Ty CLI flags, output formats, compared with mypy options
- [Ty vs Mypy Comparison Snippet](../ty/snippets/tried-ty-vs-mypy.py) — Compare Ty and mypy output on the same typed code
- [First Ty Type Check Notes](../ty/notes/2026-06-18-first-ty-type-check.md) — Installed Ty and ran first type check on a sample Python file

### Build a CLI
- [Typer Primer](../typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [First Typer Hello-World Notes](../typer/notes/2026-06-10-first-typer-hello-world.md) — Install Typer and run my first CLI hello-world app
- [Minimal CLI Demo](../typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Calculator Script](../typer/scripts/tried-typer-calculator.py) — Minimal Typer CLI calculator: add, sub, mul, div
- [First Typer CLI App Snippet](../typer/snippets/tried-first-typer-cli-app.py) — Minimal Typer CLI app with argument and option
- [Typer CLI Option + Subcommand Snippet](../typer/snippets/2026-07-05-typer-cli-option-and-subcommand.py) — Typer CLI with one option and two subcommands

### py-spy
- [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first contact notes
- [Profile Tiny Loop Script](../py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh) — Minimal CPU-bound loop for profiling practice with py-spy
- [Record Output Formats Compared (July 10)](../py-spy/notes/2026-07-10-compared-py-spy-record-output-formats.md) — flamegraph, speedscope, and raw JSON compared
- [Record Output Formats Compared (July 8)](../py-spy/notes/2026-07-08-compared-py-spy-record-output-formats.md) — flamegraph, speedscope, and raw JSON compared
- [Record Output Formats Compared (June)](../py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md) — Compared flamegraph SVG, speedscope JSON, and raw JSON formats
- [CPU Speedscope Record Script (July 10)](../py-spy/scripts/2026-07-10-cpu-speedscope-record.py) — Self-profiling CPU-bound workload with py-spy record and speedscope export
- [CPU Speedscope Record Script (July 8)](../py-spy/scripts/2026-07-08-cpu-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export
- [CPU Speedscope Record Script (June)](../py-spy/scripts/tried-cpu-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export
- [Install and Record Flamegraph](../py-spy/scripts/tried-install-and-record-flamegraph.sh) — Install py-spy and profile CPU-bound script to flamegraph SVG
- [Sampling Target Script](../py-spy/scripts/tried-py-spy-sampling.py) — Python script with CPU-bound functions for py-spy to sample
- [CLI Subcommand Notes](../py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md) — Exploring record, top, and flamegraph subcommands
- [Record & Flamegraph Script](../py-spy/scripts/tried-py-spy-record-flamegraph.sh) — Profile a CPU-bound script and output a flamegraph SVG
- [Profile Tiny Loop Script](../py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh) — Profile a CPU-bound loop with py-spy record and flamegraph output
- [CPU-Bound Simulation Snippet](../py-spy/snippets/tried-cpu-bound-simulation.py) — Minimal script for py-spy profiling practice
- [Top Session Tripped Me Up](../py-spy/notes/2026-06-08-tripped-on-py-spy-top-session.md) — First py-spy top session: permission issues, columns, key flags
- [Py-spy Quickstart Notes](../py-spy/notes/2026-06-10-followed-py-spy-quickstart.md) — Followed official quickstart: profile a sample app, flamegraph, what tripped me up
- [Speedscope Record Script](../py-spy/scripts/tried-py-spy-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export

### tox
- [tox Primer](../tox/notes/0000-primer-tox.md) — What is tox? first contact notes
- [Minimal tox Config](../tox/configs/tox.ini) — Single env with pytest deps
- [Lint and Test Env Config](../tox/configs/tried-lint-and-test-env.ini) — tox.ini with lint (ruff) and test (pytest) environments
- [First tox CLI Run Notes](../tox/notes/2026-05-31-tox-cli-first-run.md) — env list, -e flag, passing args through
- [Followed tox Quickstart Notes](../tox/notes/2026-06-11-followed-tox-quickstart.md) — Multi-env setup, what tripped me up
- [Minimal tox Run Script](../tox/scripts/tried-minimal-tox-run.sh) — Create tox.ini, run tox end-to-end with a test env

### Test APIs
- [httpie Primer](../httpie/notes/0000-primer-httpie.md) — What is HTTPie? first contact notes
- [Install and Test Script](../httpie/scripts/install_and_test_httpie.sh) — Install httpie with pipx, make GET/POST requests to JSONPlaceholder
- [Followed httpie Quickstart](../httpie/notes/2026-07-19-followed-httpie-quickstart.md) — Quickstart walkthrough: sessions, headers, JSON handling gotchas
- [httpie Request Workflow Script](../httpie/scripts/2026-07-19-httpie-request-workflow.sh) — Workflow covering GET, POST, auth, and file upload patterns
- [httpie vs curl Notes](../httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, ergonomics compared
- [HTTPie Defaults Config](../httpie/configs/2026-07-19-httpie-defaults.json) — Default request options for HTTPie CLI sessions
