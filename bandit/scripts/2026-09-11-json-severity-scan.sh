# last_verified: 2026-09-11 · bandit 1.9.4

# Minimal bandit scan: JSON output with severity filtering
# Demonstrates how to get machine-readable output and filter by severity level

TARGET="${1:-.}"
SEVERITY="${2:-medium}"

echo "=== Bandit JSON scan: target=$TARGET severity>=$SEVERITY ==="

# Run bandit with JSON formatter, filtering to medium+ severity
bandit -r "$TARGET" \
  -f json \
  --severity-level "$SEVERITY" \
  --confidence-level medium \
  -x tests,.venv,venv \
  2>/dev/null | python3 -c "
import sys, json

data = json.load(sys.stdin)
results = data.get('results', [])
metrics = data.get('metrics', {})

print(f'Total findings: {len(results)}')
print()

if not results:
    print('No findings at or above the configured threshold.')
    sys.exit(0)

# Group by severity
by_severity = {}
for r in results:
    sev = r.get('issue_severity', 'UNKNOWN')
    by_severity.setdefault(sev, []).append(r)

for sev in ['HIGH', 'MEDIUM', 'LOW']:
    items = by_severity.get(sev, [])
    if items:
        print(f'--- {sev} ({len(items)} findings) ---')
        for item in items:
            test_id = item.get('test_id', '?')
            filename = item.get('filename', '?')
            line = item.get('line_number', '?')
            msg = item.get('issue_text', '')
            print(f'  {test_id} {filename}:{line} — {msg}')
        print()

# Summary per file
file_counts = {}
for r in results:
    f = r.get('filename', '?')
    file_counts[f] = file_counts.get(f, 0) + 1

print('--- Per-file summary ---')
for f, count in sorted(file_counts.items(), key=lambda x: -x[1]):
    print(f'  {count:3d}  {f}')
"

echo ""
echo "Exit code: $?"
