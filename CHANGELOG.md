# CHANGELOG

## 2026-09-06
- psy-020: Added production py-spy profiling runbook (`py-spy/docs/production-profiling-runbook.md`) — profiling live services without downtime, sampling rate selection, flamegraph interpretation, and containerized service handling
- pau-015: Added pip-audit + uv + pre-commit integration docs (`pau/docs/integrating-pip-audit-uv-pre-commit-vulnerability-workflow.md`) — wiring pip-audit into pre-commit hooks and CI for a full dependency vulnerability workflow
- bandit-002: Added first bandit scan notes (`bandit/notes/2026-09-06-first-bandit-scan.md`) — Python version requirement wall, optional extras trap, profile vs test-ID confusion, and venv exclusion gotcha
- bandit-003: Added vulnerable-file scan demo script (`bandit/scripts/2026-09-06-scan-vulnerable-file.sh`) — creates a deliberately vulnerable Python file with os.system, subprocess.call, eval, and hardcoded secrets, then runs bandit to show test IDs and severity

## 2026-09-05
- con-045: Added pyproject.toml tool tables docs (`docs/concepts/python-packaging-project-config/pyproject-toml-tool-tables.md`) — pattern for consolidating uv, Ruff, pytest, and mypy configuration into pyproject.toml within a src-layout package
- con-047: Added AAA + parametrize + fixtures + coverage + static typing + CI integration docs (`docs/concepts/software-testing-principles/aaa-parametrize-fixtures-coverage-static-typing-ci.md`) — combining Arrange-Act-Assert, parametrized tests, fixtures, coverage thresholds, and type checking into a single CI pipeline
- pyright-004: Added first pyright type check notes (`pyright/notes/2026-09-05-first-pyright-type-check.md`) — install pyright, run initial type check, diagnostic interpretation, and differences from mypy
- pdt-023: Added dependency-health loop docs (`pdt/docs/integrating-pipdeptree-pip-audit-uv-dependency-health-loop.md`) — integrating pipdeptree, pip-audit, and uv for continuous drift, conflict, and vulnerability detection

## 2026-09-03
- ruf-019 (rework): Added one-command lint gate Python script (`ruff/scripts/ruff-lint-gate.py`) — ruff check with curated ruleset, format check, and per-file ignores for tests and init modules
- ruf-020 (rework): Added ruleset selection and per-file-ignores docs (`ruff/docs/selecting-rulesets-per-file-ignores.md`) — tiered ruleset strategy (E/W/F/I vs UP/B/C4), preview rules, and per-file-ignore patterns for S101/F401
- pdt-020: Added reusable dependency-health helper script (`pipdeptree/scripts/dependency-health-helper.py`) — JSON-tree output, warnings triage, and cycle detection for a project

## 2026-09-04
- pdt-021: Added pipdeptree + pip-audit dependency hygiene project scaffold template (`pipdeptree/templates/dependency-hygiene-scaffold/`) — src-layout package with pyproject.toml tool tables for pipdeptree/pip-audit/ruff/pytest/mypy/coverage, audit_deps.sh (uv export → pip-audit scan), and audit_deps.py (pipdeptree JSON-tree analysis with cycle detection and reverse-dependency hotspots)
- pdt-022: Added pipdeptree CI gates manifest (`pipdeptree/manifests/ci-pipdeptree-drift-conflict-cycle-gates.yaml`) — drift, conflict, and cycle gates on a Python 3.11/3.12/3.13 matrix
- bandit-007: Added bandit -s skip-tests bash snippet (`bandit/snippets/2026-09-04-skip-specific-bandit-tests.sh`) — skip specific test IDs (B101, B105) without losing the rest of the scan
Passed ([x]) ruf-019 — ruff: script — Build a one-command lint gate: ruff check with selected rules, format check, and per-file ignores as a Python wrapper · Level: L3 · 2026-09-04
Passed ([x]) ruf-020 — ruff: docs — Selecting a ruleset: E/W/F/I vs UP (pyupgrade) and preview rules, and when to use per-file-ignores · Level: L3 · 2026-09-04
- httpie-012: Added GitHub Actions CI/CD workflow docs (`httpie/docs/ci-cd-github-actions.md`) — --check-status exit-code gating, --timeout for CI reliability, --ignore-stdin for non-terminal hangs, secret handling via GitHub secrets/vars, and session file lifecycle in CI
- tox-011: Added multi-Python-version tox matrix runner (`tox/scripts/2026-09-04-multi-python-tox-matrix.sh`) — loop over pyenv Python versions, run tox -e for each, capture pass/fail in a CSV matrix

