# last_verified: 2026-09-15 · ty n/a
"""Minimal typed module demonstrating ty type checking: function signatures, generics, and reveal_type.

I started with untyped functions and added annotations incrementally, then used
reveal_type to confirm what ty infers at each point. Generics show up in the
Stack class so I could see how ty handles TypeVar and Generic together.
"""

from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    """A simple generic stack so I can check how ty infers container types."""

    def __init__(self) -> None:
        # Explicit annotation on the internal list — without this ty infers
        # list[<nothing>] and complains on push.
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


# Function signatures: ty checks that call sites match the declared types.
def first(items: list[str]) -> str:
    return items[0]


def double(n: int) -> int:
    return n * 2


# reveal_type prints what ty infers at that point in the code.
# It only works during type checking — running with plain python fails unless
# we provide a fallback (see below).
x: int = 42
reveal_type(x)

name: str = "Alice"
reveal_type(name)

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
reveal_type(stack.pop())

# ty infers list[int] here because of the literal values on the right side.
nums = [1, 2, 3]
reveal_type(nums)

# Calling an annotated function: ty checks that ["a", "b", "c"] is list[str].
result = first(["a", "b", "c"])
reveal_type(result)

val = double(5)
reveal_type(val)

# Runtime fallback so the script is importable outside ty check.
try:
    reveal_type
except NameError:
    def reveal_type(obj):  # type: ignore[no-redef]
        print(type(obj).__name__, obj)
        return obj
