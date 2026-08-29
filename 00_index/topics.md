# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Foundational concepts  ·  38 files

- **primer:** [Git Version Control](../docs/concepts/git-version-control/0000-primer-git-version-control.md)
- **primer:** [Python Programming Fundamentals](../docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md)
- **primer:** [Python Packaging & Project Config](../docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md)
- **primer:** [Software Testing Principles](../docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md)
- **primer:** [Static Type Checking & Type Hints](../docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md)
- **primer:** [Virtual Environment & Dependency Mgmt](../docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md)
- **primer:** [Security Best Practices](../docs/concepts/security-best-practices/0000-primer-security-best-practices.md)
- **docs** (6): [git-workflows-branches-tags-ci](../docs/concepts/git-version-control/git-workflows-branches-tags-ci.md), [typing-patterns-protocol-typeddict-generics](../docs/concepts/static-type-checking-type-hints/typing-patterns-protocol-typeddict-generics.md), [venv-strategies-venv-uv-tox](../docs/concepts/virtual-environment-dependency-mgmt/venv-strategies-venv-uv-tox.md), [combining-fundamentals-with-static-typing-and-testing](../docs/concepts/python-programming-fundamentals/combining-fundamentals-with-static-typing-and-testing.md), [repository-structure](../docs/repository-structure.md), [ci-ready-static-checking-pytest-pyproject](../docs/concepts/static-type-checking-type-hints/ci-ready-static-checking-pytest-pyproject.md), [choosing-build-backend](../docs/concepts/python-packaging-project-config/choosing-build-backend.md)
- **notebooks** (1): [type-narrowing-mypy-integration](../docs/concepts/static-type-checking-type-hints/notebooks/type-narrowing-mypy-integration.ipynb)
- **scripts** (10): [derive-version-from-git-tags](../docs/concepts/git-version-control/scripts/derive-version-from-git-tags.py), [build-verify-wheel](../docs/concepts/python-packaging-project-config/scripts/2026-08-12-build-verify-wheel.py), [dependency-management-cli](../docs/concepts/python-programming-fundamentals/scripts/dependency-management-cli.py), [lockfile-drift-check](../docs/concepts/virtual-environment-dependency-mgmt/scripts/lockfile-drift-check.py), [dataclasses-context-managers-decorators](../docs/concepts/python-programming-fundamentals/scripts/2026-08-27-dataclasses-context-managers-decorators.py), [2026-07-05-practice-git-version-control](../docs/concepts/git-version-control/scripts/2026-07-23-practice-git-version-control.py), [2026-08-21-build-validate-src-layout-package](../docs/concepts/python-packaging-project-config/scripts/2026-08-21-build-validate-src-layout-package.py), [build-verify-smoke-install-wheel](../docs/concepts/python-packaging-project-config/scripts/build-verify-smoke-install-wheel.py), [2026-07-05-practicing-fundamentals](../docs/concepts/python-programming-fundamentals/scripts/2026-07-05-practicing-fundamentals.py), [2026-07-27-applying-type-hints](../docs/concepts/static-type-checking-type-hints/scripts/2026-07-27-applying-type-hints.py), [2026-07-05-testing-principles](../docs/concepts/software-testing-principles/scripts/2026-07-05-testing-principles.py), [parametrized-edge-case-coverage-ci](../docs/concepts/software-testing-principles/scripts/parametrized-edge-case-coverage-ci.py), [2026-07-23-venv-practice](../docs/concepts/virtual-environment-dependency-mgmt/scripts/2026-07-23-venv-practice.py)
- _…and 3 more under `docs/concepts/*/scripts/` — browse the folders._
- **snippets** (9): [2026-08-20-parametrized-aaa-tests](../docs/concepts/software-testing-principles/snippets/2026-08-20-parametrized-aaa-tests.py), [comprehensions-generators-error-handling](../docs/concepts/python-programming-fundamentals/snippets/2026-08-11-comprehensions-generators-error-handling.py), [boundary-values-test-doubles](../docs/concepts/software-testing-principles/snippets/2026-08-12-boundary-values-test-doubles.py), [common-git-patterns](../docs/concepts/git-version-control/snippets/2026-07-23-common-git-patterns-in-python-projects.py), [2026-08-27-secure-coding-patterns](../docs/concepts/security-best-practices/snippets/2026-08-27-secure-coding-patterns.py), [2026-07-05-packaging-patterns](../docs/concepts/python-packaging-project-config/snippets/2026-07-05-packaging-patterns.py), [common-type-checking-patterns](../docs/concepts/static-type-checking-type-hints/snippets/2026-07-23-common-type-checking-patterns.py), [2026-07-27-common-venv-patterns](../docs/concepts/virtual-environment-dependency-mgmt/snippets/2026-07-27-common-venv-patterns.py)
- _…and 1 more under `docs/concepts/*/snippets/` — browse the folders._

