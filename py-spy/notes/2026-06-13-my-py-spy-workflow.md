# My py-spy workflow — record, flamegraph, top modes

I've been using py-spy for a few weeks now, and I've settled into a workflow that covers most of what I need. Here's what I actually do and what keeps tripping me up.

## record mode — my default

When I want to know where CPU time goes in a script, I reach for `record` first:

```bash
py-spy record -o flame.svg -- python my_script.py
```

This runs the script under py-spy and dumps a flamegraph SVG when it finishes. The `--duration` flag is useful if the script runs indefinitely — just cap it to 10 or 20 seconds:

```bash
py-spy record -o flame.svg --duration 15 -- python my_script.py
```

**Gotcha I keep hitting:** flags after `--` go to the Python script, not to py-spy. So `--duration` has to come before `--`, not after. I've wasted a few runs putting it in the wrong spot.

For attaching to something already running (like a web server or a long computation), I use `--pid`:

```bash
py-spy record -o flame.svg --pid $(pgrep -f my_script) --duration 10
```

This needs `sudo` unless you've tuned `kernel.perf_event_paranoid`. I always forget the first time.

## flamegraph mode — just a shortcut

`py-spy flamegraph` is basically `py-spy record -o flame.svg` under a different name. I stopped using it because `record` gives me more output format options and I want to standardize on speedscope JSON for anything non-trivial.

If I do want a flamegraph SVG fast, I use:

```bash
py-spy flamegraph -o flame.svg --pid 12345 --duration 5
```

## top mode — live monitoring

`py-spy top` gives a live-updating `htop`-style view of a running Python process. I use this when I'm iterating on performance changes and want instant feedback:

```bash
py-spy top --pid 12345
```

The default view shows function names, % of samples, and the number of samples collected. Press `?` during the session to see the keybindings — sorting by % or by function name helps a lot.

**What tripped me up:** `top` also needs root for non-child processes. And the display can be noisy if your process has a lot of internal frames — I filter with `--function` when I know which function I'm looking for.

## Output formats — what I settled on

I tried all three `record` output formats in a previous session. My take:
- **SVG** — quick share, limited analysis. I use it for a first look or to paste in a quick doc.
- **Speedscope JSON** (`-o profile.json`) — my default now. Opens in speedscope.app with timeline + flamegraph views.
- **Raw JSON** (`--format raw`) — only when I want to build a custom script to analyze the trace.

## Gotchas I still hit

1. **Permissions.** `sudo py-spy` works but then the output files are owned by root. I `chown` them after, or run the target process as root too. Not ideal.
2. **`--duration` position.** `-o file.svg --duration 10 -- python script.py` — everything before `--` is py-spy args, after is script args. Mixing them up silently misbehaves.
3. **Flamegraph noise.** Internal Python frames (gc, threading, etc.) take up a lot of space in the SVG. I zoom in on the functions I care about and ignore the rest.
4. **No thread-level separation in SVG.** The flamegraph aggregates across all threads. If I have a multi-threaded script, the SVG is a single combined view. Speedscope JSON shows per-thread timelines which is much better.

## What I'd try next

I want to profile a real pytest run next — fire up a test suite under py-spy record and find the slowest tests. Also curious about `py-spy record --subprocesses` to capture worker processes spawned by multiprocessing.
