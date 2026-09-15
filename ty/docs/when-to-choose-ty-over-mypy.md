---
last_verified: 2026-09-15
tool_version: n/a
sources: []
---

# When to choose ty over mypy: speed, error messages, and type-narrowing behavior

## Purpose

Both `ty` and `mypy` type-check Python code, but they differ in speed, diagnostic style, and how far they push type inference. Choosing between them depends on how large the codebase is, how quickly the team needs feedback, and how much type-narrowing control is needed.

This comparison covers three dimensions: raw speed, error message readability, and type-narrowing behavior.

## Speed

`ty` is designed to be faster than `mypy` on large codebases. It uses a compiled core and caches aggressively, often completing checks in a fraction of the time `mypy` needs for the same module set. For small projects (a few files), the difference is negligible. For projects with hundreds of modules, `ty`'s incremental checking and parallel analysis tend to produce noticeably shorter round-trip times.

`mypy` can narrow the gap with incremental mode enabled and tuned settings; strict mode adds overhead. In practice, `mypy` scales less gracefully on large codebases without careful config tuning.

When to pick which:
- **ty** — when fast iteration matters (e.g., pre-commit hooks, IDE integration on a large codebase).
- **mypy** — when maximum compatibility with the broader Python ecosystem matters and the codebase is small-to-medium.

## Error messages

`ty` tends to produce more concise diagnostics. It surfaces the most likely error first and avoids some of the cascading noise that `mypy` can produce when a single annotation gap triggers a cascade of inference failures. Messages like "argument missing" or "incompatible type in assignment" are stated plainly.

`mypy` messages are thorough but sometimes verbose, especially in strict mode where union types and overloads generate multiple lines of context. The detail can be valuable for complex generics, but it slows triage on simpler issues.

This is one area where the choice may depend on team preference. Teams that want actionable output on first read may lean `ty`; teams that want exhaustive diagnostic context for subtle generics issues may lean `mypy`.

## Type-narrowing behavior

`ty` and `mypy` both narrow types within control-flow branches (e.g., `if isinstance(x, str)`), but they handle some edge cases differently:

- **Assertion narrowing** — both support narrowing from `assert` statements, but `ty` is more permissive about what it accepts as a valid narrowing check. `mypy` is stricter about what `assert` expressions it trusts for narrowing.
- **`match`/`case` narrowing** — both narrow within `match` arms, but the interaction with exhaustiveness checking differs. `mypy` provides explicit exhaustiveness errors on `match`; `ty` does not yet match that level of exhaustiveness feedback.
- **Assignment-based narrowing** — `ty` sometimes infers narrower types from re-assignment patterns that `mypy` leaves broad. This can surface bugs earlier but may also surprise developers who expect broader types in certain rebound scenarios.

Neither approach is universally better; teams working heavily with `match` statements may find `mypy`'s exhaustiveness checks more useful, while teams who rely on assertion-heavy defensive code may prefer `ty`'s permissiveness.

## When to use which

| Scenario | Recommended |
|---|---|
| Large codebase, fast iteration needed | `ty` |
| Complex generics, overloads, and typing edge cases | `mypy` |
| Pre-commit hook with quick feedback | `ty` |
| Exhaustive `match`/`case` checking | `mypy` |
| New project with no existing mypy config | Either; start with `ty` for speed, migrate if needed |

## Verify

To verify the comparison yourself, run both type checkers on the same file with equivalent strictness settings and compare wall-clock time and diagnostic output:

```bash
# Check a module with ty
ty check path/to/module.py

# Check the same module with mypy
mypy path/to/module.py
```

If results differ, the divergence usually lies in how each tool interprets ambiguous inference points rather than in genuine type errors.