## httpie  ·  18 files

- **primer:** [0000-primer-httpie.md](../httpie/notes/0000-primer-httpie.md)
- **notes** (6): [installed-httpie-first-api-request](../httpie/notes/2026-08-27-installed-httpie-first-api-request.md), [followed-httpie-quickstart](../httpie/notes/2026-07-19-followed-httpie-quickstart.md), [first-httpie-request](../httpie/notes/2026-06-10-first-httpie-request.md)
- _…and 3 more under `httpie/notes/` — browse the folder._
- **docs** (2): [integrating-httpie-jq-shell-pipelines](../httpie/docs/integrating-httpie-jq-shell-pipelines.md), [scripting-request-items-offline-gating](../httpie/docs/scripting-request-items-offline-gating.md)
- **scripts** (5): [ci-safe-api-smoke-test](../httpie/scripts/ci-safe-api-smoke-test.sh), [httpie-request-workflow](../httpie/scripts/2026-07-19-httpie-request-workflow.sh), [install_and_test_httpie](../httpie/scripts/install_and_test_httpie.sh), [ci-httpie-wrapper](../httpie/scripts/ci-httpie-wrapper.sh), [multi-endpoint-smoke-runner](../httpie/scripts/multi-endpoint-smoke-runner.sh)
- **configs** (2): [httpie-session-dev](../httpie/configs/2026-08-27-httpie-session-dev.json), [httpie-defaults](../httpie/configs/2026-07-19-httpie-defaults.json)
- **snippets** (2): [httpie-core-syntax](../httpie/snippets/2026-08-27-httpie-core-syntax.sh), [tried-httpie-get-post-workflow](../httpie/snippets/tried-httpie-get-post-workflow.py)
- **notebooks** (1): [compare-session-vs-inline-auth](../httpie/notebooks/compare-session-vs-inline-auth.ipynb)

## mypy  ·  21 files

- **primer:** [0000-primer-mypy.md](../mypy/notes/0000-primer-mypy.md)
- **notes** (7): [followed-mypy-quickstart](../mypy/notes/2026-06-12-followed-mypy-quickstart.md), [tried-mypy-official-quickstart](../mypy/notes/2026-06-08-tried-mypy-official-quickstart.md), [first-mypy-run](../mypy/notes/2026-06-04-first-mypy-run.md)
- **docs** (1): [stub-strategy-ignore-missing-imports](../mypy/docs/stub-strategy-ignore-missing-imports.md)
- **scripts** (2): [tried-mypy-first-check](../mypy/scripts/tried-mypy-first-check.py), [untyped-to-strict-reveal-type](../mypy/scripts/untyped-to-strict-reveal-type.py)
- **configs** (5): [selective-mypy-strictness](../mypy/configs/2026-08-04-selective-mypy-strictness.ini), [strict-mypy-config](../mypy/configs/tried-strict-mypy-config.toml), [strict-disallow-ignore-config](../mypy/configs/tried-strict-disallow-ignore-config.ini), [minimal-mypy-config](../mypy/configs/tried-minimal-mypy-config.ini), [gradual-typing-mypy](../mypy/configs/gradual-typing-mypy.toml)
- **manifests** (1): [ci-incremental-mypy-workflow](../mypy/manifests/ci-incremental-mypy-workflow.yaml) — a fail-fast, cache-warm incremental type-check job
- **notebooks** (1): [gradual-typing-adoption](../mypy/notebooks/gradual-typing-adoption.ipynb)
- **snippets** (4): [typed-small-module](../mypy/snippets/2026-07-19-typed-small-module.py), [tried-mypy-type-errors](../mypy/snippets/tried-mypy-type-errors.py), [typed-functions-validate](../mypy/snippets/tried-validating-typed-function.py)
- _…and 1 more under `mypy/snippets/` — browse the folder._
- _…and 4 more under `mypy/notes/` — browse the folder._

