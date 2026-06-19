# 📝 Day 1 Homework — `BankAccount` (calibrated rebuild) / 📝 第1天作业 — `BankAccount`（校准重构）

> **Goal:** a class with a *protected invariant*, validated operations, transaction history, and a working `transfer` — all green, all clean.
> **Time:** 3 h · **Read first:** [`LESSON.md`](./LESSON.md)
> **You did a version of this already (9/10).** This rebuild folds your D1 fixes into the *baseline* spec and adds a rung — so "done" here means past where you were.

> 🇨🇳 **目标：** 一个具有*受保护的不变式*、经过验证的操作、交易历史以及能正常工作的 `transfer`（转账）的类——全部通过、代码整洁。
> 🇨🇳 **时间：** 3 小时 · **首先阅读：** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **你之前已经做过一个版本（9/10）。** 这次重构将你第一天的修复合并到*基线*规范中，并增加了一个台阶——因此这里的“完成”意味着超越你之前的水平。

## 📖 Before you code (edge E1 — spec precision) / 📖 动手前的准备（边界 E1 —— 规范精度）
Read this whole spec **twice**. The tests check the spec *exactly* (e.g. error types, the 2-decimal format, that `transfer` reuses validation). Last time, `transfer` was tested but not implemented — this time it's in the baseline. No red tests at the end.
> 🇨🇳 完整阅读本规范**两遍**。测试会*精确*检查规范（例如错误类型、两位小数格式、`transfer`（转账）复用验证）。上次，`transfer` 被测试但未实现 —— 这次它就在基线中。最终不再有红色测试。

## Requirements (baseline = must all pass) / 需求（基线 = 必须全部通过）

```python
acct = BankAccount("Ben", 100)
acct.balance                 # 100.0  (read-only property — no setter)
acct.deposit(50)             # balance → 150.0
acct.withdraw(30)            # balance → 120.0
acct.balance = 999           # ❌ AttributeError (invariant protected)
acct.deposit(-5)             # ❌ ValueError
acct.withdraw(10_000)        # ❌ ValueError (overdraft)
acct.history()               # list of dict records; a COPY (caller can't mutate internals)
str(acct)                    # "Ben's account — balance: 120.00"   (2 decimals!)
BankAccount.account_count    # increments once per account created
```
> 🇨🇳 示例代码展示了 `BankAccount` 类的期望行为：只读的 `balance` 属性、存款和取款引发 `ValueError` 的条件、历史记录返回副本、以及 `__str__` 的两位小数格式。

