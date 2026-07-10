# last_verified: 2026-07-10 · py-spy n/a
#
# Minimal CPU-bound workload that profiles itself with py-spy record
# and exports speedscope JSON format.
#
# Usage:
#   python 2026-07-10-cpu-speedscope-record.py
#
# The output file (speedscope_profile.json) can be dragged into
# https://www.speedscope.app/ for flamegraph + timeline views.

import os
import subprocess
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(limit):
    count = 0
    for num in range(limit):
        if is_prime(num):
            count += 1
    return count


def build_string(chunks):
    parts = []
    for i in range(chunks):
        parts.append(f"block-{i:04d}")
    return ",".join(parts)


if __name__ == "__main__":
    pid = os.getpid()
    output = "speedscope_profile.json"

    recorder = subprocess.Popen(
        [
            "py-spy", "record", "-o", output,
            "--pid", str(pid), "--duration", "8",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    time.sleep(0.5)

    for _ in range(20):
        count_primes(50_000)
        time.sleep(0.05)
        build_string(500)
        time.sleep(0.05)

    recorder.wait()

    if os.path.exists(output):
        size = os.path.getsize(output)
        print(f"Profile saved: {output} ({size} bytes)")
        print("Drag into https://www.speedscope.app/ to view.")
    else:
        print("No profile file generated.")
        print("Is py-spy installed? Try: pip install py-spy")