## 2026-09-02
- ruf-021: Added ruff format vs black comparison notebook (`ruff/notebooks/compare-ruff-format-vs-black.ipynb`) — same-file format comparison, where the outputs disagree, and single-formatter resolution with a ruff check + format check gate
- ty-013: Added ty quickstart loop snippet (`ty/snippets/2026-09-02-followed-ty-quickstart-loop.py`) — minimal typed module with generics plus the `ty check` file-scoped type-check loop and a reveal_type runtime fallback
- mypy-022: Added mypy incremental cache and follow-imports modes notebook (`mypy/notebooks/mypy-incremental-cache-follow-imports.ipynb`) — step-by-step investigation of `--cache-dir` and `--follow-imports` (normal/skip/silent), cache invalidation across Python versions, and CI-friendly invocation patterns
- mypy-022: Added mypy incremental cache and follow-imports notebook (`mypy/notebooks/explore-incremental-cache-and-follow-imports.ipynb`) — cold/warm cache invalidation, --follow-imports modes (normal/silent/skip/error), py.typed gating, python_version interactions, and what --no-incremental actually breaks
- prc-016: Added pre-commit internals docs (`prc/docs/how-pre-commit-works-under-the-hood.md`) — hook stages, pass_filenames behavior, environment variables, and debugging toolkit for failing hooks
- rich-007: Added Rich CLI status dashboard docs (`rich/docs/wiring-rich-into-a-cli-status-dashboard.md`) — assembling Console + Panel + Layout + Live for an updating dashboard, with a minimal end-to-end example and verify/common errors
- psy-019: Added py-spy profiling modes notebook (`py-spy/notebooks/compare-py-spy-top-vs-record-vs-dump.ipynb`) — side-by-side top vs record/flamegraph vs dump on the same CPU-bound target, with sample-target program, mode-by-mode reading notes, and a comparison table for choosing between them
- prc-017: Added src-layout pre-commit config with staged pinned hooks (`prc/configs/src-layout-pinned-hooks.yaml`) — ruff/mypy/pytest hooks with per-repo ids, commit-stage for fast checks and push-stage for type-check and tests
- mypy-021 (rework): Added mypy+ruff CI integration docs (`mypy/docs/integrating-mypy-ruff-ci.md`) — exit-code aggregation, cache isolation, and ANN* rule-overlap elimination

## 2026-08-31
- httpie-011: Added httpie vs curl CI gating notebook (`httpie/notebooks/compare-httpie-curl-ci-gating.ipynb`) — compare --check-status vs curl -f for CI smoke-test gating: exit-code semantics, selective status-code tolerance, timeout behavior, and failure-mode coverage
- pyproject.toml-024: Added src-layout pyproject.toml with tool tables (`pyproject.toml/configs/src-layout-pyproject.toml`) — build-system, project metadata, setuptools src-layout package discovery, and ruff/pytest/mypy/coverage configuration
## 2026-09-01
- prc-015: Added pre-commit bootstrap script (`prc/scripts/pre-commit-bootstrap.sh`) — fresh-repo scaffold: sample a config if missing, `pre-commit install`, then `pre-commit run --all-files` with non-zero exit on first-run failure

## 2026-08-30
- prc-014: Added pre-commit quickstart tripped-me-up notes (`prc/notes/2026-08-30-pre-commit-quickstart-gotchas.md`) — local hooks, --hook-stage, and pass_args gotchas after following the official quickstart

## 2026-08-29
- bandit-001: Added bandit primer (`bandit/notes/0000-primer-bandit.md`) — first-contact notes on Python security linter, test IDs, profiles, baseline workflow, and exclude paths
- typer-012: Added Typer subcommands snippet (`typer/snippets/2026-08-29-typer-subcommands.py`) — minimal CLI with subcommands, type-annotated params, and --help customization
- ty-017: Added ty minimal typed module snippet (`ty/snippets/2026-08-29-ty-minimal-module.py`) — generics, function signatures, and reveal_type usage
- httpie-010: Added httpie + pytest API scaffold template (`httpie/templates/httpie-pytest-api-scaffold/`) — FastAPI sample service, pytest integration tests via http CLI subprocess, conftest.py live-server fixture on a free port, GitHub Actions CI matrix, and pyproject.toml with httpie + pytest + fastapi deps
- mypy-019: Added type-safe Python package scaffold template (`mypy/templates/type-safe-python-package/`) — src-layout package with strict mypy, pytest, and coverage configuration in a single pyproject.toml

## 2026-08-28
- mypy-020: Added incremental mypy CI workflow (`mypy/manifests/ci-incremental-mypy-workflow.yaml`) — fail-fast type-check job with isolated MYPY_CACHE_DIR keyed by lockfile + interpreter, a warm cache step, and a cold-cache --no-incremental fallback
- con-050: Added dependency/secrets/safe-deserialization practice script (`docs/concepts/security-best-practices/scripts/2026-08-28-dependency-secrets-scan-deserialize.py`) — pip-audit dependency gate, secrets-pattern detection, env-based secret loading, and hardened XML parsing that rejects DTD/entity (XXE) payloads

## 2026-08-27
- mypy-018: Added gradual typing adoption notebook (`mypy/notebooks/gradual-typing-adoption.ipynb`) — step a small untyped project toward strict via reveal_type probes, --check-untyped-defs body checking, scoped # type: ignore[<code>] suppressions, and per-module [[tool.mypy.overrides]] ratchet
- con-044: Added dataclasses, context managers, and decorators practice script (`docs/concepts/python-programming-fundamentals/scripts/2026-08-27-dataclasses-context-managers-decorators.py`) — @dataclass with __post_init__, contextlib.contextmanager timer, retry decorator factory, and functools.wraps usage
- con-049: Added secure coding patterns snippet (`docs/concepts/security-best-practices/snippets/2026-08-27-secure-coding-patterns.py`) — parameterized SQL queries, input allowlisting, CSPRNG via secrets module, and env-var secrets handling
- httpie-009: Added httpie + jq shell pipeline docs (`httpie/docs/integrating-httpie-jq-shell-pipelines.md`) — feeding request bodies from pipes/files, parsing responses with jq, chaining API calls with command substitution, and --check-status/--ignore-stdin for CI
- httpie-013: Added first API request notes (`httpie/notes/2026-08-27-installed-httpie-first-api-request.md`) — install httpie, run my first request, and figure out why name=value and name:=value behave differently
- httpie-014: Added httpie core syntax snippet (`httpie/snippets/2026-08-27-httpie-core-syntax.sh`) — field types, JSON output, headers, and auth in a single session
- httpie-015: Added persistent httpie session config (`httpie/configs/2026-08-27-httpie-session-dev.json`) — default headers, basic auth, and session reuse for repeated API calls

