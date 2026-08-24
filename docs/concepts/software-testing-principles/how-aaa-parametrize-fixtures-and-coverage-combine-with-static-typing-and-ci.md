---
last_verified: 2026-08-24
tool_version: n/a
---

# How AAA, parametrize, fixtures, and coverage combine with static typing and CI

## Purpose

This note shows how four testing building blocks — Arrange-Act-Assert structure, `pytest.mark.parametrize`, fixtures, and coverage measurement — fit together when you add static type checking and a CI pipeline. It is one pattern among many; the pytest docs also suggest other combinations depending on team size and test speed requirements.

## When to use

Use this pattern when a single test module must exercise multiple input combinations, share expensive setup across tests, measure which lines execute, and fail fast on type mismatches before the test runner starts. It is most useful in `src/`-layout packages where import mistakes are common and CI time is a shared constraint.

## Prerequisites

- A `src/`-layout package with `pyproject.toml` declaring `[tool.pytest.ini_options]` and `[tool.mypy]`.
- `pytest`, `pytest-cov`, and `mypy` installed in the active environment.
- A CI runner that caches the environment between jobs.

## Steps

1. **Arrange-Act-Assert baseline.** Write each test function with three clearly named sections: set up the inputs (Arrange), call the production code (Act), and assert the expected state (Assert). Static type checking rewards this layout because type mismatches cluster in the Act step, where the function signature is most visible.

2. **Parametrize over input combinations.** Replace loops or repeated test functions with `@pytest.mark.parametrize("input, expected", [...])`. Type hints on the test function parameters help mypy catch argument-order mistakes inside the parametrize list, especially when the tuple contains mixed types.

3. **Share setup with fixtures.** Move repeated Arrange code into a `@pytest.fixture`. Fixtures keep the test body focused on Act/Assert and let pytest handle cleanup. Mypy does not type-check fixture bodies by default unless the fixture function is annotated and the test function requests the fixture by name with a type hint.

4. **Measure coverage.** Run `pytest --cov=src/<package> --cov-report=term-missing`. Coverage tells you which lines were never exercised by the parametrized inputs; combine that with mypy's `--strict` to ensure the untested lines are also type-safe.

5. **Wire CI.** In a GitHub Actions job, run `mypy src/` first, then `pytest --cov=src/<package> --cov-report=xml`. Upload the coverage XML as an artifact or to a coverage service. If mypy fails, the CI job exits before pytest runs, keeping feedback fast.

## Verify

- `mypy src/` returns no errors.
- `pytest --cov=src/<package>` shows the expected coverage percentage for the files under test.
- The CI job logs show mypy in a separate step before pytest, and the coverage artifact is uploaded when tests pass.

## Common errors

**Fixture scope confusion.** A `session`-scoped fixture that mutates global state can make coverage numbers lie because later tests see the mutated state. In one `src/`-layout package, a session-scoped fixture mutated a module-level list; the first test passed, but the second saw the mutated state and reported 100% coverage for code that had never been exercised cleanly. Switching to `function` scope exposed the missing branch and dropped coverage to 82%, which was accurate.

**Parametrize argument-order drift.** When the parametrize tuple and the function signature drift apart, pytest raises a `TypeError` at collection time. Adding type hints to the test function parameters lets mypy catch the mismatch earlier, before pytest starts.
