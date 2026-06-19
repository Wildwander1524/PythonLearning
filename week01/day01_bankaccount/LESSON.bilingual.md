# 📘 Day 1 — Classes, Objects & Encapsulation / 📘 第一天 — 类、对象与封装

> **Week 1 · Mon 2026-06-16** · Curriculum: Python OOP · Math: Linear Algebra I (vectors)
> **Read this actively.** Every `✍️ Self-explain` and `🔮 Predict` box is a *retrieval* point — answer it in your head (or out loud) *before* reading on. That tiny effort is what converts "I read it" into "I can do it tomorrow." (See [`../RESOURCES.md`](../RESOURCES.md) §Pedagogy.)

> 🇨🇳 **第一周 · 周一 2026-06-16** · 课程：Python OOP · 数学：线性代数 I（向量）
> 🇨🇳 **积极阅读。** 每一个 `✍️ Self-explain` 和 `🔮 Predict` 框都是一个*检索*点——在继续阅读之前，先在脑中（或大声）回答它。正是这种微小的努力，把“我读过”转化为“我明天就能做到”。（参见 [`../RESOURCES.md`](../RESOURCES.md) §Pedagogy。）

## 🎯 Objectives & mastery bar / 🎯 目标与掌握标准

| Objective | Bloom level | You've mastered it when… |
|-----------|-------------|--------------------------|
| Define a class with `__init__`/`self` | Apply | you write one from a blank file without looking |
| Distinguish instance vs **class** attributes | Understand | you can explain why `self.count += 1` breaks a shared counter |
| Enforce an invariant via `@property` | Apply | you build a value nobody outside the class can corrupt |
| Vectors: notation, add, scalar-multiply | Understand | you add/scale by hand and say what it means geometrically |

| 目标 | 布鲁姆等级 | 掌握标准 |
|------|------------|----------|
| 用 `__init__`/`self` 定义一个类 | Apply（应用） | 你可以在空白文件中不看参考写出一个 |
| 区分实例属性和**类**属性 | Understand（理解） | 你能解释为何 `self.count += 1` 会破坏共享计数器 |
| 通过 `@property` 强制执行不变量 | Apply（应用） | 你构建了一个外部无人能篡改的值 |
| 向量：记号、加法、标量乘法 | Understand（理解） | 你能手动加/缩放并说出其几何意义 |

**What's new vs. what you know:** if you've used functions and dicts, you already group *data* (a dict) and *behaviour* (functions). A **class** is the idea that those two belong *together*. Today is the foundation the rest of the week stands on — so we go slow on the "why."

> 🇨🇳 **新旧对比：** 如果你用过函数和字典，你已经将*数据*（字典）和*行为*（函数）分组了。**class（类）** 的思想就是这两者应该*在一起*。今天是一周其余内容的基础——所以我们会慢慢讲解“为什么”。

## The big picture: an object bundles state + behaviour / 大图景：对象将状态与行为捆绑在一起

A `dict` holds data. A function does work. The insight of object-orientation is that most real things are *both at once*: a bank account **has** a balance (state) **and** can deposit or withdraw (behaviour). A **class** is a blueprint that fuses them; an **object** (or *instance*) is one concrete thing built from that blueprint.

> 🇨🇳 `dict（字典）` 存放数据。函数执行工作。面向对象的洞见在于，大多数真实事物*同时兼具两者*：一个银行账户**拥有**余额（状态）**并且**能够存款或取款（行为）。**class（类）** 是将它们融合在一起的蓝图；**object（对象）**（或*instance（实例）*）则是根据该蓝图构建出的一个具体事物。

> 🏗️ **Analogy — blueprint vs house.** The class `BankAccount` is the architectural blueprint: it describes what *every* account will have (a balance) and do (deposit). Each actual account — yours, mine — is a **house** built from that one blueprint. One blueprint, many houses; change the blueprint and every house built afterward follows it.

