# pytest — quick primer

> First-day notes for someone who's never used pytest. Personal voice, plain language.

## What is it?
pytest is a testing framework for Python. It's like unittest which comes with Python, but pytest feels more like writing normal Python code. Where unittest has a lot of setup with classes and methods like `setUp` and `tearDown`, pytest lets you just write functions that start with `test_` and it handles the rest.

## What does it do?
pytest finds and runs your test functions automatically, reports results with a clean summary, and gives you helpful output when tests fail. It handles test fixtures (setup/teardown) with simple decorator syntax instead of class methods.

## Why does it exist?
Before pytest, Python testing meant either unittest (verbose boilerplate) or nose (which is now dead). pytest filled the gap with a simpler, more Pythonic approach to testing. Most Python projects today use pytest as their default test runner.

## Key terminology
- **test discovery** — pytest automatically finds files named `test_*.py` and functions named `test_*`; no manual suite creation needed
- **fixture** — a setup function decorated with `@pytest.fixture` that provides test data or resources (database connections, temp files, etc.)
- **assert** — just use Python's `assert` statement; pytest introspects it to show exactly what went wrong
- **parametrize** — feed multiple inputs to the same test using `@pytest.mark.parametrize` decorator
- **xunit-style setup** — the old unittest-style `setup_method` and `teardown_method` still work if you need them

## A tiny example
```python
# test_example.py
def test_addition():
    result = 1 + 1
    assert result == 2
```
Run with `pytest test_example.py` — that's it.

## What I'll cover next
I'll write my first real test with pytest and explore the different CLI output options it provides.