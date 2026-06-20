# Week 1 · Day 2 — Part B: Shape ABC + polymorphism
#
# Day 1 callback: BankAccount raised ValueError for invalid inputs so callers
# found out immediately when something was wrong. An ABC does the same thing at
# the *class* level: you find out the moment you try to instantiate an
# incomplete subclass, not buried deep in a runtime crash later.

# ── Imports ───────────────────────────────────────────────────────────────────
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"AreaArea={self.area()},PerimeterArea={self.perimeter()}"


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return math.pi * self.radius * 2


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                "Cannot form a triangle: sum of any two sides must be greater than the third"
            )
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Rectangle(Shape):

    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return (self.w + self.h) * 2


def total_area(shapes):
    return sum([shape.area() for shape in shapes])


# ── Quick smoke-test (run this file directly to check your work) ──────────────

if __name__ == "__main__":

    # My Result : 3.141592653589793
    print(Circle(1).area())

    # My Result : 6.0
    print(Triangle(3, 4, 5).area())

    # My Result : 9.141592653589793
    print(total_area([Circle(1), Rectangle(2, 3)]))