## 2026-08-26
- con-042 (rework): Added CI-ready static type checking with pytest and pyproject.toml docs (`docs/concepts/static-type-checking-type-hints/ci-ready-static-checking-pytest-pyproject.md`) — unified pyproject.toml for mypy/pytest/Ruff, pre-commit hook with pass_filenames=false, GitHub Actions workflow with cache isolation, incremental mypy with --num-workers, and JUnit XML output
- httpie-007: Added CI-friendly HTTPie wrapper script (`httpie/scripts/ci-httpie-wrapper.sh`) — sourceable bash library with `--ignore-stdin`, `--check-status` exit-code mapping, and jq JSON parsing helpers
- httpie-008: Added multi-endpoint API smoke-test runner (`httpie/scripts/multi-endpoint-smoke-runner.sh`) — config-driven runner with `--check-status` exit-code mapping, `--ignore-stdin`, `--timeout`, and jq assertions
- tox-012: Added minimal tox multi-Python-version test matrix config (`tox/configs/2026-08-26-minimal-tox-matrix.toml`) — py39–py312 envlist, pytest + coverage, and a lint env via `[tool.tox]` legacy_tox_ini

## 2026-08-24
- con-041: Added parametrized edge-case test suite with coverage thresholds script (`docs/concepts/software-testing-principles/scripts/parametrized-edge-case-coverage-ci.py`) — boundary-value parametrize patterns for clamp/classify/distance functions with pytest-cov integration
- pyright-001: Added pyright primer (`pyright/notes/0000-primer-pyright.md`) — first-contact notes on Microsoft's static type checker, pyrightconfig.json, diagnostics, and Pylance
- con-043: Added Security Best Practices concept primer (`docs/concepts/security-best-practices/0000-primer-security-best-practices.md`) — first-contact notes on dependency scanning, secrets hygiene, input validation, and static analysis
- con-039 (rework): Added build-verify-smoke-install wheel script (`docs/concepts/python-packaging-project-config/scripts/build-verify-smoke-install-wheel.py`) — build a src-layout wheel, verify contents, smoke-install in fresh venv, test import and entry point; uses research-backed setuptools 77.0.3
- con-038 (rework): Rewrote choosing-build-backend docs (`docs/concepts/python-packaging-project-config/choosing-build-backend.md`) — removed unsupported version specifics and URLs, corrected file path, L3 reference voice

## 2026-08-23
- uvl-016: Added uv.lock evolution notebook (`uvl/notebooks/uv-lock-evolution-add-upgrade.ipynb`) — how uv.lock changes across `uv add` / `uv add --dev` / `uv lock`, and which habits (uncommitted lock, manual pyproject edits, re-resolving) break reproducibility
- uvl-014: Added uv.lock entries, hashes, and sources docs (`uvl/docs/reading-uv-lock-entries-hashes-sources.md`) — how entries are structured, how hashes verify artifacts, how sources track origins, and what triggers lockfile updates

## 2026-08-22
- uvl-015: Added lockfile reproducibility check script (`uvl/scripts/lockfile-reproducibility-check.sh`) — verify uv.lock consistency, record hash, fresh install from lock, and detect drift
- tox-010: Added tox environment matrix pyproject.toml config (`tox/configs/2026-08-22-tox-env-matrix.toml`) — lint/typecheck/test envs via [tool.tox] legacy_tox_ini shim in one TOML file
- uv-015: Added uv workflows docs (`uv/docs/2026-08-22-uv-workflows-run-uvx-tools-version-pinning.md`) — uv run, uvx, tool management, and Python version pinning workflows
- ppt-009: Added minimal PEP 621 pyproject.toml config (`pyproject.toml/configs/2026-08-22-minimal-pep621-pyproject.toml`) — build-system, project metadata, and [tool] tables in one file
- ppt-010: Added pyproject.toml trip-up notes (`pyproject.toml/notes/2026-08-22-what-tripped-me-up-pyproject-toml.md`) — build-system vs [project], requires-python enforcement, and optional-dependencies gotchas
- ppt-011: Added pyproject.toml validation script (`pyproject.toml/scripts/2026-08-22-validate-pyproject-tomllib.py`) — tomllib parse + required-section and build-backend/requires consistency check before build tools
- uv-017: Cleaned up spurious `src/quickstart_demo/` example paths in uv quickstart notes (`uv/notes/2026-06-01-tried-uv-quickstart-scaffold.md`) — rephrased as generated output, not repo files
- pyt-014: Added pytest fixtures and scoping docs (`pytest/docs/fixtures-conftest-scoping.md`) — scoping rules, conftest.py resolution, fixture ordering, and tmp_path/tmp_path_factory usage
- pyt-015: Added red-green-refactor notebook (`pytest/notebooks/red-green-refactor-loop.ipynb`) — TDD loop walkthrough with -k test selection, -x stop-on-fail, and assertion introspection
- pyt-013: Added fixture-and-parametrize test suite script (`pytest/scripts/fixture-and-parametrize-suite.py`) — function/class/module-scoped fixtures, @pytest.mark.parametrize, and custom markers

