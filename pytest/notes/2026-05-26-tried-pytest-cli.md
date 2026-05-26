# Tried pytest CLI options today

I installed pytest with `uv add --dev pytest` and ran my first test file. Here's what I learned about the CLI.

## Basic run

```
pytest
```

That discoveres and runs all `test_*.py` files in the current directory. Green dots = pass, red F = fail.

## Useful flags I tried

- `pytest -v` — verbose mode, shows each test name. Much easier to see what's happening.
- `pytest -k "addition"` — runs only tests whose name contains "addition". Handy for focusing.
- `pytest -x` — stop after the first failure. Great for debugging.
- `pytest --tb=short` — shorter tracebacks. Less noise.

## Output formats

The default is the "short" summary — a line of dots and a summary at the end. With `-v` you get the full test names. That's all I needed today — I didn't try `--junitxml` or `--tb=long` yet.

## What I'd try next

Figure out how `--tb=long` looks, and maybe try `pytest --co` to see if it does anything useful. Also want to try `pytest --last-failed` after a partial fix.
