# last_verified: 2026-09-08 · pyright n/a

from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


def doubled(n: int) -> int:
    return n * 2


# Intentional type errors — pyright will flag these:
result = doubled("hello")
nums: list[int] = [1, 2, 3]
first_str: str = first(nums)

reveal_type(result)
