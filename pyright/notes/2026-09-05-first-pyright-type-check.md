---
last_verified: 2026-09-05
tool_version: n/a
sources: []
---

# 2026-09-05 — Install pyright and run my first type check

I wanted to try pyright after reading it's faster than mypy. Installed it with `uvx pyright` — no config needed out of the box.

Created a minimal file to test:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

reveal_type(greet)
result = greet(42)  # passing int where str expected
```

Ran `uvx pyright greet.py`. The output was immediate — one error on line 5: `Argument of type "int" is not compatible with parameter of type "str"`. Clear, direct, no config needed.

What tripped me up:
- pyright reports errors per-file by default, not per-project. If you want project-wide checking, point it at a directory or create `pyrightconfig.json`.
- The `reveal_type()` call is a debugging tool — it prints the inferred type at analysis time. It's not a runtime function; pyright strips it during analysis.
- pyright's strict mode (`"typeCheckingMode": "strict"` in pyrightconfig.json) enables many more checks than the default. I got 12 errors on a small module that mypy was fine with — mostly around optional handling and unused imports.
- Unlike mypy, pyright does not read `pyproject.toml` for its config by default. You need a `pyrightconfig.json` or CLI flags.

Running `uvx pyright src/` across a whole project felt noticeably faster than mypy on the same codebase. The error messages include the expected vs actual type inline, which makes fixing things quicker.

Next: wire pyright into a pre-commit hook and compare its output side-by-side with mypy on a real file.
