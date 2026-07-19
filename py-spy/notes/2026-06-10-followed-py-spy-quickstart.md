# Followed the official py-spy quickstart

I walked through the py-spy quickstart from the GitHub README today. Figured I'd finally profile something properly instead of just reading about it.

## Steps I followed

Installed py-spy with `pip install py-spy` — no issues there.

Created a test script with two CPU-bound functions and a loop, basically the same one I already had in `../scripts/tried-py-spy-sampling.py`. Then ran:

```bash
py-spy record -o profile.svg -- python test_script.py
```

This ran the script under py-spy and dumped a flamegraph SVG when it finished. The SVG showed one big chunk for `do_math` and a smaller one for `do_strings` — exactly what I expected since `do_math(50000)` runs way more iterations.

Next I tried attaching to a running process. Started the script in one terminal, then in another:

```bash
py-spy record -o live.svg --pid $(pgrep -f test_script) --duration 10
```

Same result, but this time I could let the script run for longer and capture a bigger sample.

The SVG files opened fine in Firefox. Hovering over a frame shows the function name and what % of samples it appeared in. The `do_math` frame was about 60% wide, `do_strings` about 35%, and the rest was Python's main loop.

## Got stuck on

1. **PID attachment on first try.** I forgot `sudo` — py-spy needs root to read another process's memory unless you've configured `kernel.perf_event_paranoid`. Got a permission error, reran with `sudo`, worked. The quickstart mentions this but I skimmed past it.

2. **`--duration` flag placement.** I put `--duration 10` before the `-- python script.py` form and py-spy ignored it. Turns out flags before `--` apply to py-spy itself, flags after go to the Python script. Putting `-o profile.svg --duration 10 -- python script.py` worked.

3. **Flamegraph readability.** The SVG was useful but overwhelming at first — lots of tiny frames from Python internals. I had to zoom in on the relevant functions before it made sense. Next time I'll try `--native` to include C frames.

## What I'd try next

I want to profile something that's not a toy — maybe a pytest run or a small web server under load. Also want to try `py-spy top` against a multi-threaded script to see if it shows thread-level hotspots. The speedscope JSON export (`-o profile.json`) also looks worth exploring for more detailed analysis.
