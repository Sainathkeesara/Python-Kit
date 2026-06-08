"""Three basic pytest tests — just getting my feet wet."""

import pytest


def test_strings():
    assert "hello".upper() == "HELLO"


def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
