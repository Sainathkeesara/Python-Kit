# last_verified: 2026-08-23 · Python 3.11

"""
Build a wheel from a src-layout package, verify its contents,
then smoke-install it into a fresh venv and confirm the import works.

This pattern closes the gap between "the wheel builds" and "the
wheel actually installs cleanly in an isolated environment."
"""

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def create_src_package(tmp: Path, backend: str = "setuptools") -> Path:
    """Write a minimal src-layout package with a __version__ attribute."""
    pkg_dir = tmp / "src" / "smoke_pkg"
    pkg_dir.mkdir(parents=True)
    (pkg_dir / "__init__.py").write_text("__version__ = '0.1.0'\n")

    backends = {
        "setuptools": (
            'requires = ["setuptools>=77.0.3", "wheel"]\n'
            'build-backend = "setuptools.build_meta"\n'
        ),
        "hatchling": (
            'requires = ["hatchling>=1.26"]\n'
            'build-backend = "hatchling.build"\n'
        ),
        "uv_build": (
            'requires = ["uv_build>=0.12.5,<0.13"]\n'
            'build-backend = "uv_build"\n'
        ),
    }
    build_system = backends.get(backend, backends["setuptools"])

    (tmp / "pyproject.toml").write_text(f"""
[build-system]
{build_system}

[project]
name = "smoke-src-pkg"
version = "0.1.0"
description = "Practice package for wheel smoke-testing"
requires-python = ">=3.11"
""")
    return tmp


def build_wheel(srcdir: Path, outdir: Path) -> Path | None:
    """Build a wheel and return the .whl path, or None on failure."""
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


def verify_wheel(wheel: Path, expected_pkg: str = "smoke_pkg") -> None:
    """Assert that the wheel contains the expected package code."""
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
        print(f"Wheel: {wheel.name} ({len(names)} entries)")
        for n in names:
            print(f"  {n}")
        assert any(f"{expected_pkg}/__init__.py" in n for n in names), (
            f"Missing {expected_pkg}/__init__.py in wheel"
        )


def smoke_test_venv(wheel: Path, venv_dir: Path) -> None:
    """Create a fresh venv, install the wheel, and confirm the import works."""
    venv_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [sys.executable, "-m", "venv", str(venv_dir)],
        check=True,
    )

    pip = venv_dir / "bin" / "pip"
    if not pip.exists():
        pip = venv_dir / "Scripts" / "pip.exe"

    result = subprocess.run(
        [str(pip), "install", "--quiet", str(wheel)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"pip install failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("Smoke install failed")

    python_exe = venv_dir / "bin" / "python"
    if not python_exe.exists():
        python_exe = venv_dir / "Scripts" / "python.exe"

    check = subprocess.run(
        [str(python_exe), "-c", "import smoke_pkg; print(smoke_pkg.__version__)"],
        capture_output=True,
        text=True,
    )
    if check.returncode != 0:
        print(f"Import check failed:\n{check.stderr}", file=sys.stderr)
        raise RuntimeError("Smoke import failed")

    print(f"Smoke test passed: {check.stdout.strip()}")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        srcdir = Path(td)
        create_src_package(srcdir)
        dist = Path(td) / "dist"
        wheel = build_wheel(srcdir, dist)
        if wheel:
            verify_wheel(wheel)
            venv = Path(td) / "smoke_venv"
            smoke_test_venv(wheel, venv)
            print("OK: wheel built, verified, and smoke-installed.")
