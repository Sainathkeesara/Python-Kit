# last_verified: 2026-09-08 · rich n/a

"""
Multi-bar progress tracker with elapsed time and ETA.

Demonstrates Rich's Progress with multiple concurrent task bars,
per-bar elapsed time display, and a computed ETA column. Each bar
represents an independent job (simulated with sleep) running at
a different speed.

Usage:
    python 2026-09-08-multi-bar-progress-tracker.py
"""

import time
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    TaskProgressColumn,
)


def main() -> None:
    jobs = [
        ("Downloading dataset", 30, 8.0),
        ("Processing images", 20, 5.0),
        ("Uploading results", 15, 10.0),
    ]

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    ) as progress:
        tasks = [
            progress.add_task(desc, total=total, speed=speed)
            for desc, total, speed in jobs
        ]

        # All jobs run concurrently; each finishes at a different time.
        while not progress.finished:
            for i, (desc, total, speed) in enumerate(jobs):
                task = progress.tasks[tasks[i]]
                if not task.finished:
                    # Advance by one unit per tick; speed controls tick rate.
                    progress.update(tasks[i], advance=1)
                    time.sleep(1.0 / speed)


if __name__ == "__main__":
    main()
