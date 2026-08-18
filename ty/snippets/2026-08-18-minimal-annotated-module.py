# last_verified: 2026-08-18 · ty n/a
"""Minimal annotated module — ty found three issues, then I fixed them."""

# Ty complained: missing parameter annotation
# Fix: add `: str`
def greet(name) -> str:
    return f"Hello, {name}"


# Ty complained: incompatible type in assignment (str -> int)
# Fix: initialize with the correct type
count: int = 0


# Ty complained: return type mismatch
# Fix: annotate `b` as `int` and return `int`
def add(a: int, b: int) -> int:
    return a + b


result: int = add(1, 2)