### Checklist / 检查清单
- [ ] `__init__(self, owner, balance=0.0)` — store `owner`, `_balance`; init `_history` as a **list**; increment `BankAccount.account_count` (via the **class**, not `self`).
> 🇨🇳 `__init__(self, owner, balance=0.0)` —— 存储 `owner`、`_balance`；将 `_history` 初始化为**列表**；通过**类**（而非 `self`）递增 `BankAccount.account_count`。
- [ ] `balance` — `@property`, **no setter** (read-only).
> 🇨🇳 `balance` —— 定义为 `@property`（装饰器属性），**没有 setter**（只读）。
- [ ] `deposit(amount)` / `withdraw(amount)` — raise `ValueError` on `amount <= 0`; `withdraw` also raises `ValueError` on overdraft. Record each in `_history`.
> 🇨🇳 `deposit(amount)` / `withdraw(amount)` —— 如果 `amount <= 0` 则引发 `ValueError`；`withdraw` 在透支时也会引发 `ValueError`。每次操作记录到 `_history`。
- [ ] `history()` — return a **copy** (`list(self._history)`), so callers can't corrupt state.
> 🇨🇳 `history()` —— 返回一个**副本**（`list(self._history)`），以防调用者破坏内部状态。
- [ ] `transfer(self, target, amount)` — move `amount` to `target` by **reusing** `self.withdraw(amount)` then `target.deposit(amount)` (don't re-validate — inherit it).
> 🇨🇳 `transfer(self, target, amount)` —— 将 `amount` 移至 `target`，通过**复用** `self.withdraw(amount)` 再 `target.deposit(amount)` 实现（不要重新验证——直接继承现有验证逻辑）。
- [ ] `__str__` — `"<owner>'s account — balance: <balance:.2f>"` (the `.2f` matters).
> 🇨🇳 `__str__` —— 格式 `"<owner>'s account — balance: <balance:.2f>"`（`.2f` 很重要）。
- [ ] No dead `pass` after `return`; use `amount <= 0` (not `== 0 or < 0`).
> 🇨🇳 不要在 `return` 之后留下无用的 `pass`；使用 `amount <= 0`（而不要写成 `== 0 or < 0`）。

## Tests (write `test_bank_account.py`) / 测试（编写 `test_bank_account.py`）
Cover at least: deposit/withdraw update balance · overdraft rejected · negative & zero deposit rejected · `balance` is read-only (assigning raises) · history records & returns a **copy** · `account_count` increments · **`transfer` moves funds and a failed transfer (overdraft) leaves *both* balances unchanged.**
> 🇨🇳 至少覆盖：存款/取款更新余额 · 透支被拒绝 · 负数和零存款被拒绝 · `balance` 只读（赋值引发异常） · 历史记录并返回**副本** · `account_count` 递增 · **`transfer`（转账）移动资金，且失败的转账（透支）使*双方*余额保持不变。**

> 🔬 The transfer-atomicity test is the new rung: if `withdraw` raises, `target.deposit` must never run. Because `transfer` calls `withdraw` *first*, this is free — but prove it.
> 🇨🇳 🔬 转账原子性测试是新增的台阶：如果 `withdraw` 引发异常，`target.deposit` 绝不能执行。因为 `transfer` *先*调用 `withdraw`，这一点自然是免费的——但要证明它。

## 🧠 Concept checks (comment at the bottom of `bank_account.py`) / 🧠 概念检查（写在 `bank_account.py` 底部注释中）
1. Why does `transfer` **not** re-check `amount > 0`? What principle is that? (One word.)
> 🇨🇳 为什么 `transfer` **不**重新检查 `amount > 0`？这是什么原则？（一个单词。）
2. What exactly makes `balance` read-only — what did you *not* write?
> 🇨🇳 究竟是什么让 `balance` 变成只读的——你*没有*写什么？
3. If `__init__` used `self.account_count += 1`, what would `BankAccount.account_count` be after 3 accounts, and why?
> 🇨🇳 如果 `__init__` 使用 `self.account_count += 1`，创建 3 个账户后 `BankAccount.account_count` 会是多少，为什么？

## ✅ Definition of done / ✅ 完成定义
- [ ] Every Requirements example behaves as shown · all tests green · concept checks answered
> 🇨🇳 每个需求示例的行为与展示一致 · 所有测试绿色 · 概念检查已回答
- [ ] No red tests, no dead code, history is a `list` · pushed to GitHub
> 🇨🇳 没有红色测试，没有死代码，`history` 是 `list` · 已推送到 GitHub

## 🌟 Stretch (pushes past your prior version) / 🌟 拓展（超越你之前的版本）
- `statement()` → a human-readable multi-line string (aligned columns, signed amounts, 2dp).
> 🇨🇳 `statement()` → 一个人类可读的多行字符串（对齐的列、带正负号的金额、两位小数）。
- A `SavingsAccount(BankAccount)` preview: add `apply_interest(rate)` — *foreshadows D2 inheritance*.
> 🇨🇳 预览 `SavingsAccount(BankAccount)`：增加 `apply_interest(rate)` —— *预示 D2 的继承*。
- Make history records a `@dataclass` `Transaction` — *foreshadows D4*.
> 🇨🇳 将历史记录做成 `@dataclass` `Transaction` —— *预示 D4*。

## 🚀 Submit / 🚀 提交
```bash
git add week01/day01_bankaccount
git commit -m "update: Week1 D1 BankAccount — transfer + list history + 2dp"
git push
```
> 🇨🇳 上述命令：暂存目录、提交并推送，提交信息描述了本次更新内容（转账、列表历史、两位小数）。
➡️ After submitting, do [`RECALL.md`](./RECALL.md) — and again cold tomorrow morning.
> 🇨🇳 ➡️ 提交后，完成 [`RECALL.md`](./RECALL.md) —— 然后明天一早再做一次，趁记忆新鲜。
