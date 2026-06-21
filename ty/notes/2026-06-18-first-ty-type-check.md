# Installed Ty and ran my first type check

I wanted to try Astral's type checker, Ty. I'd seen it mentioned as a faster alternative to mypy. Here's what happened.

## Getting it installed

The docs say `uvx ty check` but I didn't have `uvx` set up. I used:

```
uv tool install ty
```

That downloaded the binary and put it on PATH. `ty --version` showed v0.0.39.

## First check

I wrote a tiny file with a bug:

```python
def hello(name: str) -> str:
    return "Hello, " + name

hello(42)
```

Ran `ty check demo.py`. Output was fast — barely a pause — and showed:

```
error[demo.py:5:7]: Type `int` is not assignable to parameter `name` (type `str`)
```

The error included the exact column (`7`) pointing at the bad argument.

## Ran it on a whole directory

`ty check .` scanned all `.py` files in the current project. It completed in under half a second — way faster than mypy on the same project. The output was grouped by file with a summary at the end: file count, error count, duration.

## Things I stumbled on

- `uvx` isn't always available. The quickstart assumes it is, but I had to use `uv tool install ty` instead.
- Running on the whole project from root picked up `.venv/` files. I got errors from vendored libraries until I added an exclude to `pyproject.toml`.
- `ty` without `check` opens something else (maybe an interactive prompt?). I expected it to be equivalent to `ty check` like `ruff` vs `ruff check`.
- Config goes under `[tool.ty]` in `pyproject.toml`, but the quickstart doesn't show the schema — I had to search the docs.

Next I want to try Ty with `--strict` and compare error counts against mypy on the same codebase.
