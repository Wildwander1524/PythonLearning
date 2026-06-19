# 📘 Day 3 — Dunder Methods & the Python Data Model
> 🇨🇳 **[第 3 天 — 双下划线方法与 Python 数据模型]**

> **Week 1 · Wed 2026-06-18** · Curriculum: Python OOP · Math: matrices, transpose, matrix×vector
> Active reading: hit every `✍️`/`🔮`. Today's mantra: **make your objects feel native** —
> printable, comparable, addable, indexable, iterable, *just like a built-in*.
> Canonical reference: **Ramalho, *Fluent Python* Ch. 1** (the `FrenchDeck` example is the
> template for today's homework) — [`../RESOURCES.md`](../RESOURCES.md) §A.
> 🇨🇳 **第 1 周 · 周三 2026-06-18** · 课程：Python 面向对象 · 数学：矩阵、转置、矩阵乘向量
> 主动阅读：遇到 `✍️`/`🔮` 就动手。今天的信条：**让你的对象感觉像原生** —
> 可打印、可比较、可相加、可索引、可迭代，*就像内置类型一样*。
> 规范参考：**Ramalho, *Fluent Python* 第 1 章**（`FrenchDeck` 示例是今天作业的模板） — [`../RESOURCES.md`](../RESOURCES.md) §A。

## 🎯 Objectives & mastery bar
> 🇨🇳 **[目标与掌握标准]**

| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Explain *why* syntax → dunder call | Understand | you can say what `a+b`, `len(x)`, `for i in x` each dispatch to |
| Implement `__repr__`/`__eq__`/`__add__`/`__iter__` | Apply | your class behaves like a built-in number/list |
| Pair `__eq__` with `__hash__` correctly | Analyze | you know when your object is (un)hashable and why |

| 目标 | Bloom 分类 | 掌握标准 |
|------|------------|----------|
| 解释 *为什么* 语法 → 双下划线调用 | 理解 | 能说出 `a+b`、`len(x)`、`for i in x` 各自分发到哪个方法 |
| 实现 `__repr__`/`__eq__`/`__add__`/`__iter__` | 应用 | 你的类表现得像内置数字或列表 |
| 正确配对 `__eq__` 与 `__hash__` | 分析 | 知道你的对象什么时候（不）可哈希，以及为什么 |

## 🔁 Spaced callbacks (cold, first — re-tests D1 + D2)
> 🇨🇳 **[间隔回顾（冷启动，第一次 — 重测 D1 和 D2）]**

C1 (D1) why return a *copy* from `history()`? C2 (D2) **predict** `D.__mro__` for `class D(B,C)`,
`B(A)`, `C(A)`. C3 (D2) extend vs replace — which keeps the parent's guarantees?
*(Blank on C2? That's edge E3 — slow down and re-derive it.)*
> 🇨🇳 C1（D1）为什么 `history()` 返回一个*副本*？ C2（D2）**预测** `class D(B,C), B(A), C(A)` 的 `D.__mro__`。 C3（D2）扩展 vs 替换 —— 哪种保留了父类的保证？
（如果 C2 一片空白？那就是边界情况 E3 —— 放慢速度重新推导。）

---

## The big idea: built-in syntax is sugar over special methods
> 🇨🇳 **[核心思想：内置语法是特殊方法之上的语法糖]**

When you write `len(x)`, Python calls `x.__len__()`. `a + b` → `a.__add__(b)`. `print(x)` →
`x.__str__()`. **The language's syntax is method calls with special ("dunder") names.** Define
those hooks on *your* class and the same familiar syntax works on your objects.
> 🇨🇳 当你写 `len(x)` 时，Python 调用 `x.__len__()`。`a + b` → `a.__add__(b)`。`print(x)` → `x.__str__()`。**语言的语法就是调用带有特殊（"双下划线"）名字的方法。** 在你的类上定义这些钩子，同样的熟悉语法就能在你的对象上工作。

> 🎹 **Piano keys & hammers.** The keys (`+ == len() [] for`) are the interface you press;
> behind each is a hammer (`__add__ __eq__ __len__ __getitem__ __iter__`) that strikes the
> string. Built-ins ship with hammers installed. Writing dunder methods = installing your own.
> 🇨🇳 🎹 **钢琴键与击弦槌。** 键（`+ == len() [] for`）是你按下的接口；每个键后面都是一个击弦槌（`__add__ __eq__ __len__ __getitem__ __iter__`）敲击琴弦。内置类型出厂就装好了击弦槌。编写双下划线方法 = 安装你自己的击弦槌。

> 🌍 **Why it's profound (Ramalho's thesis):** Python doesn't have 50 special cases — it has
> *one protocol* everything opts into. Learn `len()` once; it works on str, list, dict, *and*
> your classes. **NumPy arrays, pandas DataFrames, and PyTorch tensors are built on exactly this
> mechanism** — `tensor_a + tensor_b` is `__add__`. Today you learn the hook those libraries use.
> 🇨🇳 🌍 **为什么这很深刻（Ramalho 的论点）：** Python 没有 50 种特殊情况 —— 它有*一个协议*，所有东西都加入。学会 `len()` 一次；它对 str、list、dict *以及*你自己的类都有效。**NumPy 数组、pandas DataFrame 和 PyTorch 张量正是建立在这个机制上** —— `tensor_a + tensor_b` 就是 `__add__`。今天你将学到那些库所使用的钩子。

---

## S1 — Representation, equality, sizing, indexing
> 🇨🇳 **[S1 — 表示、相等、大小、索引]**

### `__repr__` vs `__str__` — two audiences
> 🇨🇳 **[`__repr__` 与 `__str__` — 两类受众]**

| Method | Triggered by | Audience | Goal |
|--------|--------------|----------|------|
| `__repr__` | REPL, debugger, **inside containers**, `repr()` | the developer | unambiguous; ideally recreates the object |
| `__str__` | `print()`, `str()`, f-strings | the end user | readable, friendly |

| 方法 | 触发场景 | 受众 | 目标 |
|------|----------|------|------|
| `__repr__` | REPL、调试器、**容器内部**、`repr()` | 开发者 | 无歧义；理想情况下可重新创建对象 |
| `__str__` | `print()`、`str()`、f-string | 最终用户 | 可读、友好 |

> 🪪 **ID card vs party nametag.** `__repr__` = precise government ID for officials (debuggers);
> `__str__` = the warm "Hi, my name is ___" sticker. **Always define `__repr__`** (it's your
> debugging lifeline — without it, a list of your objects prints `<...object at 0x7f…>`).
> `__str__` falls back to `__repr__`, never the reverse — so `__repr__` alone covers both.
> 🇨🇳 🪪 **身份证 vs 派对胸牌。** `__repr__` = 给官员（调试器）看的精确政府身份证；`__str__` = 温暖的"嗨，我叫 ___"贴纸。**始终定义 `__repr__`**（它是你的调试生命线 —— 没有它，一个包含你对象的列表会打印出 `<...object at 0x7f…>`）。`__str__` 回退到 `__repr__`，反之则不会 —— 所以只定义 `__repr__` 就能同时满足两者。

> 💡 Aim for a **round-trip** repr: `eval(repr(obj))` recreates it. `Point(x=1, y=2)` is valid
> code that rebuilds the point.
> 🇨🇳 💡 争取一个**可往返**的 repr：`eval(repr(obj))` 能重新创建它。`Point(x=1, y=2)` 是能重建该点的合法代码。

### `__eq__` and the `__hash__` trap
> 🇨🇳 **[`__eq__` 与 `__hash__` 陷阱]**

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other):
        if not isinstance(other, Money): return NotImplemented   # not False — let Python try other side
        return self.cents == other.cents
