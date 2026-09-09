---
last_verified: 2026-09-09
tool_version: n/a
sources: []
---

# Security Best Practices meets Static Type Checking

> Combining secret detection with strict type checking so that a single CI run catches both "is this safe?" and "does this actually work?".

## Purpose

Security best practices and static type checking look like different concerns — one is about trust, the other about correctness — but they share a common shape: scan the code without running it, report findings before they reach production, and fail the build when the threshold is crossed. This note documents the pattern of running bandit (security) and mypy strict (types) in one pipeline, and explains why the combination catches more than either tool alone.

## When to use

- You are setting up CI for a Python project and already use mypy for type safety.
- You want secret detection and dependency scanning without adding a second pipeline.
- Your team has accepted that strict typing is a prerequisite for reading security findings with confidence.

## Prerequisites

- A Python project with a `pyproject.toml` containing a `[tool.mypy]` table with `strict = true`.
- `bandit` and `mypy` installed in the CI environment.
- A baseline of known findings so that pre-existing issues do not block every run.

## Steps

1. **Run bandit first.** Security findings are cheap to surface and often reveal real problems (hardcoded secrets, `eval()`, shell injection). Use `bandit -r src -f json -lll` for a high-severity-only gate.

2. **Run mypy strict second.** Type errors are slower to surface but catch a different class of bug — wrong argument types, missing returns, incompatible assignments. Strict mode enables every diagnostic, so expect a large initial error count.

3. **Aggregate exit codes.** Both tools exit non-zero on findings. Combine them so the pipeline fails if either tool reports issues. Do not mask one tool's failure with the other's exit code.

4. **Publish both reports.** JSON output from bandit and text output from mypy give reviewers something concrete to act on. Upload them as CI artifacts.

5. **Baseline and iterate.** Record the current state as a baseline, fix the highest-severity findings first, then tighten the gate over successive PRs.

## Example

```yaml
# .github/workflows/security.yml (conceptual)
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install bandit mypy
      - name: Security scan
        run: bandit -r src -f json -lll
      - name: Type check
        run: mypy src
```

The two steps run sequentially, and the job fails if either command exits non-zero. A single PR can therefore carry both a new security finding and a new type error, and both block merging.

## Verify

- `bandit -r src -f json -lll` exits 0 (or reports only baselined findings).
- `mypy src` exits 0.
- Removing a `# type: ignore` comment that suppresses a real error causes the type check to fail again — confirming the gate is live.
- Introducing a hardcoded secret in a sample file causes the security scan to fail — confirming that gate is live too.

## Common errors

- **Mypy ignores `pyproject.toml`.** Older mypy versions read `mypy.ini` or `setup.cfg` exclusively. Upgrade to a version that supports `[tool.mypy]`.
- **Bandit reports false positives in tests.** `assert` statements (B101) and non-security hash uses (B303) are common in test code. Exclude `tests/` or add per-file ignores.
- **Strict mode is noisy at first.** Expect hundreds of errors on an untyped codebase. Fix them in batches by module rather than trying to silence them all at once.

## How this connects to what's next

Once the combined gate is stable, the next step is wiring it into pre-commit so findings appear locally before the PR is opened. After that, dependency scanning with `pip-audit` completes the triangle: source security (bandit), type correctness (mypy), and dependency hygiene (pip-audit).