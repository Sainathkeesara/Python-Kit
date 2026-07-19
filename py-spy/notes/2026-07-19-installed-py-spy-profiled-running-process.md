---
last_verified: 2026-07-19
tool_version: n/a
---
# Installing py-spy and profiling my first *running* process

Notes to myself after finally getting py-spy pointed at a process that was already running, instead of launching one under it.

## Installing

Installed it into my project venv with `pip install py-spy`. Quick — it ships as a prebuilt binary, so there was no Rust toolchain or long compile like I half-expected. Confirmed it landed with `py-spy --version`.

## Attaching to something already running

I had a long loop running in one terminal. In a second terminal I grabbed its PID and ran:

```bash
py-spy top --pid $(pgrep -f my_loop.py)
```

`top` gives a live, `htop`-style view — function names with the % of samples currently landing in each. My hot function floated to the top within a second or two, which felt like magic compared to sprinkling `print()` everywhere.

## What tripped me up

- **Permissions.** First attempt gave a permission error. py-spy has to read another process's memory, so I needed `sudo py-spy top --pid ...`. Once I ran it with sudo it attached fine.
- **Finding the PID.** `pgrep -f my_loop.py` was easier than eyeballing `ps aux`. I kept forgetting the process has to actually *be running* when I attach — if it already exited there's nothing to sample.

## What I'd try next

Swap `top` for `record` to save a flamegraph of a live process, and see how the sampling rate flag changes what I capture.
