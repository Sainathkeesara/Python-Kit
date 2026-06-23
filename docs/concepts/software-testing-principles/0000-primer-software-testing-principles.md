# Software Testing Principles — quick primer

> First-day notes on Software Testing Principles. What it is, why it matters, and the key ideas to know.

## What is it?

Software Testing Principles are the core ideas behind verifying that code does what it's supposed to do. I just learned that testing isn't about proving the code works — it's about systematically finding where it breaks. The main types are unit tests (test one small function), integration tests (test how pieces work together), and end-to-end tests (test the full system from the user's perspective). Each serves a different purpose, and a good test suite has a mix of all three.

## Why does it matter for Python?

I use pytest almost daily now, and the tool itself is just the mechanics — the real value comes from knowing what to test and how to write tests that actually catch bugs. Testing principles tell me: test one thing per test, use descriptive test names, cover edge cases (empty input, boundary values, wrong types), and keep tests independent of each other. Without these principles, I'd write tests that pass but don't catch real regressions. Tools like tox also make more sense once I understand why different testing environments matter.

## Key terminology

- **Unit test** — Tests a single function or method in isolation. Example: `def test_add(): assert add(2, 3) == 5`
- **Assertion** — A check that a condition is true; a test passes if all its assertions pass. Example: `assert result is not None`
- **Test fixture** — Setup code that creates data or state before a test runs. Example: creating a temporary directory for file I/O tests
- **Parametrization** — Running the same test logic with different input values. Example: `@pytest.mark.parametrize("a,b,expected", [(1,2,3), (0,0,0), (-1,1,0)])`
- **Test coverage** — A metric showing what percentage of code lines are executed during tests. Example: 85% line coverage means 15% of lines are never tested
- **Red-Green-Refactor** — A TDD cycle: write a failing test (red), write code to make it pass (green), then clean up the code (refactor)
- **Mock** — A fake object that replaces a real dependency during testing. Example: mocking `requests.get()` so tests don't hit the network
- **Regression** — A bug that reappears after a change. Tests help catch regressions automatically on every run

## A concrete example

Here's a small test I wrote to practice testing principles:

```python
def is_even(n: int) -> bool:
    return n % 2 == 0

# test normal case
def test_is_even_with_even():
    assert is_even(4) is True

# test the other branch
def test_is_even_with_odd():
    assert is_even(7) is False

# test an edge case
def test_is_even_with_zero():
    assert is_even(0) is True
```

Each test checks one thing. I test both branches of the logic (even and odd) and one edge case (zero). The test names describe what they verify, so a failure immediately tells me which scenario broke.

## How this connects to what's next

Testing principles are the foundation for using pytest effectively and for setting up CI pipelines with tox. Next I'll practice writing parametrized tests in pytest and learn how to organize shared fixtures with conftest.py.
