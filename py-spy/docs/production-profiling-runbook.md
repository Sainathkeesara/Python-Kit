---
last_verified: 2026-09-06
tool_version: n/a
---

# Production py-spy runbook: profiling a live service without downtime

## Purpose

This runbook covers how to use py-spy to profile a live Python service in production without restarting it or introducing noticeable overhead. It walks through attaching to a running process, choosing appropriate sampling rates, interpreting flamegraph output, and cleaning up after profiling sessions.

## When to use

Use this runbook when:

- A production Python service is experiencing latency spikes or elevated CPU usage and you need to identify the hot code path without restarting the process.
- You need to compare profiling results across different sampling rates to balance precision against overhead.
- You want to generate a flamegraph artifact that can be shared with the team or attached to a performance ticket.
- You are profiling a service running inside a container and need to handle namespace and permission constraints.

## Prerequisites

- py-spy installed on the machine where you will run the profiler (not necessarily the same machine as the service -- remote profiling works over SSH or port forwarding).
- Ability to attach to the target process: either run as the same user, have `CAP_SYS_PTRACE` in a container, or set `kernel.perf_event_paranoid` to a permissive value.
- A running Python process to profile. You need its PID or a way to launch it.
- For containerized services: `nsenter` or `docker exec` access to the target container's PID namespace.

## Steps

### 1. Locate the target process

Find the PID of the running Python service:

```bash
pgrep -f "python.*app.py"
# or
ps aux | grep "python.*app.py"
```

For containerized services, get the container's PID from the host:

```bash
docker inspect --format '{{.State.Pid}}' <container_name>
```

### 2. Verify attach permissions

Before profiling, confirm that py-spy can attach:

```bash
py-spy dump --pid <PID>
```

If this prints stack frames, you have permission. If it fails with "permission denied" or "ptrace" errors, either:

- Run as root or with `sudo`.
- Set `kernel.perf_event_paranoid` to 1 or lower: `sysctl kernel.perf_event_paranoid=1`.
- In Docker, add `--cap-add=SYS_PTRACE` to the container run command.

### 3. Profile with `top` for a quick live view

Start with `py-spy top` to get an immediate, continuously updating view of where CPU time is spent:

```bash
py-spy top --pid <PID>
```

This produces no output file and introduces minimal overhead. Watch for functions that stay at the top of the list for more than a few seconds -- those are your hotspots. Press `q` to detach.

### 4. Record a flamegraph with appropriate sampling rate

For a shareable artifact, use `py-spy record`:

```bash
py-spy record -o profile.svg --pid <PID> --duration 30
```

Key flags for production:

- `--duration <seconds>` -- limits how long sampling runs. Use 15-60 seconds for most investigations.
- `--rate <Hz>` -- controls sampling frequency. The default (100 Hz) is safe for most services. Drop to 10-25 Hz on very high-throughput services to reduce overhead, or raise to 200-500 Hz for short bursts when you need finer resolution.
- `--format speedscope` -- writes a `.json` file for the Speedscope viewer instead of SVG, useful for very large profiles.

The overhead from `py-spy record` is typically under 1-2% CPU at default rate. At 100 Hz it interrupts the target process roughly 100 times per second, each time for a few microseconds to capture the stack.

### 5. Capture a one-shot stack dump

When you need to know what a process is blocked on right now -- a lock, I/O wait, or a C extension call -- use `dump`:

```bash
py-spy dump --pid <PID>
```

This is instantaneous and produces no file. It prints every thread's current call stack. Useful for diagnosing deadlocks or stuck threads without any sampling overhead.

### 6. Handle containerized services

For services running in Docker or Kubernetes:

```bash
# From the host, get the container PID and profile from outside
CONTAINER_PID=$(docker inspect --format '{{.State.Pid}}' <container>)
py-spy record -o profile.svg --pid $CONTAINER_PID --duration 30
```

If py-spy cannot see the process from outside, exec into the container:

```bash
docker exec -it <container> pip install py-spy
docker exec -it <container> py-spy record -o /tmp/profile.svg --pid 1 --duration 30
docker cp <container>:/tmp/profile.svg ./profile.svg
```

### 7. Interpret the flamegraph

Open the SVG in a browser. Each rectangle represents a function on the call stack:

- **Width** = proportion of samples where this function appeared. Wider bars are hotter.
- **Height** = stack depth. Taller stacks mean deeper call chains.
- **Color** is arbitrary (randomized per frame) -- do not interpret red as "bad."

How to read it:

1. Start at the top of the flamegraph (the widest bars at the top of the stack).
2. Look for wide bars that dominate the profile -- those are the functions consuming the most CPU.
3. Click a bar to zoom into that subtree. Click the "Reset zoom" button to go back.
4. Search for your own function names (Ctrl+F) to see where they appear in the profile.
5. The y-axis shows the percentage of samples. If a function appears in 40% of samples, it is responsible for roughly 40% of CPU time during the recording window.

Common misinterpretations:

- A wide bar at the bottom (low stack depth) is not necessarily the problem -- it may just be a common entry point that dispatches to many callees.
- A narrow bar deep in the stack can still be the root cause if it is a blocking call (e.g., a database query) that everything else is waiting on.
- Multiple bars of similar width in the same stack path usually indicate the entire call chain is the hotspot, not just one function.

### 8. Choose the right sampling rate

| Rate (Hz) | Overhead | Use case |
|-----------|----------|----------|
| 10 | < 0.5% | Long-running production profiling (hours), minimal impact |
| 25 | < 0.5% | Background profiling in staging, good enough for most CPU热点 |
| 100 (default) | ~1% | Standard investigation, best balance of precision and overhead |
| 200-500 | 2-5% | Short burst profiling (30s or less) when you need fine-grained resolution |

Rule of thumb: start at 100 Hz. If the flamegraph looks noisy or you are concerned about overhead, drop to 25 Hz. If you need to see very short-lived functions, raise to 200+ Hz for a brief recording.

## Verify

After completing a profiling session, confirm the output is valid:

```bash
# Check the SVG file was created and is non-empty
ls -lh profile.svg

# For speedscope output, validate JSON
python -c "import json; json.load(open('profile.json')); print('valid JSON')"
```

If the flamegraph is empty or shows only `<unknown>`, the target process may have been compiled without debug symbols. Ensure Python was built with `--enable-shared` or that the correct debug symbols are available.

## Common errors

| Error | Cause | Fix |
|-------|-------|-----|
| `permission denied` / `ptrace` | Insufficient privileges to attach | Run as root, set `kernel.perf_event_paranoid=1`, or add `CAP_SYS_PTRACE` to container |
| `No such process` | PID is stale or process exited | Re-run `pgrep` to get the current PID |
| Empty flamegraph | Process exited during recording, or debug symbols missing | Use `--duration` shorter than the expected process lifetime; check Python debug symbols |
| `Could not find Python process` | py-spy cannot locate the interpreter | Ensure you are profiling a Python process, not a compiled binary |
| Overhead complaints from monitoring | Sampling rate too high for the workload | Drop to 25 Hz or use `--duration` to limit the window |
