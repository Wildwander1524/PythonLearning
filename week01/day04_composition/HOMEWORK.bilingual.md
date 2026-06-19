# 📝 Day 4 Homework — Refactor into `Bank` + `Account` + `Ledger`
> 🇨🇳 **[第4天作业 — 重构为 `Bank` + `Account` + `Ledger`]**

> **Goal:** Take your Day-1 `BankAccount` (which did *everything*) and split it into **composed** parts, each with one job. This is the week's single most important design lesson.
> **Time:** 3 h  ·  **Read first:** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **目标：** 把你第一天写的 `BankAccount`（它包揽了*所有*事情）拆分成**组合**在一起的部分，每个部分只做一件事。这是本周最重要的一堂设计课。
> **时间：** 3 小时  ·  **先读：** [`LESSON.md`](./LESSON.md)

---

## 📖 Before you start (5 min)
> 🇨🇳 **[开始前（5分钟）]**

Skim these sections of [`LESSON.md`](./LESSON.md):
- **"Composition vs inheritance"** (Lego-vs-cast-statue, organs-vs-species) → the has-a / is-a test you'll apply throughout.
- **"The `Stack(list)` trap"** → *why* composing a list beats inheriting from one; your `Ledger` follows the same logic.
- **"`@dataclass`"** (the label-maker) → `Transaction` will be one.
- **"The mutable-default trap"** (the shared-hanger) → use `field(default_factory=list)`, never `= []`.
> 🇨🇳 快速浏览 [`LESSON.md`](./LESSON.md) 的以下部分：
> - **"组合 vs 继承"**（乐高 vs 浇筑雕像，器官 vs 物种）→ 你将全程应用的 has-a / is-a 检验。
> - **"`Stack(list)` 陷阱"** → *为什么*组合一个列表比继承列表更好；你的 `Ledger` 遵循同样的逻辑。
> - **"`@dataclass`"**（标签机）→ `Transaction` 就将是一个数据类。
> - **"可变默认值陷阱"**（共享衣架）→ 使用 `field(default_factory=list)`，永远不要用 `= []`。

> 🎯 **The mantra for today, said out loud:** *"`Account` HAS-A `Ledger`. `Bank` HAS-MANY `Account`s. `Transaction` is just data → `@dataclass`."* If you can say that sentence, you already understand the design.
> 🇨🇳 🎯 **今天请大声念出这句口诀：** *"`Account` 拥有一个 `Ledger`（HAS-A）。 `Bank` 拥有多个 `Account`（HAS-MANY）。 `Transaction` 只是数据 → `@dataclass`。"* 如果你能说出这句话，你就已经理解了这套设计。

---

## ⏱️ Suggested time budget
> 🇨🇳 **[建议时间分配]**

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 45 min | `Ledger` — owns the transaction history (records are a `@dataclass`) |
| **B** | 60 min | `Account` — owns a balance + **has-a** `Ledger` |
| **C** | 60 min | `Bank` — **has-many** `Account`s; open / find / transfer |
| **D** | 35 min | Tests, run, push |

| 模块 | 时间 | 任务 |
|-------|------|------|
| **A** | 45 分钟 | `Ledger` — 拥有交易历史（记录是 `@dataclass`） |
| **B** | 60 分钟 | `Account` — 拥有余额 + **has-a** `Ledger` |
| **C** | 60 分钟 | `Bank` — **has-many** `Account` 实例；开户 / 查找 / 转账 |
| **D** | 35 分钟 | 测试、运行、推送 |

## 📁 Files
> 🇨🇳 **[文件]**

```text
week01/day04_composition/
├── banking.py        # Transaction (dataclass), Ledger, Account, Bank
└── test_banking.py
```
> 🇨🇳 *[文件结构：本周作业目录和文件]*

---

## The design (composition, not one mega-class)
> 🇨🇳 **[设计（组合，而非一个大而全的类）]**

```text
Bank
 ├── has many → Account
 │                ├── balance (float, encapsulated)
 │                └── has-a → Ledger
 │                              └── list of Transaction (dataclass)
```
> 🇨🇳 *[组合设计：Bank 包含多个 Account，每个 Account 包含一个 Ledger，Ledger 包含 Transaction 列表]*

