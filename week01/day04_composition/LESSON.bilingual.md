# 📘 Day 4 — Composition, `@dataclass` & Design Judgment
> 🇨🇳 **[Day 4 — 组合、`@dataclass` 与设计判断]**

> **Week 1 · Thu 2026-06-19** · Curriculum: Python OOP · Math: matrix×matrix, identity, inverse
> Days 2–3 gave you *mechanisms* (inheritance, dunders). **Today is judgment** — *when* to use
> which. The headline — **"prefer composition over inheritance"** — is one of the most-repeated
> rules in software engineering; tonight you'll understand *why* in your bones.
> 🇨🇳 **第一周 · 周四 2026-06-19** · 课程：Python 面向对象 · 数学：矩阵乘法、单位阵、逆矩阵
> 第2–3天让你掌握了*机制*（继承、双下划线方法）。**今天是判断力** —— *何时*用哪种。标题——
> **"优先组合而非继承"**——是软件工程中被重复最多的规则之一；今晚你将骨子里明白*为什么*。

## 🎯 Objectives & mastery bar
> 🇨🇳 **[目标与掌握标准]**

| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Choose composition vs inheritance | **Analyze** | you justify each with the is-a/has-a test |
| Use `@dataclass` (incl. mutable-default safety) | Apply | you write one and spot the `= []` bug unprompted |
| Read/write type hints; know they're not enforced | Understand | you explain "signage, not guards" |
| Math: matrix×matrix, identity, inverse | Understand | you apply the domino rule and predict `A·I` |

| 目标 | Bloom层级 | 掌握标准… |
|------|-----------|------------|
| 选择组合还是继承 | **分析** | 能用 is-a/has-a 判断来论证每一次选择 |
| 使用 `@dataclass`（含可变默认值安全性） | 应用 | 能不受提示地写出一个并发现 `= []` 的 bug |
| 读写类型提示；知道它们运行时不被强制执行 | 理解 | 能解释"路牌，不是门卫" |
| 数学：矩阵乘法、单位阵、逆矩阵 | 理解 | 能运用多米诺规则预测 `A·I` |

## 🔁 Spaced callbacks (cold, first — re-tests D2 + D3)
> 🇨🇳 **[间隔回调（冷启动，首次——重测 D2 + D3）]**

C1 (D2) what does an **ABC** guarantee, and when does it reject a bad subclass? C2 (D3) you
defined `__eq__`; why won't your object go in a `set`, and what's the fix? C3 (D3) what must
`a + b` return?

MY ANSWER:
C1: it guarantees that all subclasses implement the abstract methods; it rejects a bad subclass at
instantiation time
C2: Because hashable objects must have a `__hash__` method, and defining `__eq__` without `__hash__` makes the object unhashable. The fix is to define a `__hash__` method that is consistent with `__eq__`.
C3: `a + b` must return a new object that represents the sum of `a` and `b`
> 🇨🇳 C1 (D2) 抽象基类保证什么？它何时拒绝一个错误的子类？ C2 (D3) 你定义了 `__eq__`；为什么你的对象
> 放不进 `set`，以及如何修正？ C3 (D3) `a + b` 必须返回什么？

---

## S1 — Composition vs inheritance
> 🇨🇳 **[S1 — 组合 vs 继承]**

| Relationship | Test | Mechanism | Example |
|--------------|------|-----------|---------|
| **Inheritance** | "A *is a* B" | subclassing | `Dog` is an `Animal` |
| **Composition** | "A *has a* B" | hold it as an attribute | `Car` has an `Engine` |

| 关系 | 测试 | 机制 | 示例 |
|------|------|------|------|
| **继承** | "A **是** B" | 子类化 | `Dog` 是 `Animal` |
| **组合** | "A **有** B" | 将其作为属性持有 | `Car` 有 `Engine` |

