# CHANGELOG

## 2026-06-17
- pyt-008: Added pytest primer (`pytest/notes/0000-primer-pytest.md`) — What is pytest? first contact notes
- ric-009: Added rich Console API renderables notes (`rich/notes/2026-06-17-explored-rich-console-api-renderables.md`) — Explored renderables, styles, and output modes
- ric-010: Added rich Console panel and table snippet (`rich/snippets/tried-rich-console-panel-table.py`) — Minimal Console script with text styling, panel, and table

## 2026-06-16
- ty-008: Added Ty CLI flags and output formats notes (`ty/notes/2026-06-16-explored-ty-cli-flags.md`) — Explored Ty CLI flags, output formats, compared with mypy options
- prc-008: Added pre-commit install and run with lint+typecheck notes (`pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md`) — Installed pre-commit, ran with ruff linting and mypy type check on a sample repo
- uv-007: Added uv CLI help and format notes (`uv/notes/2026-06-16-explored-uv-cli-help-and-format.md`) — Explored uv CLI subcommands, help topics, and output formats
- gen-005: Added quality tools pyproject.toml config (`general/configs/tried-quality-tools-pyproject.toml`) — Combined ruff, mypy, pytest config in one pyproject.toml
- ty-007: Added Ty vs mypy comparison snippet (`ty/snippets/tried-ty-vs-mypy.py`) — Compare Ty and mypy output on the same typed code
- prc-007: Added ruff + mypy hooks config snippet (`pre-commit/snippets/tried-ruff-mypy-config.yaml`) — Minimal pre-commit config with ruff and mypy hooks

## 2026-06-15
- uvl-012: Added uv.lock structure exploration notebook (`uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb`) — Walk through uv.lock sections, hashes, and reproducibility
- uvl-011: Added uv.lock direct deps extraction script (`uv.lock/scripts/tried-extract-direct-deps.py`) — Parse uv.lock and list all direct dependency entries
- tox-005: Added lint and test env tox config (`tox/configs/tried-lint-and-test-env.ini`) — Minimal tox.ini with lint (ruff) and test (pytest) environments, annotated with reasoning
- ruf-006: Added messy example snippet (`ruff/snippets/tried-messy-example.py`) — Deliberately messy Python file with various style violations
- pdt-007: Added check package deps snippet (`pipdeptree/snippets/tried-check-package-deps.py`) — Look up a specific package in pipdeptree JSON output and print its dependency chain
- tox-009: Added minimal tox run script (`tox/scripts/tried-minimal-tox-run.sh`) — Create tox.ini with test env and run tox end-to-end
- ppt-005: Added build-system config notes (`pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md`) — Exploring minimal [build-system] table in pyproject.toml
- gen-002: Added backlog capacity audit notes (`general/notes/2026-06-10-backlog-capacity-audit.md`) — Count open vs completed tasks per tool, identify next-level blockers

## 2026-06-14
- pyt-007: Added run pytest with CLI flags script (`pytest/scripts/run-pytest-with-cli-flags.sh`) — Create test file and run with -v, -k, -x, --tb=short
- pyt-009: Added install and run first pytest script (`pytest/scripts/install-and-run-first-pytest.sh`) — Install pytest and run first passing test

## 2026-06-13
- psy-012: Added py-spy workflow notes (`py-spy/notes/2026-06-13-my-py-spy-workflow.md`) — Documented record, flamegraph, top modes with gotchas
- psy-011: Added py-spy profile running process snippet (`py-spy/snippets/tried-profile-running-process.py`) — Profile a running Python process and export flamegraph SVG with py-spy
- psy-009: Added py-spy record output formats comparison notes (`py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md`) — Flamegraph SVG, speedscope JSON, raw JSON side by side
- psy-010: Added py-spy speedscope record script (`py-spy/scripts/tried-py-spy-speedscope-record.py`) — CPU-bound workload with py-spy record and speedscope JSON export
- uvl-008: Added uv.lock conflict detection snippet (`uv.lock/snippets/tried-detect-conflicting-constraints.py`) — Parse uv.lock and flag conflicting version constraints
- uvl-009: Added uv.lock generate-and-inspect script (`uv.lock/scripts/tried-generate-from-pyproject-toml.sh`) — Create pyproject.toml, generate uv.lock, inspect output
- ppt-006: Added first PEP 621 config (`pyproject.toml/configs/first-pep621-config.toml`) — PEP 621 build-system and project metadata with hatchling

## 2026-06-12
- mypy-007: Added followed mypy quickstart notes (`mypy/notes/2026-06-12-followed-mypy-quickstart.md`) — Gradual typing, strict mode, and what tripped me up
- mypy-008: Added minimal mypy.ini config (`mypy/configs/tried-minimal-mypy-config.ini`) — Strict, disallow-untyped-defs, ignore-missing-imports
- gen-003: Added cross-tool workflow notes (`general/notes/2026-06-12-figured-out-quality-tool-workflow.md`) — How Ruff, mypy, pytest, pre-commit, and uv fit together in one pipeline
- gen-004: Added first quality chain snippet (`general/snippets/tried-first-quality-chain.py`) — Run Ruff, mypy, and pytest in sequence from one script

