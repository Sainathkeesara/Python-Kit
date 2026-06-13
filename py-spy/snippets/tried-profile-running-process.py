# Profile a running Python process and export a flamegraph SVG via py-spy
# This script spawns CPU-bound work, then attaches py-spy to capture
# a flamegraph of the already-running process.
import os
import subprocess
import time


def cpu_bound_work(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


if __name__ == "__main__":
    pid = os.getpid()
    output = "flamegraph_running.svg"

    # Spawn py-spy in record mode targeting our own PID.
    # --pid attaches to the running process instead of starting a new one.
    # --duration limits collection so we don't loop forever.
    recorder = subprocess.Popen(
        ["py-spy", "record", "-o", output, "--pid", str(pid), "--duration", "8"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Give py-spy a moment to attach before the CPU work starts.
    # Without this sleep, py-spy might miss the beginning of the workload.
    time.sleep(0.5)

    for _ in range(100):
        cpu_bound_work(100_000)

    recorder.wait()

    if os.path.exists(output):
        size = os.path.getsize(output)
        print(f"Flamegraph saved to {output} ({size} bytes)")
        print("Open in a browser to view the SVG")
    else:
        print("No flamegraph file — check that py-spy is installed")
        print("  pip install py-spy")
        print("Also make sure kernel.perf_event_paranoid allows tracing:")
        print("  sudo sysctl kernel.perf_event_paranoid=-1")
