# Quick Links

## I need to...

### Set up a Python project
- [uv Primer](uv/notes/0000-primer-uv.md) — What is uv? first-contact notes
- [Install uv Script](uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [Virtual Env Notes](uv/notes/2026-05-24-virtual-env-uv.md) — Creating and exploring a virtual environment with uv
- [Quickstart Scaffold Notes](uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow
- [Bootstrap uv Script](uv/scripts/tried-bootstrap-uv-script.sh) — Bootstrap a one-file Python script with uv run and external deps
- [uv vs pip Cheat Sheet](uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md) — Command mapping and migration cheat-sheet
- [Run multiple test envs](tox/notes/2026-06-11-followed-tox-quickstart.md) — Multi-env setup, skip_install, .tox/ disk footprint

### Lint and format Python code
- [Ruff Primer](ruff/notes/0000-primer-ruff.md) — What is Ruff? first-contact notes
- [Ruff Quickstart Notes](ruff/notes/2026-06-03-tried-ruff-quickstart.md) — Lint, auto-fix, explore rules
- [Ruff Linter Config](ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [Ruff vs Flake8 Docs](ruff/docs/ruff-vs-flake8-comparison.md) — Rule coverage, migration gotchas, auto-fix comparison
- [Ruff CLI Notes](ruff/notes/2026-06-06-cli-exploration.md) — CLI flags and output formats for check and format
- [Ruff Install Script](py/scripts/install-and-lint.sh) — Install Ruff and lint a Python file
- [Ruff Config in pyproject.toml](py/configs/ruff-pyproject-toml) — Configure Ruff inside pyproject.toml
- [Messy Example Snippet](ruff/snippets/messy_example.py) — Deliberately messy code to test linter
- [Ruff-Only Hook Config](pre-commit/configs/tried-first-ruff-hooks-config.yaml) — Minimal pre-commit config with just the ruff hook

### Run tests and CI
- [pytest Primer](pytest/notes/0000-primer-pytest.md) — What is pytest? first-contact notes
- [First Test Suite Notes](pytest/notes/2026-06-08-installed-pytest-first-suite.md) — Installed pytest, ran first test suite, what tripped me up
- [Fixtures with conftest Notes](pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md) — conftest.py with shared setup/teardown using yield fixtures
- [Parametrized Tests Script](pytest/scripts/test_parametrized.py) — Parametrized tests with @pytest.mark.parametrize
- [pytest CLI Notes](pytest/notes/2026-05-26-tried-pytest-cli.md) — Exploring CLI flags and output formats
- [pytest CLI Advanced Flags Notes](pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md) — Exploring --collect-only, --fixtures, and --co flags
- [pytest vs unittest Docs](pytest/docs/pytest-vs-unittest-mapping.md) — API mapping and migration patterns from unittest
- [tox Primer](tox/notes/0000-primer-tox.md) — What is tox? first-contact notes
- [tox CLI First Run Notes](tox/notes/2026-05-31-tox-cli-first-run.md) — env list, -e flag, passing args through
- [First tox Run Tripped Me Up](tox/notes/2026-06-08-first-tox-run-tripped-me-up.md) — First tox run: env creation, isolated installs, slow feedback
- [Followed tox Quickstart Notes](tox/notes/2026-06-11-followed-tox-quickstart.md) — Multi-env setup, what tripped me up
- [Minimal tox Config](tox/configs/tox.ini) — Single env with pytest deps
- [Cross-Tool Workflow Notes](general/notes/2026-06-12-figured-out-quality-tool-workflow.md) — Ruff, mypy, pytest, pre-commit, and uv as a chain
- [First Quality Chain Snippet](general/snippets/tried-first-quality-chain.py) — Run Ruff, mypy, and pytest in sequence from one script

### Check types
- [mypy Primer](mypy/notes/0000-primer-mypy.md) — What is mypy? first-contact notes
- [Followed the Official mypy Quickstart](mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Using gradual typing and strict mode, where I got stuck
- [First mypy Run Notes](mypy/notes/2026-06-04-first-mypy-run.md) — Annotated a function, fixed type errors, tried reveal_type
- [First mypy Check Tripped Me Up](mypy/notes/2026-06-05-mypy-first-check-tripped-me-up.md) — What caught me off guard on my first mypy check
- [CLI Flags Notes](mypy/notes/2026-05-28-tried-mypy-cli-flags.md) — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [Quickstart for Existing Projects](mypy/notes/2026-05-29-tried-mypy-quickstart.md) — Running mypy on an existing codebase, what tripped me up
- [First Type Check Script](mypy/scripts/tried-mypy-first-check.py) — Intentionally broken file to run mypy against
- [Strict Mode Config](mypy/configs/tried-strict-mypy-config.toml) — Minimal mypy config with incremental strict mode and stub setup
- [Minimal Mypy Config](mypy/configs/tried-minimal-mypy-config.ini) — Three flags from the official quickstart, strict mode with per-module overrides
- [Type Error Detection Snippet](mypy/snippets/tried-mypy-type-errors.py) — Intentional type errors for mypy to catch
- [Typed Functions Validate Snippet](mypy/snippets/typed-functions-validate.py) — Small typed Python module with annotated functions
- [Ty Primer](ty/notes/0000-primer-ty.md) — What is Ty? first-contact notes
- [Ty Quickstart Notes](ty/notes/2026-06-05-tried-ty-quickstart.md) — Following the official quickstart, first check, what tripped me up
- [First Ty Markdown Render](ty/notes/2026-06-10-first-ty-markdown-render.md) — Install Ty and render my first markdown file in the terminal
- [Compare Ty vs Mypy Notes](ty/notes/2026-05-27-compare-ty-vs-mypy.md) — Comparing ty vs mypy output on the same codebase
- [Ty Config](ty/configs/tried-ty-config.toml) — Ty configuration file with enabled error codes
- [Ty Markdown CSS](ty/configs/tried-ty-markdown-css.css) — Custom CSS styling for Ty markdown rendering
- [Ty Pipeline Script](ty/scripts/tried-ty-pipeline.sh) — Pipe markdown through ty and capture formatted output
- [Run Ty on a Codebase Snippet](ty/snippets/run-ty-on-codebase.py) — Minimal example running Ty on a Python module

### Render terminal output
- [Rich Primer](rich/notes/0000-primer-rich.md) — What is Rich? first-contact notes
- [Table, Panel, Progress Script](rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Console API Notes](rich/notes/2026-06-04-tried-rich-console-api.md) — Trying print, print_json, rule, log
- [Themes and Markdown Notes](rich/notes/2026-05-27-tried-rich-themes-and-markdown.md) — Exploring themes and markdown rendering
- [Exploring Renderables Notes](rich/notes/2026-05-28-exploring-renderables.md) — Trying tables, panels, layouts, markup syntax
- [Progress Spinner Snippet](rich/snippets/tried-progress-spinner.py) — Interactive status spinner for simulated long-running task
- [Progress Bar Snippet](rich/snippets/tried-rich-progress-bar.py) — First try at rich progress bar
- [Console Logging Snippet](rich/snippets/first-rich-logger.py) — Minimal rich logging handler setup
- [Live Data Viewer Snippet](rich/snippets/tried-live-data-viewer.py) — Layout + Table + Live display in a simulated process monitor
- [Styled Output Snippet](rich/snippets/tried-rich-styled-output.py) — First styled terminal output with rich print
- [Rich CLI Notes](rich/notes/2026-06-09-tried-rich-cli.md) — Exploring the rich CLI and console features

### Audit for vulnerabilities
- [pip-audit Primer](pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first-contact notes
- [pip-audit Findings Notes](pip-audit/notes/2026-05-26-pip-audit-findings.md) — First scan results and observations
- [Install and Run Notes](pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md) — Install pip-audit and run first audit, what tripped me up
- [Scan Project Script](pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [Scan and Parse JSON Script](pip-audit/scripts/scan-and-parse-json.sh) — Scan requirements.txt and parse JSON output with jq
- [Audit and Parse Script](pip-audit/scripts/2026-06-09-audit-and-parse-json.sh) — Run pip-audit on a requirements.txt and parse JSON output
- [pip-audit Ignore Config](pip-audit/configs/pip-audit-ignore.toml) — Configure pip-audit ignore list for reviewed CVEs

### Profile a Python process
- [py-spy Primer](py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first-contact notes
- [py-spy Top Session](py-spy/notes/2026-06-08-tripped-on-py-spy-top-session.md) — First py-spy top session: permission issues, columns, key flags
- [py-spy CLI Subcommands](py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md) — Exploring record, top, and flamegraph subcommands
- [py-spy Quickstart Notes](py-spy/notes/2026-06-10-followed-py-spy-quickstart.md) — Followed official quickstart: profile a sample app, flamegraph, what tripped me up
- [Record & Flamegraph Script](py-spy/scripts/tried-py-spy-record-flamegraph.sh) — Profile a CPU-bound script and output a flamegraph SVG
- [Sampling Target Script](py-spy/scripts/tried-py-spy-sampling.py) — Python script with CPU-bound functions for py-spy to sample
- [CPU-Bound Simulation Snippet](py-spy/snippets/tried-cpu-bound-simulation.py) — Minimal script for py-spy profiling practice

### Build a CLI
- [Typer Primer](typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [First Typer Hello-World Notes](typer/notes/2026-06-10-first-typer-hello-world.md) — Install Typer and run my first CLI hello-world app
- [Typer CLI Demo](typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Calculator Script](typer/scripts/tried-typer-calculator.py) — Minimal Typer CLI calculator: add, sub, mul, div
- [Quickstart Notes](typer/notes/2026-05-29-typer-quickstart-notes.md) — What tripped me up following quickstart
- [First Typer CLI App Snippet](typer/snippets/tried-first-typer-cli-app.py) — Minimal Typer CLI app with argument and option

### Configure pre-commit hooks
- [pre-commit Primer](pre-commit/notes/0000-primer-pre-commit.md) — What is pre-commit? first-contact notes
- [Pre-commit Multi-Hook Config](pre-commit/configs/tried-multi-hook-config.yaml) — Ruff + mypy + trailing-whitespace hooks
- [Install and Run Script](pre-commit/scripts/install-and-run.sh) — Install pre-commit and run on my repo
- [Run Pre-commit on /work Notes](pre-commit/notes/2026-05-28-run-pre-commit-on-work.md) — Running pre-commit across /work and interpreting results
- [Ruff-Only Hook Config](pre-commit/configs/tried-first-ruff-hooks-config.yaml) — Minimal pre-commit config with just the ruff hook
- [Pre-commit CLI Exploration Notes](pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md) — Install pre-commit, explore CLI subcommands and flags
- [pre-commit config](pre-commit/snippets/first-pre-commit-config.yaml) — My first pre-commit hook config

### Configure pyproject.toml
- [pyproject.toml Primer](pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project
- [Multi-tool pyproject.toml Config](pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config
- [pyproject.toml Settings Notes](pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md) — Key pyproject.toml settings explained
- [First Build System Config](pyproject.toml/notes/2026-06-12-first-build-system-config.md) — First look at the [build-system] section and backends

### Understand dependency trees
- [pipdeptree Primer](pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first-contact notes
- [pipdeptree CLI Patterns I Keep Using](pipdeptree/notes/2026-06-12-pipdeptree-cli-patterns.md) — --warn silence, --freeze, --exclude, JSON output tricks
- [pipdeptree Quickstart Notes](pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md) — Following official quickstart: visualize deps, detect cycles, confusions
- [Format JSON Deps Notes](pipdeptree/notes/2026-05-29-format-json-deps.md) — Formatting output as JSON, identifying top-level vs transitive deps
- [JSON Format and Dep Type Notes](pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md) — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [Filtering & JSON Tripped Me Up](pipdeptree/notes/2026-06-07-tripped-on-pipdeptree-filtering.md) — Filter by package, JSON format quirks, missing deps
- [Install and Inspect Script](pipdeptree/scripts/install-and-inspect-deps.sh) — Install pipdeptree and inspect dependencies
- [Parse JSON Snippet](pipdeptree/snippets/parse-pipdeptree-json.py) — Parse pipdeptree JSON output and list leaf packages
- [Reverse Dependency Snippet](pipdeptree/snippets/find-reverse-deps.py) — Use --reverse to find which packages depend on a given package

### Make HTTP requests
- [httpie Primer](httpie/notes/0000-primer-httpie.md) — What is HTTPie? first-contact notes
- [First HTTPie Request Notes](httpie/notes/2026-06-10-first-httpie-request.md) — Install httpie, run my first GET with JSON and POST with form data
- [httpie vs curl Notes](httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, ergonomics compared to curl
- [First Request Tripped Me Up](httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md) — What caught me off guard on my first httpie request
- [Install and Test Script](httpie/scripts/install_and_test_httpie.sh) — Install httpie with pipx, make GET/POST requests to JSONPlaceholder
- [HTTPie GET/POST Automation Snippet](httpie/snippets/tried-httpie-get-post-workflow.py) — Python script automating httpie for a simple GET/POST workflow