## 2026-08-21
- pau-014: Added CI-friendly pip-audit scan script (`pau/scripts/2026-08-21-ci-friendly-pip-audit-scan.sh`) — Scan a lockfile for known vulnerabilities with exit-code gating for CI
- con-036: Added src-layout package build-and-verify script (`docs/concepts/python-packaging-project-config/scripts/2026-08-21-build-validate-src-layout-package.py`) — create a minimal src/ package with a console_scripts entry point, build the wheel, and verify the packaged paths

## 2026-08-20
- typer-009: Added subcommand TODO CLI script (`typer/scripts/2026-08-20-todo-cli.py`) — add/list/done subcommands over a shared JSON store, the first multi-command Typer() app
- con-037: Added parametrized AAA edge-case test snippet (`docs/concepts/software-testing-principles/snippets/2026-08-20-parametrized-aaa-tests.py`) — Arrange/Act/Assert shape combined with a fixture and @pytest.mark.parametrize

## 2026-08-18
- pdt-017: Added dependency-health report script (`pipdeptree/scripts/dependency-health-report.sh`) — Build a dependency-health report from pipdeptree --warn, reverse deps, and JSON tree
- uv-014: Added a uv project bootstrap script with a lockfile reproducibility gate (`uv/scripts/bootstrap-project-lockcheck.sh`) — uv init --package, add runtime + dev deps, sync all groups, wipe and re-sync off uv.lock, and confirm the lock is stable
- uv-016: Added a uv-managed project pyproject.toml (`uv/configs/uv-dependency-groups-pyproject.toml`) — runtime deps under [project], dev-only deps under [dependency-groups], and a uv_build src-layout backend

## 2026-08-18
- ruf-018: Added pinned [tool.ruff] rule set config (`ruff/configs/2026-08-18-pinned-rule-set.toml`) — select/ignore baseline with per-file-ignores for tests and __init__ re-exports
- typer-007: Added typer quickstart script (`typer/scripts/2026-08-18-quickstart-args-options-help.py`) — positional arg, optional arg with default, bool flag, and free --help
- typer-008: Added typer quickstart trip-up notes (`typer/notes/2026-08-18-tripped-up-typer-quickstart.md`) — what confused me about positional args, --no- flags, and docstring help
- ty-012: Added minimal annotated module with ty findings and fixes (`ty/snippets/2026-08-18-minimal-annotated-module.py`) — parameter types, assignment types, and return-type mismatches
- con-033: Added venv-strategy comparison docs for the Virtual Environment & Dependency Mgmt concept (`docs/concepts/virtual-environment-dependency-mgmt/venv-strategies-venv-uv-tox.md`) — when to reach for venv vs uv vs tox, src-layout vs flat-layout reasoning, and how the layers combine with pyproject.toml and CI
- rich-005: Added first rich output snippet (`rich/snippets/2026-08-18-first-rich-output.py`) — markup colors, a table, and a live display

## 2026-08-17
- con-032: Added a lockfile drift-detection script for the Virtual Environment & Dependency Mgmt concept (`docs/concepts/virtual-environment-dependency-mgmt/scripts/lockfile-drift-check.py`) — lockfile vs active-env comparison, importlib.metadata, and CI-style --strict exit gating
- prc-012: Added a pinned pre-commit config with ruff + pre-commit-hooks (`prc/configs/2026-08-17-pre-commit-config.yaml`) — trailing-whitespace, end-of-file-fixer, check-ast, check-yaml, and ruff/ruff-format hooks with pinned revisions
- prc-013: Added CI parity check script for pre-commit (`prc/scripts/2026-08-17-ci-parity-check.sh`) — Automate pre-commit install, run all hooks repo-wide, and verify local run matches CI behavior
- psy-017: Added end-to-end py-spy profiling script (`py-spy/scripts/profile-running-process-end-to-end.sh`) — record, flamegraph, and dump against a running CPU-bound process
- psy-018: Added py-spy profiling modes docs (`py-spy/docs/when-to-use-py-spy-modes.md`) — when to use top vs record vs dump, and how to read each output

## 2026-08-16
- con-031: Added an interactive type-narrowing notebook that drives mypy on scratch modules (`docs/concepts/static-type-checking-type-hints/notebooks/type-narrowing-mypy-integration.ipynb`) — isinstance/Optional/reassignment narrowing, reveal_type, the untyped-def silent pass and `--check-untyped-defs`, Any-poisoning, and container invariance
- mypy-014: Added docs on typing third-party deps with a stub strategy instead of the `--ignore-missing-imports` Any-poisoning trap (`mypy/docs/stub-strategy-ignore-missing-imports.md`) — stub strategy, scoped overrides, and `reveal_type` debugging
- mypy-015: Added project mypy config for gradual typing (`mypy/configs/gradual-typing-mypy.toml`) — `check_untyped_defs`, `disallow_untyped_defs` scoped per-module, `ignore_missing_imports` off, and excludes
- mypy-013: Added a script moving a small scoreboard module from untyped to `mypy --strict` clean with `reveal_type` under `if TYPE_CHECKING:` (`mypy/scripts/untyped-to-strict-reveal-type.py`) — silent-pass gotcha, empty-collection annotations, and revealed-type debugging

## 2026-08-15

