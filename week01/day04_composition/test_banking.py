"""Day 4 tests — run with: python -m pytest week01/day04_composition/"""

import pytest
from banking import Transaction, Ledger, Account, Bank


# ── Ledger ─────────────────────────────────────────────────────────────────

def test_ledger_record_and_len():
    ledger = Ledger()
    ledger.record("deposit", 100, 100)
    assert len(ledger) == 1

def test_ledger_entries_returns_copy():
    ledger = Ledger()
    ledger.record("deposit", 50, 50)
    copy = ledger.entries()
    copy.clear()
    assert len(ledger) == 1   # internal list unchanged


# ── Account ────────────────────────────────────────────────────────────────

def test_account_deposit_updates_balance_and_ledger():
    acc = Account("Alice", 0)
    acc.deposit(100)
    acc.withdraw(40)
    assert acc.balance == 60
    assert len(acc._ledger) == 2

def test_account_deposit_invalid_raises():
    acc = Account("Alice")
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_account_overdraft_raises():
    acc = Account("Alice", 50)
    with pytest.raises(ValueError):
        acc.withdraw(100)

def test_account_balance_read_only():
    acc = Account("Alice", 100)
    with pytest.raises(AttributeError):
        acc.balance = 999  # pyright: ignore[reportAttributeAccessIssue]  (intentional: balance is read-only)


# ── Bank ───────────────────────────────────────────────────────────────────

def test_bank_total_assets():
    bank = Bank("TestBank")
    bank.open_account("Alice", 100)
    bank.open_account("Bob", 200)
    assert bank.total_assets() == 300

def test_bank_transfer_moves_money():
    bank = Bank("TestBank")
    bank.open_account("Alice", 200)
    bank.open_account("Bob", 50)
    bank.transfer("Alice", "Bob", 100)
    alice, bob = bank.get("Alice"), bank.get("Bob")
    assert alice is not None and bob is not None
    assert alice.balance == 100
    assert bob.balance == 150

def test_bank_transfer_overdraft_raises():
    bank = Bank("TestBank")
    bank.open_account("Alice", 50)
    bank.open_account("Bob", 0)
    with pytest.raises(ValueError):
        bank.transfer("Alice", "Bob", 200)

def test_bank_get_unknown_returns_none():
    bank = Bank("TestBank")
    assert bank.get("nobody") is None


# ── Transaction dataclass ──────────────────────────────────────────────────

def test_transaction_eq():
    t1 = Transaction("deposit", 100, 100)
    t2 = Transaction("deposit", 100, 100)
    assert t1 == t2   # @dataclass gives __eq__ for free

def test_transaction_repr():
    t = Transaction("deposit", 50, 50)
    assert "deposit" in repr(t)
