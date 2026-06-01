"""Following the pytest quickstart — parametrized tests.

I wanted to see how @pytest.mark.parametrize works with multiple
inputs and with class-scoped tests.  Run: uv run pytest -v
"""

import pytest


def square(x: int) -> int:
    return x * x


# I tried a single test case first, then realized parametrize
# lets me cover edge cases without copying the assert.
@pytest.mark.parametrize("input_val,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (5, 25),
])
def test_square(input_val: int, expected: int) -> None:
    assert square(input_val) == expected


# Grouping tests in a class so the same params can feed
# different assertions — the quickstart showed this pattern.
class TestStringMethods:
    @pytest.mark.parametrize("s,expected", [
        ("hello", 5),
        ("", 0),
        ("abc", 3),
    ])
    def test_length(self, s: str, expected: int) -> None:
        assert len(s) == expected

    @pytest.mark.parametrize("s,expected", [
        ("hello", "olleh"),
        ("abc", "cba"),
    ])
    def test_reversed(self, s: str, expected: str) -> None:
        assert s[::-1] == expected
