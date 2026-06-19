# 📋 Day 2 Review — `animals.py` + `shapes.py`

> **Week 1 · Day 2 (Tue 2026-06-18)** — Inheritance, Polymorphism & ABCs
> **Verdict:** 🟡 **18 / 22 tests passing.** Solid structure — ABC, polymorphism, and most of the animal hierarchy are correct. Four fixable bugs below.

---

## ✅ Test results

```text
PASS  dog_speak
PASS  cat_speak_extended
PASS  bird_speak_contains_tweet
PASS  parrot_is_bird
PASS  parrot_is_animal
PASS  parrot_speak_after_learn
FAIL  dog_fetch              →  "ball" not in output (item param ignored)
PASS  cat_purr
PASS  bird_fly
PASS  mro_parrot_first
PASS  mro_bird_before_animal
PASS  shape_direct_instantiation
PASS  incomplete_subclass_raises
FAIL  circle_area            →  got π/2, expected π  (÷2 typo)
PASS  circle_perimeter
PASS  rect_area
PASS  rect_perimeter
FAIL  triangle_area          →  got 3.74, expected 6.0  (math.hypot ≠ Heron)
PASS  triangle_perimeter
PASS  circle_describe_contains_area
FAIL  total_area_mixed_shapes  ← cascades from circle_area bug
PASS  total_area_empty

18/22 tests passed
```

---

## 🎉 What you got right

| Concept | Why it's correct |
|---------|-----------------|
| **`Animal.__init__` + all `super()` calls** | Foundation-crew rule followed in every subclass |
| **`Cat.speak` — EXTEND flavor** | Calls `super().speak()` and wraps it; correct pattern |
| **MRO chain for `Parrot`** | `Parrot → Bird → Animal → object`; both `isinstance` checks prove the chain |
| **`Shape` ABC** | Contract enforces `area()`/`perimeter()`; `describe()` concrete and inherited for free |
| **`total_area`** | Perfect one-liner — zero `isinstance` checks, pure polymorphism |
| **`Triangle.__init__` validation** | Triangle-inequality check is a nice bonus — fails early and loudly |
| **Stretch goals** | `SwimMixin` (cooperative `**kwargs`), `Square(Rectangle)`, `Penguin.fly(NotImplementedError)` — all correct |
| **Concept checks** | All three answers are essentially right |

---

## 🔧 Issues to fix

### 1. 🔴 `Circle.area` — semicircle formula (1 failing test)

```python
# ❌ current — divides by 2 (that's a semicircle)
return math.pi * self.radius ** 2 / 2

# ✅ fix
return math.pi * self.radius ** 2
```

---

### 2. 🔴 `Triangle.area` — wrong function (2 failing tests, incl. total_area)

`math.hypot(s-a, s-b, s-c)` computes a Euclidean distance — nothing to do with Heron's formula.
For a 3-4-5 triangle it returns `≈3.74` instead of `6.0`.

```python
# ❌ current
return math.hypot(s - self.a, s - self.b, s - self.c)

# ✅ Heron's formula
s = (self.a + self.b + self.c) / 2
return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
```

---

### 3. 🔴 `Dog.fetch` — ignores the `item` parameter (1 failing test)

```python
# ❌ current — item is never used; "ball" is not in the output
return f"{super().speak()},and touch your fingers!"

# ✅ fix
return f"{self.name} fetches the {item}!"
```

---

### 4. 🟡 `Parrot.__init__` — MRO skip with `super(Bird, self)`

```python
# ❌ current — jumps over Bird in the MRO entirely
super(Bird, self).__init__(name, "Squawk")

# ✅ correct — call Bird, then override the sound
super().__init__(name)   # → Bird.__init__ → Animal.__init__ (sets sound="Tweet")
self.sound = "Squawk"    # override after the chain runs
```

`super(Bird, self)` skips `Bird.__init__` — it worked by accident because `Animal` still set
`sound`, but it violates the foundation-crew rule (same lesson as forgetting `super()` in Day 1).
`Penguin.__init__` has the same pattern — apply the same fix there.

---

## 🟢 Style / polish

| Location | Issue |
|----------|-------|
| `Cat.purr` | Hardcodes `"Whiskers"` — use `self.name` so any cat name works |
| `Parrot.speak` | Always appends phrase even when empty → `"... — !"`. Guard with `if self._learned_phrase:` |
| `animals.py:91` | Dead `pass` after `self._learned_phrase = phrase` in `learn()` |
| `shapes.py:82` | Orphaned `s = (...)` line in `Triangle.perimeter` (copy-paste leftover) |
| `Bird.speak` | Is a REPLACE — mark it `# REPLACE` as the homework asks |

---

## 🎯 Action items

- [ ] `Circle.area` → remove `/ 2` → reach 19/22
- [ ] `Triangle.area` → replace `math.hypot` with Heron's formula → reach 21/22
- [ ] `Dog.fetch` → use `item` parameter → reach **22/22**
- [ ] `Parrot.__init__` (and `Penguin`) → `super().__init__(name)` then `self.sound = "Squawk"`
- [ ] `Parrot.speak` → guard `if self._learned_phrase:`
- [ ] `Cat.purr` → use `self.name`
- [ ] Remove dead `pass` + orphaned `s` line + add `# REPLACE` to `Bird.speak`

> Severity legend: 🔴 bug / breaks tests · 🟡 should-fix (correctness-adjacent) · 🟢 polish

Fix the three 🔴 items, re-run `python test_day02.py`, and you're done with Day 2. ✅
