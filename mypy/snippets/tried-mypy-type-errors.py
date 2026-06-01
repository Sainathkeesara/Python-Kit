"""I wanted to see what mypy catches when you pass wrong types.

Run: uv run mypy tried-mypy-type-errors.py
"""


def greet(name: str) -> str:
    return "Hello, " + name


# mypy should flag both of these — int and bytes aren't str
result = greet(42)
result2 = greet(b"world")
