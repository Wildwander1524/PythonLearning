# 🔁 Day 6 — RECALL (cumulative whole-week retrieval test)
> 🇨🇳 **[🔁 第六天 — 回忆（整周累积检索测试）]**

> This is the week's big interleaved quiz — every day, mixed. **Say each answer out loud
> (Feynman) before checking.** Cover the answers in [`SOLUTIONS.md`](./SOLUTIONS.md). Your score
> is a *diagnostic*: it tells you which day to rebuild from a blank file in the catch-up slot.
> 🇨🇳 这是本周的大型交叉测验——每天的内容都混合在一起。**在查看答案前，先大声说出每个答案（费曼技巧）。** 答案在 [`SOLUTIONS.md`](./SOLUTIONS.md) 中。你的分数是一个*诊断*：它告诉你需要在补课时间段从空白文件重新构建哪一天的内容。

## Part 1 · Concepts (17)
> 🇨🇳 **[第一部分 · 概念（17 道）]**

**OOP fundamentals (D1)**
> 🇨🇳 OOP 基础（D1）

1. Instance vs class attribute — difference, and when each is right?
   实例属性与类属性——区别是什么，各自适用于什么场景？
2. What does `@property` give you, and why prefer it to a plain attribute?
   `@property` 给了你什么，为什么更倾向于使用它而不是普通属性？
3. Why return a *copy* from a method like `history()`?
   为什么像 `history()` 这样的方法要返回一份*副本*？

**Inheritance, polymorphism, ABC, MRO (D2)**
> 🇨🇳 继承、多态、抽象基类、MRO（D2）

4. Inheritance vs composition — the one-sentence test?
   继承与组合——用一句话判断是什么？
5. What does `super().__init__()` do, and what breaks if you forget it?
   `super().__init__()` 做了什么，忘记它会破坏什么？
6. What is an ABC, and what happens if a subclass skips an `@abstractmethod`?
   什么是 ABC，如果子类遗漏了 `@abstractmethod` 会发生什么？
7. In multiple inheritance, what does `super()` actually point to — and what is the **MRO**?
   *(Bonus: give `D.__mro__` for `class D(B, C)`, `B(A)`, `C(A)`.)*
   在多重继承中，`super()` 实际指向什么——以及什么是 **MRO**？
   *（加分题：给出 `class D(B, C)`, `B(A)`, `C(A)` 的 `D.__mro__`。）*

**Data model (D3)**
> 🇨🇳 数据模型（D3）

8. `__str__` vs `__repr__` — who calls each, which must you always define?
   `__str__` 与 `__repr__`——各自由谁调用，哪个是你必须始终定义的？
9. Two ways to make `for x in obj:` work?
   使 `for x in obj:` 可循环的两种方法？
10. What should `a + b` return — a mutated `a` or a new object? Why?
    `a + b` 应当返回什么——被修改的 `a` 还是一个全新的对象？为什么？
11. You defined `__eq__` and now your object won't go in a `set`. Why, and how do you fix it?
    你定义了 `__eq__`，现在对象却无法放入 `set`。为什么，如何修复？

**Design (D4)**
> 🇨🇳 设计（D4）

12. Why is `def f(items=[])` a bug — what's shared, and what's the fix?
    为什么 `def f(items=[])` 是个陷阱——共享了什么，如何修复？
13. When is `@dataclass` right, and how do you give it a mutable default safely?
    什么时候适合使用 `@dataclass`，如何安全地为其提供可变默认值？
14. What does `__slots__` trade away, and when is it worth it?
    `__slots__` 牺牲了什么，什么时候值得？

**Errors & context (D5)**
> 🇨🇳 错误与上下文（D5）

15. Difference between `except`, `else`, and `finally`?
    `except`、`else` 和 `finally` 的区别？
16. What does a context manager guarantee, and which two methods implement it?
    上下文管理器保证什么，由哪两个方法实现？
17. What makes a folder a package, and what does `if __name__ == "__main__":` do?
    什么使一个文件夹成为包，`if __name__ == "__main__":` 有什么作用？

> 🎯 **Score honestly:** 15–17 clean → proceed. 10–14 → rebuild the weak days' homework from a
> blank file in catch-up. <10 → spend today re-reading and tell me; we'll re-pace Week 2 rather
> than build on sand.
> 🇨🇳 🎯 **诚实评分：** 15–17 分且清晰无误 → 继续前进。10–14 → 在补课时间里，从空白文件重新构建薄弱天数的作业。小于 10 → 今天花时间重读并告知我；我们将重新规划第二周的节奏，而不是在沙滩上筑楼。

## Part 2 · Math (12 — by hand, then verify)
> 🇨🇳 **[第二部分 · 数学（12 道 — 先手算，再验证）]**

```text
 1. [2, 3] + [4, 1] = ?
 2. 3 · [1, -2] = ?
 3. [1, 2, 2] · [2, 0, 1] = ?              (dot product)
 4. ‖[6, 8]‖ = ?
 5. distance between [1, 1] and [4, 5] = ?
 6. cosine similarity of [1, 0] and [1, 1] = ?
 7. transpose of [[1,2],[3,4],[5,6]] → entries? shape?
 8. [[1, 2], [3, 4]] · [10, 20] = ?        (matrix × vector)
 9. [[2, 0], [1, 3]] · [[1, 4], [0, 5]] = ?  (matrix × matrix — domino-check first)
10. write [7, -2] as a linear combination of [1,0] and [0,1]
11. are [1,2] and [2,4] independent? what is their span?
12. [[1,2],[3,4]] · identity = ? (predict before computing)
```
> 🇨🇳 *[数学题目：向量加法、数乘、点积、范数、距离、余弦相似度、转置、矩阵乘向量、矩阵乘矩阵、线性组合、线性无关与张成空间、单位矩阵乘法预测]*

## Part 3 · The blank-file test (the real benchmark)
> 🇨🇳 **[第三部分 · 空白文件测试（真正的基准）]**

Without looking at any file, rebuild **one** of: D3 `Vector2D` *or* D5 `FileLogger`. Recognizing
your old code is easy; *reproducing* it from nothing is mastery. Whatever you can't reproduce is
precisely today's re-study target.
> 🇨🇳 不查看任何文件，重新构建 **一个** 类：D3 的 `Vector2D` 或 D5 的 `FileLogger`。认出旧代码很容易；*从零重现*才是掌握。你无法重现的部分，正是今天的复习目标。

---
> 📝 Final record for the week: in [`../learning-records/`](../learning-records/), note your quiz
> score, which day you rebuilt blind, and whether edges **E1–E4** (see
> [`../MISSION.md`](../MISSION.md)) each got retrieved after a gap. That closes the loop.
> 🇨🇳 📝 本周最终记录：在 [`../learning-records/`](../learning-records/) 中，记下你的测验分数、你在空白测试中重新构建的是哪一天的内容，以及边界案例 **E1–E4**（参见 [`../MISSION.md`](../MISSION.md)）是否在间隔后都被检索到了。这样就完成了闭环。
