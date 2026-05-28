# mypy — quick primer

> First-day notes for someone who's never used mypy. Personal voice, plain language.

## What is it?

mypy is a static type checker for Python. If you've used TypeScript for JavaScript, it's the same idea — you add type annotations to your code, and mypy checks that you're not calling functions with the wrong types or accessing attributes that don't exist. It runs as a standalone tool (not at runtime), so it catches bugs before you even execute the code.

## What does it do?

It reads your Python source files, follows the type hints you've added (or infers types from unannotated code), and reports any mismatches. You can run it on a single file or a whole project. It supports gradual typing — you can add types to part of your codebase and leave the rest unannotated, and mypy will only check what it can.

## Why does it exist?

Python is dynamically typed, which is great for fast prototyping but terrible for catching type-related bugs. Before mypy, the only way to catch a `NoneType has no attribute X` error was to run the code and hope your test covered that path. mypy catches that class of bug statically. It also serves as living documentation — type annotations tell future readers what a function expects and returns.

## Key terminology

- **Type annotation** — A hint you add to Python code that tells mypy what type a variable should be. Example: `def greet(name: str) -> str:`.
- **Gradual typing** — mypy's ability to check partially-typed code. Unannotated functions are assumed to accept and return `Any`, which mypy skips unless you pass `--check-untyped-defs`.
- **`Any`** — The "dynamic" type. Any operation is allowed on an `Any` value, and mypy won't report errors. It's the escape hatch from strict checking.
- **`reveal_type()`** — A debugging function you can drop into your code. mypy prints the inferred type of any expression when it encounters `reveal_type(x)`. Not available at runtime.
- **`# type: ignore`** — A comment that tells mypy to skip type-checking a specific line. Example: `x = foo()  # type: ignore[assignment]`.
- **`--strict`** — A flag that enables a set of strict options (checking untyped defs, disallowing `Any`, etc.). Good for greenfield projects; painful to retroactively apply to a large codebase.
- **Stub file (`.pyi`)** — A file that declares type signatures without implementation. Used for third-party packages that don't ship their own types.
- **`mypy.ini` / `pyproject.toml`** — Config files for setting mypy options per project. You can set `--strict` once in config instead of passing it on every invocation.

## A tiny example

```python
# demo.py
def greet(name: str) -> str:
    return "Hello, " + name

greet(42)          # mypy catches this
greet("World")     # this is fine
```

Run `mypy demo.py` and it prints: `error: Argument 1 to "greet" has incompatible type "int"; expected "str"`. That's the whole loop — annotate, run mypy, fix errors, repeat.

## What I'll cover next

Now that I know what mypy is and how to run it, I want to install it with uv and try it on a deliberately broken file. Then I'll explore the CLI flags like `--strict`, `--check-untyped-defs`, and `--ignore-missing-imports` to understand what each does to the output.
