# Week 1 · Day 3 — test harness for Vector2D
#
# Day 1/2 callback: same check() / expect_error() harness as before.
# Run with: python test_vector2d.py

import sys
import math
from vector2d import Vector2D


# ── Test helpers ──────────────────────────────────────────────────────────────

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


# ── Fixtures ──────────────────────────────────────────────────────────────────

v = Vector2D(3, 4)
w = Vector2D(1, 2)


# ── Display ───────────────────────────────────────────────────────────────────

check("repr_round_trip",  repr(v) == "Vector2D(3, 4)")
check("str_is_friendly",  "3" in str(v) and "4" in str(v))


# ── Equality & hashing ────────────────────────────────────────────────────────

check("eq_same_components",      Vector2D(3, 4) == Vector2D(3, 4))
check("eq_different_components", Vector2D(3, 4) != Vector2D(1, 2))
check("eq_unknown_type",         Vector2D(3, 4) != "not a vector")  # must not crash

# hashable — can live in a set (requires __hash__)
check("hashable_in_set", len({Vector2D(1, 2), Vector2D(1, 2), Vector2D(3, 4)}) == 2)


# ── Arithmetic ────────────────────────────────────────────────────────────────

check("add_components",   v + w == Vector2D(4, 6))
check("sub_components",   v - w == Vector2D(2, 2))
check("mul_scalar",       v * 2 == Vector2D(6, 8))
check("rmul_scalar",      2 * v == Vector2D(6, 8))   # reflected: 2 * v
check("neg",              -v    == Vector2D(-3, -4))

# Golden rule: + must not mutate v
v_before_x, v_before_y = v[0], v[1]
_ = v + w
check("add_no_mutation", v[0] == v_before_x and v[1] == v_before_y)


# ── Magnitude & dot product ───────────────────────────────────────────────────

check("abs_magnitude",    abs(Vector2D(3, 4)) == 5.0)         # the 3-4-5 triangle
check("abs_unit_vector",  abs(Vector2D(1, 0)) == 1.0)
check("dot_product",      Vector2D(3, 4).dot(Vector2D(1, 2)) == 11)   # 3·1 + 4·2
check("dot_orthogonal",   Vector2D(1, 0).dot(Vector2D(0, 1)) == 0)    # perpendicular → 0


# ── Indexing ──────────────────────────────────────────────────────────────────

check("getitem_0",    v[0] == 3)
check("getitem_1",    v[1] == 4)
expect_error("getitem_out_of_range", IndexError, lambda: v[2])


# ── Iteration ─────────────────────────────────────────────────────────────────

check("list_conversion",  list(v) == [3, 4])
check("unpacking",        (lambda x, y: x == 3 and y == 4)(*v))
check("for_loop_sum",     sum(c for c in v) == 7)
check("len_is_2",         len(v) == 2)


# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{passed}/{passed + failed} tests passed")
if failed:
    sys.exit(1)
