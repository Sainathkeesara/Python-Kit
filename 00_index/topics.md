# Topics

## Concepts

- [primer] docs/concepts/git-version-control/0000-primer-git-version-control.md — What is Git? first contact notes
- [primer] docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md — Variables, data types, functions, loops, and imports as the vocabulary of Python
- [primer] docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md — What is Python packaging and project config? first contact notes
- [primer] docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md — What are software testing principles? first contact notes
- [primer] docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md — What are type hints and static type checkers? first contact notes
- [primer] docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md — What are virtual environments and dependency management? first contact notes
- [doc] docs/repository-structure.md — Describes the directory layout of Python-Kit

## httpie

- [note] httpie/notes/0000-primer-httpie.md — First-contact notes for HTTPie
- [note] httpie/notes/2026-05-30-compare-httpie-vs-curl.md — Same API calls, different ergonomics compared to curl
- [note] httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md — What caught me off guard on my first httpie request
- [note] httpie/notes/2026-06-10-first-httpie-request.md — Install httpie, run my first GET with JSON and POST with form data
- [script] httpie/scripts/install_and_test_httpie.sh — Install httpie with pipx, make GET/POST requests to JSONPlaceholder
- [snippet] httpie/snippets/tried-httpie-get-post-workflow.py — Python script automating httpie for a simple GET/POST workflow

## mypy

- [note] mypy/notes/0000-primer-mypy.md — First-contact notes for mypy
- [note] mypy/notes/2026-05-28-tried-mypy-cli-flags.md — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [note] mypy/notes/2026-05-29-tried-mypy-quickstart.md — Running mypy on an existing codebase, what tripped me up
- [note] mypy/notes/2026-06-04-first-mypy-run.md — Annotated a function, fixed type errors, tried reveal_type
- [note] mypy/notes/2026-06-05-mypy-first-check-tripped-me-up.md — What caught me off guard on my first mypy check
- [note] mypy/notes/2026-06-12-followed-mypy-quickstart.md — Using gradual typing and strict mode, where I got stuck
- [script] mypy/scripts/tried-mypy-first-check.py — First mypy check script with intentional errors
- [config] mypy/configs/tried-strict-mypy-config.toml — Minimal mypy config with incremental strict mode and stub setup
- [config] mypy/configs/tried-minimal-mypy-config.ini — Three flags from the official quickstart, strict mode with per-module overrides
- [snippet] mypy/snippets/tried-mypy-type-errors.py — Intentional type errors for mypy to catch
- [snippet] mypy/snippets/tried-validating-typed-function.py — Small typed function with annotations to validate with mypy
- [snippet] mypy/snippets/typed-functions-validate.py — Small typed Python module with annotated functions

## pip-audit

- [note] pip-audit/notes/0000-primer-pip-audit.md — First-contact notes for pip-audit
- [note] pip-audit/notes/2026-05-26-pip-audit-findings.md — First scan results and observations
- [note] pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md — Install pip-audit and run first audit, what tripped me up
- [script] pip-audit/scripts/scan-project.sh — Scan project for vulnerabilities with pip-audit
- [script] pip-audit/scripts/scan-and-parse-json.sh — Scan requirements.txt and parse JSON output with jq
- [script] pip-audit/scripts/2026-06-09-audit-and-parse-json.sh — Run pip-audit on a requirements.txt and parse JSON output
- [config] pip-audit/configs/pip-audit-ignore.toml — Configure pip-audit ignore list for reviewed CVEs
- [snippet] pip-audit/snippets/list-cve-findings.py — Parse pip-audit JSON and list CVE findings with severity

## pipdeptree

- [note] pipdeptree/notes/0000-primer-pipdeptree.md — First-contact notes for pipdeptree
- [note] pipdeptree/notes/2026-05-29-format-json-deps.md — Formatting output as JSON, identifying top-level vs transitive deps
- [note] pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [note] pipdeptree/notes/2026-06-07-tripped-on-pipdeptree-filtering.md — Filter by package, JSON format quirks, and handling missing deps
- [note] pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md — Following official quickstart: visualize deps, detect cycles, confusions
- [note] pipdeptree/notes/2026-06-13-common-cli-patterns.md — CLI patterns I figured out on my own
- [note] pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md — --warn silence, --freeze, --exclude, JSON output tricks
- [script] pipdeptree/scripts/install-and-inspect-deps.sh — Install pipdeptree and inspect dependency tree
- [snippet] pipdeptree/snippets/check-package-deps.py — Check one package and print its dependency chain
- [snippet] pipdeptree/snippets/find-reverse-deps.py — Use --reverse to find which packages depend on a given package
- [snippet] pipdeptree/snippets/parse-pipdeptree-json.py — Parse pipdeptree JSON output and list leaf packages
- [snippet] pipdeptree/snippets/tried-check-package-deps.py — Minimal script to look up a package in pipdeptree JSON and walk its dependency chain
- [snippet] pipdeptree/snippets/tried-identify-leaf-packages.py — Identify leaf (top-level) packages from pipdeptree JSON

