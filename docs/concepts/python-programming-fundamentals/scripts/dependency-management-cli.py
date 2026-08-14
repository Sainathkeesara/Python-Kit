# last_verified: 2026-08-14 · Python 3.x

"""
dependency-management-cli.py
Pattern: fundamentals + dependency management in a stdlib CLI

This script demonstrates how Python fundamentals — functions, dicts,
file I/O, error handling, and argparse — combine to build a small
dependency-management tool using only the standard library.

Subcommands
-----------
list        Show every entry recorded in the local manifest.
add <pkg>  Record a package name (and optional version) in the manifest.
remove <pkg>  Delete a package entry from the manifest.
check <pkg>   Report whether a package is present and its recorded version.
init     Create a blank manifest file if one does not already exist.

The manifest is a plain JSON file (DEPENDENCIES.json by default) so it
can be version-controlled alongside source code and inspected without
any special tooling.
"""

import argparse
import json
import sys

try:
    from importlib.metadata import version as pkg_version, PackageNotFoundError
except ImportError:
    pkg_version = None
    PackageNotFoundError = Exception

MANIFEST_PATH = "DEPENDENCIES.json"


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------

def load_manifest() -> dict[str, dict]:
    """Return the manifest as a dict keyed by package name.

    An empty dict is returned when the file does not yet exist so callers
    do not need to special-case first-run scenarios.
    """
    try:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        print(f"error: manifest is corrupted — {exc}", file=sys.stderr)
        sys.exit(1)


def save_manifest(manifest: dict[str, dict]) -> None:
    """Write *manifest* to disk as pretty-printed JSON."""
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")


# ---------------------------------------------------------------------------
# Subcommand handlers
# ---------------------------------------------------------------------------

def cmd_init(_: argparse.Namespace) -> None:
    """Create an empty manifest if one is not already present."""
    import os

    if os.path.exists(MANIFEST_PATH):
        print(f"init: manifest already exists at {MANIFEST_PATH}")
        return

    save_manifest({})
    print(f"init: created blank manifest at {MANIFEST_PATH}")


def cmd_list(_: argparse.Namespace) -> None:
    """Print every package currently recorded in the manifest."""
    manifest = load_manifest()

    if not manifest:
        print("list: manifest is empty — run `add <pkg>` to record entries")
        return

    print(f"{'Package':<30} {'Version':<15} {'Source'}")
    print("-" * 60)
    for name, info in manifest.items():
        ver = info.get("version", "unknown")
        src = info.get("source", "manual")
        print(f"{name:<30} {ver:<15} {src}")


def cmd_add(args: argparse.Namespace) -> None:
    """Add *args.package* to the manifest.

    When --version is omitted the script attempts to read the installed
    version via importlib.metadata; if that fails the version is stored
    as "unknown" so the entry is still useful for tracking purposes.
    """
    manifest = load_manifest()
    name = args.package.lower()

    if name in manifest:
        print(f"add: '{name}' is already recorded (version {manifest[name].get('version')})")
        return

    version = args.version
    if version is None:
        if pkg_version is not None:
            try:
                version = pkg_version(name)
            except PackageNotFoundError:
                version = "unknown"
        else:
            version = "unknown"

    manifest[name] = {
        "version": version,
        "source": "importlib" if version != "unknown" else "manual",
    }
    save_manifest(manifest)
    print(f"add: recorded {name}=={version}")


def cmd_remove(args: argparse.Namespace) -> None:
    """Remove *args.package* from the manifest if it exists."""
    manifest = load_manifest()
    name = args.package.lower()

    if name not in manifest:
        print(f"remove: '{name}' is not in the manifest — nothing to do")
        return

    del manifest[name]
    save_manifest(manifest)
    print(f"remove: '{name}' deleted from manifest")


def cmd_check(args: argparse.Namespace) -> None:
    """Report whether *args.package* appears in the manifest."""
    manifest = load_manifest()
    name = args.package.lower()

    if name not in manifest:
        print(f"check: '{name}' — NOT recorded")
        sys.exit(1)

    info = manifest[name]
    print(f"check: '{name}' — recorded version {info.get('version', '?')} "
          f"(source: {info.get('source', '?')})")


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="depmgr",
        description="Minimal dependency manifest manager (stdlib only)",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # init
    subparsers.add_parser("init", help="Create a blank DEPENDENCIES.json")

    # list
    subparsers.add_parser("list", help="Print every recorded package")

    # add
    add_p = subparsers.add_parser("add", help="Record a package in the manifest")
    add_p.add_argument("package", help="Package name to record")
    add_p.add_argument(
        "--version", "-V",
        default=None,
        help="Override the auto-detected version string",
    )

    # remove
    rm_p = subparsers.add_parser("remove", help="Delete a package from the manifest")
    rm_p.add_argument("package", help="Package name to remove")

    # check
    chk_p = subparsers.add_parser("check", help="Verify a package is recorded")
    chk_p.add_argument("package", help="Package name to look up")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    dispatch = {
        "init":   cmd_init,
        "list":   cmd_list,
        "add":    cmd_add,
        "remove": cmd_remove,
        "check":  cmd_check,
    }
    dispatch[args.command](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
