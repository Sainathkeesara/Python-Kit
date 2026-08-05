---
last_verified: 2026-08-04
tool_version: n/a
sources: []
---

# pytest quickstart — what tripped me up

> L2 lab note: working through the official pytest quickstart, fixtures, parametrize, and conftest.

## What I set out to do

I wanted to move beyond `assert` statements in test functions and understand how pytest handles setup/teardown and running the same test against multiple inputs. The quickstart covers three things I'd heard about but never used: fixtures, `@pytest.mark.parametrize`, and `conftest.py`.

## Fixtures

A fixture is pytest's way of injecting setup code into a test. You define it with `@pytest.fixture` and then accept it as a parameter in the test function. The part that tripped me up: pytest resolves fixture parameters by name, so the parameter name in the test must match the fixture function name exactly. I named mine `db_connection` in the fixture but `conn` in the test and got a confusing "fixture not found" error.

The fix was just matching names. Once I did that, the fixture ran before each test that needed it, and pytest handled teardown with `yield` automatically.

## Parametrize

`@pytest.mark.parametrize` runs one test function against multiple input/expected-output pairs. I expected it to feel like a loop, but it generates separate test cases — each pair shows up as its own entry in the test report, which is useful for pinpointing which input failed.

The thing I kept forgetting: the first argument is a string with the parameter names separated by commas (like `"a, b, expected"`), and the second argument is a list of tuples. The string names must match the test function's parameter names exactly.

## conftest.py

`conftest.py` is a special filename pytest picks up automatically — no import needed. I put a shared fixture in it and it was available to every test in that directory and subdirectories. I initially put `conftest.py` in the wrong directory (the project root instead of the tests directory) and none of the tests could find the fixture. Moving it into `tests/` fixed it immediately.

## What I'd do differently next time

- Name fixtures and test parameters the same from the start.
- Put `conftest.py` in `tests/` (or the directory containing the tests that need it) before writing any fixtures.
- Use parametrize early — it catches mismatched expectations faster than writing individual test functions.