## pre-commit

- [note] pre-commit/notes/0000-primer-pre-commit.md — First-contact notes for pre-commit hooks
- [note] pre-commit/notes/2026-05-28-run-pre-commit-on-work.md — Running pre-commit across /work and interpreting results
- [note] pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md — Install pre-commit, explore CLI subcommands and flags
- [note] pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md — Install pre-commit, run with ruff linting and mypy type check on a sample repo
- [note] pre-commit/notes/2026-06-18-pre-commit-cli-walkthrough.md — Installed pre-commit, walked through install/run/sample-config/validate-config/autoupdate
- [script] pre-commit/scripts/install-and-run.sh — Install pre-commit and run on repo
- [config] pre-commit/configs/tried-first-ruff-hooks-config.yaml — Minimal pre-commit config with just the ruff hook
- [config] pre-commit/configs/tried-multi-hook-config.yaml — Ruff + mypy + trailing-whitespace hooks
- [snippet] pre-commit/snippets/first-pre-commit-config.yaml — First pre-commit hook config
- [snippet] pre-commit/snippets/tried-ruff-mypy-config.yaml — Minimal pre-commit config with ruff and mypy hooks

## py (Ruff / Python tooling)

- [note] py/notes/0000-primer-py.md — What is Ruff? first-contact notes
- [script] py/scripts/install-and-lint.sh — Install Ruff and lint a Python file

## py-spy

- [note] py-spy/notes/0000-primer-py-spy.md — First-contact notes for py-spy
- [note] py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md — Exploring record, top, and flamegraph subcommands
- [note] py-spy/notes/2026-06-08-tried-py-spy-top-session.md — Getting started with py-spy top: permissions and flags
- [note] py-spy/notes/2026-06-08-tripped-on-py-spy-top-session.md — First py-spy top session: permission issues, columns, key flags
- [note] py-spy/notes/2026-06-10-followed-py-spy-quickstart.md — Followed official quickstart: profile a sample app, flamegraph, what tripped me up
- [note] py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md — Compared flamegraph SVG, speedscope JSON, and raw JSON formats
- [note] py-spy/notes/2026-06-13-my-py-spy-workflow.md — Documented record, flamegraph, top modes with gotchas
- [script] py-spy/scripts/tried-py-spy-record-flamegraph.sh — Profile a CPU-bound script and output a flamegraph SVG
- [script] py-spy/scripts/tried-py-spy-sampling.py — Python script with CPU-bound functions for py-spy to sample
- [script] py-spy/scripts/tried-py-spy-speedscope-record.py — CPU-bound workload with py-spy record and speedscope JSON export
- [script] py-spy/scripts/tried-install-and-record-flamegraph.sh — Install py-spy and profile CPU-bound script to flamegraph SVG
- [snippet] py-spy/snippets/tried-cpu-bound-simulation.py — Minimal script for py-spy profiling practice
- [snippet] py-spy/snippets/tried-profile-running-process.py — Profile a running Python process and export flamegraph SVG

## pyproject.toml

- [note] pyproject.toml/notes/0000-primer-pyproject.toml.md — First-contact notes for pyproject.toml
- [note] pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md — Key pyproject.toml settings explained
- [note] pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md — Exploring the [build-system] table and how it connects to PEP 517/621
- [config] pyproject.toml/configs/first-pep621-config.toml — PEP 621 build-system and project metadata with hatchling
- [config] pyproject.toml/configs/first-pep621-pyproject.toml — PEP 621 pyproject.toml with hatchling build backend
- [config] pyproject.toml/configs/minimal-pyproject.toml — Minimal pyproject.toml for a Python project
- [config] pyproject.toml/configs/multi-tool-pyproject.toml — Combined ruff, pytest, mypy config

## pytest

