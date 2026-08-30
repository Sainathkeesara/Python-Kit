# last_verified: 2026-08-30 · rich n/a

import sys
import time
from collections import deque
from datetime import datetime

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

SEVERITY_STYLES = {
    "INFO": "dim cyan",
    "WARN": "yellow",
    "ERROR": "bold red",
}


def generate_logs(total=120, delay=0.05):
    """Yield timestamped log lines with alternating severities."""
    severities = ["INFO", "WARN", "ERROR"]
    for i in range(total):
        if i % 11 == 0:
            sev = "ERROR"
        elif i % 7 == 0:
            sev = "WARN"
        else:
            sev = "INFO"
        yield f"{datetime.now().strftime('%H:%M:%S')} [{sev}] log line {i}"
        time.sleep(delay)


def build_layout(scrollback):
    """Assemble a Layout with header, scrollback body, and footer."""
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["header"].update(Panel("Live Log Tailer", style="bold white on blue"))
    body_lines = "\n".join(str(line) for line in scrollback)
    layout["body"].update(
        Panel(body_lines, title=f"Scrollback ({len(scrollback)} lines)", border_style="blue")
    )
    layout["footer"].update(Panel("Press Ctrl+C to stop", style="dim"))
    return layout


def tail_live(max_lines=20, total_logs=120, delay=0.05):
    """Stream log lines into a fixed-size scrollback buffer rendered with Live."""
    scrollback = deque(maxlen=max_lines)
    console = Console()
    try:
        with Live(
            build_layout(scrollback),
            console=console,
            refresh_per_second=4,
            screen=False,
        ) as live:
            for line in generate_logs(total=total_logs, delay=delay):
                sev = line.split("[")[1].split("]")[0]
                styled = Text(line, style=SEVERITY_STYLES.get(sev, ""))
                scrollback.append(styled)
                live.update(build_layout(scrollback))
    except KeyboardInterrupt:
        console.print("\n[bold red]Stopped.[/bold red]")
        sys.exit(0)


if __name__ == "__main__":
    tail_live()
