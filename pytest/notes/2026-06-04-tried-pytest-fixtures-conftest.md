# Tried pytest fixtures with conftest.py

I wanted to understand how pytest fixtures work beyond the basic `@pytest.fixture` decorator. Specifically, how conftest.py shares setup and teardown across multiple test files.

## Setting up conftest.py

I created a `tests/` directory with two test files and a conftest.py:

```
tests/
├── conftest.py
├── test_users.py
└── test_posts.py
```

In conftest.py I put a fixture that sets up a temp database and cleans it up after:

```python
import pytest
import tempfile
import os

@pytest.fixture
def db_path():
    # setup — create a temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    tmp.close()
    yield tmp.name
    # teardown — remove the temp file
    os.unlink(tmp.name)
```

The `yield` pattern is nice — whatever comes before runs as setup, whatever comes after runs as teardown. No need for `addfinalizer` or try/finally blocks.

## Using the fixture in test files

In `test_users.py`:

```python
def test_create_user(db_path):
    # db_path comes from conftest.py — didn't have to import anything
    assert db_path.endswith(".db")
    # ... real test would use the path to init a DB
```

In `test_posts.py`:

```python
def test_create_post(db_path):
    assert db_path.endswith(".db")
```

Both files just declare `db_path` as a parameter and pytest wires it up. Felt like magic at first.

## What tripped me up

- I put a fixture in conftest.py inside `tests/` but tried using it from a test in the project root — it didn't work. conftest.py only applies to tests in its directory tree, not above it.
- I named my conftest.py with a capital C (`Conftest.py`) because I thought it was a class. pytest silently ignored it. The filename must be exactly `conftest.py`.
- I tried yielding multiple times from one fixture — that's a runtime error. One fixture, one yield.
- Fixture scope defaults to `function`. I wanted a DB that outlives individual tests and had to explicitly set `scope="session"` on the fixture.

## What I'd try next

I want to explore fixture parametrization with `params=` and the `request` object, and maybe chain fixtures where one fixture uses another. Also curious about `autouse=True` for fixtures that should run for every test without being explicitly requested.

```python
@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    # runs once for the whole session, no test needs to ask for it
    ...
```
