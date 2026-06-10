# Topics

## httpie
- [note] httpie/notes/0000-primer-httpie.md — First-contact notes for HTTPie
- [note] httpie/notes/2026-05-30-compare-httpie-vs-curl.md — Same API calls, different ergonomics
- [note] httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md — What caught me off guard on my first httpie request
- [script] httpie/scripts/install_and_test_httpie.sh — Install httpie, make GET/POST requests to JSONPlaceholder

## mypy
- [note] mypy/notes/0000-primer-mypy.md — First-contact notes for mypy
- [note] mypy/notes/2026-05-28-tried-mypy-cli-flags.md — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [note] mypy/notes/2026-05-29-tried-mypy-quickstart.md — Running mypy on an existing codebase, what tripped me up
- [note] mypy/notes/2026-06-04-first-mypy-run.md — Annotated a function, fixed type errors, tried reveal_type
- [note] mypy/notes/2026-06-05-mypy-first-check-tripped-me-up.md — What caught me off guard on my first mypy check
- [script] mypy/scripts/tried-mypy-first-check.py — First mypy check script with intentional errors
- [config] mypy/configs/tried-strict-mypy-config.toml — Minimal mypy config with incremental strict mode and stub setup
- [snippet] mypy/snippets/tried-mypy-type-errors.py — Intentional type errors for mypy to catch

## pip-audit
- [note] pip-audit/notes/0000-primer-pip-audit.md — First-contact notes for pip-audit
- [note] pip-audit/notes/2026-05-26-pip-audit-findings.md — First scan results and observations
- [note] pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md — Install pip-audit and run first audit, what tripped me up
- [script] pip-audit/scripts/scan-project.sh — Scan project for vulnerabilities with pip-audit
- [script] pip-audit/scripts/scan-and-parse-json.sh — Scan requirements.txt and parse JSON output with jq
- [script] pip-audit/scripts/2026-06-09-audit-and-parse-json.sh — Run pip-audit on a requirements.txt and parse JSON output
- [config] pip-audit/configs/pip-audit-ignore.toml — Configure pip-audit ignore list for reviewed CVEs

## pipdeptree
- [note] pipdeptree/notes/0000-primer-pipdeptree.md — First-contact notes for pipdeptree
- [note] pipdeptree/notes/2026-05-29-format-json-deps.md — Formatting output as JSON, identifying top-level vs transitive deps
- [note] pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [note] pipdeptree/notes/2026-06-07-tripped-on-pipdeptree-filtering.md — Filter by package, JSON format quirks, and handling missing deps
- [note] pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md — Following official quickstart: visualize deps, detect cycles, confusions
- [script] pipdeptree/scripts/install-and-inspect-deps.sh — Install pipdeptree and inspect dependency tree
- [snippet] pipdeptree/snippets/parse-pipdeptree-json.py — Parse pipdeptree JSON output and list leaf packages

## pre-commit
- [note] pre-commit/notes/0000-primer-pre-commit.md — First-contact notes for pre-commit hooks
- [note] pre-commit/notes/2026-05-28-run-pre-commit-on-work.md — Running pre-commit across /work and interpreting results
- [script] pre-commit/scripts/install-and-run.sh — Install pre-commit and run on repo
- [config] pre-commit/configs/tried-first-ruff-hooks-config.yaml — Minimal pre-commit config with just the ruff hook
- [config] pre-commit/configs/tried-multi-hook-config.yaml — Ruff + mypy + trailing-whitespace hooks
- [snippet] pre-commit/snippets/first-pre-commit-config.yaml — First pre-commit hook config

## py (Ruff / Python tooling)
- [note] py/notes/0000-primer-py.md — What is Ruff? first-contact notes
- [note] py/notes/0000-primer-pytest.md — What is pytest? first-contact notes
- [script] py/scripts/install-and-lint.sh — Install Ruff and lint a Python file
- [config] py/configs/ruff-pyproject.toml — Configure Ruff inside pyproject.toml

## py-spy
- [note] py-spy/notes/0000-primer-py-spy.md — First-contact notes for py-spy
- [note] py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md — Exploring record, top, and flamegraph subcommands
- [script] py-spy/scripts/tried-py-spy-record-flamegraph.sh — Profile a CPU-bound script and output a flamegraph SVG
- [script] py-spy/scripts/tried-py-spy-sampling.py — Python script with CPU-bound functions for py-spy to sample
- [snippet] py-spy/snippets/tried-cpu-bound-simulation.py — Minimal script for py-spy profiling practice

## pyproject.toml
- [note] pyproject.toml/notes/0000-primer-pyproject.toml.md — First-contact notes for pyproject.toml
- [note] pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md — Key pyproject.toml settings explained
- [config] pyproject.toml/configs/minimal-pyproject.toml — Minimal pyproject.toml for a Python project
- [config] pyproject.toml/configs/multi-tool-pyproject.toml — Combined ruff, pytest, mypy config

