"""Parse uv.lock and print every direct dependency with its version."""

import tomllib
import sys
from pathlib import Path


def load_lock(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def get_direct_names(lock: dict) -> set[str]:
    """Pull direct dependency names from requires-dist entries."""
    meta = lock.get("metadata", {})
    raw = meta.get("requires-dist", [])
    names = set()
    for entry in raw:
        name = entry.split()[0] if " " in entry else entry
        # strip extras markers like requests[security]
        name = name.split("[")[0]
        names.add(name)
    return names


def find_package(lock: dict, name: str) -> dict | None:
    for pkg in lock.get("package", []):
        if pkg["name"] == name:
            return pkg
    return None


def main() -> None:
    lock_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd() / "uv.lock"

    if not lock_path.exists():
        print(f"uv.lock not found at {lock_path}")
        sys.exit(1)

    lock = load_lock(lock_path)
    direct_names = get_direct_names(lock)

    if not direct_names:
        print("No direct dependencies found in uv.lock metadata.")
        return

    print(f"Direct dependencies ({len(direct_names)}):")
    print("-" * 40)
    for name in sorted(direct_names):
        pkg = find_package(lock, name)
        if pkg:
            ver = pkg.get("version", "?")
            deps = [d["name"] for d in pkg.get("dependencies", [])]
            print(f"  {name} == {ver}")
            if deps:
                print(f"      ↓ {len(deps)} transitive dep(s): {', '.join(deps[:4])}"
                      f"{'...' if len(deps) > 4 else ''}")
        else:
            print(f"  {name}  (not found in package list — possibly platform-only)")


if __name__ == "__main__":
    main()
