# last_verified: 2026-08-22 · tomllib (stdlib 3.11+)
"""Validate a pyproject.toml with tomllib before handing it to build tools.

I kept hitting cryptic build errors because my pyproject.toml had typos
or missing sections.  This script catches the obvious problems early —
parse errors, missing required keys, and mismatched build-backend —
so the build tool doesn't have to.

Usage:
    python validate-pyproject-tomllib.py pyproject.toml
"""

import sys
import tomllib
from pathlib import Path

REQUIRED_BUILD_SYSTEM_KEYS = {"requires", "build-backend"}
REQUIRED_PROJECT_KEYS = {"name", "version"}

BACKEND_TO_MODULE = {
    "hatchling.build": "hatchling",
    "setuptools.build_meta": "setuptools",
    "flit_core.buildapi": "flit_core",
    "pdm.backend": "pdm-backend",
    "uv_build": "uv_build",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
    except (tomllib.TOMLDecodeError, OSError) as exc:
        return [f"Cannot parse {path}: {exc}"]

    # --- [build-system] ---
    bs = data.get("build-system")
    if bs is None:
        errors.append("Missing [build-system] section")
    else:
        missing = REQUIRED_BUILD_SYSTEM_KEYS - bs.keys()
        if missing:
            errors.append(f"[build-system] missing keys: {', '.join(sorted(missing))}")

        backend = bs.get("build-backend", "")
        requires = bs.get("requires", [])
        expected_module = BACKEND_TO_MODULE.get(backend)
        if expected_module and not any(expected_module in r for r in requires):
            errors.append(
                f"build-backend '{backend}' expects '{expected_module}' in requires, "
                f"but requires = {requires}"
            )

    # --- [project] ---
    proj = data.get("project")
    if proj is None:
        errors.append("Missing [project] section")
    else:
        missing = REQUIRED_PROJECT_KEYS - proj.keys()
        if missing:
            errors.append(f"[project] missing keys: {', '.join(sorted(missing))}")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <pyproject.toml>", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    errors = validate(path)

    if errors:
        print(f"✗ {len(errors)} issue(s) in {path}:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"✓ {path} looks good")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
