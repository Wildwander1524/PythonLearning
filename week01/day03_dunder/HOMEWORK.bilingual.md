# 📝 Day 3 Homework — `Vector2D` (make an object feel native)
> 🇨🇳 第3天作业 — `Vector2D`（让对象像内置类型一样自然）

> **Goal:** a 2-D vector that prints, compares, adds, subtracts, scales, indexes, and iterates —
> via dunder methods. And `abs(v)` = the Day-2 **norm**; `v.dot(w)` = the Day-2 **dot product**.
> **Time:** 3 h · **Read first:** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **目标：** 一个二维向量，通过双下划线方法实现打印、比较、相加、相减、缩放、索引和迭代。`abs(v)` 返回第2天的**范数**；`v.dot(w)` 返回第2天的**点积**。
> **时间：** 3 小时 · **先阅读：** [`LESSON.md`](./LESSON.md)

## 📖 Before you code
> 🇨🇳 开始编码前

The test for *every* method: *"does this make my object behave more like a built-in `int`/
`list`?"* Re-read the **golden rule** (operators return a **new** object) and the **generator**
shortcut (`__iter__` via `yield`).
> 🇨🇳 对每个方法都要检查：*"这能让我的对象更像内置的 `int` 或 `list` 吗？"* 重新阅读**金科玉律**（操作符返回一个**新**对象）和**生成器**快捷方式（通过 `yield` 实现 `__iter__`）。

## ⏱️ Budget
> 🇨🇳 时间预算

| Block | Time | Build |
|-------|------|-------|
| A | 60 min | `__init__`, `__repr__`, `__eq__`, `__add__`, `__sub__` |
| B | 60 min | `__mul__` (scalar), `__abs__` (magnitude), `dot()` |
| C | 30 min | `__getitem__`, `__iter__` (generator) |
| D | 30 min | tests, run, push |

| 模块 | 时间 | 构建内容 |
|------|------|----------|
| A | 60 分钟 | `__init__`, `__repr__`, `__eq__`, `__add__`, `__sub__` |
| B | 60 分钟 | `__mul__`（标量乘法），`__abs__`（模长），`dot()` |
| C | 30 分钟 | `__getitem__`, `__iter__`（生成器） |
| D | 30 分钟 | 测试、运行、推送 |

## Requirements — all of this must work
> 🇨🇳 需求 —— 所有这些功能都必须能正常工作

```python
v, w = Vector2D(3, 4), Vector2D(1, 2)
repr(v)              # 'Vector2D(3, 4)'      (round-trips)
v == Vector2D(3, 4)  # True
v + w                # Vector2D(4, 6)        (NEW object — v unchanged)
v - w                # Vector2D(2, 2)
v * 2                # Vector2D(6, 8)
abs(v)               # 5.0                   = ‖v‖, the D2 NORM
v.dot(w)             # 11                    = v·w, the D2 DOT PRODUCT
v[0], v[1]           # 3, 4
x, y = v             # unpacking via iteration
list(v)              # [3, 4]
```
> 🇨🇳 *所有这些用法都必须能正常工作*

### Checklist
> 🇨🇳 检查清单

- [ ] `__repr__` → `'Vector2D(3, 4)'` (round-trip ideal).
- [ ] `__eq__` compares both components; returns **`NotImplemented`** (not `False`) for non-`Vector2D`.
- [ ] `__add__`, `__sub__`, `__mul__` return a **new** `Vector2D` — never mutate `self`.
- [ ] `__abs__` = `√(x²+y²)` (the norm). `dot(other)` = `x·x' + y·y'`.
- [ ] `__getitem__` supports `v[0]`/`v[1]`, raises `IndexError` otherwise (so iteration can stop).
- [ ] `__iter__` yields `x` then `y` (use a **generator**).
- [ ] `__repr__` → `'Vector2D(3, 4)'`（理想的可逆表示）
- [ ] `__eq__` 会比较两个分量；对非 `Vector2D` 类型返回 **`NotImplemented`**（而不是 `False`）
- [ ] `__add__`、`__sub__`、`__mul__` 都返回一个**新**的 `Vector2D`，绝不修改 `self`
- [ ] `__abs__` = `√(x²+y²)`（范数）；`dot(other)` = `x·x' + y·y'`
- [ ] `__getitem__` 支持 `v[0]`/`v[1]`，否则抛出 `IndexError`（让迭代可以停下来）
- [ ] `__iter__` 用生成器依次 `yield` `x` 和 `y`

