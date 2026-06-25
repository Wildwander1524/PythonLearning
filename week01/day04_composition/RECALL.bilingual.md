# 🔁 Day 4 — RECALL (retrieval + spaced review)
> 🇨🇳 **[第4天 — 回忆（检索 + 间隔复习）]**

> Blank mind. Once after the lesson, again cold before Day 5. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).
> 🇨🇳 放空大脑。刚刚讲完课后的第一次，第5天之前不看笔记的第二次。答案见：[`SOLUTIONS.md`](./SOLUTIONS.md)。

## 🔁 Spaced — D2 & D3 (from memory)
> 🇨🇳 **[间隔回忆 — D2 与 D3（凭记忆）]**

S1 (D2) what does an **ABC** guarantee, and *when* does it reject an incomplete subclass?
> 🇨🇳 S1 (D2) **ABC** 保证什么？以及 *何时* 它会拒绝一个未完全实现的子类？

S2 (D3) you defined `__eq__`; why is the object now unhashable, and what are the two fixes?
> 🇨🇳 S2 (D3) 你定义了 `__eq__`；为什么对象现在不可哈希？两种修复方法是什么？

S3 (D3) golden rule — what must `a + b` return, and why?
> 🇨🇳 S3 (D3) 黄金法则 —— `a + b` 必须返回什么？为什么？

## A · Free recall
> 🇨🇳 **[自由回忆]**

State "prefer composition over inheritance" and the **fragile base class** problem to a beginner,
with one analogy. When *is* inheritance still the right call?
> 🇨🇳 向初学者解释"优先使用组合而非继承"以及 **脆弱的基类** 问题，并给出一个类比。什么情况下继承仍然是正确的选择？

## B · Concept questions
> 🇨🇳 **[概念问题]**

1. The is-a / has-a test: classify each — `SavingsAccount`/`BankAccount`; `Car`/`Engine`;
   `LogLevelError`/`LogError`; `Stack`/`list`.
> 🇨🇳 1. is-a / has-a 测试：对下列每一对进行分类 —— `SavingsAccount`/`BankAccount`；`Car`/`Engine`；`LogLevelError`/`LogError`；`Stack`/`list`。

2. Why does inheriting `Stack(list)` break the abstraction? What does composing a list fix?
> 🇨🇳 2. 为什么继承 `Stack(list)` 会破坏抽象？用组合一个列表解决了什么问题？

3. Why is `def f(x=[])` a bug — what *exactly* is shared, and when is the list created?
> 🇨🇳 3. 为什么 `def f(x=[])` 是一个 bug —— 到底 *什么* 被共享了？列表在何时创建？

4. How do you give a `@dataclass` a mutable default safely, and why not `= []`?
> 🇨🇳 4. 如何安全地为 `@dataclass` 提供可变默认值？为什么不能用 `= []`？

5. What does `__slots__` trade away, and when is it actually worth it?
> 🇨🇳 5. `__slots__` 牺牲了什么？在什么时候真正值得使用？

## C · Spot-the-bug
> 🇨🇳 **[找 bug]**

```python
@dataclass
class Cart:
    items: list = []          # what's wrong, and what happens with two Carts?
```
> 🇨🇳 *该代码定义了一个数据类，但 items 的默认值使用了可变的空列表，导致所有 Cart 实例共享同一个列表对象。*

Fix it, and explain what two separate `Cart()` instances would otherwise share.
> 🇨🇳 修复它，并解释两个独立的 `Cart()` 实例原本会共享什么。

## D · Micro-build (blank file, 10 min)
> 🇨🇳 **[微型构建（空白文件，10 分钟）]**

Model a `Playlist` that **has-a** list of `Song` (`@dataclass`: `title`, `artist`). `Playlist`
exposes only `add(song)`, `__len__`, and `__iter__` (compose, don't inherit `list`). Then say in
one sentence why you didn't write `class Playlist(list)`.
> 🇨🇳 设计一个 `Playlist` 类，它 **包含（has-a）** 一个 `Song` 对象的列表（`@dataclass`，字段：`title`，`artist`）。`Playlist` 只暴露 `add(song)`、`__len__` 和 `__iter__` 方法（使用组合，不要继承 `list`）。然后用一句话说明为什么不写 `class Playlist(list)`。

## E · Math (by hand)
> 🇨🇳 **[数学（手算）]**

1. `[[2,0],[1,3]] · [[1,4],[0,5]]` = ? (check the domino rule first; result shape?)
> 🇨🇳 1. `[[2,0],[1,3]] · [[1,4],[0,5]]` = ? （先检查多米诺规则；结果形状？）

2. `[[1,2],[3,4]] · [[1,0],[0,1]]` = ? (predict before computing)
> 🇨🇳 2. `[[1,2],[3,4]] · [[1,0],[0,1]]` = ? （计算前先预测）

3. `A=[[1,1],[0,1]]`, `B=[[1,0],[1,1]]`: is `A·B == B·A`? Compute both.
> 🇨🇳 3. `A=[[1,1],[0,1]]`，`B=[[1,0],[1,1]]`：`A·B == B·A` 吗？请计算两者。

---
> ⏱️ Could you classify section B1 cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
> 🇨🇳 明天你能不看笔记完成 B1 的分类题吗？ y/n → [`../learning-records/`](../learning-records/)。


""""""
"""
## Spaced Answer:
S1. ABC guarantee there's no incomplete subclass,it will reject when the subclass instance
S2. Because the hash became None when you defined __eq__ ,For immutable objects,you best to define __hash__;
For mutable object,you best to accept __hash__ = None,and can't put your object into set or dict
S3. it must return a new object,the same reason for hash changed,and the bad bad thing appear: the same hash value but not equal


## A · Free recall Answer:
the inheritance just like building a tower,the rest of them must all change when you change the fundmental;
the composition just like LEGO or composite a bot,its easier to replace one part or test it


## B · Concept questions Answer:
1. SavingsAccount is a BankAccount; Car has an Engine; LogLevelError is a LogError; Stack has a list
2. Stack(list) let the enclosing method or state exposed to the inheritor,but composing won't
3. because local var is created before the init start,then every instance object point to a common list which the x point.
When an instance object mutate the list,then the list of every other instance object from method f will change together
4. why not =[],the same reason for Q3,the right way is x: list = field(default_factory = list)
5. slots trades flexable to running speed for fixed states,its worth it when the data is very big.


## C · Spot-the-bug Answer:
the two seperate Cart() instances would share the same items list,it should be
@dataclass
class Cart:
    items: list = field(default_factory = list)


## E · Math (by hand) Answer:
1. the shape is [[2,8],[1,12]]
2. A X identity = A,so the answer is [[1,2],[3,4]] 
3. they are not equal,A·B = [[2,1],[1,1]]  B·A = [[1,2],[1,2]]


"""

## D · Micro-build (blank file, 10 min)
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Song:
    title: str
    artist: str


class Playlist:

    def __init__(self):
        self.lst: list[Song] = []

    def __iter__(self):
        for i in self.lst:
            yield i

    def add(self, title: str, artist: str) -> None:
        self.lst.append(Song(title, artist))

    def __len__(self):
        return len(self.lst)

###  Why not class Playlist(list)?  I just know it seems symple to use compose here.
