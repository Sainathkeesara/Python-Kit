from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str


def get_user_greeting(user: User) -> str:
    return f"Hello, {user.name}!"