- httpie-006: Added notebook comparing --session vs inline auth for repeated API calls (`httpie/notebooks/compare-session-vs-inline-auth.ipynb`) — Purpose, repetition problem, session auth walkthrough, comparison table, and next verification steps
- httpie-005 (rework): Rewrote scripting docs and added session reuse coverage (`httpie/docs/scripting-request-items-offline-gating.md`) — request-item DSL, --offline preview, session reuse, and common errors

## 2026-08-14
- httpie-005: Added scripting docs on request items, --offline preview, and --check-status/--ignore-stdin gating (`httpie/docs/scripting-request-items-offline-gating.md`) — request-item DSL traps, offline request preview, and fail-loud scripting patterns
- con-034 (rework): Fixed the broken example test (missing `version` key now truly omitted so `.get` default fires) and corrected the Python version claim (PEP 585 generics are 3.9+, only PEP 604 unions need 3.10) in the fundamentals + static typing + testing integration docs (`docs/concepts/python-programming-fundamentals/combining-fundamentals-with-static-typing-and-testing.md`)
- con-035: Added Python Programming Fundamentals dependency-management CLI script (`docs/concepts/python-programming-fundamentals/scripts/dependency-management-cli.py`) — Pattern: fundamentals + dependency management using argparse, json, and importlib.metadata in a stdlib-only CLI

## 2026-08-13
- httpie-004: Added CI-safe API smoke-test script (`httpie/scripts/ci-safe-api-smoke-test.sh`) — dodges the httpie `--ignore-stdin` stdin hang in CI and gates on `--check-status` exit codes
- con-030 (rework): Rewrote type-checking patterns docs and added explicit connections to testing, packaging, and CI (`docs/concepts/static-type-checking-type-hints/typing-patterns-protocol-typeddict-generics.md`) — Protocol, TypedDict, and generics with adjacent-concept integration

## 2026-08-12
- con-030: Added type-checking patterns docs for real projects (`docs/concepts/static-type-checking-type-hints/typing-patterns-protocol-typeddict-generics.md`) — Protocol, TypedDict, and generics integration patterns
- con-025: Added Git Version Control version-from-tags script (`docs/concepts/git-version-control/scripts/derive-version-from-git-tags.py`) — Derive a package version from the nearest reachable git tag (setuptools-scm pattern) using only stdlib
- con-028: Added Python Packaging & Project Config build-and-verify wheel script (`docs/concepts/python-packaging-project-config/scripts/2026-08-12-build-verify-wheel.py`) — Build a minimal package into a wheel and inspect its contents
- con-029: Added Software Testing Principles boundary values and test doubles snippet (`docs/concepts/software-testing-principles/snippets/2026-08-12-boundary-values-test-doubles.py`) — Practice boundary-value tests and a fake test double with pytest

## 2026-08-11
- con-026: Added Git workflows docs for branches, tags, and CI gates (`docs/concepts/git-version-control/git-workflows-branches-tags-ci.md`) — Branch-and-PR flow, semantic tags, and uv-backed CI gates for the Python learning kit
- con-027: Added comprehensions, generators, and error handling snippet (`docs/concepts/python-programming-fundamentals/snippets/2026-08-11-comprehensions-generators-error-handling.py`) — Practicing list/set comprehensions, generator functions and expressions, and try/except/finally

## 2026-08-10
- uv-009 (rework): Fixed front-matter and expanded uv script/venv/lockfile workflow notes (`uv/notes/2026-08-09-tried-uv-script-venv-lockfile.md`) — What I learned building a small CLI tool with uv
- prc-011 (rework): Fixed front-matter and removed unverified version/URL references in pre-commit hook notes (`prc/notes/2026-08-09-first-pre-commit-hook.md`) — What I learned setting up my first pre-commit hook and running it once

## 2026-08-09
- pau-009: Added pip-audit scan config (`pau/configs/2026-08-09-pip-audit-scan-config.toml`) — Minimal [tool.pip-audit] section with scan defaults and ignore rules
- uv-009: Added uv script/venv/lockfile workflow notes (`uv/notes/2026-08-09-tried-uv-script-venv-lockfile.md`) — What I learned building a small CLI tool with uv
- prc-011: Added first pre-commit hook notes (`prc/notes/2026-08-09-first-pre-commit-hook.md`) — What I learned setting up my first pre-commit hook and running it once
- pau-009: Added minimal pip-audit pyproject.toml config (`pau/configs/2026-08-09-minimal-pip-audit-pyproject.toml`) — Minimal [tool.pip-audit] section with scan defaults and ignore rules

## 2026-08-07
- rich-004: Added Rich first styled console output script (`rich/scripts/2026-08-07-first-styled-rich-output.py`) — Install Rich and produce my first styled console output

## 2026-08-06
- pdt-010: Added pipdeptree tutorial notes (`pipdeptree/notes/2026-08-06-pipdeptree-tutorial.md`) — Followed the official pipdeptree tutorial: reverse trees, cycle detection, and what tripped me up
- rich-003: Added Rich inspect + live display snippet (`rich/snippets/2026-08-06-rich-inspect-live-pipeline.py`) — What I learned using Rich's inspect() and live display on a sample data pipeline

