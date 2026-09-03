---
last_verified: 2026-09-03
tool_version: 0.16.5
sources:
  - https://pynions.com/ruff-python
  - https://docs.astral.sh/ruff/linter/
---

# Selecting a Ruff Ruleset and When to Use Per-File Ignores

## Purpose

Choosing which Ruff rules to enable — and which to skip per file — is the single biggest lever on how noisy or useful your lint output is. This guide walks through the tiered ruleset strategy, the role of preview rules, and the per-file-ignore patterns that keep test suites and `__init__.py` files clean.

## When to Use

Apply this when:

- Setting up Ruff on a new project and deciding which rules to enable.
- Migrating from Flake8 and wondering which rule prefixes map to what you already had.
- Your test suite is full of false positives from `S101` (assert) or `F401` (unused imports in `__init__.py`).
- You want to adopt preview rules without destabilising CI.

## Prerequisites

- Ruff installed (`uv add --dev ruff` or `pip install ruff`).
- A `pyproject.toml` or `ruff.toml` where you can add `[tool.ruff.lint]` settings.

## The Tiered Ruleset Strategy

Ruff groups rules by prefix. Rather than enabling everything at once, a tiered approach lets you graduate rules as your codebase matures.

| Tier | Prefixes | What It Catches |
|------|----------|-----------------|
| 1 — Baseline | `E`, `W`, `F`, `I` | PEP 8 style, Pyflakes logic errors, import sorting |
| 2 — Quality | `B`, `UP`, `C4`, `SIM` | Bug patterns, pyupgrade modernisation, comprehension simplification |
| 3 — Discipline | `S`, `PL`, `TCH` | Security (bandit-ported), pylint subset, type-checking imports |

**Recommended starting point:** `select = ["E4", "E7", "E9", "F", "B", "I", "UP"]` — this is the 2026 community baseline that covers the most common issues without drowning in noise. The `E4`/`E7`/`E9` subsets avoid the pedantic `E501` (line length) that most teams disable in favour of the formatter.

### Why not `select = ["ALL"]`?

Enabling all ~700+ rules at once creates hundreds of conflicts and false positives. Ruff's own docs warn that `["ALL"]` "enables hundreds of conflicting rules." Start with Tier 1, graduate to Tier 2, and add Tier 3 only when you have bandwidth to triage.

### `select` vs `extend-select`

Prefer `lint.select` over `lint.extend-select`. An explicit `select` list makes the active ruleset visible at a glance. `extend-select` adds rules silently — which is handy for layering overrides but hides your baseline.

```toml
[tool.ruff.lint]
# Explicit baseline — everyone can see what's on
select = ["E4", "E7", "E9", "F", "B", "I", "UP"]

# Only if you want to layer on top without changing the baseline:
# extend-select = ["SIM", "C4"]
```

## Preview Rules

Ruff marks unstable or experimental rules behind `--preview`. These rules are still being refined and may change behaviour between releases.

```toml
[tool.ruff.lint]
preview = true
```

**When to enable preview:** useful for trying new rules before they stabilise. **When to avoid:** in CI on a shared repo, where a Ruff upgrade could suddenly surface new violations. A common pattern is to enable preview locally for exploration but keep CI on stable rules only.

## Per-File Ignores

Some rules are correct globally but noisy in specific files. Per-file-ignores let you silence them surgically.

### The Two Patterns You'll Need

```toml
[tool.ruff.lint.per-file-ignores]
# Tests use assert freely — S101 (assert) is expected noise
"tests/**" = ["S101"]
"**/test_*.py" = ["S101"]

# __init__.py re-exports — F401 (unused import) is a false positive
"**/__init__.py" = ["F401"]
```

### Why These Two Specifically

- **`S101` in tests:** The `assert` statement is how pytest validates expectations. Bandit's `S101` flags every `assert` as a potential security issue — correct for production code, false positive for tests.
- **`F401` in `__init__.py`:** Package init files intentionally re-export symbols. Ruff sees `from .module import Thing` and flags `Thing` as unused — but it's part of the public API.

### Adding More as Needed

Other common per-file patterns:

- `D100`–`D107` (docstring missing) for test files or scripts.
- `ANN` (missing type annotations) for legacy modules during gradual typing adoption.
- `ERA` (commented-out code) for notebooks or scratch files.

## Verify

After configuring your ruleset:

1. `ruff check .` — confirm no unexpected violations from the new rules.
2. `ruff check --select B .` — test a single prefix in isolation to see what it catches.
3. `ruff format --check .` — confirm the formatter still passes (rules don't affect formatting).

## Common Errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| Hundreds of new violations after upgrade | A new Ruff release added rules to a prefix you already selected | Pin Ruff version in CI; review changelog before upgrading |
| `F401` fires on re-exports in `__init__.py` | Missing per-file-ignores | Add `"**/__init__.py" = ["F401"]` |
| `S101` fires in every test file | No test-specific ignore | Add `"tests/**" = ["S101"]` |
| Rules seem to overlap with mypy | `ANN*` (annotations) duplicates mypy `--strict` | Disable `ANN*` when mypy `--strict` is active |

## References

- Ruff ruleset documentation: https://docs.astral.sh/ruff/linter/
- Ruff configuration guide: https://pynions.com/ruff-python
