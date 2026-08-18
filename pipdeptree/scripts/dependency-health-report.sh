#!/bin/bash
# last_verified: 2026-08-18 · pipdeptree n/a
#
# Build a dependency-health report from pipdeptree --warn, reverse deps, and JSON tree.
# Produces a summary of conflicts, top-level packages, leaf packages, and
# packages sorted by reverse-dependency count.

set -euo pipefail

if ! command -v pipdeptree >/dev/null 2>&1; then
    echo "Error: pipdeptree is not installed." >&2
    exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is required for JSON parsing." >&2
    exit 1
fi

REPORT="$(mktemp)"
trap 'rm -f "$REPORT"' EXIT

echo "=== pipdeptree warnings ==="
pipdeptree --warn 2>&1 || true

echo ""
echo "=== Reverse dependency tree ==="
pipdeptree --reverse || true

echo ""
echo "=== Full dependency tree (JSON) ==="
pipdeptree --json > "$REPORT"

echo "=== Health summary ==="
python3 - "$REPORT" <<'PYEOF'
import json, sys
from collections import Counter

with open(sys.argv[1]) as f:
    pkgs = json.load(f)

all_dep_keys = set()
for p in pkgs:
    for d in p.get("dependencies", []):
        all_dep_keys.add(d["key"])

top_level = [p for p in pkgs if p["package"]["key"] not in all_dep_keys]
leaf = [p for p in pkgs if not p.get("dependencies")]
conflicts = [
    p for p in pkgs
    if p["package"].get("required_version")
    and p["package"]["required_version"] != p["package"].get("installed_version", "")
]

reverse = Counter()
for p in pkgs:
    for d in p.get("dependencies", []):
        reverse[d["key"]] += 1

print(f"Total packages:        {len(pkgs)}")
print(f"Top-level packages:    {len(top_level)}")
print(f"Leaf packages:         {len(leaf)}")
print(f"Version conflicts:     {len(conflicts)}")

if conflicts:
    print("\nConflicts:")
    for c in conflicts:
        print(f"  {c['package']['key']}: required {c['package']['required_version']}, installed {c['package']['installed_version']}")

print("\nTop 10 reverse-dependency counts:")
for key, count in reverse.most_common(10):
    print(f"  {key}: {count}")
PYEOF
