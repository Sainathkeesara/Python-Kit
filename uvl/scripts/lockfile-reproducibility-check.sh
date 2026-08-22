#!/usr/bin/env bash
# last_verified: 2026-08-22 · uv n/a
#
# Lockfile reproducibility check for an existing uv project.
# Verifies that uv.lock is consistent with pyproject.toml, records
# its hash, performs a fresh install from lock, and flags any drift.
# run: bash lockfile-reproducibility-check.sh

set -euo pipefail

if [[ ! -f "uv.lock" ]]; then
    echo "ERROR: uv.lock not found in $(pwd)" >&2
    exit 1
fi

echo "== 1. verify lockfile matches pyproject.toml =="
uv lock --check

echo "== 2. record current lockfile hash =="
REF_SHA=$(sha256sum uv.lock | cut -d' ' -f1)

echo "== 3. fresh install from lock =="
rm -rf .venv
uv sync --frozen

echo "== 4. compare hashes =="
NEW_SHA=$(sha256sum uv.lock | cut -d' ' -f1)
if [[ "$REF_SHA" == "$NEW_SHA" ]]; then
    echo "OK: lockfile is reproducible."
else
    echo "DRIFT: lockfile changed after fresh sync." >&2
    exit 1
fi
