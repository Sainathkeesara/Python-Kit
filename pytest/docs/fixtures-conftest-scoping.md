---
last_verified: 2026-08-22
tool_version: n/a
sources: []
---

# pytest fixtures and scoping: conftest, fixture ordering, and tmp_path

## Purpose

This doc covers how pytest fixtures work under the hood — scoping rules, conftest.py resolution, fixture ordering when dependencies overlap, and the built-in `tmp_path` fixture. The goal is to move beyond "fixture = setup" and understand the mechanics that determine when a fixture runs, how many times, and in what order relative to other fixtures.

## When to use

Use this when:

- A fixture is running setup code more often than expected (e.g. a database connection recreated per-test instead of per-session).
- Two fixtures depend on the same resource and the teardown order matters.
- Tests need temporary files or directories and `tmp_path` or `tmp_path_factory` is the right choice over manual `tempfile` calls.
- Shared fixtures in `conftest.py` aren't visible to a test file that should use them.

## Prerequisites

- pytest installed (`pip install pytest` or `uv add --dev pytest`)
- A project with at least one `test_*.py` file
- Familiarity with basic `@pytest.fixture` usage (see the pytest primer in this kit)

## How fixtures work

### Scoping

A fixture's `scope` controls how often its setup/teardown runs:

| Scope | Setup runs | Teardown runs | Typical use |
|---|---|---|---|
| `function` (default) | once per test | once per test | fresh data per test |
| `class` | once per test class | once per test class | shared DB connection for a class |
| `module` | once per test file | once per test file | expensive one-time init |
| `session` | once per entire run | once per entire run | shared server, seed data |

A session-scoped fixture runs its setup exactly once at the start of the test session and tears down at the very end. A function-scoped fixture runs setup before each test function and teardown after it. The scope is set via the `scope` parameter:

```python
@pytest.fixture(scope="session")
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

When a lower-scope fixture depends on a higher-scope fixture, the higher-scope fixture's setup runs first and its teardown runs last. A function-scoped fixture that requests a session-scoped fixture will reuse the same session-scoped instance across all tests that share the session.

### conftest.py resolution

`conftest.py` is pytest's mechanism for sharing fixtures without imports. Key rules:

1. **Directory-scoped.** A `conftest.py` in `tests/` provides fixtures to all tests under `tests/` and its subdirectories. It does NOT provide fixtures to tests above it or in sibling directories.
2. **Filename is exact.** Must be `conftest.py` — capitalization matters. `Conftest.py` is silently ignored.
3. **Chained loading.** If `tests/unit/conftest.py` and `tests/conftest.py` both define a fixture with the same name, the more specific one (`tests/unit/conftest.py`) wins for tests in `tests/unit/`.
4. **No imports needed.** Tests declare fixture names as parameters; pytest resolves them from conftest.py files in the directory tree.

```
project/
├── conftest.py          # session-wide fixtures
├── tests/
│   ├── conftest.py      # test-wide fixtures
│   ├── unit/
│   │   ├── conftest.py  # unit-specific overrides
│   │   └── test_math.py
│   └── test_integration.py
```

### Fixture ordering and dependencies

When a test requests multiple fixtures, pytest resolves them by:

1. **Dependency graph.** If fixture A requests fixture B, B runs first.
2. **Scope ordering.** Higher-scope fixtures run before lower-scope fixtures.
3. **Declaration order.** When two fixtures are at the same scope and have no dependency relationship, they run in the order they appear in the test function's parameter list.

A common gotcha: two fixtures that both request the same session-scoped resource will each get their own teardown call, but the session-scoped resource's teardown runs only once — after both lower-scope fixtures have torn down.

### tmp_path and tmp_path_factory

`tmp_path` is a built-in function-scoped fixture that provides a `pathlib.Path` to a unique temporary directory. Each test gets its own directory; it's cleaned up after the test completes.

```python
def test_write_config(tmp_path):
    config_file = tmp_path / "config.toml"
    config_file.write_text("[tool.pytest]\naddopts = '-v'\n")
    assert config_file.read_text().startswith("[tool.pytest]")
```

For session-scoped temporary directories, use `tmp_path_factory`:

```python
@pytest.fixture(scope="session")
def shared_tmp(tmp_path_factory):
    return tmp_path_factory.mktemp("shared")
```

`tmp_path` is preferred over `tempfile.mkdtemp()` because pytest handles cleanup automatically and the path is unique per test.

## Verify

Run a small test to confirm scoping:

```python
import pytest

call_count = 0

@pytest.fixture(scope="session")
def session_fix():
    global call_count
    call_count += 1
    return call_count

def test_one(session_fix):
    assert session_fix == 1

def test_two(session_fix):
    assert session_fix == 1
```

Both tests pass — `session_fix` ran once. Change scope to `function` and `test_two` will fail with `assert 2 == 1`.

## Common errors

- **"fixture 'X' not found"** — the fixture is not in a `conftest.py` visible to the test file, or the filename is wrong.
- **Fixture runs too often** — scope is `function` (the default) when you wanted `session` or `module`.
- **Teardown order surprise** — fixture A depends on fixture B; B's teardown runs after A's, which may matter if B's resource is needed during A's teardown. Restructure dependencies or use `addfinalizer`.
- **`tmp_path` not cleaned up** — the directory persists between runs if the test crashes before teardown. Pytest normally cleans up, but a hard kill (SIGKILL) can leave residue.
