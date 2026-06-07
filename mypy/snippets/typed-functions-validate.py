"""Small typed module to validate with mypy.

Run: uv run mypy typed-functions-validate.py
"""


def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y


def greet(name: str, excited: bool = False) -> str:
    """Return a greeting message."""
    msg = f"Hello, {name}!"
    return msg + " 🎉" if excited else msg


def process_items(items: list[str]) -> int:
    """Return count of items longer than 3 chars."""
    return sum(1 for item in items if len(item) > 3)


# Valid calls
result = add(1, 2)
message = greet("Alice", excited=True)
count = process_items(["cat", "dog", "elephant"])

# This file should pass mypy without errors