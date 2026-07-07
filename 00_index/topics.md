# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Foundational concepts  ·  7 files

- [Git Version Control primer](../docs/concepts/git-version-control/0000-primer-git-version-control.md) — Commits, branches, remotes, and how it connects to pre-commit hooks
- [Python Packaging & Project Config primer](../docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md) — pyproject.toml, PEP 517/621, build backends, entry points
- [Python Programming Fundamentals primer](../docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md) — Basic syntax, functions, modules, error handling
- [Software Testing Principles primer](../docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md) — What makes a good test, assertions, fixtures
- [Static Type Checking & Type Hints primer](../docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md) — Type annotations, gradual typing, type checkers
- [Virtual Environment & Dependency Mgmt primer](../docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md) — Isolated environments, installing packages, lockfiles
- [Repository structure](../docs/repository-structure.md) — Directory layout and quick reference

## httpie  ·  6 files

- **primer:** [0000-primer-httpie.md](../httpie/notes/0000-primer-httpie.md)
- **notes** (4): [compare-httpie-vs-curl](../httpie/notes/2026-05-30-compare-httpie-vs-curl.md), [first-httpie-request-tripped-me-up](../httpie/notes/2026-06-06-first-httpie-request-tripped-me-up.md), [first-httpie-request](../httpie/notes/2026-06-10-first-httpie-request.md)
- **scripts** (1): [install_and_test_httpie.sh](../httpie/scripts/install_and_test_httpie.sh)
- **snippets** (1): [tried-httpie-get-post-workflow.py](../httpie/snippets/tried-httpie-get-post-workflow.py)

## mypy  ·  14 files

- **primer:** [0000-primer-mypy.md](../mypy/notes/0000-primer-mypy.md)
- **notes** (7): [tried-mypy-official-quickstart](../mypy/notes/2026-06-08-tried-mypy-official-quickstart.md), [followed-mypy-quickstart](../mypy/notes/2026-06-12-followed-mypy-quickstart.md), [tried-mypy-cli-flags](../mypy/notes/2026-05-28-tried-mypy-cli-flags.md)
- **configs** (3): [strict-disallow-ignore-config.ini](../mypy/configs/tried-strict-disallow-ignore-config.ini), [strict-mypy-config.toml](../mypy/configs/tried-strict-mypy-config.toml), [minimal-mypy-config.ini](../mypy/configs/tried-minimal-mypy-config.ini)
- **scripts** (1): [tried-mypy-first-check.py](../mypy/scripts/tried-mypy-first-check.py)
- **snippets** (3): [tried-mypy-type-errors.py](../mypy/snippets/tried-mypy-type-errors.py), [typed-functions-validate.py](../mypy/snippets/typed-functions-validate.py), [tried-validating-typed-function.py](../mypy/snippets/tried-validating-typed-function.py)
- _and 3 more under `mypy/` — browse the folder._

## pip-audit  ·  9 files

- **primer:** [0000-primer-pip-audit.md](../pip-audit/notes/0000-primer-pip-audit.md)
- **notes** (3): [pip-audit-findings](../pip-audit/notes/2026-05-26-pip-audit-findings.md), [installs-and-runs](../pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md)
- **scripts** (3): [scan-project.sh](../pip-audit/scripts/scan-project.sh), [scan-and-parse-json.sh](../pip-audit/scripts/scan-and-parse-json.sh), [audit-and-parse-json.sh](../pip-audit/scripts/2026-06-09-audit-and-parse-json.sh)
- **configs** (1): [pip-audit-ignore.toml](../pip-audit/configs/pip-audit-ignore.toml)
- **snippets** (2): [list-cve-findings.py](../pip-audit/snippets/list-cve-findings.py), [tried-list-cves.py](../pip-audit/snippets/tried-list-cves.py)

## pipdeptree  ·  13 files

- **primer:** [0000-primer-pipdeptree.md](../pipdeptree/notes/0000-primer-pipdeptree.md)
- **notes** (7): [pipdeptree-patterns-i-use](../pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md), [common-cli-patterns](../pipdeptree/notes/2026-06-13-common-cli-patterns.md), [followed-quickstart](../pipdeptree/notes/2026-06-09-followed-pipdeptree-quickstart.md)
- **scripts** (1): [install-and-inspect-deps.sh](../pipdeptree/scripts/install-and-inspect-deps.sh)
- **snippets** (5): [parse-pipdeptree-json.py](../pipdeptree/snippets/parse-pipdeptree-json.py), [find-reverse-deps.py](../pipdeptree/snippets/find-reverse-deps.py), [check-package-deps.py](../pipdeptree/snippets/check-package-deps.py)
- _and 5 more under `pipdeptree/` — browse the folder._

## pre-commit  ·  10 files