## 2026-06-11
- tox-004 (rework): Added followed tox quickstart notes (`tox/notes/2026-06-11-followed-tox-quickstart.md`) — Multi-env setup, what tripped me up
- uv-006: Added bootstrap uv script (`uv/scripts/tried-bootstrap-uv-script.sh`) — Bootstrap a one-file Python script with uv run and external deps
- uvl-005: Added first uv.lock generation notes (`uv.lock/notes/2026-06-11-generated-first-uv-lock.md`) — Install uv and generate first uv.lock, what's inside it
- pdt-009: Added reverse-dependency report snippet (`pipdeptree/snippets/find-reverse-deps.py`) — Use `--reverse` to find which packages depend on a given package

## 2026-06-10
- typer-005: Added first Typer CLI hello-world notes (`typer/notes/2026-06-10-first-typer-hello-world.md`) — Install Typer and run my first CLI hello-world
- typer-006: Added first Typer CLI app snippet (`typer/snippets/tried-first-typer-cli-app.py`) — Minimal Typer CLI app with argument and option
- ty-005: Added first Ty markdown render notes (`ty/notes/2026-06-10-first-ty-markdown-render.md`) — Install Ty and render my first markdown file
- psy-007: Added py-spy quickstart notes (`py-spy/notes/2026-06-10-followed-py-spy-quickstart.md`) — Followed official quickstart: profile a sample app, flamegraph, what tripped me up
- uv-005: Added uv install and first command notes (`uv/notes/2026-06-10-installed-uv-first-command.md`) — Install uv, ran --version, --help, and uv run on a script
- htt-001: Added HTTPie primer (`httpie/notes/0000-primer-httpie.md`) — What is HTTPie? quick primer
- htt-010: Added first HTTPie GET/POST request notes (`httpie/notes/2026-06-10-first-httpie-request.md`) — Install httpie, run my first GET with JSON and POST with form data
- htt-011: Added HTTPie GET/POST automation snippet (`httpie/snippets/tried-httpie-get-post-workflow.py`) — Python script automating httpie for a simple GET/POST workflow
- pyt-006: Added pytest CLI advanced flags notes (`pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md`) — Exploring `--collect-only`, `--fixtures`, and `--co` flags
- prc-006: Added pre-commit CLI exploration notes (`pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md`) — Install pre-commit, explore CLI subcommands and flags

## 2026-06-09
- htt-003: Reworked httpie install script to use pipx instead of pip (`httpie/scripts/install_and_test_httpie.sh`)
- pdt-001: Added pipdeptree quickstart notes (`pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md`) — Following official quickstart: visualize deps, detect cycles, confusions
- pau-005: Added pip-audit install and run notes (`pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md`) — Install pip-audit, run first audit, what tripped me up
- pau-006: Added pip-audit audit and parse script (`pip-audit/scripts/2026-06-09-audit-and-parse-json.sh`) — Run pip-audit on a requirements.txt and parse JSON output
- ty-006: Added Ty pipeline script (`ty/scripts/tried-ty-pipeline.sh`) — Pipe markdown through ty and capture formatted output
- ric-009: Added Rich CLI notes (`rich/notes/2026-06-09-tried-rich-cli.md`) — Exploring the rich CLI and console features

## 2026-06-08
- psy-005 (rework): Added py-spy top session tripped-me-up notes (`py-spy/notes/2026-06-08-tripped-on-py-spy-top-session.md`) — First py-spy top: permission, columns, key flags
- pyt-005: Added first test suite install+run notes (`pytest/notes/2026-06-08-installed-pytest-first-suite.md`) — Installed pytest, ran first suite, naming gotcha
- ric-008: Added first styled output snippet (`rich/snippets/tried-rich-styled-output.py`) — Minimal rich print with colors and markup
- uvl-006: Added uv.lock read snippet (`uv.lock/snippets/tried-reading-uv-lock.py`) — Parse uv.lock with tomllib and list package names
- tox-004: Added tox quickstart notes following official guide (`tox/notes/2026-06-08-tox-quickstart.md`)
- tox-005: Updated tox.ini with `lint` env using ruff (`tox/configs/tox.ini`)

## 2026-06-07
- mypy-003: Added typed functions validation snippet (`mypy/snippets/typed-functions-validate.py`) — Small typed Python module: annotate functions and validate with mypy
- mypy-002: Added mypy first run notes (PATH confusion, untyped function issues, --strict mode)

## 2026-06-06