- [note] pytest/notes/0000-primer-pytest.md — First-contact notes for pytest
- [note] pytest/notes/2026-05-26-tried-pytest-cli.md — Exploring CLI flags and output formats
- [note] pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md — conftest.py with shared setup/teardown using yield fixtures
- [note] pytest/notes/2026-06-08-installed-pytest-first-suite.md — Installed pytest, ran first test suite, what tripped me up
- [note] pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md — Exploring --collect-only, --fixtures, and --co flags
- [doc] pytest/docs/pytest-vs-unittest-mapping.md — API mapping and migration patterns from unittest
- [script] pytest/scripts/install-and-run-first-pytest.sh — Install pytest and run first passing test
- [script] pytest/scripts/run-pytest-with-cli-flags.sh — Create test file and run with -v, -k, -x, --tb=short
- [script] pytest/scripts/test_parametrized.py — Parametrized tests with @pytest.mark.parametrize
- [snippet] pytest/snippets/test_first_test.py — Basic test with assertions
- [snippet] pytest/snippets/three_basic_tests.py — assert, exception, parameterized tests

## rich

- [note] rich/notes/0000-primer-rich.md — First-contact notes for rich
- [note] rich/notes/2026-05-27-tried-rich-themes-and-markdown.md — Exploring themes and markdown rendering
- [note] rich/notes/2026-05-28-exploring-renderables.md — Trying tables, panels, layouts, markup syntax
- [note] rich/notes/2026-06-03-tried-rich-quickstart-tables-panels.md — Following official quickstart: Console, Table, Panel, Layout
- [note] rich/notes/2026-06-04-tried-rich-console-api.md — Trying print, print_json, rule, log
- [note] rich/notes/2026-06-09-tried-rich-cli.md — Exploring the rich CLI and console features
- [note] rich/notes/2026-06-17-explored-rich-console-api-renderables.md — Renderables, styles, and output modes
- [script] rich/scripts/first-table-panel-progress.py — First rich script with table, panel, and progress bar
- [snippet] rich/snippets/first-rich-logger.py — Minimal rich logging handler setup
- [snippet] rich/snippets/tried-live-data-viewer.py — Layout + Table + Live display in a simulated process monitor
- [snippet] rich/snippets/tried-progress-spinner.py — Interactive status spinner for simulated long-running task
- [snippet] rich/snippets/tried-rich-console-panel-table.py — Minimal Console script with text styling, panel, and table
- [snippet] rich/snippets/tried-rich-progress-bar.py — First try at rich progress bar
- [snippet] rich/snippets/tried-rich-styled-output.py — First styled terminal output with rich print

## ruff

- [note] ruff/notes/0000-primer-ruff.md — First-contact notes for Ruff
- [note] ruff/notes/2026-06-03-tried-ruff-quickstart.md — Lint, auto-fix, explore rules
- [note] ruff/notes/2026-06-06-cli-exploration.md — CLI flags, output formats for check and format commands
- [note] ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md — --show-settings, --show-files, --add-noqa, --statistics, ruff rule
- [config] ruff/configs/ruff-linter-settings.toml — Minimal ruff config with rule selection, ignores, excludes
- [config] ruff/configs/ruff-pyproject.toml — Configure Ruff inside pyproject.toml
- [doc] ruff/docs/ruff-vs-flake8-comparison.md — Rule coverage, migration gotchas, auto-fix comparison
- [snippet] ruff/snippets/messy_example.py — Deliberately messy code to test linter
- [snippet] ruff/snippets/tried-messy-example.py — Another deliberately messy file with different violations

## tox

- [note] tox/notes/0000-primer-tox.md — First-contact notes for tox
- [note] tox/notes/2026-05-31-tox-cli-first-run.md — env list, -e flag, passing args through
- [note] tox/notes/2026-06-08-first-tox-run-tripped-me-up.md — First tox run: env creation, isolated installs, slow feedback
- [note] tox/notes/2026-06-08-tox-quickstart.md — Followed the official quickstart and set up a first env
- [note] tox/notes/2026-06-11-followed-tox-quickstart.md — Multi-env setup, what tripped me up
- [config] tox/configs/tox.ini — Single env with pytest deps
- [config] tox/configs/tried-lint-and-test-env.ini — tox.ini with lint (ruff) and test (pytest) environments
- [script] tox/scripts/tried-minimal-tox-run.sh — Create tox.ini, run tox end-to-end with a test env

## ty

