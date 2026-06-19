# ✅ Day 4 — SOLUTIONS

> After a real attempt only.

## Reference — `banking.py` (key parts)
```python
from dataclasses import dataclass, field

@dataclass
class Transaction:
    kind: str
    amount: float
    balance_after: float

class Ledger:                                   # OWNS the history
    def __init__(self):
        self._entries: list[Transaction] = []   # (or field(default_factory=list) in a dataclass)
    def record(self, kind, amount, balance_after):
        self._entries.append(Transaction(kind, amount, balance_after))
    def entries(self):
        return list(self._entries)              # copy-on-read (Day-1 lesson)
    def __len__(self):
        return len(self._entries)

class Account:                                  # HAS-A Ledger (composition)
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)
        self._ledger = Ledger()                 # ← composition, not inheritance
    @property
    def balance(self): return self._balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("amount must be positive")
        self._balance += amount
        self._ledger.record("deposit", amount, self._balance)
    def withdraw(self, amount):
        if amount <= 0: raise ValueError("amount must be positive")
        if amount > self._balance: raise ValueError("overdraft")
        self._balance -= amount
        self._ledger.record("withdraw", amount, self._balance)
    def statement(self):
        return "\n".join(f"{t.kind} {t.amount:.2f} → {t.balance_after:.2f}"
                         for t in self._ledger.entries())   # DELEGATE to the ledger

class Bank:                                     # HAS-MANY Accounts
    def __init__(self, name):
        self.name = name
        self._accounts: dict[str, Account] = {}
    def open_account(self, owner, initial=0.0):
        acct = Account(owner, initial); self._accounts[owner] = acct; return acct
    def get(self, owner):                       # -> Account | None
        return self._accounts.get(owner)
    def transfer(self, src, dst, amount):
        self._accounts[src].withdraw(amount)    # reuse → validation/overdraft free, atomic
        self._accounts[dst].deposit(amount)
    def total_assets(self):
        return sum(a.balance for a in self._accounts.values())
```

## RECALL answers
**Spaced:** S1 forbids instantiating the base + forces every `@abstractmethod`; rejects at
*instantiation* (`TypeError`). S2 `__eq__` sets `__hash__=None`; immutable → add `__hash__`,
mutable → leave unhashable. S3 a **new** object — operators don't mutate operands.

**A:** Composition assembles behaviour from small parts held as attributes; inheritance couples a
child to the parent's internals, so a base change can silently break children (fragile base
class). Inheritance is right for genuine *is-a* subtypes and framework bases (`nn.Module`, ABCs,
exception hierarchies).

**B**
1. `SavingsAccount`/`BankAccount` = **is-a** (inherit); `Car`/`Engine` = **has-a** (compose);
   `LogLevelError`/`LogError` = **is-a** (inherit — genuine subtype); `Stack`/`list` = **has-a**
   (compose — a stack only *uses* a list).
2. `Stack(list)` inherits all ~40 list methods (`insert`, `sort`, …), so callers can violate
   stack discipline. Composing (`self._items = []`) lets you expose only `push`/`pop`.
3. The default list is created **once at `def`-time** and shared by all calls lacking the arg, so
   it accumulates across calls.
4. `field(default_factory=list)` — it makes a fresh list per instance; `= []` shares one list
   across all instances (same trap).
5. Trades away per-instance `__dict__` (no dynamic attributes) for lower memory + slightly faster
   access; worth it only with very many instances and a profiler's confirmation.

**C · Spot-the-bug:** `items: list = []` makes *all* `Cart` instances share one list. Fix:
`items: list = field(default_factory=list)`. Two `Cart()`s would otherwise append into the same
underlying list.

**D · Micro-build:**
```python
from dataclasses import dataclass
@dataclass
class Song:
    title: str
    artist: str
class Playlist:
    def __init__(self): self._songs: list[Song] = []   # HAS-A list
    def add(self, song): self._songs.append(song)
    def __len__(self): return len(self._songs)
    def __iter__(self): return iter(self._songs)
# Not class Playlist(list): a playlist isn't a list — it shouldn't expose sort/insert/pop etc.;
# composing exposes only the operations that make sense.
```

**E · Math:**
1. `[[2,8],[1,19]]` (inner `2=2` ✅ → `2×2`).  2. unchanged `[[1,2],[3,4]]` (×identity).
3. `A·B = [[2,1],[1,1]]`, `B·A = [[1,1],[1,2]]` → **not equal**; matrix mult isn't commutative.

## Concept-check answers (homework)
1. `Account` only *uses* a `Ledger` to store history — "account **has a** ledger," not "account
   **is a** ledger." 2. `transfer` reuses `withdraw`/`deposit`, inheriting their validation and
   overdraft checks (DRY) and getting atomicity (withdraw first) for free. 3. e.g. the `Ledger`
   can now be unit-tested in isolation (record/entries/len) without constructing a whole account.

> 📝 Record: did the is-a/has-a classification (B1) come automatically, or did any case fool you?
