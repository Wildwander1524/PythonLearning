# 🎯 Week 1 — MISSION

> **Curriculum:** Object-Oriented Python (deep) + Linear Algebra I + Orientation
> **Dates:** Mon 2026-06-16 → Sat 2026-06-21 · **Cadence:** 7 h theory + 3 h homework / day
> **This file is the control panel for the week.** Read it first on Day 1, and re-read the
> *Spaced-Review Map* every morning. It is updated as your `learning-records/` accumulate.

This workspace follows the **`/teach` method**: a lesson is not "done" when you've *read*
it — it's done when you can *retrieve* it cold a few days later and *use* it under a slightly
harder problem. That distinction (psychologists call it **fluency vs. storage strength**) is
the spine of everything here. See [`RESOURCES.md`](./RESOURCES.md) §Pedagogy for the science.

---

## 1 · The promise (what you'll own by Saturday night)

By the end of Week 1 you can:

1. **Design** a small class system and *justify* every choice — when to use a plain class,
   inheritance, an ABC, composition, or a `@dataclass` — and defend it against the
   alternative.
2. **Make your objects feel native**: print, compare, add, index, and iterate over them via
   the Python **data model** (dunder methods) — the exact mechanism NumPy/PyTorch are built on.
3. **Fail early and loudly**: exceptions, custom exception hierarchies, context managers,
   and the discipline of *never leaving a red test*.
4. **Read and reason about linear algebra**: vectors, dot product (algebraic *and* geometric),
   norms, matrices, matrix×vector and matrix×matrix, identity/inverse — and connect each to
   its role in a neural network.
5. **Hold an informed mental model** of LLMs and your three career directions, anchored by
   one primary source you can paraphrase (Karpathy; PagedAttention/vLLM).

**Capstone proof (Day 6):** a CLI contact book — OOP design, JSON persistence, a custom
exception hierarchy, dunder methods, full tests — shipped to GitHub. If you can build it
*without re-reading the week*, the week is yours.

---

## 2 · Your ability boundary (calibrated from Day 1–2 — updated as you go)

> The `/teach` method targets the **edge** of what you can already do — not the middle (too
> easy, no learning) and not far past it (frustration). This is that edge, inferred from your
> *actual* submitted code, not a guess. It tunes the homework difficulty.

