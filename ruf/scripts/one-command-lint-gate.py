# last_verified: 2026-09-13 · ruff n/a

"""One-command lint gate: ruff check + ruff format check + per-file ignores.

Runs ruff check with a selected ruleset, verifies formatting, and applies
per-file ignores for test files and init modules. Exits non-zero on any
violation — suitable as a CI pre-merge gate or local pre-commit hook.

Usage:
    python one-command-lint-gate.py [path ...]

If no paths are given, checks the current directory.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# --- Ruleset selection -------------------------------------------------------

SELECT: list[str] = ["E", "W", "F", "I"]

# Per-file ignores — tests need S101 (assert), init files need F401 (re-exports)
PER_FILE_IGNORES: dict[str, list[str]] = {
    "tests/**": ["S101"],
    "**/test_*.py": ["S101"],
    "**/__init__.py": ["F401"],
}


def run_ruff_check(paths: list[str]) -> int:
    """Run ruff check with selected rules and per-file ignores."""
    cmd = [sys.executable, "-m", "ruff", "check", "--select", ",".join(SELECT)]

    for pattern, codes in PER_FILE_IGNORES.items():
        cmd.extend(["--per-file-ignores", f"{pattern}:{','.join(codes)}"])

    cmd.extend(paths)
    print(f":: ruff check --select {','.join(SELECT)}")
    result = subprocess.run(cmd, check=False)
    return result.returncode


def run_ruff_format_check(paths: list[str]) -> int:
    """Verify formatting without modifying files."""
    cmd = [sys.executable, "-m", "ruff", "format", "--check"]
    cmd.extend(paths)
    print(":: ruff format --check")
    result = subprocess.run(cmd, check=False)
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    paths = argv[1:] if argv and len(argv) > 1 else ["."]
    paths = [p for p in paths if Path(p).exists()]
    if not paths:
        print("No valid paths to check.", file=sys.stderr)
        return 1

    check_rc = run_ruff_check(paths)
    format_rc = run_ruff_format_check(paths)

    if check_rc == 0 and format_rc == 0:
        print("\nAll checks passed.")
        return 0

    parts = []
    if check_rc != 0:
        parts.append("ruff check")
    if format_rc != 0:
        parts.append("ruff format")
    print(f"\nGate failed: {', '.join(parts)} returned non-zero.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
