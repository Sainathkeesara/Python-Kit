"""Compare Ty vs mypy on the same typed code."""
import subprocess, sys

CODE = "def add(a: int, b: int) -> int: return a + b\nresult = add('one', 2)\n"

with open("_t.py", "w") as f:
    f.write(CODE)
for tool in ["ty", "mypy"]:
    r = subprocess.run([tool, "_t.py"], capture_output=True, text=True)
    print(f"=== {tool} ===\n{r.stdout or r.stderr}")
    print(f"Errors: {len(r.stdout.splitlines())}")
subprocess.run(["rm", "_t.py"])
