# Tried the Ty quickstart — type checking with the Astral type checker

I followed the official Ty quickstart today to see how Astral's new type checker compares to mypy. I'd read the primer earlier, so I knew it was a Rust-based type checker from the uv/Ruff team, but I hadn't actually run it yet.

## Getting started

The quickstart says to run `uvx ty check` — no install needed. I didn't have `uvx` available, so I installed it globally first:

```
uv tool install ty
```

That grabbed the binary and put it on my PATH. Ran `ty --version` to confirm — version 0.0.39.

## First check

I pointed it at a small Python file with a deliberate type error:

```python
# demo.py
def greet(name: str) -> str:
    return "Hello, " + name

greet(42)
```

Ran `ty check demo.py`. The output was clear and fast — barely felt like it ran. It showed:

```
error[demo.py:5:7]: Type `int` is not assignable to parameter `name` (type `str`)
```

The error message includes the file, line, column, the expected type, and what it got. I liked that it gave me the exact column instead of just the line — makes finding the spot faster.

## Trying it on a whole project

I ran `ty check .` in the Python-Kit root. It scanned all `.py` files across the repo. The output was... a lot. Hundreds of errors from untyped libraries, missing return annotations, and implicit `Any` usage.

What surprised me: it listed errors grouped by file, with a summary at the end showing file count, error count, and check duration. It took about 0.4 seconds to scan the whole repo — noticeably faster than mypy on similar-sized projects.

## What tripped me up

- **`uvx` wasn't available.** The quickstart assumes you have `uvx` set up, but I only had `uv` installed. Had to use `uv tool install ty` instead.
- **Running on the whole repo was overwhelming.** The quickstart doesn't mention excluding virtual environments or build directories. I had a bunch of errors from `.venv/` before I added an exclude config.
- **Config file format isn't obvious.** Ty uses `pyproject.toml` under `[tool.ty]`, but I couldn't find a quick reference in the quickstart — had to dig into the docs for the config schema.
- **`ty check` vs just `ty`.** Running `ty` without `check` gives a different behavior (it opens an interactive session?). I expected `ty` to be equivalent to `ty check` like `ruff` is to `ruff check`.

## What I'd try next

I want to configure Ty with a proper `pyproject.toml` section — set strict mode, exclude `tests/` and `.venv/`, and maybe enable some of the pedantic rules. Then I'd like to integrate it into a pre-commit hook alongside Ruff so both linting and type checking run on every commit.
