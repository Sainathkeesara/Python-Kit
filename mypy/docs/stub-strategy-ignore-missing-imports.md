---
last_verified: 2026-08-16
tool_version: "2.3.1"
sources:
  - https://mypy.readthedocs.io/en/stable/common_issues.html
---

# Typing third-party dependencies: stubs vs. the `--ignore-missing-imports` trap

> L3 notes — building a project that imports third-party packages while keeping mypy useful on them.

## Purpose

The moment a project imports a package that ships no type information, mypy has three options: report a missing-import error, require a stub, or treat the module as `Any`. Reaching for `--ignore-missing-imports` feels like the fast fix, but it quietly disables checking for everything that touches that package. This doc captures a stub strategy for third-party deps and why the global ignore is the trap it is.

## The trap: `--ignore-missing-imports` and Any-poisoning

mypy's common-issues docs call this out directly: if a value's type is `Any` — from an unannotated parameter, a missing `__init__` annotation leaking into instance variables, `--ignore-missing-imports`, or a `# type: ignore` — mypy silently skips type errors that touch it. So the flow goes:

1. Import a dep with no types → mypy reports it found no implementation or library stub for the module.
2. Add `--ignore-missing-imports` → the error disappears, but the module is now `Any`.
3. Every call that passes through that module is unchecked. A wrong attribute access or a bad argument one hop downstream still passes, because the value was poisoned upstream.

That's the trap: the flag removes a visible error and opens a silent hole. It is the same mechanism as an unannotated function. The docs use `def foo(a): return '(' + a.split() + ')'` as the example — it produces no error even though `a.split()` is "obviously" a list, because the function body is never type-checked without `--check-untyped-defs`. Same poison, different door.

## Stub strategy for third-party deps

Instead of a project-wide ignore, give mypy real type information for the module:

1. **Prefer packages that ship types.** If the dep bundles its own stub files or inline annotations, imports resolve on their own and no flag is needed.
2. **Add the community stub package.** Many popular untyped libraries have separately-maintained stub packages that declare the types without reimplementing the code. Install the matching one and imports resolve.
3. **Write a minimal local stub.** If neither exists, a small `<dep>.pyi` declaring only the signatures the project actually calls is enough to un-poison the import. It doesn't need to cover the whole library.
4. **Scope the exemption, don't globalize it.** If a dep genuinely has no types and no stub, keep the gap narrow — a per-module override (`[[tool.mypy.overrides]]` with `ignore_missing_imports = true` for just that module) rather than a project-wide `--ignore-missing-imports` that Any-poisons everything.

For debugging, drop `reveal_type(x)` or `reveal_locals()` into the code to see whether a value is `Any` or a real type — then remove them before running the code, since they don't exist at runtime.

## Verify

- Run mypy with and without `--ignore-missing-imports` on a module that imports an untyped dep, and confirm which imports flip to `Any`.
- Use `reveal_type()` on the import after adding a stub to confirm it resolves to a real type instead of `Any`.
- When you do use `# type: ignore`, scope it to the error code (`# type: ignore[<code>]`) and remember the placement rule: the ignore comment must be at the start of the line's comment section to actually suppress the error.

## References

- mypy common issues: https://mypy.readthedocs.io/en/stable/common_issues.html
