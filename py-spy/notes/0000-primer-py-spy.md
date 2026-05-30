# py-spy — quick primer

> First-day notes for someone who's never used py-spy. Personal voice, plain language.

## What is it?

py-spy is a sampling profiler for Python programs — think of it as a performance microscope that peers into a running Python process and shows you what functions are eating CPU time. It's like `top` for Python call stacks, but without needing to modify your code or restart your program.

If you've ever used Chrome DevTools' Performance tab to profile JavaScript, py-spy gives you that same kind of flamegraph + function timing, but for Python. The magic part: it attaches to a running process using process-vm-readv on Linux, so it doesn't slow down your code the way `cProfile` does.

## What does it do?

You point py-spy at a running Python PID (or launch a script with it), and it samples the call stack at regular intervals. After enough samples, it shows you which functions were on the stack most often — those are your hot spots. It can output a live top-like view, save a flamegraph SVG, or record a raw profile for later analysis.

## Why does it exist?

Profiling Python has always been a pain. `cProfile` adds massive overhead (sometimes 10-50x slower), and `profile` is even worse. You can't realistically use them in production. `time` and manual logging tell you nothing about *where* time is spent inside a function. py-spy's sampling approach adds almost zero overhead — typically under 1% — so you can run it against production processes without distorting the metrics.

## Key terminology

- **Sampling profiler** — Periodically records the current call stack instead of instrumenting every function call. Example: py-spy records the stack 100 times per second by default.
- **Flamegraph** — A visualisation where each rectangle is a function call; wider = more time. Example: py-spy `--flamegraph profile.svg` produces a clickable SVG.
- **PID** — Process ID that py-spy attaches to. Example: `py-spy top --pid 1234` shows live stats for process 1234.
- **`top` subcommand** — A live, updating terminal view of the hottest functions, like htop but for Python call stacks.
- **`record` subcommand** — Saves raw profile data to a file for later analysis. Example: `py-spy record -o profile.json --pid 1234`.
- **Native frames** — C extension functions running inside the interpreter. py-spy can show them if you pass `--native`.
- **Idle time** — Time spent in `time.sleep()` or waiting on I/O; py-spy doesn't count it as busy.

## A tiny example

```bash
pip install py-spy

# Run a script under py-spy
py-spy record -o profile.svg -- python -c "
import time
total = 0
for i in range(1000000):
    total += i * i
    if i % 100000 == 0:
        time.sleep(0.1)
print(total)
"
```

This records a flamegraph SVG of a short CPU-bound script. Open `profile.svg` in a browser to see the call stacks.

## What I'll cover next

I want to try py-spy against a long-running script with identifiable functions to see the top subcommand in action, then explore the record and flamegraph outputs to understand where hot spots are. After that I'll try profiling something real — maybe a pytest test suite or a small web server.