> 🧱 **Why split it (the Lego argument):** in Day 1, one class did balance + validation + history + formatting. That's a cast statue — change one thing, re-cast the whole block. Today each brick does one job, snaps to the others, and can be tested/replaced alone. That feeling — "each piece does one thing" — is the goal.
> 🇨🇳 🧱 **为什么要拆分（乐高论证）：** 第一天里，一个类同时处理余额 + 校验 + 历史记录 + 格式化。那就像一座浇铸的雕像——改一处就要重新浇铸整块。今天每一块积木只做一件事，彼此卡合，可以单独测试/替换。那种"每个部件只做一件事"的感觉——就是今天的目标。

## Part A — `Transaction` + `Ledger` (45 min)
> 🇨🇳 **[Part A — `Transaction` + `Ledger`（45 分钟）]**

- [ ] `Transaction` as a `@dataclass`: `kind: str`, `amount: float`, `balance_after: float`. (Free `__repr__`/`__eq__` — the label-maker.)
> 🇨🇳 `Transaction` 定义为 `@dataclass`：字段 `kind: str`、`amount: float`、`balance_after: float`（免费获得 `__repr__`/`__eq__`——就像标签机）。
- [ ] `Ledger` holds a `list[Transaction]` (init via `__init__` or `field(default_factory=list)` — **never** `= []`).
> 🇨🇳 `Ledger` 持有一个 `list[Transaction]`（通过 `__init__` 或 `field(default_factory=list)` 初始化——**永远不要**用 `= []`）。
- [ ] `Ledger.record(kind, amount, balance_after)` appends a `Transaction`.
> 🇨🇳 `Ledger.record(kind, amount, balance_after)` 方法追加一条 `Transaction`。
- [ ] `Ledger.entries()` returns a **copy** of the list (copy-on-read — the Day-1 encapsulation lesson).
> 🇨🇳 `Ledger.entries()` 返回列表的**副本**（读时复制——第一天学到的封装原则）。
- [ ] `Ledger.__len__` returns the number of transactions.
> 🇨🇳 `Ledger.__len__` 返回交易条数。

## Part B — `Account` (60 min)
> 🇨🇳 **[Part B — `Account`（60 分钟）]**

- [ ] `Account(owner, balance=0)` creates `self._ledger = Ledger()` (**composition** — Account *has-a* Ledger).
> 🇨🇳 `Account(owner, balance=0)` 在内部创建 `self._ledger = Ledger()`（**组合** —— Account 拥有一个 Ledger）。
- [ ] Keep your D1 wins: private `_balance`, read-only `balance` property, validation (`amount <= 0`, overdraft).
> 🇨🇳 保留第一天的成果：私有属性 `_balance`、只读的 `balance` 属性、校验（`amount <= 0`、透支检查）。
- [ ] `deposit` / `withdraw` update the balance **and** call `self._ledger.record(...)`.
> 🇨🇳 `deposit` / `withdraw` 方法更新余额**并**调用 `self._ledger.record(...)`。
- [ ] `statement()` *delegates* to the ledger to print history (Account no longer manages a raw list).
> 🇨🇳 `statement()` *委托*给 ledger 来打印历史记录（Account 不再直接管理原始列表）。

## Part C — `Bank` (60 min)
> 🇨🇳 **[Part C — `Bank`（60 分钟）]**

