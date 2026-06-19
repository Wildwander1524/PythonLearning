# Week 1 · Day 2 — Part B: Shape ABC + polymorphism
#
# Day 1 callback: BankAccount raised ValueError for invalid inputs so callers
# found out immediately when something was wrong. An ABC does the same thing at
# the *class* level: you find out the moment you try to instantiate an
# incomplete subclass, not buried deep in a runtime crash later.

# ── Imports ───────────────────────────────────────────────────────────────────
from abc import ABC, abstractmethod
import math

# ── Abstract base class ───────────────────────────────────────────────────────


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """Every concrete shape MUST implement this."""
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """Every concrete shape MUST implement this."""
        ...

    def describe(self) -> str:
        # Concrete — shared by all shapes; do NOT reimplement in subclasses.
        # (This is the "free company perk" from the job-contract analogy.)
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


# ── Concrete shapes ───────────────────────────────────────────────────────────


class Circle(Shape):
    def __init__(self, radius: float):
        # TODO: store radius
        self.radius = radius

    def area(self) -> float:
        # TODO: π * r²  (use math.pi)
        return math.pi * self.radius**2 / 2

    def perimeter(self) -> float:
        # TODO: 2 * π * r
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        # TODO: store width and height
        self.w = w
        self.h = h

    def area(self) -> float:
        # TODO: w * h
        return self.w * self.h

    def perimeter(self) -> float:
        # TODO: 2 * (w + h)
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        # TODO: store the three side lengths
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                "Cannot form a triangle: sum of any two sides must be greater than the third"
            )
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        # Heron's formula: s = (a+b+c)/2 ; area = sqrt(s*(s-a)*(s-b)*(s-c))
        # TODO: implement
        s = (self.a + self.b + self.c) / 2
        return math.hypot(s - self.a, s - self.b, s - self.c)

    def perimeter(self) -> float:
        # TODO: a + b + c
        s = (self.a + self.b + self.c) / 2
        return self.a + self.b + self.c


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


# ── Polymorphic helper ────────────────────────────────────────────────────────


def total_area(shapes: list) -> float:
    """Return the sum of areas for any list of Shape objects.

    Rules:
    - Zero isinstance() checks allowed — let polymorphism do the work.
    - The socket doesn't care what's plugged in; it just calls .area().
    """
    # TODO: one-liner using sum() and a generator expression
    return sum(shape.area() for shape in shapes)


# ── Quick smoke-test (run this file directly to check your work) ──────────────
if __name__ == "__main__":
    shapes = [Circle(1), Rectangle(2, 3), Triangle(3, 4, 5)]
    for s in shapes:
        print(s.describe())
    print(f"Total area: {total_area(shapes):.4f}")

    # Confirm instantiating the ABC itself raises TypeError
    try:
        Shape()
        print("ERROR: Shape() should have raised TypeError")
    except TypeError as e:
        print(f"Good — Shape() blocked: {e}")
