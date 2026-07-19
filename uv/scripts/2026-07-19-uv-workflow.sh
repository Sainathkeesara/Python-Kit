#!/usr/bin/env bash
# Walk through uv init -> add -> run -> lock in a temp project

set -e

PROJECT=$(mktemp -d) && cd "$PROJECT"

echo "=== 1. Init a new project ==="
uv init demo-cli --no-readme

echo "=== 2. Add a dependency ==="
uv add requests

echo "=== 3. Write a tiny script ==="
cat > main.py << 'EOF'
import requests
r = requests.get("https://httpbin.org/get")
print(f"Status: {r.status_code}, deps: {len(r.json())}")
EOF

echo "=== 4. Run it with uv ==="
uv run python main.py

echo "=== 5. Inspect generated lockfile ==="
head -20 uv.lock
echo "... (lockfile has $(wc -l < uv.lock) lines)"

rm -rf "$PROJECT"
