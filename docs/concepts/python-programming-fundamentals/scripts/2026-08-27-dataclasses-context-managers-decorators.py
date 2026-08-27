# last_verified: 2026-08-27 · n/a

"""
I wrote this script to practice dataclasses, context managers, and decorators
—all three show up constantly in real Python code, and I kept mixing up the
syntax for each. Putting them in one file helped me see the patterns.

Covers:
- @dataclass basics, field defaults, and __post_init__
- contextlib.contextmanager for a simple file-lock pattern
- A timing decorator that wraps any function with elapsed-time logging
"""

import time
import functools
from dataclasses import dataclass, field
from contextlib import contextmanager
from typing import Callable, Any


# --- Dataclasses ---

@dataclass
class Player:
    """A game player with a score that can't go below zero."""
    name: str
    score: int = 0
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        # __post_init__ runs after the auto-generated __init__.
        # Good place for validation — I kept forgetting this exists
        # and writing custom __init__ methods instead.
        if self.score < 0:
            raise ValueError(f"Score can't be negative: {self.score}")

    def add_points(self, points: int) -> None:
        self.score = max(0, self.score + points)


# The research notes flagged: using `is` for value comparison instead of `==`.
# dataclass equality is auto-generated with ==, so this just works:
alice = Player("Alice", 100, tags=["vip"])
bob = Player("Bob")
print(f"alice == Player('Alice', 100): {alice == Player('Alice', 100)}")  # True


# --- Context managers ---

@contextmanager
def timer(label: str = "block"):
    """Measure wall-clock time for a code block.

    Usage:
        with timer("my loop"):
            do_work()
    """
    start = time.perf_counter()
    try:
        yield  # control passes to the 'with' body here
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] elapsed: {elapsed:.4f}s")


# A more practical example — temporary file-like object
@contextmanager
def managed_resource(name: str):
    """Simulate acquiring and releasing a resource (file, connection, lock)."""
    print(f"Acquiring {name}")
    resource = {"name": name, "open": True}
    try:
        yield resource
    finally:
        resource["open"] = False
        print(f"Releasing {name}")


# --- Decorators ---

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Wrap a function with elapsed-time logging.

    functools.wraps preserves the original function's __name__ and __doc__.
    I kept forgetting this and breaking help() and traceback readability.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 0.1):
    """Retry a function on exception — a decorator factory.

    The outer function returns the actual decorator. This two-layer
    pattern confused me at first — you need the extra function call
    to pass configuration to the decorator.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exc: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt < max_attempts:
                        print(f"  retry {attempt}/{max_attempts} after {delay}s...")
                        time.sleep(delay)
            raise last_exc  # type: ignore[misc]
        return wrapper
    return decorator


# --- Putting it all together ---

@timer_decorator
def slow_add(a: int, b: int) -> int:
    """A deliberately slow function to demonstrate the timer decorator."""
    time.sleep(0.05)
    return a + b


@retry(max_attempts=2, delay=0.05)
def might_fail() -> str:
    """Fails on first call, succeeds on second — demonstrates retry decorator."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("simulated network blip")
    return "success"


if __name__ == "__main__":
    # Dataclass in action
    p = Player("Charlie", 50)
    p.add_points(25)
    print(f"{p.name} score: {p.score}")  # 75

    # Context manager with the timer
    with timer("sum comprehension"):
        total = sum(i * i for i in range(10_000))
    print(f"Sum of squares: {total}")

    # Managed resource — acquire and release are printed
    with managed_resource("database-conn") as res:
        print(f"Using {res['name']} (open={res['open']})")

    # Decorated function
    result = slow_add(3, 4)
    print(f"slow_add(3, 4) = {result}")

    # Retry decorator
    try:
        msg = might_fail()
        print(f"might_finally: {msg}")
    except ConnectionError:
        print("All retries exhausted")
