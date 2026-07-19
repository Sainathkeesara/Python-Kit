# last_verified: 2026-07-19 · mypy n/a
# A tiny typed module I made to run `mypy` against a whole file, not just one function.
# Check it with: mypy 2026-07-19-typed-small-module.py

from typing import Optional


def parse_price(raw: str) -> Optional[float]:
    raw = raw.strip().lstrip("$")
    if not raw:
        return None
    return float(raw)


def total(prices: list[float]) -> float:
    return sum(prices)


values: list[float] = [parse_price("$1.50") or 0.0, parse_price("2") or 0.0]
print(total(values))
