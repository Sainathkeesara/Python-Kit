#!/usr/bin/env python3
# last_verified: 2026-09-13 · rich n/a

"""
Multi-bar progress tracker with elapsed time and ETA.

Demonstrates Rich's Progress API for tracking multiple concurrent
long-running jobs with live elapsed/ETA display.

Usage:
    python multi-bar-progress-tracker.py [--jobs N] [--duration SECONDS]

Requires: rich (pip install rich)
"""

import argparse
import random
import time

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)


def simulate_job(name: str, total: int, speed: float) -> None:
    """Simulate a job that processes items at a variable rate."""
    for _ in range(total):
        time.sleep(random.uniform(0.01, speed))


def build_progress(console: Console) -> Progress:
    """Construct a Progress instance with multi-bar-friendly columns."""
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=30),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    )


def run_multi_bar(num_jobs: int, base_duration: float) -> None:
    """Run multiple concurrent progress bars and print a summary."""
    console = Console()
    jobs = [
        (f"Job-{i + 1}", random.randint(20, 80), random.uniform(0.02, base_duration))
        for i in range(num_jobs)
    ]

    with build_progress(console) as progress:
        tasks = [
            progress.add_task(desc, total=total) for desc, total, _ in jobs
        ]

        while not progress.finished:
            for idx, (desc, total, speed) in enumerate(jobs):
                task_id = tasks[idx]
                if not progress.tasks[task_id].finished:
                    advance = random.randint(1, max(1, total // 10))
                    progress.update(task_id, advance=min(advance, total - progress.tasks[task_id].completed))

            time.sleep(0.05)

    console.print("\n[green bold]All jobs complete.[/green bold]\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Multi-bar progress tracker demo")
    parser.add_argument("--jobs", type=int, default=4, help="Number of concurrent jobs (default: 4)")
    parser.add_argument("--duration", type=float, default=0.1, help="Base sleep duration in seconds (default: 0.1)")
    args = parser.parse_args()

    run_multi_bar(args.jobs, args.duration)


if __name__ == "__main__":
    main()
