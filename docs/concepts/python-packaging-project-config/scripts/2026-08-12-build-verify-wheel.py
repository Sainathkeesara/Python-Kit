# last_verified: 2026-08-12 · n/a

"""
Practice: build a minimal package into a wheel and verify its contents.
I keep forgetting what files actually get packaged, so this script
creates a temp package, builds it, and prints the wheel manifest.
"""

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def create_temp_package(tmp: Path) -> None:
    """Write the smallest PEP 621 package I can think of."""
    (tmp / "demo_pkg").mkdir()
    (tmp / "demo_pkg" / "__init__.py").write_text("__version__ = '0.1.0'\n")
    (tmp / "pyproject.toml").write_text("""
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "demo-pkg"
version = "0.1.0"
description = "A tiny practice package"
""")


def build_wheel(srcdir: Path, outdir: Path) -> Path | None:
    """Run the build and return the first .whl found."""
    outdir.mkdir(exist_ok=True)
    result = subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--outdir", str(outdir)],
        cwd=srcdir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Build failed:\n{result.stderr}", file=sys.stderr)
        return None
    wheels = sorted(outdir.glob("*.whl"))
    return wheels[0] if wheels else None


def verify_wheel(wheel: Path) -> None:
    """A wheel is just a zip — list its files and check for __init__."""
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
        print(f"Wheel: {wheel.name} ({len(names)} entries)")
        for n in names:
            print(f"  {n}")
        assert any("demo_pkg/__init__.py" in n for n in names), "Missing package code!"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        srcdir = Path(td)
        create_temp_package(srcdir)
        wheel = build_wheel(srcdir, srcdir / "dist")
        if wheel:
            verify_wheel(wheel)
            print("OK: package built and verified.")
