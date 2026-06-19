# 📝 Day 2 Homework — Animal hierarchy + Shape ABC (calibrated rebuild)

> **Goal:** prove inheritance, `super()`, the **MRO**, override flavours, polymorphism, and ABCs
> by building two class families + tests.
> **Time:** 3 h · **Read first:** [`LESSON.md`](./LESSON.md)
> **Calibration:** your prior version was 18/22. The four fails (Heron, circle `/2`, `fetch`
> ignoring `item`, `super(Bird,self)`) are now *baseline* — and there's a new **MRO-prediction**
> requirement targeting edge E3.

## 📖 Before you code
Re-read the spec **twice** (E1). For each override, decide **extend vs replace** and label it.
For each `__init__`, the rule is `super().__init__(...)` with **no args** unless you can state
exactly why not.

## ⏱️ Budget
| Block | Time | Build |
|-------|------|-------|
| A | 80 min | `animals.py` — hierarchy + **predicted** MRO |
| B | 60 min | `shapes.py` — ABC + polymorphism |
| C | 40 min | `test_day02.py` — tests, run, push |

---

## Part A — `animals.py`
```text
Animal
├── Dog     "Woof",  fetch(item)
├── Cat     "Meow",  purr()
└── Bird    "Tweet", fly(altitude)
    └── Parrot  "Squawk", learn(phrase) → repeat it
```
- [ ] `Animal.__init__(self, name, sound)`; **every** subclass calls `super().__init__(...)`.
- [ ] Override `speak()` in ≥3 subclasses; ≥1 must be **EXTEND** (`super().speak()` + more) and
      labelled `# EXTEND`; label any **REPLACE** too.
- [ ] `Dog.fetch(item)` output **must contain `item`** (e.g. `"Rex fetches the ball!"`). *(E1)*
- [ ] `Parrot.__init__(self, name)` uses **`super().__init__(name)`** then `self.sound =
      "Squawk"` — **not** `super(Bird, self)`. *(E3 — the exact fix.)*
- [ ] `Parrot.learn("Hello")` then `.speak()` → `"Polly says Squawk — Hello!"` (and **no** dangling
      `" — !"` when nothing's been learned — guard it).
- [ ] **MRO requirement (E3):** in a comment, **write your predicted `Parrot.__mro__` first**,
      then print it and confirm. Explain in one line each why each class is in that position.

## Part B — `shapes.py`
- [ ] `Shape(ABC)` with `@abstractmethod area()` + `perimeter()`, concrete `describe()`.
- [ ] `Circle(r)` — `area = πr²` (**no `/2`** — that's a semicircle). `Rectangle(w,h)`,
      `Triangle(a,b,c)`.
- [ ] `Triangle.area` uses **Heron's formula**: `s=(a+b+c)/2`, `area=√(s(s-a)(s-b)(s-c))` — *not*
      `math.hypot`. For 3-4-5 it must give **6.0**. *(E2 — derive it, sanity-check the number.)*
- [ ] Triangle-inequality guard in `__init__` (you did this last time — keep it).
- [ ] `total_area(shapes) -> float` summing via polymorphism — **zero `isinstance`**.
- [ ] `Shape()` directly raises `TypeError`.

## Part C — `test_day02.py`
Cover at least: `Dog("Rex").fetch("ball")` contains `"ball"` · `Cat.speak` is the extended form ·
`isinstance(Parrot("Polly"), Bird)` **and** `Animal` both `True` · **`Parrot.__mro__ == (Parrot,
Bird, Animal, object)`** · `Circle(1).area()≈π` · `Triangle(3,4,5).area()==6.0` ·
`total_area([Circle(1),Rectangle(2,3)])≈9.1416` (tol `1e-6`) · `Shape()` raises `TypeError` · a
`Shape` subclass missing `area()` raises `TypeError` at instantiation.

## 🧠 Concept checks (comment at bottom of `animals.py`)
1. You used `super(Bird, self)` before and it "worked." Explain precisely *what it did to the
   MRO* and why it was wrong anyway.
2. Why does `Bird` come before `Animal` in `Parrot.__mro__`?
3. Why is `total_area` better than an `isinstance` ladder? What changes in each when you add
   `Pentagon`?

## ✅ Definition of done
- [ ] Both families built; **predicted MRO matched the printed MRO** · ≥1 labelled EXTEND ·
      `total_area` has zero `isinstance` · 3-4-5 triangle = 6.0 · all tests green · pushed.

## 🌟 Stretch
- **Cooperative `super()`:** a `SwimMixin` with `__init__(**kwargs)` calling `super().__init__`;
  watch the baton pass along a multiple-inheritance MRO (print it, predict it first).
- `Square(Rectangle)` whose `__init__(side)` calls `super().__init__(side, side)`.
- `Penguin(Bird)` overriding `fly()` to raise `NotImplementedError` — a hint that inheritance can
  model reality badly (foreshadows Day 4's "prefer composition").

## 🚀 Submit
```bash
git add week01/day02_inheritance && git commit -m "update: Week1 D2 — Heron+MRO fixes, predicted MRO" && git push
```
➡️ Then [`RECALL.md`](./RECALL.md), and again cold before Day 3.
