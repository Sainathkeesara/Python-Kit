#!/usr/bin/env python3
# last_verified: 2026-08-17 · venv concept (stdlib)

"""
Lockfile drift check.

Watches for the reproducibility failure behind most venv problems: a lockfile
that pins one version of a package while the active environment carries a
different one. The check reads a lockfile, reads the installed environment, and
reports the difference.

This joins three ideas from the Virtual Environment & Dependency Mgmt concept:
  1. a lockfile is the source of truth (name==version, one pin per line)
  2. importlib.metadata reads the *active* environment's installed packages
  3. drift is just a set difference — missing, version-mismatch, extra

Usage:
  python3 lockfile-drift-check.py requirements.lock
  python3 lockfile-drift-check.py requirements.lock --strict   # exit 1 on drift
  python3 lockfile-drift-check.py requirements.lock --freeze   # show installed set first

Exit status:
  0 — environment matches the lockfile (no drift)
  1 — drift found and --strict was given
  2 — usage error (lockfile unreadable or malformed)
"""

import argparse
import sys
from importlib import metadata


def parse_lock(lock_path):
    """Return {name: pinned_version} from a name==version lockfile."""
    pins = {}
    try:
        with open(lock_path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        print(f"could not read lockfile {lock_path}: {exc}", file=sys.stderr)
        return None

    for lineno, raw in enumerate(lines, 1):
        line = raw.split("#", 1)[0].strip()          # drop inline comments
        if not line or "==" not in line:
            continue                                  # skip blanks + extras
        name, _, version = line.partition("==")
        pins.setdefault(name.strip().lower(), version.strip())
    return pins


def installed_set():
    """Return {name: installed_version} for the active environment."""
    found = {}
    for dist in metadata.distributions():
        name = (dist.metadata.get("Name") or "").strip().lower()
        if name:
            found[name] = dist.version
    return found


def compare(pins, installed):
    missing = sorted(name for name in pins if name not in installed)
    mismatched = sorted(
        name for name in pins
        if name in installed and installed[name] != pins[name]
    )
    extra = sorted(name for name in installed if name not in pins)
    return missing, mismatched, extra


def main():
    parser = argparse.ArgumentParser(description="venv vs lockfile drift detection")
    parser.add_argument("lockfile", nargs="?", default="requirements.lock")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when drift is found (CI-style gating)")
    parser.add_argument("--freeze", action="store_true",
                        help="print the installed environment before comparing")
    args = parser.parse_args()

    pins = parse_lock(args.lockfile)
    if pins is None:
        return 2
    print(f"lockfile: {args.lockfile} ({len(pins)} pins)")

    installed = installed_set()
    if args.freeze:
        print("installed:")
        for name in sorted(installed):
            print(f"  {name}=={installed[name]}")

    missing, mismatched, extra = compare(pins, installed)

    for name in mismatched:
        print(f"DRIFT: {name} installed=={installed[name]} but lockfile pins {pins[name]}")
    for name in missing:
        print(f"DRIFT: {name} missing from environment (lockfile pins {pins[name]})")
    if extra and args.freeze:
        print(f"{len(extra)} packages installed that the lockfile does not pin "
              f"(top 5): {', '.join(extra[:5])}")

    drift_count = len(missing) + len(mismatched)
    if drift_count == 0:
        print("in sync: environment matches the lockfile")
        return 0
    print(f"drift detected: {len(missing)} missing, "
          f"{len(mismatched)} version mismatch(es)")
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())