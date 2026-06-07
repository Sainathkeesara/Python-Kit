# mypy first run — what tripped me up with PATH, untyped functions, and --strict

I installed mypy and ran my first type check today. Here's what actually happened.

## PATH confusion

First I tried `mypy --version` and got "command not found". I had installed mypy in a venv but the bin wasn't on my PATH. Fixed by running `uv run mypy` instead, or activating the venv with `source .venv/bin/activate` first.

## Untyped function issues

I started with a simple function without annotations:

```python
def add(a, b):
    return a + b

result = add(1, 2)
```

mypy ran fine, no errors. But when I added type hints to the call site:

```python
def add(a, b):
    return a + b

result: int = add(1, 2)  # No error here
result2: str = add(1, 2)  # Also no error!
```

The untyped function parameters let mypy infer any type. It didn't catch the wrong assignment because `a` and `b` could be anything.

## Trying --strict

Then I added `--strict` to see what gets stricter:

```bash
mypy --strict demo.py
```

This caught a bunch of new things:
- Missing return type annotation (`int` was inferred but explicit was required)
- Missing argument type annotations
- Missing type hint for `result` variable

The output was way more verbose. I had to add `-> int` and `a: int, b: int` to make it happy.

## What I learned

Untyped functions are essentially "don't check me" zones. The `--strict` flag forces explicit types everywhere. I need to either add real annotations or use `--ignore-missing-imports` for libraries without stubs.