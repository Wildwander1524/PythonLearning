# 📘 Day 2 — Inheritance, Polymorphism, ABCs & the MRO

> **Week 1 · Tue 2026-06-17** · Curriculum: Python OOP · Math: dot product, norm, distance
> Active reading: stop at every `✍️ Self-explain` / `🔮 Predict`. Today carries growth-edge
> **E3** (you wrote `super(Bird, self)` and skipped a class in the MRO) — the MRO drill below
> exists to close it for good.

## 🎯 Objectives & mastery bar
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Use `super()` + method overriding (extend vs replace) | Apply | you pick the right flavour without thinking |
| **Predict an MRO** of a 3-level / multiple-inheritance class | **Analyze** | you read `__mro__` cold and explain each entry |
| Design an ABC contract | Create | your ABC rejects an incomplete subclass *at instantiation* |
| Polymorphism without `isinstance` ladders | Apply | your `total_area`-style code has zero type checks |
| Math: dot product (algebraic + geometric), norm, distance | Understand | you compute by hand and read the sign of `a·b` |

## 🔁 Spaced callback (do FIRST, from memory — re-tests Day 1)
Before new material, answer cold: ① instance vs class attribute rule? ② what makes a property
read-only? ③ `[2,3] + 2·[1,-1]` = ? *(Blank? Note it — that's the spacing effect working.
Check yesterday's [`SOLUTIONS`](../day01_bankaccount/SOLUTIONS.md) only after trying.)*

---

## The big picture: share what's common, specialize what differs

Yesterday's `BankAccount` was one self-contained class. Soon you need `SavingsAccount` (adds
interest), `CheckingAccount` (allows overdraft). Copy-pasting `BankAccount` three times means a
`withdraw` bug must be fixed four places. **Inheritance** solves this: one source of truth, many
specializations.

> 🏛️ **Analogy — the master blueprint.** An architect draws one master plan, then per client
> adds a sun-room or a third bedroom rather than redrawing everything. Master = **base class**;
> each customization = **subclass**. Fix the master's plumbing and every house inherits the fix.

| Relationship | Test | Tool | Example |
|--------------|------|------|---------|
| **Inheritance** | "A *is a* B" | subclassing (today) | `Dog` **is an** `Animal` |
| **Composition** | "A *has a* B" | hold an attribute (Day 4) | `Car` **has an** `Engine` |

Keep the *is-a* test in mind — by Day 4 you'll learn beginners *over*-use inheritance.

---

## S1 — Inheritance & `super()`

```python
class Animal:
    def __init__(self, name, sound):
        self.name, self.sound = name, sound
    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")     # delegate setup to the parent (foundation crew)
    def fetch(self, item):                 # a NEW ability Animal lacks
        return f"{self.name} fetches the {item}!"
```

`Dog("Rex").speak()` works though `Dog` never defines `speak` — Python looks *up* the chain to
`Animal`. `fetch` lives only on `Dog`.

> 🏗️ **`super().__init__()` is not optional.** The parent's `__init__` is the *only* code that
> sets up the parent's attributes. Skip it and the object is half-built — `self.sound` simply
> doesn't exist, and `speak()` later raises `AttributeError`. (This is the same failure mode as
> forgetting to set `_balance` on Day 1.)

