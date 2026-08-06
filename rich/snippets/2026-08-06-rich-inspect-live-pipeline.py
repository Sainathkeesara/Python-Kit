# last_verified: 2026-08-06 · rich n/a
# What I learned using Rich's inspect() and live display on a sample data pipeline

from rich.console import Console
from rich.inspect import Inspect
from rich.live import Live
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()


def inspect_data(record):
    # Using Rich's inspect() to dump a dict's structure — great for seeing
    # what fields are actually present when the pipeline schema shifts
    console.print(Inspect(record, methods=False, private=False, title="Pipeline Record"))


def run_pipeline():
    # Simulated data pipeline: generate records, inspect one, show progress
    records = [
        {"id": 1, "name": "alpha", "value": 42, "tags": ["a", "b"]},
        {"id": 2, "name": "beta", "value": 17, "tags": ["c"]},
        {"id": 3, "name": "gamma", "value": 89, "tags": ["a", "c", "d"]},
    ]

    # Inspect the first record so I can see the shape before processing
    inspect_data(records[0])

    # Live progress display while the pipeline processes records
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Processing pipeline records...", total=len(records))
        for record in records:
            time.sleep(0.3)  # simulate work
            progress.update(task, advance=1)

    # Show a summary table of what the pipeline produced
    table = Table(title="Pipeline Summary")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Value", justify="right")
    table.add_column("Tags", style="green")

    for r in records:
        table.add_row(str(r["id"]), r["name"], str(r["value"]), ", ".join(r["tags"]))

    console.print(table)


if __name__ == "__main__":
    run_pipeline()