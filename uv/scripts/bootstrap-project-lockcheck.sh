#!/usr/bin/env bash
# last_verified: 2026-08-20 · uv
#
# Bootstrap a uv-managed project in a throwaway dir: init a src-layout
# package, add runtime + dev deps, sync every group, then prove the
# lockfile reproduces by wiping .venv and re-syncing off uv.lock.
# run: bash bootstrap-project-lockcheck.sh

set -euo pipefail

PROJECT_DIR=$(mktemp -d)
trap 'rm -rf "$PROJECT_DIR"' EXIT
cd "$PROJECT_DIR"

echo "== 1. init a src-layout package =="
uv init --package demo-svc

echo "== 2. add a runtime dependency =="
uv add "requests>=2.31"

echo "== 3. split dev-only deps into the dev group =="
uv add --dev ruff pytest

echo "== 4. generated tables =="
sed -n '1,30p' pyproject.toml

echo "== 5. sync all groups (runtime + dev) =="
uv sync --all-groups

echo "== 6. record the lockfile hash =="
REF_SHA=$(sha256sum uv.lock | cut -d' ' -f1)

echo "== 7. wipe .venv and re-sync from uv.lock alone =="
rm -rf .venv
uv sync --all-groups

NEW_SHA=$(sha256sum uv.lock | cut -d' ' -f1)
if [ "$REF_SHA" = "$NEW_SHA" ]; then
    echo "OK: uv.lock unchanged after a fresh sync -> reproducible."
else
    echo "DRIFT: lockfile changed on re-sync; check for non-pinned sources." >&2
    exit 1
fi

echo "== 8. run a dev-only tool from the recreated venv =="
uv run pytest --version