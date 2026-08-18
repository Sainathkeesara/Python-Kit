#!/usr/bin/env bash
# last_verified: 2026-08-17 · py-spy n/a

set -euo pipefail

if ! command -v py-spy >/dev/null 2>&1; then
    echo "py-spy not found; installing..."
    pip install py-spy -q
fi

PROJECT_DIR="$(mktemp -d)"
trap 'rm -rf "$PROJECT_DIR"' EXIT

cat > "$PROJECT_DIR/cpu_worker.py" <<'EOF'
import math
import time

def cpu_bound(n):
    s = 0
    for i in range(1, n):
        s += math.sqrt(i) * math.sin(i)
    return s

if __name__ == "__main__":
    while True:
        cpu_bound(500_000)
        time.sleep(0.5)
EOF

echo "=== Starting CPU-bound process in background ==="
python3 "$PROJECT_DIR/cpu_worker.py" &
WORKER_PID=$!
echo "Worker PID: $WORKER_PID"

sleep 2

echo ""
echo "=== py-spy record — flamegraph SVG ==="
py-spy record -o "$PROJECT_DIR/flamegraph.svg" --duration 5 -p "$WORKER_PID"
echo "Saved flamegraph to $PROJECT_DIR/flamegraph.svg"

echo ""
echo "=== py-spy dump — textual call stack ==="
py-spy dump -p "$WORKER_PID"

echo ""
echo "=== py-spy top — live sampling ==="
py-spy top -p "$WORKER_PID" &
TOP_PID=$!
sleep 2
kill "$TOP_PID" 2>/dev/null || true
wait "$TOP_PID" 2>/dev/null || true

kill "$WORKER_PID" 2>/dev/null || true
wait "$WORKER_PID" 2>/dev/null || true

echo ""
echo "=== Verify outputs ==="
ls -l "$PROJECT_DIR/flamegraph.svg"
echo "Script completed successfully."
