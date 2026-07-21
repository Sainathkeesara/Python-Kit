#!/usr/bin/env bash
# last_verified: 2026-07-20 · py-spy n/a

python3 -c "import math; total=sum(math.sqrt(i)*math.sin(i) for i in range(3000000)); print(total)" &
PID=$!
sleep 1
timeout 3 py-spy top --pid "$PID" 2>/dev/null || true
py-spy record --pid "$PID" --duration 3 -o /tmp/py-spy-flame.svg 2>/dev/null
kill "$PID" 2>/dev/null || true
