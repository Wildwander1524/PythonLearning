# 🔁 Day 5 — RECALL (retrieval + spaced review)
> 🇨🇳 **第5天 — 回顾（检索 + 间隔复习）**

> Blank mind. Once after the lesson, again cold before Day 6. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).
> 🇨🇳 放空大脑：学完后做一次，第6天前再冷启动做一次。答案见：[`SOLUTIONS.md`](./SOLUTIONS.md)。

## 🔁 Spaced — D1, D3, D4 (from memory)
> 🇨🇳 **间隔复习 — D1，D3，D4（凭记忆回答）**

S1 (D1) why validate + `raise` on bad input *immediately* rather than later?
> 🇨🇳 S1（D1）为什么对错误输入要立即验证并`raise`，而不是推迟处理？

S2 (D3) which dunder does `for x in obj:` use, and the two ways to support it?
> 🇨🇳 S2（D3）`for x in obj:` 使用了哪个双下划线方法？支持它的两种方式是什么？

S3 (D4) the mutable-default trap — what's shared, when is it created, what's the fix?
> 🇨🇳 S3（D4）可变默认值的陷阱——共享的是什么？什么时候创建？如何修复？

## A · Free recall
> 🇨🇳 **A · 自由回忆**

Explain to a beginner what a **context manager** guarantees and *why* you'd want it, with one
analogy. Which two methods implement it?
> 🇨🇳 向初学者解释**上下文管理器**保证什么、为什么需要它，并给出一个类比。它由哪两个方法实现？

## B · Concept questions
> 🇨🇳 **B · 概念题**

1. `except` vs `else` vs `finally` — when does each run?
   > 🇨🇳 `except`、`else`、`finally` 分别在什么时候执行？

2. Why prefer **EAFP** over LBYL in Python? Give the race-condition reason.
   > 🇨🇳 在 Python 中为什么倾向于 **EAFP**（请求宽恕）而非 LBYL（提前检查）？从竞态条件角度给出原因。

3. Why build an exception **hierarchy** instead of one `Exception`? What does the caller gain?
   > 🇨🇳 为什么要构建异常**层级**，而不是只用一个 `Exception`？调用者能得到什么好处？

4. What does `__exit__` returning `True` do, and why is `False` the right default?
   > 🇨🇳 `__exit__` 返回 `True` 会怎样？为什么默认返回 `False` 是合理的？

5. What makes a folder a **package**, and what does `if __name__ == "__main__":` accomplish?
   > 🇨🇳 什么使得一个文件夹成为**包**？`if __name__ == "__main__":` 的作用是什么？

## C · Predict the behavior
> 🇨🇳 **C · 预测行为**

```python
class Guard:
    def __enter__(self): print("enter"); return self
    def __exit__(self, *a): print("exit"); return False
with Guard():
    print("body")
    raise ValueError("boom")
print("after")
```
> 🇨🇳 *[演示 with 语句中异常抛出后，`__exit__` 返回 `False` 会重新引发异常，导致 "after" 不会打印]*

What prints, in what order, and does `"after"` print? Why?
> 🇨🇳 会打印什么？顺序是什么？`"after"` 会打印吗？为什么？

## D · Micro-build (blank file, 10 min)
> 🇨🇳 **D · 微构建（空白文件，10分钟）**

A `TempFile` context manager: `__enter__` creates a file and returns its path; `__exit__` deletes
the file **even if the block raised**. Prove (in a comment) which line guarantees deletion on the
error path.
> 🇨🇳 实现一个 `TempFile` 上下文管理器：`__enter__` 创建一个文件并返回文件路径；`__exit__` 删除文件，**即使代码块抛出了异常**。在注释中证明哪一行保证了错误路径上的删除。

## E · Math (by hand)
> 🇨🇳 **E · 数学（手算）**

1. Write `[7, -2]` as a linear combination of `[1,0]` and `[0,1]`.
   > 🇨🇳 将 `[7, -2]` 表示为 `[1,0]` 和 `[0,1]` 的线性组合。

2. Are `[1,1]` and `[1,-1]` linearly independent? What do they span?
   > 🇨🇳 `[1,1]` 与 `[1,-1]` 线性无关吗？它们张成什么空间？

3. What is `span([0,0])`? (think about what scaling the zero vector can give)
   > 🇨🇳 `span([0,0])` 是什么？（想想零向量缩放能得到什么）

---
> ⏱️ Could you write the `TempFile` (D) cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
> 🇨🇳 ⏱️ 明天不看笔记，你能凭记忆写出 `TempFile`（D）吗？是/否 → [`../learning-records/`](../learning-records/)。