- **primer:** [0000-primer-pre-commit.md](../pre-commit/notes/0000-primer-pre-commit.md)
- **notes** (5): [pre-commit-cli-walkthrough](../pre-commit/notes/2026-06-18-pre-commit-cli-walkthrough.md), [installed-lint-typecheck](../pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md), [installed-explored-cli](../pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md)
- **configs** (2): [multi-hook-config.yaml](../pre-commit/configs/tried-multi-hook-config.yaml), [first-ruff-hooks-config.yaml](../pre-commit/configs/tried-first-ruff-hooks-config.yaml)
- **scripts** (1): [install-and-run.sh](../pre-commit/scripts/install-and-run.sh)
- **snippets** (2): [first-pre-commit-config.yaml](../pre-commit/snippets/first-pre-commit-config.yaml), [ruff-mypy-config.yaml](../pre-commit/snippets/tried-ruff-mypy-config.yaml)
- _and 1 more under `pre-commit/` — browse the folder._

## py  ·  2 files

- **primer:** [0000-primer-py.md](../py/notes/0000-primer-py.md)
- **scripts** (1): [install-and-lint.sh](../py/scripts/install-and-lint.sh)

## py-spy  ·  14 files

- **primer:** [0000-primer-py-spy.md](../py-spy/notes/0000-primer-py-spy.md)
- **notes** (7): [my-py-spy-workflow](../py-spy/notes/2026-06-13-my-py-spy-workflow.md), [compared-record-output-formats](../py-spy/notes/2026-06-13-compared-py-spy-record-output-formats.md), [followed-quickstart](../py-spy/notes/2026-06-10-followed-py-spy-quickstart.md)
- **scripts** (5): [tried-cpu-speedscope-record.py](../py-spy/scripts/tried-cpu-speedscope-record.py), [tried-py-spy-speedscope-record.py](../py-spy/scripts/tried-py-spy-speedscope-record.py), [tried-py-spy-record-flamegraph.sh](../py-spy/scripts/tried-py-spy-record-flamegraph.sh)
- **snippets** (2): [tried-cpu-bound-simulation.py](../py-spy/snippets/tried-cpu-bound-simulation.py), [tried-profile-running-process.py](../py-spy/snippets/tried-profile-running-process.py)
- _and 5 more under `py-spy/` — browse the folder._

## pyproject.toml  ·  7 files

- **primer:** [0000-primer-pyproject.toml.md](../pyproject.toml/notes/0000-primer-pyproject.toml.md)
- **notes** (3): [build-system-config](../pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md), [settings](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md)
- **configs** (4): [multi-tool-pyproject.toml](../pyproject.toml/configs/multi-tool-pyproject.toml), [first-pep621-pyproject.toml](../pyproject.toml/configs/first-pep621-pyproject.toml), [minimal-pyproject.toml](../pyproject.toml/configs/minimal-pyproject.toml), [first-pep621-config.toml](../pyproject.toml/configs/first-pep621-config.toml)

## pytest  ·  11 files

- **primer:** [0000-primer-pytest.md](../pytest/notes/0000-primer-pytest.md)
- **notes** (5): [cli-advanced-flags](../pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md), [installed-first-suite](../pytest/notes/2026-06-08-installed-pytest-first-suite.md), [fixtures-conftest](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md)
- **scripts** (3): [test_parametrized.py](../pytest/scripts/test_parametrized.py), [run-pytest-with-cli-flags.sh](../pytest/scripts/run-pytest-with-cli-flags.sh), [install-and-run-first-pytest.sh](../pytest/scripts/install-and-run-first-pytest.sh)
- **docs** (1): [pytest-vs-unittest-mapping.md](../pytest/docs/pytest-vs-unittest-mapping.md)
- **snippets** (2): [test_first_test.py](../pytest/snippets/test_first_test.py), [three_basic_tests.py](../pytest/snippets/three_basic_tests.py)

## rich  ·  14 files

- **primer:** [0000-primer-rich.md](../rich/notes/0000-primer-rich.md)
- **notes** (7): [console-api-renderables](../rich/notes/2026-06-17-explored-rich-console-api-renderables.md), [rich-cli](../rich/notes/2026-06-09-tried-rich-cli.md), [console-api](../rich/notes/2026-06-04-tried-rich-console-api.md)
- **scripts** (1): [first-table-panel-progress.py](../rich/scripts/first-table-panel-progress.py)
- **snippets** (6): [tried-live-data-viewer.py](../rich/snippets/tried-live-data-viewer.py), [tried-rich-console-panel-table.py](../rich/snippets/tried-rich-console-panel-table.py), [tried-rich-styled-output.py](../rich/snippets/tried-rich-styled-output.py)
- _and 6 more under `rich/` — browse the folder._

## ruff  ·  9 files

- **primer:** [0000-primer-ruff.md](../ruff/notes/0000-primer-ruff.md)
- **notes** (4): [cli-more-flags](../ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md), [cli-exploration](../ruff/notes/2026-06-06-cli-exploration.md), [quickstart](../ruff/notes/2026-06-03-tried-ruff-quickstart.md)
- **configs** (2): [ruff-linter-settings.toml](../ruff/configs/ruff-linter-settings.toml), [ruff-pyproject.toml](../ruff/configs/ruff-pyproject.toml)
- **docs** (1): [ruff-vs-flake8-comparison.md](../ruff/docs/ruff-vs-flake8-comparison.md)
- **snippets** (2): [messy_example.py](../ruff/snippets/messy_example.py), [tried-messy-example.py](../ruff/snippets/tried-messy-example.py)

