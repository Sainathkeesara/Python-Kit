# last_verified: 2026-08-24 · Python 3.11

"""
Build a wheel from a src layout, verify it, and smoke-install it in a fresh venv.

Building a wheel and checking its contents is only half the story —
the real test is whether the installed package actually imports and runs. This script
creates a src-layout package with a console entry point, builds the wheel, verifies
its contents, then creates a fresh venv, installs the wheel, and exercises both the
import and the CLI entry point to confirm the package works end-to-end.

Uses build-backend versions verified against research.md (2026-08-24):
- setuptools 77.0.3
- hatchling 1.27.0
- uv-build 0.7.19
"""

import subprocess
import sys
import tempfile
import venv
import zipfile
from pathlib import Path


def create_src_package(tmp: Path) -> Path:
    """Write a minimal src-layout package with a console entry point."""
    pkg_dir = tmp / "src" / "greeter_pkg"
    pkg_dir.mkdir(parents=True)
    (pkg_dir / "__init__.py").write_text("__version__ = '0.1.0'\n")
    (pkg_dir / "cli.py").write_text(
        "def main() -> None:\n"
        "    print('greeter 0.1.0 says hello')\n"
    )

    pyproject = tmp / "pyproject.toml"
    pyproject.write_text("""\
[build-system]
requires = ["setuptools>=77.0.3", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "greeter-pkg"
version = "0.1.0"
description = "Tiny src-layout package for build-and-smoke-test practice"
requires-python = ">=3.11"

[project.scripts]
greeter = "greeter_pkg.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
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
    """Check that the wheel contains the package code and entry-point metadata."""
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
        print(f"Wheel: {wheel.name} ({len(names)} entries)")
        for n in names:
            print(f"  {n}")

    assert any("greeter_pkg/__init__.py" in n for n in names), \
        "Missing package code in wheel"
    assert any("greeter_pkg-0.1.0.dist-info/entry_points.txt" in n for n in names), \
        "Missing entry_points.txt — console script not packaged"


def smoke_install_wheel(wheel: Path, venv_dir: Path) -> None:
    """Create a fresh venv, install the wheel, and verify it imports and runs."""
    print(f"\nCreating fresh venv at {venv_dir}")
    venv.create(venv_dir, with_pip=True)

    pip_exe = venv_dir / "bin" / "pip"
    python_exe = venv_dir / "bin" / "python"

    print("Installing wheel into fresh venv...")
    result = subprocess.run(
        [str(pip_exe), "install", "--force-reinstall", str(wheel)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Install failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("Wheel installation failed in fresh venv")

    print("Verifying import works...")
    result = subprocess.run(
        [str(python_exe), "-c", "import greeter_pkg; print(greeter_pkg.__version__)"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Import failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("Package import failed after install")
    assert "0.1.0" in result.stdout, f"Unexpected version output: {result.stdout!r}"

    greeter_exe = venv_dir / "bin" / "greeter"
    print("Verifying console entry point works...")
    result = subprocess.run(
        [str(greeter_exe)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Entry point failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("Console entry point failed after install")
    assert "greeter 0.1.0" in result.stdout, \
        f"Unexpected entry point output: {result.stdout!r}"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        srcdir = Path(td)
        create_src_package(srcdir)

        dist = srcdir / "dist"
        wheel = build_wheel(srcdir, dist)
        if not wheel:
            sys.exit(1)

        verify_wheel(wheel)
        print("OK: wheel built and contents verified.")

        venv_dir = srcdir / "smoke_venv"
        smoke_install_wheel(wheel, venv_dir)
        print("OK: wheel smoke-installed in fresh venv — import and entry point work.")
