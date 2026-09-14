# last_verified: 2026-09-14 · bandit 1.9.4

# Minimal bandit scan with JSON output and severity filtering.
# Demonstrates how to preserve bandit's exit status so CI gates
# don't mask findings as success.

set -o pipefail

TARGET="${1:-.}"
SEVERITY="${2:-low}"

TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

bandit -r -f json "$TARGET" > "$TMPFILE" 2>/dev/null
BANDIT_EXIT=$?

jq --arg sev "$SEVERITY" '
  .results |= map(select(.issue_severity == ($sev | ascii_upcase)))
  | {results, metrics: .metrics._totals}
' "$TMPFILE"

if [ "$BANDIT_EXIT" -ne 0 ]; then
  echo "bandit found issues (exit code: $BANDIT_EXIT)" >&2
  exit "$BANDIT_EXIT"
fi
