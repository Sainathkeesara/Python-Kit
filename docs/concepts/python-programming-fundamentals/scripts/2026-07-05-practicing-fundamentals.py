# last_verified: 2026-07-05 · n/a

"""
I wrote this script to practice Python fundamentals — data types,
control flow, functions, and list comprehensions all in one place
so I can flip back to it as a reference.
"""

def classify_number(n: int) -> str:
    """Return a label for the given integer."""
    # Plain if/elif/else — nothing fancy, but I kept forgetting
    # that elif is the Python spelling, not elsif or else if
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"

# List comprehension — tripped on the order at first (expr then loop)
squares = [x * x for x in range(-3, 4)]
# Dict comprehension — same pattern, but with key: value
classified = {x: classify_number(x) for x in range(-3, 4)}

# F-strings are still my favourite Python feature
print(f"Numbers -3..3 classified: {classified}")

# Function with default args and type hints — mypy would catch mistakes here
def compute(a: float, b: float, op: str = "add") -> float:
    if op == "add":
        return a + b
    elif op == "mul":
        return a * b
    raise ValueError(f"Unknown op: {op}")

print(compute(3, 4))        # 7
print(compute(3, 4, "mul")) # 12

# Tuple unpacking in a loop — clean pattern for paired data
pairs = [(1, 2), (3, 4), (5, 6)]
pair_sums = [a + b for a, b in pairs]
print(f"Pair sums: {pair_sums}")

# args and kwargs — still gets me every time
def log_summary(name: str, *scores: int, **metadata: str) -> None:
    total = sum(scores)
    tags = ", ".join(f"{k}={v}" for k, v in metadata.items())
    print(f"{name}: total={total} [{tags}]")

log_summary("alice", 85, 92, 78, course="math", term="2026")
