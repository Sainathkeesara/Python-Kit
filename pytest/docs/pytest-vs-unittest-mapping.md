# pytest vs unittest — API mapping and migration patterns

> Following the official pytest docs on migrating from unittest, here's what worked and where I got stuck.

## The setup

I started with a small unittest test suite and tried porting it to pytest piece by piece. The official [pytest unittest migration guide](https://docs.pytest.org/en/stable/how-to/unittest-integration.html) covers the basics, but the practical gotchas only showed up when I actually ran the thing.

## Direct API mapping

| unittest | pytest | Notes |
|---|---|---|
| `unittest.TestCase` | plain `class` / no base class | pytest discovers any class with `Test` prefix |
| `self.assertEqual(a, b)` | `assert a == b` | plain `assert` — no method lookup |
| `self.assertRaises(Exc, fn)` | `pytest.raises(Exc)` | context manager, works inline |
| `self.assertAlmostEqual(a, b)` | `pytest.approx(a) == b` | returns a comparison object |
| `setUp()` / `tearDown()` | `def setup_method(self)` or `yield` fixture | fixtures are more composable |
| `@unittest.mock.patch(...)` | `monkeypatch` fixture or `mocker` (pytest-mock) | monkeypatch is built-in, mocker needs an extra plugin |
| `self.assertIn(a, b)` | `assert a in b` | plain Python |
| `self.assertTrue(cond)` | `assert cond` | plain Python |
| `@unittest.skipIf(...)` | `@pytest.mark.skipif(...)` | similar, but pytest uses marker registry |

## Steps I followed

1. **Ran pytest on the unittest suite unchanged** — it worked out of the box. pytest has a `unittest.TestCase` runner built in.
2. **Replaced `self.assertEqual` with plain `assert`** one test at a time.
3. **Switched `setUp` to a fixture** — this is where things got interesting. A `yield` fixture does what `setUp` + `tearDown` did, but I could share it across test files with `conftest.py`.
4. **Replaced `assertRaises` with `pytest.raises`** — the context manager form is cleaner.
5. **Added parametrization** — `@pytest.mark.parametrize` replaced manual for-loops in unittest.

## Where I got stuck

- **`self.skipTest(...)` doesn't work in a fixture.** In unittest you can skip from `setUp`. In pytest, you need `pytest.skip(...)` inside the fixture or use `@pytest.mark.skipif` on the test.
- **Fixtures vs `setUp` ordering.** If a test class inherits from another class's `TestCase`, the MRO for `setUp` is explicit. With fixtures, the order depends on fixture dependencies, which pytest resolves automatically — but I had one case where two fixtures requested the same resource and I got an unexpected interaction.
- **`monkeypatch` doesn't auto-restore.** `unittest.mock.patch` restores on teardown automatically. `monkeypatch` needs explicit `undo()` or you scope it to the fixture so it rolls back when the fixture goes out of scope. Easy to forget.
- **`pytest.approx` vs `assertAlmostEqual`.** `approx` works on collections (lists, dicts) which is nice, but the default tolerance differs (relative vs absolute) — caught me on the first float comparison.

## What I'd try next

- Migrate a bigger test suite with inherited `TestCase` classes to see how fixture scoping interacts with class hierarchies.
- Try `pytest-mock` for a cleaner `mocker.spy` / `mocker.patch` workflow vs raw `unittest.mock`.
- Look into `pytest-xdist` for parallel test execution — unittest suites are usually serial.