**What you already do well (don't re-teach — reinforce only):**
- ✅ Class structure, `__init__`, `self`, instance vs. class attributes (D1: `account_count`
  via `BankAccount.account_count` — the *correct* pattern, not `self.`).
- ✅ Encapsulation: private `_balance` + read-only `@property` with **no setter**.
- ✅ Input validation that raises `ValueError`; triangle-inequality guard (a nice instinct).
- ✅ `super()` in every subclass; the **EXTEND** override flavor; ABCs + polymorphism with
  **zero `isinstance` ladders** (`total_area`).
- ✅ Reaching for stretch goals unprompted (`SwimMixin`, `Square(Rectangle)`, `Penguin`).

**Your live growth edges (this week deliberately pushes on these):**
| # | Edge (evidence) | How the week targets it |
|---|-----------------|--------------------------|
| E1 | **Spec precision** — `Dog.fetch` ignored its `item` arg (test failed). | Homework specs are exact and tested; RECALL asks you to *re-read the spec* before coding. |
| E2 | **Domain/formula correctness** — `math.hypot` for Heron's; `πr²/2` semicircle. | "Derive-then-code" steps; a units/formula sanity-check ritual; these resurface in spaced review. |
| E3 | **Inheritance subtlety** — `super(Bird, self)` *skipped* `Bird` in the MRO (worked by luck). | D2/D3/D4 interleave an MRO-tracing drill until you predict `__mro__` cold. |
| E4 | **Pythonic polish & test hygiene** — tuple-grown history (O(n²)); dead `pass`; a *tested-but-unimplemented* `transfer` left red. | A "definition of done" gate every day: green tests, no dead code, no O(n²) where O(n) is trivial. |

> 🔁 **This table is a living instrument.** When a `learning-records/` entry shows an edge is
> closed (e.g., you predict an MRO correctly twice, spaced a few days apart), it graduates out
> and a new edge takes its place.

---

## 3 · Daily objectives (Bloom-tagged) & mastery bar

Each objective is tagged by cognitive level — *Remember → Understand → Apply → Analyze →
Create* — so you know whether the bar is "recall it," "explain it," or "build with it."
**Mastery = you meet the bar from memory, on a problem you haven't seen, after a day's gap.**

| Day | Objectives (level) | Mastery bar (how you prove it) |
|-----|--------------------|--------------------------------|
| **D1** Classes & encapsulation | Define classes/`__init__`/`self` *(Apply)*; distinguish instance vs class attrs *(Understand)*; enforce invariants via properties *(Apply)* | Build a class with a read-only invariant nobody can corrupt; explain *why* `self.x += 1` on a class counter is a bug. |
| **D2** Inheritance · polymorphism · ABC | Use `super()`/overriding *(Apply)*; **predict an MRO** *(Analyze)*; design an ABC contract *(Create)* | Trace `__mro__` of a 3-level + multiple-inheritance class **cold**; build an ABC that rejects an incomplete subclass at instantiation. |
| **D3** Dunder & the data model | Implement `__repr__/__eq__/__add__/__iter__` *(Apply)*; explain *why* syntax → dunder *(Understand)* | Write a class that prints, `==`-compares, `+`-adds, indexes, and `for`-iterates — and say which dunder each one fires. |
| **D4** Composition & design | Choose composition vs inheritance *(Analyze)*; use `@dataclass` correctly *(Apply)* | Refactor D1 into composed parts and *defend* each "has-a"; spot the mutable-default bug unprompted. |
| **D5** Errors · context · modules | Build a custom exception hierarchy *(Create)*; write a context manager *(Apply)* | A `with`-managed resource that releases on exception; a 3-level exception tree a caller can catch by category. |
| **D6** Mini-project (capstone) | Integrate the week *(Create)* | Ship the CLI contact book with tests, persistence, custom exceptions — **without re-reading the week**. |

---

## 4 · The Spaced-Review Map (interleaving — the part most courses skip)

> Cramming one topic per day produces *fluency that evaporates*. The fix is **interleaving**:
> every day re-tests earlier days, with the gap deliberately growing. Each day's `RECALL.md`
> opens with these callbacks **before** any new material. Do them from memory — struggling to
> retrieve *is* the learning (Bjork's "desirable difficulty").

| On Day | Re-test (spaced, from memory) | Why this item (ties to your edges) |
|--------|-------------------------------|-------------------------------------|
| D2 | D1: class vs instance attribute; the read-only-property invariant | foundation for subclass init |
| D3 | D1: encapsulation · D2: **MRO of a 3-level class** + EXTEND vs REPLACE | E3 (MRO), E1 (override precision) |
| D4 | D2: ABC contract · D3: `__eq__`/`__hash__` pairing | feeds "compose vs inherit" judgment |
| D5 | D1: validation/`ValueError` · D3: data model · D4: mutable-default trap | E4 (hygiene), E2 (correctness) |
| D6 | **Everything** — the capstone is the cumulative retrieval test | whole-week storage strength |
| Math | each math hour reuses the prior: dot product → matrix×vector → matrix×matrix | builds the NN forward-pass atom by atom |

---

## 5 · How to use this workspace each day

```
day0X_topic/
  LESSON.md      ← read actively: stop at every  ✍️ Self-explain  and  🔮 Predict  prompt
  RECALL.md      ← do FIRST thing next morning (spaced) AND after the lesson (fresh)
  HOMEWORK.md    ← the 3-h build; specs are exact and tested
  SOLUTIONS.md   ← open ONLY after a genuine attempt (peeking early kills the effect)
  *.py           ← your code (+ the provided test file)
  REVIEW.md      ← I write this when you submit: what's right, what to fix, pace
```

**The loop that actually builds memory (do this, not passive reading):**
1. **Morning** — open today's `RECALL.md`, do the *spaced* callbacks cold (no notes). Note what you blanked on.
2. **Lesson** — read `LESSON.md`; at each ✍️/🔮 prompt, *write/predict before reading on*.
3. **Build** — `HOMEWORK.md`. Re-read the spec twice before coding (edge E1).
4. **Self-check** — run tests; meet the *Definition of Done*; only then open `SOLUTIONS.md`.
5. **Record** — add 3 lines to `learning-records/<date>.md`: what was easy / what was hard /
   what to re-test. *This is what lets the next session pick up exactly where you are.*

> ⏱️ **Fluency ≠ mastery.** Finishing the lesson the same day is *fluency*. The real test is
> the next-morning `RECALL.md` cold. Treat a blank there not as failure but as the system
> doing its job — that's the gap retrieval practice exists to close.

---

## 5b · Lesson format — the video-teacher and the textbook (updated 2026-06-27)

Each day is built **interactive-HTML-first**. Think of `LESSON.interactive.html` as **a teacher
explaining by video**: it's where you go *deeper* and understand *faster*, so it's authored first
and is the primary lesson. `LESSON.bilingual.md` is **the textbook** beside the lecture — a reference
to consult, authored second. (This reverses the old "markdown first, HTML-after-recall" order.)

Because the interactive lesson now leads, it can't be something you only *watch* — passive watching
feels like learning but skips the retrieval that builds memory. So the HTML **embeds the feedback loop
itself**: *predict-before-reveal* prompts (you commit an answer before it's shown) and at least one
*quiz with instant feedback*. The cold, spaced re-tests still live **outside** the lesson — in
`RECALL.md` and `review-queue.md` — done from memory the next morning.

Every concept is taught to a **density floor**: three escalating depth passes (intuition → mechanism →
edge cases) and three worked examples, easy → hard.

> 🔔 **Reminder behavior:** new days lead with the interactive HTML (no "upgrade after RECALL" step).
> The after-recall upgrade prompt only applies to *legacy text-only* lessons that predate this change.

---

## 6 · Definition of "Week complete"
- [ ] All 6 days' homework green; capstone shipped to GitHub.
- [ ] You can, from memory: predict a 3-level MRO; name the dunder behind `+`, `==`, `len()`,
      `for`; state when to compose vs inherit; compute a dot product and a matrix×vector;
      explain PagedAttention via the parking-lot analogy.
- [ ] `learning-records/` shows each Day 1–2 growth edge (E1–E4) retrieved correctly at least
      once *after a gap* — i.e., it stuck.

➡️ Start with [`day01_bankaccount/LESSON.md`](./day01_bankaccount/LESSON.md). Skim
[`RESOURCES.md`](./RESOURCES.md) once so you know where the authoritative sources live.
