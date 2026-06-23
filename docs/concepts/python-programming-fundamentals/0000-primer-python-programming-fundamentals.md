# Python Programming Fundamentals — quick primer

> First-day notes on Python Programming Fundamentals. What it is, why it matters, and the key ideas to know.

## What is it?

Python Programming Fundamentals are the basic building blocks you use in every Python script — variables, data types (ints, strings, lists, dicts), control flow (if/else, loops), functions, and imports. I've been writing Python for a bit and these are the things I reach for constantly without even thinking. They're like the vocabulary and grammar of the language; once you know them, you can read and write almost any Python code.

## Why does it matter for Python?

Every tool in the Python ecosystem builds on these fundamentals. A pytest test is just a function with assertions inside it. A pyproject.toml file is structured like a Python dictionary. Type hints are annotations on variables and function signatures. Even when I'm configuring Ruff or mypy, I'm writing Python-flavored config files. If I don't have a solid grasp of lists, dicts, functions, and loops, the documentation for these tools won't make much sense.

## Key terminology

- **Variable** — A name that holds a value. Example: `timeout = 30`
- **String** — Text data wrapped in quotes. Example: `name = "pytest"`
- **List** — An ordered sequence, written with square brackets. Example: `tools = ["ruff", "mypy", "pytest"]`
- **Dictionary** — Key-value pairs, written with curly braces. Example: `settings = {"strict": True, "ignore": ["*.pyc"]}`
- **Function** — Reusable code defined with `def`, takes inputs and returns a result. Example: `def double(x): return x * 2`
- **Loop** — Repeat code for each item using `for`. Example: `for t in tools: print(t)`
- **Conditional** — Branch code based on a condition with `if`/`elif`/`else`. Example: `if x > 0: print("positive")`
- **Import** — Load code from another module. Example: `import json`
- **Type hint** — Annotation indicating expected type of a parameter or return value. Example: `def greet(name: str) -> str:`
- **Exception** — Runtime error caught with `try`/`except`. Example: `try: open("missing.txt") except FileNotFoundError: ...`

## A concrete example

Here's a tiny script that uses several fundamentals at once:

```python
def summarize(packages: list[dict]) -> None:
    for pkg in packages:
        name = pkg["name"]
        version = pkg.get("version", "unknown")
        print(f"{name}=={version}")

deps = [
    {"name": "ruff", "version": "0.9.0"},
    {"name": "mypy", "version": ""},
]
summarize(deps)
```

This shows a function with type hints, a list of dicts, a for loop, a method call with a default value, and an f-string — all in about 10 lines.

## How this connects to what's next

With the fundamentals down, I can focus on the quality toolchain: writing tests with pytest, catching type errors with mypy, and keeping code clean with Ruff. These tools are just Python code that builds on the same basics.
