# ✅ Day 1 — SOLUTIONS / ✅ 第1天 — 解题参考

> Open **only after** a genuine attempt at [`HOMEWORK.md`](./HOMEWORK.md) and [`RECALL.md`](./RECALL.md). Peeking early replaces *retrieval* (which builds memory) with *recognition* (which doesn't). The struggle is the point.
> 🇨🇳 请仅在认真尝试了 [`HOMEWORK.md`](./HOMEWORK.md) 和 [`RECALL.md`](./RECALL.md) 之后再打开。提前偷看会把构建记忆的“提取”过程替换成无效的“识别”。挣扎本身才是重点。

## Reference implementation — `bank_account.py` / 参考实现 — `bank_account.py`

```python
class BankAccount:
    """A bank account with a protected balance, validation, and transaction history."""

    bank_name = "PythonLearning Bank"   # class attribute — shared
    account_count = 0                   # class attribute — shared counter

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)
        self._history: list[dict] = []          # list, not tuple → O(1) appends
        BankAccount.account_count += 1          # mutate the SHARED counter via the class

    @property
    def balance(self) -> float:
        return self._balance                    # no setter ⇒ read-only ⇒ invariant protected

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount
        self._record("deposit", amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds (overdraft)")
        self._balance -= amount
        self._record("withdraw", amount)

    def transfer(self, target: "BankAccount", amount: float) -> None:
        # Reuse withdraw/deposit → validation + overdraft come for FREE (DRY).
        # withdraw runs first, so if it raises, target.deposit never runs → atomic.
        self.withdraw(amount)
        target.deposit(amount)

    def history(self) -> list:
        return list(self._history)              # a COPY — callers can't corrupt internal state

    def __str__(self) -> str:
        return f"{self.owner}'s account — balance: {self._balance:.2f}"

    def _record(self, kind: str, amount: float) -> None:
        self._history.append({"type": kind, "amount": amount, "balance": self._balance})
```
> 🇨🇳 这是一个银行账户类的参考实现，使用受保护的余额、输入验证和交易历史记录。

**Why this passes the new rung (transfer atomicity):** `transfer` calls `withdraw` *before* `deposit`. A failed `withdraw` raises and aborts the method, so `target` is never credited — both balances stay unchanged. No extra code needed; ordering gives you atomicity for free.
> 🇨🇳 **为什么这能通过新等级（转账原子性）：** `transfer` 先调用 `withdraw`，再调用 `deposit`。若 `withdraw` 失败并抛出异常，方法就会中止，`target` 永远不会被入账——双方余额保持不变。无需额外代码，顺序自然带来原子性。

## RECALL answers / 回忆练习答案

**A · Free recall (model):** A *class* is a blueprint describing the state and behaviour a kind of thing has; an *object* is one concrete thing built from it (blueprint → house). `self` is "this particular object," passed automatically so a method knows which object's data to act on.
> 🇨🇳 **A · 自由回忆（范例）：** 一个*类*是一张蓝图，描述某类事物具有的状态和行为；一个*对象*是根据蓝图构建的具体事物（蓝图 → 房屋）。`self` 表示“当前这个特定对象”，自动传入，以便方法知道要操作哪个对象的数据。

**B**
1. The object already exists before `__init__` runs (Python created it); `__init__` only *initializes* its attributes. The real construction is `__new__`.
   > 🇨🇳 1. 对象在 `__init__` 运行之前就已存在（Python 已创建对象）；`__init__` 仅负责*初始化*其属性。真正的构造方法是 `__new__`。
2. *Instance* attributes are per-object (`self.owner`); *class* attributes are one shared copy (`BankAccount.account_count`). Per-object data → instance; shared constants/counters → class.
   > 🇨🇳 2. *实例*属性属于每个对象（`self.owner`）；*类*属性是全体共享的一份数据（`BankAccount.account_count`）。每个对象独有的数据 → 实例属性；共享常量/计数器 → 类属性。
3. Defining a `@property` getter but **no setter** makes it read-only — assignment raises `AttributeError`. You want that for `balance` so it can only change through validated `deposit`/`withdraw` (the invariant).
   > 🇨🇳 3. 定义 `@property` 的 getter 而**不写 setter**，会让属性变为只读——赋值会引发 `AttributeError`。你正希望 `balance` 如此，只能通过经过验证的 `deposit`/`withdraw` 修改（保持不变量）。
4. Returning `self._history` would hand callers your *live* list; they could `.clear()` or append bogus records, corrupting state. `list(self._history)` gives a throwaway copy.
   > 🇨🇳 4. 若返回 `self._history`，会将内部的*活动列表*直接交给调用方；他们可能 `.clear()` 或添加虚假记录，破坏状态。`list(self._history)` 生成一个一次性副本。
5. `tuple += (x,)` rebuilds the whole tuple each append → O(n) per add, O(n²) total. A `list` appends in O(1).
   > 🇨🇳 5. `tuple += (x,)` 每次追加都要重建整个元组 → 每次添加 O(n)，总计 O(n²)。而 `list` 的追加是 O(1)。

**C · Predict the output**
```text
Counter.total      → 0
a.total b.total c.total → 1 1 1
```
> 🇨🇳 以上是程序的预期输出。

`self.total += 1` reads the class value (0), adds 1, and **writes a new instance attribute** that shadows the class one. Each object gets its own `total == 1`; the shared `Counter.total` is never mutated. To count instances you must write `Counter.total += 1`.
> 🇨🇳 `self.total += 1` 读取类属性的值（0），加 1，然后**写入一个新的实例属性**，遮蔽类属性。于是每个对象都得到自己的 `total == 1`；共享的 `Counter.total` 从未被修改。要统计实例个数，必须写 `Counter.total += 1`。

**D · Micro-build**
```python
class Temperature:
    unit_system = "metric"                 # class attribute
    def __init__(self, celsius: float):
        self._celsius = float(celsius)
    @property
    def celsius(self) -> float:            # read-only
        return self._celsius
    @property
    def fahrenheit(self) -> float:         # read-only, computed
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(t.celsius, t.fahrenheit)             # 25.0 77.0
```
> 🇨🇳 这是一个 Temperature 类的微型实现，具有只读的摄氏度和华氏度属性。

**E · Math**
1. `[6, 4]`
   > 🇨🇳 1. `[6, 4]`
2. `[6, 0, -3]`
   > 🇨🇳 2. `[6, 0, -3]`
3. `[0, 0]` — the **zero vector**; `v + (-1)·v` is the *additive inverse* cancelling out.
   > 🇨🇳 3. `[0, 0]` —— **零向量**；`v + (-1)·v` 是*加法逆元*，相互抵消。

## Concept-check answers (homework) / 概念检查答案（作业）
1. **DRY** (Don't Repeat Yourself) / reuse — `transfer` delegates to `withdraw`/`deposit`, so it inherits their validation; re-checking would duplicate logic that could drift.
   > 🇨🇳 1. **DRY**（不要重复自己）/复用 —— `transfer` 委托给 `withdraw`/`deposit`，因此继承了它们的验证；重复检查会复制逻辑且可能不一致。
2. You did **not** write a `@balance.setter`. A getter-only property is read-only.
   > 🇨🇳 2. 你确实**没有**写 `@balance.setter`。只有 getter 的属性是只读的。
3. `BankAccount.account_count` would be **0** — `self.account_count += 1` creates shadowing instance attributes (each `== 1`) and never touches the shared class counter.
   > 🇨🇳 3. `BankAccount.account_count` 会保持 **0** —— `self.account_count += 1` 创建了遮蔽的实例属性（每个 `== 1`），从未触碰共享的类计数器。
