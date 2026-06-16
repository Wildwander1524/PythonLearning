class BankAccount:
    """A simple bank account with encapsulation, validation, and transaction history."""

    bank_name = "PythonLearning Bank"  # class attribute — shared by all accounts
    account_count = 0  # class attribute — tracks how many accounts exist

    def __init__(self, owner: str, balance: float = 0):
        """Initialize the account. Increment account_count."""
        # TODO: store owner, set self._balance, append to self._history, increment account_count
        self.owner = owner
        self._balance = balance
        self._history = ()
        self.min_balance = 10
        BankAccount.account_count += 1
        pass

    # ------------------------------------------------------------------
    # Property (Level 2)
    # ------------------------------------------------------------------

    @property
    def balance(self) -> float:
        """Read-only balance. No setter — external code cannot overwrite it."""
        # TODO: return self._balance
        return self._balance
        pass

    # ------------------------------------------------------------------
    # Core operations (Level 1 + 2)
    # ------------------------------------------------------------------

    def deposit(self, amount: float) -> None:
        """Add amount to balance. Raise ValueError for zero or negative amount."""
        # TODO: validate amount, update self._balance, record in history
        if amount == 0 or amount < 0:
            raise ValueError("Invalid Amount")
        self._balance += amount
        self._history += (
            {"type": "deposit", "amount": amount, "balance": self._balance},
        )

    def withdraw(self, amount: float) -> None:
        """Subtract amount from balance. Raise ValueError for invalid or overdraft."""
        # TODO: validate amount, check overdraft, update self._balance, record in history
        if amount <= 0:
            raise ValueError("Invalid Amount")
        elif self._balance - amount < self.min_balance:
            raise ValueError("Overdraft")
        # elif amount > self._balance:
        #     raise ValueError('Overdraft')
        self._balance -= amount
        self._history += (
            {"type": "withdraw", "amount": amount, "balance": self._balance},
        )

    # ------------------------------------------------------------------
    # History (Level 3)
    # ------------------------------------------------------------------

    def history(self) -> list:
        """Return a COPY of the transaction history list."""
        # TODO: return a copy so callers cannot mutate the internal list
        return list(self._history)

    def statement(self) -> str:
        """Return a formatted multi-line string of all transactions."""
        # TODO: build and return a readable string from self._history
        return "\n".join(f"{i}: {item}" for i, item in enumerate(list(self._history)))

    # ------------------------------------------------------------------
    # String representation (Level 1)
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """Return e.g. "Ben's account — balance: 100.00"."""
        # TODO: format owner name and balance
        return f"{self.owner}'s account — balance: {self._balance}"
        pass

    @staticmethod
    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)


# ------------------------------------------------------------------
# Quick manual smoke-test (delete or comment out when tests are written)
# ------------------------------------------------------------------
if __name__ == "__main__":
    acct = BankAccount("Ben", 100)
    acct.deposit(50)
    acct.withdraw(30)
    print(acct)
    print(acct.statement())
    print("Accounts created:", BankAccount.account_count)
