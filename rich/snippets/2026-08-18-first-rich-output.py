# last_verified: 2026-08-18 · rich n/a
# My first rich output: markup colors, a table, and a live display

import time
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()
console.print("[red]hello[/] [bold green]world[/]")  # markup colors

table = Table(title="Tools")
table.add_column("Tick", style="cyan")
table.add_row("0", "starting")

with Live(table, console=console):
    for i in range(6):
        table.add_row(str(i), "ok")
        time.sleep(0.2)