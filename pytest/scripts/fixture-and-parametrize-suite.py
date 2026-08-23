# last_verified: 2026-08-22 · pytest n/a

"""Fixture-and-parametrize test suite demonstrating fixtures, parametrize, and markers.

Run:  uv run pytest fixture-and-parametrize-suite.py -v
      uv run pytest fixture-and-parametrize-suite.py -m slow -v

Custom markers used below (slow, integration) should be registered in
pyproject.toml under [tool.pytest.ini_options] to suppress warnings:

    [tool.pytest.ini_options]
    markers = ["slow: marks tests as slow (deselect with '-m \"not slow\"')"]
"""

import pytest


# ---------------------------------------------------------------------------
# Code under test
# ---------------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount


# ---------------------------------------------------------------------------
# Fixtures — function, class, and module scope
# ---------------------------------------------------------------------------

@pytest.fixture
def fresh_account() -> BankAccount:
    """Default function-scoped fixture: a new instance for every test."""
    return BankAccount("fresh")


@pytest.fixture(scope="class")
def shared_account() -> BankAccount:
    """Class-scoped fixture: one instance reused across all tests in a class."""
    return BankAccount("shared", balance=100.0)


@pytest.fixture(scope="module")
def module_account() -> BankAccount:
    """Module-scoped fixture: created once per module, torn down after the last test."""
    return BankAccount("module", balance=500.0)


# ---------------------------------------------------------------------------
# Parametrized tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("amount,expected", [
    (10.0, 10.0),
    (50.0, 50.0),
    (0.01, 0.01),
])
def test_deposit_increases_balance(fresh_account: BankAccount, amount: float, expected: float) -> None:
    fresh_account.deposit(amount)
    assert fresh_account.balance == expected


@pytest.mark.parametrize("amount", [-1.0, 0.0])
def test_deposit_rejects_non_positive(fresh_account: BankAccount, amount: float) -> None:
    with pytest.raises(ValueError, match="deposit amount must be positive"):
        fresh_account.deposit(amount)


@pytest.mark.slow
def test_large_deposit(fresh_account: BankAccount) -> None:
    fresh_account.deposit(1_000_000.0)
    assert fresh_account.balance == 1_000_000.0


# ---------------------------------------------------------------------------
# Class-scoped fixture: shared_account is one instance for this whole class
# ---------------------------------------------------------------------------

class TestSharedAccount:
    def test_initial_balance(self, shared_account: BankAccount) -> None:
        assert shared_account.balance == 100.0

    @pytest.mark.parametrize("amount,expected", [
        (25.0, 75.0),
        (100.0, 0.0),
    ])
    def test_withdraw_reduces_balance(self, shared_account: BankAccount, amount: float, expected: float) -> None:
        shared_account.withdraw(amount)
        assert shared_account.balance == expected

    def test_overdraw_raises(self, shared_account: BankAccount) -> None:
        with pytest.raises(ValueError, match="insufficient funds"):
            shared_account.withdraw(200.0)


# ---------------------------------------------------------------------------
# Module-scoped fixture: module_account is one instance for this class
# ---------------------------------------------------------------------------

class TestModuleAccount:
    def test_module_balance(self, module_account: BankAccount) -> None:
        assert module_account.balance == 500.0

    def test_module_withdraw(self, module_account: BankAccount) -> None:
        module_account.withdraw(100.0)
        assert module_account.balance == 400.0


# ---------------------------------------------------------------------------
# Integration-style test: combining multiple concepts in one flow
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_account_lifecycle(fresh_account: BankAccount) -> None:
    fresh_account.deposit(200.0)
    fresh_account.withdraw(50.0)
    assert fresh_account.balance == 150.0
