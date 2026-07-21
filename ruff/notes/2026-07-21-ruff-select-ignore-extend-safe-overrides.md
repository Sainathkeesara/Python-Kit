---
last_verified: 2026-07-21
tool_version: n/a
sources: []
---

# What I learned about Ruff's select, ignore, extend-safe, and per-directory overrides

I went through the Ruff rule configuration docs and tried each concept on a small project. Here's what stuck and what confused me.

## select and ignore — not a toggle, it's a filter

I expected `select = ["E"]` plus `ignore = ["E501"]` to mean "enable all E rules, then turn off E501." That's mostly right, but `select` defines the *complete* set of rules that run — `ignore` only removes rules from within that set. If I set `select = ["F"]`, no E rules run at all, even if they're not ignored. I tripped on this when adding `"E501"` to `ignore` and wondering why other E rules still fired — they were never in the selected set to begin with.

## extend-safe — opt into safe fixes only

I ran `ruff check --fix` on a file with some naming issues and was surprised when Ruff renamed a variable. That's an unsafe fix — it can break code. The `extend-safe` key tells Ruff to only apply fixes that are guaranteed safe:

```toml
[tool.ruff.lint]
extend-safe = ["E", "F", "W"]
```

With `extend-safe`, Ruff skips the rename-style fixes and only applies things like removing unused imports or fixing whitespace. I like this for CI where I want auto-fixes but not surprises. The `--unsafe-fixes` flag overrides it locally if I want to review changes first.

## Per-directory overrides — different rules for different folders

My project has `src/` (production code) and `tests/` (test files). I want stricter naming rules in `src/` but more lenient ones in `tests/`. Per-directory overrides let me do that:

```toml
[tool.ruff.lint.per-file-ignores]
"src/**" = []
"tests/**" = ["N801", "N802", "N803"]
```

The pattern syntax is glob-like. I used `"tests/**"` to cover every test file. I initially tried `"tests/*"` which only matched files directly inside `tests/`, not subdirectories. Took a few tries to get the right pattern.

## The order that actually worked for me

I set up my `ruff.toml` in this order:

1. `select` for the base rule set I want
2. `extend-safe` for the auto-fix subset
3. `ignore` for anything noisy that I'll clean up later
4. Per-file-ignores for exceptions

Running `ruff check . --statistics` after each change helped me see what was actually enabled before moving on.

## What I'd do differently

Use `--diff` before committing config changes so I can see exactly which rules are newly active. And add rules incrementally — starting with `["E", "F"]` and expanding once I've addressed the current batch.
