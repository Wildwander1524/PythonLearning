# 🔁 Day 3 — RECALL (retrieval + spaced review)

> Blank mind. Once after the lesson, again cold before Day 4. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).

## 🔁 Spaced — D1 & D2 (from memory)
S1 (D1) what does a read-only `@property` protect, and how do you make one?
S2 (D2) **predict** `Parrot.__mro__` for `Parrot(Bird)`, `Bird(Animal)`. (E3 — must be cold.)
S3 (D2) cosine similarity formula, and why it's used over the raw dot product for embeddings.

## A · Free recall
In your own words: *why is built-in syntax like `len(x)` and `a + b` "just" method calls?* What
does that buy Python (and you)?

## B · Concept questions
1. Which of `__repr__`/`__str__` must you **always** define, and why? Which falls back to which?
2. You define `__eq__`; now `set()` of your objects raises `TypeError`. Explain the rule and both
   fixes (immutable vs mutable).
3. Two distinct ways to make `for x in obj:` work.
4. Why return `NotImplemented` (not `False`) from `__eq__` for an unknown type?
5. What is a **generator**, and why prefer it to hand-writing `__next__`?

## C · Predict the output
```python
class V:
    def __init__(self, x): self.x = x
    def __add__(self, o): self.x += o.x; return self     # ⚠️ note this
a = V(1); b = V(2)
c = a + b
print(a.x, c.x, a is c)
```
What prints — and what *rule* did this code break?

## D · Micro-build (blank file, 8 min)
A `Fraction(num, den)`: `__repr__` → `'Fraction(1, 2)'`; `__eq__` by cross-multiplication
(`1/2 == 2/4`); `__add__` returning a **new** `Fraction` (`a/b + c/d = (ad+bc)/bd`). No
simplification needed.

## E · Math (by hand)
1. Transpose of `[[1,2],[3,4],[5,6]]` — entries and shape?
2. `[[1,2],[3,4]] · [10, 20]` (matrix×vector) = ?
3. `[[0,-1],[1,0]] · [1,0]` = ? (this matrix rotates 90° — do you see it?)

---
> ⏱️ Could you do section D cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
