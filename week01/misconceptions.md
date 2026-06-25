# 🪤 Misconceptions Catalog — Week 1

> The *topic's* canonical traps (not your personal slips — those are the growth edges E1–E4).
> Each is **Trap → Counterexample → Correct**, tagged to the edge it feeds. I mine this to write
> distractor-rich questions and to pre-empt predictable errors.
> Maintained per the `/teach` skill's *Retrieval Discipline* rule #4.

## OOP & the data model (D1–D3)

**M1 · "`__add__` may mutate `self`."**  ⟶ E4
- Counter: `5 + 3` doesn't change `5`. If `a + b` alters `a`, then `c = a + b; … a …` is corrupted.
- Correct: operators return a **new** object; operands are untouched (value semantics).

**M2 · "Defining `__eq__` leaves the object hashable."**  ⟶ E4
- Counter: add it, then `set()` your object → `TypeError: unhashable type`.
- Correct: defining `__eq__` sets `__hash__ = None`. Equal-must-hash-equal can't be auto-verified.

**M3 · "A mutable object can safely define `__hash__`."**  ⟶ E4  *(caught in your `vector2d.py`)*
- Counter: `s.add(v)` with `v=(1,2)`; then `v.x = 9`; now `v in s` → `False` though `v` is still in
  the old bucket. A **ghost entry**.
- Correct: only define `__hash__` if you *promise* immutability. Mutable → leave it unhashable.

**M13 · "The `__eq__`/`__hash__` *contract* is 'define `__eq__` → `__hash__` becomes `None`'."**  ⟶ E4  *(surfaced 2026-06-22 cold check)*
- Counter: that's the **guardrail** Python auto-applies, not the contract. The contract is a separate
  invariant: `a == b ⟹ hash(a) == hash(b)`. (And **not** the reverse — equal hashes needn't mean equal
  objects; that's a legal *collision*, e.g. `hash(-1) == hash(-2) == -2`.)
- Correct: contract = "equal objects must hash equal"; `__hash__ = None` is merely *how Python protects*
  that contract when it can no longer verify it.

**M4 · "Iterable and iterator are the same thing."**  ⟶ —
- Counter: a `list` is iterable but **not** its own iterator — `iter(lst)` hands back a *separate*
  cursor each call; `next(lst)` raises `TypeError`.
- Correct: iterable has `__iter__` (makes cursors); iterator also has `__next__` and is one-shot.

**M5 · "Return `False` from `__eq__` for an unknown type."**  ⟶ —
- Counter: `False` blocks Python from trying the reflected `other.__eq__(self)` — the other type
  may know how to compare.
- Correct: return `NotImplemented` so the comparison can cooperate (like `super()` along the MRO).

**M6 · "`super()` means *the parent class*."**  ⟶ E3  *(the Day-2 `Parrot` bug)*
- Counter: in `D(B, C)` with `B(A)`, `C(A)`, inside `C` `super()` is **`A`**, but inside `B` it's
  **`C`** — it follows `__mro__`, not a fixed parent. `super(Bird, self)` *skipped* `Bird`.
- Correct: `super()` = "next class in `self`'s MRO," resolved at call time.

## Composition & design (D4)

**M7 · "Inherit from `list` to reuse its code."**  ⟶ E4
- Counter: `class Stack(list)` leaks all ~40 list methods — your "stack" can `.insert()` and
  `.sort()`.
- Correct: **compose** (`self._items = []`) and expose only `push`/`pop`. Has-a, not is-a.

**M8 · "`def f(x=[])` makes a fresh list each call."**  ⟶ E4
- Counter: the list is built **once at def-time**; `f("a"); f("b")` → `['a','b']`.
- Correct: default to `None`, create inside; or `field(default_factory=list)` in a dataclass.

## Linear algebra

**M9 · "Matrix multiplication is commutative (`A·B = B·A`)."**  ⟶ E2
- Counter: shapes alone often forbid it; even when both exist they usually differ. "Socks then
  shoes" ≠ "shoes then socks."
- Correct: order encodes "do B, then A." Generally `A·B ≠ B·A`.

**M10 · "Every matrix has an inverse."**  ⟶ E2
- Counter: a projection 3-D→2-D destroys info — you can't un-flatten a pancake (singular).
- Correct: only non-singular (full-rank) square matrices invert.

**M11 · "`math.hypot` gives any triangle's area."**  ⟶ E2  *(the Day-2 Heron slip)*
- Counter: `hypot` is the **length of a 2-vector** (√(x²+y²)), not an area. Used right in D3's
  `__abs__`, wrong in D2's triangle.
- Correct: match the formula to the job — Heron for area, `hypot` for norm.

**M12 · "`(a + b)² = a² + b²`."**  ⟶ E2  *(generic algebra trap)*
- Counter: `(1+2)² = 9`, not `1 + 4 = 5`. Missing the `2ab` cross term.
- Correct: `(a+b)² = a² + 2ab + b²`.

## Errors, exceptions & context managers (D5)

**M14 · "Catch broadly — `except Exception:` (or bare `except:`) is the safe default."**  ⟶ E4
- Counter: bare `except:` also swallows `KeyboardInterrupt` / `SystemExit` (those are `BaseException`,
  *not* `Exception`) — you can't even Ctrl-C out — and it hides the real bug behind a generic catch.
- Correct: catch the **narrowest** type you can actually handle; let the rest propagate. `except
  Exception` belongs only at a top-level boundary, never bare.

**M15 · "The order of `except` blocks doesn't matter."**  ⟶ E3
- Counter: `except Exception:` placed *before* `except ValueError:` shadows the specific one — matching
  is top-down, first hit wins, so the `ValueError` arm is dead code.
- Correct: order **specific → general** (subclasses before their parents), same instinct as MRO.

**M16 · "A custom exception should subclass `BaseException`."**  ⟶ E3
- Counter: `BaseException` is the root of *system-exiting* signals (`SystemExit`, `KeyboardInterrupt`).
  Subclass it and a normal `except Exception:` will sail right past your error.
- Correct: inherit from **`Exception`** (or a more specific built-in). Give the app one base class
  (`class MyAppError(Exception)`) so callers can catch the whole family with `except MyAppError:`.

**M17 · "`with` (a context manager) suppresses exceptions raised inside it."**  ⟶ E4
- Counter: `with open(...)` still lets a `ValueError` from inside propagate. `__exit__` swallows the
  exception **only if it returns a truthy value**; returning `None`/falsy (the default) re-raises.
- Correct: `__exit__` runs **guaranteed** — success *or* error, like `finally` — for cleanup; suppression
  is opt-in via `return True`. And `as` binds whatever `__enter__` *returns*, not the manager itself.

---
> When a new day's topic lands, add its 2–4 classic traps here *before* writing that day's RECALL,
> so the questions can include the trap as a distractor.
