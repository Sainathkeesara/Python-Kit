# last_verified: 2026-08-04 · pytest n/a

import pytest


@pytest.fixture
def sample_items():
    return [
        {"name": "apple", "price": 1.20},
        {"name": "banana", "price": 0.80},
        {"name": "cherry", "price": 2.50},
    ]


@pytest.fixture
def empty_cart():
    return []


def test_cart_total(sample_items):
    cart = sample_items.copy()
    total = sum(item["price"] for item in cart)
    assert total == pytest.approx(4.50)


def test_cart_has_items(sample_items):
    assert len(sample_items) == 3


def test_empty_cart_total(empty_cart):
    assert sum(item["price"] for item in empty_cart) == 0


@pytest.mark.parametrize(
    "item_count, expected_total",
    [
        (1, 1.20),
        (2, 2.00),
        (3, 4.50),
        (0, 0.00),
    ],
)
def test_cart_parametrized(sample_items, item_count, expected_total):
    cart = sample_items[:item_count]
    total = sum(item["price"] for item in cart)
    assert total == pytest.approx(expected_total)