## tox  ·  8 files

- **primer:** [0000-primer-tox.md](../tox/notes/0000-primer-tox.md)
- **notes** (5): [followed-quickstart](../tox/notes/2026-06-11-followed-tox-quickstart.md), [quickstart](../tox/notes/2026-06-08-tox-quickstart.md), [cli-first-run](../tox/notes/2026-05-31-tox-cli-first-run.md)
- **configs** (2): [tox.ini](../tox/configs/tox.ini), [tried-lint-and-test-env.ini](../tox/configs/tried-lint-and-test-env.ini)
- **scripts** (1): [tried-minimal-tox-run.sh](../tox/scripts/tried-minimal-tox-run.sh)
- _and 1 more under `tox/` — browse the folder._

## ty  ·  11 files

- **primer:** [0000-primer-ty.md](../ty/notes/0000-primer-ty.md)
- **notes** (6): [first-ty-type-check](../ty/notes/2026-06-18-first-ty-type-check.md), [cli-flags-formats](../ty/notes/2026-06-16-explored-ty-cli-flags.md), [first-markdown-render](../ty/notes/2026-06-10-first-ty-markdown-render.md)
- **configs** (2): [tried-ty-config.toml](../ty/configs/tried-ty-config.toml), [tried-ty-markdown-css.css](../ty/configs/tried-ty-markdown-css.css)
- **scripts** (1): [tried-ty-pipeline.sh](../ty/scripts/tried-ty-pipeline.sh)
- **snippets** (2): [run-ty-on-codebase.py](../ty/snippets/run-ty-on-codebase.py), [tried-ty-vs-mypy.py](../ty/snippets/tried-ty-vs-mypy.py)
- _and 2 more under `ty/` — browse the folder._

## typer  ·  6 files

- **primer:** [0000-primer-typer.md](../typer/notes/0000-primer-typer.md)
- **notes** (3): [first-typer-hello-world](../typer/notes/2026-06-10-first-typer-hello-world.md), [quickstart-tripped-me](../typer/notes/2026-05-29-typer-quickstart-notes.md)
- **scripts** (2): [typer_cli_demo.py](../typer/scripts/typer_cli_demo.py), [tried-typer-calculator.py](../typer/scripts/tried-typer-calculator.py)
- **snippets** (1): [tried-first-typer-cli-app.py](../typer/snippets/tried-first-typer-cli-app.py)

## uv  ·  12 files

- **primer:** [0000-primer-uv.md](../uv/notes/0000-primer-uv.md)
- **notes** (6): [cli-help-and-format](../uv/notes/2026-06-16-explored-uv-cli-help-and-format.md), [installed-first-command](../uv/notes/2026-06-10-installed-uv-first-command.md), [quickstart-scaffold](../uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md)
- **scripts** (3): [install-and-first-command.sh](../uv/scripts/install-and-first-command.sh), [hello-with-dep.py](../uv/scripts/hello-with-dep.py), [tried-bootstrap-uv-script.sh](../uv/scripts/tried-bootstrap-uv-script.sh)
- **configs** (1): [uv-pyproject-settings.toml](../uv/configs/2026-05-26-uv-pyproject-settings.toml)
- **snippets** (1): [run-with-uv.py](../uv/snippets/run-with-uv.py)
- **docs** (1): [uv-vs-pip-cheat-sheet.md](../uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md)
- _and 2 more under `uv/` — browse the folder._

## uv.lock  ·  11 files

- **primer:** [0000-primer-uv.lock.md](../uv.lock/notes/0000-primer-uv.lock.md)
- **notes** (4): [packages-checksums-markers](../uv.lock/notes/2026-06-18-uv-lock-packages-checksums-markers.md), [generated-first-lock](../uv.lock/notes/2026-06-11-generated-first-uv-lock.md), [structure](../uv.lock/notes/2026-05-26-uv-lock-structure.md)
- **scripts** (4): [generate-uv-lock.sh](../uv.lock/scripts/generate-uv-lock.sh), [tried-extract-direct-deps.py](../uv.lock/scripts/tried-extract-direct-deps.py), [tried-uv-lock-reproducibility.sh](../uv.lock/scripts/tried-uv-lock-reproducibility.sh)
- **snippets** (2): [tried-reading-uv-lock.py](../uv.lock/snippets/tried-reading-uv-lock.py), [tried-detect-conflicting-constraints.py](../uv.lock/snippets/tried-detect-conflicting-constraints.py)
- **notebooks** (1): [exploring-uv-lock-structure.ipynb](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb)
- _and 1 more under `uv.lock/` — browse the folder._
