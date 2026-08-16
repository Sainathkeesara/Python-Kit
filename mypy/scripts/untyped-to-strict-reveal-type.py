# last_verified: 2026-08-16 · mypy 2.3.1

"""A small scoreboard module migrated from untyped to mypy --strict clean.

The first version had no annotations anywhere, and `mypy` still reported
Success — the silent-pass gotcha: unannotated functions are deliberately
never type-checked, so body errors like mixing str and int slid through.
Annotating every parameter and return, then running with --strict,
surfaced all of them.

reveal_type() prints exactly what mypy infers for an expression. It only
exists in mypy's world (it is not callable at runtime), so the calls live
behind `if TYPE_CHECKING:` — mypy still analyzes that block and prints the
revealed types, but Python never executes it. Remove them before running
the file as plain Python.

Run with:  uv run mypy --strict untyped-to-strict-reveal-type.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import reveal_type


def parse_line(line: str) -> tuple[str, int]:
    """Split "player:points" into (name, points).

    reveal_type under TYPE_CHECKING shows mypy infers "str" for `name`
    even though `partition` returns a tuple of unknowns until narrowed.
    """
    name, _, raw = line.partition(":")
    if TYPE_CHECKING:
        reveal_type(name)
    return name.strip(), int(raw)


def tally(lines: list[str]) -> dict[str, list[int]]:
    """Group per-player point lists.

    The explicit `scores: dict[str, list[int]] = {}` matters: mypy will
    not infer the `list[int]` value type from an empty literal alone, so
    the annotation pins it (the empty-collection trap).
    """
    scores: dict[str, list[int]] = {}
    for line in lines:
        name, points = parse_line(line)
        scores.setdefault(name, []).append(points)
    if TYPE_CHECKING:
        reveal_type(scores)
    return scores


def best_player(scores: dict[str, list[int]]) -> str | None:
    """Return the player with the highest total, or None for empty input."""
    best: str | None = None
    best_total = -1
    for name, points in scores.items():
        total = sum(points)
        if total > best_total:
            best_total = total
            best = name
    return best


def main(lines: list[str]) -> None:
    scores = tally(lines)
    print(sorted(scores))
    print("best:", best_player(scores))


if __name__ == "__main__":
    main(["alice:3", "bob:7", "alice:2", "bob:1"])