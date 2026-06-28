# 🗓️ Review Queue — data-driven spacing (SM-2-lite)

> Replaces guesswork about *what to re-test*. Updated whenever a RECALL / homework item is
> graded. Surface **due-today** items at session start, before new material.
> Maintained per the `/teach` skill's *Retrieval Discipline* rule #3.

## How the numbers work (SM-2-lite)

- **quality (q)** 0–5: 0–2 = failed/shaky · 3 = correct but effortful · 4 = solid · 5 = instant.
- On grade:
  - `q ≤ 2` → `interval = 1 day`, knock `ease` down by 0.2 (floor 1.3).
  - `q = 3` → keep `interval` small (×1.2), `ease` unchanged.
  - `q ≥ 4` → `interval` grows: 1 → 6 → `round(interval × ease)`; nudge `ease` +0.1 (cap 2.8).
- `next-due = last-seen + interval`. Default `ease = 2.5`.

## Due / overdue (check these first)

| Concept | Edge | Last seen | q | ease | interval | **Next due** |
|---------|------|-----------|---|------|----------|--------------|
| Matrix × vector (row·vector dots) | E2 | 2026-06-27 | 2 | 2.1 | 1d | **2026-06-28** |
| Why raise immediately = **fail fast** (C1, D1) | E1 | 2026-06-27 | 1 | 2.3 | 1d | **2026-06-28** |
| Mutable default — *when* created (def-time, not per-call) (C3, D4) | E4 | 2026-06-27 | 2 | 2.3 | 1d | **2026-06-28** |

> ⚠️ **Still overdue (untested this session, due 06-26):** Matrix × matrix / identity / non-commutativity,
> `NotImplemented` vs `False`, `__repr__` vs `__str__`, read-only `@property`, EXTEND vs REPLACE.
> Quick q4 maintenance reps — knock out next session start before new material.

> ✅ **2026-06-27 — Day-5 spaced callbacks + 2 overdue cold re-tests graded** (session start, cold):
> - *Generator = `yield`-fn / auto `StopIteration`* — **q4 graduated**: "Python automatically raises
>   StopIteration" unaided & cold (searched last time). 1d→6d, ease 2.3→2.4, → Scheduled, **due 07-03**.
> - *Matrix × vector* (E2) — **q2**: shape ✓ + entry 1 ✓, entry 2 arithmetic slip (17→13) corrected on
>   one nudge. Recurring E2 careless-arithmetic edge. Reset 1d, ease 2.3→2.1, **due 06-28**.
> - *C2 (D3) `for`→`StopIteration`* — **q4**: named the loop-ending exception cold. Folds into iterator items.
> - *C1 (D1) why raise immediately* — **q1 (forgot)**: **fail-fast** principle revealed after a genuine
>   attempt (had answered the *how* not the *why*). Re-queue 1d, **due 06-28**.
> - *C3 (D4) mutable default — the *when** — **q2**: first "first instance" (wrong) → corrected to
>   **def-time** on retry. Re-queue 1d, **due 06-28**.

