---
last_verified: 2026-09-05
tool_version: n/a
sources: []
---

# Combining AAA, parametrize, fixtures, coverage, and static typing in CI

## Purpose

This document shows how five testing practices — the Arrange-Act-Assert (AAA) pattern, `pytest.mark.parametrize`, fixtures, coverage measurement, and static type checking — compose into a single coherent CI pipeline. Each technique solves a different problem; together they form a feedback loop that catches logic errors, type mismatches, and untested code paths before merge.

## When to use

Use this combined approach when:

- The project has more than a handful of tests and needs consistent structure across contributors.
- CI must enforce a minimum coverage threshold alongside type safety.
- Test data sets are growing and hand-writing individual test functions for each case is no longer practical.
- Shared resources (database connections, API clients, temporary directories) appear in multiple test modules.

## Prerequisites

- `pytest` installed and runnable (`pytest --version`).
- `coverage` (or `pytest-cov`) for measuring line coverage.
- A type checker — `mypy` or `pyright` — configured for the project.
- A CI system (GitHub Actions, GitLab CI, tox, or equivalent) that can run multiple check steps sequentially.

## Steps

### 1. Structure every test with AAA

The Arrange-Act-Assert pattern gives each test three clearly separated sections:

```python
def test_calculate_total_with_discount():
    # Arrange
    items = [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]
    discount = 0.10

    # Act
    total = calculate_total(items, discount=discount)

    # Assert
    assert total == 225.0  # (200 + 50) * 0.90
```

AAA keeps tests readable and makes failures easy to diagnose — the assertion line tells you exactly what went wrong. When a test grows beyond three distinct actions, it is usually testing two things and should be split.

### 2. Replace repetitive test functions with `@pytest.mark.parametrize`

Parametrize runs the same test body with different inputs, eliminating copy-paste:

```python
@pytest.mark.parametrize(
    "items, discount, expected",
    [
        ([{"price": 100, "qty": 2}], 0.0, 200.0),
        ([{"price": 100, "qty": 2}], 0.10, 180.0),
        ([], 0.0, 0.0),
    ],
    ids=["no-discount", "ten-percent", "empty-cart"],
)
def test_calculate_total(items, discount, expected):
    assert calculate_total(items, discount=discount) == expected
```

The `ids` parameter give each case a human-readable name in the test output. Parametrize is most effective when the test body is identical across cases and only the data changes — if the logic branches, separate tests are clearer.

### 3. Extract shared setup into fixtures

Fixtures handle setup and teardown that multiple tests need. They are declared as functions decorated with `@pytest.fixture` and requested by name in test signatures:

```python
@pytest.fixture
def sample_cart():
    return [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]


def test_total_before_discount(sample_cart):
    assert calculate_total(sample_cart, discount=0.0) == 250.0


def test_total_after_discount(sample_cart):
    assert calculate_total(sample_cart, discount=0.10) == 225.0
```

Fixtures can be scoped (`function`, `class`, `module`, `session`) to control how often setup runs. A `session`-scoped database fixture, for example, connects once per test run rather than once per test function — a significant speedup for integration suites.

### 4. Measure coverage and enforce a threshold

`pytest-cov` wraps `coverage.py` and reports which lines were executed:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

The `--cov-fail-under=80` flag makes the pipeline fail if coverage drops below 80%. Coverage is a blunt instrument — it tells you what was *run*, not what was *verified* — but it catches dead code and untested branches cheaply. Combine it with mutation testing (e.g., `mutmut`) for stronger guarantees when the project warrants it.

### 5. Add static type checking to the pipeline

Type checkers like `mypy` or `pyright` catch type mismatches at analysis time, before tests even run:

```bash
mypy src/ --strict
pyright
```

When type checking runs alongside tests in CI, the two complement each other: type checkers catch structural errors (wrong argument types, missing returns), while tests catch behavioral errors (correct types, wrong logic). Configuring `disallow_untyped_defs = true` in `mypy` forces every function to have type annotations, which makes the type checker maximally useful.

### 6. Wire everything into CI

A minimal CI pipeline runs these checks in sequence:

```yaml
# .github/workflows/ci.yml (abbreviated)
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
  - run: pip install -e ".[dev]"
  - run: mypy src/ --strict
  - run: pytest --cov=src --cov-report=term-missing --cov-fail-under=80
  - run: ruff check src/ tests/
```

The order matters: type checking first (fast, catches structural issues), then tests with coverage (slower, catches behavioral issues), then linting (catches style). Failing fast on type errors saves CI minutes.

With `tox`, the same pipeline can be expressed as environment targets:

```ini
[tox]
envlist = typecheck, test, lint

[testenv:typecheck]
commands = mypy src/ --strict

[testenv:test]
commands = pytest --cov=src --cov-fail-under=80

[testenv:lint]
commands = ruff check src/ tests/
```

## Verify

After implementing this pipeline, verify that:

1. A type error in production code causes `mypy`/`pyright` to fail before tests run.
2. A missing test case for a new branch drops coverage below the threshold and fails the CI step.
3. Parametrized test cases appear individually in the test output with their `ids`.
4. Fixtures are shared correctly — changing a fixture in `conftest.py` updates all dependent tests.
5. The CI pipeline completes in a reasonable time (type check + tests + lint should be under a few minutes for small-to-medium projects).

## Common errors

- **Coverage threshold too high, too early.** Setting `--cov-fail-under=90` on a codebase at 60% coverage blocks every PR. Start at the current level and ratchet up gradually.
- **Parametrize with complex IDs.** Auto-generated IDs like `test_calculate_total[items0-discount0-expected0]` are unreadable. Always pass explicit `ids` when the default names are not descriptive.
- **Fixture scope mismatch.** A `function`-scoped fixture that creates a database connection runs once per test — correct for isolation, slow for suites with hundreds of tests. Promote to `module` or `session` scope when the resource is safe to share.
- **Type checker and test runner disagree on environment.** If `mypy` sees different installed packages than `pytest` (e.g., missing stubs), type errors appear in CI but not locally. Pin the same virtual environment for both, or use `--python-version` to align targets.
- **Ignoring type-check failures.** Adding `# type: ignore` without a comment explaining why defeats the purpose. Track suppressions and review them periodically — each one is a known gap in type safety.
