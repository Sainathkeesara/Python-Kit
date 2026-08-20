---
last_verified: 2026-08-17
tool_version: n/a
---

# py-spy profiling modes: top, record, and dump

## Purpose
This document explains when to use each of py-spy's three primary profiling modes — `top`, `record`, and `dump` — and how to interpret their output. It is aimed at someone who has installed py-spy and needs to decide which command to run first.

## When to use

**Use `py-spy top` when you need a quick, live view of where a Python process is spending its time.** It displays a continuously updating table of the hottest functions, similar to the system `top` command. Run it against a running PID or launch a new process directly. This mode is useful for answering "what is this process doing right now?" without producing files.

**Use `py-spy record` when you want a flamegraph or speedscope profile you can inspect offline or share.** It samples the target process and writes the profile to a file. Flamegraphs show stack depth on one axis and sample population on the other, so wider bars indicate hot call paths. This is the right choice when you need a shareable artifact or want to zoom into a specific region.

**Use `py-spy dump` when you want a one-shot textual snapshot of every thread's current call stack.** It prints raw stack frames without aggregation. This is useful for checking what a process is blocked on — for example, whether a thread is waiting on I/O, holding a lock, or stuck in a C extension.

## Prerequisites
- py-spy installed in the current environment.
- Permission to attach to the target process (same user or elevated privileges).
- A running Python process to profile, or a command to launch.

## How to read each output

### top
The `top` view refreshes a table of functions sorted by sample count. A function that stays at the top for several seconds indicates a CPU-bound hotspot. If the list flips rapidly between many functions, the workload is distributed across more code paths.

### record (flamegraph)
A flamegraph is an SVG where each rectangle represents a function on the stack. Width corresponds to how many samples hit that function. To find a hotspot, look for wide bars near the top. Most SVG viewers support zoom and search. A speedscope export writes a `.json` file that some users prefer for zooming across large traces.

### dump
`py-spy dump` prints something like:

```
Process 1234: python3 app.py
Thread 0x7f123456 (running):
    myapp.worker (worker.py:42)
    myapp.main (main.py:88)
    ...
```

Each thread block shows its current call stack. Threads inside system calls such as `select` or `sleep` are typically blocked on I/O. Threads inside a tight loop in application code are CPU-bound.

## Verify
Run each mode against a CPU-bound process and confirm the output matches the expected shape:

1. Launch a CPU-bound process in the background.
2. Run `py-spy record -o /tmp/flame.svg --duration 3 -p <pid>` and confirm the SVG file exists.
3. Run `py-spy dump -p <pid>` and confirm the worker function appears in the stack output.
4. Run `py-spy top -p <pid>` for a few seconds, then stop it. Confirm the top function matches the worker.

## Common errors
- **Permission denied:** py-spy needs permission to read the target process memory. Run as the same user or with elevated privileges. On macOS, system integrity protections may block profiling of system Python — use a user-installed interpreter instead.
- **Missing symbols:** if the flamegraph shows `???` or unnamed frames, the target binary was stripped or built without debug symbols. Reinstall Python with symbols or profile interpreted code paths instead.
- **`py-spy top` scrolls too fast:** the sample rate is configurable. Pass a lower rate to slow the refresh, or pipe through a pager.
