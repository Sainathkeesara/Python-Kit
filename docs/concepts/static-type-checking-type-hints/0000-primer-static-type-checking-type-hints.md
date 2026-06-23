# Static Type Checking & Type Hints — quick primer

> First-day notes on static type checking and type hints. What they are, why they matter, and the key ideas to know.

## What is it?

I just learned that type hints are a way to annotate Python code with the expected types of variables, function parameters, and return values. They were introduced in Python 3.5 through PEP 484. Static type checking is what happens when a tool like mypy or Pyright reads those annotations and checks whether the code actually uses values in a way that matches the declared types — without running the program.

It's like having a spell-checker for your code's data flow. You write `def greet(name: str) -> str:` and the type checker can tell you if you later try to pass an integer where a string is expected. Python itself ignores these annotations at runtime — they're entirely optional and meant for developer tooling.

## Why does it matter for Python?

As a Python practitioner, I deal with a lot of code that gets passed around between functions, modules, and even different developers. Without type hints, I have to read the implementation to figure out what a function expects and returns. With them, the signature tells me directly.

The big wins I see:
- Catching bugs early — calling a function with the wrong argument type gets flagged before I even run the tests.
- Better editor support — autocomplete, jump-to-definition, and inline docs all work better when types are annotated.
- Self-documenting code — the types serve as living documentation that can't go out of date the way comments can.

In the Python ecosystem, tools like mypy, Pyright (used by VS Code's Pylance), and Ty all do static type checking. Ruff also has rules that catch some type-related issues.

## Key terminology

- **Type hint** — An annotation on a variable, parameter, or return value indicating its expected type. Example: `age: int = 25` or `def get_name() -> str:`.
- **Static type checker** — A tool that analyzes source code without running it to find type inconsistencies. Example: running `mypy script.py` to find mismatched types.
- **Gradual typing** — Python's approach where you can add type hints to part of your codebase while leaving the rest untyped. The checker only enforces the typed parts.
- **`Any`** — A special type that tells the checker "this could be anything, don't check it." Useful when migrating legacy code.
- **`Optional[str]`** — Shorthand for `Union[str, None]`. Means the value could be a string or `None`.
- **Type stub (`.pyi`)** — A file that declares types for code you didn't write, like third-party libraries without built-in type hints.
- **`reveal_type()`** — A debugging function that makes the type checker print what type it infers for an expression. Example: `reveal_type(some_var)` in mypy will output the inferred type.
- **`--strict`** — A mode that enables all the strictest checks. In mypy, this flags untyped functions, missing return types, and more.

## A concrete example

Here's a tiny example I tried to understand how type checking works:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 5)      # OK — both args are ints
bad = add("hello", 2)   # mypy flags: Argument 1 has incompatible type "str"; expected "int"
```

Running `mypy --strict` on this file would pass on line 1-3 and flag line 4 with an error. Without type hints, both calls would run without complaint at runtime (Python would just concatenate "hello" with 2), but the second call is almost certainly a bug.

## How this connects to what's next

With this foundation, I can now make sense of tools like mypy and Ty, which are static type checkers for Python. Typer also builds on type hints — it uses function annotations to automatically generate CLI argument parsers, so understanding type hints is a prerequisite for using it effectively.