```python
class Car:
    def __init__(self):
        self.engine = Engine()          # HAS-A: the Car owns an Engine
    def start(self):
        return self.engine.start()      # and delegates to it
```
> 🇨🇳 *[组合示例——Car 持有 Engine 对象并将 start 方法委托给它]*

> 🧱 **Lego vs a cast statue.** Composition = Lego: independent bricks snap together; swap the
> engine without touching the rest. Inheritance = one cast statue: to change the arm you re-cast
> the whole thing, and every copy changes too. Software changes constantly → reach for Lego.
> 🇨🇳 🧱 **乐高与浇铸雕像。** 组合 = 乐高：独立的积木拼接在一起；换发动机不必碰其余部分。
> 继承 = 一座浇铸雕像：要换手臂就得重新浇铸整个雕像，所有副本也都跟着变。软件不断变化 → 去拿乐高。

### Why "prefer composition" — the fragile base class problem
> 🇨🇳 **[为什么"优先组合"——脆弱的基类问题]**

Inheritance couples a child to the parent's *internals*. Change the parent and you can silently
break every child — even ones written by people who never saw your change.
> 🇨🇳 继承将子类耦合到父类的*内部实现*。改动父类可能悄无声息地破坏所有子类——甚至是那些从未见过你修改的人写的。

> 💣 **Renovating a tower's ground floor.** Subclasses are floors stacked on the base; move a
> load-bearing wall (a base method) and floors 2–40 crack. With composition the pieces are
> neighboring houses joined by a clear road (the public interface) — renovate inside one, the
> neighbors don't care. Loose coupling = survivable software.
> 🇨🇳 💣 **改造塔楼的底层。** 子类是堆叠在基础上的楼层；移动一面承重墙（基类方法），2到40层全裂。
> 组合中的组件就像通过清晰的马路（公共接口）相连的邻居房屋——在其中一间内部翻修，邻居毫不关心。
> 松耦合 = 可存活的软件。

**The classic trap — `Stack(list)`:**
```python
class Stack(list):                 # ❌ inheriting LEAKS all 40 list methods
    def push(self, x): self.append(x)
s = Stack(); s.push(1); s.insert(0, 99); s.sort()   # 😱 a "stack" you can insert into and sort?!

class Stack:                       # ✅ compose: expose ONLY push/pop
    def __init__(self): self._items = []
    def push(self, x): self._items.append(x)
    def pop(self): return self._items.pop()
    def __len__(self): return len(self._items)
```
> 🇨🇳 *[经典陷阱：继承 list 暴露了所有40个列表方法；组合则只暴露 push 和 pop]*

> **Composition lets you choose exactly what to expose** — and that control *is* the abstraction.
> 🇨🇳 **组合让你精确选择暴露什么**——而这种控制*就是*抽象。

> 🔑 **The rule, stated fairly:** inheritance for genuine *is-a* subtypes (and framework bases
> like `nn.Module`); composition for *has-a* and assembling behaviour. When unsure, compose —
> extracting an interface later is easy; untangling a deep inheritance tree is not.
> 🇨🇳 🔑 **规则公正地说：** 继承用于真正的 *is-a* 子类型（以及像 `nn.Module` 这样的框架基类）；
> 组合用于 *has-a* 和行为组装。不确定时用组合——之后提取接口容易；解开深的继承树很难。

> ✍️ **Self-explain (interleave D2):** an exception hierarchy `LogLevelError(LogError)` (Day 5)
> *is* inheritance — and it's correct. Why is that genuine is-a, while `Stack(list)` isn't?
> *(A `LogLevelError` truly **is a** kind of `LogError` — a subtype used wherever the base is
> expected. A `Stack` is **not a** kind of list; it only wants to *use* a list internally →
> has-a.)*
> 🇨🇳 ✍️ **自解释（穿插 D2）：** 一个异常层级 `LogLevelError(LogError)`（第5天）*是*继承——而且正确。
> 为什么它是真正的 is-a，而 `Stack(list)` 不是？
> *（`LogLevelError` 真正**是**一种 `LogError`——可在任何需要基类的地方使用它的子类型。
> `Stack` **不是**一种列表；它只想在内部*使用*一个列表 → has-a。）*