## pau  ·  4 files

- **primer:** [0000-primer-pip-audit.md](../pau/notes/0000-primer-pip-audit.md)
- **configs** (2): [minimal-pip-audit-pyproject](../pau/configs/2026-08-09-minimal-pip-audit-pyproject.toml), [pip-audit-scan-config](../pau/configs/2026-08-09-pip-audit-scan-config.toml)
- **scripts** (1): [ci-friendly-pip-audit-scan](../pau/scripts/2026-08-21-ci-friendly-pip-audit-scan.sh)

## pip-audit  ·  12 files

- **primer:** [0000-primer-pip-audit.md](../pip-audit/notes/0000-primer-pip-audit.md)
- **notes** (4): [followed-pip-audit-quickstart](../pip-audit/notes/2026-07-17-followed-pip-audit-quickstart.md), [installs-and-runs-pip-audit](../pip-audit/notes/2026-06-09-installs-and-runs-pip-audit.md), [pip-audit-findings](../pip-audit/notes/2026-05-26-pip-audit-findings.md)
- **scripts** (3): [scan-project](../pip-audit/scripts/scan-project.sh), [scan-and-parse-json](../pip-audit/scripts/scan-and-parse-json.sh), [audit-and-parse-json](../pip-audit/scripts/2026-06-09-audit-and-parse-json.sh)
- **configs** (1): [pip-audit-ignore](../pip-audit/configs/pip-audit-ignore.toml)
- **snippets** (4): [parse-pip-audit-json-cves-2026-07-13](../pip-audit/snippets/2026-07-13-parse-pip-audit-json-cves.py), [parse-pip-audit-json-cves](../pip-audit/snippets/2026-07-10-parse-pip-audit-json-cves.py), [list-cve-findings](../pip-audit/snippets/list-cve-findings.py)
- _…and 1 more under `pip-audit/snippets/` — browse the folder._

## pipdeptree  ·  18 files

- **primer:** [0000-primer-pipdeptree.md](../pipdeptree/notes/0000-primer-pipdeptree.md)
- **notes** (8): [pipdeptree-tutorial](../pipdeptree/notes/2026-08-06-pipdeptree-tutorial.md), [pipdeptree-patterns-i-use](../pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md), [common-cli-patterns](../pipdeptree/notes/2026-06-13-common-cli-patterns.md)
- **scripts** (3): [dependency-health-report](../pipdeptree/scripts/dependency-health-report.sh), [list-package-deps](../pipdeptree/scripts/list-package-deps.py), [install-and-inspect-deps](../pipdeptree/scripts/install-and-inspect-deps.sh)
- **configs** (1): [dev-dependencies-pipdeptree](../pipdeptree/configs/2026-07-19-dev-dependencies-pipdeptree.toml)
- **snippets** (6): [build-dependency-report](../pipdeptree/snippets/2026-08-04-build-dependency-report.py), [parse-pipdeptree-json](../pipdeptree/snippets/parse-pipdeptree-json.py), [find-reverse-deps](../pipdeptree/snippets/find-reverse-deps.py)
- _…and 3 more under `pipdeptree/snippets/` — browse the folders._