- psy-004: Added py-spy record & flamegraph script (`py-spy/scripts/tried-py-spy-record-flamegraph.sh`)
- htt-002: Added httpie first-request tripped-me-up notes (`httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md`)
- ruf-004: Added Ruff primer (`ruff/notes/0000-primer-ruff.md`)
- ruf-006: Added messy example snippet (`ruff/snippets/messy_example.py`)
- ruf-007: Added Ruff CLI exploration notes (`ruff/notes/2026-06-06-cli-exploration.md`)

## 2026-06-05

- ty-001: Added Ty quickstart notes (`ty/notes/2026-06-05-tried-ty-quickstart.md`)
- uv-003: Added uv vs pip command mapping cheat-sheet (`uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md`)
- tox-002: Verified minimal tox.ini config with one test environment (`tox/configs/tox.ini`)
- typer-002: Added Typer calculator script (`typer/scripts/tried-typer-calculator.py`)
- prc-002: Added minimal pre-commit config with ruff hook (`pre-commit/configs/tried-first-ruff-hooks-config.yaml`)
- uvl-002: Added uv.lock reproducibility test script (`uv.lock/scripts/tried-uv-lock-reproducibility.sh`)

## 2026-06-04

- pyt-002: Added pytest fixtures with conftest notes (`pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md`)
- pyt-003: Added pytest vs unittest API mapping docs (`pytest/docs/pytest-vs-unittest-mapping.md`)
- ppt-002: Added multi-tool pyproject.toml config (`pyproject.toml/configs/multi-tool-pyproject.toml`)
- ty-002: Added Ty markdown CSS template (`ty/configs/tried-ty-markdown-css.css`)

- ruf-003: Added Ruff vs Flake8 comparison docs (`ruff/docs/ruff-vs-flake8-comparison.md`)
- prc-004: Added pre-commit multi-hook config (`pre-commit/configs/tried-multi-hook-config.yaml`)
- ric-003: Added rich console API notes (`rich/notes/2026-06-04-tried-rich-console-api.md`)
- mypy-003: Added first mypy run notes (`mypy/notes/2026-06-04-first-mypy-run.md`)
- pau-002: Added pip-audit JSON scan script (`pip-audit/scripts/scan-and-parse-json.sh`)

## 2026-06-03

- ruf-001: Added Ruff quickstart notes (`ruff/notes/2026-06-03-tried-ruff-quickstart.md`)
- ric-004: Added interactive progress spinner snippet (`rich/snippets/tried-progress-spinner.py`)
- ric-005: Added Rich quickstart tables/panels notes (`rich/notes/2026-06-03-tried-rich-quickstart-tables-panels.md`)
- ric-006: Added live data viewer snippet (`rich/snippets/tried-live-data-viewer.py`)

## 2026-06-01

- uv-001: Added uv quickstart scaffold notes (`uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md`)
- ruf-002: Added minimal ruff linter config (`ruff/configs/ruff-linter-settings.toml`)
- mypy-004: Added mypy quickstart for existing projects notes (`mypy/notes/2026-05-29-tried-mypy-quickstart.md`)
- mypy-005: Added minimal mypy strict mode config (`mypy/configs/tried-strict-mypy-config.toml`)
- pyt-001: Added parametrized tests script (`pytest/scripts/test_parametrized.py`)
- uv-002: Added hello-world with dependency script (`uv/scripts/hello-with-dep.py`)
- mypy-002: Added type error detection snippet (`mypy/snippets/tried-mypy-type-errors.py`)

## 2026-05-31

- tox-001: Added tox primer (`tox/notes/0000-primer-tox.md`)
- tox-001 (rework): Rewrote primer to ≤300 words, ≤15 lines, first-person scratchy voice
- tox-002: Added minimal tox config (`tox/configs/tox.ini`)
- tox-003: Added tox CLI first run notes (`tox/notes/2026-05-31-tox-cli-first-run.md`)

## 2026-05-30

- htp-001: Added httpie primer (`httpie/notes/0000-primer-httpie.md`)
- htp-002: Added httpie install and test script (`httpie/scripts/install_and_test_httpie.sh`)
- htp-003: Added httpie vs curl comparison notes (`httpie/notes/2026-05-30-compare-httpie-vs-curl.md`)

- psy-001: Added py-spy primer (`py-spy/notes/0000-primer-py-spy.md`)
- psy-001 (rework): Removed L1-forbidden word "production" from primer — replaced with "in real workloads" and "live systems"
- psy-002: Added py-spy sampling script (`py-spy/scripts/tried-py-spy-sampling.py`)
- psy-003: Added py-spy CLI subcommand notes (`py-spy/notes/2026-05-30-tried-py-spy-cli-subcommands.md`)

