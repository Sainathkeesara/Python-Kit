# last_verified: 2026-08-05 · rich n/a

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from time import sleep

console = Console()

console.print(Panel("Styled output demo", title="Rich Script", border_style="bright_blue"))

table = Table(title="Python Tools")
table.add_column("Tool", style="cyan", no_wrap=True)
table.add_column("Purpose", style="green")
table.add_column("Status", justify="center")
table.add_row("Rich", "Styled terminal output", "ready")
table.add_row("uv", "Package manager", "ready")
table.add_row("Ruff", "Linter", "ready")
console.print(table)

console.print("\n[bold]Processing steps:[/bold]")
for step in track(range(5), description="Working..."):
    sleep(0.1)

console.print("[bold green]Done![/bold green]")