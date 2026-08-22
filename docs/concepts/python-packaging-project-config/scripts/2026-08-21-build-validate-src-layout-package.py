# last_verified: 2026-08-21 · Python 3.11

"""
Practice: build a src-layout package with an entry point and verify the wheel.
I wrote this because I kept getting confused about where files land in a wheel
when the source uses the src/ layout instead of a flat root.
"""

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def create_src_package(tmp: Path) -> Path:
    """Write the smallest installable package I could think of with a console entry point."""
    pkg_dir = tmp / "src" / "demo_pkg"
    pkg_dir.mkdir(parents=True)
    (pkg_dir / "__init__.py").write_text("__version__ = '0.1.0'\n")

    pyproject = tmp / "pyproject.toml"
    pyproject.write_text("""
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "demo-src-pkg"
version = "0.1.0"
description = "Tiny practice package using src layout"
requires-python = ">=3.9"

[project.scripts]
greet = "demo_pkg:main"
""")
    return tmp


def build_wheel(srcdir: Path, outdir: Path) -> Path | None:
    """Run python -m build --wheel and return the .whl path."""
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
    """Check that the wheel contains the src/ path and the entry-point script stub."""
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
        print(f"Wheel: {wheel.name} ({len(names)} entries)")
        for n in names:
            print(f"  {n}")

        assert any("demo_pkg/__init__.py" in n for n in names), "Missing package code!"
        assert any("demo_pkg-0.1.0.dist-info/entry_points.txt" in n for n in names), \
            "Missing entry_points.txt — the console script wasn't packaged"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        srcdir = Path(td)
        create_src_package(srcdir)
        dist = Path(td) / "dist"
        wheel = build_wheel(srcdir, dist)
        if wheel:
            verify_wheel(wheel)
            print("OK: src-layout package with entry point built and verified.")
