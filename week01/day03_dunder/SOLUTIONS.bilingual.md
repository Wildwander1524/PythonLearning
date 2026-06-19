# ✅ Day 3 — SOLUTIONS
> 🇨🇳 ✅ 第3天 — 解答

> After a real attempt only.
> 🇨🇳 只在实际尝试之后。

## Reference — `vector2d.py`
> 🇨🇳 参考 — `vector2d.py`

```python
import math

class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"          # round-trips

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented                        # let Python try the reflected ==
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)   # NEW object
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, k):                                # scalar
        return Vector2D(self.x * k, self.y * k)

    def __abs__(self):
        return math.hypot(self.x, self.y)                # = √(x²+y²) = the D2 NORM
    def dot(self, other):
        return self.x * other.x + self.y * other.y       # = the D2 DOT PRODUCT

    def __getitem__(self, i):
        if i == 0: return self.x
        if i == 1: return self.y
        raise IndexError("Vector2D index out of range")  # lets iteration detect the end
    def __iter__(self):
        yield self.x                                     # generator = iterator for free
        yield self.y

    # Stretch:
    def __rmul__(self, k): return self * k               # 2 * v
    def __neg__(self): return Vector2D(-self.x, -self.y)
    def __hash__(self): return hash((self.x, self.y))    # safe only if treated as immutable
```
> 🇨🇳 *二维向量类，支持加、减、标量乘、点积、迭代、长度等运算，包含特殊方法。*

> Note `__abs__` uses `math.hypot(x, y)` — the *correct* use of hypot (Euclidean length of a
> 2-vector), in contrast to Day 2 where `hypot` was wrongly substituted for Heron's formula.
> Same function, right tool here, wrong tool there — the lesson is *match the formula to the job*.
> 🇨🇳 注意：`__abs__` 使用了 `math.hypot(x, y)` —— 这是 hypot 的正确用法（二维向量的欧几里得长度），与第2天中错误地用 hypot 代替海伦公式形成了对比。同一个函数，此处用对工具，彼处用错 —— 教训是*将公式与任务匹配*。

## RECALL answers
> 🇨🇳 回忆答案

**Spaced:** S1 it protects an invariant (value only changes through controlled methods); omit the
`@x.setter`. S2 `(Parrot, Bird, Animal, object)`. S3 `cos = a·b/(‖a‖‖b‖)`; removes magnitude so
it compares meaning/direction not length.
> 🇨🇳 **间隔记忆：** S1 保护不变量（值仅通过受控方法改变）；省略 `@x.setter`。S2 `(Parrot, Bird, Animal, object)`。S3 `cos = a·b/(‖a‖‖b‖)`；去除大小，比较的是含义/方向而非长度。

**A:** Python defines a *protocol* (special methods); syntax dispatches to it. One rule learned
once works on every type including yours → consistency, and your objects interoperate with
built-in functions and operators.
> 🇨🇳 **A:** Python 定义了*协议*（特殊方法）；语法会分派到这些方法。一条规则学习一次，适用于包括你自定义类型在内的所有类型 → 带来一致性，且你的对象能与内建函数和运算符互通。

**B** 1. `__repr__` always (REPL/debugger/containers); `__str__` falls back to `__repr__`, never
the reverse. 2. Defining `__eq__` sets `__hash__=None` (equal must hash equal; Python can't
verify). Immutable → add `__hash__`; mutable → leave unhashable. 3. Define `__iter__` (best a
generator) **or** define `__getitem__` and let Python index `0,1,2…` until `IndexError`.
4. So Python can try `other.__eq__(self)` (reflected) — maybe the other type knows how to
compare; `False` would lie. 5. A `yield`-function that *is* an iterator; Python writes
`__next__`/`StopIteration` for you → less code, fewer bugs.
> 🇨🇳 **B** 1. `__repr__` 永远优先（REPL/调试器/容器）；`__str__` 回退到 `__repr__`，反之不然。2. 定义 `__eq__` 会将 `__hash__` 设为 `None`（相等必须哈希相等；Python 无法验证）。不可变对象 → 添加 `__hash__`；可变对象 → 保持不可哈希。3. 定义 `__iter__`（最好用生成器）**或** 定义 `__getitem__`，让 Python 从 `0,1,2…` 索引直到 `IndexError`。4. 以便 Python 可以尝试 `other.__eq__(self)`（反射）—— 可能对方类型知道如何比较；直接返回 `False` 会说谎。5. 一个 `yield` 函数*就是*迭代器；Python 帮你写好了 `__next__`/`StopIteration` → 代码更少，bug 更少。