---

## S1b — `@dataclass`: boilerplate for free
> 🇨🇳 **[S1b — `@dataclass`：免费的样板代码]**

```python
from dataclasses import dataclass, field

@dataclass
class Transaction:
    kind: str
    amount: float
    balance_after: float
# free __init__, __repr__, __eq__ generated from the fields
```
> 🇨🇳 *[用 @dataclass 自动生成 __init__、__repr__、__eq__ 方法]*

> 🏭 **A label-maker for data classes.** Hand-writing `__init__`/`__repr__`/`__eq__` is
> hand-lettering the same label 500 times; `@dataclass` is the printer.
> 🇨🇳 🏭 **数据类的标签机。** 手写 `__init__`/`__repr__`/`__eq__` 就像手工书写同一标签500次；
> `@dataclass` 就是那台打印机。

| Need | How |
|------|-----|
| default | `count: int = 0` |
| **mutable** default | `items: list = field(default_factory=list)` — **never** `= []` |
| immutable + hashable | `@dataclass(frozen=True)` |
| ordering | `@dataclass(order=True)` |

| 需求 | 写法 |
|------|------|
| 默认值 | `count: int = 0` |
| **可变**默认值 | `items: list = field(default_factory=list)` —— **绝不要** `= []` |
| 不可变且可哈希 | `@dataclass(frozen=True)` |
| 可排序 | `@dataclass(order=True)` |

> ⚠️ Never `tags: list = []` — all instances would share one list (the S2 trap in disguise).
> 🇨🇳 ⚠️ 绝不要写 `tags: list = []` —— 所有实例会共享同一个列表（S2 陷阱的变种）。

---

## S2 — Type hints, the mutable-default trap, `__slots__`
> 🇨🇳 **[S2 — 类型提示、可变默认值陷阱、`__slots__`]**

**Type hints** document for humans + tools (`mypy`); they are **not** enforced at runtime.
```python
def total(amounts: list[float]) -> float: ...
def find(name: str) -> "Account | None": ...
```
> 🇨🇳 *[函数签名中添加类型提示，供人类阅读和 mypy 检查，运行时不做强制]*

> 🛂 **Signage, not guards.** Hints are airport signs ("Gate B12 →"); the guard is `mypy`, run
> separately. Hint your signatures (params + return) — that's 80% of the value.
> 🇨🇳 🛂 **路牌，不是门卫。** 类型提示就是机场指示牌（"B12登机口→"）；门卫是单独运行的 `mypy`。
> 给签名（参数+返回值）加提示——占用20%的功夫换来80%的价值。

**The #1 Python gotcha — mutable default arguments:**
```python
def add_item(item, bucket=[]):     # ❌ the list is created ONCE at def-time, reused forever
    bucket.append(item); return bucket
add_item("a"); add_item("b")       # → ['a','b']  😱

def add_item(item, bucket=None):   # ✅
    if bucket is None: bucket = []
    bucket.append(item); return bucket
```
> 🇨🇳 *[可变默认参数陷阱——错误的写法导致列表在函数定义时创建一次并被反复使用；正确的写法用 None 作默认并在内部创建新列表]*

> 🧥 **A closet with one shared hanger** installed at construction (`def`) time — every guest
> piles coats on the same hook. Default to `None`, create the real object inside. (This is edge
> **E4** — Pythonic hygiene.)
> 🇨🇳 🧥 **一个只装了一个公用衣架的衣橱**在构造（`def`）时安装——每位客人都把外套堆在同一个钩子上。
> 用 `None` 做默认值，在函数内部创建真正的对象。（这是边界案例 **E4** —— Python 整洁之道。）

