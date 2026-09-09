---
last_verified: 2026-09-09
tool_version: n/a
sources: []
---

# 2026-09-09 — What I learned doing the pyright quickstart

I'd run pyright once before (the `2026-09-05` note), but this time I dug into the parts that actually bite: strict mode, `# type: ignore` comments, and missing-import errors. Here's what surprised me.

## Strict mode is a big jump from default

Default `typeCheckingMode` is `basic`, and it felt lenient — a few obvious errors, nothing dramatic. Switching to `"strict"` on the same file produced about a dozen more diagnostics. Most were around optional handling (`None` checks I'd skipped) and unused imports that basic mode doesn't flag. The lesson: strict is not just "more of the same", it turns on whole categories of checks. I set it in `pyrightconfig.json`:

```json
{
  "typeCheckingMode": "strict"
}
```

and re-ran `uvx pyright src/`. The error count jumped immediately, which is exactly what I wanted — it told me where the untyped gaps were.

## `# type: ignore` is line-scoped, not file-scoped

I assumed a `# type: ignore` at the top of a file would quiet everything below it. It doesn't — it only suppresses the diagnostic on that one line. If I need to silence a block, pyright wants a named ignore with a code, like `# type: ignore[reportUnusedImport]`, which makes the suppression auditable. Blanket `# type: ignore` still works but should be a red flag that something needs real fixing.

## Missing imports are warnings, not errors, by default

When pyright can't find a third-party package's type stubs, it reports `reportMissingImports` as a *warning* unless you set it to `"error"`. That means a broken import can sail through a strict run if the package simply has no stubs. I set `"reportMissingImports": "error"` in config so a missing `py.typed` or absent stub fails the check instead of getting buried in the warnings count. For packages I know are fine (pandas, numpy), I can also pin them in `typeCheckingMode` overrides per-module.

## What I'd try next

I want to run `pyright --verifytypes <package>` to see how complete a library's type coverage actually is, and compare strict-vs-basic output on a real mixed-typed module. After that, wiring pyright into pre-commit alongside mypy so I can see the error deltas side by side.