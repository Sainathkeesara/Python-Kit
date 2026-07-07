# last_verified: 2026-07-05 · n/a

"""
Applying testing principles I just learned — I wanted to practice
writing isolated, repeatable tests. Using pytest because that's
what the Python kit uses day-to-day.
"""

import pytest


def divide(a: float, b: float) -> float:
    """Simple division — raised an exception for zero divisor."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Independent tests — one failing doesn't block the others
def test_divide_positive():
    assert divide(10, 2) == 5.0


def test_divide_negative():
    assert divide(-10, 2) == -5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Parametrize — tripped on the decorator syntax at first
@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2.0),
    (1, 3, 1 / 3),
    (0, 5, 0.0),
])
def test_divide_parametrized(a, b, expected):
    """Runs three times with different inputs — keeps tests DRY."""
    assert divide(a, b) == expected


# Fixture for shared setup — avoids repeating arrange code
@pytest.fixture
def sample_values() -> dict:
    return {"a": 15.0, "b": 3.0, "expected": 5.0}


def test_divide_with_fixture(sample_values):
    result = divide(sample_values["a"], sample_values["b"])
    assert result == sample_values["expected"]
