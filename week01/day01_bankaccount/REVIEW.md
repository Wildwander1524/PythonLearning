# 📋 Day 1 Review — `BankAccount`

> **Week 1 · Day 1 (Mon 2026-06-16)** — Classes & objects
> **Verdict:** 🟢 **9 / 10 tests passing.** Strong first day. One real bug (a tested-but-missing method) and a handful of style fixes below.

---

## ✅ Test results

```text
PASS  test_deposit_increases_balance
PASS  test_withdraw_decreases_balance
PASS  test_overdraft_is_rejected
PASS  test_negative_deposit_is_rejected
PASS  test_zero_deposit_is_rejected
PASS  test_balance_property_is_readonly
PASS  test_history_records_transactions
PASS  test_history_returns_copy
PASS  test_account_count_increments
FAIL  test_accounts_transfer  →  'BankAccount' has no attribute 'transfer'

9/10 tests passed
```

---

## 🎉 What you got right

| Concept | Why it's correct |
|---------|------------------|
| **Encapsulation** | `_balance` is private, the `@property` has **no setter**, so `acct.balance = 9999` correctly raises `AttributeError`. |
| **Validation** | All four invalid cases (`deposit ≤ 0`, `withdraw ≤ 0`, overdraft) raise `ValueError`. |
| **Copy-on-read** | `history()` returns `list(self._history)` — callers get a copy and can't corrupt your internal state. |
| **Class attribute** | `BankAccount.account_count += 1` is the **correct** pattern. Using `self.account_count += 1` would have silently created an instance attribute and broken the shared counter. |
| **Test design** | Clean, readable, one assertion-focus per test. |

---

## 🔧 Issues to fix

### 1. 🔴 `transfer` is tested but never implemented — the failing test

You wrote `test_accounts_transfer` (the stretch goal) but never added the method. **Never leave a permanently-failing test.** Either implement it or remove the test.

```python
def transfer(self, target: "BankAccount", amount: float) -> None:
    """Move `amount` from this account into `target`."""
    self.withdraw(amount)      # reuses validation + overdraft check
    target.deposit(amount)     # reuses validation
```

> 💡 Notice this **reuses** `withdraw`/`deposit`, so it inherits their validation for free. Don't re-check `amount` here — that would duplicate logic. Your test calls `BankAccount.transfer(acct1, acct2, 20)`, which works fine with this instance method (it's just `acct1.transfer(acct2, 20)` written the long way).

---

### 2. 🟡 `self._history = ()` — wrong container (tuple, not list)

You store history as a **tuple** and grow it with `+=`. It works, but it's the wrong tool:

- Tuples are for **fixed** records; lists are for **growing** sequences.
- Every `tuple += (...)` builds a **brand-new tuple** and copies all elements — O(n) every append, O(n²) overall.

```python
# ❌ current
self._history = ()
self._history += ({"type": "deposit", ...},)

# ✅ better
self._history = []
self._history.append({"type": "deposit", ...})
```

---

### 3. 🟡 `amount == 0 or amount < 0` — redundant

```python
# ❌ noisy
if amount == 0 or amount < 0:

# ✅ one condition
if amount <= 0:
```

---

### 4. 🟡 Dead `pass` after `return`

Several methods end with `return ...` immediately followed by `pass`. Python never reaches it — it's leftover scaffold. Delete every `pass` that follows a `return`.

---

### 5. 🟢 `__str__` doesn't format to 2 decimals

Your docstring promises `"...balance: 100.00"` but the code prints `100`.

```python
return f"{self.owner}'s account — balance: {self._balance:.2f}"
```

---

### 6. 🟢 `statement()` dumps raw dicts

`0: {'type': 'deposit', 'amount': 50, 'balance': 150}` is hard to read. A human-friendly format:

```python
def statement(self) -> str:
    lines = [f"Statement — {self.owner} ({self.bank_name})"]
    for i, t in enumerate(self._history, start=1):
        sign = "+" if t["type"] == "deposit" else "-"
        lines.append(f"  #{i:<3} {t['type']:<9} {sign}{t['amount']:>8.2f}   bal: {t['balance']:>8.2f}")
    return "\n".join(lines)
```

---

## 🎯 Action items

- [ ] Implement `transfer()` → reach **10/10**
- [ ] `self._history` → `list` + `.append()`
- [ ] `amount <= 0` (both methods)
- [ ] Delete dead `pass` lines
- [ ] `:.2f` formatting in `__str__`
- [ ] (Optional) prettier `statement()`

> Severity legend: 🔴 bug / breaks tests · 🟡 should-fix (correctness-adjacent / performance) · 🟢 polish

Fix these for practice, re-run `python test_bank_account.py`, and you're done with Day 1. ✅
