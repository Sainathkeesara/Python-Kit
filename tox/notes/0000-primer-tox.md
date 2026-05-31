# tox — quick primer

> First-day notes for someone who's never used tox. Personal voice, plain language.

## What is it?

tox is a test automation tool that wraps your test runner and dependency installer in isolated environments. If you've ever run `pytest` and had it fail because a dependency was missing, tox solves that — it creates a fresh virtualenv for every environment you define, installs the exact dependencies you list, then runs your tests. Think of it as a CI-pipeline-in-a-directory that you can also run locally. It's the Python community's answer to "works on my machine" complaints.

## What does it do?

It reads a `tox.ini` file, spins up virtual environments, installs deps, and runs arbitrary commands (usually tests). You can define multiple environments — one for Python 3.10, another for 3.11, maybe one with extra test dependencies. Running `tox` gives you a full matrix in one shot. It also handles linting, type-checking, and packaging steps if you want.

## Why does it exist?

Before tox, teams either wrote ad-hoc shell scripts to manage test envs or relied solely on CI. If a test only failed on Python 3.10 and you were developing on 3.11, you wouldn't know until CI ran. tox bridges that gap by making the same harness available locally and remotely. Anyone contributing to a library with a tox setup can run `tox` and get the same result the CI will.

## Key terminology

- **Environment** — A tox-managed virtualenv identified by a name like `py311` or `lint`. Each has its own Python interpreter and dependency set.
- **Factor** — A dimension of testing, usually a Python version. `py310`, `py311` are factors.
- **deps** — The list of packages tox installs into each environment before running commands.
- **commands** — The shell commands tox executes in order inside each env. Typically `[pytest, flake8, mypy]`.
- **tox.ini** — The configuration file that defines environments, dependencies, and commands.
- **envlist** — The list of environment names tox actually runs when you type `tox` with no arguments.
- **isolated build** — tox builds your package in a clean env before testing it, catching packaging bugs that `pip install -e .` would miss.

## A tiny example

Create a `tox.ini` with one environment, add a trivial test file, and run:

```ini
[tox]
envlist = py311

[testenv]
deps = pytest
commands = pytest
```

```python
# test_add.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
```

Run `tox` from the terminal. tox creates a `.tox/py311/` virtualenv, installs pytest, and runs the test.

## What I'll cover next

I should play with multiple envs (say `py310` and `py311` side by side) and see how tox handles failures per env. Then I want to figure out how to add a lint env that runs ruff on top of the test envs.
