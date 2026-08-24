# last_verified: 2026-08-24 · n/a

"""
Pattern: parametrized edge-case suite with coverage thresholds wired to CI.

Demonstrates how a single parametrized test function replaces dozens of
hand-written edge-case tests, and how to enforce coverage via pytest-cov
so CI fails when new code slips through untested.

Run with:
    pytest parametrized-edge-case-coverage-ci.py --cov=. --cov-fail-under=80 -v
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import pytest


# ---------------------------------------------------------------------------
# Production code under test
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp *value* into [lo, hi].  The interesting edges are lo==hi,
    values outside both bounds, and exact-boundary inputs."""
    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")
    return max(lo, min(hi, value))


def classify_distance(d: float) -> str:
    """Bucket a non-negative distance into a human label.

    The parametrized suite below exercises every boundary:
    zero, negative (invalid), tiny positive, and the three thresholds.
    """
    if d < 0:
        raise ValueError("distance must be non-negative")
    if d == 0:
        return "origin"
    if d < 1.0:
        return "near"
    if d < 10.0:
        return "mid"
    return "far"


# ---------------------------------------------------------------------------
# Parametrized edge-case suite
# ---------------------------------------------------------------------------

class TestClamp:
    """Parametrized boundary-value tests for clamp()."""

    @pytest.mark.parametrize(
        "value, lo, hi, expected",
        [
            # --- boundary: value == lo ---
            (0.0, 0.0, 10.0, 0.0),
            # --- boundary: value == hi ---
            (10.0, 0.0, 10.0, 10.0),
            # --- inside range ---
            (5.0, 0.0, 10.0, 5.0),
            # --- below lo ---
            (-1.0, 0.0, 10.0, 0.0),
            # --- above hi ---
            (15.0, 0.0, 10.0, 10.0),
            # --- lo == hi: degenerate range ---
            (5.0, 3.0, 3.0, 3.0),
            # --- negative range ---
            (-10.0, -5.0, -1.0, -5.0),
            # --- floats near boundary ---
            (9.999, 0.0, 10.0, 9.999),
            (10.001, 0.0, 10.0, 10.0),
        ],
        ids=[
            "value-equals-lo",
            "value-equals-hi",
            "inside-range",
            "below-lo",
            "above-hi",
            "degenerate-lo-eq-hi",
            "negative-range",
            "float-near-hi",
            "float-above-hi",
        ],
    )
    def test_clamp_boundary(self, value: float, lo: float, hi: float, expected: float) -> None:
        assert clamp(value, lo, hi) == expected

    def test_clamp_raises_on_inverted_bounds(self) -> None:
        with pytest.raises(ValueError, match="lo .* must be <= hi"):
            clamp(5.0, 10.0, 0.0)


class TestClassifyDistance:
    """Parametrized boundary tests for classify_distance()."""

    @pytest.mark.parametrize(
        "distance, expected",
        [
            (0.0, "origin"),
            (0.001, "near"),
            (0.999, "near"),
            (1.0, "mid"),
            (5.0, "mid"),
            (9.999, "mid"),
            (10.0, "far"),
            (100.0, "far"),
        ],
        ids=[
            "zero-is-origin",
            "tiny-positive-is-near",
            "just-under-1-is-near",
            "exactly-1-is-mid",
            "midpoint",
            "just-under-10-is-mid",
            "exactly-10-is-far",
            "large-distance",
        ],
    )
    def test_classify_boundary(self, distance: float, expected: str) -> None:
        assert classify_distance(distance) == expected

    def test_classify_rejects_negative(self) -> None:
        with pytest.raises(ValueError, match="distance must be non-negative"):
            classify_distance(-1.0)


class TestPointDistance:
    """Parametrized tests covering the distance formula at edge cases."""

    @pytest.mark.parametrize(
        "p1, p2, expected",
        [
            (Point(0, 0), Point(0, 0), 0.0),
            (Point(0, 0), Point(3, 4), 5.0),
            (Point(-1, -1), Point(2, 3), 5.0),
            (Point(1.5, 2.5), Point(1.5, 2.5), 0.0),
        ],
        ids=[
            "same-point",
            "pythagorean-triple",
            "negative-coords",
            "float-coords-same-point",
        ],
    )
    def test_distance(self, p1: Point, p2: Point, expected: float) -> None:
        assert p1.distance_to(p2) == pytest.approx(expected)
        # Distance is symmetric
        assert p2.distance_to(p1) == pytest.approx(expected)
