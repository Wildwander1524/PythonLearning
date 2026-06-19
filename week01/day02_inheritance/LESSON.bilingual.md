# 📘 Day 2 — Inheritance, Polymorphism, ABCs & the MRO / Day 2 — 继承、多态、抽象基类与方法解析顺序

> **Week 1 · Tue 2026-06-17** · Curriculum: Python OOP · Math: dot product, norm, distance
> 🇨🇳 **第一周 · 周二 2026-06-17** · 课程：Python OOP · 数学：点积、范数、距离

> Active reading: stop at every `✍️ Self-explain` / `🔮 Predict`. Today carries growth-edge **E3** (you wrote `super(Bird, self)` and skipped a class in the MRO) — the MRO drill below exists to close it for good.
> 🇨🇳 主动阅读：在每个 `✍️ Self-explain` / `🔮 Predict` 处停下。今天承载成长边缘 **E3**（你写了 `super(Bird, self)` 并跳过了 MRO 中的一个类）——下面的 MRO 练习就是为了彻底解决它。

## 🎯 Objectives & mastery bar / 目标与掌握标准
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Use `super()` + method overriding (extend vs replace) | Apply | you pick the right flavour without thinking |
| **Predict an MRO** of a 3-level / multiple-inheritance class | **Analyze** | you read `__mro__` cold and explain each entry |
| Design an ABC contract | Create | your ABC rejects an incomplete subclass *at instantiation* |
| Polymorphism without `isinstance` ladders | Apply | your `total_area`-style code has zero type checks |
| Math: dot product (algebraic + geometric), norm, distance | Understand | you compute by hand and read the sign of `a·b` |

| 目标 | 布鲁姆分类 | 掌握时机… |
|------|---------|---------|
| 使用 `super()` + 方法覆盖（扩展 vs 替换） | Apply（应用） | 你不假思索地选择正确的风格 |
| **预测一个三层次 / 多重继承类的 MRO（方法解析顺序）** | **Analyze（分析）** | 你能冷静地阅读 `__mro__` 并解释每个条目 |
| 设计一个 ABC（抽象基类）契约 | Create（创造） | 你的 ABC 在实例化时拒绝不完整的子类 |
| 不使用 `isinstance` 条件链的多态 | Apply（应用） | 你的 `total_area` 风格代码没有类型检查 |
| 数学：点积（代数 + 几何）、范数、距离 | Understand（理解） | 你手动计算并能读取 `a·b` 的符号 |

## 🔁 Spaced callback (do FIRST, from memory — re-tests Day 1) / 间隔回呼（先做，凭记忆 —— 重新测试 Day 1）

