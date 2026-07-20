#!/usr/bin/env bash
# last_verified: 2026-07-20 · py-spy n/a

tmpdir=$(mktemp -d)
cat > "$tmpdir/cpu_loop.py" <<'EOF'
import math

def busy_loop():
    total = 0.0
    for i in range(500000):
        total += math.sqrt(i) * math.sin(i)
    print(total)

if __name__ == "__main__":
    busy_loop()
EOF

python3 "$tmpdir/cpu_loop.py" &
pid=$!
echo "PID: $pid"

timeout 3 py-spy top --pid "$pid" || true

py-spy record --pid "$pid" --duration 5 --output "$tmpdir/flamegraph.svg"
echo "Flamegraph saved to $tmpdir/flamegraph.svg"

kill "$pid" 2>/dev/null || true
rm -rf "$tmpdir"
