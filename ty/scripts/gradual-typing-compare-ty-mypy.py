# last_verified: 2026-09-08 · ty n/a
"""
Gradual typing with ty: annotate a small project incrementally and compare ty vs mypy output.

Writes a mini inventory module through three annotation stages, runs ty and mypy on each
stage, and prints a side-by-side comparison of diagnostics.
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

STAGES = {
    "stage-0-untyped": '''\
def create_item(name, price, quantity):
    return {"name": name, "price": price, "quantity": quantity}

def total_value(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def discount(item, percent):
    return item["price"] * (1 - percent / 100)
''',
    "stage-1-partial": '''\
def create_item(name: str, price: float, quantity: int):
    return {"name": name, "price": price, "quantity": quantity}

def total_value(items):
    total = 0.0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def discount(item, percent):
    return item["price"] * (1 - percent / 100)
''',
    "stage-2-fully-typed": '''\
from typing import Sequence, TypedDict

class Item(TypedDict):
    name: str
    price: float
    quantity: int

def create_item(name: str, price: float, quantity: int) -> Item:
    return {"name": name, "price": price, "quantity": quantity}

def total_value(items: Sequence[Item]) -> float:
    total: float = 0.0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def discount(item: Item, percent: float) -> float:
    return item["price"] * (1 - percent / 100)
''',
}


def check_tool_available(tool: str) -> bool:
    """Return True if the type checker is on PATH."""
    return subprocess.run(["which", tool], capture_output=True).returncode == 0


def run_checker(tool: str, source: str, workdir: Path) -> tuple[int, str, str]:
    """
    Write source to workdir/module.py, run tool, and capture output.
    Returns (returncode, stdout, stderr).
    """
    target = workdir / "module.py"
    target.write_text(source, encoding="utf-8")
    try:
        proc = subprocess.run(
            [tool, str(target)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=workdir,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except FileNotFoundError:
        return 127, "", f"{tool} is not installed"
    except subprocess.TimeoutExpired:
        return 124, "", f"{tool} timed out after 30s"
    except Exception as exc:
        return 1, "", str(exc)


def summarize(tool: str, rc: int, out: str, err: str) -> list[str]:
    """Format checker output for display."""
    lines = (out or err).strip().splitlines()
    if not lines:
        return [f"  {tool} (exit {rc}): no output"]
    return [f"  {tool} (exit {rc}):"] + [f"    {line}" for line in lines[:8]]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare ty vs mypy across incremental typing stages"
    )
    parser.add_argument(
        "--tool",
        choices=["ty", "mypy", "both"],
        default="both",
        help="Which checker to run",
    )
    args = parser.parse_args()

    tools = []
    if args.tool in ("ty", "both"):
        tools.append("ty")
    if args.tool in ("mypy", "both"):
        tools.append("mypy")

    missing = [t for t in tools if not check_tool_available(t)]
    if missing:
        print(f"Missing tools: {', '.join(missing)}. Install them before running this script.")
        sys.exit(1)

    with tempfile.TemporaryDirectory(prefix="ty_compare_") as tmp:
        workdir = Path(tmp)
        print("=== Gradual typing: ty vs mypy ===\n")
        for stage_name, source in STAGES.items():
            print(f"--- {stage_name} ---")
            for tool in tools:
                rc, out, err = run_checker(tool, source, workdir)
                for line in summarize(tool, rc, out, err):
                    print(line)
            print()


if __name__ == "__main__":
    main()
