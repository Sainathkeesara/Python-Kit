# last_verified: 2026-07-27 · Static Type Checking n/a

import sys
from typing import TypedDict


class UserProfile(TypedDict):
    """I started with TypedDict because it lets me declare the exact keys
    a dictionary should have, which is clearer than a plain dict annotation."""

    username: str
    email: str
    active: bool


def load_user(data: dict[str, object]) -> UserProfile:
    """Validate and coerce raw input into a typed UserProfile.

    I raise ValueError early if required keys are missing or the types
    don't match, so the caller gets a single clear error instead of
    an AttributeError later.
    """
    required = {"username": str, "email": str, "active": bool}
    for key, expected in required.items():
        value = data.get(key)
        if not isinstance(value, expected):
            raise ValueError(f"{key} must be {expected.__name__}, got {type(value).__name__}")
    return UserProfile(
        username=data["username"],
        email=data["email"],
        active=data["active"],
    )


def filter_active(users: list[UserProfile]) -> list[UserProfile]:
    """Return only active users. The list[UserProfile] annotation means
    mypy will catch me if I accidentally return a list of plain dicts."""
    return [u for u in users if u["active"]]


def format_username(user: UserProfile) -> str:
    """Simple formatter with an explicit return type."""
    return user["username"].lower().strip()


def main() -> None:
    raw_users = [
        {"username": " Alice ", "email": "alice@example.com", "active": True},
        {"username": "Bob", "email": "bob@example.com", "active": False},
        {"username": "Carol", "email": "carol@example.com", "active": True},
    ]

    typed_users: list[UserProfile] = []
    for raw in raw_users:
        try:
            typed_users.append(load_user(raw))
        except ValueError as exc:
            print(f"Skipping bad user: {exc}", file=sys.stderr)

    active_users = filter_active(typed_users)
    for user in active_users:
        print(format_username(user))


if __name__ == "__main__":
    main()