## 2026-08-05
- rich-001: Added Rich quickstart tripped-me-up notes (`rich/notes/2026-08-05-followed-rich-quickstart.md`) — What I learned following the official Rich quickstart: markup syntax, table alignment, Live refresh rate, and console width gotchas
- rich-002: Added Rich styled output script (`rich/scripts/2026-08-05-rich-styled-output-tables-progress.py`) — Minimal Rich script demonstrating panels, tables, and progress bars
- ty-009: Added minimal Ty config (`ty/configs/2026-08-05-minimal-ty-config.toml`) — Minimal Ty configuration with pyproject.toml for type-checking settings
- tox-008: Added tox install and first-env script (`tox/scripts/2026-08-05-install-tox-and-first-env.sh`) — Install tox, write a minimal tox.ini, and run a first test environment
- uv-013: Added uv quickstart tripped-me-up notes (`uv/notes/2026-08-05-uv-quickstart-tripped-up.md`) — What I learned following the official uv quickstart: scaffold, deps, run, and what tripped me up

## 2026-08-04
- pdt-016: Added pipdeptree dependency report snippet (`pipdeptree/snippets/2026-08-04-build-dependency-report.py`) — Build a tiny dependency report from pipdeptree JSON for a selected package
- uvl-010: Added uv.lock mapping notes (`uvl/notes/2026-08-04-uv-lock-mapping-to-pyproject.md`) — What I learned examining uv.lock: how the lockfile maps to pyproject.toml dependencies
- mypy-012: Added selective mypy strictness config (`mypy/configs/2026-08-04-selective-mypy-strictness.ini`) — Minimal mypy.ini with selective strictness flags (warn_return_any, disallow_untyped_defs, warn_unused_ignores)
- pyt-010: Added pytest quickstart tripped-me-up notes (`pytest/notes/2026-08-04-tried-pytest-quickstart.md`) — [FILE MISSING] content superseded by `pytest/notes/2026-06-04-tried-pytest-fixtures-conftest.md`
- pyt-011: Added minimal pytest fixture and parametrize suite (`pytest/scripts/2026-08-04-minimal-fixture-parametrize-suite.py`) — [FILE MISSING] content superseded by `pytest/scripts/fixture-and-parametrize-suite.py`
- ty-010: Added Ty quickstart tripped-me-up notes (`ty/notes/2026-08-04-followed-ty-quickstart.md`) — What I learned following the official Ty quickstart: install, run, type mismatches, and config gotchas
- ty-011: Added minimal Ty type-checking workflow snippet (`ty/snippets/2026-08-04-ty-type-checking-workflow.py`) — Minimal typed Python module demonstrating Ty check workflow

## 2026-08-03
- ruf-004: Added Ruff quick primer (`ruff/notes/0000-primer-ruff.md`) — First-day notes explaining what Ruff is, key terminology, and a tiny example

## 2026-08-01
- uvl-004: Added uv.lock quick primer (`uvl/notes/0000-primer-uv.lock.md`) — First-day notes explaining what uv.lock is, key terminology, and a tiny example

## 2026-07-31
- ruf-004: Added Ruff quick primer (`ruff/notes/0000-primer-ruff.md`) — First-day notes explaining what Ruff is, key terminology, and a tiny config example

## 2026-07-27
- con-019: Added Static Type Checking & Type Hints applying-type-hints script (`docs/concepts/static-type-checking-type-hints/scripts/2026-07-27-applying-type-hints.py`) — Python script demonstrating typed dictionaries, runtime validation, and filtering with type annotations
- con-021: Added Virtual Environment & Dependency Mgmt common-venv-patterns snippet (`docs/concepts/virtual-environment-dependency-mgmt/snippets/2026-07-27-common-venv-patterns.py`) — Python snippet showing venv creation, requirements pinning, install, and freeze workflows

## 2026-07-26
- pau-004: Added pip-audit quick primer (`pau/notes/0000-primer-pip-audit.md`) — First-day notes explaining what pip-audit is, key terminology, and a tiny scan example

## 2026-07-23
- ruf-016: Rework: Removed `set -euo pipefail` from end-to-end Ruff lint-and-format workflow script (`ruff/scripts/end-to-end-ruff-lint-format.sh`) — Replaced with `set -e`
- con-016: Added Git Version Control practice script (`docs/concepts/git-version-control/scripts/2026-07-23-practice-git-version-control.py`) — Python script exercising init, add, commit, and branch workflows in a temp directory
- con-017: Added Git Version Control common patterns snippet (`docs/concepts/git-version-control/snippets/2026-07-23-common-git-patterns-in-python-projects.py`) — Python snippets for status checks, feature branch creation, and remote branch listing via subprocess
- con-018: Added Static Type Checking & Type Hints common patterns snippet (`docs/concepts/static-type-checking-type-hints/snippets/2026-07-23-common-type-checking-patterns.py`) — Python snippets demonstrating basic functions, Optional, and Union type hints
- con-020: Added Virtual Environment & Dependency Mgmt practice script (`docs/concepts/virtual-environment-dependency-mgmt/scripts/2026-07-23-venv-practice.py`) — Python script exercising venv creation, package install, requirements export, and offline dep caching

## 2026-07-21
- ruf-012: Added minimal standalone ruff.toml (`ruff/configs/2026-07-21-minimal-standalone-ruff.toml`) — One selected rule (E), one ignored rule (E501)
- ruf-015: Added Ruff select/ignore/extend-safe/per-directory overrides notes (`ruff/notes/2026-07-21-ruff-select-ignore-extend-safe-overrides.md`) — Replaced "production code" with "application code"

## 2026-07-20
- psy-014: Rework: Reduced py-spy top+record profile script to ≤15 lines, added sleep for py-spy attach timing (`py-spy/scripts/2026-07-20-profile-tiny-loop-py-spy.sh`) — Profile a tiny Python loop with py-spy top (live view) and py-spy record (flamegraph SVG)