> 🇨🇳 🏗️ **类比——蓝图与房屋。** 类 `BankAccount` 就是建筑蓝图：它描述了*每个*账户将**拥有**什么（余额）和**做**什么（存款）。每一个实际账户——你的、我的——都是用这张蓝图建成的**房屋**。一张蓝图，多座房屋；修改蓝图，此后建造的所有房屋都会遵循它。

This "state + behaviour together, behind a clean interface" idea is the whole game. Berkeley's CS61A frames it as *data abstraction* — a user of your object should be able to use it correctly while knowing nothing about how it stores its data internally ([Composing Programs, Ch. 2](https://www.composingprograms.com/)).

> 🇨🇳 这个“状态与行为结合，隐藏在一个清晰接口之后”的思想是整个核心。伯克利 CS61A 将其表述为*数据抽象*——你的对象的用户应能在完全不知晓其内部如何存储数据的情况下正确使用它（[Composing Programs, Ch. 2](https://www.composingprograms.com/)）。

## S1 — Classes, `__init__`, and `self` / S1 — 类、`__init__` 与 `self`

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner          # instance attribute — unique to THIS account
        self._balance = balance     # leading _ = "internal, please don't touch directly"

    def deposit(self, amount: float) -> None:
        self._balance += amount
```
> 🇨🇳 这段代码定义了一个 `BankAccount` 类，包含初始化方法 `__init__` 和存款方法 `deposit`。

Three things that trip people up, made precise:

1. **`__init__` is not "the constructor" — it's the *initializer*.** By the time `__init__` runs, the object already exists (Python built it). `__init__`'s only job is to *furnish* it with starting attributes. `acct = BankAccount("Ben", 100)` creates the blank object, then calls `__init__(acct, "Ben", 100)`.

> 🇨🇳 1. **`__init__` 不是“构造函数”——它是*初始化器*。** 当 `__init__` 运行时，对象已经存在（Python 已创建了它）。`__init__` 的唯一工作是用起始属性将其*布置*妥当。`acct = BankAccount("Ben", 100)` 先创建空白对象，然后调用 `__init__(acct, "Ben", 100)`。

2. **`self` is just "this particular object."** It's the first parameter of every method, and Python passes it automatically: `acct.deposit(50)` becomes `BankAccount.deposit(acct, 50)`. `self` is how a method knows *which* account's balance to change.

> 🇨🇳 2. **`self` 就是“这个特定的 object（对象）”。** 它是每个方法的第一个参数，Python 会自动传入：`acct.deposit(50)` 变成 `BankAccount.deposit(acct, 50)`。`self` 就是方法知晓要更改*哪个*账户的余额的方式。

3. **Assigning `self.x` creates/sets an attribute on this object.** There's no separate "declare your fields" step — attributes spring into existence when you assign them.

> 🇨🇳 3. **给 `self.x` 赋值会在这个 object（对象）上创建/设置一个 attribute（属性）。** 没有单独的“声明字段”步骤—— attribute（属性）会在你赋值时立即诞生。

> 🧠 **Under the hood — an object is (almost) a dict.** Each instance carries a hidden `__dict__` mapping attribute names to values. `self.owner = "Ben"` literally does `acct.__dict__["owner"] = "Ben"`. Run `print(acct.__dict__)` and you'll *see* it. This demystifies attributes: they're dictionary entries with nicer syntax. (Day 4's `__slots__` is about *removing* this dict to save memory.)

> 🇨🇳 🧠 **底层原理——一个 object（对象）几乎就是一个 dict（字典）。** 每个 instance（实例）都携带一个隐藏的 `__dict__`，它把 attribute（属性）名映射到值。`self.owner = "Ben"` 实际上做的就是 `acct.__dict__["owner"] = "Ben"`。运行 `print(acct.__dict__)` 就会看到它。这就揭开了 attribute（属性）的神秘面纱：它们就是拥有更漂亮语法的字典条目。（第4天的 `__slots__` 讲的是如何*移除*这个字典以节省内存。）

> ✍️ **Self-explain:** in `acct.deposit(50)`, you wrote one argument (`50`) but `deposit` is defined with two parameters (`self, amount`). Where did `self` come from? Say it before reading on. *(Answer: `acct.deposit(50)` is sugar for `BankAccount.deposit(acct, 50)` — the object left of the dot becomes `self`.)*

> 🇨🇳 ✍️ **自我解释：** 在 `acct.deposit(50)` 中，你写了一个实参（`50`），但 `deposit` 却定义了两个形参（`self, amount`）。`self` 是从哪里来的？在往下读之前先说出来。*（答案：`acct.deposit(50)` 是 `BankAccount.deposit(acct, 50)` 的语法糖——点号左边的 object（对象）就成了 `self`。）*

## S2 — Instance vs. class attributes (the bug that bit you on Day 1's counter) / S2 — 实例属性 vs. 类属性（Day 1 计数器中咬你的 bug）

```python
class BankAccount:
    bank_name = "PythonLearning Bank"   # CLASS attribute — ONE copy, shared by all accounts
    account_count = 0                   # CLASS attribute — a shared counter

    def __init__(self, owner):
        self.owner = owner              # INSTANCE attribute — a separate copy per account
        BankAccount.account_count += 1  # ✅ increment the SHARED counter on the CLASS
```
> 🇨🇳 这段代码演示了类属性（`bank_name`, `account_count`）与实例属性（`self.owner`）的区别，并在 `__init__` 中正确递增共享计数器。

| | Instance attribute | Class attribute |
|---|---|---|
| Defined by | `self.x = ...` inside a method | `x = ...` directly in the class body |
| Lives | one copy **per object** | **one** copy, shared by all objects |
| Use for | per-object state (owner, balance) | shared constants / counters (`bank_name`, `account_count`) |

| | Instance attribute（实例属性） | Class attribute（类属性） |
|---|---|---|
| 定义方式 | 在方法内部通过 `self.x = ...` 定义 | 直接在类体中通过 `x = ...` 定义 |
| 存放位置 | 每个 object（对象）**一份** | **一份**拷贝，由所有 object（对象）共享 |
| 用途 | 逐对象的状态（所有者、余额） | 共享常量 / 计数器（`bank_name`、`account_count`） |

> 🔮 **Predict (this is exactly the slip to immunize against):** suppose `__init__` had `self.account_count += 1` instead of `BankAccount.account_count += 1`. After making 3 accounts, what does `BankAccount.account_count` equal? What does each account's `.account_count` equal?
>
> <details><summary>reveal</summary>
>
> `BankAccount.account_count` stays **0**. Reason: `self.account_count += 1` reads the class value (0) on the first hit, adds 1, and writes the result to a *new instance* attribute that **shadows** the class one. Each account ends up with its own `account_count == 1`; the shared class counter is never touched. **Mutating shared state must go through the class (`BankAccount.account_count`), not `self`.**
> </details>

> 🇨🇳 🔮 **预测（这正是一个需要免疫的失误）：** 假设 `__init__` 中写的是 `self.account_count += 1` 而非 `BankAccount.account_count += 1`。在创建了3个账户后，`BankAccount.account_count` 等于什么？每个账户的 `.account_count` 又等于什么？
> 🇨🇳 <details><summary>揭示</summary>
> 🇨🇳 `BankAccount.account_count` 保持为 **0**。原因：`self.account_count += 1` 第一次读取类值（0），加1，然后将结果写入一个*新的 instance（实例）*属性，该属性**遮蔽**了类属性。每个账户最终拥有自己的 `account_count == 1`；共享的类计数器从未被触及。**修改共享状态必须通过类（`BankAccount.account_count`），而不是通过 `self`。**
> 🇨🇳 </details>

## S2b — Encapsulation & `@property`: build an invariant nobody can break / S2b — 封装与 `@property`：构建一个无人能破的不变量

A balance should never be settable to garbage from outside, and should never be silently overwritten. Encapsulation = hide the raw data, expose a *controlled* interface.

> 🇨🇳 余额永远不应被外部设为垃圾值，也不应被悄悄覆盖。encapsulation（封装）= 隐藏原始数据，暴露一个*受控*的接口。

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance         # _name = convention for "internal"

    @property
    def balance(self) -> float:         # read access: acct.balance  (looks like an attribute)
        return self._balance            # NO setter defined → acct.balance = 999 raises AttributeError
```
> 🇨🇳 这段代码通过 `@property` 将 `balance` 设置为只读属性，防止外部直接赋值修改。

- `acct.balance` *calls* the method but *reads* like a plain attribute — callers don't change how they use it. (CS61A/CS106 call this preserving the *interface* while controlling the *implementation*.)

> 🇨🇳 - `acct.balance` *调用*方法，但*读取*起来就像一个普通 attribute（属性）——调用者无需改变使用方式。（CS61A/CS106 称之为在控制*实现*的同时保持*接口*不变。）

- **No `@balance.setter`** ⇒ the balance is **read-only from outside**. The only way it changes is through `deposit`/`withdraw`, which can *validate*. That's the invariant: balance only ever moves through code you control.

> 🇨🇳 - **没有 `@balance.setter`** ⇒ 余额是**从外部只读的**。它改变的唯一途径是通过 `deposit`/`withdraw`，它们可以进行*验证*。这就是不变量：余额只通过你控制的代码变动。

> 🔒 **Analogy — a bank teller window.** Your cash (`_balance`) is in the vault, not on the counter. Customers don't reach into the vault; they slide a request through the window (`deposit`/`withdraw`), and the teller checks it's valid first. `@property` is the window: you can *see* the total, but you can't *set* it by reaching in.

> 🇨🇳 🔒 **类比——银行出纳窗口。** 你的现金（`_balance`）在保险库里，不在柜台上。客户不能直接伸手进保险库；他们通过窗口递入请求（`deposit`/`withdraw`），出纳员首先检查其有效性。`@property` 就是那个窗口：你能*看到*总额，但不能伸手进去*设置*。

> ✍️ **Self-explain:** your Day-1 code stored history as a tuple grown with `+=`. Why is a `list` with `.append()` the right tool here? *(Tuples are immutable, so `t += (x,)` builds a brand-new tuple and copies every element each time — O(n) per append, O(n²) total. A list appends in O(1). Right container = right cost.)*

> 🇨🇳 ✍️ **自我解释：** 你第1天的代码将历史记录存储为一个通过 `+=` 增长的元组。为什么用 `list` 配合 `.append()` 才是正确的工具？*（元组是不可变的，所以 `t += (x,)` 每次都会构建一个全新的元组并拷贝所有元素——每次追加 O(n)，总计 O(n²)。list（列表）追加是 O(1)。正确的容器 = 正确的开销。）*

## S3 — Math: vectors (the first rung of the linear-algebra ladder) / S3 — 数学：向量（线性代数阶梯的第一级）

A **vector** is an ordered list of numbers — *and* an arrow in space. Hold both pictures.

> 🇨🇳 **vector（向量）** 是一个有序的数字列表——*也*是空间中的一个箭头。请同时持有这两幅图景。

```text
v = [3, 4]          # "list of numbers" picture  AND  "arrow from origin to (3,4)" picture
```
> 🇨🇳 这行文本表示一个向量：既是数字列表 `[3,4]`，也是从原点到 (3,4) 的箭头。

**Addition** (component-wise) = "do one trip, then the other":
```text
[1, 2] + [3, 1] = [1+3, 2+1] = [4, 3]
```
> 🇨🇳 向量加法（分量式）= “先走一段，再走另一段”。

**Scalar multiplication** = "stretch/shrink the arrow":
```text
3 · [1, 2] = [3, 6]      # same direction, 3× longer
-1 · [1, 2] = [-1, -2]   # same length, opposite direction
```
> 🇨🇳 标量乘法 = “拉伸/缩短箭头”。

> 🚶 **Analogy — walking instructions.** `[3, 4]` = "3 east, 4 north." Adding vectors = doing the two walks back-to-back; you end up at the sum. Scaling by 3 = doing the same walk three times as far. This "arrows you add and stretch" picture is the foundation 3Blue1Brown builds everything else on — watch *Essence of Linear Algebra* Ch.1 tonight ([3b1b](https://www.3blue1brown.com/topics/linear-algebra)).

> 🇨🇳 🚶 **类比——行走指令。** `[3, 4]` = “向东3，向北4”。向量相加 = 连着走两段路程；你最终会到达和的位置。缩放3倍 = 沿同一路线走三倍远。这幅“你可以相加和拉伸的箭头”图景，是 3Blue1Brown 构建其他一切的基础——今晚观看 *Essence of Linear Algebra* 第1章（[3b1b](https://www.3blue1brown.com/topics/linear-algebra)）。

> 🔮 **Predict, then check by hand:** ① `[2, -1] + [1, 5]` = ? ② `0.5 · [4, 10]` = ? ③ what arrow is `[3,4] + (-1)·[3,4]`? *(Answers: `[3,4]`; `[2,5]`; the zero vector `[0,0]` — a vector plus its negative cancels, just like `5 + (-5) = 0`.)*

> 🇨🇳 🔮 **预测，然后手动验证：** ① `[2, -1] + [1, 5]` = ? ② `0.5 · [4, 10]` = ? ③ `[3,4] + (-1)·[3,4]` 是什么箭头？*（答案：`[3,4]`；`[2,5]`；零向量 `[0,0]` —— 一个向量加上其负向量会抵消，就像 `5 + (-5) = 0`。）*

*Tomorrow (D2) this becomes the **dot product** — the single most important operation for your LLM career. Today's "add and scale" is its prerequisite.*

> 🇨🇳 *明天（第二天）这将是**点积**——对你 LLM 职业生涯最重要的一种运算。今天的“加法和缩放”是它的前提。*

## S4 — Frontier: a working environment + Git / S4 — 前沿：一个可工作的环境 + Git

Today's frontier slot is *runway-building*, not reading. Goal: Python runs, Git tracks your work, the repo is on GitHub. Per [`../RESOURCES.md`](../RESOURCES.md) §E your envs are already installed — so this is mostly *verification*.

> 🇨🇳 今天的前沿时段是*跑道建设*，而非阅读。目标：Python 能运行，Git 跟踪你的工作，仓库在 GitHub 上。根据 [`../RESOURCES.md`](../RESOURCES.md) §E，你的环境已经安装好了——所以这主要是*验证*。

```bash
python --version                 # any 3.10+ is fine for Week 1
cd E:/Code/MyProjects/PythonLearning
git status                       # clean working tree?
python week01/day01_bankaccount/bank_account.py   # your code runs?
```
> 🇨🇳 这几条命令用于检查 Python 版本、进入项目目录、查看 Git 状态，并运行你的银行账户代码以确保一切正常。

> 🧰 **Why now?** You won't train a model for weeks, but a learner who fights their tools every day burns energy that should go to concepts. Tools sorted once = friction-free for 13 weeks.

> 🇨🇳 🧰 **为什么现在？** 你几周内还不会训练模型，但一个每天与工具作斗争的学习者会把本应用在概念上的精力消耗掉。工具一次搞定 = 13 周零摩擦。

## 🧠 Cheat-sheet / 🧠 速查表

```python
class Thing:
    shared = 0                      # CLASS attribute (one copy, all instances)
    def __init__(self, x):
        self.x = x                  # INSTANCE attribute (per object)
        Thing.shared += 1           # mutate shared state via the CLASS, never self
    @property
    def value(self):                # read like an attribute (thing.value)
        return self._v              # no setter ⇒ read-only ⇒ invariant protected
```
> 🇨🇳 这段代码展示了类定义的基本结构：类属性、实例属性、通过类修改共享状态，以及使用 `@property` 保护只读属性。

| Term | One-liner | Analogy |
|------|-----------|---------|
| class / object | blueprint / a house built from it | architectural plan |
| `__init__` | *initializes* an already-created object | furnishing an empty house |
| `self` | "this particular object" | the house being worked on |
| instance attr | per-object state (`self.x`) | each house's furniture |
| class attr | shared across all (`Class.x`) | the shared blueprint label |
| `@property` (no setter) | controlled, read-only access | the teller window |
| vector add / scale | component-wise / stretch | back-to-back walks / longer walk |

| 术语 | 一句话 | 类比 |
|------|--------|------|
| class(类) / object(对象) | 蓝图 / 根据蓝图建造的房屋 | 建筑平面图 |
| `__init__` | *初始化*一个已创建的对象 | 给空房子配备家具 |
| `self` | “这个特定的对象” | 正在被施工的房屋 |
| instance attr(实例属性) | 逐对象的状态（`self.x`） | 每座房屋的家具 |
| class attr(类属性) | 在所有对象间共享（`Class.x`） | 共享的蓝图标签 |
| `@property`（无 setter） | 受控的只读访问 | 出纳窗口 |
| vector(向量)加法/缩放 | 分量式 / 拉伸 | 连续走路 / 更长的行走 |

## ⚠️ Common pitfalls / ⚠️ 常见陷阱

1. **`self.counter += 1` on a shared counter** → creates a shadowing instance attribute; the class counter never moves. Mutate via `Class.counter`.

> 🇨🇳 1. **在共享计数器上使用 `self.counter += 1`** → 会创建一个遮蔽的 instance attribute（实例属性）；类计数器纹丝不动。应通过 `Class.counter` 修改。

2. **A settable balance** (`acct.balance = 999`) → skips validation, breaks the invariant. Omit the setter to make it read-only.

> 🇨🇳 2. **可设置的余额**（`acct.balance = 999`）→ 跳过了验证，破坏了不变量。省略 setter 使其只读。

3. **Tuple grown with `+=` for history** → O(n²). Use a `list` + `.append()`.

> 🇨🇳 3. **用 `+=` 扩展元组记录历史** → O(n²)。使用 `list`（列表）配合 `.append()`。

4. **Leaving a `transfer()` test red** → never commit a failing test you wrote. Implement it or delete it. (This is growth-edge **E4** from [`../MISSION.md`](../MISSION.md).)

> 🇨🇳 4. **让 `transfer()` 测试保持红色** → 永远不要提交你编写的失败测试。要么实现它，要么删除它。（这是 [`../MISSION.md`](../MISSION.md) 中的成长边界 **E4**。）

## ✅ Storage-strength check (do this from memory tomorrow, not today) / ✅ 存储强度检查（明天凭记忆做，不是今天）

Without looking: (a) write a 6-line class with one class attribute and one read-only property; (b) state the instance-vs-class rule in one sentence; (c) compute `[2,3] + 2·[1,-1]`. If any is shaky, that's your re-read target — note it in [`../learning-records/`](../learning-records/).

> 🇨🇳 不看材料：（a）编写一个 6 行的类，包含一个 class attribute（类属性）和一个只读 property（属性）；（b）用一句话说明实例与类的规则；（c）计算 `[2,3] + 2·[1,-1]`。如果任何一处有动摇，那就是你需要重读的目标——将其记录在 [`../learning-records/`](../learning-records/) 中。

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md). Re-read the spec **twice** before coding (edge E1).

> 🇨🇳 ➡️ **构建它：** [`HOMEWORK.md`](./HOMEWORK.md)。在编码前把规范**读两遍**（边界 E1）。