**`__slots__`** trades flexibility for memory: replaces the per-instance `__dict__` (from Day 1's
"object is almost a dict") with a fixed layout. Only when a profiler says millions of instances
cost too much memory. 🎒 Foam camera case (snug, light, no room for a third lens) vs a duffel.
> 🇨🇳 **`__slots__`** 用灵活性换取内存：用固定布局替换每个实例的 `__dict__`（第1天说的"对象几乎是一个字典"）。
> 仅当性能分析器表明几百万个实例耗费太多内存时才用。🎒 泡沫相机包（紧凑、轻便、塞不下第三支镜头）vs 一个行李袋。

---

## S3 — Math: matrix×matrix, identity, inverse
> 🇨🇳 **[S3 — 数学：矩阵乘法、单位阵、逆矩阵]**

`A (m×n) · B (n×p) = C (m×p)`. **Inner dims must match**; each `Cᵢⱼ = Σₖ Aᵢₖ Bₖⱼ` (row·col).
> 🇨🇳 `A (m×n) · B (n×p) = C (m×p)`。**内侧维度必须匹配**；每个 `Cᵢⱼ = Σₖ Aᵢₖ Bₖⱼ`（行·列）。

```text
[1 2][5 6]   [19 22]
[3 4][7 8] = [43 50]
```
> 🇨🇳 *[示例：2×2矩阵相乘，计算过程]*

> 🁢 **Domino rule:** write shapes adjacent `(m×n)(n×p)` — inner numbers must touch & match;
> outer numbers survive. `(2×3)(3×4)→(2×4)` ✅; `(2×3)(2×3)` → inner `3≠2` ❌. Prevents 90% of
> shape errors.
> 🇨🇳 🁢 **多米诺规则：** 把形状并排写 `(m×n)(n×p)` —— 内侧数字必须相邻且相等；外侧数字留下。
> `(2×3)(3×4)→(2×4)` ✅；`(2×3)(2×3)` → 内侧 `3≠2` ❌。预防90%的形状错误。

> 🎬 **Order matters: `A·B ≠ B·A`.** A matrix is a transformation; `A·B` = "do B, then A."
> "socks then shoes" ≠ "shoes then socks."
> 🇨🇳 🎬 **顺序很重要：`A·B ≠ B·A`。** 矩阵是一种变换；`A·B` = "先做 B，再做 A"。
> "先穿袜子再穿鞋" ≠ "先穿鞋再穿袜子"。

**Identity `I`** (1s on diagonal): `A·I = A` — the do-nothing transform (clear glass).
**Inverse `A⁻¹`**: `A·A⁻¹ = I` — the *undo*. ↩️ Ctrl-Z. But not every matrix has one: a
projection that flattens 3-D→2-D destroys info (singular — can't un-flatten a pancake).
> 🇨🇳 **单位阵 `I`**（对角线上是1）：`A·I = A` —— 什么也不做的变换（透明玻璃）。
> **逆矩阵 `A⁻¹`**：`A·A⁻¹ = I` —— *撤销*。↩️ Ctrl-Z。但不是每个矩阵都有逆：
> 一个将3D压扁到2D的投影会丢失信息（奇异——无法把煎饼再还原成立方体）。

> 🚀 Stacking NN layers = chaining matrix products; attention (Week 10) uses `Q·Kᵀ`; "why is my
> matmul throwing a shape error?" is a *daily* DL reality — the domino rule is the fix.
> 🇨🇳 🚀 堆叠神经网络层 = 链式矩阵乘积；注意力机制（第10周）用到 `Q·Kᵀ`；"为什么我的 matmul 抛出形状错误？"
> 是*每天*都会遇到的深度学习现实——多米诺规则就是解决方案。

> 🔮 **By hand:** ① `[[1,2],[3,4]]·[[1,0],[0,1]]` (predict first). ② is `[[1,1]]·[[2],[3]]` valid?
> shape? ③ why can't you do `(2×3)·(2×3)`? *(① unchanged. ② valid, `(1×2)(2×1)→(1×1)=[5]`.
> ③ inner `3≠2`.)*
> 🇨🇳 🔮 **手算：** ① `[[1,2],[3,4]]·[[1,0],[0,1]]`（先预测）。 ② `[[1,1]]·[[2],[3]]` 合法吗？形状？
> ③ 为什么不能做 `(2×3)·(2×3)`？ *（① 不变。 ② 合法，`(1×2)(2×1)→(1×1)=[5]`。 ③ 内侧 `3≠2`。）*

