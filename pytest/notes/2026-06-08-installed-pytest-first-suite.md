# Installed pytest and ran my first test suite

I installed pytest with `uv add --dev pytest` in my project. Wrote a tiny test file called `test_math.py` with two functions: `test_add` and `test_sub`. Each one just has an `assert` statement.

Ran `pytest` from the project root. Saw two green dots and a passing summary. That was it — no config, no test loader, no `unittest.TestCase`. I was skeptical it'd find my file, but it just worked.

## What tripped me up

I named my file `test-math.py` with a hyphen instead of an underscore. pytest silently skipped it. Renamed to `test_math.py` and it picked up both tests. The docs say it globs for `test_*.py` — hyphens aren't part of that pattern.

Also, I didn't install pytest at first — just wrote the file and ran `pytest`. Got `command not found`. Forgot I needed to install it in the venv first. `uv add --dev pytest` fixed that.

## What I'd try next

Learn how to test exceptions with `pytest.raises` and try `-k` to filter tests by name.
