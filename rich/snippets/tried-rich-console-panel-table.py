from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

table = Table(title="Languages")
table.add_column("Name", style="cyan")
table.add_column("Paradigm", style="magenta")
table.add_row("Python", "multi-paradigm")
table.add_row("Haskell", "functional")

panel = Panel(
    Text("Hello from rich!", style="bold green"),
    title="Greeting",
)

console.print(table)
console.print(panel)
