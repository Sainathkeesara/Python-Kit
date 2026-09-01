#!/usr/bin/env bash
# last_verified: 2026-09-01 · pre-commit n/a
# Bootstrap pre-commit on a fresh repo: ensure the config exists, install the
# git hook, and run --all-files. Designed for first-run setup and CI bootstrap.
# Distinct from ci-parity-check.sh: this script scaffolds a missing config and
# handles the initial install; ci-parity-check.sh assumes the repo is already
# wired and only re-verifies the install + bypass state.

set -e

CONFIG_FILE=".pre-commit-config.yaml"

echo "==> Checking for ${CONFIG_FILE}..."
if [ ! -f "${CONFIG_FILE}" ]; then
    echo "No ${CONFIG_FILE} found."
    echo "Generate one with: pre-commit sample-config > ${CONFIG_FILE}"
    if command -v pre-commit >/dev/null 2>&1; then
        echo "Pre-commit is installed; sampling a default config from the local install."
        pre-commit sample-config > "${CONFIG_FILE}"
    else
        echo "Pre-commit is not installed. Install it first:"
        echo "  pip install pre-commit"
        echo "  pre-commit sample-config > ${CONFIG_FILE}"
        exit 1
    fi
fi

if ! command -v pre-commit >/dev/null 2>&1; then
    echo "ERROR: pre-commit not on PATH. Run: pip install pre-commit"
    exit 1
fi

if [ ! -d ".git" ]; then
    echo "ERROR: not inside a git working tree. Run from the repo root."
    exit 1
fi

echo "==> Installing pre-commit hook into .git/hooks/..."
pre-commit install

echo "==> Running hooks on all files (CI parity)..."
pre-commit run --all-files --show-diff-on-failure
rc=$?

if [ "${rc}" -ne 0 ]; then
    echo "Hooks reported failures (exit ${rc}). CI would fail the same way."
    exit "${rc}"
fi

echo "==> Bootstrap complete. Hooks installed and clean."