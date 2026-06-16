# 📘 Week 1 · Day 2 — Inheritance, Polymorphism & ABCs

> **Date:** Tue 2026-06-17  ·  **Curriculum:** Python OOP deep-dive  ·  **Math:** Linear Algebra I

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | Single / multi inheritance · `super()` · MRO |
| **S2** Core Theory B | 2 h | Polymorphism · method overriding · Abstract Base Classes (`abc`) |
| **S3** Math | 1 h | Dot product · vector norm · distance |
| **S4** Frontier | 2 h | "What is an LLM" + the 3 career directions (reading, no code) |
| **Homework** | 3 h | See [`HOMEWORK.md`](./HOMEWORK.md) |

---

## 📑 Contents

1. [S1 — Inheritance & `super()`](#s1--inheritance--super)
2. [S2 — Polymorphism & Abstract Base Classes](#s2--polymorphism--abstract-base-classes)
3. [S3 — Math: dot product, norm, distance](#s3--math-dot-product-norm-distance)
4. [S4 — Frontier: LLMs & your 3 directions](#s4--frontier-llms--your-3-directions)
5. [🧠 Cheat-sheet](#-cheat-sheet)

---

## S1 — Inheritance & `super()`

**Inheritance** lets a child class *reuse* a parent's code and *extend or override* it.
**`super()`** is how a child calls the parent's version of a method.

### Single inheritance

```python
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Woof")        # delegate to Animal.__init__

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"


d = Dog("Rex")
print(d.speak())          # Rex says Woof   ← inherited
print(d.fetch("ball"))    # Rex fetches the ball!
```

> ⚠️ **`super().__init__(...)` is not optional.** Skip it and `Animal.__init__` never runs — `self.name` and `self.sound` won't exist, and the next attribute access crashes.

### Method overriding

A child can **redefine** a parent method. The parent version still exists — reach it with `super()`.

```python
class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Meow")

    def speak(self) -> str:                   # OVERRIDE
        base = super().speak()                # "Whiskers says Meow"
        return f"{base} (and purrs)"
```

### Multiple inheritance & the MRO

```python
class Flyable:
    def move(self): return "flying"

class Swimmable:
    def move(self): return "swimming"

class Duck(Flyable, Swimmable):
    pass

print(Duck().move())     # → "flying"   (Flyable is listed first)
print(Duck.__mro__)
# (Duck, Flyable, Swimmable, object)
```

**MRO = Method Resolution Order.** When you call a method, Python searches classes **left-to-right** along `__mro__` (computed by the *C3 linearization* algorithm) and uses the **first** match. This is why the order in `class Duck(Flyable, Swimmable)` matters.

> 🔑 **Rule of thumb:** leftmost parent wins ties. Inspect any class's lookup order with `ClassName.__mro__`.

---

## S2 — Polymorphism & Abstract Base Classes

### Polymorphism

*Same interface, different behavior per type.* Python doesn't check the type — it just calls the method on whatever object is there (**duck typing**).

```python
animals = [Dog("Rex"), Cat("Whiskers"), Animal("Parrot", "Squawk")]
for a in animals:
    print(a.speak())     # each object runs ITS OWN speak()
```

### Abstract Base Classes (`abc`)

Use an ABC when you want to **force** every subclass to implement certain methods — a *contract*.

```python
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...          # no body — subclass MUST provide one

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:            # concrete — shared by all shapes
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)
```

What the ABC enforces:

| Attempt | Result |
|---------|--------|
| `Shape()` | ❌ `TypeError: Can't instantiate abstract class Shape` |
| Subclass that forgets `area()` | ❌ `TypeError` on instantiation |
| `Circle(2).describe()` | ✅ works — `describe()` calls the subclass's `area()` |

> 🚀 **Why this matters for AI/ML:** every PyTorch model subclasses `nn.Module` and **must** implement `forward()`. It's the exact same "base class defines the contract, you fill in the method" pattern you're learning today — just at industrial scale.

---

## S3 — Math: dot product, norm, distance

> Notation: vectors `a = [a₀, a₁, …, aₙ₋₁]`, `b = [b₀, …, bₙ₋₁]`, same length `n`.

### Dot product

```text
a · b  =  a₀·b₀ + a₁·b₁ + … + aₙ₋₁·bₙ₋₁
       =  ‖a‖ · ‖b‖ · cos(θ)          (θ = angle between a and b)
```

| Sign of `a · b` | Angle | Meaning |
|-----------------|-------|---------|
| `> 0` | `< 90°` | similar direction |
| `= 0` | `= 90°` | **orthogonal** (perpendicular) |
| `< 0` | `> 90°` | opposite direction |

### Norm (length) & distance

```text
‖a‖            =  sqrt(a₀² + a₁² + … + aₙ₋₁²)          # vector length
dist(a, b)     =  ‖a − b‖  =  sqrt( Σ (aᵢ − bᵢ)² )      # Euclidean distance
cosine_sim     =  (a · b) / (‖a‖ · ‖b‖)                 # direction-only similarity
```

> 🚀 **Why this matters:** LLMs compare meaning with **cosine similarity** of text embeddings. Every vector-database lookup in RAG (Week 12) is dot products at massive scale. This 1-hour topic is the literal core of semantic search.

### Practice (solve by hand, then verify)

```python
import math

a = [1, 2, 3]
b = [4, 0, -1]

dot     = sum(x * y for x, y in zip(a, b))            # = 1
norm_a  = math.sqrt(sum(x ** 2 for x in a))           # = sqrt(14) ≈ 3.742
norm_b  = math.sqrt(sum(x ** 2 for x in b))           # = sqrt(17) ≈ 4.123
cos_sim = dot / (norm_a * norm_b)                     # ≈ 0.0648
dist    = math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))   # = sqrt(25) = 5.0
```

**Do these by hand first** (this is the point of the math hour), then run the code to check:
1. `[2,1] · [1,2]` = ?
2. `‖[3,4]‖` = ?  (classic 3-4-5)
3. Are `[1,0]` and `[0,1]` orthogonal? What's their dot product?
4. Distance between `[0,0]` and `[3,4]` = ?

---

## S4 — Frontier: LLMs & your 3 directions

> **Today is reading, not coding** — build mental models, take notes. Budget ~2 h.

### Part 1 — "What is an LLM" (~45 min)

Watch/read Andrej Karpathy's **"Intro to Large Language Models"** (search the title on YouTube, ~1 h talk; a written summary is fine if you're short on time).

**Note these three takeaways in your own words:**
- **Next-token prediction** — an LLM is trained to predict the next word, over and over.
- **Scale** — more data + parameters + compute → qualitatively better behavior.
- **Emergent abilities** — skills (reasoning, translation) that appear only past a certain scale.

### Part 2 — Your 3 career directions (~60 min)

These are *your* differentiators (industrial LLM + edge focus). Skim each and form one mental model:

| Direction | Search term | Mental model to form |
|-----------|-------------|----------------------|
| **vLLM / inference acceleration** 🥇 | *"vLLM PagedAttention explained"* | GPUs are expensive → you must serve one model to many users at once. vLLM batches requests with a **paged KV-cache** (like OS virtual memory, but for attention). |
| **Edge multimodal (MobileCLIP)** | *"MobileCLIP Apple"* (read the abstract) | **CLIP** maps images and text into the *same* vector space so you can compare them. **"Mobile"** = compress it to run on-device, no cloud. |
| **Video understanding** | *"Video-LLaMA paper"* (abstract) | Video = sequence of image frames (+ audio). The hard part is **temporal reasoning** — understanding change *across* frames. |

> 📌 **Priority reminder (from your plan §1):** `vLLM/TensorRT-LLM` is **mainstream / near-required** — top priority. Edge-multimodal is your **strategic differentiator**. Video understanding is an **elective showcase**.

### Part 3 — Reflection (~15 min)

Write a few sentences in a study journal:

> *Of the 3 directions, which connects most to my engineering background, and why?*

No right answer — this clarifies where you'll aim your capstone in Week 13.

---

## 🧠 Cheat-sheet

```python
# INHERITANCE
class Child(Parent):
    def __init__(self, ...):
        super().__init__(...)        # ALWAYS call parent __init__
    def method(self):
        return super().method() + "extra"   # extend, don't replace

# MRO
Child.__mro__            # exact left-to-right lookup order

# ABSTRACT BASE CLASS
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def must_implement(self): ...    # subclass is forced to define this

# POLYMORPHISM = call the same method on different types; each runs its own
```

| Term | One-liner |
|------|-----------|
| **Inheritance** | child reuses + extends parent |
| **`super()`** | call the parent's version |
| **Override** | child redefines a parent method |
| **MRO** | the order Python searches classes for a method |
| **Polymorphism** | same call, type-specific behavior |
| **ABC** | base class that forces subclasses to implement methods |
| **Dot product** | `Σ aᵢbᵢ`; sign tells you the angle relationship |
| **Cosine similarity** | dot product normalized → direction-only similarity |

---

➡️ **Next:** open [`HOMEWORK.md`](./HOMEWORK.md) and build the Animal hierarchy + Shape ABC.
