# 📝 Day 2 Homework — Animal hierarchy + Shape ABC

> **Goal:** Prove you understand inheritance, `super()`, the MRO, method overriding, polymorphism, and abstract base classes — by building two small class families and testing them.
> **Time:** 3 h  ·  **Read first:** [`LEARNING.md`](./LEARNING.md)

---

## 📖 Before you start (5 min)

Skim these sections of [`LEARNING.md`](./LEARNING.md) — you'll apply each directly:
- **"`super()` is not optional"** + **"What `super()` actually is"** → you'll call it in every subclass.
- **"MRO"** + **the relay-race analogy** → you'll print and explain `Parrot.__mro__`.
- **"Extend vs replace"** (the gift-wrapping analogy) → decide this consciously for each override.
- **"ABC = job contract / wall-socket standard"** → you'll build `Shape` as a contract.
- **"Polymorphism deletes the `isinstance` ladder"** → your `total_area` must have zero `isinstance`.

> 🎯 **The mindset for today:** as you write each line, narrate the analogy out loud — *"Is this is-a or has-a? Am I extending or replacing? Who's next in the MRO?"* The homework is the gym; the analogies are your form.

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 90 min | `animals.py` — the inheritance hierarchy + MRO |
| **B** | 60 min | `shapes.py` — the abstract base class + polymorphism |
| **C** | 30 min | `test_day02.py` — tests, run, push |

## 📁 Files

```text
week01/day02_inheritance/
├── animals.py
├── shapes.py
└── test_day02.py
```

---

## Part A — `animals.py` (90 min)

Build this **3-level** hierarchy (the third level, `Parrot`, is what makes the MRO interesting):

```text
Animal
├── Dog      speaks "Woof",   has fetch(item)
├── Cat      speaks "Meow",   has purr()
└── Bird     speaks "Tweet",  has fly(altitude)
    └── Parrot   speaks "Squawk", can learn(phrase) then repeat it
```

**Requirements**

- [ ] `Animal.__init__(self, name, sound)` sets both attributes; **every** subclass calls `super().__init__(...)` (the foundation-crew rule).
- [ ] Override `speak()` in at least **3** of the 4 subclasses.
- [ ] In **at least one** override, use the **extend** flavor: call `super().speak()` and add to its result (not a full replace). Add a comment marking it `# EXTEND`.
- [ ] `Parrot` is **multi-level** (`Parrot → Bird → Animal`). Its `__init__` takes only `name`; the sound is hardcoded to `"Squawk"`.
- [ ] `Parrot.learn("Hello")` stores a phrase; afterwards `Parrot.speak()` returns e.g. `"Polly says Squawk — Hello!"`.
- [ ] Print `Parrot.__mro__` and write a **comment explaining each class in the chain** and why it's in that order (children before parents).

> 💡 **Hint for `Parrot.speak`:** call `super().speak()` to get the base `"... says Squawk"`, then append the learned phrase. Reuse, don't rewrite — that's the gift-wrapping "extend."

## Part B — `shapes.py` (60 min)

Implement the `Shape` ABC from [`LEARNING.md`](./LEARNING.md), then:

- [ ] `Circle(radius)`, `Rectangle(w, h)`, `Triangle(a, b, c)` — all subclass `Shape`.
- [ ] `Triangle.area()` uses **Heron's formula**: `s = (a+b+c)/2`, `area = sqrt(s(s-a)(s-b)(s-c))`.
- [ ] Inherit the **concrete** `describe()` from `Shape` — don't reimplement it in each subclass (that's the "free company perk" from the contract analogy).
- [ ] A standalone `total_area(shapes: list) -> float` that sums areas via **polymorphism** — **no `isinstance` checks** (that's the whole point; the socket doesn't care what's plugged in).
- [ ] Confirm `Shape()` directly raises `TypeError` (the contract rejects an unsigned hire).

## Part C — `test_day02.py` (30 min)

Reuse the Day-1 harness style. Cover at minimum:

- [ ] `Dog("Rex").speak()` returns the expected string
- [ ] `isinstance(Parrot("Polly"), Bird)` and `isinstance(Parrot("Polly"), Animal)` are both `True` (proves the chain)
- [ ] `total_area([Circle(1), Rectangle(2, 3)])` ≈ `9.1416` (use a tolerance: `abs(got - exp) < 1e-6`)
- [ ] Instantiating `Shape()` raises `TypeError`
- [ ] A subclass of `Shape` that forgets `area()` *also* raises `TypeError` when instantiated
- [ ] `Parrot.learn("Hello")` then `.speak()` contains `"Hello"`

---

## 🧠 Concept checks (answer in a comment at the bottom of `animals.py`)

1. You removed `super().__init__()` from `Dog`. What error appears, and *why* (in foundation-crew terms)?
2. In `Parrot.__mro__`, why does `Bird` appear before `Animal`?
3. Why is `total_area` better than a function with `if isinstance(s, Circle): ... elif ...`? What happens to each when you add a new `Pentagon` shape?

## ✅ Definition of done

- [ ] Both class families implemented; `Parrot.__mro__` printed + explained
- [ ] At least one `# EXTEND` override using `super()`
- [ ] `total_area` works with **zero** `isinstance` checks
- [ ] All tests pass: `python test_day02.py`
- [ ] Concept checks answered; pushed to GitHub

## 🌟 Stretch

- **Cooperative `super()`:** give `Bird` and a new `mixin` class each an `__init__` that calls `super().__init__(**kwargs)`, and watch the baton pass along the MRO (the relay-race demo from `LEARNING.md`).
- Add `Square(Rectangle)` whose `__init__(side)` calls `super().__init__(side, side)` — a single-arg subclass of a 2-arg parent.
- Add `Penguin(Bird)` that **overrides** `fly()` to raise `NotImplementedError("penguins can't fly")` — a lesson in when inheritance models reality badly (foreshadows Day 4's "prefer composition").

---

## 🚀 Submit

```bash
git add week01/day02_inheritance
git commit -m "add: Week1 D2 inheritance and ABC"
git push
```
