# Compared py-spy record output formats

I already knew py-spy could dump a flamegraph SVG, but today I tried all three `record` output formats side by side: flamegraph (`-o flame.svg`), speedscope (`-o profile.json`), and raw JSON (`-o raw.json --format raw`). Here's what I found.

## Flamegraph SVG (`-o file.svg`)

The default. I ran:

```bash
py-spy record -o flame.svg -- python cpu_worker.py --duration 10
```

The SVG is a self-contained interactive viewer — opened in Firefox, hovered over frames, zoomed into regions. The visual hierarchy makes it easy to spot the hot path. `do_math` was the widest top-level frame, which matched what I expected.

**Downside:** the SVG doesn't preserve per-sample timing. You get aggregate sample counts per frame, but can't drill into individual samples. Also the SVG file was ~120 KB for a 10-second trace, which is manageable.

## Speedscope JSON (`-o profile.json`)

This time I used:

```bash
py-spy record -o profile.json -- python cpu_worker.py --duration 10
```

This outputs a JSON file in the speedscope format. I opened it in the speedscope web app (https://www.speedscope.app/) — drag-and-drop the file. The UI gives you three views: time order (left-to-right flamechart), left-heavy (same as flamegraph but sorted), and sandwich (aggregate by function).

Speedscope's "time order" view was useful for seeing when `do_math` vs `do_strings` ran — they alternated since my script calls them in sequence, but py-spy sampling meant the samples blurred across calls. Still, the visual separation was better than the SVG for understanding execution flow over time.

**Downside:** need a browser/separate tool to view it. The file was ~90 KB for 10 seconds.

## Raw JSON (`-o raw.json --format raw`)

```bash
py-spy record -o raw.json --format raw -- python cpu_worker.py --duration 10
```

This dumps samples as a JSON array of stack traces. Each entry has a `time` in seconds and a `stack` array of function names from leaf to root.

```json
[
  {
    "time": 0.5,
    "stack": ["do_math", "<module>"]
  },
  {
    "time": 0.7,
    "stack": ["do_strings", "<module>"]
  }
]
```

I could parse this myself — count frame frequency, compute wall-time estimates, filter by function. The raw format is useful if I want to build a custom visualization or integrate with another tool. At ~50 KB for 10 seconds it's the smallest of the three.

**Downside:** no built-in visualization. You need to process it yourself.

## What I'd do differently

The speedscope format is the most versatile — speedscope.app shows both aggregate flamegraph and timeline views. I'll use `-o profile.json` as my default going forward, and only drop to raw JSON if I need custom analysis. The SVG is fine for quick sharing but limited.

What I want to try next: running py-spy record on a real pytest run to see which tests are slowest.
