#!/usr/bin/env python3
# last_verified: 2026-09-03 · ruff 0.8.0

"""
One-command lint gate for Ruff.

Combines ruff check (with configurable rules), format check,
and per-file ignore handling into a single Python wrapper.

Usage:
    python ruff-lint-gate.py [directory]
    python ruff-lint-gate.py --config pyproject.toml
    python ruff-lint-gate.py --select E,F,W --ignore E501
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Optional


def run_ruff_check(
    target: str,
    select: list[str],
    ignore: list[str],
    per_file_ignores: dict[str, list[str]],
    config: Optional[str] = None,
) -> tuple[int, str]:
    """Run ruff check with specified rules and per-file ignores."""
    cmd = ["ruff", "check", target]

    if select:
        cmd.extend(["--select", ",".join(select)])

    if ignore:
        cmd.extend(["--ignore", ",".join(ignore)])

    if per_file_ignores:
        for pattern, rules in per_file_ignores.items():
            cmd.extend(["--per-file-ignores", f"{pattern}:{','.join(rules)}"])

    if config:
        cmd.extend(["--config", config])

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def run_ruff_format_check(
    target: str, config: Optional[str] = None
) -> tuple[int, str]:
    """Run ruff format check."""
    cmd = ["ruff", "format", "--check", target]

    if config:
        cmd.extend(["--config", config])

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def main() -> int:
    parser = argparse.ArgumentParser(
        description="One-command Ruff lint gate: check + format + per-file ignores"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Directory or file to lint (default: current directory)",
    )
    parser.add_argument(
        "--config",
        help="Path to ruff configuration file",
    )
    parser.add_argument(
        "--select",
        nargs="+",
        default=["E", "F", "W", "I"],
        help="Rule prefixes to enable (default: E F W I)",
    )
    parser.add_argument(
        "--ignore",
        nargs="+",
        default=[],
        help="Rule prefixes to ignore",
    )
    parser.add_argument(
        "--per-file-ignores",
        nargs="+",
        metavar="PATTERN:RULES",
        help="Per-file ignores in PATTERN:RULE1,RULE2 format",
    )

    args = parser.parse_args()

    # Parse per-file-ignores
    per_file_ignores: dict[str, list[str]] = {}
    if args.per_file_ignores:
        for item in args.per_file_ignores:
            if ":" in item:
                pattern, rules = item.split(":", 1)
                per_file_ignores[pattern] = rules.split(",")

    # Run ruff check
    print("=== ruff check ===")
    check_exit, check_output = run_ruff_check(
        args.target,
        args.select,
        args.ignore,
        per_file_ignores,
        args.config,
    )
    print(check_output)

    # Run format check
    print("\n=== ruff format --check ===")
    format_exit, format_output = run_ruff_format_check(args.target, args.config)
    print(format_output)

    # Summary
    print("\n=== Summary ===")
    if check_exit == 0 and format_exit == 0:
        print("✓ All checks passed")
        return 0
    else:
        failures = []
        if check_exit != 0:
            failures.append(f"ruff check failed (exit {check_exit})")
        if format_exit != 0:
            failures.append(f"ruff format check failed (exit {format_exit})")
        print(f"✗ {'; '.join(failures)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
