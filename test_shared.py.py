import pytest


def test_funded_account_has_initial_balance(funded_account):
    assert funded_account.balance == 1000


def test_withdraw_from_funded_account(funded_account):
    funded_account.withdraw(150)
    assert funded_account.balance == 850
