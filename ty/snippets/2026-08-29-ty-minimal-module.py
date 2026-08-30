# last_verified: 2026-08-29 · ty
"""Minimal typed module demonstrating ty type checking: function signatures, generics, and reveal_type."""

from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


def first(items: list[str]) -> str:
    return items[0]


def doubled(n: int) -> int:
    return n * 2


# reveal_type tells the type checker to report the inferred type at this point.
# ty will print the type it infers for each variable.
x: int = 42
reveal_type(x)

name: str = "Alice"
reveal_type(name)

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
reveal_type(stack.pop())

nums = [1, 2, 3]
reveal_type(nums)

result = first(["a", "b", "c"])
reveal_type(result)

val = doubled(5)
reveal_type(val)
