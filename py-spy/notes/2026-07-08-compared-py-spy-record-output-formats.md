---
last_verified: 2026-07-08
tool_version: n/a
---

# Compared py-spy record output formats — flamegraph, speedscope, raw

I already knew py-spy could dump a flamegraph, but I wanted to understand the trade-offs between all three `record` output formats. Here's what I found running each against the same CPU-bound script.

## The test script

I used a small Python file that does number crunching in a loop — the same `../scripts/cpu_worker.py` for all three runs so the comparison is fair.

## Flamegraph SVG (`-o flame.svg`)

This is the default output. Command:

```bash
py-spy record -o flame.svg -- python cpu_worker.py --duration 10
```

The SVG opens in a browser and shows a flamegraph you can hover and zoom. The widest frames are the hottest code paths. For my test script, `do_math` was the widest bar — exactly what I expected.

**What tripped me up:** the SVG doesn't preserve per-sample timing. You see aggregate sample counts per function but can't tell when each function ran during the trace. Also the SVG was ~120 KB for a 10-second run — fine for one-off sharing but not great for archiving.

## Speedscope JSON (`-o profile.json`)

```bash
py-spy record -o profile.json -- python cpu_worker.py --duration 10
```

This produces a JSON file in the speedscope format. I opened it by dragging it into speedscope.app. The UI gives three views:
- Time order — a left-to-right flamechart that shows when each function was on-CPU
- Left-heavy — same as the flamegraph but sorted by sample count
- Sandwich — aggregate frame costs in a table

The time-order view was useful for seeing that `do_math` and `do_strings` ran in sequence — my script calls them one after another, but py-spy's sampling blurred the boundary in the SVG. Speedscope made it visible.

**What tripped me up:** you need a browser or separate viewer. The file was ~90 KB — smaller than the SVG, which surprised me.

## Raw JSON (`-o raw.json --format raw`)

```bash
py-spy record -o raw.json --format raw -- python cpu_worker.py --duration 10
```

This dumps an array of samples, each with a `time` field and a `stack` array from leaf to root. Example:

```json
[
  {"time": 0.5, "stack": ["do_math", "<module>"]},
  {"time": 0.7, "stack": ["do_strings", "<module>"]}
]
```

I could parse this myself with a small Python script — count frame frequency, compute wall-time estimates, filter by function name. The raw format is the most flexible but also the most work.

**What tripped me up:** after a few seconds the stack arrays get long because py-spy includes internal Python frames. I had to filter out `<frozen importlib>` and similar noise. At ~50 KB for 10 seconds, it's the smallest format.

## Which format I'm sticking with

Speedscope JSON is my default now. It gives me both the flamegraph overview AND a timeline view in one file. I'll use raw JSON only if I need custom analysis, and SVG only for quick slack shares where the recipient doesn't want to open a browser.

## What I'd try next

Run `py-spy record` against a real pytest run to find the slowest tests, using speedscope JSON so I can see test execution order. Also curious how the `--subprocesses` flag affects multi-process output.