Before new material, answer cold: ① instance vs class attribute rule? ② what makes a property read-only? ③ `[2,3] + 2·[1,-1]` = ? *(Blank? Note it — that's the spacing effect working.)*
> 🇨🇳 在学习新内容之前，先冷静回答：① 实例属性与类属性的规则？② 什么使属性只读？③ `[2,3] + 2·[1,-1]` = ？*（一片空白？记下来 —— 这正是间隔效应在起作用。）*

## The big picture: share what's common, specialize what differs / 全局视角：共享共性，特化差异

Yesterday's `BankAccount` was one self-contained class. Soon you need `SavingsAccount` (adds interest), `CheckingAccount` (allows overdraft). Copy-pasting `BankAccount` three times means a `withdraw` bug must be fixed four places. **Inheritance** solves this: one source of truth, many specializations.
> 🇨🇳 昨天的 `BankAccount` 是一个独立的类。很快你就需要 `SavingsAccount`（添加利息）、`CheckingAccount`（允许透支）。把 `BankAccount` 复制粘贴三次，意味着一个 `withdraw` 的 bug 要在四个地方修复。**继承（Inheritance）** 解决了这个问题：一个真相来源，多种特化。

> 🏛️ **Analogy — the master blueprint.** An architect draws one master plan, then per client adds a sun-room or a third bedroom rather than redrawing everything. Master = **base class**; each customization = **subclass**. Fix the master's plumbing and every house inherits the fix.
> 🇨🇳 🏛️ **类比 —— 主蓝图。** 建筑师绘制一份主方案，然后为每个客户增加一个阳光房或第三间卧室，而不是重新绘制全部。主方案 = **基类（base class）**；每个定制 = **子类（subclass）**。修复主设计的管道，每一栋房子都继承了这个修复。

| Relationship | Test | Tool | Example |
|--------------|------|------|---------|
| **Inheritance** | "A *is a* B" | subclassing (today) | `Dog` **is an** `Animal` |
| **Composition** | "A *has a* B" | hold an attribute (Day 4) | `Car` **has an** `Engine` |

| 关系 | 检验 | 工具 | 示例 |
|------|------|------|------|
| **继承（Inheritance）** | “A *是* B” | 子类化（今天） | `Dog` **是** `Animal` |
| **组合（Composition）** | “A *拥有* B” | 持有属性（第4天） | `Car` **拥有** `Engine` |

## S1 — Inheritance & `super()` / 继承与 `super()`

```python
class Animal:
    def __init__(self, name, sound):
        self.name, self.sound = name, sound
    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")     # delegate setup to the parent (foundation crew)
    def fetch(self, item):                 # a NEW ability Animal lacks
        return f"{self.name} fetches the {item}!"
```
> 🇨🇳 示例代码：`Animal` 基类与 `Dog` 子类，`Dog` 使用 `super()` 委托父类初始化并添加新方法 `fetch`。

`Dog("Rex").speak()` works though `Dog` never defines `speak` — Python looks *up* the chain to `Animal`. `fetch` lives only on `Dog`.
> 🇨🇳 即使 `Dog` 从未定义 `speak`，`Dog("Rex").speak()` 也能运行 —— Python 会沿继承链向上查找 `Animal`。`fetch` 只存在于 `Dog` 上。

> 🏗️ **`super().__init__()` is not optional.** The parent's `__init__` is the *only* code that sets up the parent's attributes. Skip it and the object is half-built — `self.sound` simply doesn't exist, and `speak()` later raises `AttributeError`.
> 🇨🇳 🏗️ **`super().__init__()` 不是可选的。** 父类的 `__init__` 是设置父类属性的唯一代码。跳过它，对象就是半构建的 —— `self.sound` 根本不存在，稍后 `speak()` 会抛出 `AttributeError`。

> ✍️ **Self-explain (edge E1, from your Day-2 submission):** your `Dog.fetch` returned a string that *ignored* its `item` argument, so the test "ball in output" failed. What must `fetch("ball")` contain? *(`"...fetches the ball!"` — use the parameter the spec names. Coding what the spec *says*, not what's close, is edge E1.)*
> 🇨🇳 ✍️ **自己解释（边缘 E1，来自你 Day-2 的提交）：** 你的 `Dog.fetch` 返回了一个字符串，忽略了它的 `item` 参数，所以测试 “ball in output” 失败了。`fetch("ball")` 应该包含什么？*（`"...fetches the ball!"` —— 使用规范命名的参数。编写规范要求的内容，而不是近似内容，这就是边缘 E1。）*

### Override: replace vs extend / 覆盖：替换 vs 扩展
```python
class Cat(Animal):
    def __init__(self, name): super().__init__(name, "Meow")
    def speak(self):                          # OVERRIDE
        return f"{super().speak()}... then ignores you"   # EXTEND: reuse parent + add
```
> 🇨🇳 示例代码：`Cat` 覆盖 `speak` 方法，调用 `super().speak()` 进行扩展。

| Flavour | What | When |
|---------|------|------|
| **Replace** | ignore parent, write fresh | parent's behaviour irrelevant |
| **Extend** | call `super().method()`, add to it | want parent's work *plus* more |

| 风格 | 含义 | 何时使用 |
|------|------|---------|
| **替换（Replace）** | 忽略父类，全新编写 | 父类的行为不相关 |
| **扩展（Extend）** | 调用 `super().method()`，增加内容 | 需要父类的工作再加上更多 |

> 🎁 *Extend* = add a bow to an already-wrapped gift. *Replace* = rewrap from scratch. **Mark each override `# EXTEND` or `# REPLACE`.**
> 🇨🇳 🎁 *扩展* = 给已经包装好的礼物加上蝴蝶结。*替换* = 从头重新包装。**在每个覆盖方法处标记 `# EXTEND` 或 `# REPLACE`。**

## S2 — The MRO (this is the E3 drill — do it slowly) / MRO 方法解析顺序（这是 E3 专项练习 —— 慢慢做）

Python lets a class have **several** parents, searched **left-to-right**. The famous trap is the **diamond**: a shared ancestor reached by two paths. Python runs the ancestor **once**, via the **Method Resolution Order**.
> 🇨🇳 Python 允许一个类有多个父类，按从左到右的顺序搜索。著名的陷阱是**菱形继承（diamond）**：一个共享祖先通过两条路径可达。Python 通过**方法解析顺序（Method Resolution Order，MRO）** 确保该祖先只运行一次。

> The **MRO** is the single, flattened, deduplicated order Python searches to resolve a method. Inspect with `Class.__mro__`. `super()` delegates to **the next class in the MRO** — *not* simply "the parent."
> 🇨🇳 **MRO** 是 Python 解析方法时使用的一条扁平化、去重后的单一搜索顺序。可用 `Class.__mro__` 查看。`super()` 会委托给 **MRO 中的下一个类** —— 而不仅仅是“父类”。

```python
class Animal:    ...
class Bird(Animal):   ...
class Parrot(Bird):   ...
print(Parrot.__mro__)
# (Parrot, Bird, Animal, object)   ← children before parents; object is the universal base
```
> 🇨🇳 示例代码：三层继承的 `__mro__` 输出，子类在前，父类在后，`object` 是总基类。

> 🐛 **Your exact bug, dissected.** You wrote `super(Bird, self).__init__(name, "Squawk")` in `Parrot.__init__`. `super(Bird, self)` means "start the MRO search *after* `Bird`" — so it **skips `Bird.__init__` entirely**. Correct: `super().__init__(name)` then `self.sound = "Squawk"`. **`super()` with no args is what you want 99% of the time.**
> 🇨🇳 🐛 **你的确切 bug，剖析。** 你在 `Parrot.__init__` 中写了 `super(Bird, self).__init__(name, "Squawk")`。`super(Bird, self)` 意思是“从 MRO 中 `Bird` 之后开始搜索” —— 因此它**完全跳过了 `Bird.__init__`**。正确做法：`super().__init__(name)` 然后 `self.sound = "Squawk"`。**99% 的情况下，你应该使用无参数的 `super()`。**

> 🔮 **Predict the MRO (write it before revealing):**
> 🇨🇳 🔮 **预测 MRO（在展开前写下来）：**
> ```python
> class A: ...
> class B(A): ...
> class C(A): ...
> class D(B, C): ...
> ```
> What is `D.__mro__`?
> 🇨🇳 `D.__mro__` 是什么？
> <details><summary>reveal</summary>
> 🇨🇳 点击显示
>
> `(D, B, C, A, object)`. Rules: children before parents; left-to-right (`B` before `C`); the shared ancestor `A` appears **once**. This is **C3 linearization**.
> 🇨🇳 `(D, B, C, A, object)`。规则：子类先于父类；从左到右（`B` 先于 `C`）；共享祖先 `A` 只出现一次。这是 **C3 线性化（C3 linearization）**。
> </details>

## S3 — Polymorphism & Abstract Base Classes / 多态与抽象基类

**Polymorphism** = one call, type-specific behaviour, *no `if/elif` type-ladder*:
> 🇨🇳 **多态（Polymorphism）** = 一次调用，类型特定行为，*无需 `if/elif` 类型判断链*：

```python
for a in [Dog("Rex"), Cat("Whiskers")]:
    print(a.speak())      # each runs ITS OWN speak()
```
> 🇨🇳 示例代码：遍历不同对象，每个对象调用自己的 `speak()` 实现。

> 🔌 The universal power socket: the wall delivers power; lamp/kettle each do their own thing. Polymorphism lets you **delete** the `isinstance` ladder.
> 🇨🇳 🔌 万能电源插座：墙壁提供电力；台灯/水壶各做各的事。多态让你可以**删除** `isinstance` 条件链。

**Abstract Base Classes** enforce a contract. An ABC *can't be instantiated* and *forces* subclasses to implement every `@abstractmethod`:
> 🇨🇳 **抽象基类（Abstract Base Classes，ABCs）** 强制一个契约。ABC 不能被实例化，并且强制子类实现每一个 `@abstractmethod`：

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
    def describe(self):                 # CONCRETE — written once, inherited by all
        return f"Area={self.area():.2f}"
```
> 🇨🇳 示例代码：`Shape` 是一个 ABC，子类必须实现 `area` 方法，而 `describe` 为具体方法可直接继承。

> 📜 **Job-contract analogy.** `Shape` posts: "be any shape, but you *must* tell me `area()`; in return you get `describe()` free." HR (Python) rejects an incomplete subclass at instantiation.
> 🇨🇳 📜 **劳动合同类比。** `Shape` 发布：“可以是任何形状，但你*必须*告诉我 `area()`；作为回报，你免费获得 `describe()`。” 在实例化时，HR（Python）会拒绝不完整的子类。

> 🚀 **This is `nn.Module`.** Every PyTorch network subclasses `nn.Module` and *must* implement `forward()` — the exact "base defines the contract, you fill the required method" pattern.
> 🇨🇳 🚀 **这就是 `nn.Module`。** 每个 PyTorch 网络都子类化 `nn.Module`，并且*必须*实现 `forward()` —— 正是“基类定义契约，你填充必需方法”的模式。

## S4 — Math: dot product, norm, distance (the career formula) / 数学：点积、范数、距离（职业生涯公式）

**Algebraic:** `a · b = Σ aᵢbᵢ` → a single number. **Geometric:** `a · b = ‖a‖‖b‖cos θ`.
> 🇨🇳 **代数定义：** `a · b = Σ aᵢbᵢ` → 一个标量。**几何定义：** `a · b = ‖a‖‖b‖cos θ`。

| sign of `a·b` | angle | meaning |
|---------------|-------|---------|
| `> 0` | `< 90°` | similar direction |
| `= 0` | `= 90°` | **orthogonal** |
| `< 0` | `> 90°` | opposite |

| `a·b` 的符号 | 角度 | 含义 |
|-------------|------|------|
| `> 0` | `< 90°` | 相似方向 |
| `= 0` | `= 90°` | **正交（orthogonal）** |
| `< 0` | `> 90°` | 相反方向 |

**Cosine similarity** = the dot product with lengths divided out → direction only, in `[-1, 1]`.
> 🇨🇳 **余弦相似度（Cosine similarity）** = 除掉长度的点积 → 仅保留方向，结果在 `[-1, 1]` 范围。

> 🚀 **The single most important formula for your career.** An LLM turns a sentence into an **embedding**; "how similar are two sentences?" = cosine similarity of their embeddings. Every RAG system (Week 12) *is* cosine similarity at scale.
> 🇨🇳 🚀 **你职业生涯中最重要的一条公式。** 大语言模型将句子转换为**嵌入（embedding）**；“两个句子有多相似？”= 它们嵌入的余弦相似度。每一个 RAG 系统（第12周）本质上都是大规模余弦相似度。

**Norm & distance:** `‖a‖ = √(Σ aᵢ²)`; `dist(a,b) = ‖a−b‖`.
> 🇨🇳 **范数与距离：** `‖a‖ = √(Σ aᵢ²)`；`dist(a,b) = ‖a−b‖`。

## 🧠 Cheat-sheet / 速查表
```python
class Child(Parent):
    def __init__(self, ...):
        super().__init__(...)              # no-args super() = the right call almost always
Child.__mro__                              # the fixed search order; super() follows THIS
a·b = Σaᵢbᵢ = ‖a‖‖b‖cosθ ;  cos_sim = a·b/(‖a‖‖b‖) ;  ‖a‖=√Σaᵢ²
```
> 🇨🇳 关键代码与公式：子类构造、MRO 查看、点积与余弦相似度计算。

## ⚠️ Common pitfalls / 常见陷阱
1. **`super(Bird, self)`** when you mean `super()` → silently skips a class in the MRO (your E3 bug).
   > 🇨🇳 本想使用 `super()` 却误用了 `super(Bird, self)` → 无声无息地跳过了 MRO 中的一个类（你的 E3 bug）。
2. **Forgetting `super().__init__()`** → half-built object, later `AttributeError`.
   > 🇨🇳 忘记调用 `super().__init__()` → 半构建的对象，随后出现 `AttributeError`。
3. **`isinstance` ladders** → that's polymorphism asking to be used.
   > 🇨🇳 `isinstance` 条件链 → 那是多态正在呼唤被使用。

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — Animal tree + Shape ABC, with an MRO you must *predict before printing*.
> 🇨🇳 ➡️ **动手构建：** [`HOMEWORK.md`](./HOMEWORK.md) —— 动物继承树 + Shape ABC，含有一个你必须*在打印前预测*的 MRO。