## pytest
- [note] pytest/notes/2026-05-26-tried-pytest-cli.md — Exploring CLI flags and output formats
- [note] pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md — conftest.py with shared setup/teardown using yield fixtures
- [script] pytest/scripts/test_parametrized.py — Parametrized tests with @pytest.mark.parametrize
- [snippet] pytest/snippets/test_first_test.py — Basic test with assertions
- [doc] pytest/docs/pytest-vs-unittest-mapping.md — API mapping and migration patterns from unittest

## rich
- [note] rich/notes/0000-primer-rich.md — First-contact notes for rich
- [note] rich/notes/2026-05-27-tried-rich-themes-and-markdown.md — Exploring themes and markdown rendering
- [note] rich/notes/2026-05-28-exploring-renderables.md — Trying tables, panels, layouts, markup syntax
- [note] rich/notes/2026-06-03-tried-rich-quickstart-tables-panels.md — Following official quickstart: Console, Table, Panel, Layout
- [note] rich/notes/2026-06-04-tried-rich-console-api.md — Trying print, print_json, rule, log
- [script] rich/scripts/first-table-panel-progress.py — First rich script with table, panel, and progress bar
- [snippet] rich/snippets/first-rich-logger.py — Minimal rich logging handler setup
- [snippet] rich/snippets/tried-live-data-viewer.py — Layout + Table + Live display in a simulated process monitor
- [snippet] rich/snippets/tried-progress-spinner.py — Interactive status spinner for simulated long-running task
- [snippet] rich/snippets/tried-rich-progress-bar.py — First try at rich progress bar

## ruff
- [note] ruff/notes/0000-primer-ruff.md — First-contact notes for Ruff
- [note] ruff/notes/2026-06-03-tried-ruff-quickstart.md — Lint, auto-fix, explore rules
- [note] ruff/notes/2026-06-06-cli-exploration.md — CLI flags, output formats for check and format commands
- [config] ruff/configs/ruff-linter-settings.toml — Minimal ruff config with rule selection, ignores, excludes
- [doc] ruff/docs/ruff-vs-flake8-comparison.md — Rule coverage, migration gotchas, auto-fix comparison
- [snippet] ruff/snippets/messy_example.py — Deliberately messy code to test linter

## tox
- [note] tox/notes/0000-primer-tox.md — First-contact notes for tox
- [note] tox/notes/2026-05-31-tox-cli-first-run.md — env list, -e flag, passing args through
- [config] tox/configs/tox.ini — Single env with pytest deps

## ty
- [note] ty/notes/0000-primer-ty.md — First-contact notes for ty
- [note] ty/notes/2026-05-27-compare-ty-vs-mypy.md — Comparing ty vs mypy output on the same codebase
- [note] ty/notes/2026-06-05-tried-ty-quickstart.md — Following the official quickstart, first check, what tripped me up
- [config] ty/configs/tried-ty-config.toml — Ty configuration file with enabled error codes
- [config] ty/configs/tried-ty-markdown-css.css — Custom CSS styling for Ty markdown rendering
- [script] ty/scripts/tried-ty-pipeline.sh — Pipe markdown through ty and capture formatted output
- [snippet] ty/snippets/run-ty-on-codebase.py — Minimal example running ty on a Python module

## typer
- [note] typer/notes/0000-primer-typer.md — First-contact notes for typer
- [note] typer/notes/2026-05-29-typer-quickstart-notes.md — What tripped me up following the quickstart
- [script] typer/scripts/tried-typer-calculator.py — Minimal Typer CLI calculator: add, sub, mul, div
- [script] typer/scripts/typer_cli_demo.py — CLI with positional and optional arguments

## uv
- [note] uv/notes/0000-primer-uv.md — What is uv? first-contact notes
- [note] uv/notes/2026-05-24-virtual-env-uv.md — Creating and exploring a virtual environment with uv
- [note] uv/notes/2026-05-26-cli-commands-beyond-basics.md — Exploring uv CLI commands beyond the basics
- [note] uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md — Following uv init, add, run workflow
- [script] uv/scripts/install-and-first-command.sh — Install uv and run first command
- [script] uv/scripts/hello-with-dep.py — PEP 723 inline metadata, uv run with requests
- [config] uv/configs/2026-05-26-uv-pyproject-settings.toml — Configure uv settings in pyproject.toml
- [snippet] uv/snippets/run-with-uv.py — Minimal script to run with uv run
- [doc] uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md — Command mapping and migration cheat-sheet

## uv.lock
- [note] uv.lock/notes/0000-primer-uv.lock.md — First-contact notes for uv.lock
- [note] uv.lock/notes/2026-05-26-uv-lock-structure.md — Reading and understanding uv.lock internals
- [script] uv.lock/scripts/generate-uv-lock.sh — Generate a uv.lock file with uv sync
- [script] uv.lock/scripts/tried-uv-lock-reproducibility.sh — Test that uv.lock checksums are stable across lock commands
