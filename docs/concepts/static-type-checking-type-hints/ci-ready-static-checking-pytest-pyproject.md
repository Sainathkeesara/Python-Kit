---
last_verified: 2026-08-26
tool_version: n/a
sources:
  - https://mypy.readthedocs.io/en/stable/config_file.html
  - https://pypi.org/project/mypy/
  - https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026
  - https://technoscripts.com/python-ci-cd-github-actions/
  - https://akakritagya.hashnode.dev/how-i-set-up-a-python-project-in-2026-uv-ruff-mypy-and-friends
  - https://python-type-hints.com/static-analysis-tools-ci-integration/ruff-linter-integration/integrating-ruff-check-with-mypy-in-ci/
  - https://mypy-lang.blogspot.com/2026/07/mypy-23-released.html
  - https://pydevtools.com/blog/mypy-2-0-parallel-type-checking
  - https://www.propelcode.ai/blog/python-type-hints-code-review-guide-mypy-best-practices
---

# CI-ready static type checking with pytest and pyproject.toml

## Purpose

This pattern shows how to wire mypy, pytest, and pyproject.toml together so a single configuration drives local pre-commit checks, editor integration, and CI type-checking gates. The goal is a consistent type layer across every checkout without maintaining separate configs for each surface.

## When to use

- A Python package that wants type checking in CI without drift between local and remote runs
- Teams adopting gradual typing who need `--strict` as the baseline but want incremental adoption
- Projects using uv for dependency management that want the same config file to drive mypy, Ruff, and pytest

## Prerequisites

- Python project with `src/` layout (or flat layout with `pyproject.toml` at root)
- mypy installed as a dev dependency
- pytest for test execution
- GitHub Actions (or equivalent CI) for the workflow examples

## Pattern: unified pyproject.toml

The key insight is putting all tool configuration in one `pyproject.toml` so the type-checking contract travels with the code. A minimal config for this pattern:

```toml
[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "Example package with unified type checking"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "mypy",
    "pytest",
    "pytest-mypy-plugins",
]

[tool.mypy]
python_version = "3.10"
strict = true
namespace_packages = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
follow_imports = "normal"
mypy_path = ["src"]

[tool.mypy.plugins]
pydantic.mypy = "pydantic.mypy"

[tool.pytest.ini_options]
addopts = "-ra --strict-markers --strict-config"
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"

[tool.ruff]
select = ["E", "W", "F", "I", "UP", "B"]
ignore = ["ANN101", "ANN102", "ANN201", "ANN202", "ANN204", "ANN401"]
target-version = "py310"
src = ["src"]
```

The Ruff `ignore` list disables `ANN*` rules that overlap with mypy `--strict`, eliminating duplicate diagnostics [source: https://python-type-hints.com/static-analysis-tools-ci-integration/ruff-linter-integration/integrating-ruff-check-with-mypy-in-ci/]. The mypy `mypy_path` uses config-relative paths so imports resolve from `src/` regardless of working directory [source: https://mypy.readthedocs.io/en/stable/config_file.html].

## Pattern: pre-commit hook for fast local feedback

A local pre-commit hook runs mypy on staged files before every commit, catching type errors before they reach CI. The hook should disable `pass_filenames` so mypy receives the whole package context [source: https://akakritagya.hashnode.dev/how-i-set-up-a-python-project-in-2026-uv-ruff-mypy-and-friends]:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: mypy
        name: mypy
        entry: uv run mypy src/
        language: system
        pass_filenames: false
        types: [python]
```

The `uv run mypy src/` invocation ensures mypy runs in the project's managed environment with the same dependencies as CI [source: https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026].

## Pattern: GitHub Actions workflow with cache isolation

The CI workflow separates mypy and Ruff caches to avoid the "phantom pass" where a stale type graph reports clean on broken code [source: https://python-type-hints.com/static-analysis-tools-ci-integration/ruff-linter-integration/integrating-ruff-check-with-mypy-in-ci/]. Use uv's caching for dependency installation and separate cache keys for each tool:

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  type-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: uv
      - name: Install dependencies
        run: uv sync --dev
      - name: Run mypy
        run: uv run mypy --strict src/
      - name: Run Ruff
        run: uv run ruff check src/
      - name: Run tests with type-aware plugins
        run: uv run pytest --cov=src
```

The `pytest-mypy-plugins` package enables mypy to understand pytest fixtures and parametrization, reducing false positives in test modules [source: https://www.propelcode.ai/blog/python-type-hints-code-review-guide-mypy-best-practices].

## Pattern: incremental type checking for faster PR feedback

For large codebases, mypy's incremental mode caches type information between runs. In CI, enable it with a dedicated cache directory and `--num-workers` for parallel checking [source: https://pydevtools.com/blog/mypy-2-0-parallel-type-checking]:

```bash
# In CI, after installing dependencies
uv run mypy --strict --incremental --cache-dir .mypy_cache --num-workers 4 src/
```

The `--num-workers` flag can provide up to 5x speedup with 8 workers on large projects, though startup overhead dominates on small codebases. For PR checks, combine with `--follow-imports=skip` to limit scope to changed files, falling back to a full scan when configuration or dependency files change [source: https://python-type-hints.com/static-analysis-tools-ci-integration/ruff-linter-integration/integrating-ruff-check-with-mypy-in-ci/].

## Pattern: JUnit XML output for CI visibility

Mypy can emit JUnit XML so CI platforms surface type errors as test failures with file/line links. Enable it for CI runs only, since reports disable incremental mode and slow down the workflow [source: https://mypy.readthedocs.io/en/stable/config_file.html]:

```bash
uv run mypy --strict --junit-xml mypy-results.xml src/
```

The `junit_format` option controls granularity: `global` (default) produces one test entry with all errors; `per_file` produces one entry per file with failures, which is more actionable in CI dashboards.

## Verification checklist

After wiring these pieces together, verify the integration:

1. **Local pre-commit**: `git commit` triggers mypy on `src/` — untyped functions and signature mismatches fail before commit.
2. **CI type-check job**: The GitHub Actions workflow passes on clean code, fails with actionable links on type errors.
3. **Test suite runs after type gate**: Pytest only executes if mypy and Ruff pass, ensuring runtime tests run on type-clean code.
4. **Cache isolation works**: Re-running CI with no code changes hits uv and mypy caches, completing in seconds.
5. **Incremental mode detects changes**: Edit a typed function signature, push — mypy re-checks only affected modules and flags callers.

## Common errors

- **Forgetting `pass_filenames: false` in pre-commit**: Mypy receives only staged files, misses cross-file type dependencies, and reports false passes.
- **Sharing cache directories between Ruff and mypy**: The AST-hash cache (`.ruff_cache`) and type-graph cache (`.mypy_cache`) corrupt each other, producing phantom passes.
- **Running mypy without `src/` in `mypy_path`**: Imports resolve from the working directory instead of the package root, causing false `import not found` errors.
- **Leaving `ANN*` rules enabled in Ruff with mypy `--strict`**: Duplicate diagnostics on missing annotations clutter CI output without adding signal.
- **Enabling mypy reports (`--junit-xml`, `--html-report`) on every run**: Reports disable incremental mode, making every run a full cold start.

## How this connects to what's next

This pattern establishes the type-checking foundation that other tools build on: Typer uses function annotations for CLI generation, Pyright provides IDE integration, and Pydantic validates runtime data against the same types. The unified `pyproject.toml` becomes the single source of truth for the project's type contract across all surfaces.