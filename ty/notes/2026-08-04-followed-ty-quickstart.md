---
last_verified: 2026-08-04
tool_version: n/a
---

# Ty — quickstart notes

> What I learned following the official Ty quickstart. First-day scratch notes.

## What is it?

Ty is a type checker for Python from the Astral team (same folks who make Ruff). It checks your Python code for type errors using the same type annotations you already write with `typing` or built-in syntax. Think of it as a faster, more opinionated alternative to mypy — it reads your annotations and tells you where things don't line up.

## What does it do?

I installed Ty and ran it against a small Python file. It scanned the code, found a couple of type mismatches I'd overlooked (a function returning `int` where `str` was expected, and a missing return annotation), and printed them out with line numbers. It was fast — noticeably faster than mypy on the same file.

## Why does it exist?

Before Ty, mypy was the go-to static type checker for Python. It works, but it's slow and the config can be fiddly. Ty aims to be zero-config and fast out of the box, so you can just add annotations and get feedback without spending time on setup.

## Key terminology

- **Annotation** — a type hint you add to a variable or function signature. Example: `def greet(name: str) -> str:`
- **Type mismatch** — when a value doesn't match the annotation. Example: passing an `int` to a parameter declared as `str`.
- **Return annotation** — the `-> type` part of a function signature. Example: `def add(a: int, b: int) -> int:`
- **Strict mode** — a Ty option that enforces checking all functions, even ones without annotations. Example: `ty --strict myfile.py`
- **Unannotated** — a function or variable with no type hint. Example: `def legacy(x):` has no annotations.

## A tiny example

```python
# save as demo.py
def greet(name: str) -> str:
    return f"Hello, {name}"

result = greet("world")
print(result)
```

Run `ty check demo.py` and it should pass cleanly. Change `greet(42)` and Ty will flag the type mismatch.

## What I'll cover next

Next I want to try Ty with a real project — adding annotations to an existing codebase and seeing what breaks. I'll also explore how Ty integrates with `pyproject.toml` for config.