- [note] ty/notes/0000-primer-ty.md — First-contact notes for ty
- [note] ty/notes/2026-05-27-compare-ty-vs-mypy.md — Comparing ty vs mypy output on the same codebase
- [note] ty/notes/2026-06-05-tried-ty-quickstart.md — Following the official quickstart, first check, what tripped me up
- [note] ty/notes/2026-06-10-first-ty-markdown-render.md — Install Ty and render my first markdown file in the terminal
- [note] ty/notes/2026-06-16-explored-ty-cli-flags.md — Explored Ty CLI flags, output formats, compared with mypy options
- [note] ty/notes/2026-06-18-first-ty-type-check.md — Installed Ty and ran first type check on a sample Python file
- [config] ty/configs/tried-ty-config.toml — Ty configuration file with enabled error codes
- [config] ty/configs/tried-ty-markdown-css.css — Custom CSS styling for Ty markdown rendering
- [script] ty/scripts/tried-ty-pipeline.sh — Pipe markdown through ty and capture formatted output
- [snippet] ty/snippets/run-ty-on-codebase.py — Minimal example running Ty on a Python module
- [snippet] ty/snippets/tried-ty-vs-mypy.py — Compare Ty and mypy output on the same typed code

## typer

- [note] typer/notes/0000-primer-typer.md — First-contact notes for typer
- [note] typer/notes/2026-05-29-typer-quickstart-notes.md — What tripped me up following the quickstart
- [note] typer/notes/2026-06-10-first-typer-hello-world.md — Install Typer and run my first CLI hello-world app
- [script] typer/scripts/tried-typer-calculator.py — Minimal Typer CLI calculator: add, sub, mul, div
- [script] typer/scripts/typer_cli_demo.py — CLI with positional and optional arguments
- [snippet] typer/snippets/tried-first-typer-cli-app.py — Minimal Typer CLI app with argument and option

## uv

- [note] uv/notes/0000-primer-uv.md — What is uv? first-contact notes
- [note] uv/notes/2026-05-24-virtual-env-uv.md — Creating and exploring a virtual environment with uv
- [note] uv/notes/2026-05-26-cli-commands-beyond-basics.md — Exploring uv CLI commands beyond the basics
- [note] uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md — Following uv init, add, run workflow
- [note] uv/notes/2026-06-10-installed-uv-first-command.md — Install uv, ran --version, --help, and uv run on a script
- [note] uv/notes/2026-06-16-explored-uv-cli-help-and-format.md — Explored uv CLI subcommands, help topics, and output formats
- [script] uv/scripts/install-and-first-command.sh — Install uv and run first command
- [script] uv/scripts/hello-with-dep.py — PEP 723 inline metadata, uv run with requests
- [script] uv/scripts/tried-bootstrap-uv-script.sh — Bootstrap a one-file Python script with uv run and external deps
- [config] uv/configs/2026-05-26-uv-pyproject-settings.toml — Configure uv settings in pyproject.toml
- [snippet] uv/snippets/run-with-uv.py — Minimal script to run with uv run
- [doc] uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md — Command mapping and migration cheat-sheet

## uv.lock

- [note] uv.lock/notes/0000-primer-uv.lock.md — First-contact notes for uv.lock
- [note] uv.lock/notes/2026-05-26-uv-lock-structure.md — Reading and understanding uv.lock internals
- [note] uv.lock/notes/2026-06-11-generated-first-uv-lock.md — Install uv and generate first uv.lock, what's inside it
- [note] uv.lock/notes/2026-06-18-uv-lock-packages-checksums-markers.md — Explored uv.lock: package versions, checksums, and dependency markers
- [script] uv.lock/scripts/generate-uv-lock.sh — Generate a uv.lock file with uv sync
- [script] uv.lock/scripts/tried-extract-direct-deps.py — Parse uv.lock and list all direct dependency entries with versions
- [script] uv.lock/scripts/tried-generate-from-pyproject-toml.sh — Create pyproject.toml by hand, generate uv.lock, and inspect the output
- [script] uv.lock/scripts/tried-uv-lock-reproducibility.sh — Test that uv.lock checksums are stable across lock commands
- [snippet] uv.lock/snippets/tried-detect-conflicting-constraints.py — Parse uv.lock and flag packages with conflicting version constraints
- [snippet] uv.lock/snippets/tried-reading-uv-lock.py — Parse uv.lock with Python and list package names
- [notebook] uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb — Walk through uv.lock sections, hashes, and reproducibility mechanisms