---

## S4 — Frontier: vLLM & PagedAttention (your #1 direction)
> 🇨🇳 **[S4 — 前沿：vLLM 与 PagedAttention（你的首要方向）]**

Reading only (~2 h). **Problem:** generating text, an LLM keeps a **KV-cache** in scarce GPU
memory that *grows* with the conversation. Naïvely you pre-reserve one big contiguous block per
request sized for the worst case → most sits empty → memory (not compute) caps how many users
you serve.
> 🇨🇳 只需阅读（约2小时）。**问题：** 生成文本时，大语言模型在稀缺的GPU显存中维护一个随对话*增长*的
> **KV缓存**。天真做法是为每个请求预保留一个按最坏情况大小分配的连续大块 → 大部分空闲 → 内存（而非计算）
> 限制了你能服务的用户数。

> 🅿️ **Parking lot with SUV-sized stalls, all reserved up front.** Smart cars waste most of
> their space; the lot "fills" while half-empty.
> 🇨🇳 🅿️ **全被预定的 SUV 尺寸停车位。** 大部分车位浪费；停车场"满了"其实还一半空着。

**PagedAttention** breaks the KV-cache into small fixed-size **pages**, allocated on demand and
freed on finish — exactly like an **OS's virtual memory**. Fragmentation vanishes; far more
concurrent requests fit. 🅿️➡️ Repaint into small stalls, handed out as cars arrive, reclaimed
on exit → several times more cars. **That repainting is PagedAttention** (Kwon et al. 2023; 2–4×
throughput — [`../RESOURCES.md`](../RESOURCES.md) §D).
> 🇨🇳 **PagedAttention** 将 KV 缓存拆分成固定大小的小**页面**，按需分配，结束释放 —— 就像**操作系统的虚拟内存**。
> 碎片化消失；可以容纳远多于原来的并发请求。🅿️➡️ 重新画成小停车位，来车即发，离开即回收 → 可容纳数倍的车。
> **这个重新画线的动作就是 PagedAttention**（Kwon 等，2023；2–4倍吞吐量——[`../RESOURCES.md`](../RESOURCES.md) §D）。

> ✍️ Write 3 sentences: *what is a KV-cache? what does PagedAttention do to it? why does that
> raise the number of users you can serve?* If you can do it from the parking-lot analogy,
> today's frontier landed — and you can hold your own on it in an interview.
> 🇨🇳 ✍️ 写3句话：*什么是KV缓存？PagedAttention 对它做了什么？为什么这样能提高可服务的用户数？*
> 如果你能用停车场的类比说出来，今天的前沿就落地了——面试时你也能侃侃而谈。

---

## 🧠 Cheat-sheet
> 🇨🇳 **[速查表]**

```python
class Car:                                  # COMPOSITION ("has-a") — prefer
    def __init__(self): self.engine = Engine()
@dataclass
class Rec:
    tags: list = field(default_factory=list)   # mutable default DONE RIGHT
def f(bucket=None):                          # mutable default ARG done right
    if bucket is None: bucket = []
# A·B: inner dims match, order matters;  A·I = A;  A·A⁻¹ = I (may not exist)
```
> 🇨🇳 *[速查表：组合示例、@dataclass 的可变默认字段、可变默认参数的安全写法，以及矩阵运算规则]*

