# 🔁 Day 2 — RECALL (retrieval practice + first spaced review) / 🔁 第二天 — 回忆（检索练习 + 首次间隔复习）

> Blank mind, no scrolling. Do once after the lesson, then **cold tomorrow before Day 3**. Answers in [`SOLUTIONS.md`](./SOLUTIONS.md). Log blanks in [`../learning-records/`](../learning-records/).
> 🇨🇳 清空大脑，不要翻阅。课后做一次，然后**明天冷回忆**，在第三天之前。答案见 [`SOLUTIONS.md`](./SOLUTIONS.md)。空白部分记录在 [`../learning-records/`](../learning-records/)。

## 🔁 Spaced — Day 1 (answer from memory, this is the interleaving) / 🔁 间隔 — 第一天（凭记忆回答，这是交错练习）
S1. Instance vs class attribute — rule + one use of each.
> 🇨🇳 S1. 实例属性与类属性 — 规则及各自的一种用途。
S2. What single thing makes a property read-only?
> 🇨🇳 S2. 哪一件事会让属性变为只读？
S3. `[2,3] + 2·[1,-1]` = ?  *(if you blank, that's the signal — then check D1 SOLUTIONS)*
> 🇨🇳 S3. `[2,3] + 2·[1,-1]` = ?  *(如果你空白，那是信号——然后检查 D1 SOLUTIONS)*

## A · Free recall / A · 自由回忆
Explain `super()` to a beginner *without* saying "the parent class." (If you can't avoid that phrase accurately, re-read the MRO section — that's the whole point of today.)
> 🇨🇳 向初学者解释 `super()`，并且*不说*“父类”。（如果你无法准确避免这个说法，重新阅读 MRO 部分——这就是今天的关键。）

## B · Concept questions / B · 概念问题
1. **Extend vs replace** — what's the difference, and which is the safer default? Why?
   > 🇨🇳 1. **扩展与替换** — 区别是什么？哪个是更安全的默认选择？为什么？
2. What does an **ABC** guarantee, and *when* does it fail an incomplete subclass — at definition or at instantiation?
   > 🇨🇳 2. **抽象基类（ABC）** 保证了什么？它在什么时候会检查出不完整的子类——定义时还是实例化时？
3. Why does defining `total_area` with polymorphism beat an `isinstance` ladder when a new shape is added?
   > 🇨🇳 3. 当添加新形状时，为什么用多态定义 `total_area` 胜过一长串 `isinstance` 判断？
4. Geometric meaning of `a·b = 0`? Of `a·b < 0`?
   > 🇨🇳 4. `a·b = 0` 的几何含义是什么？`a·b < 0` 呢？
5. What is **cosine similarity**, and why is it (not the raw dot product) used to compare sentence embeddings?
   > 🇨🇳 5. 什么是**余弦相似度（cosine similarity）**，为什么用它（而不是原始点积）来比较句子嵌入（sentence embeddings）？

## C · Predict the MRO (the E3 mastery rep) / C · 预测 MRO（E3 精通复现）
```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...
class E(C): ...
class F(D, E): ...
```
> 🇨🇳 这段代码定义了一个类层次结构，用于练习方法解析顺序（MRO）：A 是基类，B、C 继承 A，D 继承 B 和 C，E 继承 C，F 继承 D 和 E。

Write `F.__mro__` **before** checking. (Hint: children before parents; left-to-right; each ancestor appears once, after all paths to it.) Then *verify in a REPL*.
> 🇨🇳 在检查之前写出 `F.__mro__`。（提示：子类先于父类；从左到右；每个祖先只出现一次，出现在所有通向它的路径之后。）然后在 REPL 中*验证*。

## D · Spot-the-bug / D · 找Bug
```python
class Parrot(Bird):
    def __init__(self, name):
        super(Bird, self).__init__(name, "Squawk")   # what's wrong?
```
> 🇨🇳 这段代码错误地使用了 `super(Bird, self)`，跳过了 Parrot 自己的 MRO，直接查找 Bird 的父类，破坏了协作继承顺序。

Name the bug, say what it does to the MRO, and write the correct two lines.
> 🇨🇳 指出 bug，说明它对 MRO 的影响，并写出正确的两行代码。

## E · Micro-build (blank file, 8 min) / E · 微型构建（空白文件，8分钟）
An ABC `PaymentMethod` with abstract `pay(amount)`; two concrete subclasses (`Cash`, `Card`); a function `checkout(methods, amount)` that calls `.pay(amount)` on each **with no `isinstance`**. Confirm `PaymentMethod()` raises `TypeError`.
> 🇨🇳 一个抽象基类 `PaymentMethod`，包含抽象方法 `pay(amount)`；两个具体子类（`Cash`、`Card`）；一个函数 `checkout(methods, amount)`，对每个支付方式调用 `.pay(amount)`，**不使用 `isinstance`**。确认 `PaymentMethod()` 会引发 `TypeError`。

## F · Math (by hand) / F · 数学（手算）
1. `[1,2,2] · [2,0,1]` = ?    2. `‖[6,8]‖` = ?    3. cosine similarity of `[1,0]` and `[1,1]` = ?
> 🇨🇳 1. `[1,2,2] · [2,0,1]` = ?    2. `‖[6,8]‖` = ?    3. `[1,0]` 和 `[1,1]` 的余弦相似度 = ?

---
> ⏱️ Could you produce section C's MRO cold tomorrow? y/n → record it. Two spaced "yes" = edge **E3 graduates**.
> 🇨🇳 ⏱️ 你明天能冷不丁写出 C 部分的 MRO 吗？y/n → 记录下来。两次间隔“是的” = 达成 **E3 毕业**。
