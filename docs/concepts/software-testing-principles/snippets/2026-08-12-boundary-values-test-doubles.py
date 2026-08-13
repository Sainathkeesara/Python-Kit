# last_verified: 2026-08-12 · n/a

"""
Applying testing principles I just read about — boundary values
and test doubles. I wanted to see how they feel in actual pytest code.
"""

import pytest


# --- System under test ---


def categorize_age(age: int) -> str:
    """Return a bucket name for an age. Used to practice boundary tests."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 13:
        return "child"
    if age < 20:
        return "teen"
    if age < 65:
        return "adult"
    return "senior"


# --- Boundary value tests ---
# I picked the edges of each range: just inside and just outside.

@pytest.mark.parametrize("age,expected", [
    (0, "child"),       # boundary: 0 is the minimum valid age
    (-1, None),         # just below lower bound
    (12, "child"),      # last value of child range
    (13, "teen"),       # first value of teen range
    (19, "teen"),       # last value of teen range
    (20, "adult"),      # first value of adult range
    (64, "adult"),      # last value of adult range
    (65, "senior"),     # first value of senior range
])
def test_age_boundaries(age, expected):
    if expected is None:
        with pytest.raises(ValueError):
            categorize_age(age)
    else:
        assert categorize_age(age) == expected


# --- Test double: fake external service ---
# Instead of hitting a real API, I fake the response.


class FakeWeatherAPI:
    """Minimal test double — returns canned responses."""

    def __init__(self, temp_f: float) -> None:
        self.temp_f = temp_f

    def get_temperature(self, city: str) -> float:
        return self.temp_f


def plan_activity(city: str, api) -> str:
    """Decide based on fake API data."""
    temp = api.get_temperature(city)
    if temp > 80:
        return "swimming"
    if temp > 50:
        return "hiking"
    return "museum"


def test_activity_planning_with_fake():
    fake = FakeWeatherAPI(temp_f=85)
    assert plan_activity("Austin", fake) == "swimming"

    fake = FakeWeatherAPI(temp_f=40)
    assert plan_activity("Chicago", fake) == "museum"
