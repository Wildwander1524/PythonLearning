# 📘 Week 1 · Day 6 — Consolidate + Mini-Project

> **Date:** Sat 2026-06-21  ·  **Curriculum:** Review the week  ·  **Math:** Linear Algebra I recap

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | Review the week; self-quiz (below) |
| **S2** Core Theory B | 2 h | Mini-project build (see [`HOMEWORK.md`](./HOMEWORK.md)) |
| **S3** Math | 1 h | Week-1 math recap + practice problems (below) |
| **S4** Frontier | 2 h | Catch-up / re-read weak spots — finish PyTorch install + the vLLM notes if pending |
| **Homework** | 3 h | **Mini-project:** CLI contact book → [`HOMEWORK.md`](./HOMEWORK.md) |

> 🧭 **Saturday is for consolidation, not new material.** This is the most underrated day of the week. New input stops; you turn this week's fragile, freshly-learned pieces into durable, connected knowledge — and prove it by *building* something that uses all of them.

---

## 📑 Contents

1. [Why consolidation day matters (the learning science)](#why-consolidation-day-matters-the-learning-science)
2. [The week as one story](#the-week-as-one-story)
3. [S1 — Self-quiz](#s1--self-quiz)
4. [S3 — Math recap + practice](#s3--math-recap--practice-problems)
5. [S4 — Catch-up](#s4--catch-up)
6. [✅ End-of-Week-1 checklist](#-end-of-week-1-checklist)

---

## Why consolidation day matters (the learning science)

You might feel the urge to push ahead to new content. Resist it. Here's the evidence-based reason a review day produces more lasting skill than a sixth day of new material:

> 🌱 **Analogy — wet concrete needs to cure.** All week you've been *pouring* concrete (new concepts). Concrete that's poured but never allowed to cure stays weak and cracks under load. Consolidation day is the curing: no new pouring, just letting what you poured set into something that can bear weight. Skip it and next week's heavier load (NumPy on top of shaky OOP) cracks the foundation.

Three techniques to actually use today — each with the reason it works:

- **Active recall (the self-quiz below).** Don't *re-read* your notes — that creates a false "I recognize this, so I know it" feeling. Instead, *retrieve* the answer from a blank mind first, then check. 🏋️ *Analogy:* re-reading is watching someone else lift weights; recall is lifting them yourself. Only the second builds muscle. Retrieval is the single most effective study technique in the research literature.
- **The Feynman technique.** Explain each concept *out loud, in plain language, as if teaching a beginner.* The moment you stumble or reach for jargon to paper over a gap, you've found exactly what you don't truly understand. 🧒 *Analogy:* if you can't explain `super()` to a smart 12-year-old, you don't get it yet — you've only memorized the words.
- **Interleaving (the mini-project).** Instead of practicing one skill in isolation, the contact-book project *mixes* classes + exceptions + dataclasses + context managers + persistence in one task. 🥗 *Analogy:* a real meal mixes ingredients; you don't eat the flour, then the eggs, then the sugar separately. Interleaved practice is harder in the moment but produces knowledge you can actually *combine* under real conditions — which is the only kind that matters on the job.

---

## The week as one story

Before the quiz, see how the five days connect into a single arc — because isolated facts fade, but a *story* sticks:

> **You started (D1)** with a single class that did everything — a `BankAccount`. **(D2)** You learned to *share* behavior across related classes with inheritance, and to *guarantee* shared contracts with ABCs. **(D3)** You made your objects feel *native* — printable, comparable, addable, iterable — by implementing the data-model hooks. **(D4)** You learned *judgment*: that a pile of inheritance is often worse than assembling small parts (composition), and how to declare data cleanly (dataclasses) and safely (the mutable-default trap). **(D5)** You made code *survive failure* — exceptions for things going wrong, context managers for guaranteed cleanup, packages for organizing it all. **(D6, today)** You weld it all into one working program.

Notice the **math arc** running underneath in parallel: vectors (D2) → matrices and matrix×vector (D3) → matrix×matrix and inverses (D4) → linear combinations and span (D5). That's not a random grab-bag — it's the exact ladder you'll climb again in Week 8 when a "neural network layer" turns out to be `W·x + b`, and in Week 10 when "attention" turns out to be matrix products. **This week you quietly learned the alphabet of deep learning.**

---

## S1 — Self-quiz

Cover the answer key. For each question, **say your answer out loud first** (Feynman), *then* reveal and compare. If you can't answer cleanly, that topic is your re-read target for S4.

**OOP fundamentals (D1)**
1. Difference between an **instance attribute** and a **class attribute**? When is each right?
2. What does `@property` give you, and why prefer it to a plain attribute?
3. Why return a *copy* from a method like `history()`?

**Inheritance & polymorphism (D2)**
4. When inheritance vs composition? (the "is-a" / "has-a" test)
5. What does `super().__init__()` do, and what breaks if you forget it?
6. What is an **abstract base class**, and what happens if a subclass skips an `@abstractmethod`?
7. In multiple inheritance, what does `super()` actually point to — and what's the **MRO**?

**Data model (D3)**
8. `__str__` vs `__repr__` — who calls each, and which must you always define?
9. Two ways to make `for x in obj:` work?
10. What should `a + b` return — a mutated `a`, or a new object? Why?
11. You defined `__eq__` and now your object won't go in a `set`. Why, and how do you fix it?

**Design (D4)**
12. Why is `def f(items=[])` a bug? What exactly is shared, and what's the fix?
13. When is `@dataclass` the right tool? How do you give it a mutable default safely?
14. What does `__slots__` trade away, and when is it worth it?

**Errors & context (D5)**
15. Difference between `except`, `else`, and `finally`?
16. What does a **context manager** guarantee, and which two methods implement it?
17. What makes a folder a **package**, and what does `if __name__ == "__main__":` do?

<details>
<summary>💡 Answer key (open only after attempting all 17)</summary>

1. **Instance** = per-object state (`self.x`). **Class** = shared across all instances (`Class.count`). Shared constants/counters → class; per-object data → instance.
2. `@property` exposes a method as a read-only/controlled attribute — encapsulation and validation *without* changing how callers access it (`obj.balance`, not `obj.get_balance()`).
3. So external code can't mutate your internal list and silently corrupt the object's state.
4. Inheritance for genuine **is-a** subtypes (and ABCs/framework bases); composition for **has-a** and assembling behavior. Default to composition — looser coupling, survives change.
5. Runs the parent's initializer so inherited attributes get set; skip it and those attributes never exist → `AttributeError` later. A subclass `__init__` should almost always call it.
6. A class that can't be instantiated and *forces* subclasses to implement its `@abstractmethod`s; a subclass that skips one **can't be instantiated** (`TypeError`) — failing early and loudly.
7. `super()` points to **the next class in the MRO**, which in multiple inheritance may be a *sibling*, not a parent. The **MRO** is the fixed left-to-right, deduplicated ancestor search order (`Class.__mro__`), computed by C3 linearization.
8. `__repr__` → developer/REPL/debuggers/containers (**always define**); `__str__` → `print`/users (define when it differs). `__str__` falls back to `__repr__`, not vice-versa.
9. Define `__iter__` (best as a generator with `yield`), **or** define `__getitem__` and let Python's old iteration protocol index `0,1,2,…` until `IndexError`.
10. A **new** object — operators must not mutate their operands (`5 + 3` doesn't change `5`).
11. Defining `__eq__` sets `__hash__ = None` (equal objects must hash equal; Python can't verify your logic, so it disables hashing). Fix: if the object is immutable, define `__hash__` too; if mutable, leave it unhashable (correct).
12. The default list is created **once at `def` time** and shared across all calls, so it accumulates. Fix: default to `None`, create a fresh list inside.
13. For data-holding classes — it auto-writes `__init__`/`__repr__`/`__eq__`. Mutable default → `field(default_factory=list)`, never `= []`.
14. It trades away dynamic attributes (no per-instance `__dict__`, can't add new attrs) for lower memory and slightly faster access. Worth it only with very many instances and a profiler's say-so.
15. `except` handles a raised error; `else` runs only if the `try` raised nothing; `finally` always runs (cleanup, every path).
16. Guaranteed setup *and* teardown even on error; `__enter__` and `__exit__`.
17. An `__init__.py` file inside it makes it a package. `if __name__ == "__main__":` runs a block only when the file is executed directly, not when imported.
</details>

> 🎯 **Scoring honestly:** 15–17 clean = solid, proceed. 10–14 = re-do the weak days' homework from a blank file in S4. Below 10 = spend Saturday re-reading, and tell me — we'll adjust Week 2's pace rather than build on sand.

---

## S3 — Math recap + practice problems

**Week-1 toolkit:** vectors (add, scalar-multiply), dot product, norm/length, distance, cosine similarity, matrices (transpose, matrix×vector, matrix×matrix, identity, inverse intuition), linear combinations & span.

> 🪢 **See the thread:** every one of these reappears in deep learning. Dot product → attention scores. Matrix×vector → a network layer. Span/independence → PCA. Norm → loss functions and regularization. You're not reviewing trivia; you're rehearsing the operations you'll run thousands of times.

Solve by hand, then verify in Python/NumPy if unsure.

```text
 1. [2, 3] + [4, 1] = ?
 2. 3 · [1, -2] = ?
 3. [1, 2, 2] · [2, 0, 1] = ?              (dot product)
 4. ‖[6, 8]‖ = ?                           (norm)
 5. distance between [1, 1] and [4, 5] = ?
 6. cosine similarity of [1, 0] and [1, 1] = ?
 7. transpose of [[1, 2], [3, 4], [5, 6]] → entries? shape?
 8. [[1, 2], [3, 4]] · [10, 20] = ?        (matrix × vector)
 9. [[2, 0], [1, 3]] · [[1, 4], [0, 5]] = ?   (matrix × matrix — check the domino rule first)
10. Write [7, -2] as a linear combination of [1, 0] and [0, 1].
11. Are [1, 2] and [2, 4] linearly independent? What is their span?
12. Multiply [[1,2],[3,4]] by the identity [[1,0],[0,1]] — predict before computing.
```

<details>
<summary>💡 Answers</summary>

1. `[6, 4]`
2. `[3, -6]`
3. `2 + 0 + 2 = 4`
4. `sqrt(36+64) = sqrt(100) = 10`
5. `sqrt(3² + 4²) = sqrt(25) = 5`
6. `1 / (1 · sqrt(2)) = 1/√2 ≈ 0.707`
7. `[[1,3,5],[2,4,6]]`, shape `2×3`
8. `[1·10+2·20, 3·10+4·20] = [50, 110]`
9. `[[2,8],[1,19]]` (inner dims `2=2` ✅ → result `2×2`)
10. `7·[1,0] + (-2)·[0,1]`
11. **Dependent** (`[2,4] = 2·[1,2]`); span = just the line through `[1,2]`, *not* the plane.
12. Unchanged: `[[1,2],[3,4]]` — that's what "identity" means.
</details>

---

## S4 — Catch-up

Use this slot to **close gaps**, not start new things:
- [ ] PyTorch installed and importing? (`python -c "import torch; print(torch.__version__)"`)
- [ ] Wrote the 3-sentence PagedAttention note from D4? (KV-cache → paging → more users)
- [ ] Re-read whichever day scored weakest on the quiz. If a topic didn't click, **re-do that day's homework from a blank file** — reproduction-from-scratch is the ultimate test of understanding.
- [ ] Re-skim the Digest #1 reflection; keep your career direction in view as you build the capstone.

> 🔁 **The blank-file test.** Recognizing code you wrote is easy; *reproducing* it from nothing is the real benchmark. If you can rebuild Day 3's `Vector2D` on an empty file without peeking, you own it. If you can't, that's not failure — that's the exact gap consolidation day exists to find and fill.

---

## ✅ End-of-Week-1 checklist

- [ ] D1 BankAccount — fixed to 10/10
- [ ] D2 inheritance + ABC — pushed
- [ ] D3 Vector2D — pushed
- [ ] D4 composed Bank/Account/Ledger — pushed
- [ ] D5 logger package — pushed
- [ ] D6 mini-project (contact book) — pushed
- [ ] Self-quiz: all 17 answered confidently (Feynman-style, out loud)
- [ ] Math: all 12 problems correct
- [ ] PyTorch installed; frontier notes written

When this is all ticked, tell me **"Week 1 done"** and I'll mark Week 1 ✅ in the plan, write the Week-1 retro (what was strong, what to reinforce), and prep **Week 2 (NumPy)** — where today's by-hand vector and matrix math becomes one-line vectorized code, and you'll *feel* why the math came first.

➡️ **Build the capstone:** [`HOMEWORK.md`](./HOMEWORK.md)
