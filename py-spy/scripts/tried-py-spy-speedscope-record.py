# Self-contained: run CPU-bound work and profile with py-spy record
# Saving speedscope JSON output for timeline + flamegraph views
import os
import subprocess
import time


def cpu_work(n):
    total = sum(i ** 2 for i in range(n))
    return total


if __name__ == "__main__":
    pid = os.getpid()
    output = "speedscope_profile.json"

    recorder = subprocess.Popen(
        ["py-spy", "record", "-o", output, "--pid", str(pid), "--duration", "6"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Give py-spy a moment to attach before starting work
    time.sleep(0.5)

    for _ in range(25):
        cpu_work(200_000)
        time.sleep(0.1)

    recorder.wait()

    if os.path.exists(output):
        size = os.path.getsize(output)
        print(f"Speedscope profile saved to {output} ({size} bytes)")
        print("Open at https://www.speedscope.app/ — drag the file in")
    else:
        print("No profile file — check py-spy is installed and has permissions")