**C · Predict:** prints `3 3 True`. It **broke the golden rule** — `__add__` mutated `self` and
returned it, so `a` changed and `c is a`. `a + b` must return a *new* `V` and leave `a` alone.
> 🇨🇳 **C · 预测：** 打印 `3 3 True`。它**违反了黄金法则** —— `__add__` 修改了 `self` 并返回自身，因此 `a` 变了且 `c is a`。`a + b` 必须返回一个*新* `V`，而让 `a` 保持不变。

**D · Fraction:**
> 🇨🇳 **D · 分数类：**

```python
class Fraction:
    def __init__(self, num, den): self.num, self.den = num, den
    def __repr__(self): return f"Fraction({self.num}, {self.den})"
    def __eq__(self, o):
        if not isinstance(o, Fraction): return NotImplemented
        return self.num * o.den == o.num * self.den          # cross-multiply
    def __add__(self, o):
        return Fraction(self.num*o.den + o.num*self.den, self.den*o.den)   # new object
# Fraction(1,2) == Fraction(2,4)  → True ; Fraction(1,2)+Fraction(1,3) == Fraction(5,6) → True
```
> 🇨🇳 *通过交叉相乘实现分数相等判断和加法，返回新分数对象。*

**E · Math:** 1. `[[1,3,5],[2,4,6]]`, shape `2×3`. 2. `[1·10+2·20, 3·10+4·20] = [50, 110]`.
3. `[0·1+(-1)·0, 1·1+0·0] = [0, 1]` — `[1,0]` (pointing east) rotated 90° CCW to `[0,1]` (north). ✅
> 🇨🇳 **E · 数学：** 1. `[[1,3,5],[2,4,6]]`，形状 `2×3`。2. `[1·10+2·20, 3·10+4·20] = [50, 110]`。3. `[0·1+(-1)·0, 1·1+0·0] = [0, 1]` —— 表示 `[1,0]`（指向东）逆时针旋转 90° 变成 `[0,1]`（指向北）。✅

## Concept-check answers (homework)
> 🇨🇳 概念检查答案（作业）

1. `a + b` must not consume its operands (`5+3` doesn't change `5`); returning a new object keeps
   `a`,`b` reusable and matches every built-in numeric type.
> 🇨🇳 `a + b` 不得消耗其操作数（就像 `5+3` 不改变 `5`）；返回新对象保持 `a`,`b` 可重用，并与所有内建数值类型行为一致。

2. `x` then `y`; the generator function *ends* after the second `yield`, which raises
   `StopIteration` automatically.
> 🇨🇳 先 `x` 后 `y`；生成器函数在第二个 `yield` 之后*结束*，自动引发 `StopIteration`。

3. It prints `[<...Vector2D object at 0x...>]` — containers use `__repr__`, so a missing one
   makes debugging lists/log output useless.
> 🇨🇳 打印 `[<...Vector2D object at 0x...>]` —— 容器使用 `__repr__`，缺少它会让列表/日志输出在调试时毫无用处。

> 📝 Record: which dunder did you forget existed? That's a Day-4/6 re-test candidate.
> 🇨🇳 📝 记录：你忘了哪个双下划线方法的存在？那是第4/6天重测的候选内容。
