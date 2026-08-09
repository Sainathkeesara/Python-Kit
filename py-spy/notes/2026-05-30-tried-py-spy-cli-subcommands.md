# Tried py-spy CLI subcommands: record, top, flamegraph

I ran my sampling target script (`../scripts/tried-py-spy-sampling.py`) in one terminal, then played with py-spy's three main subcommands in another.

## `py-spy top`

`py-spy top --pid <PID>` gives a live-updating terminal view sorted by % of samples. The hottest function showed up first — in my case `do_math` consistently took ~60% of samples, `do_strings` ~35%, and the `time.sleep` was invisible (py-spy ignores idle time by default). Press `q` to quit.

It refreshes every few hundred ms and feels responsive even on a busy process.

## `py-spy record`

`py-spy record -o profile.json --pid <PID> --duration 5` writes raw samples to a JSON file. Each sample is a list of stack frames. I could parse this myself if I wanted, but the main use is feeding it to the flamegraph subcommand.

Without `--duration` it runs until you Ctrl+C, which is handy for longer profiling sessions.

## `py-spy flamegraph` (built into `record`)

Actually, you don't need a separate flamegraph subcommand — `py-spy record -o flame.svg ...` produces the SVG directly. The flamegraph is a stacked bar chart where each row is a stack frame level, wider blocks mean more samples. Hovering shows the function name and sample count.

I tried `py-spy record -o flame.svg --pid <PID> --duration 10` and opened the SVG in a browser. It clearly showed `do_math` as the widest block at the top level.

## What I noticed

- All three subcommands need either `--pid` or you can prepend `py-spy record ... -- python script.py`.
- The overhead was barely noticeable — the target script didn't slow down.
- py-spy includes Python frames only by default; `--native` adds C extension frames.
