# last_verified: 2026-08-07 · rich n/a

from rich.console import Console
from rich.panel import Panel

console = Console()
console.print("[bold red]Hello[/bold red] from [cyan]Rich[/cyan]!")
console.print(Panel("First styled console output", title="Rich", border_style="green"))