- pdt-002: Updated install and inspect script to change to /work before running pipdeptree (pipdeptree/scripts/install-and-inspect-deps.sh)
- pdt-003: Added JSON format and dependency type notes (pipdeptree/notes/2026-05-30-format-json-and-identify-deps.md)
## 2026-05-29

- pdt-001: Added pipdeptree primer (`pipdeptree/notes/0000-primer-pipdeptree.md`)
- pdt-002: Added install and inspect script (`pipdeptree/scripts/install-and-inspect-deps.sh`)
- pdt-003: Added JSON format notes (`pipdeptree/notes/2026-05-29-format-json-deps.md`)

- typ-001: Added Typer primer (`typer/notes/0000-primer-typer.md`)
- typ-002: Added minimal CLI app script (`typer/scripts/typer_cli_demo.py`)
- typ-003: Added Typer quickstart notes (`typer/notes/2026-05-29-typer-quickstart-notes.md`)

## 2026-05-28

- prc-001: Added pre-commit run notes (`pre-commit/notes/2026-05-28-run-pre-commit-on-work.md`)
- ric-001: Added rich table/panel/progress script (`rich/scripts/first-table-panel-progress.py`)
- ric-002: Added rich renderables exploration notes (`rich/notes/2026-05-28-exploring-renderables.md`)

- myp-001: Added mypy primer (`mypy/notes/0000-primer-mypy.md`)
- myp-002: Added first mypy type check script (`mypy/scripts/tried-mypy-first-check.py`)
- myp-003: Added mypy CLI flags notes (`mypy/notes/2026-05-28-tried-mypy-cli-flags.md`)

## 2026-05-27

- py-031: Added rich console logging snippet (`rich/snippets/first-rich-logger.py`)
- py-032: Added rich themes and markdown notes (`rich/notes/2026-05-27-tried-rich-themes-and-markdown.md`)
- py-033: Added rich progress bar snippet (`rich/snippets/tried-rich-progress-bar.py`)

- py-020: Added pre-commit config snippet (`pre-commit/snippets/first-pre-commit-config.yaml`)
- py-021: Added install pre-commit script (`pre-commit/scripts/install-and-run.sh`)
- py-053: Restructured README with documented repository structure (`docs/repository-structure.md`)
- py-025: Added pip-audit ignore list config (`pip-audit/configs/pip-audit-ignore.toml`)
- py-026: Added Ty primer (`ty/notes/0000-primer-ty.md`)
- py-027: Added Ty run snippet (`ty/snippets/run-ty-on-codebase.py`)

## 2026-05-26

- py-022: Added pip-audit primer (`pip-audit/notes/0000-primer-pip-audit.md`)
- py-023: Added scan project script (`pip-audit/scripts/scan-project.sh`)
- py-024: Added pip-audit findings notes (`pip-audit/notes/2026-05-26-pip-audit-findings.md`)

- py-017: Added uv pyproject.toml settings config (`uv/configs/2026-05-26-uv-pyproject-settings.toml`)
- py-018: Added uv CLI beyond basics notes (`uv/notes/2026-05-26-cli-commands-beyond-basics.md`)
- py-019: Added pre-commit primer (`pre-commit/notes/0000-primer-pre-commit.md`)

- py-014: Added uv.lock structure notes (`uv.lock/notes/2026-05-26-uv-lock-structure.md`)
- py-015: Added generate uv.lock script (`uv.lock/scripts/generate-uv-lock.sh`)
- py-016: Added uv run snippet (`uv/snippets/run-with-uv.py`)

- py-008: Added pytest first test snippet (`pytest/snippets/test_first_test.py`)
- py-009: Added pytest CLI exploration notes (`pytest/notes/2026-05-26-tried-pytest-cli.md`)
- py-010: Added pyproject.toml primer (`pyproject.toml/notes/0000-primer-pyproject.toml.md`)
- py-011: Added minimal pyproject.toml config (`pyproject.toml/configs/minimal-pyproject.toml`)
- py-011 (rework): Fixed build-backend to `setuptools.build_meta` (`pyproject.toml/configs/minimal-pyproject.toml`)
- py-012: Added pyproject.toml settings notes (`pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md`)
- py-013: Added uv.lock primer (`uv.lock/notes/0000-primer-uv.lock.md`)

## 2026-05-25

- py-005: Added Ruff install script (`py/scripts/install-and-lint.sh`)
- py-006: Added Ruff config (`py/configs/ruff-pyproject.toml`)
- py-007: Added pytest primer (`pytest/notes/0000-primer-pytest.md`)
- py-004: Added Ruff primer (`py/notes/0000-primer-py.md`)

## 2026-05-24

- py-001: Added uv primer (`uv/notes/0000-primer-uv.md`)
- py-002: Added uv install script (`uv/scripts/install-and-first-command.sh`)
- py-003: Added uv virtual env notes (`uv/notes/2026-05-24-virtual-env-uv.md`)
