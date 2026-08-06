---
last_verified: 2026-08-06
tool_version: n/a
---

# py-spy — CLI subcommands I explored

> First look at py-spy's CLI. I ran the main subcommands and checked what each one does.

## What I tried

I installed py-spy with `pip install py-spy` and then ran each subcommand against a small test script.

### `py-spy top`

I ran `py-spy top --pid <PID>` and it showed a live-updating table of which Python functions were using the most CPU. It's like `top` but for Python call stacks — I could see the function names and how much time they spent.

### `py-spy record`

I ran `py-spy record --pid <PID> -o profile.svg` and it generated a flamegraph SVG. The flamegraph makes it easy to spot wide stacks that are eating CPU. I used it on a tight loop and could see exactly which function was the bottleneck.

### `py-spy flamegraph`

This subcommand generates a flamegraph from a previously recorded profile. I pointed it at the SVG from `record` and it rendered the same visualization. It's useful when I want to regenerate the graph without re-running the profiler.

### `py-spy --help`

Running `py-spy --help` lists all available subcommands and their flags. I used it to discover the `--duration` flag for `record`, which lets me limit how long the profiling runs.

## What I noticed

- `top` is live and interactive — it updates in real time.
- `record` produces a file I can open in a browser.
- `--help` is the best starting point for discovering flags I didn't know about.

## What I'll try next

I want to try `py-spy dump` to see raw call stack data, and experiment with the `--subprocess` flag to profile child processes.