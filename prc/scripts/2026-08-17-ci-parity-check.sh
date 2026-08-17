#!/usr/bin/env bash
# last_verified: 2026-08-17 · pre-commit n/a
# Automate pre-commit install and --all-files runs with a CI parity check.
# Installs the git hook, runs every hook repo-wide, and verifies the run
# wasn't masked by local bypass variables.

echo "==> Installing pre-commit hooks..."
pre-commit install

echo "==> Running hooks on all files (CI mode)..."
pre-commit run --all-files --show-diff-on-failure
rc=$?

if [ $rc -ne 0 ]; then
    echo "Hook run failed with exit code $rc. CI would see the same failure."
    exit $rc
fi

echo "==> Parity check: confirming no SKIP bypass is active..."
if [ -n "${SKIP:-}" ]; then
    echo "WARNING: SKIP is set ($SKIP). CI ignores SKIP, so this local pass is misleading."
    exit 1
fi

echo "==> Done. Local run matches CI behavior."
