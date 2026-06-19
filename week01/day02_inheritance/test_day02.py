# Week 1 · Day 2 — test harness
#
# Day 1 callback: same style as test_bank_account.py — one focused assertion per
# test, clear names, no pytest needed (just run: python test_day02.py).

import sys
import math

# ── Import the modules you built ──────────────────────────────────────────────
from animals import Animal, Dog, Cat, Bird, Parrot
from shapes import Shape, Circle, Rectangle, Triangle, total_area


# ── Test helpers (copied from Day 1 harness) ──────────────────────────────────

passed = 0
failed = 0

def check(name: str, condition: bool) -> None:
    global passed, failed
    if condition:
        print(f"PASS  {name}")
        passed += 1
    else:
        print(f"FAIL  {name}")
        failed += 1

def expect_error(name: str, exc_type: type, fn) -> None:
    global passed, failed
    try:
        fn()
        print(f"FAIL  {name}  →  expected {exc_type.__name__}, got nothing")
        failed += 1
    except exc_type:
        print(f"PASS  {name}")
        passed += 1
    except Exception as e:
        print(f"FAIL  {name}  →  expected {exc_type.__name__}, got {type(e).__name__}: {e}")
        failed += 1


# ── Part A: animals ───────────────────────────────────────────────────────────

# Basic speak
check("dog_speak", Dog("Rex").speak() == "Rex says Woof")
check("cat_speak_extended", "then ignores you" in Cat("Whiskers").speak())
check("bird_speak_contains_tweet", "Tweet" in Bird("Tweety").speak())

# Inheritance chain for Parrot
polly = Parrot("Polly")
check("parrot_is_bird",   isinstance(polly, Bird))
check("parrot_is_animal", isinstance(polly, Animal))

# Parrot.learn + speak
polly.learn("Hello")
check("parrot_speak_after_learn", "Hello" in polly.speak())

# Fetch and purr
check("dog_fetch",  "ball" in Dog("Rex").fetch("ball"))
check("cat_purr",   "purr" in Cat("Whiskers").purr().lower())
check("bird_fly",   "100" in Bird("Tweety").fly(100))

# MRO order: Parrot → Bird → Animal → object
mro = Parrot.__mro__
check("mro_parrot_first", mro[0] is Parrot)
check("mro_bird_before_animal", mro.index(Bird) < mro.index(Animal))


# ── Part B: shapes ────────────────────────────────────────────────────────────

# Shape ABC cannot be instantiated directly
expect_error("shape_direct_instantiation", TypeError, lambda: Shape())

# A subclass that forgets area() also raises TypeError
def _make_bad_shape():
    class BadShape(Shape):
        def perimeter(self): return 0.0
    BadShape()
expect_error("incomplete_subclass_raises", TypeError, _make_bad_shape)

# Individual shapes
c = Circle(1)
check("circle_area",      abs(c.area() - math.pi) < 1e-9)
check("circle_perimeter", abs(c.perimeter() - 2 * math.pi) < 1e-9)

r = Rectangle(3, 4)
check("rect_area",      r.area() == 12.0)
check("rect_perimeter", r.perimeter() == 14.0)

t = Triangle(3, 4, 5)
check("triangle_area",      abs(t.area() - 6.0) < 1e-9)
check("triangle_perimeter", t.perimeter() == 12.0)

# describe() is inherited — should work without reimplementing
check("circle_describe_contains_area", "Area=" in Circle(2).describe())

# Polymorphic total_area
got = total_area([Circle(1), Rectangle(2, 3)])
exp = math.pi * 1 ** 2 + 2 * 3   # ≈ 9.1416
check("total_area_mixed_shapes", abs(got - exp) < 1e-6)

# total_area with empty list
check("total_area_empty", total_area([]) == 0.0)


# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{passed}/{passed + failed} tests passed")
if failed:
    sys.exit(1)
