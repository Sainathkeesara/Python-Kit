# Topics

## httpie
- [note] httpie/notes/0000-primer-httpie.md — First-contact notes for HTTPie
- [note] httpie/notes/2026-05-30-compare-httpie-vs-curl.md — Same API calls, different ergonomics
- [script] httpie/scripts/install_and_test_httpie.sh — Install httpie, make GET/POST requests to JSONPlaceholder

## mypy
- [note] mypy/notes/0000-primer-mypy.md — First-contact notes for mypy
- [note] mypy/notes/2026-05-28-tried-mypy-cli-flags.md — Trying --strict, --check-untyped-defs, --ignore-missing-imports
- [note] mypy/notes/2026-05-29-tried-mypy-quickstart.md — Running mypy on an existing codebase, what tripped me up
- [script] mypy/scripts/tried-mypy-first-check.py — Intentionally broken file to run mypy against
- [config] mypy/configs/tried-strict-mypy-config.toml — Minimal mypy config with incremental strict mode and stub setup
- [snippet] mypy/snippets/tried-mypy-type-errors.py — Intentional type errors for mypy to catch

## pip-audit
- [note] pip-audit/notes/0000-primer-pip-audit.md — First-contact notes for pip-audit
- [note] pip-audit/notes/2026-05-26-pip-audit-findings.md — First scan results and observations
- [script] pip-audit/scripts/scan-project.sh — Scan project for vulnerabilities with pip-audit
- [config] pip-audit/configs/pip-audit-ignore.toml — Configure pip-audit ignore list for reviewed CVEs

## pipdeptree
- [note] pipdeptree/notes/0000-primer-pipdeptree.md — First-contact notes for pipdeptree
- [note] pipdeptree/notes/2026-05-29-format-json-deps.md — Formatting output as JSON, identifying top-level vs transitive deps
- [note] pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md — Formatting pipdeptree output as JSON and identifying top-level vs transitive deps
- [script] pipdeptree/scripts/install-and-inspect-deps.sh — Install pipdeptree and inspect dependency tree

## pre-commit
- [note] pre-commit/notes/0000-primer-pre-commit.md — First-contact notes for pre-commit hooks
- [note] pre-commit/notes/2026-05-28-run-pre-commit-on-work.md — Running pre-commit across /work and interpreting results
- [script] pre-commit/scripts/install-and-run.sh — Install pre-commit and run on repo
- [snippet] pre-commit/snippets/first-pre-commit-config.yaml — First pre-commit hook config

## py (Ruff / Python tooling)
- [note] py/notes/0000-primer-py.md — What is Ruff? first-contact notes
- [note] py/notes/0000-primer-pytest.md — What is pytest? first-contact notes
- [script] py/scripts/install-and-lint.sh — Install Ruff and lint a Python file
- [config] py/configs/ruff-pyproject.toml — Configure Ruff inside pyproject.toml

## py-spy
- [note] py-spy/notes/0000-primer-py-spy.md — First-contact notes for py-spy
- [note] py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md — Exploring record, top, and flamegraph subcommands
- [script] py-spy/scripts/tried-py-spy-sampling.py — Python script with CPU-bound functions for py-spy to sample

## pyproject.toml
- [note] pyproject.toml/notes/0000-primer-pyproject.toml.md — First-contact notes for pyproject.toml
- [note] pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md — Key pyproject.toml settings explained
- [config] pyproject.toml/configs/minimal-pyproject.toml — Minimal pyproject.toml for a Python project

## pytest
- [note] pytest/notes/2026-05-26-tried-pytest-cli.md — Exploring CLI flags and output formats
- [snippet] pytest/snippets/test_first_test.py — Basic test with assertions
- [script] pytest/scripts/test_parametrized.py — Parametrized tests with @pytest.mark.parametrize

## rich
- [note] rich/notes/0000-primer-rich.md — First-contact notes for rich
- [note] rich/notes/2026-05-27-tried-rich-themes-and-markdown.md — Exploring themes and markdown rendering
- [note] rich/notes/2026-05-28-exploring-renderables.md — Trying tables, panels, layouts, markup syntax
- [script] rich/scripts/first-table-panel-progress.py — First rich script with table, panel, and progress bar
- [snippet] rich/snippets/first-rich-logger.py — Minimal rich logging handler setup
- [snippet] rich/snippets/tried-rich-progress-bar.py — First try at rich progress bar

## ruff
- [config] ruff/configs/ruff-linter-settings.toml — Minimal ruff config with rule selection, ignores, excludes

## ty
- [note] ty/notes/0000-primer-ty.md — First-contact notes for ty
- [note] ty/notes/2026-05-27-compare-ty-vs-mypy.md — Comparing ty vs mypy output on the same codebase
- [config] ty/configs/tried-ty-config.toml — Ty configuration file with enabled error codes
- [snippet] ty/snippets/run-ty-on-codebase.py — Minimal example running ty on a Python module

## typer
- [note] typer/notes/0000-primer-typer.md — First-contact notes for typer
- [note] typer/notes/2026-05-29-typer-quickstart-notes.md — What tripped me up following the quickstart
- [script] typer/scripts/typer_cli_demo.py — CLI with positional and optional arguments

## tox
- [note] tox/notes/0000-primer-tox.md — First-contact notes for tox
- [note] tox/notes/2026-05-31-tox-cli-first-run.md — env list, -e flag, passing args through
- [config] tox/configs/tox.ini — Single env with pytest deps

## uv
- [note] uv/notes/0000-primer-uv.md — What is uv? first-contact notes
- [note] uv/notes/2026-05-24-virtual-env-uv.md — Creating and exploring a virtual environment with uv
- [note] uv/notes/2026-05-26-cli-commands-beyond-basics.md — Exploring uv CLI commands beyond the basics
- [note] uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md — Following uv init, add, run workflow
- [script] uv/scripts/install-and-first-command.sh — Install uv and run first command
- [script] uv/scripts/hello-with-dep.py — PEP 723 inline metadata, uv run with requests
- [config] uv/configs/2026-05-26-uv-pyproject-settings.toml — Configure uv settings in pyproject.toml
- [snippet] uv/snippets/run-with-uv.py — Minimal script to run with uv run

## uv.lock
- [note] uv.lock/notes/0000-primer-uv.lock.md — First-contact notes for uv.lock
- [note] uv.lock/notes/2026-05-26-uv-lock-structure.md — Reading and understanding uv.lock internals
- [script] uv.lock/scripts/generate-uv-lock.sh — Generate a uv.lock file with uv sync
