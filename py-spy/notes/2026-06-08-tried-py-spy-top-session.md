# First py-spy top session — what tripped me up

> These are my scratchy first-run notes. No polish, just what happened.

Installed py-spy with pip just to try it. Then I launched a tiny CPU loop in the background and attached `py-spy top --pid` to it.

First surprise: `py-spy top` without `--pid` doesn't default to the only Python process on my system — it just prints nothing unless I explicitly pass `--pid <PID>`. I ran `py-spy top` and stared at the terminal for ten seconds wondering why nothing happened. The help text mentions `--pid`, but I expected it to auto-pick the active process. That's not how it works.

I also tripped over needing `sudo`. Even though the script was running under my own user, `py-spy top --pid <PID>` refused with a permission error until I ran it via sudo. The error message said "Permission Denied" with no hint about re-running with elevated privileges, so I assumed my install was broken. Five minutes of reading the readme later: py-spy needs elevated permissions on Linux to read another process's memory via process-vm-readv. Doing `sudo py-spy top --pid <PID>` worked immediately after that.

Cols confused me first because I didn't know what "own" vs "total" time meant. OWN is the time spent inside the function itself; TOTAL includes time spent in subfunctions it called. So a recursive function that just calls itself would show OWN = tiny and TOTAL = huge. I kept reading the numbers upside down.

The `--rate` flag lets me dial the sample rate up or down. Default is 100 Hz. I tried `--rate 1000` to get faster updates in `top` mode and watched the ` Own Time` column jump around like crazy; at high sample rates the stats are noisier. Default 100 is fine.

`--` separator broke me once when I wanted to profile a script with its own args. I typed `py-spy top -- python myscript.py --arg val` and got an "unrecognized arguments" error. I had placed `--pid` and the script in the same invocation. The trick: only use `--` when you launch the target with py-spy, e.g. `py-spy top -- python myscript.py --arg val` works; don't mix with `--pid`.

One last gotcha: the `top` view updates every second by default and only shows the union of sampled stacks while it's running. If your process sleeps most of the time it looks like nothing is using CPU, which is accurate but underwhelming.

Key flags that mattered to me: `--pid`, `--rate`, `--`, `--native` to see C extension frames.
