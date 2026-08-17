---
last_verified: 2026-08-17
tool_version: n/a
---

# When to use py-spy top vs record/flamegraph vs dump, and how to read the output

## Purpose
This doc explains the three main interaction modes in py-spy — `top`, `record`, and `dump` — and when each is the right tool for profiling a running Python process. The goal is to help you pick the right mode for the question you're asking and to interpret the output without getting lost in flamegraph noise.

## When to use
- Use `top` when you want a live, updating view of where a process is spending CPU right now. It's the quickest way to spot a hot function without stopping the process.
- Use `record` when you need a flamegraph SVG (or speedscope JSON) for deeper analysis or sharing. It samples over a window and produces a file you can open offline.
- Use `dump` when you want a one-shot snapshot of the current call stack for every thread — useful for quick diagnosis without the overhead of generating a flamegraph.

## Prerequisites
- py-spy installed (`pip install py-spy`).
- Root access or a relaxed `kernel.perf_event_paranoid` setting if profiling a process you don't own.

## Steps

### Using `top`
`py-spy top --pid <PID>` attaches to a running process and prints a live updating view. The output shows function names alongside the percentage of samples they appeared in. Press `q` to detach.

### Using `record`
`py-spy record -o profile.svg --pid <PID>` samples the target and writes a flamegraph SVG. The SVG is a single file where wider frames mean more samples; hover over a frame to see the exact function name and percentage.

### Using `dump`
`py-spy dump --pid <PID>` prints the current call stack of every thread to the terminal and exits immediately. There's no sampling window and no output file. This is the fastest way to confirm what a stuck process is waiting on.

## Verify
Run each mode against a process you control:

```bash
# 1. record: samples a short-lived script and writes a flamegraph
cat > /tmp/brief_work.py <<'EOF'
import time
for _ in range(50):
    time.sleep(0.01)
EOF
py-spy record -o /tmp/profile.svg -- python /tmp/brief_work.py
```

The SVG should open in a browser with the same function at the widest frame.

```bash
# 2. top: live view of a long-running process (press q to detach)
python -c "while True: pass" &
TARGET_PID=$!
py-spy top --pid $TARGET_PID
kill $TARGET_PID 2>/dev/null || true
```

The output should show Python frames dominating the sample.

```bash
# 3. dump: one-shot snapshot
python -c "while True: pass" &
TARGET_PID=$!
sleep 0.5
py-spy dump --pid $TARGET_PID
kill $TARGET_PID
```

`dump` should list the same function at the top of the stack.
