# 📘 Day 4 — Composition, `@dataclass` & Design Judgment

> **Week 1 · Thu 2026-06-19** · Curriculum: Python OOP · Math: matrix×matrix, identity, inverse
> Days 2–3 gave you *mechanisms* (inheritance, dunders). **Today is judgment** — *when* to use
> which. The headline — **"prefer composition over inheritance"** — is one of the most-repeated
> rules in software engineering; tonight you'll understand *why* in your bones.

## 🎯 Objectives & mastery bar
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Choose composition vs inheritance | **Analyze** | you justify each with the is-a/has-a test |
| Use `@dataclass` (incl. mutable-default safety) | Apply | you write one and spot the `= []` bug unprompted |
| Read/write type hints; know they're not enforced | Understand | you explain "signage, not guards" |
| Math: matrix×matrix, identity, inverse | Understand | you apply the domino rule and predict `A·I` |

## 🔁 Spaced callbacks (cold, first — re-tests D2 + D3)
C1 (D2) what does an **ABC** guarantee, and when does it reject a bad subclass? C2 (D3) you
defined `__eq__`; why won't your object go in a `set`, and what's the fix? C3 (D3) what must
`a + b` return?

---

## S1 — Composition vs inheritance

| Relationship | Test | Mechanism | Example |
|--------------|------|-----------|---------|
| **Inheritance** | "A *is a* B" | subclassing | `Dog` is an `Animal` |
| **Composition** | "A *has a* B" | hold it as an attribute | `Car` has an `Engine` |

```python
class Car:
    def __init__(self):
        self.engine = Engine()          # HAS-A: the Car owns an Engine
    def start(self):
        return self.engine.start()      # and delegates to it
```

> 🧱 **Lego vs a cast statue.** Composition = Lego: independent bricks snap together; swap the
> engine without touching the rest. Inheritance = one cast statue: to change the arm you re-cast
> the whole thing, and every copy changes too. Software changes constantly → reach for Lego.

### Why "prefer composition" — the fragile base class problem
Inheritance couples a child to the parent's *internals*. Change the parent and you can silently
break every child — even ones written by people who never saw your change.

> 💣 **Renovating a tower's ground floor.** Subclasses are floors stacked on the base; move a
> load-bearing wall (a base method) and floors 2–40 crack. With composition the pieces are
> neighboring houses joined by a clear road (the public interface) — renovate inside one, the
> neighbors don't care. Loose coupling = survivable software.

**The classic trap — `Stack(list)`:**
```python
class Stack(list):                 # ❌ inheriting LEAKS all 40 list methods
    def push(self, x): self.append(x)
s = Stack(); s.push(1); s.insert(0, 99); s.sort()   # 😱 a "stack" you can insert into and sort?!

class Stack:                       # ✅ compose: expose ONLY push/pop
    def __init__(self): self._items = []
    def push(self, x): self._items.append(x)
    def pop(self): return self._items.pop()
    def __len__(self): return len(self._items)
```
> **Composition lets you choose exactly what to expose** — and that control *is* the abstraction.

> 🔑 **The rule, stated fairly:** inheritance for genuine *is-a* subtypes (and framework bases
> like `nn.Module`); composition for *has-a* and assembling behaviour. When unsure, compose —
> extracting an interface later is easy; untangling a deep inheritance tree is not.

> ✍️ **Self-explain (interleave D2):** an exception hierarchy `LogLevelError(LogError)` (Day 5)
> *is* inheritance — and it's correct. Why is that genuine is-a, while `Stack(list)` isn't?
> *(A `LogLevelError` truly **is a** kind of `LogError` — a subtype used wherever the base is
> expected. A `Stack` is **not a** kind of list; it only wants to *use* a list internally →
> has-a.)*

---

## S1b — `@dataclass`: boilerplate for free
```python
from dataclasses import dataclass, field

@dataclass
class Transaction:
    kind: str
    amount: float
    balance_after: float
# free __init__, __repr__, __eq__ generated from the fields
```
> 🏭 **A label-maker for data classes.** Hand-writing `__init__`/`__repr__`/`__eq__` is
> hand-lettering the same label 500 times; `@dataclass` is the printer.

| Need | How |
|------|-----|
| default | `count: int = 0` |
| **mutable** default | `items: list = field(default_factory=list)` — **never** `= []` |
| immutable + hashable | `@dataclass(frozen=True)` |
| ordering | `@dataclass(order=True)` |

> ⚠️ Never `tags: list = []` — all instances would share one list (the S2 trap in disguise).

---

## S2 — Type hints, the mutable-default trap, `__slots__`

**Type hints** document for humans + tools (`mypy`); they are **not** enforced at runtime.
```python
def total(amounts: list[float]) -> float: ...
def find(name: str) -> "Account | None": ...
```
> 🛂 **Signage, not guards.** Hints are airport signs ("Gate B12 →"); the guard is `mypy`, run
> separately. Hint your signatures (params + return) — that's 80% of the value.

**The #1 Python gotcha — mutable default arguments:**
```python
def add_item(item, bucket=[]):     # ❌ the list is created ONCE at def-time, reused forever
    bucket.append(item); return bucket
add_item("a"); add_item("b")       # → ['a','b']  😱

def add_item(item, bucket=None):   # ✅
    if bucket is None: bucket = []
    bucket.append(item); return bucket
```
> 🧥 **A closet with one shared hanger** installed at construction (`def`) time — every guest
> piles coats on the same hook. Default to `None`, create the real object inside. (This is edge
> **E4** — Pythonic hygiene.)

