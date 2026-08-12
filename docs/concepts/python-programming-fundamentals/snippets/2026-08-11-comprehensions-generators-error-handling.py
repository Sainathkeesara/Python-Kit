# last_verified: 2026-08-11 · n/a

"""
I wrote this to practice three fundamentals I keep reaching for in the kit:
comprehensions for transforming data, generators for lazy sequences, and
try/except for failures that are really just part of the job.
"""


def parse_scores(lines: list[str]) -> dict[str, int]:
    """Turn 'name,score' lines into a dict, skipping anything malformed."""
    valid: dict[str, int] = {}
    for line in lines:
        try:
            name, raw = line.split(",")
            valid[name.strip()] = int(raw.strip())
        except (ValueError, TypeError):
            # A bad line shouldn't blow up the whole batch — just skip it.
            continue
    return valid


# List comprehension — the same loop but expressed as data.
scores = parse_scores(["ada,42", "lin,37", "bogus-line", "grace,51"])
top = {name for name, value in scores.items() if value > 40}
print(f"Scored above 40: {sorted(top)}")

# Generator expression — yields one value at a time instead of a whole list.
total = sum(value for value in scores.values())
average = total / len(scores) if scores else 0.0
print(f"Average score: {average:.1f}")

# A generator function: pauses between yields, so a long sequence is cheap.
def running_average(values: list[int]):
    total, count = 0, 0
    for value in values:
        total += value
        count += 1
        yield round(total / count, 1)

print("Running averages:", list(running_average([10, 20, 30])))


# try/except/finally — cleanup runs whether or not the block raised.
def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")


print(safe_divide(1, 0))  # inf — I'd rather have a value than a crash.
