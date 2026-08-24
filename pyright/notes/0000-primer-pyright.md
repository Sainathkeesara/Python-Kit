---
last_verified: 2026-08-24
tool_version: n/a
sources: []
---

# Pyright — quick primer

> First-day notes for someone who's never used Pyright. Personal voice, plain language.

## What is it?

Started looking into Pyright today — it's a static type checker for Python, made by Microsoft. If you've used mypy, Pyright does the same job but is written in TypeScript and apparently runs faster on big codebases. It lives in the VS Code / Pylance world but works fine from the CLI too. The main difference from mypy is it uses its own config file (`pyrightconfig.json`) and doesn't have the same plugin ecosystem.

## What does it do?

You point it at your Python files and it follows the type hints, reporting errors where things don't match — wrong argument types, missing returns, incompatible assignments. In VS Code through Pylance it also gives you quick-fix suggestions and autocomplete. From the CLI it's just a checker, no editor integration.

## Why does it exist?

Type hints are useless if nobody checks them. Before Pyright (or mypy), you'd write `def greet(name: str) -> str:` and hope nobody passes an int. Pyright catches that at edit time — no CI run, no runtime `TypeError`. And since VS Code ships Pylance (which is Pyright under the hood), a lot of teams are already running it without realizing it.

## Key terminology

- **`pyrightconfig.json`** — config file in your project root. Controls Python version, include/exclude paths, strictness. Example: `{"typeCheckingMode": "strict"}`.
- **Diagnostics** — the errors and warnings Pyright reports. Each has a file, line, column, and a message like `"Argument of type \"str\" cannot be assigned to parameter of type \"int\""`.
- **Type stubs (`.pyi`)** — skeleton files describing types for third-party libs that don't ship their own annotations. Pyright auto-downloads these for popular packages.
- **`reportMissingImports`** — setting to `"warning"` or `"none"` to suppress errors from imports Pyright can't resolve. Handy for optional deps.
- **`typeCheckingMode`** — `"off"`, `"basic"`, or `"strict"`. Strict enables every diagnostic; basic is a sensible starting point.
- **Pylance** — the VS Code extension wrapping Pyright. Gives type checking, autocomplete, go-to-definition in the editor.

## A tiny example

```python
# example.py — run `pyright example.py` to check it
def greet(name: str) -> str:
    return f"Hello, {name}!"

# This is fine
result = greet("world")

# Pyright catches this: Argument of type "int" cannot be assigned to parameter of type "str"
# bad = greet(42)
```

Running `pyright example.py` prints something like:

```
No pyproject.toml or pyrightconfig.json found; using default settings.
0 errors, 0 warnings, 0 notes
```

Uncomment the `bad = greet(42)` line and Pyright yells before you ever run the script.

## What I'll cover next

Want to try running Pyright on an actual project with mixed typed/untyped code — see how `--verifytypes` works, experiment with `pyrightconfig.json` strictness levels, and compare the output to what mypy gives on the same files.
