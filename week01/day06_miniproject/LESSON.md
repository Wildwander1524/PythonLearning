# 📘 Day 6 — Consolidate + Capstone

> **Week 1 · Sat 2026-06-21** · Review the week · Math: Linear Algebra I recap
> **The most underrated day of the week.** New input stops; you turn this week's fragile,
> freshly-poured pieces into durable, connected knowledge — and *prove* it by building something
> that uses all of them.

## 🎯 Objective & mastery bar
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| **Integrate** the whole week into one program | **Create** | you ship the capstone **without re-reading** the week |

This is the cumulative storage-strength test the whole week pointed at. The capstone is the
proof; today's `RECALL.md` is the cumulative quiz that tells you which days are solid first.

---

## Why consolidation day works (the learning science)
You'll feel the urge to push to new content. Resist it.
> 🌱 **Wet concrete must cure.** All week you *poured* concrete (new concepts). Poured-but-uncured
> concrete cracks under load. Today is the cure: no new pouring, just letting it set into
> something that bears weight — before next week's heavier load (NumPy on top of OOP).

Three techniques, each with its reason:
- **Active recall** (today's `RECALL.md`): *retrieve* from a blank mind, don't re-read. 🏋️
  Re-reading is watching someone lift; recall is lifting. Retrieval is the single most effective
  technique in the research literature ([`../RESOURCES.md`](../RESOURCES.md) §C).
- **The Feynman technique:** explain each concept *out loud, in plain words, to a beginner*. The
  moment you reach for jargon to paper over a gap, you found the gap. 🧒 If you can't explain
  `super()` to a smart 12-year-old, you've memorized words, not understanding.
- **Interleaving** (the capstone): one task that *mixes* classes + exceptions + dataclasses +
  context managers + persistence. 🥗 A real meal mixes ingredients; you don't eat the flour, then
  the eggs. Interleaved practice is harder now and far more durable later — the only kind that
  helps on the job.

---

## The week as one story (isolated facts fade; a story sticks)
> **(D1)** one class that did everything — `BankAccount`. **(D2)** *share* behaviour across
> related classes (inheritance) and *guarantee* contracts (ABCs). **(D3)** make objects feel
> *native* — printable, comparable, addable, iterable — via the data model. **(D4)** *judgment*:
> a pile of inheritance is often worse than assembling small parts (composition); declare data
> cleanly (`@dataclass`) and safely (the mutable-default trap). **(D5)** make code *survive
> failure* — exceptions, context managers, packages. **(D6, today)** weld it into one program.

> 🪢 **The math arc underneath, in parallel:** vectors (D2) → dot product (D2) → matrix×vector
> (D3) → matrix×matrix & inverse (D4) → linear combinations & span (D5). That's not a grab-bag —
> it's the exact ladder you re-climb in Week 8 (`W·x + b` *is* a layer) and Week 10 (attention
> *is* matrix products). **This week you quietly learned the alphabet of deep learning.**

---

## Today's flow
1. **`RECALL.md`** — the cumulative self-quiz (17 concept Qs + 12 math problems). Do it
   Feynman-style, out loud, *before* peeking. Your score tells you which day to shore up.
2. **The blank-file test** — pick your weakest day and **re-build its homework from an empty
   file**. Reproducing from nothing (not recognizing) is the real benchmark. Can't rebuild Day 3's
   `Vector2D` cold? That's not failure — that's the exact gap today exists to find and fill.
3. **Capstone** — [`HOMEWORK.md`](./HOMEWORK.md): the CLI contact book that uses every day.
4. **Catch-up** — verify PyTorch imports; confirm your 3-sentence PagedAttention note; re-skim
   the Digest reflection so your career direction stays in view as you build.

---

## ✅ End-of-Week-1 checklist
- [ ] D1 BankAccount → 10/10 (transfer + list history + 2dp)
- [ ] D2 inheritance + ABC; **predicted MRO matched** (edge E3)
- [ ] D3 `Vector2D` (data model)
- [ ] D4 composed `Bank`/`Account`/`Ledger`
- [ ] D5 `logkit` logger package (closes file on error)
- [ ] D6 capstone contact book → GitHub
- [ ] `RECALL.md` cumulative quiz: 15+/17 clean, all 12 math correct
- [ ] PyTorch verified; PagedAttention note written
- [ ] `learning-records/` shows edges E1–E4 each retrieved correctly **after a gap**

When all ticked, tell me **"Week 1 done"** — I'll mark Week 1 ✅ in the study plan, write your
Week-1 retro (strengths + what to reinforce in Week 2), update your ability boundary in
[`../MISSION.md`](../MISSION.md), and open **Week 2 — NumPy**, where this week's by-hand vector
and matrix math becomes one-line vectorized code and you'll *feel* why the math came first.

➡️ **The cumulative quiz:** [`RECALL.md`](./RECALL.md) · **the capstone:** [`HOMEWORK.md`](./HOMEWORK.md)
