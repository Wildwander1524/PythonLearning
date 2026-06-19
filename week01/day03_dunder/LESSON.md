# 📘 Day 3 — Dunder Methods & the Python Data Model

> **Week 1 · Wed 2026-06-18** · Curriculum: Python OOP · Math: matrices, transpose, matrix×vector
> Active reading: hit every `✍️`/`🔮`. Today's mantra: **make your objects feel native** —
> printable, comparable, addable, indexable, iterable, *just like a built-in*.
> Canonical reference: **Ramalho, *Fluent Python* Ch. 1** (the `FrenchDeck` example is the
> template for today's homework) — [`../RESOURCES.md`](../RESOURCES.md) §A.

## 🎯 Objectives & mastery bar
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Explain *why* syntax → dunder call | Understand | you can say what `a+b`, `len(x)`, `for i in x` each dispatch to |
| Implement `__repr__`/`__eq__`/`__add__`/`__iter__` | Apply | your class behaves like a built-in number/list |
| Pair `__eq__` with `__hash__` correctly | Analyze | you know when your object is (un)hashable and why |

## 🔁 Spaced callbacks (cold, first — re-tests D1 + D2)
C1 (D1) why return a *copy* from `history()`? C2 (D2) **predict** `D.__mro__` for `class D(B,C)`,
`B(A)`, `C(A)`. C3 (D2) extend vs replace — which keeps the parent's guarantees?
*(Blank on C2? That's edge E3 — slow down and re-derive it.)*

---

## The big idea: built-in syntax is sugar over special methods

When you write `len(x)`, Python calls `x.__len__()`. `a + b` → `a.__add__(b)`. `print(x)` →
`x.__str__()`. **The language's syntax is method calls with special ("dunder") names.** Define
those hooks on *your* class and the same familiar syntax works on your objects.

> 🎹 **Piano keys & hammers.** The keys (`+ == len() [] for`) are the interface you press;
> behind each is a hammer (`__add__ __eq__ __len__ __getitem__ __iter__`) that strikes the
> string. Built-ins ship with hammers installed. Writing dunder methods = installing your own.

> 🌍 **Why it's profound (Ramalho's thesis):** Python doesn't have 50 special cases — it has
> *one protocol* everything opts into. Learn `len()` once; it works on str, list, dict, *and*
> your classes. **NumPy arrays, pandas DataFrames, and PyTorch tensors are built on exactly this
> mechanism** — `tensor_a + tensor_b` is `__add__`. Today you learn the hook those libraries use.

---

## S1 — Representation, equality, sizing, indexing

### `__repr__` vs `__str__` — two audiences
| Method | Triggered by | Audience | Goal |
|--------|--------------|----------|------|
| `__repr__` | REPL, debugger, **inside containers**, `repr()` | the developer | unambiguous; ideally recreates the object |
| `__str__` | `print()`, `str()`, f-strings | the end user | readable, friendly |

> 🪪 **ID card vs party nametag.** `__repr__` = precise government ID for officials (debuggers);
> `__str__` = the warm "Hi, my name is ___" sticker. **Always define `__repr__`** (it's your
> debugging lifeline — without it, a list of your objects prints `<...object at 0x7f…>`).
> `__str__` falls back to `__repr__`, never the reverse — so `__repr__` alone covers both.

> 💡 Aim for a **round-trip** repr: `eval(repr(obj))` recreates it. `Point(x=1, y=2)` is valid
> code that rebuilds the point.

### `__eq__` and the `__hash__` trap
```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other):
        if not isinstance(other, Money): return NotImplemented   # not False — let Python try other side
        return self.cents == other.cents
```
> ⚠️ **The moment you define `__eq__`, Python sets `__hash__ = None`** → your object can't go in
> a `set`/`dict`. Contract: *equal objects must hash equal*; Python can't verify your new logic,
> so it disables hashing to keep you safe. If the object is **immutable** and you want it
> hashable, define `__hash__` too (`return hash(self.cents)`); if **mutable**, leave it
> unhashable (correct — a mutable key's hash would drift).
> 🏷️ *Coat-check ticket:* if two "equal" coats got different tickets, you'd never find your coat.

> ✍️ **Self-explain (interleave with D2):** exceptions are objects in an inheritance tree
> (you'll see Day 5). What does returning `NotImplemented` (not `False`) from `__eq__` let Python
> do? *(Try the **reflected** comparison `other.__eq__(self)` — cooperation, like `super()` along
> the MRO. `False` would wrongly declare "not equal" without asking the other operand.)*

### `__len__` / `__getitem__`
```python
class Playlist:
    def __init__(self, songs): self.songs = songs
    def __len__(self): return len(self.songs)            # len(pl)
    def __getitem__(self, i): return self.songs[i]       # pl[0], pl[-1], and... iteration!
```
> 🎟️ **Hidden superpower:** with `__getitem__` but no `__iter__`, `for x in pl:` *still works* —
> Python falls back to `pl[0], pl[1], …` until `IndexError`. One good `__getitem__` gives
> indexing *and* looping. (This is the old iteration protocol Ramalho's `FrenchDeck` relies on.)

---

## S2 — Operator overloading & iterators

| You write | Python calls | Returns |
|-----------|--------------|---------|
| `a + b` | `a.__add__(b)` | a **new** object |
| `a * k` | `a.__mul__(k)` | new object |
| `a == b` | `a.__eq__(b)` | bool |
| `abs(a)` | `a.__abs__()` | a number |

> 🧾 **Golden rule: return a new object, never mutate.** `c = a + b` must leave `a`, `b`
> unchanged (`5 + 3` doesn't alter `5`). 🍪 Combining two recipes invents a third; it doesn't
> erase the originals.

> 🪞 **Reflected operators.** `2 * v` (int on the left): Python tries `int.__mul__(2, v)` → the
> int shrugs (`NotImplemented`) → Python tries `v.__rmul__(2)`. Define `__rmul__` and `2 * v`
> works. Same "ask left; if it shrugs, ask right" cooperation as `__eq__`. *(Today's stretch.)*

### Iterators — the protocol behind every `for`
| Role | Method | Job |
|------|--------|-----|
| **iterable** | `__iter__` | "I can produce an iterator" (a book that *can* be read) |
| **iterator** | `__next__` | "next item, or raise `StopIteration`" (a bookmark) |

> 🍬 **Pez dispenser.** The box (iterable) hands you a loaded dispenser (iterator); each click
> (`__next__`) pops the next candy; empty → `StopIteration`. Two dispensers from one box click
> independently — which is why the roles are separate.

> 💡 **The shortcut you'll actually use — generators.** Any method with `yield` *is* an iterator;
> Python writes `__next__`/`StopIteration` for you:
> ```python
> def __iter__(self):
>     yield self.x      # first next() → x
>     yield self.y      # second → y; function ends → StopIteration automatically
> ```
> Now `for c in v`, `list(v)`, and `x, y = v` (unpacking) all work. 📼 A cassette that remembers
> the playhead. **You'll use exactly this in today's `Vector2D`.**

> 🦥 **Why laziness matters:** an iterator yields one item at a time, so you can loop a 100 GB
> file on 8 GB RAM. PyTorch `DataLoader`s are iterators streaming batches — you'll lean on this
> from Week 8.

---

## S3 — Math: matrices, transpose, matrix×vector

A **matrix** = an `m×n` grid of numbers — *and* a function that transforms vectors (rotate,
scale, project). Hold both. `A[1][2]` = row 1, col 2 (rows first, always).

**Transpose** flips rows↔columns: a `2×3` becomes `3×2`, `(Aᵀ)ᵢⱼ = Aⱼᵢ`.

**Matrix × vector** — each output entry is a **dot product** (yesterday's tool!) of a matrix row
with the vector:
```text
[1 2] [5]   [1·5+2·6]   [17]
[3 4] [6] = [3·5+4·6] = [39]
```
- **Row picture:** each output = (row)·(vector).
- **Column picture:** output = a *linear combination of the columns*: `5·[1,3]+6·[2,4]=[17,39]`
  (this is Day 5's span/linear-combinations, foreshadowed).

> 🚀 **The most important operation in your roadmap.** A neural-net layer is `output = W·x + b`
> — a matrix times a vector. "Deep" = many of these stacked. Every forward pass (Week 8+) and
> every attention block (Week 10) is built from matrix×vector. 3B1B Ch.3 makes the
> "matrix = transformation" picture click ([3b1b](https://www.3blue1brown.com/topics/linear-algebra)).

> 🔮 **By hand:** ① transpose `[[1,2,3]]` (shape?). ② `[[2,0],[0,2]]·[3,5]` = ? what did that
> matrix *do* to the vector? ③ `[[1,0],[0,1]]·[7,9]` = ? why "identity"? *(① `[[1],[2],[3]]`,
> 3×1. ② `[6,10]` — doubled it (scaling). ③ `[7,9]` unchanged — identity does nothing.)*

---

## S4 — Frontier: verify PyTorch (it's already installed)

Per [`../RESOURCES.md`](../RESOURCES.md) §E your `dl` env already has torch 2.12 + CUDA. So
today is *verification*, not install:
```bash
conda activate dl
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# expect:  2.12.0+cu126 True
```
Then see today's lesson made concrete:
```python
import torch
x = torch.tensor([[1., 2.], [3., 4.]])
print(x.T)                              # transpose — the S3 op, one attribute away
print(x @ torch.tensor([5., 6.]))       # matrix×vector → tensor([17., 39.])
```
`x.T` is your by-hand transpose; `@` is `__matmul__`. **A tensor implements the exact dunders
you're studying** (`__add__`, `__getitem__`, `__repr__`, `__matmul__`). PyTorch = today's data
model + today's linear algebra, welded together.

---

## 🧠 Cheat-sheet
```python
__repr__    # ALWAYS define (REPL, debugger, containers)
__str__     # only when user form differs; falls back to __repr__
__eq__      # defining it ⇒ object unhashable until you add __hash__ (immutable only)
__len__ / __getitem__   # len(x) / x[i]  (getitem alone also enables for-loops)
__add__ / __mul__       # return a NEW object; never mutate self
__rmul__    # 2 * x  (reflected: left operand shrugged)
__iter__    # easiest as a generator with `yield`
```
| Term | One-liner | Analogy |
|------|-----------|---------|
| data model | syntax → dunder calls | piano keys → hammers |
| `__repr__`/`__str__` | dev / user text | ID card / nametag |
| `__eq__`+`__hash__` | define together for immutables | equal coats need equal tickets |
| reflected op | right operand handles it | "left shrugged, ask the right" |
| iterable / iterator | "can give a reader" / "is the bookmark" | candy box / loaded Pez |
| generator | `yield`-function that *is* an iterator | cassette remembering the playhead |
| matrix×vector | stack of row·vector dots | the atom of a NN layer |

## ⚠️ Common pitfalls
1. **No `__repr__`** → `<…object at 0x…>` in lists/debuggers. Define it first.
2. **Mutating `self` in `__add__`** → `a+b` must not change `a`. Return new.
3. **`__eq__` without `__hash__`** → `TypeError: unhashable` in a set. Add `__hash__` (immutable) or accept it (mutable).
4. **Hand-writing `__next__`** when a generator (`yield`) is shorter and safer.
5. **Returning `False` (not `NotImplemented`) from `__eq__`** for unknown types → blocks the reflected comparison.

## ✅ Storage-strength check (cold, tomorrow)
From a blank file: a class that `repr`s round-trip, `==`-compares, `+`-adds (new object), and
`for`-iterates via `yield`. Say which dunder each of `==`, `+`, `for` fires. Shaky → log it.

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — `Vector2D`, where `abs(v)` *is* the D2 norm and
`v.dot(w)` *is* the D2 dot product. You're now coding the linear algebra you did on paper.