## Tests (`test_vector2d.py`)
> 🇨🇳 测试（`test_vector2d.py`）

At least: `v + w == Vector2D(4,6)` · `abs(Vector2D(3,4)) == 5.0` · `Vector2D(3,4).dot(Vector2D(1,
2)) == 11` · `list(Vector2D(3,4)) == [3,4]` · `v[2]` raises `IndexError` · **`v + w` leaves `v`
unchanged** (proves the golden rule).
> 🇨🇳 至少包含这些测试：`v + w == Vector2D(4,6)` · `abs(Vector2D(3,4)) == 5.0` · `Vector2D(3,4).dot(Vector2D(1,2)) == 11` · `list(Vector2D(3,4)) == [3,4]` · `v[2]` 抛出 `IndexError` · **`v + w` 之后 `v` 的值不变**（证明黄金法则）。

## 🧠 Concept checks (comment at bottom of `vector2d.py`)
> 🇨🇳 概念检查（写在 `vector2d.py` 底部注释中）

1. Why must `__add__` return a new `Vector2D` (cookie-recipe reasoning)?
2. Your `__iter__` uses `yield` — what two values, and how does Python know to stop?
3. Delete `__repr__`: what does `[Vector2D(3,4)]` print, and why is that bad?
1. 为什么 `__add__` 必须返回一个新的 `Vector2D`（用饼干配方的类比推理）？
2. 你的 `__iter__` 使用了 `yield` —— 会产生哪两个值，Python 怎么知道什么时候停止？
3. 删除 `__repr__`：`[Vector2D(3,4)]` 会打印出什么，为什么不好？

## ✅ Definition of done
> 🇨🇳 完成定义

Every Requirements line runs as shown · tests green · concept checks answered · pushed.
> 🇨🇳 每条需求都像展示的那样运行 · 测试通过 · 概念检查已回答 · 已推送。

## 🌟 Stretch
> 🇨🇳 进阶挑战

- `__rmul__` so `2 * v` works — trace *why* (`int.__mul__(2,v)` → `NotImplemented` →
  `v.__rmul__(2)`).
- `__neg__` so `-v == Vector2D(-x,-y)`.
- Make it **hashable**: add `__hash__` (you defined `__eq__`). Why only safe if treated as
  immutable? (coat-check reasoning).
- Generalize to `VectorND(*components)` with a tuple internally — `__iter__`, `dot`, `__abs__`
  all generalize. *(This is Ramalho's `Vector` from Fluent Python Ch.1 — compare yours to his.)*
- `__rmul__` 让 `2 * v` 也能工作 —— 追溯一下**原因**（`int.__mul__(2,v)` → `NotImplemented` → `v.__rmul__(2)`）
- `__neg__` 让 `-v == Vector2D(-x,-y)` 成立
- 使其**可哈希**：添加 `__hash__`（因为你定义了 `__eq__`）。为什么只有在对象被视为不可变时才是安全的？（衣帽间推理）
- 泛化为 `VectorND(*components)` 内部使用元组 —— `__iter__`、`dot`、`__abs__` 都可以通用化。*（这就是 Ramalho 在《流畅的 Python》第1章里的 `Vector` —— 把你的实现和他的对比一下）*

## 🚀 Submit
> 🇨🇳 提交

```bash
git add week01/day03_dunder && git commit -m "add: Week1 D3 Vector2D (data model)" && git push
```
> 🇨🇳 *将作业提交到 Git 仓库*

➡️ Then [`RECALL.md`](./RECALL.md), and again cold before Day 4.
> 🇨🇳 然后完成 [`RECALL.md`](./RECALL.md)，并且在第4天之前再复习一次（冷启动记忆）。
