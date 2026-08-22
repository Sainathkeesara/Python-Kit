#!/bin/bash
# last_verified: 2026-08-21 · pip-audit 2.10.1
#
# CI-friendly pip-audit scan against a lockfile with exit-code gating.
# Usage: ./2026-08-21-ci-friendly-pip-audit-scan.sh <lockfile> [extra pip-audit args]
#
# Exit codes:
#   0 - no vulnerabilities found
#   1 - vulnerabilities found (or pip-audit error)
#   2 - missing lockfile argument



if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <lockfile> [extra pip-audit args]" >&2
  exit 2
fi

LOCKFILE="$1"
shift

if [[ ! -f "$LOCKFILE" ]]; then
  echo "Error: lockfile not found: $LOCKFILE" >&2
  exit 2
fi

# Ensure pip-audit is installed
if ! command -v pip-audit &>/dev/null; then
  echo "Installing pip-audit..." >&2
  pip install pip-audit
fi

echo "Scanning $LOCKFILE for known vulnerabilities..." >&2

# Run pip-audit against the lockfile
# --strict: fail if any dependency collection fails
# --desc: include vulnerability descriptions (human-readable)
# --format columns for CI logs
pip-audit --requirement "$LOCKFILE" --strict --desc --format columns "$@"