> ✅ **2026-06-25 — 3 overdue items tested cold** (start of Day-5 session, before new material):
> - *Generator = `yield`-fn* — **q2**: `StopIteration` named but **searched** (no unaided recall). Reset 1d, ease 2.5→2.3, due 06-26.
> - *Matrix × vector* — **q2**: `[[6],[15]]` values right but **searched** + structure was scaffolded. Reset 1d, ease 2.5→2.3, due 06-26.
> - *Two ways to make `for` work* (`__iter__`/`__getitem__`) — **q4 graduated**: both named cold, distinction held; banked the `IndexError`-stops-`__getitem__` nuance. 2d→6d, **due 07-01** (→ Scheduled).
>
> ✅ **2026-06-24 — Day-4 RECALL graded** (composition / `@dataclass` / matrix math; grill folded in):
> - *Composition vs inheritance* (E4) — **solid q4**: B1 all four · B2 `sort`/`insert` leak · D `Playlist`
>   has-a + `append`/`extend`/`insert`/`sort`. Grill Q1+Q2 cleared. **2d → 6d** (due 06-30).
> - *`@dataclass` mutable-default* (E4) — **solid q4**: `field(default_factory=list)`, shared-list fix,
>   `__slots__` speed→memory slip self-corrected on one nudge. **2d → 6d** (due 06-30).
> - *`__eq__`/`__hash__`* (E4) — **q3**: fixes + guardrail cold (S2), but the **contract invariant**
>   (`a==b ⟹ hash(a)==hash(b)`) still wasn't *stated* — re-test the invariant. Held, due 06-27.
> - *Golden rule `__add__`* (E4) — **pulled back to q3**: "new object" right, but the *why* cross-wired
>   with the hash contract (2 nudges to reach "operands unchanged + no aliasing"). Re-test the WHY. Due 06-27.
> - *Matrix × matrix / identity / non-commutativity* (E2) — **q3**: `A·I=A` instant, `A·B≠B·A` known,
>   but row·col **arithmetic slipped twice** (E1→19, E3 (1,2) entry) — needed recompute. Drill it. Due 06-26.

## Scheduled (not yet due)

| Concept | Edge | Last seen | q | ease | interval | Next due |
|---------|------|-----------|---|------|----------|----------|
| Matrix × matrix / identity / non-commutativity (by hand) | E2 | 2026-06-24 | 3 | 2.5 | 2d | 2026-06-26 |
| `NotImplemented` vs `False` in `__eq__` | — | 2026-06-20 | 4 | 2.6 | 6d | 2026-06-26 |
| `__repr__` vs `__str__` (fallback direction) | — | 2026-06-20 | 4 | 2.6 | 6d | 2026-06-26 |
| Read-only `@property` invariant (no setter) | — | 2026-06-18 | 4 | 2.6 | 6d | 2026-06-26 |
| EXTEND vs REPLACE override flavor | E3 | 2026-06-18 | 4 | 2.6 | 6d | 2026-06-26 |
| Golden rule: `__add__` — re-test the ***why*** (operands unchanged, no aliasing) | E4 | 2026-06-24 | 3 | 2.5 | 3d | 2026-06-27 |
| `__eq__` / `__hash__` — re-test the **contract invariant** | E4 | 2026-06-24 | 3 | 2.3 | 3d | 2026-06-27 |
| 3-level MRO prediction (`super()` ≠ parent) | E3 | 2026-06-22 | 4↑ | 2.6 | 5d | 2026-06-27 |
| Iterable vs iterator vs generator | — | 2026-06-22 | 4↑ | 2.5 | 6d | 2026-06-28 |
| Generator = `yield`-fn (auto `StopIteration`) | — | 2026-06-27 | 4↑ | 2.4 | 6d | 2026-07-03 |
| Two ways to make `for` work (`__iter__` / `__getitem__`, `IndexError` stop) | E1 | 2026-06-25 | 4↑ | 2.6 | 6d | 2026-07-01 |
| Composition vs inheritance (is-a / has-a) | E4 | 2026-06-24 | 4↑ | 2.6 | 6d | 2026-06-30 |
| `@dataclass` mutable-default (`field(default_factory=…)`) | E4 | 2026-06-24 | 4↑ | 2.6 | 6d | 2026-06-30 |
| Dot product / norm by hand | E2✅ | 2026-06-20 | 5 | 2.7 | 11d | 2026-07-01 |

## Awaiting first exposure (add once graded)

- Matrix **inverse** (compute by hand) ← D4 math — covered conceptually, not yet drilled
- Custom exception hierarchy · context managers ← D5

---
> Edges: **E1** spec precision · **E2** formula/units · **E3** MRO/inheritance · **E4** Pythonic
> hygiene. A concept tagged to an edge that reaches q≥4 *after a gap* helps graduate that edge.
