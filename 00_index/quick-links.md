# Quick Links

## uv

- [uv Primer](../uv/notes/0000-primer-uv.md) — What is uv? first contact notes
- [Install uv Script](../uv/scripts/install-and-first-command.sh) — Install uv and run first command
- [Virtual Env Notes](../uv/notes/2026-05-24-virtual-env-uv.md) — Creating and exploring a virtual environment with uv
- [Quickstart Scaffold Notes](../uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md) — Following uv init, add, run workflow

## Ruff

- [Ruff Primer](../py/notes/0000-primer-py.md) — What is Ruff? first contact notes
- [Ruff Install Script](../py/scripts/install-and-lint.sh) — Install Ruff and lint a Python file
- [Ruff Config](../py/configs/ruff-pyproject.toml) — Configure Ruff with pyproject.toml
- [Ruff Linter Config](../ruff/configs/ruff-linter-settings.toml) — Minimal ruff config with rule selection, ignores, excludes

## pytest

- [pytest Primer](../py/notes/0000-primer-pytest.md) — What is pytest? first contact notes
- [pytest First Test Snippet](../pytest/snippets/test_first_test.py) — My first pytest test, basic assertions
- [pytest CLI Notes](../pytest/notes/2026-05-26-tried-pytest-cli.md) — Exploring CLI flags and output formats
- [Parametrized Tests Script](../pytest/scripts/test_parametrized.py) — Parametrized tests with @pytest.mark.parametrize

## pyproject.toml

- [pyproject.toml Primer](../pyproject.toml/notes/0000-primer-pyproject.toml.md) — What is pyproject.toml? first contact notes
- [Minimal pyproject.toml Config](../pyproject.toml/configs/minimal-pyproject.toml) — Minimal pyproject.toml for a Python project
- [pyproject.toml Settings Notes](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md) — Key pyproject.toml settings explained

## uv.lock

- [uv.lock Primer](../uv.lock/notes/0000-primer-uv.lock.md) — What is uv.lock? first contact notes
- [uv.lock Structure Notes](../uv.lock/notes/2026-05-26-uv-lock-structure.md) — Reading and understanding uv.lock internals
- [Generate uv.lock Script](../uv.lock/scripts/generate-uv-lock.sh) — Generate a uv.lock with uv sync

## uv

- [Run Python Script with uv Snippet](../uv/snippets/run-with-uv.py) — Minimal script to run with uv run
- [uv pyproject.toml Config](../uv/configs/2026-05-26-uv-pyproject-settings.toml) — Configure uv settings in pyproject.toml
- [uv CLI Beyond Basics](../uv/notes/2026-05-26-cli-commands-beyond-basics.md) — Exploring uv CLI commands beyond basics
- [Hello World with Dep Script](../uv/scripts/hello-with-dep.py) — PEP 723 inline metadata, uv run with requests

## pre-commit

- [pre-commit Primer](../pre-commit/notes/0000-primer-pre-commit.md) — What is pre-commit? first contact notes
- [pre-commit config](../pre-commit/snippets/first-pre-commit-config.yaml) — My first pre-commit hook config
- [Install and Run Script](../pre-commit/scripts/install-and-run.sh) — Install pre-commit and run on my repo

## pip-audit

- [pip-audit Primer](../pip-audit/notes/0000-primer-pip-audit.md) — What is pip-audit? first contact notes
- [Scan Project Script](../pip-audit/scripts/scan-project.sh) — Scan my project for vulnerabilities with pip-audit
- [pip-audit Findings Notes](../pip-audit/notes/2026-05-26-pip-audit-findings.md) — First scan results and observations
- [pip-audit Ignore Config](../pip-audit/configs/pip-audit-ignore.toml) — Configure pip-audit ignore list for reviewed CVEs

## rich

- [Rich Primer](../rich/notes/0000-primer-rich.md) — What is Rich? first contact notes
- [Console Logging Snippet](../rich/snippets/first-rich-logger.py) — Minimal rich logging handler setup
- [Progress Bar Snippet](../rich/snippets/tried-rich-progress-bar.py) — First try at rich progress bar
- [Themes and Markdown Notes](../rich/notes/2026-05-27-tried-rich-themes-and-markdown.md) — Exploring themes and markdown rendering

## mypy

- [mypy Primer](../mypy/notes/0000-primer-mypy.md) — What is mypy? first contact notes
- [First Type Check Script](../mypy/scripts/tried-mypy-first-check.py) — Intentionally broken file to run mypy against
- [CLI Flags Notes](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md) — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [Quickstart for Existing Projects](../mypy/notes/2026-05-29-tried-mypy-quickstart.md) — Running mypy on an existing codebase, what tripped me up
- [Strict Mode Config](../mypy/configs/tried-strict-mypy-config.toml) — Minimal mypy config with incremental strict mode and stub setup
- [Type Error Detection Snippet](../mypy/snippets/tried-mypy-type-errors.py) — Intentional type errors for mypy to catch

## pre-commit

- [Run Pre-commit on /work Notes](../pre-commit/notes/2026-05-28-run-pre-commit-on-work.md) — Running pre-commit across /work and interpreting results

## rich

- [Table, Panel, Progress Script](../rich/scripts/first-table-panel-progress.py) — First rich script with table, panel, and progress bar
- [Exploring Renderables Notes](../rich/notes/2026-05-28-exploring-renderables.md) — Trying tables, panels, layouts, markup syntax

## Ty

- [Ty Primer](../ty/notes/0000-primer-ty.md) — What is Ty? first contact notes
- [Run Ty on a Codebase Snippet](../ty/snippets/run-ty-on-codebase.py) — Minimal example running Ty on a Python module
## pipdeptree

- [pipdeptree Primer](../pipdeptree/notes/0000-primer-pipdeptree.md) — What is pipdeptree? first contact notes
- [Install and Inspect Script](../pipdeptree/scripts/install-and-inspect-deps.sh) — Install pipdeptree and inspect the /work project\'s dependency tree
- [JSON Format Notes](../pipdeptree/notes/2026-05-29-format-json-deps.md) — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [JSON Format and Dependency Type Notes](../pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md) — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps


## Typer

- [Typer Primer](../typer/notes/0000-primer-typer.md) — What is Typer? first contact notes
- [Minimal CLI Demo](../typer/scripts/typer_cli_demo.py) — CLI with positional and optional arguments
- [Quickstart Notes](../typer/notes/2026-05-29-typer-quickstart-notes.md) — What tripped me up following quickstart

## py-spy

- [py-spy Primer](../py-spy/notes/0000-primer-py-spy.md) — What is py-spy? first contact notes
- [Sampling Target Script](../py-spy/scripts/tried-py-spy-sampling.py) — Python script with CPU-bound functions for py-spy to sample
- [CLI Subcommand Notes](../py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md) — Exploring record, top, and flamegraph subcommands

## tox

- [tox Primer](../tox/notes/0000-primer-tox.md) — What is tox? first contact notes
- [Minimal tox Config](../tox/configs/tox.ini) — Single env with pytest deps
- [First tox CLI Run Notes](../tox/notes/2026-05-31-tox-cli-first-run.md) — env list, -e flag, passing args through

## httpie

- [httpie Primer](../httpie/notes/0000-primer-httpie.md) — What is HTTPie? first contact notes
- [Install and Test Script](../httpie/scripts/install_and_test_httpie.sh) — Install httpie, make GET/POST requests to JSONPlaceholder
- [httpie vs curl Notes](../httpie/notes/2026-05-30-compare-httpie-vs-curl.md) — Same API calls, ergonomics compared