**`__slots__`** trades flexibility for memory: replaces the per-instance `__dict__` (from Day 1's
"object is almost a dict") with a fixed layout. Only when a profiler says millions of instances
cost too much memory. 🎒 Foam camera case (snug, light, no room for a third lens) vs a duffel.

---

## S3 — Math: matrix×matrix, identity, inverse

`A (m×n) · B (n×p) = C (m×p)`. **Inner dims must match**; each `Cᵢⱼ = Σₖ Aᵢₖ Bₖⱼ` (row·col).
```text
[1 2][5 6]   [19 22]
[3 4][7 8] = [43 50]
```
> 🁢 **Domino rule:** write shapes adjacent `(m×n)(n×p)` — inner numbers must touch & match;
> outer numbers survive. `(2×3)(3×4)→(2×4)` ✅; `(2×3)(2×3)` → inner `3≠2` ❌. Prevents 90% of
> shape errors.

> 🎬 **Order matters: `A·B ≠ B·A`.** A matrix is a transformation; `A·B` = "do B, then A."
> "socks then shoes" ≠ "shoes then socks."

**Identity `I`** (1s on diagonal): `A·I = A` — the do-nothing transform (clear glass).
**Inverse `A⁻¹`**: `A·A⁻¹ = I` — the *undo*. ↩️ Ctrl-Z. But not every matrix has one: a
projection that flattens 3-D→2-D destroys info (singular — can't un-flatten a pancake).

> 🚀 Stacking NN layers = chaining matrix products; attention (Week 10) uses `Q·Kᵀ`; "why is my
> matmul throwing a shape error?" is a *daily* DL reality — the domino rule is the fix.

> 🔮 **By hand:** ① `[[1,2],[3,4]]·[[1,0],[0,1]]` (predict first). ② is `[[1,1]]·[[2],[3]]` valid?
> shape? ③ why can't you do `(2×3)·(2×3)`? *(① unchanged. ② valid, `(1×2)(2×1)→(1×1)=[5]`.
> ③ inner `3≠2`.)*

---

## S4 — Frontier: vLLM & PagedAttention (your #1 direction)

Reading only (~2 h). **Problem:** generating text, an LLM keeps a **KV-cache** in scarce GPU
memory that *grows* with the conversation. Naïvely you pre-reserve one big contiguous block per
request sized for the worst case → most sits empty → memory (not compute) caps how many users
you serve.

> 🅿️ **Parking lot with SUV-sized stalls, all reserved up front.** Smart cars waste most of
> their space; the lot "fills" while half-empty.

**PagedAttention** breaks the KV-cache into small fixed-size **pages**, allocated on demand and
freed on finish — exactly like an **OS's virtual memory**. Fragmentation vanishes; far more
concurrent requests fit. 🅿️➡️ Repaint into small stalls, handed out as cars arrive, reclaimed
on exit → several times more cars. **That repainting is PagedAttention** (Kwon et al. 2023; 2–4×
throughput — [`../RESOURCES.md`](../RESOURCES.md) §D).

> ✍️ Write 3 sentences: *what is a KV-cache? what does PagedAttention do to it? why does that
> raise the number of users you can serve?* If you can do it from the parking-lot analogy,
> today's frontier landed — and you can hold your own on it in an interview.

---

## 🧠 Cheat-sheet
```python
class Car:                                  # COMPOSITION ("has-a") — prefer
    def __init__(self): self.engine = Engine()
@dataclass
class Rec:
    tags: list = field(default_factory=list)   # mutable default DONE RIGHT
def f(bucket=None):                          # mutable default ARG done right
    if bucket is None: bucket = []
# A·B: inner dims match, order matters;  A·I = A;  A·A⁻¹ = I (may not exist)
```
| Term | One-liner | Analogy |
|------|-----------|---------|
| composition | "has-a"; hold a part (prefer) | Lego |
| fragile base class | base change breaks children | renovating a tower's ground floor |
| `@dataclass` | auto `__init__`/`__repr__`/`__eq__` | label-maker |
| type hints | docs for humans+`mypy`; not enforced | signage, not guards |
| mutable-default trap | one shared object across calls | shared hanger |
| `__slots__` | drop `__dict__` for memory (profiled) | foam case vs duffel |
| matrix mult | inner dims match; order matters | socks then shoes |
| inverse | the undo (may not exist) | Ctrl-Z / can't un-flatten a pancake |
| PagedAttention | paged KV-cache → more users | repainted parking lot |

## ⚠️ Common pitfalls
1. **Inheriting to reuse code that's really has-a** (`Stack(list)`) → leaks the whole interface. Compose.
2. **`def f(x=[])` / `tags: list = []`** → shared-mutable-default. `None`+create, or `field(default_factory=list)`.
3. **Believing hints enforce types** → run `mypy`.
4. **`__slots__` by default** → costs flexibility; profiler-driven only.
5. **Assuming `A·B == B·A`** → matrix mult isn't commutative.
6. **Expecting every matrix to invert** → singular ones (projections) don't.

## ✅ Storage-strength check (cold, tomorrow)
State the is-a/has-a rule + one consequence of getting it wrong; write a `@dataclass` with a safe
mutable default; predict `A·I`; explain PagedAttention in 2 sentences. Shaky → log it.

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — refactor Day-1's mega-class into composed
`Bank` + `Account` + `Ledger`. Narrate: *"Account HAS-A Ledger; Bank HAS-MANY Accounts;
Transaction is data → `@dataclass`."*