## 2026-07-19
- httpie-001: Added followed httpie quickstart notes (`httpie/notes/2026-07-19-followed-httpie-quickstart.md`) — Followed official quickstart: GET, POST, raw JSON, headers, what tripped me up
- httpie-002: Added httpie request workflow script (`httpie/scripts/2026-07-19-httpie-request-workflow.sh`) — GET, POST, JSON body, custom headers, --check-status
- mypy-011: Added minimal typed module snippet (`mypy/snippets/2026-07-19-typed-small-module.py`) — Minimal typed Python file to validate with mypy on a small module
- psy-011: Added py-spy install + live-process profiling notes (`py-spy/notes/2026-07-19-installed-py-spy-profiled-running-process.md`) — What I learned installing py-spy and profiling my first running Python process with `py-spy top`
- uv-006: Added minimal pyproject.toml for uv-managed project (`uv/configs/2026-07-19-uv-managed-project.toml`) — Minimal pyproject.toml with project metadata, dependencies, scripts, and hatchling build-backend
- uv-007: Added minimal uv workflow script (`uv/scripts/2026-07-19-uv-workflow.sh`) — Walk through uv init, add, run, and inspect generated lockfile

## 2026-07-17
- pau-007: Added pip-audit quickstart tripped-me-up notes (`pip-audit/notes/2026-07-17-followed-pip-audit-quickstart.md`) — Followed official quickstart: --local, --require-hashes, --fix gotchas, exit codes, --ignore-vuln
- prc-010: Added pre-commit ruff+trailing-whitespace run script (`pre-commit/scripts/run-pre-commit-ruff-trailing-ws.sh`) — Set up sample project, configure pre-commit, run hooks once
- pdt-011: Added pipdeptree library dependency-listing script (`pipdeptree/scripts/list-package-deps.py`) — Minimal Python script using pipdeptree as a library to list all dependencies of a package

## 2026-07-13
- pau-005: Added pip-audit JSON CVE parser snippet (`pip-audit/snippets/2026-07-13-parse-pip-audit-json-cves.py`) — Parse pip-audit JSON output and list packages with CVEs and severity

## 2026-07-10
- pau-005: Added pip-audit JSON CVE parser snippet (`pip-audit/snippets/2026-07-10-parse-pip-audit-json-cves.py`) — Parse pip-audit JSON output and list packages with CVEs and severity

## 2026-07-08
- psy-009: Added py-spy record output formats comparison notes (`py-spy/notes/2026-07-08-compared-py-spy-record-output-formats.md`) — Compared flamegraph SVG, speedscope JSON, and raw JSON output formats
- psy-010: Added py-spy self-profile speedscope script (`py-spy/scripts/2026-07-08-cpu-speedscope-record.py`) — CPU-bound workload with py-spy record and speedscope JSON export

## 2026-07-05
- con-007: Added Python Programming Fundamentals practice script (`docs/concepts/python-programming-fundamentals/scripts/2026-07-05-practicing-fundamentals.py`) — Practicing data types, control flow, functions, comprehensions, args/kwargs
- con-008: Added Python Packaging patterns snippet (`docs/concepts/python-packaging-project-config/snippets/2026-07-05-packaging-patterns.py`) — Reading pyproject.toml metadata and discovering packages
- con-009: Added Software Testing Principles practice script (`docs/concepts/software-testing-principles/scripts/2026-07-05-testing-principles.py`) — Writing isolated, parametrized tests with fixtures

## 2026-06-29
- pau-005: Added pip-audit CVE listing snippet (`pip-audit/snippets/tried-list-cves.py`) — Parse pip-audit JSON output to list packages with CVEs and their severity
- psy-010: Added py-spy speedscope record script (`py-spy/scripts/tried-cpu-speedscope-record.py`) — CPU-bound workload with py-spy record and speedscope JSON export

## 2026-06-26
- mypy-007: Added official mypy quickstart notes (`mypy/notes/2026-06-08-tried-mypy-official-quickstart.md`) — Followed official docs: gradual typing, strict mode, reveal_type, what tripped me up
- mypy-008: Added strict/disallow/ignore mypy.ini config (`mypy/configs/tried-strict-disallow-ignore-config.ini`) — Minimal mypy.ini with strict, disallow_untyped_defs, ignore_missing_imports

## 2026-06-23
- con-001: Added Git Version Control primer (`docs/concepts/git-version-control/0000-primer-git-version-control.md`) — What is Git? first contact notes
- con-002: Added Python Programming Fundamentals primer (`docs/concepts/python-programming-fundamentals/0000-primer-python-programming-fundamentals.md`) — What are Python programming fundamentals? first contact notes
- con-003: Added Python Packaging & Project Config primer (`docs/concepts/python-packaging-project-config/0000-primer-python-packaging-project-config.md`) — What is Python packaging and project config? first contact notes
- con-004: Added Software Testing Principles primer (`docs/concepts/software-testing-principles/0000-primer-software-testing-principles.md`) — What are software testing principles? first contact notes
- con-005: Added Static Type Checking & Type Hints primer (`docs/concepts/static-type-checking-type-hints/0000-primer-static-type-checking-type-hints.md`) — What are type hints and static type checkers? first contact notes
- con-006: Added Virtual Environment & Dependency Mgmt primer (`docs/concepts/virtual-environment-dependency-mgmt/0000-primer-virtual-environment-dependency-mgmt.md`) — What are virtual environments and dependency management? first contact notes

