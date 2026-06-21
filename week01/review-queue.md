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
| Iterable vs iterator vs generator | — | 2026-06-21 | 2 | 2.3 | 1d | **2026-06-22** ⏰ |
| `__eq__` / `__hash__` contract + mutable footgun | E4 | 2026-06-21 | 2 | 2.3 | 1d | **2026-06-22** ⏰ |
| 3-level MRO prediction (`super()` ≠ parent) | E3 | 2026-06-20 | 3 | 2.5 | 2d | **2026-06-22** ⏰ |

## Scheduled (not yet due)

| Concept | Edge | Last seen | q | ease | interval | Next due |
|---------|------|-----------|---|------|----------|----------|
| Generator = `yield`-fn (auto `StopIteration`) | — | 2026-06-21 | 3 | 2.5 | 2d | 2026-06-23 |
| Matrix × vector (row·vector dots) | E2 | 2026-06-21 | 3 | 2.5 | 2d | 2026-06-23 |
| Two ways to make `for` work (`__iter__` / `__getitem__`) | E1 | 2026-06-21 | 3 | 2.5 | 2d | 2026-06-23 |
| `NotImplemented` vs `False` in `__eq__` | — | 2026-06-20 | 4 | 2.6 | 6d | 2026-06-26 |
| `__repr__` vs `__str__` (fallback direction) | — | 2026-06-20 | 4 | 2.6 | 6d | 2026-06-26 |
| Golden rule: `__add__` returns a NEW object | E4 | 2026-06-20 | 4 | 2.6 | 6d | 2026-06-26 |
| Read-only `@property` invariant (no setter) | — | 2026-06-18 | 4 | 2.6 | 6d | 2026-06-26 |
| EXTEND vs REPLACE override flavor | E3 | 2026-06-18 | 4 | 2.6 | 6d | 2026-06-26 |
| Dot product / norm by hand | E2✅ | 2026-06-20 | 5 | 2.7 | 11d | 2026-07-01 |

## Awaiting first exposure (add once graded)

- Composition vs inheritance (is-a / has-a)  ← D4
- `@dataclass` + mutable-default safety (`field(default_factory=...)`)  ← D4
- Matrix × matrix · identity · inverse  ← D4 math
- Custom exception hierarchy · context managers  ← D5

---
> Edges: **E1** spec precision · **E2** formula/units · **E3** MRO/inheritance · **E4** Pythonic
> hygiene. A concept tagged to an edge that reaches q≥4 *after a gap* helps graduate that edge.