```
> 🇨🇳 *[定义 Money 类，实现基于美分的相等比较，对非 Money 类型返回 NotImplemented 以允许反向比较尝试]*

> ⚠️ **The moment you define `__eq__`, Python sets `__hash__ = None`** → your object can't go in
> a `set`/`dict`. Contract: *equal objects must hash equal*; Python can't verify your new logic,
> so it disables hashing to keep you safe. If the object is **immutable** and you want it
> hashable, define `__hash__` too (`return hash(self.cents)`); if **mutable**, leave it
> unhashable (correct — a mutable key's hash would drift).
> 🏷️ *Coat-check ticket:* if two "equal" coats got different tickets, you'd never find your coat.
> 🇨🇳 ⚠️ **定义 `__eq__` 的那一刻，Python 会将 `__hash__` 设为 `None`** → 你的对象不能放入 `set`/`dict`。契约：*相等的对象必须哈希相等*；Python 无法验证你的新逻辑，所以禁用哈希以保证安全。如果对象是**不可变**的，且你希望它可哈希，同时定义 `__hash__`（`return hash(self.cents)`）；如果是**可变**的，就让它不可哈希（正确做法 —— 可变键的哈希值会"漂移"）。
> 🏷️ *衣帽间存根票：* 如果两件"相等"的外套拿到不同的存票，你就永远找不到你的外套。

> ✍️ **Self-explain (interleave with D2):** exceptions are objects in an inheritance tree
> (you'll see Day 5). What does returning `NotImplemented` (not `False`) from `__eq__` let Python
> do? *(Try the **reflected** comparison `other.__eq__(self)` — cooperation, like `super()` along
> the MRO. `False` would wrongly declare "not equal" without asking the other operand.)*
> 🇨🇳 ✍️ **自我解释（与 D2 穿插）：** 异常是继承树中的对象（你会在第 5 天看到）。从 `__eq__` 返回 `NotImplemented`（而非 `False`）能让 Python 做什么？*（尝试**反射**比较 `other.__eq__(self)` —— 合作，就像 `super()` 沿着 MRO 一样。`False` 会错误地声明"不相等"，而不去询问另一个操作数。）*

### `__len__` / `__getitem__`
> 🇨🇳 **[`__len__` / `__getitem__`]**

```python
class Playlist:
    def __init__(self, songs): self.songs = songs
    def __len__(self): return len(self.songs)            # len(pl)
    def __getitem__(self, i): return self.songs[i]       # pl[0], pl[-1], and... iteration!
