from rich.console import Console
from time import sleep

console = Console()

with console.status("[bold green]Working on it...", spinner="dots"):
    sleep(3)

console.print("[green]Done![/green]")
