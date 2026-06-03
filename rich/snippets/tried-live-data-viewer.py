# Live data viewer with Rich: Layout + Table + Live display
# Simulates a process monitor that updates every second

from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
from time import sleep

console = Console()

def make_table(iteration):
    table = Table(title=f"Process Snapshot — Iteration {iteration}")
    table.add_column("PID", style="cyan", justify="right")
    table.add_column("Name", style="magenta")
    table.add_column("CPU%", justify="right")
    table.add_column("Memory MB", justify="right")

    # Simulated process data — in a real tool this would come from psutil or similar
    processes = [
        ("1024", "python", "14.2", "85.3"),
        ("2048", "node", "8.7", "120.1"),
        ("3072", "nginx", "2.1", "45.6"),
        ("4096", "postgres", "5.4", "210.0"),
    ]
    for pid, name, cpu, mem in processes:
        table.add_row(pid, name, cpu, mem)
    return table

def make_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )
    layout["header"].update(
        Panel(Text("Live Process Monitor", style="bold white on blue"), style="bold")
    )
    layout["footer"].update(
        Panel(f"Press Ctrl+C to exit | Last updated: {datetime.now():%H:%M:%S}")
    )
    return layout

# Layout and Live context manager — Live re-renders the whole layout on each loop
layout = make_layout()
iteration = 0
with Live(layout, refresh_per_second=2, screen=True):
    try:
        while True:
            iteration += 1
            table = make_table(iteration)
            layout["body"].update(table)
            layout["footer"].update(
                Panel(f"Press Ctrl+C to exit | Last updated: {datetime.now():%H:%M:%S}")
            )
            sleep(1)
    except KeyboardInterrupt:
        console.print("[bold yellow]Monitoring stopped.[/]")
