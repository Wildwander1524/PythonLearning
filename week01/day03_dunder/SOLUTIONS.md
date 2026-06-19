# ✅ Day 3 — SOLUTIONS

> After a real attempt only.

## Reference — `vector2d.py`
```python
import math

class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"          # round-trips

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented                        # let Python try the reflected ==
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)   # NEW object
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, k):                                # scalar
        return Vector2D(self.x * k, self.y * k)

    def __abs__(self):
        return math.hypot(self.x, self.y)                # = √(x²+y²) = the D2 NORM
    def dot(self, other):
        return self.x * other.x + self.y * other.y       # = the D2 DOT PRODUCT

    def __getitem__(self, i):
        if i == 0: return self.x
        if i == 1: return self.y
        raise IndexError("Vector2D index out of range")  # lets iteration detect the end
    def __iter__(self):
        yield self.x                                     # generator = iterator for free
        yield self.y

    # Stretch:
    def __rmul__(self, k): return self * k               # 2 * v
    def __neg__(self): return Vector2D(-self.x, -self.y)
    def __hash__(self): return hash((self.x, self.y))    # safe only if treated as immutable
```
> Note `__abs__` uses `math.hypot(x, y)` — the *correct* use of hypot (Euclidean length of a
> 2-vector), in contrast to Day 2 where `hypot` was wrongly substituted for Heron's formula.
> Same function, right tool here, wrong tool there — the lesson is *match the formula to the job*.

## RECALL answers
**Spaced:** S1 it protects an invariant (value only changes through controlled methods); omit the
`@x.setter`. S2 `(Parrot, Bird, Animal, object)`. S3 `cos = a·b/(‖a‖‖b‖)`; removes magnitude so
it compares meaning/direction not length.

**A:** Python defines a *protocol* (special methods); syntax dispatches to it. One rule learned
once works on every type including yours → consistency, and your objects interoperate with
built-in functions and operators.

**B** 1. `__repr__` always (REPL/debugger/containers); `__str__` falls back to `__repr__`, never
the reverse. 2. Defining `__eq__` sets `__hash__=None` (equal must hash equal; Python can't
verify). Immutable → add `__hash__`; mutable → leave unhashable. 3. Define `__iter__` (best a
generator) **or** define `__getitem__` and let Python index `0,1,2…` until `IndexError`.
4. So Python can try `other.__eq__(self)` (reflected) — maybe the other type knows how to
compare; `False` would lie. 5. A `yield`-function that *is* an iterator; Python writes
`__next__`/`StopIteration` for you → less code, fewer bugs.

**C · Predict:** prints `3 3 True`. It **broke the golden rule** — `__add__` mutated `self` and
returned it, so `a` changed and `c is a`. `a + b` must return a *new* `V` and leave `a` alone.

**D · Fraction:**
```python
class Fraction:
    def __init__(self, num, den): self.num, self.den = num, den
    def __repr__(self): return f"Fraction({self.num}, {self.den})"
    def __eq__(self, o):
        if not isinstance(o, Fraction): return NotImplemented
        return self.num * o.den == o.num * self.den          # cross-multiply
    def __add__(self, o):
        return Fraction(self.num*o.den + o.num*self.den, self.den*o.den)   # new object
# Fraction(1,2) == Fraction(2,4)  → True ; Fraction(1,2)+Fraction(1,3) == Fraction(5,6) → True
```

**E · Math:** 1. `[[1,3,5],[2,4,6]]`, shape `2×3`. 2. `[1·10+2·20, 3·10+4·20] = [50, 110]`.
3. `[0·1+(-1)·0, 1·1+0·0] = [0, 1]` — `[1,0]` (pointing east) rotated 90° CCW to `[0,1]` (north). ✅

## Concept-check answers (homework)
1. `a + b` must not consume its operands (`5+3` doesn't change `5`); returning a new object keeps
   `a`,`b` reusable and matches every built-in numeric type. 2. `x` then `y`; the generator
   function *ends* after the second `yield`, which raises `StopIteration` automatically. 3. It
   prints `[<...Vector2D object at 0x...>]` — containers use `__repr__`, so a missing one makes
   debugging lists/log output useless.

> 📝 Record: which dunder did you forget existed? That's a Day-4/6 re-test candidate.
