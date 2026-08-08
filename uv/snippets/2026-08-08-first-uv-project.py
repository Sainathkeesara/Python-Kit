# last_verified: 2026-08-08 · uv 0.12.2
"""Walk through uv project init, dep add, and script execution.

I wanted one file that touches the whole uv project lifecycle
without leaving Python. Each step shells out to the uv CLI.
"""

import subprocess
import sys
from pathlib import Path

PROJECT = Path("mini-uv-demo")


def init_project() -> None:
    """Create a new uv project with no README boilerplate."""
    subprocess.run(
        [sys.executable, "-m", "uv", "init", str(PROJECT), "--no-readme"],
        check=True,
    )
    print(f"Project initialized at {PROJECT}/")


def add_dependency(name: str) -> None:
    """Add a dependency and let uv update the lockfile."""
    subprocess.run(
        [
            sys.executable,
            "-m",
            "uv",
            "add",
            "--directory",
            str(PROJECT),
            name,
        ],
        check=True,
    )
    print(f"Added {name}")


def write_and_run(filename: str, code: str) -> None:
    """Write a script into the project and run it via uv."""
    target = PROJECT / filename
    target.write_text(code, encoding="utf-8")
    subprocess.run(
        [sys.executable, "-m", "uv", "run", "--directory", str(PROJECT), str(target)],
        check=True,
    )


if __name__ == "__main__":
    init_project()
    add_dependency("httpx")
    write_and_run(
        "main.py",
        "import httpx\n"
        "print('httpx installed — ready for requests')\n",
    )
