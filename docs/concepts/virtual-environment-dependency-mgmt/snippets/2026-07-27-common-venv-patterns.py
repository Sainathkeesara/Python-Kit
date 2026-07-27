# last_verified: 2026-07-27 · venv concept

import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: str, cwd: Path) -> tuple[int, str, str]:
    """Run a shell command and return (returncode, stdout, stderr).
    I use this wrapper instead of calling subprocess.run inline so I can
    print diagnostics in one place if something fails.
    """
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def create_venv(directory: Path) -> Path:
    """Create a virtual environment inside the given directory.
    Returns the path to the venv's Python interpreter.
    """
    venv_path = directory / ".venv"
    code, _, err = run(f"{sys.executable} -m venv {venv_path}", directory)
    if code != 0:
        raise RuntimeError(f"venv creation failed: {err}")
    python = venv_path / "bin" / "python"
    return python


def install_requirements(python: Path, requirements: Path) -> None:
    """Install dependencies from a requirements file.
    I skip the install if the file is empty or missing so the snippet
    still runs on machines without network access.
    """
    if not requirements.exists() or requirements.stat().st_size == 0:
        print("No requirements.txt to install")
        return
    code, _, err = run(f"{python} -m pip install -r {requirements}", python.parent)
    if code != 0:
        print(f"pip install skipped: {err}")


def write_requirements(directory: Path, packages: list[str]) -> Path:
    """Write a minimal requirements.txt with pinned versions.
    I pin versions because I've been bitten by floating ranges pulling
    in incompatible transitive dependencies during demos.
    """
    req = directory / "requirements.txt"
    req.write_text("\n".join(packages) + "\n")
    return req


def freeze_environment(python: Path, output: Path) -> None:
    """Capture the installed packages to a freeze file.
    This is the pattern I use to snapshot a known-good environment
    before switching branches or upgrading a dependency.
    """
    code, out, _ = run(f"{python} -m pip freeze", python.parent)
    if code == 0:
        output.write_text(out + "\n")
        print(f"Wrote {output}")


def main() -> None:
    tmp = tempfile.mkdtemp(prefix="venv_patterns_")
    root = Path(tmp)
    print(f"Working in: {root}")

    python = create_venv(root)
    print(f"Created venv: {python}")

    req_file = write_requirements(root, ["requests==2.32.3", "pydantic==2.11.3"])
    print(f"Wrote {req_file}")

    install_requirements(python, req_file)

    freeze_path = root / "pinned.txt"
    freeze_environment(python, freeze_path)


if __name__ == "__main__":
    main()
