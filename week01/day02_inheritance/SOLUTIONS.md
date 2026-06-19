# ✅ Day 2 — SOLUTIONS

> Open only after attempting [`HOMEWORK.md`](./HOMEWORK.md) + [`RECALL.md`](./RECALL.md).

## Reference — `animals.py` (key parts)
```python
class Animal:
    def __init__(self, name, sound):
        self.name, self.sound = name, sound
    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name): super().__init__(name, "Woof")
    def fetch(self, item):                       # E1: USE the parameter
        return f"{self.name} fetches the {item}!"

class Cat(Animal):
    def __init__(self, name): super().__init__(name, "Meow")
    def speak(self):                             # EXTEND
        return f"{super().speak()}... then ignores you"
    def purr(self): return f"{self.name} purrs..."   # use self.name, not a hardcoded name

class Bird(Animal):
    def __init__(self, name): super().__init__(name, "Tweet")
    def speak(self):                             # REPLACE (labelled)
        return f"{self.name} says {self.sound * 3}"
    def fly(self, altitude): return f"{self.name} flies at {altitude} m"

class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)                   # E3 FIX: runs Bird.__init__ → Animal.__init__
        self.sound = "Squawk"                    # override AFTER the chain
        self._learned = ""
    def learn(self, phrase): self._learned = phrase
    def speak(self):                             # EXTEND, guarded
        base = f"{self.name} says {self.sound}"
        return f"{base} — {self._learned}!" if self._learned else base

# MRO — predict FIRST, then verify:
# Parrot.__mro__ == (Parrot, Bird, Animal, object)
#   Parrot — most specialised, searched first (children before parents)
#   Bird   — Parrot's direct parent; before Animal because it's nearer in the chain
#   Animal — Bird's parent; supplies __init__/speak the others build on
#   object — universal base; every chain ends here
```

## Reference — `shapes.py` (key parts)
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): ...
    @abstractmethod
    def perimeter(self): ...
    def describe(self):
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2          # NO /2
    def perimeter(self): return 2 * math.pi * self.r

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("violates triangle inequality")
        self.a, self.b, self.c = a, b, c
    def area(self):                                        # Heron — NOT math.hypot
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self): return self.a + self.b + self.c

def total_area(shapes):
    return sum(s.area() for s in shapes)                  # zero isinstance
```
**Heron sanity check (E2):** 3-4-5 → `s=6`, `area=√(6·3·2·1)=√36=6.0`. ✅ (`math.hypot(s-a,s-b,
s-c)=√(3²+2²+1²)=√14≈3.74` — clearly wrong; the sanity number catches it instantly.)

---

## RECALL answers
**Spaced (D1):** S1 instance = per-object (`self.x`), class = shared (`Cls.x`); per-object data
vs shared constant/counter. S2 no `@x.setter`. S3 `[2,3]+[2,-2]=[4,1]`.

**A — super() without "parent":** `super()` returns a proxy that delegates to **the next class in
`self`'s MRO** after the current one. In a single chain that happens to be the parent; in
multiple inheritance it can be a sibling.

**B**
1. Extend = `super().method()` + additions (keeps parent's guarantees); replace = fresh logic.
   Extend is the safer default. 2. It forbids instantiating the base and forces every
   `@abstractmethod` to be implemented; failure is at **instantiation** (`TypeError`), not
   definition. 3. The polymorphic version never changes when you add `Pentagon` (just give it an
   `area()`); the ladder needs a new `elif` edited into existing, tested code. 4. `a·b=0` ⇒
   orthogonal (90°, unrelated); `a·b<0` ⇒ obtuse angle, pointing oppositely. 5. Cosine similarity
   = `a·b/(‖a‖‖b‖)` ∈ [−1,1]; it removes magnitude so it compares *direction* (meaning) not
   length — long embeddings don't get artificially "more similar."

**C — `F.__mro__`:** `(F, D, B, E, C, A, object)`.
Reasoning (C3): `F` first; merge `D`'s line `(D,B,...A)` with `E`'s `(E,C,A)` keeping
left-to-right and "children before parents" — `D`, then `B` (no other class depends on it yet),
then `E` before `C`? Check: `C` can't appear until everything that subclasses it (`E`) is placed,
so `E` then `C`; `A` last before `object` (both `B`-path and `C` precede it). Verify in a REPL —
*verifying* is part of the rep.

**D — spot-the-bug:** `super(Bird, self)` starts the search **after** `Bird`, skipping
`Bird.__init__`. Fix:
```python
super().__init__(name)      # runs Bird.__init__ → Animal.__init__
self.sound = "Squawk"
```

**E — micro-build:**
```python
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): ...
class Cash(PaymentMethod):
    def pay(self, amount): return f"paid {amount} in cash"
class Card(PaymentMethod):
    def pay(self, amount): return f"charged {amount} to card"
def checkout(methods, amount):
    return [m.pay(amount) for m in methods]      # no isinstance
# PaymentMethod() → TypeError ✅
```

**F — math:** 1. `2+0+2=4`  2. `√(36+64)=10`  3. `1/(1·√2)=1/√2≈0.707`.

## Concept-check answers (homework)
1. `super(Bird, self)` resolves to the MRO entry **after** `Bird` (i.e. `Animal`), so
   `Bird.__init__` is skipped; it only worked because `Animal` still set `sound`. Wrong because
   it violates the foundation-crew rule — if `Bird.__init__` had its own setup, it'd be lost.
2. `Bird` is `Parrot`'s direct parent and nearer in the chain; MRO is children-before-parents,
   left-to-right. 3. See B3.

> 📝 Record: did your **predicted** MRO match the printed one? If yes twice (spaced), E3 graduates.
