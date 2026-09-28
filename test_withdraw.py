import pytest

from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw_reduces_balance(account):
    account.withdraw(25)
    assert account.balance == 75


def test_withdraw_raises_for_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200)
