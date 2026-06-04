# Ruff vs Flake8 — what I learned comparing them

I've been using Ruff as my linter, but most of the Python community came up on Flake8. I wanted to understand how they actually compare — not just "Ruff is faster" but what you gain and lose when switching.

## Rule coverage

Flake8 is really a plugin system. The core (`pycodestyle` + `pyflakes`) checks about ~50 rules for style (E, W) and logic errors (F). Everything else comes from plugins — `flake8-bugbear` (B), `flake8-simplify` (SIM), `flake8-comprehensions` (C4), `pep8-naming` (N), and dozens more.

Ruff reimplements ~700+ rules out of the box, including nearly all Flake8 core rules and the most popular plugins. Here's the mapping I've found so far:

| Flake8 source | Ruff prefix | Status |
|---|---|---|
| pycodestyle (E, W) | E, W | Full coverage |
| pyflakes (F) | F | Full coverage |
| flake8-builtins (A) | A | Yes |
| flake8-bugbear (B) | B | Yes, plus extra |
| flake8-comprehensions (C4) | C4 | Yes |
| flake8-import-order (I) | I | Yes |
| flake8-simplify (SIM) | SIM | Yes |
| pep8-naming (N) | N | Yes |
| flake8-docstrings (D) | D | Partial — Ruff doesn't re-export pydocstyle entirely |
| pylint (PL) | PL | Partial — subset |
| tryceratops (TRY) | TRY | Yes |
| eradicate (ERA) | ERA | Yes |

What surprised me: Ruff has rules Flake8 plugins don't cover at all — like `RUF` (Ruff-specific rules) for things like useless `if` expressions, `flake8-use-pathlib` equivalents, and even some `pylint` rules ported over.

## Migration gotchas

### 1. Plugin granularity

In Flake8 I'd install `flake8-bugbear` and get all its rules automatically. With Ruff I need to explicitly opt into each rule prefix:

```toml
[tool.ruff]
select = ["B", "SIM", "C4"]
```

It's more explicit but also means I can mix and match at a finer level. I like it, but the first time I forgot to add `SIM` to `select` and wondered why `list()` wasn't flagged.

### 2. No first-party way to run a single "plugin"

With Flake8 you can run `flake8 --select B` to see what bugbear catches. In Ruff, the equivalent is `ruff check --select B` — but Ruff doesn't have a concept of "plugin", just rule prefixes. Once I understood that, configuring it got easier.

### 3. Per-file ignores are different

```ini
# Flake8 — per-file-ignores in setup.cfg
[flake8]
per-file-ignores = __init__.py:F401
```

```toml
# Ruff — per-file-ignores in pyproject.toml
[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]
```

Same idea, different syntax. The TOML version is cleaner in my opinion.

### 4. Auto-fix coverage

This is where Ruff pulls ahead. Flake8 shows you the problem; Ruff fixes many of them automatically with `--fix`. Things like removing unused imports (F401), sorting imports (I), and converting old-style set literals (C4) all auto-fix without extra plugins.

## What I'd try next

I want to run both on the same codebase side by side and compare the full output lists. I also want to try Ruff's `--preview` mode — it enables rules that aren't stable yet, which is something Flake8 doesn't really have an equivalent for. And I should check if any Flake8-only plugins I might need (like `flake8-print` or `flake8-todos`) have Ruff equivalents or if I'd need to keep Flake8 around for those.
