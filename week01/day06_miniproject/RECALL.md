# 🔁 Day 6 — RECALL (cumulative whole-week retrieval test)

> This is the week's big interleaved quiz — every day, mixed. **Say each answer out loud
> (Feynman) before checking.** Cover the answers in [`SOLUTIONS.md`](./SOLUTIONS.md). Your score
> is a *diagnostic*: it tells you which day to rebuild from a blank file in the catch-up slot.

## Part 1 · Concepts (17)

**OOP fundamentals (D1)**
1. Instance vs class attribute — difference, and when each is right?
2. What does `@property` give you, and why prefer it to a plain attribute?
3. Why return a *copy* from a method like `history()`?

**Inheritance, polymorphism, ABC, MRO (D2)**
4. Inheritance vs composition — the one-sentence test?
5. What does `super().__init__()` do, and what breaks if you forget it?
6. What is an ABC, and what happens if a subclass skips an `@abstractmethod`?
7. In multiple inheritance, what does `super()` actually point to — and what is the **MRO**?
   *(Bonus: give `D.__mro__` for `class D(B, C)`, `B(A)`, `C(A)`.)*

**Data model (D3)**
8. `__str__` vs `__repr__` — who calls each, which must you always define?
9. Two ways to make `for x in obj:` work?
10. What should `a + b` return — a mutated `a` or a new object? Why?
11. You defined `__eq__` and now your object won't go in a `set`. Why, and how do you fix it?

**Design (D4)**
12. Why is `def f(items=[])` a bug — what's shared, and what's the fix?
13. When is `@dataclass` right, and how do you give it a mutable default safely?
14. What does `__slots__` trade away, and when is it worth it?

**Errors & context (D5)**
15. Difference between `except`, `else`, and `finally`?
16. What does a context manager guarantee, and which two methods implement it?
17. What makes a folder a package, and what does `if __name__ == "__main__":` do?

> 🎯 **Score honestly:** 15–17 clean → proceed. 10–14 → rebuild the weak days' homework from a
> blank file in catch-up. <10 → spend today re-reading and tell me; we'll re-pace Week 2 rather
> than build on sand.

## Part 2 · Math (12 — by hand, then verify)
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

## Part 3 · The blank-file test (the real benchmark)
Without looking at any file, rebuild **one** of: D3 `Vector2D` *or* D5 `FileLogger`. Recognizing
your old code is easy; *reproducing* it from nothing is mastery. Whatever you can't reproduce is
precisely today's re-study target.

---
> 📝 Final record for the week: in [`../learning-records/`](../learning-records/), note your quiz
> score, which day you rebuilt blind, and whether edges **E1–E4** (see
> [`../MISSION.md`](../MISSION.md)) each got retrieved after a gap. That closes the loop.