- [ ] `Bank(name)` holds `self._accounts` — a `dict[str, Account]` keyed by owner.
> 🇨🇳 `Bank(name)` 维护 `self._accounts`——一个以户主名为键的 `dict[str, Account]`。
- [ ] `open_account(owner, initial=0) -> Account`
> 🇨🇳 `open_account(owner, initial=0) -> Account`
- [ ] `get(owner) -> Optional[Account]` (use the type hint from `LEARNING.md`)
> 🇨🇳 `get(owner) -> Optional[Account]`（使用 `LEARNING.md` 中介绍的类型提示）
- [ ] `transfer(from_owner, to_owner, amount)` — look up both, then `withdraw` + `deposit`. **Reuse** those methods so validation/overdraft come for free (don't re-validate here).
> 🇨🇳 `transfer(from_owner, to_owner, amount)` —— 查找两个账户，然后调用 `withdraw` 和 `deposit`。**复用**这些方法，校验和透支检查就会自动生效（不要在这里重复校验）。
- [ ] `total_assets() -> float` — sum of all account balances.
> 🇨🇳 `total_assets() -> float` —— 所有账户余额的总和。

## Tests (Block D)
> 🇨🇳 **[测试（模块 D）]**

- [ ] Opening 2 accounts → `bank.total_assets()` is their sum
> 🇨🇳 开立两个账户 → `bank.total_assets()` 应等于这两者之和
- [ ] `deposit` then `withdraw` → that account's ledger has the right number of entries
> 🇨🇳 先存款再取款 → 该账户的 ledger 中交易条数正确
- [ ] `transfer` moves money correctly **and** is rejected on overdraft (raises `ValueError`)
> 🇨🇳 `transfer` 能正确转账**并且**在透支时被拒绝（抛出 `ValueError`）
- [ ] `Ledger.entries()` returns a copy (mutating the returned list doesn't change the ledger)
> 🇨🇳 `Ledger.entries()` 返回的是副本（修改返回的列表不会影响 ledger 内部数据）
- [ ] `bank.get("nobody")` returns `None`
> 🇨🇳 `bank.get("nobody")` 返回 `None`

---

## 🧠 Concept checks (comment at the bottom of `banking.py`)
> 🇨🇳 **[概念检查（写在 `banking.py` 底部的注释中）]**

1. Why is `Account` *has-a* `Ledger` rather than `Account(Ledger)` (inheritance)? Say it with the is-a/has-a test.
> 🇨🇳 1. 为什么 `Account` 是*拥有一个* `Ledger`（has-a），而不是 `Account(Ledger)`（继承）？请用 is-a / has-a 检验回答。
2. What does `transfer` gain by *reusing* `withdraw`/`deposit` instead of editing balances directly?
> 🇨🇳 2. `transfer` 通过*复用* `withdraw`/`deposit` 而不是直接编辑余额，获得了什么好处？
3. Open `day01_bankaccount/bank_account.py` side by side. Name one thing that's now easier to test in isolation than it was in Day 1.
> 🇨🇳 3. 并排打开 `day01_bankaccount/bank_account.py`，说出一个现在可以更容易独立测试的地方（相比第一天）。

## ✅ Definition of done
> 🇨🇳 **[完成的定义]**

- [ ] Four classes, each with a single clear responsibility
> 🇨🇳 四个类，每个类承担一项清晰的职责
- [ ] `Account` **has-a** `Ledger`; `Bank` **has-many** `Account`s (composition throughout)
> 🇨🇳 `Account` **has-a** `Ledger`；`Bank` **has-many** `Account`（全程使用组合）
- [ ] `Transaction` is a `@dataclass`; no mutable-default bug
> 🇨🇳 `Transaction` 是 `@dataclass`；没有可变默认值的 bug
- [ ] All tests pass; concept checks answered; pushed to GitHub
> 🇨🇳 所有测试通过；概念检查已回答；代码已推送到 GitHub

## 🌟 Stretch
> 🇨🇳 **[进阶挑战]**

- `Bank.richest_customer() -> Account` using `max(..., key=...)`.
> 🇨🇳 `Bank.richest_customer() -> Account`，使用 `max(..., key=...)` 实现。
- Make `Transaction` `frozen=True` (immutable) and add `timestamp` defaulting via `field(default_factory=datetime.now)`.
> 🇨🇳 将 `Transaction` 设为 `frozen=True`（不可变），并添加 `timestamp` 字段，默认值用 `field(default_factory=datetime.now)`。
- Add a `min_balance` policy to `Account`, raising a custom exception on violation (previews Day 5).
> 🇨🇳 给 `Account` 添加 `min_balance` 策略，违反时抛出自定义异常（为第 5 天做准备）。
- Rebuild `Stack` two ways — `class Stack(list)` vs a composed `self._items` — and write one sentence on why the composed version is safer (the leak from `LEARNING.md`).
> 🇨🇳 用两种方式重建 `Stack`：`class Stack(list)` 与组合版的 `self._items`，并写一句话说明为什么组合版本更安全（参考 `LEARNING.md` 里的"泄漏"问题）。

---

## 🚀 Submit
> 🇨🇳 **[提交]**

```bash
git add week01/day04_composition
git commit -m "add: Week1 D4 composed Bank/Account/Ledger"
git push
```
> 🇨🇳 *[提交命令]*

➡️ Then [`RECALL.md`](./RECALL.md), and again cold before Day 5.
> 🇨🇳 然后复习 [`RECALL.md`](./RECALL.md)，并在第 5 天开始前再冷回想一次。