## prc  ·  3 files

- **notes** (1): [first-pre-commit-hook](../prc/notes/2026-08-09-first-pre-commit-hook.md)
- **scripts** (1): [ci-parity-check](../prc/scripts/2026-08-17-ci-parity-check.sh)
- **configs** (1): [pre-commit-config](../prc/configs/2026-08-17-pre-commit-config.yaml)

## pre-commit  ·  11 files

- **primer:** [0000-primer-pre-commit.md](../pre-commit/notes/0000-primer-pre-commit.md)
- **notes** (5): [pre-commit-cli-walkthrough](../pre-commit/notes/2026-06-18-pre-commit-cli-walkthrough.md), [installed-pre-commit-ran-lint-typecheck](../pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md), [installed-pre-commit-explored-cli](../pre-commit/notes/2026-06-10-installed-pre-commit-explored-cli.md)
- **scripts** (2): [run-pre-commit-ruff-trailing-ws](../pre-commit/scripts/run-pre-commit-ruff-trailing-ws.sh), [install-and-run](../pre-commit/scripts/install-and-run.sh)
- **configs** (2): [tried-multi-hook-config](../pre-commit/configs/tried-multi-hook-config.yaml), [tried-first-ruff-hooks-config](../pre-commit/configs/tried-first-ruff-hooks-config.yaml)
- **snippets** (2): [tried-ruff-mypy-config](../pre-commit/snippets/tried-ruff-mypy-config.yaml), [first-pre-commit-config](../pre-commit/snippets/first-pre-commit-config.yaml)

## py  ·  2 files

- **primer:** [0000-primer-py.md](../py/notes/0000-primer-py.md)
- **scripts** (1): [install-and-lint](../py/scripts/install-and-lint.sh)

## py-spy  ·  24 files

- **primer:** [0000-primer-py-spy.md](../py-spy/notes/0000-primer-py-spy.md)
- **notes** (10): [installed-py-spy-profiled-running-process](../py-spy/notes/2026-07-19-installed-py-spy-profiled-running-process.md), [compared-py-spy-record-output-formats (July 10)](../py-spy/notes/2026-07-10-compared-py-spy-record-output-formats.md), [compared-py-spy-record-output-formats (July 8)](../py-spy/notes/2026-07-08-compared-py-spy-record-output-formats.md)
- **docs** (2): [when-to-use-py-spy-top-vs-record-flamegraph-vs-dump](../py-spy/docs/when-to-use-py-spy-top-vs-record-flamegraph-vs-dump.md), [when-to-use-py-spy-modes](../py-spy/docs/when-to-use-py-spy-modes.md)
- **scripts** (10): [profile-tiny-loop-py-spy](../py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh), [profile-running-process-end-to-end](../py-spy/scripts/profile-running-process-end-to-end.sh), [cpu-speedscope-record (July 10)](../py-spy/scripts/2026-07-10-cpu-speedscope-record.py), [cpu-speedscope-record (July 8)](../py-spy/scripts/2026-07-08-cpu-speedscope-record.py)
- **snippets** (2): [tried-cpu-bound-simulation](../py-spy/snippets/tried-cpu-bound-simulation.py), [tried-profile-running-process](../py-spy/snippets/tried-profile-running-process.py)
- _…and 7 more under `py-spy/notes/` and 6 more under `py-spy/scripts/` — browse the folders._

## pyproject.toml  ·  11 files

