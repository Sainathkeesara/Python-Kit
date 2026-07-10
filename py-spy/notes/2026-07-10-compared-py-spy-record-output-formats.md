---
last_verified: 2026-07-10
tool_version: n/a
---

# What I learned comparing py-spy's record output formats

I'd been using py-spy's default flamegraph output for a while, but I wanted to understand the actual difference between the three `record` output formats. Here's what I did, what broke, and what I'd try next.

## Steps I followed

I wrote a small CPU-bound script that does math and string operations in a loop, then ran `py-spy record` against it three times — once per format.

**1. Flamegraph SVG (`-o flame.svg`):**

```bash
py-spy record -o flame.svg -- python cpu_worker.py --duration 10
```

The SVG opened right in Firefox. I could hover over frames and see the function name and sample count. The widest bar was my `do_math` function — the hot path was obvious immediately. The SVG was self-contained, so I could share it as a file without extra tools.

**2. Speedscope JSON (`-o profile.json`):**

```bash
py-spy record -o profile.json -- python cpu_worker.py --duration 10
```

This produced a JSON file. I opened speedscope.app and dragged the file in. The time-order view showed something the SVG hid: my `do_math` and `do_strings` calls ran in alternating blocks, not in parallel. The SVG just showed them both as wide bars. Speedscope's timeline made the execution order visible.

**3. Raw JSON (`-o raw.json --format raw`):**

```bash
py-spy record -o raw.json --format raw -- python cpu_worker.py --duration 10
```

This dumped a JSON array of individual samples — each with a `time` field and a `stack` array. I wrote a quick Python one-liner to count which function appeared most at the top of the stack. The raw data was the smallest file (~50 KB vs ~120 KB for SVG) and the most flexible.

## Got stuck on

**Permission denied on first run.** `py-spy record` needs elevated permissions to read another process's memory. I'd forgotten to run with `sudo` when attaching to a PID directly. Using `py-spy record -- python script.py` (wrapping the target as a subprocess) avoided this — py-spy handles the permissions internally in that mode.

**Speedscope file association.** My first `py-spy record -o profile.json` didn't include `--format speedscope` explicitly. py-spy infers the format from the file extension, so `.json` defaults to speedscope format. That worked, but I wasn't sure at first — I checked `py-spy record --help` to confirm.

**Raw JSON stack noise.** The raw format includes internal Python frames like `<frozen importlib>` and `<built-in method exec>`. I had to filter those out when counting frame frequencies. A quick `grep -v frozen` in a pipe script worked for a one-off analysis.

## What I'd try next

I want to run `py-spy record --subprocesses` against a multiprocessing workload to see how speedscope handles multiple threads. Also curious how the raw JSON format changes when sampling at `--rate 1000` vs the default.
