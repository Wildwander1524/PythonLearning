# Week 1 · Day 3 — Vector2D: dunder methods & the data model
#
# Day 2 callback: you computed dot products and norms by hand in S3 math.
# Today those same formulas become __abs__ and dot() — the math on paper
# becomes methods on an object. PyTorch tensors do the exact same thing
# via @ and .norm(). You are not doing separate exercises; you are building
# the same thing at increasing scale.

import math

class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.den})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.num * other.den == other.num * self.den

    def __hash__(self):
        return hash(self.num / self.den)

    def __add__(self, other: object) -> object:
        return Fraction((self.num * other.den + other.num * self.den), self.den * other.den)



class Vector2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector2D({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other) -> object:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> object:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self) -> object:
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar: float) -> object:
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> object:
        return Vector2D(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __len__(self):
        return 2

    def __getitem__(self, item):
        return (self.x, self.y)[item]

    def __iter__(self):
        yield self.x
        yield self.y

    def dot(self, other: object) -> float:
        return self.x * other.x + self.y * other.y


if __name__ == '__main__':
    v, w = Vector2D(3, 4), Vector2D(1, 2)

    print(repr(v))  # 'Vector2D(3, 4)'      (round-trips)
    print(v == Vector2D(3, 4))  # True
    print(v + w)  # Vector2D(4, 6)        (NEW object — v unchanged)
    print(v - w)  # Vector2D(2, 2)
    print(v * 2)  # Vector2D(6, 8)
    print(abs(v))  # 5.0                   = ‖v‖, the D2 NORM
    print(v.dot(w))  # 11                    = v·w, the D2 DOT PRODUCT
    print(v[0], v[1])  # 3, 4
    x, y = v  # unpacking via iteration
    print(list(v))  # [3, 4]



# ── Concept-check answers (fill in after finishing the implementation) ────────

# Q1: Why must __add__ return a new Vector2D instead of modifying self.x/self.y?
# A1: Avoid hash collisions 

# Q2: You defined __iter__ with yield. What two values does it produce,
#     and how does Python know to stop?
# A2: It essentially created a generator, as he adheres to the lazy principle: proceed step by step, pausing after each one

# Q3: If you delete __repr__, what does [Vector2D(3, 4)] print, and why is
#     that bad for debugging?
# A3: Printing an address makes it hard to visually identify the issue during debugging, reducing efficiency.