| Term | One-liner | Analogy |
|------|-----------|---------|
| composition | "has-a"; hold a part (prefer) | Lego |
| fragile base class | base change breaks children | renovating a tower's ground floor |
| `@dataclass` | auto `__init__`/`__repr__`/`__eq__` | label-maker |
| type hints | docs for humans+`mypy`; not enforced | signage, not guards |
| mutable-default trap | one shared object across calls | shared hanger |
| `__slots__` | drop `__dict__` for memory (profiled) | foam case vs duffel |
| matrix mult | inner dims match; order matters | socks then shoes |
| inverse | the undo (may not exist) | Ctrl-Z / can't un-flatten a pancake |
| PagedAttention | paged KV-cache → more users | repainted parking lot |

| 术语 | 一句话 | 类比 |
|------|--------|------|
| 组合 | "has-a"；持有一个部件（优先） | 乐高 |
| 脆弱的基类 | 基类改动破坏子类 | 改造塔楼的底层 |
| `@dataclass` | 自动生成 `__init__`/`__repr__`/`__eq__` | 标签机 |
| 类型提示 | 给人+ `mypy` 的文档；不强制 | 路牌，不是门卫 |
| 可变默认值陷阱 | 多次调用共享同一对象 | 公用衣架 |
| `__slots__` | 去掉 `__dict__` 省内存（分析后使用） | 泡沫包 vs 行李袋 |
| 矩阵乘法 | 内维度匹配；顺序重要 | 先袜子后鞋 |
| 逆矩阵 | 撤销操作（可能不存在） | Ctrl-Z / 无法把煎饼还原成立方体 |
| PagedAttention | 分页 KV 缓存 → 服务更多用户 | 重新画线的停车场 |

## ⚠️ Common pitfalls
> 🇨🇳 **[常见陷阱]**

1. **Inheriting to reuse code that's really has-a** (`Stack(list)`) → leaks the whole interface. Compose.
2. **`def f(x=[])` / `tags: list = []`** → shared-mutable-default. `None`+create, or `field(default_factory=list)`.
3. **Believing hints enforce types** → run `mypy`.
4. **`__slots__` by default** → costs flexibility; profiler-driven only.
5. **Assuming `A·B == B·A`** → matrix mult isn't commutative.
6. **Expecting every matrix to invert** → singular ones (projections) don't.
> 🇨🇳 1. **为了复用代码而继承实际是 has-a 的关系**（`Stack(list)`）→ 泄露整个接口。用组合。
> 2. **`def f(x=[])` / `tags: list = []`** → 共享可变默认值。改用 `None`+创建，或 `field(default_factory=list)`。
> 3. **认为类型提示会强制类型** → 运行 `mypy`。
> 4. **默认使用 `__slots__`** → 牺牲灵活性；只应由性能分析驱动。
> 5. **假设 `A·B == B·A`** → 矩阵乘法不可交换。
> 6. **期望每个矩阵都可逆** → 奇异矩阵（如投影）不可逆。

## ✅ Storage-strength check (cold, tomorrow)
> 🇨🇳 **[存储强度检查（明早冷启动）]**

State the is-a/has-a rule + one consequence of getting it wrong; write a `@dataclass` with a safe
mutable default; predict `A·I`; explain PagedAttention in 2 sentences. Shaky → log it.
> 🇨🇳 说出 is-a/has-a 规则 + 弄错的一个后果；写一个带有安全可变默认值的 `@dataclass`；预测 `A·I`；
> 用两句话解释 PagedAttention。不牢靠就记录下来。

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — refactor Day-1's mega-class into composed
`Bank` + `Account` + `Ledger`. Narrate: *"Account HAS-A Ledger; Bank HAS-MANY Accounts;
Transaction is data → `@dataclass`."*
> 🇨🇳 ➡️ **动手构建：** [`HOMEWORK.md`](./HOMEWORK.md) —— 将第1天的巨类重构为组合式的 `Bank` +
> `Account` + `Ledger`。口述：*"Account HAS-A Ledger；Bank HAS-MANY Accounts；
> Transaction 是数据 → `@dataclass`。"*
