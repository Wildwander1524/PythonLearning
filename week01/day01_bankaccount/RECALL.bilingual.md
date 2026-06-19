# 🔁 Day 1 — RECALL (retrieval practice) / 第1天 — 回忆（检索练习）

> **How to use:** answer from a **blank mind** — no scrolling up, no notes. Struggling to retrieve *is* the learning (Bjork's desirable difficulty). Do this once after the lesson, then **again cold tomorrow morning** before Day 2. Mark what you blanked on in [`../learning-records/`](../learning-records/). Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).
>
> *(Day 1 is the first day, so there's no spaced callback yet — that starts in D2's RECALL, which will re-test today's material cold.)*

> 🇨🇳 **使用方法：** 清空大脑回答——不向上滚动，不看笔记。努力回忆*就是*学习（Bjork 的“可取困难”）。课后做一次，然后在第2天开始前**明天早上再次冷回忆**。把你遗忘的内容标记在 [`../learning-records/`](../learning-records/) 中。答案：[`SOLUTIONS.md`](./SOLUTIONS.md)。
>
> 🇨🇳 *（第1天是第一天，所以还没有间隔回调——这将在第2天的 RECALL 中开始，会重新冷测试今天的材料。）*

## A · Free recall (write 3–4 sentences, no peeking) / A · 自由回忆（写3-4句话，不许偷看）
Explain to an imaginary beginner: *what is a class, what is an object, and what is `self`?* Use one analogy. (This is the Feynman test — if you reach for jargon to cover a gap, you found the gap.)

> 🇨🇳 向一个想象中的初学者解释：*什么是类，什么是对象，什么是 `self`？* 用一个类比。（这是费曼测试——如果你用专业术语来掩盖知识的缺口，你就找到了这个缺口。）

## B · Concept questions / B · 概念问题
1. `__init__` is often called "the constructor." Why is "**initializer**" more accurate?
   > 🇨🇳 1. `__init__` 常被称为“构造器”。为什么“**初始化器**”更准确？
2. State the **instance vs class attribute** rule in one sentence, then give one good use of each.
   > 🇨🇳 2. 用一句话说明**实例属性 vs 类属性**的规则，然后分别给出每种的一个好用法。
3. What makes a property **read-only**, and why would you *want* that for `balance`?
   > 🇨🇳 3. 什么使得一个属性是**只读的**，为什么你会*希望* `balance` 是只读的？
4. Your `history()` returns `list(self._history)` instead of `self._history`. What attack does the copy prevent?
   > 🇨🇳 4. 你的 `history()` 返回 `list(self._history)` 而不是 `self._history`。这个复制能防止什么攻击？
5. Why is a `list` (not a tuple grown with `+=`) the right container for history? (Cost reason.)
   > 🇨🇳 5. 为什么 `list`（而不是用 `+=` 增长的元组）是存储历史的合适容器？（成本原因）

## C · Predict the output / C · 预测输出
```python
class Counter:
    total = 0
    def __init__(self):
        self.total += 1          # note: self, not Counter

a, b, c = Counter(), Counter(), Counter()
print(Counter.total)             # ?
print(a.total, b.total, c.total) # ?
```
> 🇨🇳 这段代码定义了一个 `Counter` 类，`total` 为类属性，但在 `__init__` 中通过 `self.total += 1` 创建了实例属性 `total`，导致类属性未被修改，且每个实例有自己的 `total`。

What prints, and *why*? (This is growth-edge E-counter — the trap you avoided; keep avoiding it.)

> 🇨🇳 打印什么，*为什么*？（这是成长边界“计数器陷阱”——你避开的陷阱；继续避开它。）

## D · Micro-build (from a blank file, 5 min) / D · 微构建（从空白文件开始，5分钟）
Write — without looking — a `Temperature` class: stores `_celsius`; exposes a **read-only** `celsius` property and a **read-only** `fahrenheit` property (computed: `c*9/5+32`); a class attribute `unit_system = "metric"`. Then instantiate and print both. *(This re-uses today's exact skills on a fresh problem — the real mastery test.)*

> 🇨🇳 在不看代码的情况下编写——一个 `Temperature` 类：存储 `_celsius`；暴露一个**只读** `celsius` 属性和一个**只读** `fahrenheit` 属性（计算：`c*9/5+32`）；一个类属性 `unit_system = "metric"`。然后实例化并打印两者。*（这是将今天学到的技能用到新问题上——真正的掌握测试。）*

## E · Math (by hand) / E · 数学（手算）
1. `[5, -2] + [1, 6]` = ?
   > 🇨🇳 1. `[5, -2] + [1, 6]` = ?
2. `3 · [2, 0, -1]` = ?
   > 🇨🇳 2. `3 · [2, 0, -1]` = ?
3. What single vector is `[7, 7] + (-1)·[7, 7]`, and what's the one-word name for the operation `v + (-1)·v`?
   > 🇨🇳 3. `[7, 7] + (-1)·[7, 7]` 得到的单一向量是什么？操作 `v + (-1)·v` 的单字名称是什么？

---
> ⏱️ **Self-rating:** could you do section D cold *tomorrow*? Honest y/n → record it. A "no" isn't failure; it's the signal that tells tomorrow's spaced review what to hit.

> 🇨🇳 ⏱️ **自评：** 你能在*明天*冷回忆的情况下完成 D 部分吗？如实 y/n → 记录下来。“不”不是失败；它是告诉明天的间隔复习该攻击哪里的信号。
