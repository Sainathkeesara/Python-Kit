# Rich — quick primer

> First-day notes for someone who's never used Rich. Personal voice, plain language.

## What is it?

Rich is a Python library for making terminal output look good — colors, tables, progress bars, syntax-highlighted code, the works. If you've ever used `print()` and wished the output had some visual structure (or just wasn't a wall of monochrome text), Rich is the answer. Think of it like what Bootstrap did for HTML — not strictly necessary, but once you've used it, going back feels like a downgrade.

## What does it do?

Rich lets you render formatted text, tables, markdown, syntax-highlighted source code, tree views, progress bars, and even full terminal dashboards — all from Python. It handles colors automatically, wraps text nicely, and inspects objects better than pprint. You can `print` with it or log with it, and the output adapts to your terminal width.

## Why does it exist?

Before Rich, making a good-looking terminal app in Python meant either:
- Stringing together ANSI escape codes by hand (fragile and unreadable)
- Reaching for `curses` (powerful but painful for simple tasks)
- Just accepting ugly output

Will McGugan built Rich because he wanted a clean API for rich terminal output that Just Worked. The project blew up fast — it's now a dependency of tools like pip, pytest, and FastAPI's CLI. Day to day, library authors use it for CLI output, data scientists use it to eyeball DataFrames in the terminal, and devs use its `inspect()` as a better `dir()`.

## Key terminology

- **Console** — The main object you import (`from rich.console import Console`). Everything flows through it. Example: `console = Console(); console.print("hello", style="bold green")`.
- **Renderable** — Anything Rich knows how to display: a `Table`, a `Panel`, a `Text` object, a string. Example: passing a `Table` instance to `console.print()`.
- **Panel** — A bordered box around content. Example: `panel = Panel("inside text", title="My Box")`.
- **Table** — Lets you add columns and rows with alignment and styles. Example: `table.add_column("Name"); table.add_row("Alice")`.
- **Live** — A context manager that re-renders output in place — used for progress and real-time dashboards. Example: `with Live(table, refresh_per_second=4): ...`.
- **Progress** — A pre-built progress bar widget. Supports multiple bars, transfers with speeds, and spinners. Example: `for _ in Progress().track(range(100)): ...`.
- **Markdown** — Renders markdown text to formatted terminal output. Example: `console.print(Markdown("# Hello\n- list item"))`.
- **Syntax** — Syntax-highlights source code with a Pygments-based theme. Example: `console.print(Syntax('print("hi")', "python"))`.
- **inspect** — A drop-in replacement for `pprint` that shows type, signature, docs, and values. Example: `console.print(inspect(my_object))`.
- **Theme** — A dict mapping style names to style strings, reusable across a Console. Example: `console = Console(theme=Theme({"info": "dim cyan"}))`.

## A tiny example

```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="My Tools")
table.add_column("Tool", style="cyan")
table.add_column("Purpose", style="green")

table.add_row("uv", "Package manager")
table.add_row("Ruff", "Linter")
table.add_row("Rich", "Pretty terminal")

console.print(table)
```

This prints a bordered, color-formatted table to the terminal. The headers are bold, columns are colored, and the whole thing wraps to terminal width.

## What I'll cover next

I want to try Rich's logging handler next — hook it into a real script and see how the timestamps and levels look. After that, maybe a progress bar for a batch job and then a Markdown renderer for CLI help output.
