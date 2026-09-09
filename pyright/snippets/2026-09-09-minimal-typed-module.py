# last_verified: 2026-09-09 · pyright n/a

# Minimal typed module for pyright exploration.
# Run: pyright this_file.py
# Expected diagnostics: reportMissingImports, reportOptionalMemberAccess


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def get_first(items: list[str]) -> str | None:
    """pyright flags .upper() below as reportOptionalMemberAccess."""
    if items:
        return items[0]
    return None


result = get_first(["a", "b"])
# print(result.upper())  # uncomment to see pyright diagnostic
