# pytest — quick primer

> First-day notes for someone who's never used pytest. Personal voice, plain language.

## What is it?

pytest is a testing framework for Python. If you've ever written `if __name__ == '__main__'` blocks to test your functions, or used `unittest` and felt like it was too much boilerplate, pytest is the alternative people keep recommending. It's to testing what `requests` is to HTTP — simpler, less ceremony, and you get more done with fewer lines.

pytest is a testing framework for Python. It's like unittest which comes with Python, but pytest feels more like writing normal Python code. Where unittest has a lot of setup with classes and methods like `setUp` and `tearDown`, pytest lets you just write functions that start with `test_` and it handles the rest.

## What does it do?

You write functions with names like `test_something`, and pytest finds them, runs them, and reports which passed and which failed. It handles test discovery, fixtures (setup/teardown), parameterized tests, and plugins for coverage, mocking, and more. You can run it with one command: `python -m pytest`.

pytest finds and runs your test functions automatically, reports results with a clean summary, and gives you helpful output when tests fail. It handles test fixtures (setup/teardown) with simple decorator syntax instead of class methods.

## Why does it exist?

Before pytest, Python had `unittest` in the standard library. It works, but it forces you into class-based tests, camelCase method names, and a lot of `self.assertEqual` calls. If you just want to assert that two things are equal, `assert x == y` is a lot less typing. pytest exists because the community wanted testing to feel like writing regular Python, not like writing Java.

Day to day, it's used by almost everyone doing Python development — from data scientists checking their transformations to web developers testing API endpoints. It's the de facto standard.

Before pytest, Python testing meant either unittest (verbose boilerplate) or nose (which is now dead). pytest filled the gap with a simpler, more Pythonic approach to testing. Most Python projects today use pytest as their default test runner.

## Key terminology

- **Test function** — A function whose name starts with `test_` that pytest discovers and runs. Example: `def test_add(): assert 1 + 1 == 2`.
- **Assertion** — A plain `assert` statement. pytest rewrites them to give you detailed diff output when they fail.
- **Fixture** — A function decorated with `@pytest.fixture` that provides setup (like a database connection or a temp file). Tests that need it list the fixture name as a parameter. Example: `def test_db(db_connection): ...`.
- **Parametrization** — Running the same test function with different inputs. Example: `@pytest.mark.parametrize('a,b,expected', [(1,2,3), (0,0,0)])`.
- **Conftest.py** — A special file where you put shared fixtures. pytest automatically loads conftest.py files from the test directory and its parents.
- **Test discovery** — The way pytest finds tests: by default, it looks for files named `test_*.py` and functions named `test_*` inside them.
- **Markers** — Decorators like `@pytest.mark.skip` or `@pytest.mark.slow` that give pytest extra info about a test. You can also define custom markers.
- **Plugin** — A package that extends pytest, like `pytest-cov` for coverage or `pytest-mock` for mocking. Tons of plugins exist.
- **test discovery** — pytest automatically finds files named `test_*.py` and functions named `test_*`; no manual suite creation needed
- **fixture** — a setup function decorated with `@pytest.fixture` that provides test data or resources (database connections, temp files, etc.)
- **assert** — just use Python's `assert` statement; pytest introspects it to show exactly what went wrong
- **parametrize** — feed multiple inputs to the same test using `@pytest.mark.parametrize` decorator
- **xunit-style setup** — the old unittest-style `setup_method` and `teardown_method` still work if you need them

## A tiny example

```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
```

Run it with `python -m pytest test_example.py -v` and you'll see two passing tests with green dots.

```python
# test_example.py
def test_addition():
    result = 1 + 1
    assert result == 2
```
Run with `pytest test_example.py` — that's it.

## What I'll cover next

I want to understand fixtures deeply — how to share setup across tests without repeating code — and try parametrized tests so I can stop writing the same test five times with different inputs. After that, conftest.py patterns and maybe pytest-cov for coverage reporting.

I'll write my first real test with pytest and explore the different CLI output options it provides.
