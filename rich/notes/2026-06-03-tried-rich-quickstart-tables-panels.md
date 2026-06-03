# Tried the Rich quickstart — tables, panels, and layout

I followed the official Rich quickstart to build formatted terminal output with tables and panels. Already had Rich installed from previous sessions, so I jumped straight into the code.

## Following the quickstart

The quickstart starts with `Console` — that's the main object. You import it and use `.print()` instead of Python's built-in `print()`:

```python
from rich.console import Console
console = Console()
console.print("Hello, [bold green]Rich[/bold green]!")
```

The inline markup syntax (`[bold green]...[/bold green]`) was new to me — it's like BBCode. You can nest styles, which is cleaner than f-string formatting for terminal output.

## Tables

Next I tried `Table`. You create one, add columns, add rows, and print it:

```python
from rich.table import Table

table = Table(title="Processes")
table.add_column("PID", style="cyan", justify="right")
table.add_column("Name", style="magenta")
table.add_column("CPU%", justify="right")
table.add_row("1234", "python", "12.5")
table.add_row("5678", "node", "8.2")
console.print(table)
```

The output is a properly aligned table with borders and colored columns. I liked that you can set per-column justification and style without post-processing.

## Panels

Panels wrap content in a bordered box with an optional title:

```python
from rich.panel import Panel

panel = Panel("This is inside the panel", title="Status")
console.print(panel)
```

You can nest panels inside each other, or put a Table inside a Panel for a framed look.

## Layout

The `Layout` class splits the terminal into regions. I haven't used it much yet but the quickstart shows how to define a header-body-footer split:

```python
from rich.layout import Layout
layout = Layout()
layout.split_column(
    Layout(name="header", size=3),
    Layout(name="body"),
    Layout(name="footer", size=3),
)
```

This didn't print anything on its own — you have to assign renderables to each named section and then print the layout. Took me a minute to realize that.

## Got stuck on

- **Layout is not auto-displaying.** I expected `layout.split_column(...)` to immediately show something. It just sets up the structure. You have to assign content to each piece and then `console.print(layout)`.
- **Inline markup vs `Style` objects.** The quickstart uses both `"[bold red]text[/]"` and `Style(color="red", bold=True)`. I kept mixing them up. The inline syntax is faster for quick things; Style objects are better when you reuse the same style across multiple prints.
- **Table columns don't resize dynamically mid-output.** If you print a table once, then print a wider one, the first table's column widths are locked. Makes sense — it's not a spreadsheet — but caught me off guard.

## What I'd try next

I want to combine tables with `Live` display so the table updates in place as data changes — like a real-time dashboard. That seems like the most practical use case for Rich in day-to-day dev work.