- **primer:** [0000-primer-pyproject.toml.md](../pyproject.toml/notes/0000-primer-pyproject.toml.md)
- **notes** (4): [pyproject-toml-settings](../pyproject.toml/notes/2026-05-26-pyproject-toml-settings.md), [explored-pyproject-build-system](../pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md), [what-tripped-me-up-pyproject-toml](../pyproject.toml/notes/2026-08-22-what-tripped-me-up-pyproject-toml.md)
- **configs** (6): [multi-tool-pyproject.toml](../pyproject.toml/configs/multi-tool-pyproject.toml), [first-pep621-pyproject.toml](../pyproject.toml/configs/first-pep621-pyproject.toml), [minimal-pyproject.toml](../pyproject.toml/configs/minimal-pyproject.toml), [minimal-pep621-pyproject](../pyproject.toml/configs/2026-08-22-minimal-pep621-pyproject.toml)
- _…and 2 more under `pyproject.toml/configs/` — browse the folder._
- **scripts** (1): [validate-pyproject-tomllib](../pyproject.toml/scripts/2026-08-22-validate-pyproject-tomllib.py)

## pytest  ·  15 files

- **primer:** [0000-primer-pytest.md](../pytest/notes/0000-primer-pytest.md)
- **notes** (5): [explored-pytest-cli-advanced-flags](../pytest/notes/2026-06-10-explored-pytest-cli-advanced-flags.md), [installed-pytest-first-suite](../pytest/notes/2026-06-08-installed-pytest-first-suite.md), [tried-pytest-fixtures-conftest](../pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md)
- **scripts** (4): [test_parametrized](../pytest/scripts/test_parametrized.py), [run-pytest-with-cli-flags](../pytest/scripts/run-pytest-with-cli-flags.sh), [install-and-run-first-pytest](../pytest/scripts/install-and-run-first-pytest.sh), [fixture-and-parametrize-suite](../pytest/scripts/fixture-and-parametrize-suite.py)
- **configs** (1): [minimal-pytest-config](../pytest/configs/2026-07-19-minimal-pytest-config.toml)
- **docs** (2): [pytest-vs-unittest-mapping](../pytest/docs/pytest-vs-unittest-mapping.md), [fixtures-conftest-scoping](../pytest/docs/fixtures-conftest-scoping.md)
- **snippets** (2): [test_first_test](../pytest/snippets/test_first_test.py), [three_basic_tests](../pytest/snippets/three_basic_tests.py)
- **notebooks** (1): [red-green-refactor-loop](../pytest/notebooks/red-green-refactor-loop.ipynb)

## pyright  ·  1 file

- **primer:** [0000-primer-pyright.md](../pyright/notes/0000-primer-pyright.md)

## rich  ·  19 files

- **primer:** [0000-primer-rich.md](../rich/notes/0000-primer-rich.md)
- **notes** (8): [followed-rich-quickstart](../rich/notes/2026-08-05-followed-rich-quickstart.md), [explored-rich-console-api-renderables](../rich/notes/2026-06-17-explored-rich-console-api-renderables.md), [tried-rich-cli](../rich/notes/2026-06-09-tried-rich-cli.md)
- **scripts** (3): [first-styled-rich-output](../rich/scripts/2026-08-07-first-styled-rich-output.py), [rich-styled-output-tables-progress](../rich/scripts/2026-08-05-rich-styled-output-tables-progress.py), [first-table-panel-progress](../rich/scripts/first-table-panel-progress.py)
- **snippets** (8): [rich-inspect-live-pipeline](../rich/snippets/2026-08-06-rich-inspect-live-pipeline.py), [first-rich-output](../rich/snippets/2026-08-18-first-rich-output.py), [tried-rich-console-panel-table](../rich/snippets/tried-rich-console-panel-table.py)
- _…and 4 more under `rich/notes/` and 5 more under `rich/snippets/` — browse the folders._

## ruff  ·  15 files

