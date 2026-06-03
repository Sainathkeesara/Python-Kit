# Tried the Ruff quickstart — lint, auto-fix, explore rules

I followed the official Ruff quickstart to get a feel for how Ruff works day-to-day. I already had Ruff installed from earlier, so I jumped straight into linting.

## Linting a file

I wrote a deliberately messy Python file with unused imports, long lines, and bad naming:

```python
import os, sys
from pathlib import Path

MY_CONSTANT_value = 42

def f(x):
    return x * 2
```

Ran `ruff check messy.py`. It flagged the unused `os` import, the `Path` import (also unused), the non-uppercase constant name, and the short function name `f`. Output was clear — each issue had a rule code like `F401`, `N815`, `N802`.

I liked that Ruff didn't need a config file to start — sensible defaults picked up the common issues immediately.

## Auto-fixing

`ruff check --fix messy.py` removed the unused imports automatically. The `N` naming violations stayed because Ruff won't auto-fix those — they need manual renaming. The output showed what was fixed and what remained.

I checked the file after the fix — the `import os` and `from pathlib import Path` lines were gone. No side effects.

## Exploring rules

I used `ruff rule E501` to read the docs for the line-too-long rule, and `ruff rule F401` for unused import. The terminal output is concise — rule code, what it catches, and an example.

Ran `ruff check --show-settings` to see what Ruff resolved from defaults. It showed target version `py311` and no explicit `select` or `ignore`, meaning it uses the recommended rule set.

## What tripped me up

- I expected `--fix` to fix everything, including naming violations. Ruff intentionally doesn't auto-fix `N` rules because renaming is a semantic change. Makes sense but got me at first.
- Running `ruff check .` in a project with a `.venv/` flagged files in `.venv/`. Had to add `exclude = [".venv"]` in `pyproject.toml` to skip them. The quickstart doesn't mention this.
- The difference between `ruff check` and `ruff format` wasn't obvious. `check` is lint (find bugs, style issues), `format` is auto-formatter (like Black). I was using `format` thinking it would lint.

## What I'd try next

I want to set up a proper `pyproject.toml` with Ruff config — pick a rule set, add ignores for things I disagree with, and wire it into a pre-commit hook so I don't forget to lint before committing.
