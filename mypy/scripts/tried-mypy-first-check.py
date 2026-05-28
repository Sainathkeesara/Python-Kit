"""Intentionally type-broken file to test mypy with.

Run: uv run mypy tried-mypy-first-check.py
"""


def add(x: int, y: int) -> int:
    return x + y


result: str = add(1, 2)  # mypy: Incompatible types in assignment

print(add("hello", "world"))  # mypy: Argument 1 to "add" has incompatible type "str"; expected "int"


def process(items: list[int]) -> None:
    for item in items:
        print(item + 1)


process([1, 2, "three"])  # mypy: List item 2 has incompatible type "str"; expected "int"


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


p = Person("Alice")
print(p.name * 2)  # fine
print(p.age)       # mypy: "Person" has no attribute "age"