## 2026-06-18
- prc-006: Added pre-commit CLI walkthrough notes (`pre-commit/notes/2026-06-18-pre-commit-cli-walkthrough.md`) — Installed pre-commit, walked through install/run/sample-config/validate-config/autoupdate
- ty-006: Added first Ty type check notes (`ty/notes/2026-06-18-first-ty-type-check.md`) — Installed Ty and ran first type check on a sample Python file
- uvl-007: Added uv.lock packages/checksums/markers notes (`uv.lock/notes/2026-06-18-uv-lock-packages-checksums-markers.md`) — Explored uv.lock package versions, checksums, and dependency markers

## 2026-06-17
- pyt-008: Added pytest primer (`pytest/notes/0000-primer-pytest.md`) — What is pytest? first contact notes
- ric-009: Added rich Console API renderables notes (`rich/notes/2026-06-17-explored-rich-console-api-renderables.md`) — Explored renderables, styles, and output modes
- ric-010: Added rich Console panel and table snippet (`rich/snippets/tried-rich-console-panel-table.py`) — Minimal Console script with text styling, panel, and table
- ruf-007: Added Ruff CLI more flags notes (`ruff/notes/2026-06-17-tried-ruff-cli-more-flags.md`) — Tried --show-settings, --show-files, --add-noqa, --statistics, ruff rule
- pdt-008: Added pipdeptree patterns I use notes (`pipdeptree/notes/2026-06-17-pipdeptree-patterns-i-use.md`) — More CLI patterns: --graph-output, --local-only, --python-version, --all
- psy-008: Added install and record flamegraph script (`py-spy/scripts/tried-install-and-record-flamegraph.sh`) — Install py-spy and profile CPU-bound script to flamegraph SVG

## 2026-06-16
- ty-008: Added Ty CLI flags and output formats notes (`ty/notes/2026-06-16-explored-ty-cli-flags.md`) — Explored Ty CLI flags, output formats, compared with mypy options
- prc-008: Added pre-commit install and run with lint+typecheck notes (`pre-commit/notes/2026-06-16-installed-pre-commit-ran-lint-typecheck.md`) — Installed pre-commit, ran with ruff linting and mypy type check on a sample repo
- uv-007: Added uv CLI help and format notes (`uv/notes/2026-06-16-explored-uv-cli-help-and-format.md`) — Explored uv CLI subcommands, help topics, and output formats
- gen-005: Added quality tools pyproject.toml config — Combined ruff, mypy, pytest config in one pyproject.toml
- ty-007: Added Ty vs mypy comparison snippet (`ty/snippets/tried-ty-vs-mypy.py`) — Compare Ty and mypy output on the same typed code
- prc-007: Added ruff + mypy hooks config snippet (`pre-commit/snippets/tried-ruff-mypy-config.yaml`) — Minimal pre-commit config with ruff and mypy hooks
- tox-005: Upgraded tox config voice (`tox/configs/tried-lint-and-test-env.ini`) — Enhanced comments with structured reasoning
- ruf-006: Trimmed messy example (`ruff/snippets/tried-messy-example.py`)
- pdt-007: Trimmed check-package-deps (`pipdeptree/snippets/tried-check-package-deps.py`)

## 2026-06-15
- uvl-012: Added uv.lock structure exploration notebook (`uv.lock/notebooks/tried-exploring-uv-lock-structure.ipynb`) — Walk through uv.lock sections, hashes, and reproducibility
- uvl-011: Added uv.lock direct deps extraction script (`uv.lock/scripts/tried-extract-direct-deps.py`) — Parse uv.lock and list all direct dependency entries
- tox-005: Added lint and test env tox config (`tox/configs/tried-lint-and-test-env.ini`) — Minimal tox.ini with lint (ruff) and test (pytest) environments, annotated with reasoning
- ruf-006: Added messy example snippet (`ruff/snippets/tried-messy-example.py`) — Deliberately messy Python file with various style violations
- pdt-007: Added check package deps snippet (`pipdeptree/snippets/tried-check-package-deps.py`) — Look up a specific package in pipdeptree JSON output and print its dependency chain
- tox-009: Added minimal tox run script (`tox/scripts/tried-minimal-tox-run.sh`) — Create tox.ini with test env and run tox end-to-end
- ppt-005: Added build-system config notes (`pyproject.toml/notes/2026-06-05-explored-pyproject-build-system.md`) — Exploring minimal [build-system] table in pyproject.toml
- gen-002: Added backlog capacity audit notes — Count open vs completed tasks per tool, identify next-level blockers

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
- gen-003: Added cross-tool workflow notes — How Ruff, mypy, pytest, pre-commit, and uv fit together in one pipeline
- gen-004: Added first quality chain snippet — Run Ruff, mypy, and pytest in sequence from one script

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
- py-006: Added Ruff config (`ruff/configs/ruff-pyproject.toml`)
- py-007: Added pytest primer (`pytest/notes/0000-primer-pytest.md`)
- py-004: Added Ruff primer (`py/notes/0000-primer-py.md`)

## 2026-05-24

- py-001: Added uv primer (`uv/notes/0000-primer-uv.md`)
- py-002: Added uv install script (`uv/scripts/install-and-first-command.sh`)
- py-003: Added uv virtual env notes (`uv/notes/2026-05-24-virtual-env-uv.md`)
