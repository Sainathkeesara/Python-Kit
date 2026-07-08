# last_verified: 2026-07-08 · py-spy n/a
#
# Runs CPU-bound work and profiles itself with py-spy record in speedscope
# JSON format.  The output can be opened at https://www.speedscope.app/
#
# Using --pid so py-spy attaches to this script's own process instead of
# wrapping it as a subprocess — avoids nesting confusion.

import os
import subprocess
import time


def do_math(n):
    """Crunch numbers so py-spy has something to sample."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


def do_strings(n):
    """String operations — another CPU-heavy target for the profiler."""
    result = ""
    for i in range(n):
        result += chr(65 + (i % 26))
    return result


if __name__ == "__main__":
    pid = os.getpid()
    output = "speedscope_profile.json"

    # Launch py-spy in record mode attached to this PID.
    # --duration caps the trace at 6 seconds so it doesn't run forever.
    recorder = subprocess.Popen(
        [
            "py-spy", "record", "-o", output,
            "--pid", str(pid), "--duration", "6",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Give py-spy a moment to attach before starting work.
    time.sleep(0.5)

    # Alternate between math and string work so the speedscope timeline
    # shows two distinct activity blocks.
    for _ in range(15):
        do_math(200_000)
        time.sleep(0.1)
        do_strings(100_000)
        time.sleep(0.1)

    recorder.wait()

    if os.path.exists(output):
        size = os.path.getsize(output)
        print(f"Speedscope profile saved to {output} ({size} bytes)")
        print("Drag the file into https://www.speedscope.app/ to view it.")
    else:
        print("No profile file generated — is py-spy installed?")
        print("Install with: uv tool install py-spy  or  pip install py-spy")
