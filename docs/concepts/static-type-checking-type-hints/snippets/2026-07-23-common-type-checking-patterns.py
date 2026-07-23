# last_verified: 2026-07-23 · Static Type Checking n/a

from typing import Optional, Union


def greet(name: str) -> str:
    """A basic typed function — return type is explicit."""
    return f"Hi, {name}"


def find_user(user_id: int) -> dict[str, str]:
    """Return a dict; when the value might be missing, use get with a default."""
    users = {1: "Alice", 2: "Bob"}
    return {"name": users.get(user_id, "Unknown")}


def process_items(items: list[str]) -> dict[str, int]:
    """Map a list of strings to their lengths."""
    return {item: len(item) for item in items}


# I use Optional when a value can be None.
maybe_name: Optional[str] = None
if maybe_name is None:
    print("Name is missing")

# Union is for values that could be one of several types.
score: Union[int, float] = 95
