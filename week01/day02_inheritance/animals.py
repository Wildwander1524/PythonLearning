# Week 1 · Day 2 — Part A: Animal hierarchy
#
# Day 1 callback: In BankAccount you stored _balance as a private attribute and
# validated inputs in methods. Today's pattern is the same — Animal.__init__ is
# the "foundation crew" that sets the attributes every subclass relies on.
# Miss it (like forgetting _balance setup) and the object is half-built.

# ── Imports ──────────────────────────────────────────────────────────────────
# (nothing needed here — no ABC for the animal tree)


# ── Base class ────────────────────────────────────────────────────────────────


class Animal:
    def __init__(self, name: str, sound: str):
        # TODO: store name and sound as instance attributes
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        # TODO: return e.g. "Rex says Woof"
        return f"{self.name} says {self.sound}"


# ── Subclasses (level 1) ──────────────────────────────────────────────────────


class Dog(Animal):
    def __init__(self, name: str):
        # TODO: call super().__init__ with the right sound hardcoded
        super().__init__(name, "Woof")

    def fetch(self, item: str) -> str:
        # TODO: return e.g. "Rex fetches the ball!"
        return f"{super().speak()},and touch your fingers!"


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Meow")

    def speak(self) -> str:  # EXTEND — call super().speak() and add to it
        # TODO: get the base string from super(), then add "... then ignores you"
        return f"{super().speak()}... then ignores you"

    def purr(self) -> str:
        # TODO: return e.g. "Whiskers purrs..."
        return f"Whiskers purrs..."


class SwimMixin:

    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def swim(self):
        return f"{self.name} is swimming!"


class Bird(Animal):
    def __init__(self, name: str):
        # TODO: call super().__init__ with the right sound
        super().__init__(name, "Tweet")

    def speak(self) -> str:
        # TODO: your choice — EXTEND or REPLACE. Mark with a comment.
        return f"{self.name} says {self.sound * 3}."

    def fly(self, altitude: int) -> str:
        # TODO: return e.g. "Tweety flies at 100 m"
        return f"{self.name} flies at {altitude} m"


# ── Subclass (level 2) ────────────────────────────────────────────────────────


class Parrot(Bird):
    """Multi-level: Parrot → Bird → Animal."""

    def __init__(self, name: str):
        # TODO: call super().__init__ — sound is hardcoded to "Squawk"
        # Note: Bird.__init__ only takes a name, so figure out who sets the sound
        super(Bird, self).__init__(name, "Squawk")
        self._learned_phrase: str = ""  # starter: where the learned phrase lives

    def learn(self, phrase: str) -> None:
        # TODO: store the phrase so speak() can use it
        self._learned_phrase = phrase
        pass

    def speak(self) -> str:  # EXTEND
        # TODO: call super().speak() to get "Polly says Squawk",
        # then append " — <phrase>" if a phrase has been learned
        return f"{super().speak()} — {self._learned_phrase}!"


class Penguin(Bird):

    # TODO: replace fly()
    def __init__(self, name: str):
        super(Bird, self).__init__(name, "pengpeng")

    def fly(self, altitude: int) -> str:
        raise NotImplementedError("penguins can't fly")


# ── MRO inspection ────────────────────────────────────────────────────────────
# TODO: uncomment and run this block, then fill in the comment explaining each entry.

# print(Parrot.__mro__)
# Expected: (<class 'Parrot'>, <class 'Bird'>, <class 'Animal'>, <class 'object'>)
#
# Parrot   — most specialised; searched first (children before parents)
# Bird     — TODO: explain why Bird comes before Animal
# Animal   — TODO: explain what Animal contributes and why it's here
# object   — TODO: explain what object is and why every class chain ends here


# ── Concept-check answers (fill these in after finishing the homework) ─────────

# Q1: You removed super().__init__() from Dog. What error appears and why?
# A1: TODO:After removing super().__init__(), the initialization happens directly via Dog.__init__(self, name) when you call d = Dog("Rex"). At that point, the object d only has a name attribute. If you then call d.speak, an AttributeError will occur.

# Q2: In Parrot.__mro__, why does Bird appear before Animal?
# A2: TODO:Because the MRO lookup order is left‑to‑right ancestor – that is, it first searches the parent classes from left to right; if not found, it goes up to the parent's parent, again from left to right, until it finds the method or reaches object. If it still isn't found, an AttributeError is raised.


# Q3: Why is total_area (in shapes.py) better than if isinstance(...) ladders?
#     What happens to each when you add a new Pentagon shape?
# A3: TODO:The latter approach better follows the "duck typing" principle. When adding a new Pentagon shape, the former approach only requires creating a new Pentagon class and adding an area method, while the latter requires modifying the existing source code – obviously the latter is more troublesome.
