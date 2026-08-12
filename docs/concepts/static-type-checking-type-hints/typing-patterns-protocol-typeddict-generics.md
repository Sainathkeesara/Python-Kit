---
last_verified: 2026-08-12
tool_version: n/a
sources:
  - https://mypy.readthedocs.io/en/stable/getting_started.html
  - https://mypy.readthedocs.io/en/stable/common_issues.html
  - https://betterstack.com/community/guides/scaling-python/mypy-explained/
---

# Type-checking patterns in real projects: Protocol, TypedDict, and generics

## Purpose

The primer covers single annotations — `str`, `int`, `list[str]`. Real projects need more: a function that accepts "anything with a `read()` method", a dict that must have exactly the keys the code expects, and a container class that works for several element types without losing type information. These three patterns — Protocol, TypedDict, and generics — are the ones that actually show up once a codebase is being type-checked.

## When to use

- **Protocol** — when a function only needs a specific behavior (methods/attributes), not a specific class. The caller passes any object that supports the shape; no inheritance required.
- **TypedDict** — when a function takes or returns a dict with a known, fixed shape (a config object, a JSON payload). It replaces the vague `dict[str, Any]`.
- **Generics (`TypeVar` / `Generic`)** — when a class or function should preserve the element type of what it holds or returns, instead of downgrading everything to `Any` or `object`.

## The patterns

### Protocol: duck typing without a shared base class

```python
from typing import Protocol


class Readable(Protocol):
    def read(self) -> str: ...


def consume(source: Readable) -> str:
    return source.read()
```

Any object with a `read() -> str` method satisfies `Readable` — a file, a `StringIO`, a test double. The type checker validates the structure, so the consumer can be tested against a stub without a real file. Note the `...` bodies: a Protocol only declares the shape.

### TypedDict: a dict with a fixed shape

```python
from typing import TypedDict


class BuildConfig(TypedDict):
    python_version: str
    deps: list[str]
```

Constructing a `BuildConfig` with a missing key or a wrong value type is now a type error, not a runtime surprise. This is the main improvement over `dict[str, Any]`, which lets any key in and never flags a typo.

### Generics: preserving the element type

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

`Stack[int]` and `Stack[str]` are distinct types, and `pop()` returns the declared element type instead of `Any`. The `TypeVar` binds at the call site; the pattern composes with Protocol — `T` can be bounded to a Protocol, e.g. `TypeVar("T", bound=Readable)`.

## Combining them

The three patterns integrate in a typed pipeline. A function can take a `Readable` (Protocol), parse it into a `BuildConfig` (TypedDict), and hand it to a generic processor:

```python
def load_config(source: Readable) -> BuildConfig:
    raw = source.read()
    return {"python_version": "3.10", "deps": ["uv", "mypy"]}


def run(processor: Stack[BuildConfig], config: BuildConfig) -> None:
    processor.push(config)
```

Each layer keeps its own guarantee: structural flexibility in, fixed dict shape in the middle, element-type preservation on the way out.

## Verify

Run mypy on the module:

```bash
mypy --strict module.py
```

`--strict` turns on checks like `disallow_untyped_defs`, so a Protocol whose methods are missing annotations is caught rather than silently accepted. While developing, `reveal_type(some_expression)` prints the inferred type of any expression in the mypy output — useful to confirm a `TypeVar` bound resolved to the type expected.

## Common errors

- **Protocol methods without `...`.** A Protocol whose methods raise `NotImplementedError` instead of using `...` is not purely structural and can be flagged as abstract at runtime.
- **`dict[str, Any]` instead of TypedDict.** Any key/type mistake slips through; `Any` defeats checking at the point it appears.
- **A `TypeVar` used once.** A `TypeVar` that appears in only one position gives the checker nothing to bind, and the inferred type degenerates toward `Any`.

## References

- https://mypy.readthedocs.io/en/stable/getting_started.html
- https://mypy.readthedocs.io/en/stable/common_issues.html
- https://betterstack.com/community/guides/scaling-python/mypy-explained/
