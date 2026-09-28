import pytest


@pytest.fixture
def tracked_account():
    print("[setup]")
    account = type("DummyAccount", (), {"balance": 100})()
    yield account
    print("[teardown]")


def test_balance_starts_at_100(tracked_account):
    assert tracked_account.balance == 100


def test_balance_is_still_100_after_read(tracked_account):
    assert tracked_account.balance == 100
