# Quick Links

## uv
- [uv Primer](../uv/notes/0000-primer-uv.md) — What is uv? first contact notes
- [Install uv Script](../uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [Virtual Env Notes](../uv/notes/2026-05-24-virtual-env-uv.md) — Creating and exploring a virtual environment with uv
- [Quickstart Scaffold Notes](../uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow
- [Hello with Dep Script](../uv/scripts/hello-with-dep.py) — PEP 723 inline metadata, uv run with requests
- [Run with uv Snippet](../uv/snippets/run-with-uv.py) — Minimal script to run with uv run
- [uv pyproject.toml Config](../uv/configs/2026-05-26-uv-pyproject-settings.toml) — Configure uv settings in pyproject.toml
- [CLI Beyond Basics](../uv/notes/2026-05-26-cli-commands-beyond-basics.md) — Exploring uv CLI commands beyond basics
- [uv vs pip Cheat Sheet](../uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md) — Command mapping and migration cheat-sheet
- [Install and First Command Notes](../uv/notes/2026-06-10-installed-uv-first-command.md) — Install uv, ran --version, --help, and uv run on a script
- [Bootstrap uv Script](../uv/scripts/tried-bootstrap-uv-script.sh) — Bootstrap a one-file Python script with uv run and external deps
- [CLI Help and Format Notes](../uv/notes/2026-06-16-explored-uv-cli-help-and-format.md) — Explored uv CLI subcommands, help topics, and output formats

## Ruff / py-tooling
- [Ruff Primer](../ruff/notes/0000-primer-ruff.md) — What is Ruff? first contact notes
- [More Ruff CLI Flags](../ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md) — Tried --show-settings, --show-files, --add-noqa, --statistics, ruff rule
- [Ruff Install Script](../ruff/scripts/install-and-lint.sh) — Install Ruff and lint a Python file
- [Ruff Config in pyproject.toml](../ruff/configs/ruff-pyproject.toml) — Configure Ruff inside pyproject.toml
- [Ruff Linter Config](../ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [Ruff Quickstart Notes](../ruff/notes/2026-06-03-tried-ruff-quickstart.md) — Lint, auto-fix, explore rules
- [Ruff vs Flake8 Docs](../ruff/docs/ruff-vs-flake8-comparison.md) — Rule coverage, migration gotchas, auto-fix comparison
- [Ruff CLI Notes](../ruff/notes/2026-06-06-cli-exploration.md) — CLI flags and output formats
- [Messy Example Snippet](../ruff/snippets/messy_example.py) — Deliberately broken code to test linter
- [Tried Messy Example Snippet](../ruff/snippets/tried-messy-example.py) — Another deliberately messy file with different violations
- [pytest Primer](../pytest/notes/0000-primer-pytest.md) — What is pytest? first contact notes

## pytest
- [First Test Suite Notes](../pytest/notes/2026-06-08-installed-pytest-first-suite.md) — Installed pytest, ran first test suite, what tripped me up
- [pytest First Test Snippet](../pytest/snippets/test_first_test.py) — My first pytest test, basic assertions
- [Three Basic Tests Snippet](../pytest/snippets/three_basic_tests.py) — assert, exception, parameterized tests
- [pytest CLI Notes](../pytest/notes/2026-05-26-tried-pytest-cli.md) — Exploring CLI flags and output formats
- [Fixtures with conftest Notes](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md) — conftest.py with shared setup/teardown using yield fixtures
- [Parametrized Tests Script](../pytest/scripts/test_parametrized.py) — Parametrized tests with @pytest.mark.parametrize
- [pytest vs unittest Docs](../pytest/docs/pytest-vs-unittest-mapping.md) — API mapping and migration patterns from unittest
- [pytest CLI Advanced Flags Notes](../pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md) — Exploring `--collect-only`, `--fixtures`, and `--co` flags
- [Run pytest with CLI Flags Script](../pytest/scripts/run-pytest-with-cli-flags.sh) — Create test file and run with -v, -k, -x, --tb=short
- [Install and Run First pytest Script](../pytest/scripts/install-and-run-first-pytest.sh) — Install pytest and run first passing test

## pyproject.toml
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project
- [Multi-tool pyproject.toml Config](../pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config
- [First PEP 621 Config](../pyproject.toml/configs/first-pep621-config.toml) — PEP 621 build-system and project metadata with hatchling
- [pyproject.toml Settings Notes](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md) — Key pyproject.toml settings explained
- [Build-System Config Notes](../pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md) — Exploring the [build-system] table and how it connects to PEP 517/621

## uv.lock
- [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) — What is uv.lock? first contact notes
- [Generate First uv.lock Notes](../uv.lock/notes/2026-06-11-generated-first-uv-lock.md) — Install uv and generate first uv.lock, what's inside it
- [uv.lock Structure Notes](../uv.lock/notes/2026-05-26-uv-lock-structure.md) — Reading and understanding uv.lock internals
- [Generate uv.lock Script](../uv.lock/scripts/generate-uv-lock.sh) — Generate a uv.lock with uv sync
- [Reproducibility Test Script](../uv.lock/scripts/tried-uv-lock-reproducibility.sh) — Test that uv.lock checksums are stable across lock commands
- [Generate from pyproject.toml Script](../uv.lock/scripts/tried-generate-from-pyproject-toml.sh) — Create pyproject.toml by hand, generate uv.lock, and inspect the output
- [Read uv.lock Snippet](../uv.lock/snippets/tried-reading-uv-lock.py) — Parse uv.lock with Python and list package names
- [Detect Conflicting Constraints Snippet](../uv.lock/snippets/tried-detect-conflicting-constraints.py) — Parse uv.lock and flag packages with conflicting version constraints
- [Exploring uv.lock Structure Notebook](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb) — Walk through uv.lock sections, hashes, and reproducibility mechanisms
- [Extract Direct Dependencies Script](../uv.lock/scripts/tried-extract-direct-deps.py) — Parse uv.lock and list all direct dependency entries with versions

## pre-commit
- [pre-commit Primer](../pre-commit/notes/0000-primer-pre-commit.md) — What is pre-commit? first contact notes
- [pre-commit config](../pre-commit/snippets/first-pre-commit-config.yaml) — My first pre-commit hook config
- [Pre-commit Multi-Hook Config](../pre-commit/configs/tried-multi-hook-config.yaml) — Ruff + mypy + trailing-whitespace hooks
- [Install and Run Script](../pre-commit/scripts/install-and-run.sh) — Install pre-commit and run on my repo
- [Run Pre-commit on /work Notes](../pre-commit/notes/2026-05-28-run-pre-commit-on-work.md) — Running pre-commit across /work and interpreting results
- [Ruff-Only Hook Config](../pre-commit/configs/tried-first-ruff-hooks-config.yaml) — Minimal pre-commit config with just the ruff hook
- [Pre-commit CLI Exploration Notes](../pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md) — Install pre-commit, explore CLI subcommands and flags
- [Install and Run Lint + Typecheck Notes](../pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md) — Install pre-commit, run with ruff linting and mypy type check on a sample repo
- [Ruff + Mypy Hooks Config Snippet](../pre-commit/snippets/tried-ruff-mypy-config.yaml) — Minimal pre-commit config with ruff and mypy hooks

## pip-audit
- [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first contact notes
- [CVE Findings Snippet](../pip-audit/snippets/list-cve-findings.py) — Parse pip-audit JSON and list CVE findings with severity
- [Scan Project Script](../pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [Scan and Parse JSON Script](../pip-audit/scripts/scan-and-parse-json.sh) — Scan requirements.txt and parse JSON output with jq
- [Audit and Parse Script](../pip-audit/scripts/2026-06-09-audit-and-parse-json.sh) — Run pip-audit on a requirements.txt and parse JSON output
- [pip-audit Findings Notes](../pip-audit/notes/2026-05-26-pip-audit-findings.md) — First scan results and observations
- [Install and Run Notes](../pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md) — Install pip-audit and run first audit, what tripped me up
- [pip-audit Ignore Config](../pip-audit/configs/pip-audit-ignore.toml) — Configure pip-audit ignore list for reviewed CVEs

## rich
- [Rich Primer](../rich/notes/0000-primer-rich.md) — What is Rich? first contact notes
- [Console API Notes](../rich/notes/2026-06-04-tried-rich-console-api.md) — Trying print, print_json, rule, log
- [Console API Renderables Notes](../rich/notes/2026-06-17-explored-rich-console-api-renderables.md) — Renderables, styles, and output modes
- [Console Logging Snippet](../rich/snippets/first-rich-logger.py) — Minimal rich logging handler setup
- [Progress Bar Snippet](../rich/snippets/tried-rich-progress-bar.py) — First try at rich progress bar
- [Table, Panel, Progress Script](../rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Themes and Markdown Notes](../rich/notes/2026-05-27-tried-rich-themes-and-markdown.md) — Exploring themes and markdown rendering
- [Exploring Renderables Notes](../rich/notes/2026-05-28-exploring-renderables.md) — Trying tables, panels, layouts, markup syntax
- [Progress Spinner Snippet](../rich/snippets/tried-progress-spinner.py) — Interactive status spinner for simulated long-running task
- [Quickstart Tables/Panels Notes](../rich/notes/2026-06-03-tried-rich-quickstart-tables-panels.md) — Following official quickstart: Console, Table, Panel, Layout
- [Live Data Viewer Snippet](../rich/snippets/tried-live-data-viewer.py) — Layout + Table + Live display in a simulated process monitor
- [Styled Output Snippet](../rich/snippets/tried-rich-styled-output.py) — First styled terminal output with rich print
- [Console Panel and Table Snippet](../rich/snippets/tried-rich-console-panel-table.py) — Minimal Console script with text styling, panel, and table
- [Rich CLI Notes](../rich/notes/2026-06-09-tried-rich-cli.md) — Exploring the rich CLI and console features

## mypy
- [mypy Primer](../mypy/notes/0000-primer-mypy.md) — What is mypy? first contact notes
- [First mypy Run Notes](../mypy/notes/2026-06-04-first-mypy-run.md) — Annotated a function, fixed type errors, tried reveal_type
- [First Type Check Script](../mypy/scripts/tried-mypy-first-check.py) — Intentionally broken file to run mypy against
- [CLI Flags Notes](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md) — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [Quickstart for Existing Projects](../mypy/notes/2026-05-29-tried-mypy-quickstart.md) — Running mypy on an existing codebase, what tripped me up
- [Strict Mode Config](../mypy/configs/tried-strict-mypy-config.toml) — Minimal mypy config with incremental strict mode and stub setup
- [Type Error Detection Snippet](../mypy/snippets/tried-mypy-type-errors.py) — Intentional type errors for mypy to catch
- [Typed Functions Validate Snippet](../mypy/snippets/typed-functions-validate.py) — Small typed Python module with annotated functions
- [Followed mypy Quickstart Notes](../mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Gradual typing, strict mode, what tripped me up
- [Minimal mypy.ini Config](../mypy/configs/tried-minimal-mypy-config.ini) — Strict, disallow-untyped-defs, ignore-missing-imports

## Ty
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

## typer
- [Typer Primer](../typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [First Typer Hello-World Notes](../typer/notes/2026-06-10-first-typer-hello-world.md) — Install Typer and run my first CLI hello-world app
- [Minimal CLI Demo](../typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Quickstart Notes](../typer/notes/2026-05-29-typer-quickstart-notes.md) — What tripped me up following quickstart
- [Calculator Script](../typer/scripts/tried-typer-calculator.py) — Minimal Typer CLI calculator: add, sub, mul, div
- [First Typer CLI App Snippet](../typer/snippets/tried-first-typer-cli-app.py) — Minimal Typer CLI app with argument and option

## py-spy
- [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first contact notes
- [Install and Record Flamegraph](../py-spy/scripts/tried-install-and-record-flamegraph.sh) — Install py-spy and profile CPU-bound script to flamegraph SVG
- [Sampling Target Script](../py-spy/scripts/tried-py-spy-sampling.py) — Python script with CPU-bound functions for py-spy to sample
- [CLI Subcommand Notes](../py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md) — Exploring record, top, and flamegraph subcommands
- [Record & Flamegraph Script](../py-spy/scripts/tried-py-spy-record-flamegraph.sh) — Profile a CPU-bound script and output a flamegraph SVG
- [CPU-Bound Simulation Snippet](../py-spy/snippets/tried-cpu-bound-simulation.py) — Minimal script for py-spy profiling practice
- [Top Session Tripped Me Up](../py-spy/notes/2026-06-08-tripped-on-py-spy-top-session.md) — First py-spy top session: permission issues, columns, key flags
- [Py-spy Quickstart Notes](../py-spy/notes/2026-06-10-followed-py-spy-quickstart.md) — Followed official quickstart: profile a sample app, flamegraph, what tripped me up
- [Record Output Formats Notes](../py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md) — Compared flamegraph SVG, speedscope JSON, and raw JSON formats
- [Speedscope Record Script](../py-spy/scripts/tried-py-spy-speedscope-record.py) — CPU-bound workload with py-spy record and speedscope JSON export
- [Py-spy Workflow Notes](../py-spy/notes/2026-06-13-my-py-spy-workflow.md) — Documented record, flamegraph, top modes with gotchas
- [Profile Running Process Snippet](../py-spy/snippets/tried-profile-running-process.py) — Profile a running Python process and export flamegraph SVG
- [Profile Running Process Snippet](../py-spy/snippets/tried-profile-running-process.py) — Profile a running Python process and export flamegraph SVG

## pipdeptree
- [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first contact notes
- [Pipdeptree Patterns I Use](../pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md) — More CLI patterns: --graph-output, --local-only, --python-version, --all
- [Install and Inspect Script](../pipdeptree/scripts/install-and-inspect-deps.sh) — Install pipdeptree and inspect the /work project's dependency tree
- [JSON Format Notes](../pipdeptree/notes/2026-05-29-format-json-deps.md) — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [JSON Format and Dependency Type Notes](../pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md) — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [Parse JSON Snippet](../pipdeptree/snippets/parse-pipdeptree-json.py) — Parse pipdeptree JSON output and list leaf packages
- [Reverse Dependency Snippet](../pipdeptree/snippets/find-reverse-deps.py) — Use `--reverse` to find which packages depend on a given package
- [Filtering & JSON Tripped Me Up](../pipdeptree/notes/2026-06-07-tripped-on-pipdeptree-filtering.md) — Filter by package, JSON format quirks, missing deps
- [pipdeptree Quickstart Notes](../pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md) — Following official quickstart: visualize deps, detect cycles, confusions
- [Package Dependency Chain Snippet](../pipdeptree/snippets/check-package-deps.py) — Check one package and print its dependency chain
- [Check Package Deps Snippet](../pipdeptree/snippets/tried-check-package-deps.py) — Minimal script to look up a package in pipdeptree JSON and walk its dependency chain
- [Common CLI Patterns Notes](../pipdeptree/notes/2026-06-13-common-cli-patterns.md) — CLI patterns I figured out on my own

## tox
- [tox Primer](../tox/notes/0000-primer-tox.md) — What is tox? first contact notes
- [Minimal tox Config](../tox/configs/tox.ini) — Single env with pytest deps
- [Lint and Test Env Config](../tox/configs/tried-lint-and-test-env.ini) — L2: tox.ini with lint (ruff) and test (pytest) environments, annotated with reasoning
- [First tox CLI Run Notes](../tox/notes/2026-05-31-tox-cli-first-run.md) — env list, -e flag, passing args through
- [Followed tox Quickstart Notes](../tox/notes/2026-06-11-followed-tox-quickstart.md) — Multi-env setup, what tripped me up
- [Minimal tox Run Script](../tox/scripts/tried-minimal-tox-run.sh) — Create tox.ini, run tox end-to-end with a test env

## httpie
- [httpie Primer](../httpie/notes/0000-primer-httpie.md) — What is HTTPie? first contact notes
- [Install and Test Script](../httpie/scripts/install_and_test_httpie.sh) — Install httpie with pipx, make GET/POST requests to JSONPlaceholder
- [httpie vs curl Notes](../httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, ergonomics compared
- [First Request Tripped Me Up](../httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md) — What caught me off guard on my first httpie request
- [First HTTPie Request Notes](../httpie/notes/2026-06-10-first-httpie-request.md) — Install httpie, run my first GET with JSON and POST with form data
- [HTTPie GET/POST Automation Snippet](../httpie/snippets/tried-httpie-get-post-workflow.py) — Python script automating httpie for a simple GET/POST workflow

## General
- [Cross-Tool Workflow Notes](../general/notes/2026-06-12-figured-out-quality-tool-workflow.md) — How Ruff, mypy, pytest, pre-commit, and uv fit together
- [First Quality Chain Snippet](../general/snippets/tried-first-quality-chain.py) — Run Ruff, mypy, and pytest in sequence from one script
- [Backlog Capacity Audit Notes](../general/notes/2026-06-10-backlog-capacity-audit.md) — Count open vs completed tasks per tool, identify blockers
- [Quality Tools pyproject.toml Config](../general/configs/tried-quality-tools-pyproject.toml) — First combined ruff, mypy, pytest config in one pyproject.toml
