# 📝 Day 3 Homework — `Vector2D`

> **Goal:** Build a 2D vector class that behaves like a native Python type — using dunder methods for arithmetic, equality, display, indexing, and iteration. Install your own "hammers."
> **Time:** 3 h  ·  **Read first:** [`LEARNING.md`](./LEARNING.md)

---

## 📖 Before you start (5 min)

Skim these sections of [`LEARNING.md`](./LEARNING.md):
- **"The data model"** (piano-keys/hammers analogy) → the *why* behind every method below.
- **"`__repr__` vs `__str__`"** (ID-card/nametag) → you'll define `__repr__` (always).
- **"The golden rule of operators"** → `+`, `-`, `*` must return a **new** object, never mutate.
- **"Iterators / generators"** (Pez-dispenser, cassette-tape) → implement `__iter__` with `yield`.
- **"Reflected operators"** (`__rmul__`) → the `2 * v` stretch goal.

> 🎯 **The test for every method:** *"Does this make my object behave more like a built-in `int` or `list`?"* If yes, you're doing it right.

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 60 min | Core: `__init__`, `__repr__`, `__eq__`, `__add__`, `__sub__` |
| **B** | 60 min | Scalar `__mul__`, `__abs__` (magnitude), `dot()` |
| **C** | 30 min | Indexing + iteration (`__getitem__`, `__iter__`) |
| **D** | 30 min | Tests, run, push |

## 📁 Files

```text
week01/day03_dunder/
├── vector2d.py
└── test_vector2d.py
```

---

## Requirements

Build `Vector2D` so that **all** of the following work:

```python
v = Vector2D(3, 4)
w = Vector2D(1, 2)

repr(v)               # 'Vector2D(3, 4)'   ← round-trips: valid code to recreate it
v == Vector2D(3, 4)   # True
v + w                 # Vector2D(4, 6)
v - w                 # Vector2D(2, 2)
v * 2                 # Vector2D(6, 8)      (scalar multiply)
abs(v)                # 5.0                 (magnitude = sqrt(3² + 4²) = the D2 vector NORM)
v.dot(w)              # 11                  (3·1 + 4·2 = the D2 DOT PRODUCT)
v[0], v[1]            # 3, 4                (indexing)
x, y = v              # unpacking via iteration
list(v)               # [3, 4]
```

### Checklist

- [ ] `__init__(self, x, y)` stores both components
- [ ] `__repr__` → `'Vector2D(3, 4)'` (aim for the round-trip ideal — looks like code that recreates it)
- [ ] `__eq__` compares both components; return `NotImplemented` (not `False`) if `other` isn't a `Vector2D`
- [ ] `__add__` and `__sub__` return a **new** `Vector2D` (golden rule: never mutate `self`)
- [ ] `__mul__(self, scalar)` scales both components
- [ ] `__abs__` returns the magnitude — *this is literally the vector norm from Day 2's math*
- [ ] `dot(self, other)` returns the dot product — *literally Day 2's dot product*
- [ ] `__getitem__` supports `v[0]` / `v[1]`, raises `IndexError` otherwise (so iteration can detect "the end")
- [ ] `__iter__` yields `x` then `y` (use a **generator** with `yield` — the cassette-tape shortcut)

> 💡 **You are now *implementing* the linear algebra you studied.** `abs(v)` is `‖v‖`; `v.dot(w)` is `v · w`. Day 2 was the math on paper; today it's the code. Tomorrow PyTorch tensors will do the same via `@` and `.norm()`.

---

## Tests (Block D)

Reuse the Day-1/2 harness style. Cover at minimum:

- [ ] `Vector2D(3, 4) + Vector2D(1, 2) == Vector2D(4, 6)`
- [ ] `abs(Vector2D(3, 4)) == 5.0`
- [ ] `Vector2D(3, 4).dot(Vector2D(1, 2)) == 11`
- [ ] `list(Vector2D(3, 4)) == [3, 4]` (iteration works)
- [ ] `v[2]` raises `IndexError`
- [ ] **`v + w` does not mutate `v`** (check `v` is unchanged afterward — proves the golden rule)

---

## 🧠 Concept checks (comment at the bottom of `vector2d.py`)

1. Why must `__add__` return a *new* `Vector2D` instead of modifying `self.x`/`self.y`? (Give the cookie-recipe reasoning.)
2. You defined `__iter__` with `yield`. What two values does it produce, and how does Python know to stop?
3. If you delete `__repr__`, what does `[Vector2D(3,4)]` print, and why is that bad for debugging?

## ✅ Definition of done

- [ ] Every example in the Requirements block runs as shown
- [ ] All tests pass: `python test_vector2d.py`
- [ ] Concept checks answered; pushed to GitHub

## 🌟 Stretch

- **Reflected operator:** add `__rmul__` so `2 * v` works (not just `v * 2`). Trace *why* Python falls back to it: `int.__mul__(2, v)` returns `NotImplemented`, so Python tries `v.__rmul__(2)`.
- Add `__neg__` so `-v` returns `Vector2D(-x, -y)`.
- Make it **hashable**: add `__hash__` (since you defined `__eq__`) so vectors can go in a `set`. Why is this only safe if the vector is treated as immutable? (The coat-check-ticket reasoning.)
- Generalize to `VectorND(*components)` using a tuple internally — `__iter__`, `dot`, and `__abs__` all generalize cleanly.

---

## 🚀 Submit

```bash
git add week01/day03_dunder
git commit -m "add: Week1 D3 Vector2D with operator overloading"
git push
```