- **primer:** [0000-primer-ruff.md](../ruff/notes/0000-primer-ruff.md)
- **notes** (6): [ruff-select-ignore-extend-safe-overrides](../ruff/notes/2026-07-21-ruff-select-ignore-extend-safe-overrides.md), [tripped-on-ruff-first-project](../ruff/notes/2026-07-19-tripped-on-ruff-first-project.md), [tried-ruff-cli-more-flags](../ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md)
- **configs** (5): [pinned-rule-set](../ruff/configs/2026-08-18-pinned-rule-set.toml), [minimal-standalone-ruff-2026-07-21](../ruff/configs/2026-07-21-minimal-standalone-ruff.toml), [ruff-linter-settings.toml](../ruff/configs/ruff-linter-settings.toml)
- **docs** (1): [ruff-vs-flake8-comparison](../ruff/docs/ruff-vs-flake8-comparison.md)
- **scripts** (1): [end-to-end-ruff-lint-format](../ruff/scripts/end-to-end-ruff-lint-format.sh)
- **snippets** (2): [tried-messy-example](../ruff/snippets/tried-messy-example.py), [messy_example](../ruff/snippets/messy_example.py)
- _…and 2 more under `ruff/configs/` — browse the folder._

## tox  ·  11 files

- **primer:** [0000-primer-tox.md](../tox/notes/0000-primer-tox.md)
- **notes** (5): [followed-tox-quickstart](../tox/notes/2026-06-11-followed-tox-quickstart.md), [tox-quickstart](../tox/notes/2026-06-08-tox-quickstart.md), [first-tox-run-tripped-me-up](../tox/notes/2026-06-08-first-tox-run-tripped-me-up.md)
- **configs** (4): [tox.ini](../tox/configs/tox.ini), [tried-lint-and-test-env.ini](../tox/configs/tried-lint-and-test-env.ini), [tox-env-matrix](../tox/configs/2026-08-22-tox-env-matrix.toml), [2026-08-26-minimal-tox-matrix](../tox/configs/2026-08-26-minimal-tox-matrix.toml)
- **scripts** (2): [install-tox-and-first-env](../tox/scripts/2026-08-05-install-tox-and-first-env.sh), [tried-minimal-tox-run](../tox/scripts/tried-minimal-tox-run.sh)

## ty  ·  15 files

- **primer:** [0000-primer-ty.md](../ty/notes/0000-primer-ty.md)
- **notes** (7): [followed-ty-quickstart](../ty/notes/2026-08-04-followed-ty-quickstart.md), [first-ty-type-check](../ty/notes/2026-06-18-first-ty-type-check.md), [explored-ty-cli-flags](../ty/notes/2026-06-16-explored-ty-cli-flags.md)
- **configs** (3): [minimal-ty-config](../ty/configs/2026-08-05-minimal-ty-config.toml), [tried-ty-config.toml](../ty/configs/tried-ty-config.toml), [tried-ty-markdown-css.css](../ty/configs/tried-ty-markdown-css.css)
- **scripts** (1): [tried-ty-pipeline](../ty/scripts/tried-ty-pipeline.sh)
- **snippets** (4): [minimal-annotated-module](../ty/snippets/2026-08-18-minimal-annotated-module.py), [ty-type-checking-workflow](../ty/snippets/2026-08-04-ty-type-checking-workflow.py), [run-ty-on-codebase](../ty/snippets/run-ty-on-codebase.py)
- _…and 1 more under `ty/notes/` — browse the folder._

## typer  ·  10 files

- **primer:** [0000-primer-typer.md](../typer/notes/0000-primer-typer.md)
- **notes** (4): [tripped-up-typer-quickstart](../typer/notes/2026-08-18-tripped-up-typer-quickstart.md), [first-typer-hello-world](../typer/notes/2026-06-10-first-typer-hello-world.md), [typer-quickstart-notes](../typer/notes/2026-05-29-typer-quickstart-notes.md)
- **scripts** (4): [quickstart-args-options-help](../typer/scripts/2026-08-18-quickstart-args-options-help.py), [todo-cli](../typer/scripts/2026-08-20-todo-cli.py), [typer_cli_demo](../typer/scripts/typer_cli_demo.py), [tried-typer-calculator](../typer/scripts/tried-typer-calculator.py)
- **snippets** (2): [typer-cli-option-and-subcommand](../typer/snippets/2026-07-05-typer-cli-option-and-subcommand.py), [tried-first-typer-cli-app](../typer/snippets/tried-first-typer-cli-app.py)

