# last_verified: 2026-08-20 · n/a
"""
Practicing the AAA pattern with parametrize and a fixture, after the
testing-principles notes. I kept writing tests where setup, the call,
and the check all blurred together — this snippet makes each beat explicit.
"""

import pytest


def checkout_total(items: list[float], tax_rate: float) -> float:
    """Subtotal plus tax, rounded to cents. The edge cases live in the tests."""
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("tax_rate must be between 0 and 1")
    if any(price < 0 for price in items):
        raise ValueError("prices cannot be negative")
    return round(sum(items) * (1 + tax_rate), 2)


class TestCheckoutTotal:
    """Every test is shaped Arrange -> Act -> Assert so the intent is readable."""

    @pytest.fixture
    def prices(self):
        # Arrange helper: a starter basket the parametrized cases build on.
        return [4.0, 6.0]

    @pytest.mark.parametrize(
        "extra, tax, expected",
        [
            (0.0, 0.00, 10.0),  # edge: base basket, no tax
            (0.0, 0.10, 11.0),  # edge: tax only, nothing added
            (5.0, 0.00, 15.0),  # edge: extra item, no tax
            (5.0, 0.20, 18.0),  # edge: extra item + 20% tax -> 15 * 1.2
        ],
    )
    def test_total(self, prices, extra, tax, expected):
        # Arrange
        items = prices + [extra]
        # Act
        result = checkout_total(items, tax)
        # Assert
        assert result == expected

    @pytest.mark.parametrize("tax", [-0.5, 1.5])
    def test_rejects_out_of_range_tax(self, tax):
        # Arrangement is done by the parameter — Act and Assert fold together
        # because the whole point is "calling this should blow up".
        with pytest.raises(ValueError, match="tax_rate must be between 0 and 1"):
            checkout_total([1.0], tax)

    def test_rejects_negative_price(self):
        with pytest.raises(ValueError, match="prices cannot be negative"):
            checkout_total([1.0, -2.0], 0.0)

    def test_empty_cart_is_zero(self):
        # Arrange
        items: list[float] = []
        # Act
        result = checkout_total(items, 0.1)
        # Assert
        assert result == 0.0
