# 🔁 Day 2 — RECALL (retrieval practice + first spaced review)

> Blank mind, no scrolling. Do once after the lesson, then **cold tomorrow before Day 3**.
> Answers in [`SOLUTIONS.md`](./SOLUTIONS.md). Log blanks in [`../learning-records/`](../learning-records/).

## 🔁 Spaced — Day 1 (answer from memory, this is the interleaving)
S1. Instance vs class attribute — rule + one use of each.
S2. What single thing makes a property read-only?
S3. `[2,3] + 2·[1,-1]` = ?  *(if you blank, that's the signal — then check D1 SOLUTIONS)*

## A · Free recall
Explain `super()` to a beginner *without* saying "the parent class." (If you can't avoid that
phrase accurately, re-read the MRO section — that's the whole point of today.)

## B · Concept questions
1. **Extend vs replace** — what's the difference, and which is the safer default? Why?
2. What does an **ABC** guarantee, and *when* does it fail an incomplete subclass — at definition
   or at instantiation?
3. Why does defining `total_area` with polymorphism beat an `isinstance` ladder when a new shape
   is added?
4. Geometric meaning of `a·b = 0`? Of `a·b < 0`?
5. What is **cosine similarity**, and why is it (not the raw dot product) used to compare
   sentence embeddings?

## C · Predict the MRO (the E3 mastery rep)
```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...
class E(C): ...
class F(D, E): ...
```
Write `F.__mro__` **before** checking. (Hint: children before parents; left-to-right; each
ancestor appears once, after all paths to it.) Then *verify in a REPL*.

## D · Spot-the-bug
```python
class Parrot(Bird):
    def __init__(self, name):
        super(Bird, self).__init__(name, "Squawk")   # what's wrong?
```
Name the bug, say what it does to the MRO, and write the correct two lines.

## E · Micro-build (blank file, 8 min)
An ABC `PaymentMethod` with abstract `pay(amount)`; two concrete subclasses (`Cash`, `Card`);
a function `checkout(methods, amount)` that calls `.pay(amount)` on each **with no `isinstance`**.
Confirm `PaymentMethod()` raises `TypeError`.

## F · Math (by hand)
1. `[1,2,2] · [2,0,1]` = ?    2. `‖[6,8]‖` = ?    3. cosine similarity of `[1,0]` and `[1,1]` = ?

---
> ⏱️ Could you produce section C's MRO cold tomorrow? y/n → record it. Two spaced "yes" = edge
> **E3 graduates**.
