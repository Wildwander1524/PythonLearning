# 🔁 Day 3 — RECALL (retrieval + spaced review)
> 🇨🇳 **🔁 第三天 — 回忆（检索 + 间隔复习）**

> Blank mind. Once after the lesson, again cold before Day 4. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).
> 🇨🇳 一片空白。学完课立即一次，第四天前不复习再次回想。答案见：[`SOLUTIONS.md`](./SOLUTIONS.md)。

## 🔁 Spaced — D1 & D2 (from memory)
> 🇨🇳 **🔁 间隔复习 — D1 & D2（凭记忆）**

- S1 (D1) what does a read-only `@property` protect, and how do you make one?
> 🇨🇳 S1（D1）只读 `@property` 保护了什么，如何创建？
- S2 (D2) **predict** `Parrot.__mro__` for `Parrot(Bird)`, `Bird(Animal)`. (E3 — must be cold.)
> 🇨🇳 S2（D2）**预测** `Parrot(Bird)`、`Bird(Animal)` 的 `Parrot.__mro__`。（E3 — 必须在不复习的情况下完成）
- S3 (D2) cosine similarity formula, and why it's used over the raw dot product for embeddings.
> 🇨🇳 S3（D2）余弦相似度公式，以及为什么在嵌入中使用它而非原始点积。

## A · Free recall
> 🇨🇳 **A · 自由回忆**

In your own words: *why is built-in syntax like `len(x)` and `a + b` "just" method calls?* What
does that buy Python (and you)?
> 🇨🇳 用你自己的话说：*为什么像 `len(x)` 和 `a + b` 这样的内置语法"只是"方法调用？* 这给 Python（和你）带来了什么好处？

## B · Concept questions
> 🇨🇳 **B · 概念问题**

1. Which of `__repr__`/`__str__` must you **always** define, and why? Which falls back to which?
> 🇨🇳 1. 你必须**始终**定义 `__repr__` 和 `__str__` 中的哪一个，为什么？哪个会回退到哪个？
2. You define `__eq__`; now `set()` of your objects raises `TypeError`. Explain the rule and both
   fixes (immutable vs mutable).
> 🇨🇳 2. 你定义了 `__eq__`；现在用 `set()` 存放你的对象却抛出 `TypeError`。解释这一规则以及两种修复方法（不可变 vs 可变）。
3. Two distinct ways to make `for x in obj:` work.
> 🇨🇳 3. 让 `for x in obj:` 能工作的两种不同方法。
4. Why return `NotImplemented` (not `False`) from `__eq__` for an unknown type?
> 🇨🇳 4. 为什么在 `__eq__` 中遇到未知类型时返回 `NotImplemented`（而不是 `False`）？
5. What is a **generator**, and why prefer it to hand-writing `__next__`?
> 🇨🇳 5. 什么是**生成器**，为什么它优于手动编写 `__next__` 方法？

## C · Predict the output
> 🇨🇳 **C · 预测输出**

```python
class V:
    def __init__(self, x): self.x = x
    def __add__(self, o): self.x += o.x; return self     # ⚠️ note this
a = V(1); b = V(2)
c = a + b
print(a.x, c.x, a is c)
```
> 🇨🇳 *定义了修改自身并返回自身的 `__add__` 方法，破坏了加法应返回新对象的语义。*

What prints — and what *rule* did this code break?
> 🇨🇳 输出什么——并且这段代码违反了哪条*规则*？

## D · Micro-build (blank file, 8 min)
> 🇨🇳 **D · 微型构建（空白文件，8分钟）**

A `Fraction(num, den)`: `__repr__` → `'Fraction(1, 2)'`; `__eq__` by cross-multiplication
(`1/2 == 2/4`); `__add__` returning a **new** `Fraction` (`a/b + c/d = (ad+bc)/bd`). No
simplification needed.
> 🇨🇳 一个 `Fraction(num, den)` 类：`__repr__` → `'Fraction(1, 2)'`；`__eq__` 通过交叉乘法实现（`1/2 == 2/4`）；`__add__` 返回一个**新**的 `Fraction` 对象（`a/b + c/d = (ad+bc)/bd`）。无需化简。

## E · Math (by hand)
> 🇨🇳 **E · 手算数学**

1. Transpose of `[[1,2],[3,4],[5,6]]` — entries and shape?
> 🇨🇳 1. `[[1,2],[3,4],[5,6]]` 的转置——元素和形状？
2. `[[1,2],[3,4]] · [10, 20]` (matrix×vector) = ?
> 🇨🇳 2. 矩阵乘向量 `[[1,2],[3,4]] · [10, 20]` = ？
3. `[[0,-1],[1,0]] · [1,0]` = ? (this matrix rotates 90° — do you see it?)
> 🇨🇳 3. `[[0,-1],[1,0]] · [1,0]` = ？（该矩阵旋转90°——你看出来了吗？）

---
> ⏱️ Could you do section D cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
> 🇨🇳 ⏱️ 明天能冷做 D 部分吗？ y/n → [`../learning-records/`](../learning-records/)。