```
> 🇨🇳 *[定义 Playlist 类，支持 len() 获取歌曲数量，通过索引获取歌曲，并且自动支持迭代]*

> 🎟️ **Hidden superpower:** with `__getitem__` but no `__iter__`, `for x in pl:` *still works* —
> Python falls back to `pl[0], pl[1], …` until `IndexError`. One good `__getitem__` gives
> indexing *and* looping. (This is the old iteration protocol Ramalho's `FrenchDeck` relies on.)
> 🇨🇳 🎟️ **隐藏的超能力：** 有了 `__getitem__` 而没有 `__iter__`，`for x in pl:` *依然能运行* —— Python 回退到依次尝试 `pl[0], pl[1], …` 直到 `IndexError`。一个设计良好的 `__getitem__` 同时提供索引*和*循环。（这就是 Ramalho 的 `FrenchDeck` 所依赖的旧式迭代协议。）

---

## S2 — Operator overloading & iterators
> 🇨🇳 **[S2 — 运算符重载与迭代器]**

| You write | Python calls | Returns |
|-----------|--------------|---------|
| `a + b` | `a.__add__(b)` | a **new** object |
| `a * k` | `a.__mul__(k)` | new object |
| `a == b` | `a.__eq__(b)` | bool |
| `abs(a)` | `a.__abs__()` | a number |

| 你写 | Python 调用 | 返回 |
|------|-------------|------|
| `a + b` | `a.__add__(b)` | 一个**新**对象 |
| `a * k` | `a.__mul__(k)` | 新对象 |
| `a == b` | `a.__eq__(b)` | 布尔值 |
| `abs(a)` | `a.__abs__()` | 一个数字 |

> 🧾 **Golden rule: return a new object, never mutate.** `c = a + b` must leave `a`, `b`
> unchanged (`5 + 3` doesn't alter `5`). 🍪 Combining two recipes invents a third; it doesn't
> erase the originals.
> 🇨🇳 🧾 **黄金法则：返回新对象，绝不改变原对象。** `c = a + b` 必须让 `a`、`b` 保持不变（`5 + 3` 不会改变 `5`）。🍪 结合两份食谱创造出第三份，而不是抹去原食谱。

> 🪞 **Reflected operators.** `2 * v` (int on the left): Python tries `int.__mul__(2, v)` → the
> int shrugs (`NotImplemented`) → Python tries `v.__rmul__(2)`. Define `__rmul__` and `2 * v`
> works. Same "ask left; if it shrugs, ask right" cooperation as `__eq__`. *(Today's stretch.)*
> 🇨🇳 🪞 **反射运算符。** `2 * v`（int 在左边）：Python 尝试 `int.__mul__(2, v)` → int 没辙，返回 `NotImplemented` → Python 再尝试 `v.__rmul__(2)`。定义 `__rmul__`，`2 * v` 就能工作。和 `__eq__` 相同的"问左边；如果左边没辙就问右边"的合作模式。*（今天的延伸内容。）*

### Iterators — the protocol behind every `for`
> 🇨🇳 **[迭代器 — 每个 `for` 循环背后的协议]**

| Role | Method | Job |
|------|--------|-----|
| **iterable** | `__iter__` | "I can produce an iterator" (a book that *can* be read) |
| **iterator** | `__next__` | "next item, or raise `StopIteration`" (a bookmark) |

| 角色 | 方法 | 职责 |
|------|------|------|
| **可迭代对象** | `__iter__` | "我能生成一个迭代器"（一本*可以*阅读的书） |
| **迭代器** | `__next__` | "下一项，或引发 `StopIteration`"（一个书签） |

> 🍬 **Pez dispenser.** The box (iterable) hands you a loaded dispenser (iterator); each click
> (`__next__`) pops the next candy; empty → `StopIteration`. Two dispensers from one box click
> independently — which is why the roles are separate.
> 🇨🇳 🍬 **Pez 糖果盒。** 盒子（可迭代对象）递给你一个装满的分配器（迭代器）；每按一下（`__next__`）弹出下一颗糖；空了 → `StopIteration`。同一个盒子拿出的两个分配器各自独立出糖 —— 这就是为什么角色要分开。

> 💡 **The shortcut you'll actually use — generators.** Any method with `yield` *is* an iterator;
> Python writes `__next__`/`StopIteration` for you:
> ```python
> def __iter__(self):
>     yield self.x      # first next() → x
>     yield self.y      # second → y; function ends → StopIteration automatically
> ```
> Now `for c in v`, `list(v)`, and `x, y = v` (unpacking) all work. 📼 A cassette that remembers
> the playhead. **You'll use exactly this in today's `Vector2D`.**
> 🇨🇳 💡 **你实际会用的快捷方式 —— 生成器。** 任何带 `yield` 的方法*就是*一个迭代器；Python 为你写好 `__next__`/`StopIteration`：
> ```python
> def __iter__(self):
>     yield self.x      # 第一次 next() → x
>     yield self.y      # 第二次 → y；函数结束 → 自动 StopIteration
> ```
> 现在 `for c in v`、`list(v)` 以及 `x, y = v`（解包）都能工作。📼 一盘能记住播放头的磁带。**你会在今天的 `Vector2D` 中恰好用到这个。**

> 🦥 **Why laziness matters:** an iterator yields one item at a time, so you can loop a 100 GB
> file on 8 GB RAM. PyTorch `DataLoader`s are iterators streaming batches — you'll lean on this
> from Week 8.
> 🇨🇳 🦥 **为什么惰性很重要：** 迭代器一次产出一项，所以你可以在 8 GB 内存上循环处理 100 GB 文件。PyTorch 的 `DataLoader` 就是流式产出批次的迭代器 —— 从第 8 周起你会依赖这一点。

---

## S3 — Math: matrices, transpose, matrix×vector
> 🇨🇳 **[S3 — 数学：矩阵、转置、矩阵乘向量]**

A **matrix** = an `m×n` grid of numbers — *and* a function that transforms vectors (rotate,
scale, project). Hold both. `A[1][2]` = row 1, col 2 (rows first, always).
> 🇨🇳 **矩阵** = 一个 `m×n` 的数字网格 —— *同时也*是将向量进行变换（旋转、缩放、投影）的函数。两者都要把握。`A[1][2]` = 第 1 行第 2 列（始终先行后列）。

**Transpose** flips rows↔columns: a `2×3` becomes `3×2`, `(Aᵀ)ᵢⱼ = Aⱼᵢ`.
> 🇨🇳 **转置** 翻转行和列：一个 `2×3` 变成 `3×2`，`(Aᵀ)ᵢⱼ = Aⱼᵢ`。

**Matrix × vector** — each output entry is a **dot product** (yesterday's tool!) of a matrix row
with the vector:
> 🇨🇳 **矩阵乘向量** —— 输出向量的每一元都是矩阵的某一行与向量的**点积**（昨天的工具！）：

```text
[1 2] [5]   [1·5+2·6]   [17]
[3 4] [6] = [3·5+4·6] = [39]
```
> 🇨🇳 *[演示 2x2 矩阵乘以列向量，得到结果向量的代数推导]*

- **Row picture:** each output = (row)·(vector).
- **Column picture:** output = a *linear combination of the columns*: `5·[1,3]+6·[2,4]=[17,39]`
  (this is Day 5's span/linear-combinations, foreshadowed).
> 🇨🇳 - **行视角：** 每个输出分量 = （行）·（向量）。
> - **列视角：** 输出 = *列的线性组合*：`5·[1,3]+6·[2,4]=[17,39]`（这是第 5 天的张成空间/线性组合的铺垫）。

> 🚀 **The most important operation in your roadmap.** A neural-net layer is `output = W·x + b`
> — a matrix times a vector. "Deep" = many of these stacked. Every forward pass (Week 8+) and
> every attention block (Week 10) is built from matrix×vector. 3B1B Ch.3 makes the
> "matrix = transformation" picture click ([3b1b](https://www.3blue1brown.com/topics/linear-algebra)).
> 🇨🇳 🚀 **你学习路线图中最重要的运算。** 神经网络的每一层是 `output = W·x + b` —— 一个矩阵乘以向量。"深度"就是许多层堆叠。每一次前向传播（第 8 周起）和每一个注意力模块（第 10 周）都建立在矩阵乘向量之上。3Blue1Brown 第 3 章帮你打通"矩阵 = 变换"的图像（[3b1b](https://www.3blue1brown.com/topics/linear-algebra)）。

> 🔮 **By hand:** ① transpose `[[1,2,3]]` (shape?). ② `[[2,0],[0,2]]·[3,5]` = ? what did that
> matrix *do* to the vector? ③ `[[1,0],[0,1]]·[7,9]` = ? why "identity"? *(① `[[1],[2],[3]]`,
> 3×1. ② `[6,10]` — doubled it (scaling). ③ `[7,9]` unchanged — identity does nothing.)*
> 🇨🇳 🔮 **动手算：** ① 转置 `[[1,2,3]]`（形状是？）。② `[[2,0],[0,2]]·[3,5]` = ? 这个矩阵对向量*做了什么*？③ `[[1,0],[0,1]]·[7,9]` = ? 为什么叫"单位矩阵"？*（① `[[1],[2],[3]]`，3×1。② `[6,10]` — 将向量放大了一倍（缩放）。③ `[7,9]` 不变 —— 单位矩阵什么都不做。）*

---

## S4 — Frontier: verify PyTorch (it's already installed)
> 🇨🇳 **[S4 — 前沿：验证 PyTorch（已安装）]**

Per [`../RESOURCES.md`](../RESOURCES.md) §E your `dl` env already has torch 2.12 + CUDA. So
today is *verification*, not install:
> 🇨🇳 根据 [`../RESOURCES.md`](../RESOURCES.md) §E，你的 `dl` 环境已经安装了 torch 2.12 + CUDA。所以今天是*验证*，而非安装：

```bash
conda activate dl
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# expect:  2.12.0+cu126 True
```
> 🇨🇳 *[激活 conda 环境并检查 PyTorch 版本及 CUDA 是否可用]*

Then see today's lesson made concrete:
> 🇨🇳 然后看看今天所学如何具体化：

```python
import torch
x = torch.tensor([[1., 2.], [3., 4.]])
print(x.T)                              # transpose — the S3 op, one attribute away
print(x @ torch.tensor([5., 6.]))       # matrix×vector → tensor([17., 39.])
```
> 🇨🇳 *[创建 PyTorch 张量，展示转置属性和矩阵乘向量操作]*

`x.T` is your by-hand transpose; `@` is `__matmul__`. **A tensor implements the exact dunders
you're studying** (`__add__`, `__getitem__`, `__repr__`, `__matmul__`). PyTorch = today's data
model + today's linear algebra, welded together.
> 🇨🇳 `x.T` 就是你手算的转置；`@` 就是 `__matmul__`。**张量正好实现了你正在学习的那些双下划线方法**（`__add__`、`__getitem__`、`__repr__`、`__matmul__`）。PyTorch = 今天的数据模型 + 今天的线性代数，焊接在一起。

---

## 🧠 Cheat-sheet
> 🇨🇳 **[速查表]**

```python
__repr__    # ALWAYS define (REPL, debugger, containers)
__str__     # only when user form differs; falls back to __repr__
__eq__      # defining it ⇒ object unhashable until you add __hash__ (immutable only)
__len__ / __getitem__   # len(x) / x[i]  (getitem alone also enables for-loops)
__add__ / __mul__       # return a NEW object; never mutate self
__rmul__    # 2 * x  (reflected: left operand shrugged)
__iter__    # easiest as a generator with `yield`
```
> 🇨🇳 *[双下划线方法速查：注释说明各方法的用途和注意事项]*

| Term | One-liner | Analogy |
|------|-----------|---------|
| data model | syntax → dunder calls | piano keys → hammers |
| `__repr__`/`__str__` | dev / user text | ID card / nametag |
| `__eq__`+`__hash__` | define together for immutables | equal coats need equal tickets |
| reflected op | right operand handles it | "left shrugged, ask the right" |
| iterable / iterator | "can give a reader" / "is the bookmark" | candy box / loaded Pez |
| generator | `yield`-function that *is* an iterator | cassette remembering the playhead |
| matrix×vector | stack of row·vector dots | the atom of a NN layer |

| 术语 | 一句话解释 | 类比 |
|------|------------|------|
| 数据模型 | 语法 → 双下划线调用 | 钢琴键 → 击弦槌 |
| `__repr__`/`__str__` | 开发者 / 用户文本 | 身份证 / 姓名贴 |
| `__eq__`+`__hash__` | 不可变对象要一起定义 | 相等的外套需要相等的存票 |
| 反射运算符 | 右操作数来处理 | "左边耸肩，问右边" |
| 可迭代对象 / 迭代器 | "能提供阅读器" / "就是书签" | 糖果盒 / 装好的 Pez 分配器 |
| 生成器 | 带 `yield` 的函数，*本身*就是迭代器 | 记住播放头的磁带 |
| 矩阵乘向量 | 一行行点积的堆叠 | 神经网络层的基本单元 |

## ⚠️ Common pitfalls
> 🇨🇳 **[常见陷阱]**

1. **No `__repr__`** → `<…object at 0x…>` in lists/debuggers. Define it first.
2. **Mutating `self` in `__add__`** → `a+b` must not change `a`. Return new.
3. **`__eq__` without `__hash__`** → `TypeError: unhashable` in a set. Add `__hash__` (immutable) or accept it (mutable).
4. **Hand-writing `__next__`** when a generator (`yield`) is shorter and safer.
5. **Returning `False` (not `NotImplemented`) from `__eq__`** for unknown types → blocks the reflected comparison.
> 🇨🇳 1. **没有 `__repr__`** → 列表和调试器中显示 `<…object at 0x…>`。优先定义它。
> 2. **在 `__add__` 中修改 `self`** → `a+b` 绝不能改变 `a`。返回新对象。
> 3. **有 `__eq__` 却无 `__hash__`** → 放入集合时报 `TypeError: unhashable`。若不可变则添加 `__hash__`，若可变就接受不可哈希。
> 4. **手写 `__next__`** 而用生成器 (`yield`) 更短、更安全。
> 5. **对未知类型从 `__eq__` 返回 `False`（而非 `NotImplemented`）** → 阻断了反射比较。

## ✅ Storage-strength check (cold, tomorrow)
> 🇨🇳 **[存储强度检查（冷启动，明天）]**

From a blank file: a class that `repr`s round-trip, `==`-compares, `+`-adds (new object), and
`for`-iterates via `yield`. Say which dunder each of `==`, `+`, `for` fires. Shaky → log it.
> 🇨🇳 从空白文件开始：写一个类，能往返 `repr`、`==` 比较、`+` 加法（新对象），以及通过 `yield` 实现 `for` 迭代。说出 `==`、`+`、`for` 各自触发哪个双下划线方法。生疏 → 记下来。

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — `Vector2D`, where `abs(v)` *is* the D2 norm and
`v.dot(w)` *is* the D2 dot product. You're now coding the linear algebra you did on paper.
> 🇨🇳 ➡️ **动手构建：** [`HOMEWORK.md`](./HOMEWORK.md) — `Vector2D`，其中 `abs(v)` *就是* D2 范数，而 `v.dot(w)` *就是* D2 点积。你现在正在将纸上做的线性代数写成代码。
