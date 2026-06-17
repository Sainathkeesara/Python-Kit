#!/usr/bin/env bash
# Install py-spy, create a CPU-bound script, profile it, save flamegraph SVG

pip install py-spy -q

cat > cpu_heavy.py << 'EOF'
import math
s = 0
for i in range(1, 100000):
    s += math.sqrt(i) * math.sin(i)
print(s)
EOF

py-spy record -o flamegraph.svg --duration 10 -- python3 cpu_heavy.py
echo "Saved flamegraph.svg"
