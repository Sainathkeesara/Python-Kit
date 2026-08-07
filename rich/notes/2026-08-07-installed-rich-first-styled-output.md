---
last_verified: 2026-08-07
tool_version: n/a
---

# Installed Rich and made my first styled console output

> First try: `pip install rich`, three lines of Python, color in the terminal.

## Install

```bash
pip install rich
```

No config step — it just works once it's in.

## First styled output

```python
from rich.console import Console
console = Console()
console.print("[bold red]hello world[/bold red]")
```

Ran it and got bold red "hello world" in my terminal. That's the whole win.

The thing that caught me: Rich's inline markup `[bold red]...[/bold red]` needs every tag closed. I wrote `[bold red]oops` and the terminal printed the raw `[bold red]` text — no error, just literal brackets. I closed the tag and it styled correctly. It's like HTML, but an unclosed tag doesn't warn, it just falls through.

That's all — no tables, no panels, no progress bar. Just `console.print(...)` with a style string. Feels like the smallest possible step up from `print()`.

## What I'd try next

A `Table` for structured rows, then a `Progress` bar via `track()` to see how much nicer this is than hand-rolling spinners.
