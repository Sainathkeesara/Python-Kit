# Ty — quick primer

> First-day notes for someone who's never used Ty. Personal voice, plain language.

## What is it?

I just learned about Ty. It's another Python type checker — but written in Rust by the Astral team (the same people who made Ruff and uv). From what I can tell, it's their answer to mypy: same job (check your type annotations), but built for speed from the ground up. The idea is that instead of waiting seconds for mypy on a medium-sized project, Ty should feel instant. It uses the same PEP 484 annotations mypy uses, so code I already typed should Just Work.

## What does it do?

I point it at a Python file or a directory and it scans everything, follows imports, and tells me where my function calls or assignments don't match the type annotations I wrote. If I mark a parameter as `int` and pass a `str`, it catches it and shows me the exact line and character. It also tries to figure out types even when I leave annotations off — so I can run it on a partially-typed project and still get useful warnings.

## Why does it exist?

Type-checking big Python projects is slow with mypy, especially in CI. The Astral team saw an opening: if Ruff could make linting fast, why not do the same for type checking? Ty exists so I can run type checks on every save or every commit without it becoming a bottleneck. It's also meant to play nice with Ruff and uv — the idea is a unified Rust toolchain for Python that handles linting, formatting, package management, and now type checking, all on the same runtime.

## Key terminology

- **Type annotation** — The `: int` or `-> str` syntax that tells Python (and Ty) what type something should be. Example: `def greet(name: str) -> str: return f"Hello {name}"`.
- **Type inference** — Ty figuring out types even when I don't write them. Example: `x = 42` means `x` is `int` without me saying so.
- **Gradual typing** — I can add types to one function and leave the rest untyped. Ty checks what it can and skips the rest. Example: I typed my API layer but not my tests yet.
- **`--strict`** — Turns on every check Ty has: no implicit `Any`, no untyped decorators, no missing return types. Example: `ty --strict src/`.
- **PEP 484** — The spec that defines Python's type annotation syntax. Example: `Optional[str]`, `List[int]`, `Union[str, int]`.
- **`Any`** — The "trust me" type that tells Ty to skip checking. Example: `x: Any = some_dynamic_value()`.
- **Type stub** — A `.pyi` file that adds type info for libraries that don't ship their own. Example: `types-requests` adds type hints for the requests library.

## A tiny example

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))       # OK
print(add("hi", 5))    # type error: Argument 1 has incompatible type "str"; expected "int"
```

I save this as `test.py` and run `ty test.py`. Ty prints the error on the second call with the exact line and column. No config file needed for this.

## What I'll cover next

I want to try running Ty on an actual project I have with real dependencies, see how many errors pop up in `--strict` mode, and compare the speed against mypy on the same codebase. After that I'll look into setting it up in a pre-commit hook so every commit gets type-checked automatically.
