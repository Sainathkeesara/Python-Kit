#!/bin/bash
# last_verified: 2026-09-04 · pip-audit 2.10.1
#
# Run pip-audit against the project's exported requirements lockfile.
# Exits 0 if no vulnerabilities are found, 1 otherwise.

set -euo pipefail

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is required. Install it from https://docs.astral.sh/uv/" >&2
    exit 1
fi

if ! command -v pip-audit >/dev/null 2>&1; then
    echo "Error: pip-audit is not installed. Run: uv pip install pip-audit" >&2
    exit 1
fi

LOCKFILE="requirements.lock"

echo "Exporting resolved dependencies to $LOCKFILE..."
uv export --format=requirements-txt -o "$LOCKFILE"

echo "Running pip-audit on $LOCKFILE..."
pip-audit -r "$LOCKFILE" --no-deps --disable-pip
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "No vulnerabilities found."
else
    echo "Vulnerabilities detected — review the output above."
fi

exit $EXIT_CODE
