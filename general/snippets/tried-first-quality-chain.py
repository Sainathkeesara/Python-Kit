#!/usr/bin/env python3
"""Run Ruff, mypy, and pytest in sequence. Stop if any step fails."""

import subprocess
import sys

CHECKS = [
    ("ruff check .", "Ruff linting failed"),
    ("mypy .", "mypy type check failed"),
    ("pytest", "pytest tests failed"),
]

for cmd, fail_msg in CHECKS:
    # TODO: might want to pass --fix to ruff at some point
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(fail_msg, file=sys.stderr)
        sys.exit(result.returncode)

print("All quality checks passed")
