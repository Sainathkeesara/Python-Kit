# last_verified: 2026-07-23 · venv concept

import os
import sys
import subprocess
import tempfile

def run(cmd, **kw):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, **kw)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def venv_practice():
    tmp = tempfile.mkdtemp(prefix="venv_practice_")
    print(f"Working in: {tmp}")

    code, out, err = run("python3 -m venv .venv", cwd=tmp)
    assert code == 0, f"venv creation failed: {err}"
    venv_python = os.path.join(tmp, ".venv", "bin", "python")
    print(f"virtual environment created: {venv_python}")

    code, out, err = run(f"{venv_python} -m pip install requests==2.32.3")
    if code != 0:
        print(f"  pip install skipped (no network): {err}")
        return
    print("installed requests==2.32.3")

    code, out, err = run(f"{venv_python} -m pip list --format=freeze", cwd=tmp)
    print("installed packages:")
    for line in out.splitlines()[:5]:
        print(f"  {line}")

    requirements_path = os.path.join(tmp, "requirements.txt")
    with open(requirements_path, "w") as fh:
        fh.write(out + "\n")
    print("requirements.txt written")

    code, _, err = run(f"{venv_python} -m pip install -r {requirements_path} --target .dep_cache", cwd=tmp)
    if code != 0:
        print(f"  deps install to .dep_cache skipped: {err}")

if __name__ == "__main__":
    venv_practice()
