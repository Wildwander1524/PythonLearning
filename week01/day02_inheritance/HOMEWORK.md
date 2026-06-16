# 📝 Day 2 Homework — Animal hierarchy + Shape ABC

> **Goal:** Prove you understand inheritance, `super()`, multi-level chains, method overriding, polymorphism, and abstract base classes — by building two small class families and testing them.
> **Time:** 3 h  ·  **Companion theory:** [`LEARNING.md`](./LEARNING.md)

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 90 min | `animals.py` — the inheritance hierarchy |
| **B** | 60 min | `shapes.py` — the abstract base class + polymorphism |
| **C** | 30 min | `test_day02.py` — tests, run, push |

## 📁 Files to create

```text
week01/
└── day02_inheritance/
    ├── animals.py
    ├── shapes.py
    └── test_day02.py
```

---

## Part A — `animals.py` (90 min)

Build this **3-level** hierarchy:

```text
Animal
├── Dog      speaks "Woof",   has fetch(item)
├── Cat      speaks "Meow",   has purr()
└── Bird     speaks "Tweet",  has fly(altitude)
    └── Parrot   speaks "Squawk", can learn(phrase) then repeat it
```

**Requirements**

- [ ] `Animal.__init__(self, name, sound)` sets both attributes; **every** subclass calls `super().__init__(...)`.
- [ ] Override `speak()` in at least **3** of the 4 subclasses.
- [ ] `Parrot` is **multi-level** (`Parrot → Bird → Animal`). Its `__init__` takes only `name`; the sound is hardcoded to `"Squawk"`.
- [ ] `Parrot.learn("Hello")` stores a phrase; afterwards `Parrot.speak()` returns something like `"Polly says Squawk — Hello!"`.
- [ ] Print `Parrot.__mro__` and add a **comment** explaining each class in the chain.

> 💡 **Hint for `Parrot`:** call `super().speak()` to get the base `"... says Squawk"`, then append the learned phrase. Reuse, don't rewrite.

---

## Part B — `shapes.py` (60 min)

Implement the `Shape` ABC from [`LEARNING.md`](./LEARNING.md), then:

- [ ] `Circle(radius)`, `Rectangle(w, h)`, `Triangle(a, b, c)` — all subclass `Shape`.
- [ ] `Triangle.area()` uses **Heron's formula**:
  ```text
  s = (a + b + c) / 2
  area = sqrt( s · (s−a) · (s−b) · (s−c) )
  ```
- [ ] A standalone function `total_area(shapes: list) -> float` that sums areas via **polymorphism** — **no `isinstance` checks** allowed (that's the whole point).
- [ ] Confirm `Shape()` directly raises `TypeError`.

> 💡 `total_area` should be ~2 lines: just loop and call `.area()` on each shape. If you're reaching for `isinstance`, stop — polymorphism already handles it.

---

## Part C — `test_day02.py` (30 min)

Reuse the harness style from Day 1. **Cover at minimum:**

- [ ] `Dog("Rex").speak()` returns the expected string
- [ ] `isinstance(Parrot("Polly"), Bird)` is `True` (proves the chain)
- [ ] `total_area([Circle(1), Rectangle(2, 3)])` ≈ `9.1416` (use a tolerance, e.g. `abs(got - exp) < 1e-6`)
- [ ] Instantiating `Shape()` raises `TypeError`
- [ ] `Parrot.learn("Hello")` then `.speak()` contains `"Hello"`

> 💡 **Comparing floats:** never `assert area == 9.1416`. Floating-point math isn't exact — assert the *difference* is tiny:
> ```python
> assert abs(got - expected) < 1e-6, f"got {got}"
> ```

---

## ✅ Definition of done

- [ ] Both class families implemented; `Parrot.__mro__` printed + explained
- [ ] `total_area` works with **zero** `isinstance` checks
- [ ] All tests pass when you run `python test_day02.py`
- [ ] Pushed to GitHub

## 🌟 Stretch (only if you finish early)

- Add a `Square(Rectangle)` that calls `super().__init__(side, side)` — single-arg subclass of a 2-arg parent.
- Add `__str__` to every shape so `print(Circle(2))` is readable.
- Add a `Penguin(Bird)` that **overrides** `fly()` to raise `NotImplementedError("penguins can't fly")` — a lesson in when inheritance models reality badly.

---

## 🚀 Submit

```bash
git add week01/day02_inheritance
git commit -m "add: Week1 D2 inheritance and ABC"
git push
```

Then send it over (or say **"D2 done"**) and I'll review it, tick Week 1 in the plan, and prep Day 3 (dunder methods & the data model).
