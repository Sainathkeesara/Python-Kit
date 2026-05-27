"""
Run Ty on a Python codebase — minimal example.
Usage:  python run-ty-on-codebase.py
        (or copy this file into your project and run it with uv)
"""

import subprocess
import sys

# A small typed module to check — pretend this is your actual codebase
CODE = '''
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# Intentional type error — passing a string where int is expected
result = add("one", 2)
'''

def main():
    with open("_test_input.py", "w") as f:
        f.write(CODE)

    result = subprocess.run(
        ["ty", "--show-column-numbers", "_test_input.py"],
        capture_output=True,
        text=True,
    )

    print("=== Ty output ===")
    print(result.stdout or result.stderr)
    print("=== Done ===")

    if result.returncode != 0:
        print(f"Ty found {result.stdout.count('error[')} error(s)")
    else:
        print("No type errors found!")

    # Clean up the temp file
    subprocess.run(["rm", "_test_input.py"])


if __name__ == "__main__":
    main()
