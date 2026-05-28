from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from time import sleep

console = Console()

table = Table(title="Python Tools")
table.add_column("Tool", style="cyan")
table.add_column("Purpose")
table.add_row("uv", "Package manager")
table.add_row("Ruff", "Linter")
table.add_row("pytest", "Test runner")
console.print(table)

console.print(Panel("Hello from Rich!", title="Greeting"))

for step in track(range(5), description="Processing..."):
    sleep(0.2)