## uv  ·  20 files

- **primer:** [0000-primer-uv.md](../uv/notes/0000-primer-uv.md)
- **notes** (8): [uv-script-venv-lockfile](../uv/notes/2026-08-09-tried-uv-script-venv-lockfile.md), [uv-quickstart-tripped-up](../uv/notes/2026-08-05-uv-quickstart-tripped-up.md), [explored-uv-cli-help-and-format](../uv/notes/2026-06-16-explored-uv-cli-help-and-format.md)
- **scripts** (5): [bootstrap-project-lockcheck](../uv/scripts/bootstrap-project-lockcheck.sh), [install-and-first-command](../uv/scripts/install-and-first-command.sh), [hello-with-dep](../uv/scripts/hello-with-dep.py), [uv-workflow](../uv/scripts/2026-07-19-uv-workflow.sh)
- **configs** (3): [uv-dependency-groups-pyproject](../uv/configs/uv-dependency-groups-pyproject.toml), [uv-managed-project](../uv/configs/2026-07-19-uv-managed-project.toml), [uv-pyproject-settings](../uv/configs/2026-05-26-uv-pyproject-settings.toml)
- **docs** (2): [uv-vs-pip-cheat-sheet](../uv/docs/2026-06-05-uv-vs-pip-cheat-sheet.md), [uv-workflows-run-uvx-tools-version-pinning](../uv/docs/2026-08-22-uv-workflows-run-uvx-tools-version-pinning.md)
- **snippets** (2): [first-uv-project](../uv/snippets/2026-08-08-first-uv-project.py), [run-with-uv](../uv/snippets/run-with-uv.py)
- _…and 5 more under `uv/notes/` — browse the folder._

## uv.lock  ·  11 files

- **primer:** [0000-primer-uv.lock.md](../uv.lock/notes/0000-primer-uv.lock.md)
- **notes** (4): [uv-lock-packages-checksums-markers](../uv.lock/notes/2026-06-18-uv-lock-packages-checksums-markers.md), [generated-first-uv-lock](../uv.lock/notes/2026-06-11-generated-first-uv-lock.md), [uv-lock-structure](../uv.lock/notes/2026-05-26-uv-lock-structure.md)
- **scripts** (4): [tried-generate-from-pyproject-toml](../uv.lock/scripts/tried-generate-from-pyproject-toml.sh), [tried-uv-lock-reproducibility](../uv.lock/scripts/tried-uv-lock-reproducibility.sh), [generate-uv-lock](../uv.lock/scripts/generate-uv-lock.sh)
- **snippets** (2): [tried-reading-uv-lock](../uv.lock/snippets/tried-reading-uv-lock.py), [tried-detect-conflicting-constraints](../uv.lock/snippets/tried-detect-conflicting-constraints.py)
- **notebooks** (1): [exploring-uv-lock-structure.ipynb](../uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb)

## uvl  ·  6 files

- **primer:** [0000-primer-uv.lock.md](../uvl/notes/0000-primer-uv.lock.md)
- **notes** (2): [uv-lock-mapping-to-pyproject](../uvl/notes/2026-08-04-uv-lock-mapping-to-pyproject.md)
- **docs** (2): [uv-lock-dependencies](../uvl/docs/2026-08-08-uv-lock-dependencies.md), [reading-uv-lock-entries-hashes-sources](../uvl/docs/reading-uv-lock-entries-hashes-sources.md)
- **scripts** (1): [lockfile-reproducibility-check](../uvl/scripts/lockfile-reproducibility-check.sh)
- **notebooks** (1): [uv-lock-evolution-add-upgrade](../uvl/notebooks/uv-lock-evolution-add-upgrade.ipynb)
