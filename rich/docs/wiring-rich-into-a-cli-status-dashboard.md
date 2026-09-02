---
last_verified: 2026-09-02
tool_version: n/a
sources:
---

# Wiring Rich into a CLI status dashboard with Console + Panel + Layout

## Purpose
A small status dashboard is one of the most useful patterns you can build with Rich — a single Live render area that updates on a timer, split into a header, body, and footer with `Layout`. This doc covers the assembly: a `Console` for output routing, `Panel` for bordered content blocks, `Layout` (with `Live`) for the refresh loop, and `Table` for tabular data inside the body. It assumes you want a terminal app that feels responsive without redrawing the entire screen by hand.

## When to use
Use this pattern for anything that needs to update in place: a long-running job with a progress summary, a queue monitor, a deployment watch, a multi-process supervisor. If you only need one print per event, plain `console.print()` is simpler. If you need a full-screen TUIs with menus, look at Textual instead.

## Prerequisites
- Python 3.9 or newer (Rich uses `Live` and `Layout` from the standard top-level imports).
- Rich installed in the active environment (`pip install rich` or `uv add rich`).
- A terminal that supports basic cursor movement. `Live` will degrade gracefully on dumb terminals but the refresh effect requires a real TTY.

## Assembling the pieces
The building blocks you compose are:

- **`Console`** — the output target. One `Console` instance per app; pass `file=sys.stdout` for explicit routing.
- **`Panel`** — a bordered box around any renderable. `Panel(content, title="...", border_style="...")` wraps text, a `Table`, or another `Layout`.
- **`Layout`** — a container that divides the screen into named regions (`header`, `body`, `footer`). `Layout.split_column(...)` and `Layout.split_row(...)` are the two structural methods.
- **`Table`** — tabular data with box-drawing borders. Renderable directly, or wrapped in a `Panel`.
- **`Live`** — a context manager that re-renders a renderable on a timer or on demand.

The dashboard typically builds a root `Layout` first, splits the root into header / body / footer rows, then updates each region by assigning a new renderable to the region's `update(...)` method.

## A minimal dashboard
The snippet below shows the smallest complete example: a `Console`, a `Layout` with header/body/footer, a `Table` for the body, and a `Live` loop that updates the body once a second. Drop it into `dashboard.py` and run it.

```python
# last_verified: 2026-09-02 · rich n/a
import time
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

console = Console()


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )
    layout["header"].update(Panel("Status: starting up", title="Header"))
    layout["footer"].update(Panel("Press Ctrl-C to exit", title="Footer"))
    return layout


def make_table(rows: list[tuple[str, str]]) -> Table:
    table = Table(title="Workers", expand=True)
    table.add_column("Name")
    table.add_column("State", justify="right")
    for name, state in rows:
        table.add_row(name, state)
    return table


def main() -> None:
    layout = make_layout()
    workers = [("worker-1", "idle"), ("worker-2", "idle")]
    with Live(layout, console=console, refresh_per_second=2) as live:
        for tick in range(5):
            time.sleep(1)
            workers[0] = ("worker-1", f"tick={tick}")
            layout["body"].update(Panel(make_table(workers), title="Body"))
            live.refresh()


if __name__ == "__main__":
    main()
```

The `Live` context manager owns the screen while the loop runs. `refresh_per_second=2` caps the redraw rate so a fast producer can't flood the terminal. After the loop exits (or the context unwinds on Ctrl-C), the screen returns to normal and the final state is preserved.

## Verify
Run the snippet in a real terminal window (not a captured CI log) and watch for:

1. The header row appears at the top with a border.
2. The body row contains a bordered table that updates once per second.
3. The footer row shows the exit hint.
4. Pressing Ctrl-C exits cleanly; the terminal cursor returns to a usable state.

A quick manual check is to substitute a counter for the sleep and confirm the body region updates without flicker. If you see flicker, the most common cause is mixing `Console.print` and `Live` in the same loop — let `Live` own output while it is active.

## Common errors
- **Updating the root Layout instead of a region:** assigning a new renderable to the root `Layout` wipes the split structure. Update regions by name (`layout["body"].update(...)`), not by reassigning the root.
- **`Live` outside a TTY:** `Live` will silently fall back to a non-refreshing render in CI logs. Pass `redirect_stdout=True` or write the render to a file if you need a recorded artifact for an assertion.
- **Mixing `console.print` inside a `Live` block:** stray prints fight `Live` for cursor control and produce overlapping output. Use `live.console.print(...)` if you need to log from inside the block, or buffer messages into a footer region.
- **Calling `Live.refresh()` too often:** a high `refresh_per_second` combined with a slow renderable will visibly stutter. Either throttle the producer or render a smaller body region.