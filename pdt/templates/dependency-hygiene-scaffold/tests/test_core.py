from dep_hygiene.core import greet


def test_greet() -> None:
    assert greet("World") == "Hello, World!"
