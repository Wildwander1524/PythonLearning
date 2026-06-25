"""Day 4 — Composition: Transaction · Ledger · Account · Bank"""

from dataclasses import dataclass
from typing import Optional


# ── Part A ─────────────────────────────────────────────────────────────────

# class Bank:

#     def __init__(self, name: str, accounts: list = None):
#         self.name = name
#         self._accounts = [] if accounts is None else accounts

#     def open_account(self, owner: str, initial: float = 0) -> object:
#         acct = Account(owner, initial)
#         self._accounts.append(acct)
#         return acct

#     def get(self, owner) -> object:
#         for account in self._accounts:
#             if account.owner == owner:
#                 return account

#     def transfer(self, from_owner: str, to_owner: str, amount: float) -> None:
#         self.get(from_owner).withdraw(amount)
#         self.get(to_owner).deposit(amount)

#     def total_assets(self) -> float:
#         return sum([acct.balance for acct in self._accounts])

#     def richest_customer(self):
#         return max(self._accounts,key=Account.balance)

# class Account:

#     def __init__(self, owner: str, balance: float = 0):
#         self.owner = owner
#         self._balance = balance
#         self._ledger = Ledger()

#     @property
#     def balance(self):
#         return self._balance

#     @property
#     def ledger(self):
#         return self._ledger

#     def withdraw(self, amount: float) -> None:
#         if amount <= 0:
#             raise ValueError('withdraw amount must be positive')
#         elif self._balance < amount:
#             raise ValueError('insufficient funds (overdraft)')
#         self._balance -= amount
#         self._ledger.record("withdraw", f"-{amount:.2f}", f"{self._balance:.2f}")

#     def deposit(self, amount: float) -> None:
#         if amount <= 0:
#             raise ValueError('deposit amount must be positive')
#         self._balance += amount
#         self._ledger.record("deposit", f"{amount:.2f}", f"{self._balance:.2f}")


# @dataclass
# class Transaction:
#     kind: str
#     amount: float
#     balance_after: float


# @dataclass
# class Ledger:
#     _items: list = field(default_factory=list)

#     def record(self, kind, amount, balance_after) -> list:
#         self._items.append(Transaction(kind, amount, balance_after))

#     def entries(self) -> list:
#         return self._items.copy()

#     def statement(self) -> str:
#         return '\n'.join(f"{i}: {item}" for i, item in enumerate(self._items))

#     def __len__(self) -> int:
#         return len(Ledger._items)


# if __name__ == '__main__':
#     bank_E = Bank('EAST BANK')
#     bank_N = Bank('NORTH BANK')
#     acct_Alex = bank_E.open_account('Alex', 1000)
#     acct_John = bank_E.open_account('John', 1000)
#     acct_Ben = bank_N.open_account('Ben', 2000)
#     acct_Alex.deposit(500)  # 1500
#     acct_Alex.deposit(500)  # 2000
#     acct_Alex.deposit(500)  # 2500
#     acct_Ben.withdraw(500)  # 1500
#     acct_Ben.withdraw(500)  # 1000
#     acct_Ben.withdraw(500)  # 500
#     print(acct_Alex.ledger.entries)
#     print(acct_Ben.ledger.entries)
#     print(acct_Alex.ledger.statement())
#     print(bank_E.total_assets())
#     print(bank_N.total_assets())
#     print(bank_E.total_assets() == bank_N.total_assets())
#     print(bank_E.get('Alex'))
#     bank_E.transfer('Alex','John',2500)
#     print(bank_E.total_assets())
#     print(bank_N.total_assets())
#     print(bank_E.total_assets() == bank_N.total_assets())
#     print(bank_E.get('nobody'))
#     print(bank_E.richest_customer())




@dataclass
class Transaction:
    kind: str
    amount: float
    balance_after: float


class Ledger:
    def __init__(self):
        self._entries: list[Transaction] = []

    def record(self, kind: str, amount: float, balance_after: float) -> None:
        self._entries.append(Transaction(kind, amount, balance_after))

    def entries(self) -> list[Transaction]:
        return self._entries.copy()

    def __len__(self) -> int:
        return len(self._entries)



# ── Part B ─────────────────────────────────────────────────────────────────

class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._ledger = Ledger()   # HAS-A

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('deposit amount must be positive')
        self._balance += amount
        self._ledger.record("deposit", amount, self._balance)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('withdraw amount must be positive')
        elif self._balance < amount:
            raise ValueError('insufficient funds (overdraft)')
        self._balance -= amount
        self._ledger.record("withdraw", -amount, self._balance)

    def statement(self) -> str:
        return '\n'.join(f"{i}: {item}" for i, item in enumerate(self._ledger.entries()))


# ── Part C ─────────────────────────────────────────────────────────────────

class Bank:
    def __init__(self, name: str):
        self.name = name
        self._accounts: dict[str, Account] = {}

    def open_account(self, owner: str, initial: float = 0.0) -> Account:
        self._accounts[owner] = Account(owner,initial)
        return self._accounts[owner]

    def get(self, owner: str) -> Optional[Account]:
        return  self._accounts.get(owner)

    def transfer(self, from_owner: str, to_owner: str, amount: float) -> None:
        src = self.get(from_owner)
        dst = self.get(to_owner)
        if src is None or dst is None:
            raise ValueError('one or both accounts do not exist')
        src.withdraw(amount)
        dst.deposit(amount)

    def total_assets(self) -> float:
        return sum([acct.balance for acct in self._accounts.values()])

    def richest_customer(self):
        lst = []
        for account in self._accounts.values():
            lst.append((account.balance, account.owner))
        lst_cus = sorted(lst, key=lambda x: x[0], reverse=True)
        return lst_cus[0][1]

# ── Concept checks (fill these in after all tests pass) ───────────────────

"""
1. Why is Account has-a Ledger rather than Account(Ledger) (inheritance)?
   Use the is-a / has-a test.
Answer:Why is Account has-a Ledger rather than Account(Ledger) (inheritance)? Say it with the is-a/has-a test.
if the Account is a Ledger,then the Account will change after Ledger changed,

2. What does transfer gain by reusing withdraw/deposit instead of editing
   balances directly?
Answer:What does transfer gain by reusing withdraw/deposit instead of editing balances directly?
the code is lighter,and its the rule 'DRY'

3. Open day01_bankaccount/bank_account.py side by side. Name one thing that
   is now easier to test in isolation than it was in Day 1.
Answer:Open day01_bankaccount/bank_account.py side by side. Name one thing that's now easier to test in isolation than it was in Day 1.
you can test any part of them easier than before,more logical to check 

"""
