# 📘 Week 1 · Day 2 — Inheritance, Polymorphism & ABCs

> **Date:** Tue 2026-06-17  ·  **Curriculum:** Python OOP deep-dive  ·  **Math:** Linear Algebra I

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | Single / multi inheritance · `super()` · MRO |
| **S2** Core Theory B | 2 h | Polymorphism · method overriding · Abstract Base Classes (`abc`) |
| **S3** Math | 1 h | Dot product · vector norm · distance |
| **S4** Frontier | 2 h | "What is an LLM" + the 3 career directions (reading, no code) |
| **Homework** | 3 h | See [`HOMEWORK.md`](./HOMEWORK.md) |

> 🧭 **How to read this file.** Each concept is introduced three times, deliberately: once as an **analogy** (to build intuition), once as **code** (to make it concrete), and once as **"under the hood"** (so you understand *why* it works, not just *that* it works). Don't skip the analogies — they're the hooks your memory hangs the syntax on.

---

## 📑 Contents

1. [The big picture: why inheritance exists](#the-big-picture-why-inheritance-exists)
2. [S1 — Inheritance & `super()`](#s1--inheritance--super)
3. [S2 — Polymorphism & Abstract Base Classes](#s2--polymorphism--abstract-base-classes)
4. [S3 — Math: dot product, norm, distance](#s3--math-dot-product-norm-distance)
5. [S4 — Frontier: LLMs & your 3 directions](#s4--frontier-llms--your-3-directions)
6. [🧠 Cheat-sheet](#-cheat-sheet)
7. [⚠️ Common pitfalls](#️-common-pitfalls-recap)

---

## The big picture: why inheritance exists

Yesterday you built a `BankAccount` — one self-contained class. That works until you need a `SavingsAccount` (adds interest), a `CheckingAccount` (allows overdraft), and a `BusinessAccount` (has multiple signatories). You *could* copy-paste `BankAccount` three times and tweak each. But now a bug in `withdraw` has to be fixed in four places, and they'll drift apart over time. This is the problem inheritance solves: **share what's common, specialize only what differs.**

> 🏛️ **Analogy — the architect's master blueprint.** An architect draws one master blueprint for "a house": foundation, plumbing, roof. For each client they don't redraw everything — they take the master and add a sun-room here, a third bedroom there. The master is the **base class**; each customized house is a **subclass**. Fix a plumbing flaw in the master and every house built from it inherits the fix. That is the entire economic argument for inheritance: **one source of truth, many specializations.**

The two relationships you'll learn to tell apart this week:

| Relationship | Plain-English test | Today's tool | Example |
|--------------|--------------------|--------------|---------|
| **Inheritance** | "A *is a* kind of B" | subclassing (today) | a `Dog` **is an** `Animal` |
| **Composition** | "A *has a* B" | holding an attribute (Day 4) | a `Car` **has an** `Engine` |

Today is entirely about the first one. Keep the "is-a" test in your head — by Day 4 you'll see that beginners over-use inheritance, and knowing *when not to* is as important as knowing how.

---

## S1 — Inheritance & `super()`

**Inheritance** lets a child class *reuse* a parent's code and then *extend or override* it. The child automatically gets every attribute and method the parent defined — for free, without retyping them.

### Single inheritance — the foundation

```python
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"


class Dog(Animal):                      # Dog inherits everything from Animal
    def __init__(self, name: str):
        super().__init__(name, "Woof")  # delegate setup to the parent

    def fetch(self, item: str) -> str:  # a NEW ability Animal doesn't have
        return f"{self.name} fetches the {item}!"


d = Dog("Rex")
print(d.speak())        # Rex says Woof   ← inherited, never written in Dog
print(d.fetch("ball"))  # Rex fetches the ball!
```

Read what just happened slowly, because it's the core mechanic:

1. `Dog("Rex")` calls `Dog.__init__`.
2. `Dog.__init__` calls `super().__init__(name, "Woof")`, which runs `Animal.__init__`, setting `self.name` and `self.sound`.
3. `d.speak()` — `Dog` has no `speak`, so Python looks *up* to `Animal` and finds it there.
4. `d.fetch("ball")` — this lives on `Dog`; `Animal` has never heard of it.

> 🧬 **Analogy — inherited traits.** You have your parents' eye color without "deciding" to; you inherited it. `Dog` has `speak()` without redefining it — inherited. But you also have traits your parents don't (`fetch`), and you can have the *same* trait expressed differently (a different bark — that's overriding, next).

### `super().__init__()` is not optional — here's what breaks

```python
class Cat(Animal):
    def __init__(self, name: str):
        self.name = name            # ❌ forgot super().__init__
        # self.sound was never set!

c = Cat("Whiskers")
c.speak()   # 💥 AttributeError: 'Cat' object has no attribute 'sound'
```

The parent's `__init__` is the only code that sets up the parent's part of the object. Skip it, and the object is **half-constructed** — the attributes the parent promised simply don't exist.

> 🏗️ **Analogy — building on a foundation.** `Animal.__init__` pours the foundation (name, sound). `Cat.__init__` builds the walls on top. If you start building walls without calling the foundation crew first, the house has nothing to stand on. `super().__init__()` is you phoning the foundation crew *before* you start your own work.

### What `super()` actually *is* (under the hood)

Most tutorials say "`super()` calls the parent." That's a useful lie. The truth is more powerful:

> `super()` returns a temporary **proxy object** that delegates method calls to the **next class in the MRO** (Method Resolution Order — see below), *not* simply "the parent." In single inheritance those are the same thing, so the lie works. In multiple inheritance they differ, and that difference is exactly what makes cooperative multiple inheritance possible.

You'll feel why this matters in two minutes, when we hit the diamond.

### Method overriding — same name, new behavior

A child can **redefine** a method it inherited. The parent's version still exists; reach it with `super()`.

```python
class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Meow")

    def speak(self) -> str:                 # OVERRIDE Animal.speak
        base = super().speak()              # "Whiskers says Meow" (parent's version)
        return f"{base}... then ignores you"  # extend, don't discard
```

There are two flavors of override, and good code uses the right one:

| Flavor | What you do | When |
|--------|-------------|------|
| **Replace** | ignore the parent, write fresh logic | the parent's behavior is irrelevant |
| **Extend** | call `super().method()`, then add to it | you want the parent's work *plus* more |

> 🎁 **Analogy — re-wrapping a gift.** "Extend" is taking the gift the parent already wrapped and adding a bow (`super().speak()` + extra). "Replace" is throwing out their wrapping and starting over. Extending is usually the safer instinct: you keep the parent's guarantees and only add.

### Multiple inheritance & the diamond problem

Python lets a class have **several** parents. This is powerful and occasionally dangerous.

```python
class Flyable:
    def move(self): return "flying"

class Swimmable:
    def move(self): return "swimming"

class Duck(Flyable, Swimmable):   # two parents
    pass

print(Duck().move())   # → "flying"   (Flyable is listed first)
```

Why "flying" and not "swimming"? Because Python searches parents **left-to-right**. `Flyable` comes first in `class Duck(Flyable, Swimmable)`, so its `move` wins. Reorder the parents and the answer flips.

Now the famous trap — the **diamond**:

```text
        Animal              Everyone ultimately inherits from Animal.
        /    \              Both Flyable and Swimmable extend it.
   Flyable  Swimmable       Duck inherits from BOTH.
        \    /              → the inheritance graph is shaped like a ◆ diamond.
         Duck
```

The question the diamond poses: when `Duck` calls a method, and both branches lead back to `Animal`, **how many times should `Animal`'s code run, and in what order?** Naïve languages run `Animal` twice (once per path) — a notorious source of bugs. Python guarantees it runs **exactly once**, via the MRO.

### MRO — the Method Resolution Order

> The **MRO** is the single, flattened, deduplicated ordering of all ancestor classes that Python searches when resolving a method. Every class has one. Inspect it with `ClassName.__mro__` or `ClassName.mro()`.

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'Animal'>, <class 'object'>)
```

Read that as a priority list: "to find a method, check `Duck` first, then `Flyable`, then `Swimmable`, then `Animal`, finally `object` (the universal base of everything in Python)." The **first** class that has the method wins. Notice `Animal` appears **once**, even though two paths lead to it — the diamond is collapsed into a clean line.

> 🚌 **Analogy — the chain of command.** The MRO is an org chart for "who do I ask?" You ask the most junior, most specialized person first (`Duck`). If they don't know, the question escalates up a *fixed, agreed* chain until someone answers. C3 linearization (below) is just the algorithm HR used to publish that chain so there's never ambiguity about who gets asked next.

#### How the MRO is computed: C3 linearization (the gist)

Python builds the MRO with an algorithm called **C3 linearization**. You don't need to run it by hand, but understanding its two guarantees demystifies every "why did *that* method get called?" surprise:

1. **Children before parents.** A class always appears before any class it inherits from. (You ask the specialist before the generalist.)
2. **Left-to-right order is preserved.** If you wrote `class Duck(Flyable, Swimmable)`, then `Flyable` is searched before `Swimmable`.

C3 merges these rules across the *whole* hierarchy into one consistent order. If the rules are contradictory (rare, in pathological hierarchies), Python **refuses to create the class** and raises `TypeError` at definition time — a feature, not a bug: it's telling you the hierarchy is genuinely ambiguous.

#### Why `super()` + MRO = cooperative inheritance

Here's the payoff for that "proxy to the next class in the MRO" definition from earlier. Watch each class call `super().__init__()` and the call *flow along the MRO* so every ancestor initializes exactly once:

```python
class Animal:
    def __init__(self, **kw):
        print("Animal init")
        super().__init__(**kw)     # eventually reaches object

class Flyable(Animal):
    def __init__(self, **kw):
        print("Flyable init")
        super().__init__(**kw)     # NOT necessarily Animal — the NEXT in MRO

class Swimmable(Animal):
    def __init__(self, **kw):
        print("Swimmable init")
        super().__init__(**kw)

class Duck(Flyable, Swimmable):
    pass

Duck()
# Flyable init
# Swimmable init      ← super() in Flyable went here, not straight to Animal!
# Animal init         ← runs ONCE, despite two paths
```

This is why "`super()` means the parent" is a lie: inside `Flyable`, `super()` pointed to `Swimmable`, its *sibling*, because that's what came next in `Duck`'s MRO. Each class cooperates by passing the baton along the chain.

> 🏃 **Analogy — a relay race.** Each runner (class) does their leg and hands the baton (`super().__init__`) to *the next runner on the track*, which they don't choose — the track (MRO) decides. The baton crosses the finish line (`object`) exactly once. This is why it's called **cooperative** multiple inheritance: everyone passes the baton; nobody hoards it or drops it.

---

## S2 — Polymorphism & Abstract Base Classes

### Polymorphism — one interface, many behaviors

The word is Greek: *poly* (many) + *morph* (form). One name, many forms. In code: **you call the same method, and the right type-specific behavior happens automatically.**

```python
animals = [Dog("Rex"), Cat("Whiskers"), Animal("Parrot", "Squawk")]
for a in animals:
    print(a.speak())     # each object runs ITS OWN speak() — no if/elif needed
```

> 🔌 **Analogy — the universal power socket.** Every appliance exposes the same interface — a plug. The wall doesn't care whether it's a lamp, a laptop charger, or a kettle; it just delivers power and each device *does its own thing* with it. `speak()` is the plug; lamp/kettle/charger are `Dog`/`Cat`/`Parrot`. Polymorphism is the promise "if you expose the standard plug, I can power you without knowing what you are."

The power of polymorphism is what it lets you *delete*: the `if isinstance(a, Dog): ... elif isinstance(a, Cat): ...` ladder. That ladder is a code smell — every new animal forces you to edit it. Polymorphism replaces the whole ladder with one line that never changes when you add a new type.

### Duck typing — Python's flavor of polymorphism

Python doesn't check an object's *type* before calling a method. It just calls the method and sees if it works.

> 🦆 **Analogy — the original quote.** *"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't demand a birth certificate proving the object is a `Duck`. If it has a `.quack()` method, Python will happily call it. The object's **capabilities** matter, not its **lineage**.

```python
class Person:
    def speak(self): return "Hello"

def make_it_speak(thing):
    return thing.speak()     # works for Dog, Cat, Person — anything with .speak()

make_it_speak(Dog("Rex"))    # "Rex says Woof"
make_it_speak(Person())      # "Hello"   — not an Animal at all, but it has speak()!
```

This is liberating (flexible, less boilerplate) but risky (nothing *forces* a class to provide `.speak()` until something crashes at runtime). Which is exactly the problem the next tool solves.

### Abstract Base Classes (`abc`) — enforcing a contract

Sometimes "I hope every subclass implements `speak()`" isn't good enough — you want to **guarantee** it, and fail *loudly and early* if someone forgets. An **Abstract Base Class (ABC)** is a class that:

- **cannot be instantiated directly**, and
- **forces** subclasses to implement every method marked `@abstractmethod`.

```python
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...          # no body — every subclass MUST supply one

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:            # CONCRETE — shared by all shapes, written once
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

What the ABC enforces, and *when* it catches you:

| Attempt | Result | When it fails |
|---------|--------|---------------|
| `Shape()` | ❌ `TypeError: Can't instantiate abstract class Shape` | immediately |
| `class Tri(Shape)` that forgets `area()` | ❌ `TypeError` the moment you try `Tri(...)` | at instantiation, not definition |
| `Circle(2).describe()` | ✅ works — `describe()` calls the subclass's `area()` | — |

> 📜 **Analogy — a job description / employment contract.** `Shape` is a job posting that says: "Whatever kind of shape you are, you *must* be able to tell me your `area()` and `perimeter()`. In return, I'll give you a free `describe()` that works for everyone." `@abstractmethod` is a required clause. Try to "hire" a shape (instantiate it) that hasn't signed every required clause, and HR (Python) rejects it on the spot. The concrete `describe()` is a company-wide perk every employee gets without re-implementing.

> 🔧 **Analogy — a wall socket standard.** An ABC is like the legal standard for electrical outlets in a country. The standard *mandates* the shape of the prongs (the abstract methods). Any manufacturer (subclass) is free to build whatever appliance they want, but it **must** present the mandated prong layout or it literally cannot plug in (cannot be instantiated). The standard guarantees interoperability without dictating what the appliance does.

#### Why this matters more than it looks

The ABC moves an error from "deep in production, at 2 a.m., when `describe()` calls a missing `area()`" to "the instant you try to create the object." **Failing early and loudly is one of the most valuable properties a design can have** — it shrinks the distance between a mistake and its discovery.

> 🚀 **Connection to your ML future — this is `nn.Module`.** Every neural network you write in PyTorch (Week 8+) will look like:
> ```python
> class MyNet(nn.Module):
>     def forward(self, x):     # you MUST implement this
>         ...
> ```
> `nn.Module` uses this exact "base class defines the contract; you fill in the required method" pattern. When you implement `forward()`, you are doing precisely what `Circle` does when it implements `area()`. Today's toy `Shape` and next month's neural net are the *same idea* at different scales. Recognizing that now means PyTorch won't feel like magic later — it'll feel familiar.

---

## S3 — Math: dot product, norm, distance

> Notation: vectors `a = [a₀, a₁, …, aₙ₋₁]` and `b = [b₀, …, bₙ₋₁]`, same length `n`. A vector is just an ordered list of numbers — but also an **arrow** in space, and switching between those two mental pictures is the whole skill.

### The dot product — two ways to see it

**Algebraically** — multiply matching components, sum the results:

```text
a · b  =  a₀·b₀ + a₁·b₁ + … + aₙ₋₁·bₙ₋₁     (always a single number, never a vector)
```

**Geometrically** — it measures how much two arrows point the *same way*:

```text
a · b  =  ‖a‖ · ‖b‖ · cos(θ)               (θ = angle between the arrows)
```

| Sign of `a · b` | Angle `θ` | Meaning | Picture |
|-----------------|-----------|---------|---------|
| `> 0` | `< 90°` | pointing *similarly* | → → |
| `= 0` | `= 90°` | **orthogonal** (unrelated) | → ↑ |
| `< 0` | `> 90°` | pointing *oppositely* | → ← |

> 💪 **Analogy — pushing a cart (physics: work = force · distance).** Imagine pushing a cart. If you push *exactly* in the direction it rolls, all your effort counts — big positive dot product. If you push at an angle, only part of your effort helps. If you push *perpendicular* to the motion (straight down on a flat cart), you do *zero* useful work — that's the orthogonal case, dot product = 0. The dot product literally measures "how much of vector A is contributing in the direction of vector B."

> 🧲 **Analogy — agreement score.** Think of two people rating 5 movies, each rating becoming a vector component. The dot product is high when they liked and disliked the *same* films (vectors aligned), near zero when their tastes are unrelated, and negative when one loves what the other hates. This is *exactly* how recommendation systems and search find "similar" things — and it's the seed of the next idea.

### Cosine similarity — the dot product, normalized

Raw dot products are inflated by length: a long vector dotted with anything gives a big number, even if the *directions* barely agree. To compare **direction only**, divide out the lengths:

```text
cosine_similarity(a, b)  =  (a · b) / (‖a‖ · ‖b‖)        →  always between -1 and +1
```

`+1` = identical direction, `0` = orthogonal, `-1` = opposite. Because it ignores magnitude, it answers "are these two things *about the same thing*?" regardless of scale.

> 🚀 **This is the single most important formula for your career.** When an LLM turns a sentence into an **embedding** (a vector of, say, 1,536 numbers capturing its meaning), "how similar are these two sentences?" becomes "what's the cosine similarity of their embeddings?" Every RAG system (Week 12), every semantic search, every "find related documents" feature is, at its core, **cosine similarity at massive scale**. You are learning the math of the thing you want to build a career on. Sit with this one.

### Norm (length) and distance

```text
‖a‖          =  sqrt(a₀² + a₁² + … + aₙ₋₁²)            # length of the arrow (Pythagoras, n-D)
dist(a, b)   =  ‖a − b‖  =  sqrt( Σ (aᵢ − bᵢ)² )        # straight-line gap between two points
```

> 📐 **Analogy — Pythagoras, scaled up.** In 2-D, `‖[3,4]‖ = sqrt(3²+4²) = 5` is just the hypotenuse of a 3-4-5 triangle. The norm is Pythagoras' theorem refusing to stop at two dimensions: in 50-D it's the same idea — square every leg, sum, square-root. Distance is the norm of the *difference* vector: "walk from A to B, how far did you go in a straight line?"

### Practice — do these by hand, *then* verify

The point of the math hour is the by-hand reps. Compute first, run second.

```python
import math
a = [1, 2, 3]
b = [4, 0, -1]

dot     = sum(x * y for x, y in zip(a, b))                     # = 1
norm_a  = math.sqrt(sum(x ** 2 for x in a))                    # = sqrt(14) ≈ 3.742
norm_b  = math.sqrt(sum(x ** 2 for x in b))                    # = sqrt(17) ≈ 4.123
cos_sim = dot / (norm_a * norm_b)                              # ≈ 0.0648  (nearly orthogonal!)
dist    = math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))   # = sqrt(25) = 5.0
```

By-hand drills:
1. `[2,1] · [1,2]` = ?  *(then: are they orthogonal? what's the angle's sign telling you?)*
2. `‖[3,4]‖` = ?  *(the classic — should be instant)*
3. Dot product of `[1,0]` and `[0,1]`? What does the answer say about their angle?
4. Distance between `[0,0]` and `[3,4]`?  Between `[1,1]` and `[4,5]`?
5. **Stretch:** two vectors both of length 10 have a dot product of 0. What's their cosine similarity, and what does that mean geometrically?

---

## S4 — Frontier: LLMs & your 3 directions

> **Today is reading, not coding** — ~2 h building mental models. Take notes in your own words; if you can't explain it simply, you haven't got it yet.

### Part 1 — "What is an LLM" (~45 min)

Watch/read Andrej Karpathy's **"Intro to Large Language Models"** (search the title; ~1 h talk, or a written summary if you're short on time).

Three takeaways to write in your own words, each with the analogy that makes it stick:

- **Next-token prediction.** An LLM is trained to do one absurdly simple thing billions of times: *predict the next word*. 🎮 *Analogy — phone autocomplete on steroids.* Your phone guesses the next word from the last few; an LLM guesses the next token from thousands of tokens of context, and from that single trick, fluent reasoning *emerges*.
- **Scale.** More data + more parameters + more compute → qualitatively (not just quantitatively) better behavior. 🍳 *Analogy — a kitchen.* A bigger kitchen with more ingredients and more cooks doesn't just make *more* food — past a threshold it can make *kinds* of dishes a tiny kitchen never could.
- **Emergent abilities.** Skills (translation, arithmetic, chain-of-thought reasoning) that *did not exist* in smaller models suddenly appear past a scale threshold. 💧 *Analogy — phase transition.* Water doesn't get "more solid" as it cools — at 0 °C it abruptly *becomes ice*, a different state. Abilities emerge in LLMs the same way: not gradually, but as thresholds are crossed.

### Part 2 — Your 3 career directions (~60 min)

These are *your* differentiators (industrial LLM + edge focus). Skim each and form one durable mental model:

| Direction | Search term | The one mental model to form |
|-----------|-------------|------------------------------|
| **vLLM / inference acceleration** 🥇 | *"vLLM PagedAttention explained"* | GPUs are expensive → you must serve one model to *many* users at once. vLLM batches requests using a **paged KV-cache** — exactly like an operating system's virtual memory, but for the model's attention memory. |
| **Edge multimodal (MobileCLIP)** | *"MobileCLIP Apple"* (read the abstract) | **CLIP** maps images and text into the *same* vector space so you can compare a photo to a caption with — yes — a dot product. **"Mobile"** = compress it small enough to run *on the device*, no cloud, for privacy and latency. |
| **Video understanding** | *"Video-LLaMA paper"* (abstract) | Video = a sequence of image frames (+ audio). The hard part isn't seeing one frame; it's **temporal reasoning** — understanding what *changed* across frames and why. |

> 📌 **Priority reminder (plan §1).** `vLLM/TensorRT-LLM` is **mainstream / near-required** — your top priority. Edge-multimodal is your **strategic differentiator** (fits your industrial/Germany aim). Video understanding is an **elective showcase**. Notice that all three share one DNA: *doing more with less compute* — the defining pressure of the whole field.

### Part 3 — Reflection (~15 min)

Write a few sentences in a study journal:

> *Of the 3 directions, which connects most to my engineering background, and why?*

No right answer — this seeds where you'll point your Week-13 capstone.

---

## 🧠 Cheat-sheet

```python
# INHERITANCE
class Child(Parent):
    def __init__(self, ...):
        super().__init__(...)             # ALWAYS — sets up the parent's part
    def method(self):
        return super().method() + "extra" # EXTEND (vs replace)

# MRO — the fixed search order; super() follows THIS, not "the parent"
Child.__mro__            # (Child, ..., object)

# ABSTRACT BASE CLASS — enforce a contract, fail early
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def must_implement(self): ...         # subclass is FORCED to define this
    def shared(self): ...                 # concrete: free for all subclasses

# POLYMORPHISM = same call, type-specific behavior; deletes if/elif type-ladders
```

| Term | One-liner | Analogy |
|------|-----------|---------|
| **Inheritance** | child reuses + extends parent | master blueprint → customized houses |
| **`super()`** | proxy to the *next class in the MRO* | phone the foundation crew first |
| **Override (extend)** | redefine, but call `super()` too | add a bow to an already-wrapped gift |
| **MRO** | fixed left-to-right ancestor search order | the org chart of "who do I ask?" |
| **Diamond problem** | shared ancestor reached by 2 paths | C3 makes the baton cross the line once |
| **Polymorphism** | one interface, many behaviors | universal power socket |
| **Duck typing** | capability matters, not type | "quacks like a duck → it's a duck" |
| **ABC** | base class that mandates methods | job description / outlet standard |
| **Dot product** | `Σ aᵢbᵢ`; sign ↔ angle | useful work pushing a cart |
| **Cosine similarity** | dot product ÷ lengths → direction-only | "are these about the same thing?" |

---

## ⚠️ Common pitfalls (recap)

1. **Forgetting `super().__init__()`** → half-built object, `AttributeError` later. *If a subclass defines `__init__`, it almost always must call `super().__init__()`.*
2. **Replacing when you meant to extend** → you silently drop the parent's setup/logic. Ask: "do I still want what the parent did?" If yes, call `super()`.
3. **Reaching for `isinstance` ladders** → that's polymorphism asking to be used. Let each type own its behavior.
4. **Using inheritance for a "has-a" relationship** → e.g. `class Car(Engine)`. A car *has* an engine, it *is not* one. (Day 4 fixes this instinct.)
5. **Defining `__eq__` but forgetting `__hash__`** → object becomes unhashable in sets/dicts. (More on Day 3.)
6. **Expecting `super()` to mean "the parent"** → in multiple inheritance it means "the next in the MRO," possibly a *sibling*. Print `__mro__` when surprised.

➡️ **Next:** open [`HOMEWORK.md`](./HOMEWORK.md) and build the Animal hierarchy + Shape ABC. As you write it, narrate each choice out loud: "Is this is-a or has-a? Am I extending or replacing? What's the MRO of `Parrot`?"
