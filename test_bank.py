import pytest

from bank import BankAccount, InsufficientFunds


@pytest.fixture
def account():
    return BankAccount("alice", balance=100)


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100


def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100


def test_zero_deposit_is_refused(account):
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(0)


def test_withdrawing_whole_balance_leaves_zero(account):
    account.withdraw(account.balance)
    assert account.balance == 0


def test_two_withdrawals_both_reduce_balance(account):
    account.withdraw(25)
    account.withdraw(25)
    assert account.balance == 50


def test_interest_uses_approximate_comparison(account):
    account.add_interest(0.10)
    assert account.balance == pytest.approx(110)
