"""My first pytest test — keeping it simple."""


def test_addition():
    assert 1 + 1 == 2


def test_string_upper():
    assert "hello".upper() == "HELLO"


# TODO: learn how to test exceptions and fixtures next
