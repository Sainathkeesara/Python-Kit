#!/usr/bin/env bash
# Profile a CPU-bound Python script with py-spy record and output a flamegraph SVG

tmp_script=$(mktemp /tmp/cpu-bound-XXXXXX.py)

cat > "$tmp_script" <<- 'PYEOF'
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
n = 2
while count < 1000:
    if is_prime(n):
        count += 1
    n += 1

print(f"Found {count} primes")
PYEOF

echo "Starting CPU-bound script under py-spy..."
py-spy record -o flamegraph.svg --duration 15 -- python3 "$tmp_script"
echo "Flamegraph saved to flamegraph.svg"

rm "$tmp_script"
