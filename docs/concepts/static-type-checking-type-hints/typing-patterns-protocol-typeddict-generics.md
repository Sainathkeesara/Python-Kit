---
last_verified: 2026-08-13
tool_version: n/a
sources:
  - https://mypy.readthedocs.io/en/stable/getting_started.html
  - https://mypy.readthedocs.io/en/stable/common_issues.html
  - https://betterstack.com/community/guides/scaling-python/mypy-explained/
  - https://pre-commit.com/
  - https://technoscripts.com/python-code-quality-ruff-mypy/
---

# Type-checking patterns in real projects: Protocol, TypedDict, and generics

## Purpose

This doc covers the three patterns that show up once a codebase moves beyond basic `str`, `int`, and `list[str]` annotations: Protocol for structural subtyping, TypedDict for fixed-shape dictionaries, and generics for preserving element types. The goal is a small set of patterns that cover the majority of "real project" type-checking needs. The docs suggest starting with Protocol when you need duck typing without a shared base class, and adding TypedDict and generics as the codebase grows.

## Steps

### Protocol: duck typing without a shared base class

```python
from typing import Protocol


class Readable(Protocol):
    def read(self) -> str: ...


def consume(source: Readable) -> str:
    return source.read()
```

Any object with a `read() -> str` method satisfies `Readable` — a file, a `StringIO`, or a test double. The type checker validates the structure, so the consumer can be tested against a stub without a real file. The `...` bodies mean the Protocol only declares the shape; it does not implement behavior.

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

`Stack[int]` and `Stack[str]` are distinct types, and `pop()` returns the declared element type instead of `Any`. The `TypeVar` binds at the call site; the pattern composes with Protocol — `T` can be bounded to a Protocol, for example `TypeVar("T", bound=Readable)`.

### Combining the three patterns

The patterns integrate in a typed pipeline. A function can take a `Readable` (Protocol), parse it into a `BuildConfig` (TypedDict), and hand it to a generic processor:

```python
def load_config(source: Readable) -> BuildConfig:
    raw = source.read()
    return {"python_version": "3.10", "deps": ["uv", "mypy"]}


def run(processor: Stack[BuildConfig], config: BuildConfig) -> None:
    processor.push(config)
```

Each layer keeps its own guarantee: structural flexibility in, fixed dict shape in the middle, element-type preservation on the way out.

## How this connects to testing, packaging, and CI

One way to think about these patterns is as the type-checking layer that sits between writing code and running tests. The docs suggest a few integration points:

- **Testing.** A Protocol lets you pass a lightweight test double to a consumer without a real file or network call. mypy then validates that the double matches the expected shape before pytest ever runs. Running mypy first in a pre-commit hook means type errors fail fast, and the pytest suite only sees code that already passes the type gate. [source: https://technoscripts.com/python-code-quality-ruff-mypy/]
- **Packaging.** A typed package declares its public API in `pyproject.toml` under `[tool.mypy]`. Downstream consumers get inline types automatically, which removes the need for separate stub packages. This is one place where packaging metadata and type checking overlap — the project config is the contract both humans and tools read. [source: https://betterstack.com/community/guides/scaling-python/mypy-explained/]
- **CI.** The same mypy config committed to the repo runs in CI as a required status check. If the config pins `disallow_untyped_defs = True`, a PR that adds an untyped function fails the build before merge. This mirrors how tests and linting work: define the rule in config, run it in CI, and the gate is consistent across every checkout. [source: https://pre-commit.com/]

The combination is not automatic — each tool does one thing — but when the same config drives local pre-commit hooks and CI checks, the type layer becomes part of the commit workflow rather than an afterthought.

## Verify

Run mypy on the module:

```bash
mypy --strict module.py
```

`--strict` turns on checks like `disallow_untyped_defs`, so a Protocol whose methods are missing annotations is caught rather than silently accepted. While developing, `reveal_type(some_expression)` prints the inferred type of any expression in the mypy output — useful to confirm a `TypeVar` bound resolved to the type expected.

## Common errors

- **Protocol methods without `...`.** A Protocol whose methods raise `NotImplementedError` instead of using `...` is not purely structural and can be flagged as abstract at runtime. One common cause is copying a real class body into a Protocol without replacing the implementation with `...`.
- **`dict[str, Any]` instead of TypedDict.** Any key/type mistake slips through; `Any` defeats checking at the point it appears. This is the main error when migrating a small module: the dict was convenient until a typo in a key name produced a runtime `KeyError` that mypy could have caught.
- **A `TypeVar` used once.** A `TypeVar` that appears in only one position gives the checker nothing to bind, and the inferred type degenerates toward `Any`. This happens when a single-method generic class forgets that the TypeVar needs a second occurrence to stay meaningful.

## References

- https://mypy.readthedocs.io/en/stable/getting_started.html
- https://mypy.readthedocs.io/en/stable/common_issues.html
- https://betterstack.com/community/guides/scaling-python/mypy-explained/
- https://pre-commit.com/
- https://technoscripts.com/python-code-quality-ruff-mypy/
