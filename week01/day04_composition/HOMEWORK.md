# 📝 Day 4 Homework — Refactor into `Bank` + `Account` + `Ledger`

> **Goal:** Take your Day-1 `BankAccount` (which did *everything*) and split it into **composed** parts, each with one job. This is the week's single most important design lesson.
> **Time:** 3 h  ·  **Read first:** [`LEARNING.md`](./LEARNING.md)

---

## 📖 Before you start (5 min)

Skim these sections of [`LEARNING.md`](./LEARNING.md):
- **"Composition vs inheritance"** (Lego-vs-cast-statue, organs-vs-species) → the has-a / is-a test you'll apply throughout.
- **"The `Stack(list)` trap"** → *why* composing a list beats inheriting from one; your `Ledger` follows the same logic.
- **"`@dataclass`"** (the label-maker) → `Transaction` will be one.
- **"The mutable-default trap"** (the shared-hanger) → use `field(default_factory=list)`, never `= []`.

> 🎯 **The mantra for today, said out loud:** *"`Account` HAS-A `Ledger`. `Bank` HAS-MANY `Account`s. `Transaction` is just data → `@dataclass`."* If you can say that sentence, you already understand the design.

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 45 min | `Ledger` — owns the transaction history (records are a `@dataclass`) |
| **B** | 60 min | `Account` — owns a balance + **has-a** `Ledger` |
| **C** | 60 min | `Bank` — **has-many** `Account`s; open / find / transfer |
| **D** | 35 min | Tests, run, push |

## 📁 Files

```text
week01/day04_composition/
├── banking.py        # Transaction (dataclass), Ledger, Account, Bank
└── test_banking.py
```

---

## The design (composition, not one mega-class)

```text
Bank
 ├── has many → Account
 │                ├── balance (float, encapsulated)
 │                └── has-a → Ledger
 │                              └── list of Transaction (dataclass)
```

> 🧱 **Why split it (the Lego argument):** in Day 1, one class did balance + validation + history + formatting. That's a cast statue — change one thing, re-cast the whole block. Today each brick does one job, snaps to the others, and can be tested/replaced alone. That feeling — "each piece does one thing" — is the goal.

## Part A — `Transaction` + `Ledger` (45 min)

- [ ] `Transaction` as a `@dataclass`: `kind: str`, `amount: float`, `balance_after: float`. (Free `__repr__`/`__eq__` — the label-maker.)
- [ ] `Ledger` holds a `list[Transaction]` (init via `__init__` or `field(default_factory=list)` — **never** `= []`).
- [ ] `Ledger.record(kind, amount, balance_after)` appends a `Transaction`.
- [ ] `Ledger.entries()` returns a **copy** of the list (copy-on-read — the Day-1 encapsulation lesson).
- [ ] `Ledger.__len__` returns the number of transactions.

## Part B — `Account` (60 min)

- [ ] `Account(owner, balance=0)` creates `self._ledger = Ledger()` (**composition** — Account *has-a* Ledger).
- [ ] Keep your D1 wins: private `_balance`, read-only `balance` property, validation (`amount <= 0`, overdraft).
- [ ] `deposit` / `withdraw` update the balance **and** call `self._ledger.record(...)`.
- [ ] `statement()` *delegates* to the ledger to print history (Account no longer manages a raw list).

## Part C — `Bank` (60 min)

- [ ] `Bank(name)` holds `self._accounts` — a `dict[str, Account]` keyed by owner.
- [ ] `open_account(owner, initial=0) -> Account`
- [ ] `get(owner) -> Optional[Account]` (use the type hint from `LEARNING.md`)
- [ ] `transfer(from_owner, to_owner, amount)` — look up both, then `withdraw` + `deposit`. **Reuse** those methods so validation/overdraft come for free (don't re-validate here).
- [ ] `total_assets() -> float` — sum of all account balances.

## Tests (Block D)

- [ ] Opening 2 accounts → `bank.total_assets()` is their sum
- [ ] `deposit` then `withdraw` → that account's ledger has the right number of entries
- [ ] `transfer` moves money correctly **and** is rejected on overdraft (raises `ValueError`)
- [ ] `Ledger.entries()` returns a copy (mutating the returned list doesn't change the ledger)
- [ ] `bank.get("nobody")` returns `None`

---

## 🧠 Concept checks (comment at the bottom of `banking.py`)

1. Why is `Account` *has-a* `Ledger` rather than `Account(Ledger)` (inheritance)? Say it with the is-a/has-a test.
2. What does `transfer` gain by *reusing* `withdraw`/`deposit` instead of editing balances directly?
3. Open `day01_bankaccount/bank_account.py` side by side. Name one thing that's now easier to test in isolation than it was in Day 1.

## ✅ Definition of done

- [ ] Four classes, each with a single clear responsibility
- [ ] `Account` **has-a** `Ledger`; `Bank` **has-many** `Account`s (composition throughout)
- [ ] `Transaction` is a `@dataclass`; no mutable-default bug
- [ ] All tests pass; concept checks answered; pushed to GitHub

## 🌟 Stretch

- `Bank.richest_customer() -> Account` using `max(..., key=...)`.
- Make `Transaction` `frozen=True` (immutable) and add `timestamp` defaulting via `field(default_factory=datetime.now)`.
- Add a `min_balance` policy to `Account`, raising a custom exception on violation (previews Day 5).
- Rebuild `Stack` two ways — `class Stack(list)` vs a composed `self._items` — and write one sentence on why the composed version is safer (the leak from `LEARNING.md`).

---

## 🚀 Submit

```bash
git add week01/day04_composition
git commit -m "add: Week1 D4 composed Bank/Account/Ledger"
git push
```
