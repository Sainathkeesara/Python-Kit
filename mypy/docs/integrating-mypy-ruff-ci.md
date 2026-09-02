---
last_verified: 2026-09-02
tool_version: "2.3.1"
sources:
  - https://mypy.readthedocs.io/en/stable/common_issues.html
  - https://pynions.com/ruff-python
---

# Integrating mypy with ruff in CI

> L4 notes — exit-code aggregation, cache isolation, and ANN* rule-overlap elimination when running both tools in a single pipeline.

## Purpose

Running mypy and ruff in the same CI pipeline is the standard Python quality gate, but three friction points emerge quickly: aggregating their exit codes so the job fails on either tool's violations, keeping their caches isolated so stale results don't leak across runs, and eliminating ANN* rule overlaps where ruff's annotation checks conflict with mypy's type enforcement. This doc captures a working integration pattern that addresses all three.

## Exit-code aggregation

Both mypy and ruff exit non-zero on violations. A naive CI script runs them sequentially and checks `$?` after each, but this breaks down when you want a single pass/fail signal. The pattern that works:

```bash
#!/usr/bin/env bash
set -uo pipefail

mypy_exit=0
ruff_exit=0

mypy src/ || mypy_exit=$?
ruff check . || ruff_exit=$?
ruff format --check . || ruff_exit=$((ruff_exit + 1))

if [ "$mypy_exit" -ne 0 ] || [ "$ruff_exit" -ne 0 ]; then
  echo "CI gate failed: mypy=$mypy_exit ruff=$ruff_exit"
  exit 1
fi
```

The key detail: `set -uo pipefail` prevents early exit on the first failure while still catching pipeline errors. Each tool runs to completion so the developer sees all violations in one CI run, not a fixed-them-one-only-to-see-the-other pattern. This approach is simpler than collecting exit codes in an array and produces the same result.

## Cache isolation

mypy's incremental cache (`MYPY_CACHE_DIR`) and ruff's cache (`.ruff_cache/`) can collide in unexpected ways when CI agents share workspace directories across jobs. The fix is explicit cache isolation:

**mypy:** Set `MYPY_CACHE_DIR` to a path keyed by the Python version and lockfile hash:

```yaml
env:
  MYPY_CACHE_DIR: .mypy-cache-${{ matrix.python-version }}-${{ hashFiles('uv.lock') }}
```

**ruff:** Ruff's cache is auto-managed and version-aware, but it also respects `RUFF_CACHE_DIR`. If you pin ruff versions (recommended), the default cache location is fine. If you don't pin, isolate it the same way:

```yaml
env:
  RUFF_CACHE_DIR: .ruff-cache-${{ hashFiles('pyproject.toml') }}
```

Both caches should be restored from a CI cache action keyed by their respective paths. A cold-cache run with `--no-incremental` for mypy on the first CI pass after a lockfile change prevents stale-type errors from a previous dependency version.

## ANN* rule-overlap elimination

Ruff's `ANN` rules (flake8-annotations) check for missing type annotations, but mypy's `--strict` mode does the same thing — and more, including type-narrowing checks that ruff cannot perform. Running both produces duplicate violations: ruff flags a missing annotation, mypy flags the same function as untyped. The overlap is noise.

The fix is to disable ANN rules when mypy is active:

```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP", "SIM", "RUF"]
# ANN rules disabled — mypy covers type annotations more thoroughly
ignore = ["ANN001", "ANN002", "ANN003", "ANN101", "ANN102", "ANN201", "ANN202", "ANN204", "ANN205", "ANN206"]
```

Alternatively, use per-file-ignores to keep ANN rules for files mypy doesn't check (scripts, configs, tests):

```toml
[tool.ruff.lint.per-file-ignores]
"tests/**" = ["ANN"]  # Keep ANN for tests — mypy may not cover test files
"scripts/**" = []
```

This pattern lets mypy own type-annotation enforcement in production code while ruff handles it only where mypy doesn't reach.

## Verify

- Run the aggregation script with one tool failing and confirm the overall exit code is 1.
- Clear both cache directories and run CI twice — confirm the second run uses incremental cache and completes faster.
- Enable ANN rules alongside mypy `--strict` and confirm duplicate violations appear; then disable ANN and confirm they disappear.

## Common errors

- **mypy cache corruption after dependency update:** If mypy reports errors that disappear on a clean run, the cache is stale. Fix: `rm -rf .mypy-cache-*` or bump the cache key in CI.
- **ruff format undoes mypy autofixes:** Run `ruff check --fix .` before `ruff format .` — the formatter can revert linter changes if the order is reversed. Source: https://pynions.com/ruff-python
- **ANN rules fire after mypy passes:** Ruff runs faster than mypy in CI, so developers see ANN violations first and fix them manually, only for mypy to flag the same issues. Disabling ANN eliminates this two-pass frustration.

## References

- mypy common issues: https://mypy.readthedocs.io/en/stable/common_issues.html
- Ruff project patterns: https://pynions.com/ruff-python
