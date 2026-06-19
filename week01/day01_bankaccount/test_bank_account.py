from bank_account import BankAccount

# ------------------------------------------------------------------
# Helper
# ------------------------------------------------------------------


def run_all_tests():
    tests = [
        test_deposit_increases_balance,
        test_withdraw_decreases_balance,
        test_overdraft_is_rejected,
        test_negative_deposit_is_rejected,
        test_zero_deposit_is_rejected,
        test_balance_property_is_readonly,
        test_history_records_transactions,
        test_account_count_increments,
        test_accounts_transfer,
        test_statement_multiline_str,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed")


# ------------------------------------------------------------------
# Tests — fill these in during Block D
# ------------------------------------------------------------------


def test_deposit_increases_balance():
    acct = BankAccount("Ben", 100)
    acct.deposit(50)
    assert acct.balance == 150, f"Expected 150, got {acct.balance}"


def test_withdraw_decreases_balance():
    # TODO: create account, withdraw, assert correct balance
    acct = BankAccount("Ben", 100)
    acct.withdraw(50)
    assert acct.balance == 50, f"Expected 50, got {acct.balance}"


def test_overdraft_is_rejected():
    acct = BankAccount("Ben", 100)
    try:
        acct.withdraw(500)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # expected


def test_negative_deposit_is_rejected():
    # TODO: assert ValueError raised for deposit(-10)
    acct = BankAccount("Ben", 100)
    try:
        acct.deposit(-10)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # expected


def test_zero_deposit_is_rejected():
    # TODO: assert ValueError raised for deposit(0)
    acct = BankAccount("Ben", 100)
    try:
        acct.deposit(0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # expected


def test_balance_property_is_readonly():
    acct = BankAccount("Ben", 100)
    try:
        acct.balance = 9999
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass  # expected — no setter defined


def test_history_records_transactions():
    # TODO: deposit + withdraw, assert len(acct.history()) == 2
    acct = BankAccount("Ben", 100)
    acct.deposit(50)
    acct.withdraw(50)
    assert len(acct._history) == 2, f"Expected 2, got {len(acct._history)}"


def test_account_count_increments():
    before = BankAccount.account_count
    BankAccount("Alice", 0)
    BankAccount("Bob", 0)
    assert (
        BankAccount.account_count == before + 2
    ), f"Expected {before + 2}, got {BankAccount.account_count}"


def test_accounts_transfer():
    acct1 = BankAccount("Alice", 100)
    acct2 = BankAccount("Bob", 80)
    acct1.transfer(acct2, 20)
    assert (
        acct1.balance == 80 and acct2.balance == 100
    ), f"Expected 80,100, got {acct1.balance},{acct2.balance}"


def test_statement_multiline_str():
    acct = BankAccount("Ben", 100)
    acct.deposit(50)
    acct.withdraw(50)
    stmt = acct.statement()
    assert isinstance(stmt, str), f"Expected string, got {type(stmt)}"
    assert "\n" in stmt, f"Expected multiline string, got: {stmt}"


# ------------------------------------------------------------------

if __name__ == "__main__":
    run_all_tests()
