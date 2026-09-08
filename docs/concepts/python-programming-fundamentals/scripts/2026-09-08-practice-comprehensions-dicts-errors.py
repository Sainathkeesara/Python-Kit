# last_verified: 2026-09-08 · n/a

"""
I practiced comprehensions, dicts, and error handling in one script
so I can flip back to it as a quick reference. Each section is a
small exercise I worked through.
"""

# ── List comprehensions ──────────────────────────────────────────

# Basic: filter and transform in one pass
numbers = range(-5, 6)
positives_squared = [x ** 2 for x in numbers if x > 0]
print(f"Positives squared: {positives_squared}")

# Nested: flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(f"Flattened matrix: {flat}")

# Conditional expression inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(f"Labels: {labels}")

# ── Dict comprehensions ──────────────────────────────────────────

# Build a word-length mapping
words = ["hello", "world", "python", "is", "great"]
lengths = {w: len(w) for w in words}
print(f"Word lengths: {lengths}")

# Invert a dict
inverted = {v: k for k, v in lengths.items()}
print(f"Inverted: {inverted}")

# Filter with dict comprehension
long_words = {w: l for w, l in lengths.items() if l > 3}
print(f"Long words: {long_words}")

# ── set comprehension ────────────────────────────────────────────

# Unique characters in a sentence
sentence = "hello world"
unique_chars = {ch for ch in sentence if ch != " "}
print(f"Unique chars: {sorted(unique_chars)}")

# ── Error handling ───────────────────────────────────────────────

# Basic try/except pattern
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print(f"  Cannot divide {a} by zero")
        return None

print(f"\nDivide 10/3: {safe_divide(10, 3)}")
print(f"Divide 10/0: {safe_divide(10, 0)}")

# Catching specific exceptions vs bare except
def parse_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        # Don't use bare except — it catches KeyboardInterrupt too
        print(f"  '{value}' is not a valid integer")
        return -1

print(f"Parse '42': {parse_int('42')}")
print(f"Parse 'abc': {parse_int('abc')}")

# Using else and finally
def read_config(path: str) -> dict:
    """Read a config file, returning empty dict on any failure."""
    try:
        with open(path) as f:
            content = f.read()
        # If we get here, the file opened successfully
    except FileNotFoundError:
        print(f"  Config file '{path}' not found, using defaults")
        return {}
    except PermissionError:
        print(f"  No permission to read '{path}'")
        return {}
    else:
        # Only runs if no exception occurred
        print(f"  Config loaded from '{path}'")
        # In real code: return json.loads(content)
        return {"loaded": True}
    finally:
        # Always runs — good for cleanup, not return values
        print(f"  Finished attempting to read '{path}'")

print("\nReading existing file:")
_ = read_config("/etc/hostname")
print("Reading missing file:")
_ = read_config("/nonexistent/config.json")

# ── Combining comprehensions with error handling ─────────────────

def batch_convert(values: list[str]) -> list[int]:
    """Convert strings to ints, skipping failures."""
    results = []
    for v in values:
        try:
            results.append(int(v))
        except ValueError:
            print(f"  Skipping '{v}' — not an integer")
    return results

raw = ["1", "2", "oops", "4", "5.5", "6"]
converted = batch_convert(raw)
print(f"\nBatch convert {raw}: {converted}")

# Same thing with a comprehension (less readable but one-liner)
# Note: try/except in a comprehension is ugly — explicit loop is better
