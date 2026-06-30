# tried-cpu-speedscope-record.py — self-profile with py-spy and save speedscope JSON
# Using --pid trick because py-spy record needs a target process
import os
import subprocess
import time

def busy_loop(n):
    # just crunching numbers so py-spy has something to sample
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    pid = os.getpid()
    out_file = "cpu_profile.json"

    # launch py-spy in record mode, attaching to this script's own PID
    # tried py-spy record -o ... -- python script.py first but the
    # subprocess nesting was confusing — attaching to self is simpler
    recorder = subprocess.Popen(
        ["py-spy", "record", "-o", out_file, "--pid", str(pid), "--duration", "5"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # give py-spy a moment to attach before starting work
    time.sleep(0.5)

    for _ in range(20):
        busy_loop(300_000)
        time.sleep(0.1)

    recorder.wait()

    if os.path.exists(out_file):
        kb = os.path.getsize(out_file) / 1024
        print(f"saved {out_file} ({kb:.1f} KB)")
        print("open at https://www.speedscope.app/ and drag the file in")
    else:
        print("no profile output — is py-spy installed?")
