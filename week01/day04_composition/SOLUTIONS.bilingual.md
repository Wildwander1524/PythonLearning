# ✅ Day 4 — SOLUTIONS
> 🇨🇳 **[第4天 — 解答]**

> After a real attempt only.
> 🇨🇳 仅在真正尝试过之后阅读。

## Reference — `banking.py` (key parts)
> 🇨🇳 **[参考 — `banking.py`（关键部分）]**

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
> 🇨🇳 *[银行账户系统：使用 dataclass 定义交易，组合实现账本、账户和银行，展示组合胜过继承。]*

## RECALL answers
> 🇨🇳 **[复习答案]**

**Spaced:** S1 forbids instantiating the base + forces every `@abstractmethod`; rejects at
*instantiation* (`TypeError`). S2 `__eq__` sets `__hash__=None`; immutable → add `__hash__`,
mutable → leave unhashable. S3 a **new** object — operators don't mutate operands.
> 🇨🇳 **间隔复习：** S1 禁止实例化基类，强制所有 `@abstractmethod`，在*实例化*时报错（`TypeError`）。S2 定义 `__eq__` 会将 `__hash__` 设为 `None`；不可变类型应自行添加 `__hash__`，可变类型则保持不可哈希。S3 返回的是**新**对象——运算符不会修改操作数。

**A:** Composition assembles behaviour from small parts held as attributes; inheritance couples a
child to the parent's internals, so a base change can silently break children (fragile base
class). Inheritance is right for genuine *is-a* subtypes and framework bases (`nn.Module`, ABCs,
exception hierarchies).
> 🇨🇳 **A：** 组合将行为组装成作为属性持有的小部件；继承将子类与父类的内部耦合，基类的改动可能会悄无声息地破坏子类（脆弱的基类问题）。继承适用于真正的*是一个*子类型和框架基类（如 `nn.Module`、抽象基类、异常层次结构）。

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
> 🇨🇳 **B**
> 1. `SavingsAccount`/`BankAccount` = **是一个**（继承）；`Car`/`Engine` = **有一个**（组合）；
>    `LogLevelError`/`LogError` = **是一个**（继承——真正的子类型）；`Stack`/`list` = **有一个**
>    （组合——栈只是*使用*列表）。
> 2. `Stack(list)` 继承了约 40 个列表方法（`insert`、`sort` 等），调用者可能违反栈的规程。组合方式（`self._items = []`）只暴露 `push`/`pop`。
> 3. 默认列表在**函数定义时**创建一次，由所有未提供该参数的调用共享，因此会在多次调用间累积内容。
> 4. `field(default_factory=list)` 会为每个实例创建一个新列表；而 `= []` 在所有实例间共享同一个列表（相同陷阱）。
> 5. 舍弃实例的 `__dict__`（无动态属性）以换取更低内存和稍快的访问速度；仅在有极多实例且经过性能分析确认后才有价值。

**C · Spot-the-bug:** `items: list = []` makes *all* `Cart` instances share one list. Fix:
`items: list = field(default_factory=list)`. Two `Cart()`s would otherwise append into the same
underlying list.
> 🇨🇳 **C · 找漏洞：** `items: list = []` 让*所有* `Cart` 实例共享同一个列表。修正：`items: list = field(default_factory=list)`。否则两个 `Cart()` 实例会向同一个底层列表追加元素。

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
> 🇨🇳 *[使用 dataclass 定义 Song，组合实现 Playlist，避免继承 list 仅暴露 add/len/iter 操作]*
> 🇨🇳 不要写成 `class Playlist(list):`，播放列表并非列表——不应暴露 `sort`/`insert`/`pop` 等方法；组合只暴露有意义的操作。

**E · Math:**
1. `[[2,8],[1,19]]` (inner `2=2` ✅ → `2×2`).  2. unchanged `[[1,2],[3,4]]` (×identity).
3. `A·B = [[2,1],[1,1]]`, `B·A = [[1,1],[1,2]]` → **not equal**; matrix mult isn't commutative.
> 🇨🇳 **E · 数学：**
> 1. `[[2,8],[1,19]]`（内部 `2=2` ✅ → `2×2`）。
> 2. 不变 `[[1,2],[3,4]]`（乘以单位矩阵）。
> 3. `A·B = [[2,1],[1,1]]`，`B·A = [[1,1],[1,2]]` → **不相等**；矩阵乘法不可交换。

## Concept-check answers (homework)
> 🇨🇳 **[概念检查答案（作业）]**

1. `Account` only *uses* a `Ledger` to store history — "account **has a** ledger," not "account
   **is a** ledger."
> 🇨🇳 `Account` 只是*使用* `Ledger` 来存储历史记录——"账户**有一个**账本"，而不是"账户**是一个**账本"。

2. `transfer` reuses `withdraw`/`deposit`, inheriting their validation and overdraft checks (DRY)
   and getting atomicity (withdraw first) for free.
> 🇨🇳 `transfer` 重用 `withdraw`/`deposit`，继承了它们的验证和透支检查（DRY），并免费获得了原子性（先取款）。

3. e.g. the `Ledger` can now be unit-tested in isolation (record/entries/len) without constructing
   a whole account.
> 🇨🇳 例如，现在可以单独对 `Ledger` 进行单元测试（record/entries/len），而无需构造完整的账户。

> 📝 Record: did the is-a/has-a classification (B1) come automatically, or did any case fool you?
> 🇨🇳 📝 记录：is-a/has-a 分类（B1）你是一下子就能正确判断，还是有哪个例子让你搞混了？
