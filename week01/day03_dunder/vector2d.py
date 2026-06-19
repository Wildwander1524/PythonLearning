# Week 1 · Day 3 — Vector2D: dunder methods & the data model
#
# Day 2 callback: you computed dot products and norms by hand in S3 math.
# Today those same formulas become __abs__ and dot() — the math on paper
# becomes methods on an object. PyTorch tensors do the exact same thing
# via @ and .norm(). You are not doing separate exercises; you are building
# the same thing at increasing scale.

import math


class Vector2D:
    """2D vector that behaves like a native Python numeric type."""

    # ── Construction & display ─────────────────────────────────────────────

    def __init__(self, x: float, y: float):
        # TODO: store x and y as instance attributes
        pass

    def __repr__(self) -> str:
        # TODO: return 'Vector2D(3, 4)'  — round-trip format (valid Python to recreate it)
        # Day 3 rule: __repr__ is for the developer, always define it first.
        pass

    def __str__(self) -> str:
        # TODO: return a friendlier string like '(3, 4)'
        # (If you leave this out Python falls back to __repr__ — that's fine too.)
        pass

    # ── Equality ──────────────────────────────────────────────────────────

    def __eq__(self, other) -> bool:
        # TODO: return True only if other is a Vector2D with the same x and y.
        # Return NotImplemented (not False!) if other is an unknown type —
        # that tells Python "I don't know; try the other operand's __eq__."
        pass

    def __hash__(self):
        # Defining __eq__ makes the object unhashable by default (the coat-check rule).
        # We restore it here so vectors can live in sets/dicts.
        # Safe because we treat Vector2D as immutable (we never change x or y in-place).
        # TODO: return hash of a tuple of the components
        pass

    # ── Arithmetic ────────────────────────────────────────────────────────

    def __add__(self, other: "Vector2D") -> "Vector2D":
        # TODO: return a NEW Vector2D whose components are the element-wise sum.
        # Golden rule: never mutate self — like combining two recipes into a third.
        pass

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        # TODO: return a NEW Vector2D — element-wise difference
        pass

    def __mul__(self, scalar: float) -> "Vector2D":
        # TODO: scalar multiply — return a NEW Vector2D with each component × scalar
        # This handles v * 2.
        pass

    def __rmul__(self, scalar: float) -> "Vector2D":
        # Reflected multiply — handles 2 * v.
        # Python calls this when int.__mul__(2, v) returns NotImplemented.
        # TODO: delegate to __mul__ (one line)
        pass

    def __neg__(self) -> "Vector2D":
        # TODO: return Vector2D(-self.x, -self.y)  so that -v works
        pass

    # ── Magnitude & dot product ───────────────────────────────────────────

    def __abs__(self) -> float:
        # TODO: return the magnitude (Euclidean norm) — sqrt(x² + y²)
        # Day 2 callback: this IS ‖v‖ from S3 math. Use math.sqrt or math.hypot.
        pass

    def dot(self, other: "Vector2D") -> float:
        # TODO: return the dot product x1*x2 + y1*y2
        # Day 2 callback: this IS the dot product formula from S3 math.
        pass

    # ── Indexing & iteration ──────────────────────────────────────────────

    def __len__(self) -> int:
        # A 2D vector always has 2 components.
        return 2

    def __getitem__(self, index: int) -> float:
        # TODO: return self.x for index 0, self.y for index 1.
        # Raise IndexError for anything else — this is how for-loops know to stop
        # if they use the old __getitem__ iteration protocol.
        pass

    def __iter__(self):
        # TODO: yield x, then yield y  (generator shortcut — the cassette-tape trick)
        # This enables: for c in v, list(v), x, y = v  — all at once.
        pass


# ── Concept-check answers (fill in after finishing the implementation) ────────

# Q1: Why must __add__ return a new Vector2D instead of modifying self.x/self.y?
# A1: TODO

# Q2: You defined __iter__ with yield. What two values does it produce,
#     and how does Python know to stop?
# A2: TODO

# Q3: If you delete __repr__, what does [Vector2D(3, 4)] print, and why is
#     that bad for debugging?
# A3: TODO
