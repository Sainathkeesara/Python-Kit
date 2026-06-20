# Quick Links

## I need to...

### Set up a Python project
- [uv Primer](../uv/notes/0000-primer-uv.md) — What is uv? first contact notes
- [Install uv Script](../uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [Virtual Env Notes](../uv/notes/2026-05-24-virtual-env-uv.md) — Creating and exploring a virtual environment with uv
- [Quickstart Scaffold Notes](../uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow
- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project

### Lint and format code
- [Ruff Primer](../ruff/notes/0000-primer-ruff.md) — What is Ruff? first contact notes
- [Install Ruff Script](../py/scripts/install-and-lint.sh) — Install Ruff and lint a Python file
- [Ruff Quickstart Notes](../ruff/notes/2026-06-03-tried-ruff-quickstart.md) — Lint, auto-fix, explore rules
- [Ruff CLI Notes](../ruff/notes/2026-06-06-cli-exploration.md) — CLI flags and output formats
- [More Ruff CLI Flags](../ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md) — `--show-settings`, `--show-files`, `--add-noqa`, `--statistics`, `ruff rule`
- [Ruff Linter Config](../ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes
- [Ruff vs Flake8 Docs](../ruff/docs/ruff-vs-flake8-comparison.md) — Rule coverage, migration gotchas, auto-fix comparison
- [Messy Example Snippet](../ruff/snippets/messy_example.py) — Deliberately broken code to test linter
- [Multi-tool pyproject.toml Config](../pyproject.toml/configs/multi-tool-pyproject.toml) — Combined ruff, pytest, mypy config

### Type-check Python code
- [mypy Primer](../mypy/notes/0000-primer-mypy.md) — What is mypy? first contact notes
- [First mypy Run Notes](../mypy/notes/2026-06-04-first-mypy-run.md) — Annotated a function, fixed type errors, tried reveal_type
- [CLI Flags Notes](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md) — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [Strict Mode Config](../mypy/configs/tried-strict-mypy-config.toml) — Minimal mypy config with incremental strict mode and stub setup
- [Followed mypy Quickstart Notes](../mypy/notes/2026-06-12-followed-mypy-quickstart.md) — Gradual typing, strict mode, what tripped me up
- [Ty Primer](../ty/notes/0000-primer-ty.md) — What is Ty? alternative type checker notes
- [Compare Ty vs Mypy Notes](../ty/notes/2026-05-27-compare-ty-vs-mypy.md) — Comparing ty vs mypy output on the same codebase
- [Ty vs Mypy Snippet](../ty/snippets/tried-ty-vs-mypy.py) — Compare Ty and mypy output on the same typed code

### Run tests
- [pytest Primer](../pytest/notes/0000-primer-pytest.md) — What is pytest? first contact notes
- [First Test Suite Notes](../pytest/notes/2026-06-08-installed-pytest-first-suite.md) — Installed pytest, ran first test suite, what tripped me up
- [pytest CLI Notes](../pytest/notes/2026-05-26-tried-pytest-cli.md) — Exploring CLI flags and output formats
- [Fixtures with conftest Notes](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md) — conftest.py with shared setup/teardown using yield fixtures
- [pytest vs unittest Docs](../pytest/docs/pytest-vs-unittest-mapping.md) — API mapping and migration patterns from unittest
- [tox Primer](../tox/notes/0000-primer-tox.md) — What is tox? first contact notes
- [tox Quickstart Notes](../tox/notes/2026-06-11-followed-tox-quickstart.md) — Multi-env setup, what tripped me up
- [Pre-commit Multi-Hook Config](../pre-commit/configs/tried-multi-hook-config.yaml) — Ruff + mypy + trailing-whitespace hooks

### Audit dependencies
- [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first contact notes
- [Scan Project Script](../pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [CVE Findings Snippet](../pip-audit/snippets/list-cve-findings.py) — Parse pip-audit JSON and list CVE findings with severity
- [pip-audit Ignore Config](../pip-audit/configs/pip-audit-ignore.toml) — Configure pip-audit ignore list for reviewed CVEs
- [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first contact notes
- [Pipdeptree Patterns I Use](../pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md) — --warn silence, --freeze, --exclude, JSON output tricks
- [Parse JSON Snippet](../pipdeptree/snippets/parse-pipdeptree-json.py) — Parse pipdeptree JSON output and list leaf packages
- [Reverse Dependency Snippet](../pipdeptree/snippets/find-reverse-deps.py) — Use `--reverse` to find which packages depend on a given package

### Profile performance
- [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first contact notes
- [Install and Record Flamegraph](../py-spy/scripts/tried-install-and-record-flamegraph.sh) — Install py-spy and profile CPU-bound script to flamegraph SVG
- [Sample Script for Profiling](../py-spy/scripts/tried-py-spy-sampling.py) — Python script with CPU-bound functions for py-spy to sample
- [Record Output Formats Notes](../py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md) — Compared flamegraph SVG, speedscope JSON, and raw JSON formats

### Build a CLI
- [Typer Primer](../typer/notes/0000-primer-typer.md) — First-contact notes for typer
- [First Typer Hello-World Notes](../typer/notes/2026-06-10-first-typer-hello-world.md) — Install Typer and run my first CLI hello-world app
- [Minimal CLI Demo](../typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Calculator Script](../typer/scripts/tried-typer-calculator.py) — Minimal Typer CLI calculator: add, sub, mul, div

### Test APIs
- [httpie Primer](../httpie/notes/0000-primer-httpie.md) — What is HTTPie? first contact notes
- [Install and Test Script](../httpie/scripts/install_and_test_httpie.sh) — Install httpie with pipx, make GET/POST requests to JSONPlaceholder
- [httpie vs curl Notes](../httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, ergonomics compared

### Make terminal output look good
- [Rich Primer](../rich/notes/0000-primer-rich.md) — What is Rich? first contact notes
- [Console API Notes](../rich/notes/2026-06-04-tried-rich-console-api.md) — Trying print, print_json, rule, log
- [Console API Renderables Notes](../rich/notes/2026-06-17-explored-rich-console-api-renderables.md) — Renderables, styles, and output modes
- [Table, Panel, Progress Script](../rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Styled Output Snippet](../rich/snippets/tried-rich-styled-output.py) — First styled terminal output with rich print

### Understand uv.lock
- [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) — What is uv.lock? first contact notes
- [uv.lock Structure Notes](../uv.lock/notes/2026-05-26-uv-lock-structure.md) — Reading and understanding uv.lock internals
- [Generate uv.lock Script](../uv.lock/scripts/generate-uv-lock.sh) — Generate a uv.lock with uv sync
- [Read uv.lock Snippet](../uv.lock/snippets/tried-reading-uv-lock.py) — Parse uv.lock with Python and list package names
- [Exploring uv.lock Structure Notebook](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb) — Walk through uv.lock sections, hashes, and reproducibility

### Chain quality tools together
- [Cross-Tool Workflow Notes](../general/notes/2026-06-12-figured-out-quality-tool-workflow.md) — How Ruff, mypy, pytest, pre-commit, and uv fit together
- [First Quality Chain Snippet](../general/snippets/tried-first-quality-chain.py) — Run Ruff, mypy, and pytest in sequence from one script
- [Quality Tools pyproject.toml Config](../general/configs/tried-quality-tools-pyproject.toml) — First combined ruff, mypy, pytest config in one pyproject.toml
- [Backlog Capacity Audit Notes](../general/notes/2026-06-10-backlog-capacity-audit.md) — Count open vs completed tasks per tool, identify blockers
