# ✅ Day 2 — SOLUTIONS / 第二天解答

> Open only after attempting [`HOMEWORK.md`](./HOMEWORK.md) + [`RECALL.md`](./RECALL.md).
> 🇨🇳 仅在尝试过 [`HOMEWORK.md`](./HOMEWORK.md) 和 [`RECALL.md`](./RECALL.md) 后再打开。

## Reference — `animals.py` (key parts) / 参考 —— `animals.py`（关键部分）
```python
class Animal:
    def __init__(self, name, sound):
        self.name, self.sound = name, sound
    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name): super().__init__(name, "Woof")
    def fetch(self, item):                       # E1: USE the parameter
        return f"{self.name} fetches the {item}!"

class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)                   # E3 FIX: runs Bird.__init__ → Animal.__init__
        self.sound = "Squawk"                    # override AFTER the chain
        self._learned = ""
    def speak(self):                             # EXTEND, guarded
        base = f"{self.name} says {self.sound}"
        return f"{base} — {self._learned}!" if self._learned else base

# Parrot.__mro__ == (Parrot, Bird, Animal, object)
```
> 🇨🇳 动物类层次结构的关键代码：基类 `Animal`，子类 `Dog`，以及通过 `Bird` 多重继承的 `Parrot`，展示了 `super()` 链和 `speak` 方法的扩展。

## Reference — `shapes.py` (key parts) / 参考 —— `shapes.py`（关键部分）
```python
import math
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2          # NO /2
class Triangle(Shape):
    def area(self):                                        # Heron — NOT math.hypot
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
def total_area(shapes):
    return sum(s.area() for s in shapes)                  # zero isinstance
```
> 🇨🇳 形状类层次结构的关键代码：`Circle`（圆）和 `Triangle`（三角形）的面积计算实现，以及多态函数 `total_area`。

**Heron sanity check (E2):** 3-4-5 → `s=6`, `area=√(6·3·2·1)=√36=6.0`. ✅ (`math.hypot(...)≈3.74` — clearly wrong; the sanity number catches it.)
> 🇨🇳 海伦公式合理性检查（E2）：3-4-5 三角形，`s=6`，面积 = √(6·3·2·1) = √36 = 6.0。✅（`math.hypot(...)≈3.74` 明显错误；通过合理性检查数字可以发现。）

## RECALL answers / 回顾答案
**Spaced (D1):** S1 instance = per-object (`self.x`), class = shared (`Cls.x`). S2 no `@x.setter`. S3 `[4,1]`.
> 🇨🇳 间隔复习（D1）：S1 实例变量是每个对象独立的（`self.x`），类变量是共享的（`Cls.x`）。S2 没有 `@x.setter`。S3 结果为 `[4,1]`。

**A — super() without "parent":** `super()` returns a proxy that delegates to **the next class in `self`'s MRO** after the current one.
> 🇨🇳 A — 没有“父类”的 super()：`super()` 返回一个代理，该代理将调用委托给**当前类之后、`self` 的 MRO（方法解析顺序）中的下一个类**。

**B** 1. Extend = `super().method()` + additions; replace = fresh logic; extend is safer (keeps parent's guarantees). 2. Forces every `@abstractmethod`; fails at **instantiation** (`TypeError`). 3. The polymorphic version never changes when you add `Pentagon`; the ladder needs a new `elif` in tested code. 4. `a·b=0` ⇒ orthogonal; `a·b<0` ⇒ opposite. 5. `cos = a·b/(‖a‖‖b‖)`; removes magnitude so it compares direction/meaning not length.
> 🇨🇳 **B**
> 1. 扩展（extend）是在 `super().method()` 基础上增加额外逻辑；替换（replace）则是全新的实现；扩展更安全（因为它保留了父类的保证）。
> 2. 强制每个 `@abstractmethod` 都必须实现；会在**实例化**时失败（抛出 `TypeError`）。
> 3. 多态版本在添加 `Pentagon` 时无需任何改动；阶梯式代码则需要在已测试的代码中添加新的 `elif`。
> 4. `a·b=0` ⇒ 正交；`a·b<0` ⇒ 方向相反。
> 5. `cos = a·b/(‖a‖‖b‖)`；移除了量级的影响，因此比较的是方向/语义，而非长度。

**C — `F.__mro__`:** `(F, D, B, E, C, A, object)`. Verify in a REPL.
> 🇨🇳 C — `F.__mro__`：`(F, D, B, E, C, A, object)`。可以在 REPL 中验证。

**D — spot-the-bug:** `super(Bird, self)` starts the search **after** `Bird`, skipping `Bird.__init__`. Fix: `super().__init__(name)` then `self.sound = "Squawk"`.
> 🇨🇳 D — 找错误：`super(Bird, self)` 从 `Bird` **之后**开始搜索，跳过了 `Bird.__init__`。修复方法：使用 `super().__init__(name)` 然后设置 `self.sound = "Squawk"`。

**E — micro-build:**
```python
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): ...
class Cash(PaymentMethod):
    def pay(self, amount): return f"paid {amount} in cash"
def checkout(methods, amount):
    return [m.pay(amount) for m in methods]      # no isinstance
# PaymentMethod() → TypeError ✅
```
> 🇨🇳 微构建示例：定义抽象基类 `PaymentMethod` 及其具体子类 `Cash`，实现 `checkout` 函数的多态，无需 `isinstance` 检查。实例化 `PaymentMethod` 将引发 `TypeError`。

**F — math:** 1. `4`  2. `10`  3. `1/√2≈0.707`.
> 🇨🇳 F — 数学：1. 点积为 `4`。 2. 范数为 `10`。 3. 余弦相似度为 `1/√2`（约 0.707）。

## Concept-check answers (homework) / 概念检查答案（作业）
1. `super(Bird, self)` resolves to the MRO entry **after** `Bird` (i.e. `Animal`), skipping `Bird.__init__`; it only worked because `Animal` still set `sound`.
   > 🇨🇳 `super(Bird, self)` 会解析到 MRO 中 `Bird` **之后**的条目（即 `Animal`），跳过了 `Bird.__init__`；它之所以能工作，只是因为 `Animal` 仍然设置了 `sound` 属性。
2. `Bird` is nearer in the chain; MRO is children-before-parents, left-to-right.
   > 🇨🇳 因为 `Bird` 在继承链中更近；MRO（方法解析顺序）的顺序是子类先于父类，从左到右。
3. See B3.
   > 🇨🇳 见 B 部分第 3 项。