> ✍️ **Self-explain (edge E1, from your Day-2 submission):** your `Dog.fetch` returned a string
> that *ignored* its `item` argument, so the test "ball in output" failed. Re-read the spec
> above: what must `fetch("ball")` contain? *(`"...fetches the ball!"` — use the parameter the
> spec names. Coding what the spec *says*, not what's close, is edge E1.)*

### Override: replace vs extend
```python
class Cat(Animal):
    def __init__(self, name): super().__init__(name, "Meow")
    def speak(self):                          # OVERRIDE
        return f"{super().speak()}... then ignores you"   # EXTEND: reuse parent + add
```
| Flavour | What | When |
|---------|------|------|
| **Replace** | ignore parent, write fresh | parent's behaviour irrelevant |
| **Extend** | call `super().method()`, add to it | want parent's work *plus* more |

> 🎁 *Extend* = add a bow to an already-wrapped gift. *Replace* = rewrap from scratch. Extending
> is the safer default — you keep the parent's guarantees. **Mark each override `# EXTEND` or
> `# REPLACE`** (your `Bird.speak` was a replace left unmarked — label intent).

---

## S2 — The MRO (this is the E3 drill — do it slowly)

Python lets a class have **several** parents, searched **left-to-right**. The famous trap is the
**diamond**: a shared ancestor reached by two paths. Naïve languages run the ancestor twice;
Python runs it **once**, via the **Method Resolution Order**.

> The **MRO** is the single, flattened, deduplicated order Python searches to resolve a method.
> Inspect with `Class.__mro__`. `super()` delegates to **the next class in the MRO** — *not*
> simply "the parent." In single inheritance those coincide (so "super = parent" is a useful
> lie); in multiple inheritance the next MRO class can be a **sibling**.

```python
class Animal:    ...
class Bird(Animal):   ...
class Parrot(Bird):   ...
print(Parrot.__mro__)
# (Parrot, Bird, Animal, object)   ← children before parents; object is the universal base
```

> 🐛 **Your exact bug, dissected.** You wrote `super(Bird, self).__init__(name, "Squawk")` in
> `Parrot.__init__`. `super(Bird, self)` means "start the MRO search *after* `Bird`" — so it
> **skips `Bird.__init__` entirely** and calls `Animal.__init__`. It only *looked* fine because
> `Animal` still set `sound`. Correct: `super().__init__(name)` (→ runs `Bird.__init__` →
> `Animal.__init__`), then `self.sound = "Squawk"` to override after the chain. **`super()` with
> no args is what you want 99% of the time.**

> 🔮 **Predict the MRO (the mastery rep — write it before revealing):**
> ```python
> class A: ...
> class B(A): ...
> class C(A): ...
> class D(B, C): ...
> ```
> What is `D.__mro__`?
> <details><summary>reveal</summary>
>
> `(D, B, C, A, object)`. Rules: children before parents (so `D` first, `A` after both `B`,`C`);
> left-to-right (`B` before `C`); the shared ancestor `A` appears **once**, after *both* paths to
> it are exhausted. This is **C3 linearization**. If you can produce this cold twice (spaced),
> edge E3 graduates.
> </details>

> 🏃 **Relay-race analogy.** Each class does its leg and hands the baton (`super().__init__`) to
> *the next runner the track (MRO) chooses* — possibly a sibling. The baton crosses the finish
> (`object`) exactly once. That's **cooperative** inheritance.

---

## S3 — Polymorphism & Abstract Base Classes

**Polymorphism** = one call, type-specific behaviour, *no `if/elif` type-ladder*:
```python
for a in [Dog("Rex"), Cat("Whiskers")]:
    print(a.speak())      # each runs ITS OWN speak()
```
> 🔌 The universal power socket: the wall delivers power; lamp/kettle each do their own thing.
> Polymorphism lets you **delete** the `isinstance` ladder — every new type would force you to
> edit it. (Your `total_area` had zero `isinstance` — textbook. Keep that instinct.)

**Duck typing** — Python checks *capability*, not lineage: if it has `.speak()`, call it. Liberating but unguarded — until:

**Abstract Base Classes** enforce a contract. An ABC *can't be instantiated* and *forces*
subclasses to implement every `@abstractmethod`:
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def perimeter(self) -> float: ...
    def describe(self):                 # CONCRETE — written once, inherited by all
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"
```
| Attempt | Result | When |
|---------|--------|------|
| `Shape()` | `TypeError` | immediately |
| subclass missing `area()` | `TypeError` | at *instantiation* |
| `Circle(2).describe()` | works (calls subclass `area`) | — |

> 📜 **Job-contract analogy.** `Shape` posts: "be any shape you like, but you *must* tell me
> `area()` and `perimeter()`; in return you get `describe()` free." `@abstractmethod` = a
> required clause; HR (Python) rejects an unsigned hire (incomplete subclass) on the spot.

> 🚀 **This is `nn.Module`.** Every PyTorch network you write (Week 8+) subclasses `nn.Module`
> and *must* implement `forward()` — the exact "base defines the contract, you fill the required
> method" pattern as `Circle` implementing `area()`. Today's toy ABC = next month's neural net.

---

## S4 — Math: dot product, norm, distance (the career formula)

**Algebraic:** `a · b = Σ aᵢbᵢ` → always a single number.
**Geometric:** `a · b = ‖a‖‖b‖cos θ` → how much two arrows point the same way.

| sign of `a·b` | angle | meaning |
|---------------|-------|---------|
| `> 0` | `< 90°` | similar direction |
| `= 0` | `= 90°` | **orthogonal** (unrelated) |
| `< 0` | `> 90°` | opposite |

> 💪 **Pushing a cart** (physics `work = F·d`): push along the motion → all effort counts (big
> `+`); push perpendicular → zero useful work (orthogonal, `a·b=0`).

**Cosine similarity** = the dot product with lengths divided out → direction only, in `[-1, 1]`:
```text
cos_sim(a,b) = (a·b) / (‖a‖‖b‖)
```
> 🚀 **The single most important formula for your career.** An LLM turns a sentence into an
> **embedding** (a vector). "How similar are two sentences?" = cosine similarity of their
> embeddings. Every RAG system (Week 12), every semantic search *is* cosine similarity at scale.
> 3Blue1Brown's "dot products and duality" shows *why* the algebraic and geometric forms agree —
> watch it ([3b1b](https://www.3blue1brown.com/lessons/dot-products/)).

**Norm & distance:** `‖a‖ = √(Σ aᵢ²)` (Pythagoras, n-D); `dist(a,b) = ‖a−b‖`.

> 🔮 **By hand, then verify:** `a=[1,2,3]`, `b=[4,0,-1]`. Compute `a·b`, `‖a‖`, and decide:
> are they closer to aligned or orthogonal? *(`a·b = 1`; `‖a‖=√14≈3.74`; tiny positive dot vs
> the lengths ⇒ nearly orthogonal — `cos≈0.06`.)* **This becomes `Vector2D.dot` + `abs()` in
> tomorrow's homework — you'll *code* exactly this.**

### Frontier (≈2 h reading, no code)
Watch/read **Karpathy's "Intro to LLMs"**; write, in your own words, three takeaways:
*next-token prediction* (autocomplete on steroids), *scale* (more data/params/compute → new
kinds of ability), *emergence* (abilities appear past a threshold, like water→ice). Then skim
your 3 directions (vLLM / MobileCLIP / Video-LLaMA) — one mental model each
([`../RESOURCES.md`](../RESOURCES.md) §D).

---

## 🧠 Cheat-sheet
```python
class Child(Parent):
    def __init__(self, ...):
        super().__init__(...)              # no-args super() = the right call almost always
    def m(self):
        return super().m() + "extra"       # EXTEND (vs REPLACE)
Child.__mro__                              # the fixed search order; super() follows THIS
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def required(self): ...                # subclass FORCED to implement; else TypeError
a·b = Σaᵢbᵢ = ‖a‖‖b‖cosθ ;  cos_sim = a·b/(‖a‖‖b‖) ;  ‖a‖=√Σaᵢ²
```
| Term | One-liner | Analogy |
|------|-----------|---------|
| `super()` | proxy to the *next MRO class* | phone the foundation crew |
| MRO | fixed L-to-R, deduped ancestor order | the org chart of "who do I ask?" |
| extend/replace | reuse parent + add / rewrite | add a bow / rewrap |
| ABC | base that mandates methods | job contract / outlet standard |
| polymorphism | one call, many behaviours; kills `isinstance` ladders | universal socket |
| dot product | `Σaᵢbᵢ`; sign ↔ angle | useful work pushing a cart |
| cosine similarity | dot ÷ lengths → direction only | "about the same thing?" |

## ⚠️ Common pitfalls
1. **`super(Bird, self)`** when you mean `super()` → silently skips a class in the MRO (your E3 bug).
2. **Forgetting `super().__init__()`** → half-built object, later `AttributeError`.
3. **Replacing when you meant to extend** → you drop the parent's setup. Label intent.
4. **`isinstance` ladders** → that's polymorphism asking to be used.
5. **`__eq__` without `__hash__`** → unhashable (more on Day 3).
6. **Reading `super()` as "the parent"** → in multiple inheritance it's the next MRO class, maybe a sibling.

## ✅ Storage-strength check (cold, tomorrow)
Produce `D.__mro__` for `class D(B, C)` above; build a 5-line ABC that rejects an incomplete
subclass; compute `[1,0]·[0,1]` and say what the answer means. Shaky → log it.

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — Animal tree + Shape ABC, with an MRO you must
*predict before printing*.
