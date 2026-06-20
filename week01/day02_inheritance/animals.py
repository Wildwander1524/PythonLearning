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
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"


class Dog(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Woof")

    def speak(self) -> str:
        return f"{super().speak()}"

    def fetch(self, item) -> str:
        return f"{self.name} fetches the {item}!"


class Cat(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Meow")

    # EXTEND
    def speak(self) -> str:
        return f"{super().speak()},then ignores you"

    def purr(self) -> str:
        return f"{self.name} purrs contentedly"


class Bird(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Tweet")

    # EXTEND
    def speak(self) -> str:
        return f"{super().speak()},then flies around you!"

    def fly(self, altitude: int) -> str:
        return f"{self.name} flies at {int(altitude)} m"


class Parrot(Bird):

    def __init__(self, name: str):
        super().__init__(name)
        self.sound = "Squawk"

    def learn(self, phrase: str) -> str:
        self._phrase = phrase

    def speak(self) -> str:
        base_speak = super().speak()
        if hasattr(self, "_phrase"):
            return f"{self.name} says {self._phrase}'"
        return base_speak


class Penguin(Bird):

    # TODO: replace fly()
    def __init__(self, name: str):
        super().__init__(name, "pengpeng")
        self.sound = "pengpeng"

    def fly(self, altitude: int) -> str:
        raise NotImplementedError("penguins can't fly")


# ── Quick smoke-test (run this file directly to check your work) ──────────────

if __name__ == "__main__":

    # My Result : Parrot => Bird => Animal => Object
    print(Parrot.__mro__)


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

# Q1: You used super(Bird, self) before and it "worked." Explain precisely what it did to the MRO and why it was wrong anyway
# A1: when I used super(Bird, self),the start point in MRO changed from Parrot to Bird,
# then go on as it' ruler: Children precede Parents,and fixed left to right

# Q2: Why does Bird come before Animal in Parrot.__mro__?
# A3: Children precede Parents,and fixed left to right

# Q3: Why is total_area better than an isinstance ladder?
# A3: more flexible,makes debugging easier
