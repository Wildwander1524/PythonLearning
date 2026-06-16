# 📘 Week 1 · Day 4 — Composition & Design

> **Date:** Thu 2026-06-19  ·  **Curriculum:** Python OOP deep-dive  ·  **Math:** Linear Algebra I

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | Composition vs inheritance · dataclasses (`@dataclass`) |
| **S2** Core Theory B | 2 h | Type hints · `typing` · mutability · `__slots__` |
| **S3** Math | 1 h | Matrix multiplication · identity / inverse intuition |
| **S4** Frontier | 2 h | Read the vLLM / PagedAttention intro (concept, no code) |
| **Homework** | 3 h | Refactor D1 account into `Bank` + `Account` + `Ledger` → [`HOMEWORK.md`](./HOMEWORK.md) |

> 🧭 **Today is the design day.** Days 2–3 gave you *mechanisms* (inheritance, dunders). Today is about *judgment*: when to use which mechanism. The headline lesson — **"prefer composition over inheritance"** — is one of the most repeated pieces of advice in all of software engineering, and by tonight you'll understand *why* in your bones, not just as a slogan.

---

## 📑 Contents

1. [S1 — Composition vs inheritance](#s1--composition-vs-inheritance)
2. [S1b — `@dataclass`](#s1b-dataclass--boilerplate-for-free)
3. [S2 — Type hints, mutability, `__slots__`](#s2--type-hints-mutability-__slots__)
4. [S3 — Math: matrix multiplication, identity, inverse](#s3--math-matrix-multiplication-identity-inverse)
5. [S4 — Frontier: vLLM & PagedAttention](#s4--frontier-vllm--pagedattention-your-1-direction)
6. [🧠 Cheat-sheet](#-cheat-sheet)
7. [⚠️ Common pitfalls](#️-common-pitfalls)

---

## S1 — Composition vs inheritance

Two ways for classes to relate. Telling them apart is today's core skill.

| Relationship | Plain-English test | Mechanism | Example |
|--------------|--------------------|-----------|---------|
| **Inheritance** | "A *is a* B" | subclassing (Day 2) | a `Dog` **is an** `Animal` |
| **Composition** | "A *has a* B" | hold it as an attribute | a `Car` **has an** `Engine` |

```python
# COMPOSITION — Car HAS-A Engine (it holds one as an attribute)
class Engine:
    def start(self):
        return "Vroom"

class Car:
    def __init__(self):
        self.engine = Engine()        # the Car owns an Engine
    def start(self):
        return self.engine.start()    # and delegates work to it
```

> 🧱 **Analogy — Lego vs a cast statue.** *Composition* is Lego: small, independent bricks (an `Engine`, a `Ledger`, a `Wheel`) that snap together into a `Car`. Don't like the engine? Pop it out, snap in a better one — the rest is untouched. *Inheritance* is a single statue cast from one mold: to change the arm, you re-cast the whole thing, and every copy made from that mold changes too. Lego systems survive change; cast statues resist it. Real software changes constantly — so you reach for Lego (composition) by default.

> 🫀 **Analogy — organs vs species.** Inheritance answers "what *kind of thing* is this?" — a dog *is a kind of* animal (biological taxonomy, an is-a tree). Composition answers "what is this *made of*?" — a body *has* a heart, lungs, liver (an assembly of parts, a has-a graph). When you catch yourself unsure, say the sentence out loud: "A car **is an** engine" sounds absurd → it's composition. "A savings account **is a** bank account" sounds right → inheritance.

### Why "prefer composition over inheritance"? The fragile base class problem

Inheritance creates a *tight, permanent* coupling: the child depends on the parent's internal behavior, not just its public interface. Change the parent and you can silently break every child — even children written by other people who never saw your change. This is the famous **fragile base class problem.**

> 💣 **Analogy — renovating the ground floor of an apartment tower.** With inheritance, subclasses are floors stacked directly on the base class. Move a load-bearing wall on the ground floor (change a base method), and floors 2 through 40 may crack — including apartments you don't own and can't see. With composition, the pieces are *neighboring houses* connected by a clearly-defined road (the public interface). Renovate inside one house and the neighbors don't care, as long as the road still connects them. Loose coupling = independent change = survivable software.

**The concrete classic trap — `Stack(list)`:**

```python
# ❌ Inheriting from list LEAKS everything
class Stack(list):
    def push(self, x): self.append(x)
    def pop_top(self): return self.pop()

s = Stack()
s.push(1); s.push(2)
s.insert(0, 99)   # 😱 list.insert leaked in — you can violate stack discipline!
s.sort()          # 😱 so did sort — a "stack" you can sort?!

# ✅ Composing a list gives you CONTROL of the interface
class Stack:
    def __init__(self):
        self._items = []            # HAS-A list, privately
    def push(self, x): self._items.append(x)
    def pop(self):     return self._items.pop()
    def __len__(self): return len(self._items)
    # only push/pop/len are exposed — true stack discipline
```

Inheriting from `list` made `Stack` an `is-a list`, dragging in 40 methods that break the abstraction. Composing a list says "a stack *has* a list inside, but only exposes push/pop." **Composition lets you choose exactly what to expose** — and that control is the whole point of building an abstraction.

> 🔑 **The rule, stated fairly:** Use **inheritance** for genuine *is-a* subtype relationships (and for ABCs / framework base classes like `nn.Module`). Use **composition** for *has-a* and for assembling behavior from parts. When in doubt, compose — you can always extract an interface later, but untangling a deep inheritance tree is far more painful.

---

## S1b — `@dataclass` — boilerplate for free

A huge fraction of classes mostly just *hold data*. Writing `__init__`, `__repr__`, and `__eq__` for each by hand is repetitive and error-prone. `@dataclass` generates them from your field declarations:

```python
from dataclasses import dataclass, field

@dataclass
class Transaction:
    kind: str
    amount: float
    balance_after: float

t = Transaction("deposit", 50, 150)
print(t)                                  # Transaction(kind='deposit', amount=50, balance_after=150)  ← free __repr__
t == Transaction("deposit", 50, 150)      # True  ← free __eq__ (compares all fields)
```

> 🏭 **Analogy — a label-maker for data classes.** Hand-writing `__init__`/`__repr__`/`__eq__` is like hand-lettering the same shipping label 500 times. `@dataclass` is the label printer: you type the fields once, it stamps out all the boilerplate, identically, every time. Less typing, zero copy-paste typos, and the intent ("this class is a bundle of these fields") jumps off the page.

| Need | How | Why |
|------|-----|-----|
| Default value | `count: int = 0` | optional field |
| **Mutable** default (list/dict/set) | `items: list = field(default_factory=list)` | **never** `= []` — see the S2 trap |
| Immutable + hashable | `@dataclass(frozen=True)` | makes instances read-only *and* hashable |
| Ordering (`<`, `>`) | `@dataclass(order=True)` | auto-generates comparison dunders |

> ⚠️ **The one dataclass rule you must not forget:** never write `tags: list = []` as a default. All instances would *share the same list object* (the S2 mutable-default bug, in disguise). `field(default_factory=list)` exists precisely to give each instance its own fresh list.

---

## S2 — Type hints, mutability, `__slots__`

### Type hints + `typing` — documentation the editor understands

```python
from typing import Optional

def total(amounts: list[float]) -> float:    # takes a list of floats, returns a float
    return sum(amounts)

def find(name: str) -> Optional["Account"]:   # returns an Account OR None
    ...
```

Modern syntax (Python 3.9+): `list[float]`, `dict[str, int]`, `tuple[int, ...]`. `Optional[X]` means `X | None`.

> 🚨 **Critical truth: hints do NOT enforce types at runtime.** Python will happily run `total("not a list")` and crash *inside* the function. Hints are for **humans and tools** — your editor's autocomplete, and static checkers like `mypy` that read the hints and flag mismatches *before* you run. 🛂 *Analogy:* type hints are the *signage* at an airport ("Gate B12 →"), not the *security guards*. They guide and document; they don't physically stop anyone. The guard (actual enforcement) is `mypy`, which you run separately.

> 🌗 **The philosophy — gradual typing.** Python lets you add hints *incrementally*: none at first, then on the tricky functions, then everywhere if you like. You get documentation + tooling benefits proportional to the effort you invest, with no all-or-nothing commitment. For a learner: hint your function signatures (params + return). That's where 80% of the value is.

### Mutability & the #1 Python gotcha: mutable default arguments

This bug catches *everyone* once. Understand it deeply now and you'll spot it forever.

```python
# ❌ BROKEN — the list is created ONCE, when the function is defined, and reused forever
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

add_item("a")    # ['a']
add_item("b")    # ['a', 'b']   ← WHAT? 'a' is still here!
add_item("c")    # ['a', 'b', 'c']  ← they all share ONE list
```

> 🧠 **Why this happens (the mechanic that explains it).** Default argument values are evaluated **exactly once — at the moment Python reads the `def` line**, not each time the function is called. So `bucket=[]` creates *one* list object, attached to the function itself. Every call that doesn't pass `bucket` reuses *that same list*, accumulating across calls.

> 🧥 **Analogy — a coat closet with one shared hanger.** You build a closet and install a single hanger at construction time (`def` time). Every guest who doesn't bring their own hanger uses *that one shared hanger* — so everyone's coats pile onto the same hook, tangled together. The fix: don't pre-install a hanger; give each guest a fresh one when they arrive.

```python
# ✅ CORRECT — sentinel default, fresh object created per call
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []          # a NEW list, every call
    bucket.append(item)
    return bucket
```

The rule: **never use a mutable object (`[]`, `{}`, `set()`) as a default argument.** Default to `None` and create the real object inside. (Immutable defaults — `0`, `""`, `None`, `(  )` — are safe, because they can't be mutated to leak state.)

### `__slots__` — trading flexibility for memory

By default, every instance carries a `__dict__` — a hidden dictionary mapping attribute names to values. It's wonderfully flexible (you can bolt on new attributes anytime) but memory-hungry. `__slots__` swaps that dict for a fixed, compact layout:

```python
class Point:
    __slots__ = ("x", "y")        # these are the ONLY attributes allowed; no per-instance __dict__
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(1, 2)
p.z = 3          # ❌ AttributeError — 'z' isn't in __slots__
```

| | Default (`__dict__`) | `__slots__` |
|---|---|---|
| Memory per instance | higher (carries a dict) | lower (fixed layout) |
| Add new attrs at runtime | ✅ yes | ❌ no |
| Attribute access speed | normal | slightly faster |
| When to use | almost always | millions of instances, profiler says so |

> 🎒 **Analogy — a custom-molded camera case vs a duffel bag.** A `__dict__` is a duffel bag: floppy, roomy, you can stuff anything in, but it wastes space and is heavier. `__slots__` is a foam case milled with exact cutouts for your camera and two lenses: lighter, snug, faster to grab each piece — but you *cannot* shove in a third lens it wasn't cut for. Use the foam case only when you're shipping thousands of identical kits and the weight savings actually matter. **`__slots__` is a profiler-driven optimization, not a default.** Don't reach for it until memory is a measured problem.

---

## S3 — Math: matrix multiplication, identity, inverse

### Matrix × matrix — chaining transformations

`A` is `m × n`, `B` is `n × p` → `C = A·B` is `m × p`. **The inner dimensions must match** (`n == n`); the outer ones become the result's shape. Each entry `Cᵢⱼ` is the dot product of row `i` of A with column `j` of B:

```text
        n=2                              Cᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ
[ 1  2 ] [ 5  6 ]   [ 1·5+2·7   1·6+2·8 ]   [ 19  22 ]
[ 3  4 ] [ 7  8 ] = [ 3·5+4·7   3·6+4·8 ] = [ 43  50 ]
  2×2      2×2                                  2×2
```

> 🔢 **The shape rule, as a domino analogy.** Write the shapes side by side: `(m × n)(n × p)`. The two **inner** numbers must touch and match (`n` = `n`) — like dominoes, the touching ends must agree. The two **outer** numbers `(m … p)` survive as the result's shape. `(2×3)(3×4) → (2×4)`. ✅  `(2×3)(2×3)` → inner `3 ≠ 2` → ❌ illegal. This one trick prevents 90% of beginner shape errors.

> 🎬 **Analogy — matrices as transformations, multiplication as "do this, then that."** A matrix is a machine that transforms vectors — one rotates, one scales, one shears. Multiplying matrices `A·B` builds a *combined* machine that does B's transformation **then** A's, in one step. This is why **order matters: `A·B ≠ B·A`.** "Put on socks, then shoes" ≠ "put on shoes, then socks." Composing transformations is inherently order-sensitive, and matrix multiplication faithfully captures that.

### Identity matrix `I` — the "1" of matrices

Ones on the diagonal, zeros elsewhere. `A·I = I·A = A` for any compatible `A`.

```text
       [ 1  0  0 ]
I₃ =   [ 0  1  0 ]      multiplying by I changes nothing — like multiplying a number by 1
       [ 0  0  1 ]
```

> 🪟 **Analogy — a perfectly clear pane of glass.** The identity matrix is a transformation that does *nothing* — vectors pass through unchanged, like light through spotless glass. Every algebraic system needs its "do-nothing" element (0 for addition, 1 for multiplication); for matrices, that's `I`.

### Inverse `A⁻¹` — the "undo" matrix

`A⁻¹` is the transformation that *reverses* `A`: `A·A⁻¹ = I`. It's the matrix analogue of "divide." Solving `A·x = b` becomes `x = A⁻¹·b`.

> ↩️ **Analogy — Ctrl-Z.** If `A` rotates a vector 30° clockwise, `A⁻¹` rotates it 30° counter-clockwise — applying both lands you exactly where you started (`I`). But here's the catch: **not every action is undoable.** A matrix that *flattens* 3-D space onto a 2-D plane (a projection) destroys information — you can't reconstruct the lost dimension, so it has **no inverse** (it's called *singular*). 🫓 *Analogy:* you can't un-flatten a pancake back into the ball of dough. Likewise, dividing by zero is forbidden because nothing "undoes" multiplication by zero. Singular matrices are the matrix version of zero in that respect.

> 🚀 **Why this matters for ML.** Stacking neural-net layers = chaining matrix multiplications (the "do this, then that" composition). The Transformer's attention mechanism (Week 10) is built from products like `Q·Kᵀ`. And "why is my matrix multiplication throwing a shape error?" will be a *daily* debugging reality in deep learning — the domino shape rule you're learning today is the fix. This hour is high-leverage.

**Practice:**
1. `[[1,2],[3,4]] · [[1,0],[0,1]]` = ? *(multiply by identity — predict before computing)*
2. Is `[[1,1]] · [[2],[3]]` valid? Apply the domino rule. What shape is the result?
3. Why can't you multiply a `2×3` by another `2×3`? State it in domino terms.
4. **Stretch:** compute `A·B` and `B·A` for `A=[[1,1],[0,1]]`, `B=[[1,0],[1,1]]`. Confirm they differ — feel non-commutativity firsthand.

---

## S4 — Frontier: vLLM & PagedAttention (your #1 direction)

> Reading only, no code (~2 h). This is your **highest-priority** career direction (plan §1: inference acceleration is *mainstream / near-required*). You'll actually deploy with vLLM in Week 9 — today is about owning the core mental model so that week is comprehension, not panic.

### First, the problem — why serving an LLM is hard

When an LLM generates text, it remembers everything said so far in a structure called the **KV-cache** (key-value cache). Every new token appends to this cache. The cache is large, lives in scarce GPU memory, and *grows* as the conversation lengthens.

Now serve *thousands* of users at once. The naïve approach pre-reserves one big contiguous block of GPU memory per request, sized for the *longest possible* output. Most requests finish early, so most of that reserved memory sits empty — **massive waste from fragmentation and over-allocation.** Memory, not raw compute, becomes the wall that limits how many users you can serve.

> 🅿️ **Analogy — a parking lot with painted full-size SUV spaces.** Imagine a lot where every car, even a tiny smart car, is assigned a space painted for the biggest SUV — *and* you must reserve all your spaces up front for the whole day. Smart cars waste most of their space; the lot "fills up" while half of it is literally empty air. That's naïve KV-cache allocation: reserved-for-the-worst-case, contiguous, mostly idle.

### The idea — PagedAttention

> **PagedAttention** breaks the KV-cache into small, fixed-size **pages** (blocks). Pages are allocated *on demand* as the output grows, and freed/reused when a request finishes — exactly like an **operating system's virtual memory** manages RAM in pages. The result: memory fragmentation nearly vanishes, and the GPU can hold *far more* simultaneous requests in the same memory.

> 🅿️➡️ **Same parking lot, fixed.** Now repaint the lot into many *small* stalls, hand them out one at a time only as each car actually arrives, and reclaim a stall the instant a car leaves. The same physical lot now serves several times more cars, because you stopped reserving SUV-sized space for smart cars. **That repainting is PagedAttention.** The OS-virtual-memory parallel is the whole insight: the trick that let computers run more programs than fit in RAM is the same trick that lets a GPU serve more users than naïve allocation allows.

That's the one paragraph to remember. If you can explain the parking-lot analogy, you understand PagedAttention well enough for an interview.

### The 2026 landscape (current context, for orientation)

| Engine | Core strength | When you'd reach for it |
|--------|---------------|-------------------------|
| **vLLM** | PagedAttention; fast startup; swap models freely | **The default** — flexible, fast to iterate |
| **TensorRT-LLM** | Compiles a model → a hyper-optimized engine (fused kernels, FP8) | Max throughput/latency on NVIDIA; ~15–30% faster on H100, but a ~28-min compile step and far less flexible |
| **SGLang** | Strong for structured / agentic, multi-step workloads | Increasingly used alongside the two above |

The current production anchor people cite: **H100/H200 + TensorRT-LLM + FP8 quantization.** The mainstream *default* people start with: **vLLM.** Your Week-9 plan (serve with vLLM → then accelerate with TensorRT-LLM) mirrors exactly how the industry actually ladders up. You're aimed correctly.

### Read (skim, take notes)
- vLLM docs — the "PagedAttention" section: <https://docs.vllm.ai/>
- For 2026 context: [vLLM vs TensorRT-LLM (Medium, 2026)](https://medium.com/synthetic-futures/vllm-vs-tensorrt-llm-the-definitive-2026-comparison-for-llm-inference-ed0943fb81d2)

> ✍️ **Note-to-self check (write 3 sentences):** *What is a KV-cache? What does PagedAttention do to it? Why does that raise the number of users you can serve?* If you can answer those three from the parking-lot analogy, today's frontier landed.

---

## 🧠 Cheat-sheet

```python
# COMPOSITION (prefer this — "has-a")     # INHERITANCE (only for true "is-a")
class Car:                                 class SavingsAccount(BankAccount): ...
    def __init__(self):
        self.engine = Engine()   # owns a part, exposes a chosen interface

from dataclasses import dataclass, field
@dataclass
class Rec:
    name: str
    tags: list = field(default_factory=list)   # mutable default DONE RIGHT

def f(bucket=None):                # mutable default ARGUMENT done right
    if bucket is None: bucket = []

class Point:
    __slots__ = ("x", "y")         # memory optimization — only when profiled
```

| Term | One-liner | Analogy |
|------|-----------|---------|
| **composition** | "has-a"; hold a part as an attribute (prefer) | Lego bricks |
| **inheritance** | "is-a"; genuine subtype only | a single cast statue |
| **fragile base class** | base change silently breaks children | renovating a tower's ground floor |
| **`@dataclass`** | auto `__init__`/`__repr__`/`__eq__` | a label-maker for data |
| **type hints** | docs for humans + `mypy`; *not* enforced | airport signage, not guards |
| **mutable default trap** | one shared object across calls | a closet's single shared hanger |
| **`__slots__`** | drop `__dict__` to save memory | foam camera case vs duffel |
| **matrix mult** | inner dims match; order matters | "socks then shoes" ≠ "shoes then socks" |
| **identity `I`** | the do-nothing transform | clear pane of glass |
| **inverse `A⁻¹`** | the undo transform (may not exist) | Ctrl-Z (can't un-flatten a pancake) |
| **PagedAttention** | paged KV-cache → more concurrent users | repainted parking lot |

---

## ⚠️ Common pitfalls

1. **Inheriting to reuse code when it's really "has-a"** → `Stack(list)` leaks the parent's whole interface. Compose instead and expose only what you mean to.
2. **`def f(x=[])` / `tags: list = []`** → shared-mutable-default bug. Use `None` + create inside, or `field(default_factory=list)`.
3. **Believing type hints enforce types** → they don't at runtime; run `mypy` for actual checking.
4. **Reaching for `__slots__` by default** → it costs flexibility (no dynamic attributes, awkward with multiple inheritance). Only when a profiler says memory matters.
5. **Assuming `A·B == B·A`** → matrix multiplication is *not* commutative. Order = "do this, then that."
6. **Expecting every matrix to have an inverse** → singular matrices (e.g. projections) don't. "You can't un-flatten a pancake."

➡️ **Next:** [`HOMEWORK.md`](./HOMEWORK.md) — refactor your Day-1 bank into composed `Bank` + `Account` + `Ledger`. As you split it, narrate: *"Account HAS-A Ledger. Bank HAS-MANY Accounts. Transaction is just data → `@dataclass`."*
