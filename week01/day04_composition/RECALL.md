# 🔁 Day 4 — RECALL (retrieval + spaced review)

> Blank mind. Once after the lesson, again cold before Day 5. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).

## 🔁 Spaced — D2 & D3 (from memory)
S1 (D2) what does an **ABC** guarantee, and *when* does it reject an incomplete subclass?
S2 (D3) you defined `__eq__`; why is the object now unhashable, and what are the two fixes?
S3 (D3) golden rule — what must `a + b` return, and why?

## A · Free recall
State "prefer composition over inheritance" and the **fragile base class** problem to a beginner,
with one analogy. When *is* inheritance still the right call?

## B · Concept questions
1. The is-a / has-a test: classify each — `SavingsAccount`/`BankAccount`; `Car`/`Engine`;
   `LogLevelError`/`LogError`; `Stack`/`list`.
2. Why does inheriting `Stack(list)` break the abstraction? What does composing a list fix?
3. Why is `def f(x=[])` a bug — what *exactly* is shared, and when is the list created?
4. How do you give a `@dataclass` a mutable default safely, and why not `= []`?
5. What does `__slots__` trade away, and when is it actually worth it?

## C · Spot-the-bug
```python
@dataclass
class Cart:
    items: list = []          # what's wrong, and what happens with two Carts?
```
Fix it, and explain what two separate `Cart()` instances would otherwise share.

## D · Micro-build (blank file, 10 min)
Model a `Playlist` that **has-a** list of `Song` (`@dataclass`: `title`, `artist`). `Playlist`
exposes only `add(song)`, `__len__`, and `__iter__` (compose, don't inherit `list`). Then say in
one sentence why you didn't write `class Playlist(list)`.

## E · Math (by hand)
1. `[[2,0],[1,3]] · [[1,4],[0,5]]` = ? (check the domino rule first; result shape?)
2. `[[1,2],[3,4]] · [[1,0],[0,1]]` = ? (predict before computing)
3. `A=[[1,1],[0,1]]`, `B=[[1,0],[1,1]]`: is `A·B == B·A`? Compute both.

---
> ⏱️ Could you classify section B1 cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
