# What tripped me up on my first py-spy top session

I ran `py-spy top --pid 12345` and immediately got "permission denied". Needed `sudo py-spy top --pid 12345` — py-spy reads `/proc/PID/mem` which needs root for processes I didn't start myself.

Once that worked, the TUI showed up but I had no idea what I was looking at. The columns are:

- **%CPU** — sample count, not wall time. Was confused why a sleep-heavy function showed 0% while a tight loop showed 90%.
- **Ownership** — each frame's % is relative to its parent, not total. I thought the numbers added wrong until I realized that.

Flag I kept forgetting:

| Flag | What it does |
|------|-------------|
| `-n` | number of samples (default 100). Crank this down to 10 for quick checks. |
| `-d` | delay between samples in seconds (default 0.1). Bump to 1 if the TUI flickers. |
| `-p` | PID to attach to. I kept passing the script name at first. |

Running `py-spy top --pid $(pgrep -f my_script.py)` saved me from looking up the PID each time.

Biggest gotcha: py-spy only sees native Python frames by default. C extensions show as `<external>` unless you pass `--native`.
