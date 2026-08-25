---
last_verified: 2026-08-25
tool_version: n/a
sources:
  - https://pydevtools.com/blog/mypy-2-0-parallel-type-checking
  - https://www.propelcode.ai/blog/python-type-hints-code-review-guide-mypy-best-practices
  - https://www.guvi.in/blog/python-packaging-with-pyproject-toml/
  - https://packaging.python.org/en/latest/guides/writing-pyproject-toml
---

# Pattern: static type checking + pytest + pyproject.toml in a CI-ready Python project

## Purpose

This pattern shows how to wire mypy (or another type checker) into a Python project alongside pytest, using `pyproject.toml` as the single configuration hub. The goal is a CI pipeline that runs type checks and tests in sequence, catches type errors before they reach production, and keeps configuration maintainable as the project grows.

The pattern works for projects that already use `pyproject.toml` for build metadata and tool settings. It assumes a src-layout or flat-layout Python package with pytest as the test runner.

## Steps

### 1. Declare mypy and pytest in `pyproject.toml`

Add both tools to the `[project.optional-dependencies]` section so they install together in CI:

```toml
[project.optional-dependencies]
dev = [
    "mypy>=2.0",
    "pytest>=8.0",
    "pytest-mypy-plugins>=2.0",
]
```

The `pytest-mypy-plugins` package lets pytest discover and run mypy as part of the test suite, so a single `pytest` invocation covers both unit tests and type checks.

### 2. Configure mypy in `pyproject.toml`

```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

The `strict = true` flag enables the broadest set of checks. The overrides section relaxes rules for test files where type annotations are often omitted.

### 3. Configure pytest to run mypy

```toml
[tool.pytest.ini_options]
addopts = "--mypy"
testpaths = ["tests", "src"]
```

The `--mypy` flag tells pytest to run mypy on collected test modules. This means `pytest` alone runs both tests and type checks.

### 4. Set up a CI workflow

A minimal GitHub Actions workflow that runs type checks and tests:

```yaml
name: CI
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -e ".[dev]"
      - run: pytest --mypy
```

The workflow installs the package with dev dependencies, then runs `pytest --mypy` to execute both tests and type checks in one pass.

### 5. Separate type checking from tests (optional)

If type checks should run independently (e.g., faster feedback on type errors alone), add a separate step:

```yaml
      - run: mypy src/
      - run: pytest tests/
```

This lets CI report type errors and test failures separately, which can speed up debugging when one fails but the other passes.

## Verify

After setting up the pattern:

1. Run `pytest --mypy` locally — it should collect both test files and mypy checks.
2. Intentionally introduce a type error (e.g., pass a string to an int parameter) and verify mypy catches it.
3. Run `pytest` without `--mypy` to confirm tests still pass in isolation.
4. Check that `pyproject.toml` is the only configuration file — no separate `mypy.ini` or `setup.cfg` should exist.

## Common pitfalls

- **Forgetting `pytest-mypy-plugins`**: Without it, `--mypy` is not recognized and pytest fails with an unknown option error.
- **Conflicting mypy versions**: If `mypy` is pinned in `pyproject.toml` but a different version is installed globally, type check results may vary. Use virtual environments to isolate.
- **Test files without type annotations**: With `disallow_untyped_defs = true`, mypy will flag test functions missing type hints. The override for `tests.*` relaxes this, but it's worth adding annotations gradually.

## References

- mypy strict mode documentation: https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict
- pytest-mypy-plugins: https://github.com/TypedDev/pytest-mypy-plugins
- pyproject.toml tool configuration: https://packaging.python.org/en/latest/guides/writing-pyproject-toml
