# 📘 Week 1 · Day 3 — Dunder Methods & the Data Model

> **Date:** Wed 2026-06-18  ·  **Curriculum:** Python OOP deep-dive  ·  **Math:** Linear Algebra I

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | `__str__` · `__repr__` · `__eq__` · `__len__` · `__getitem__` |
| **S2** Core Theory B | 2 h | Operator overloading (`__add__` …) · iterators (`__iter__`/`__next__`) |
| **S3** Math | 1 h | Matrices: definition, transpose, matrix × vector |
| **S4** Frontier | 2 h | Install CUDA-ready PyTorch (CPU is fine) + verify |
| **Homework** | 3 h | `Vector2D` with full operator overloading + iteration → [`HOMEWORK.md`](./HOMEWORK.md) |

> 🧭 **Today's mantra:** *make your objects feel native.* By the end you'll be able to write a class whose instances can be printed, compared with `==`, added with `+`, measured with `len()`, indexed with `[]`, and looped over with `for` — just like a built-in list or number. That "it just works" feeling is what people mean by **Pythonic**.

---

## 📑 Contents

1. [The big idea: Python's data model](#the-big-idea-pythons-data-model)
2. [S1 — Representation, equality, sizing, indexing](#s1--representation-equality-sizing-indexing)
3. [S2 — Operator overloading & iterators](#s2--operator-overloading--iterators)
4. [S3 — Math: matrices](#s3--math-matrices)
5. [S4 — Frontier: install PyTorch](#s4--frontier-install-pytorch-)
6. [🧠 Cheat-sheet](#-cheat-sheet)
7. [⚠️ Common pitfalls](#️-common-pitfalls)

---

## The big idea: Python's data model

Here's something that surprises people: when you write `len(x)`, Python doesn't have special built-in knowledge of `x`. It simply calls `x.__len__()`. When you write `a + b`, Python calls `a.__add__(b)`. When you `print(x)`, Python calls `x.__str__()`. **The built-in syntax of the language is just sugar over method calls with special names.**

> **"Dunder"** = **d**ouble **under**score. `__len__` is "dunder len." These methods are the *hooks* Python's syntax reaches for.

> 🎹 **Analogy — piano keys and hammers.** The keys (`+`, `==`, `len()`, `[]`, `for`) are the friendly interface you press. Behind each key is a hammer (`__add__`, `__eq__`, `__len__`, `__getitem__`, `__iter__`) that actually strikes the string. Built-in types ship with the hammers pre-installed. When *you* write a class, defining dunder methods is **installing your own hammers** so the same familiar keys work on your objects. The pianist (someone using your class) never has to know which hammer fires — they just play.

> 🌍 **Why this is profound, not just convenient.** This design is why Python feels so consistent. You learn `len()` once and it works on strings, lists, dicts, *and* the classes you'll write — because they all implement the same `__len__` hook. The language doesn't have 50 special cases; it has *one protocol* that everything opts into. This idea — "define a small set of methods and the whole language cooperates with your object" — is called the **data model**, and it's arguably Python's single best feature.

This is the deep reason today matters for your career: PyTorch tensors, NumPy arrays, and pandas DataFrames are *built on this exact mechanism*. When you write `tensor_a + tensor_b` next month, you're calling `__add__`. Understanding the hook today means those libraries will feel like extensions of the language rather than mysterious black boxes.

---

## S1 — Representation, equality, sizing, indexing

### `__str__` vs `__repr__` — the two faces of an object

Both turn an object into text, but for **different audiences**:

| Method | Triggered by | Audience | Goal |
|--------|-------------|----------|------|
| `__repr__` | `repr(x)`, the REPL, debuggers, being inside a list/dict | **the developer** | *unambiguous*; ideally valid Python that recreates the object |
| `__str__` | `str(x)`, `print(x)`, f-strings | **the end user** | *readable and friendly* |

> 🪪 **Analogy — ID card vs nametag.** `__repr__` is your government ID: precise, complete, unambiguous, meant for officials (developers) who need to know *exactly* what this is — full name, ID number, everything needed to look you up. `__str__` is the "Hi, my name is ___" sticker at a party: warm, short, for casual human consumption. A good object wears both: the ID for the debugger, the nametag for the user.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"   # looks like code that recreates it
    def __str__(self):
        return f"({self.x}, {self.y})"            # friendly


p = Point(1, 2)
print(p)        # (1, 2)            → __str__ (print prefers str)
print(repr(p))  # Point(x=1, y=2)   → __repr__
p               # Point(x=1, y=2)   → REPL shows repr
[p, p]          # [Point(x=1, y=2), Point(x=1, y=2)]  → containers ALWAYS use repr
```

That last line is the practical kicker: **a list of your objects prints each one with `__repr__`, not `__str__`.** This is why a class with no `__repr__` shows the dreaded `<__main__.Point object at 0x7f8b2c>` inside lists — useless for debugging.

> 🔑 **The rule, memorized once:** *Always* define `__repr__` (it's your debugging lifeline). Define `__str__` *only* when the user-facing form should differ from the developer form. If `__str__` is missing, Python falls back to `__repr__` — so `__repr__` alone covers both in a pinch. There is no fallback the other way.

> 💡 **Pro convention:** make `__repr__` *round-trip* — `eval(repr(obj))` should recreate the object. `Point(x=1, y=2)` is valid Python that rebuilds the point. You won't always achieve it, but aiming for it forces a genuinely informative repr.

### `__eq__` — what does "equal" mean for *your* type?

By default, `a == b` for custom objects means "are these the *same object* in memory?" (identity), which is almost never what you want.

```python
class Money:
    def __init__(self, cents):
        self.cents = cents

m1 = Money(100)
m2 = Money(100)
m1 == m2     # WITHOUT __eq__ → False  (two different objects, even with equal contents!)
```

> 👯 **Analogy — identical twins.** Without `__eq__`, Python compares like a paranoid bouncer checking fingerprints: two identical twins (same contents) are still "not equal" because they're physically different people. Defining `__eq__` tells Python *what you actually care about* — "for money, equal means same number of cents, I don't care that they're separate objects."

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented        # "I don't know how to compare to that" — let Python try other.__eq__
        return self.cents == other.cents

Money(100) == Money(100)   # True ✅
```

> ⚠️ **The `__eq__`/`__hash__` trap (important).** The moment you define `__eq__`, Python sets `__hash__` to `None`, making your object **unhashable** — it can no longer go in a `set` or be a `dict` key. Why? Because the contract is: *equal objects must have equal hashes.* Python can't guarantee your new equality logic respects that, so it disables hashing to keep you safe.
> - **If the object is immutable** and you want it hashable: define `__hash__` too, e.g. `def __hash__(self): return hash(self.cents)`.
> - **If it's mutable:** leave it unhashable (correct — mutable things shouldn't be dict keys, since their hash would change underneath the dict).
> - 🏷️ *Analogy:* the hash is a coat-check ticket number computed from your coat. If two "equal" coats got *different* tickets, you'd never find your coat again. So the rule "equal ⇒ same hash" is non-negotiable, and Python enforces it by making you opt back in deliberately.

### `__len__` and `__getitem__` — making an object sequence-like

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):                  # enables  len(playlist)
        return len(self.songs)
    def __getitem__(self, index):       # enables  playlist[0]  ...and more (see below)
        return self.songs[index]


pl = Playlist(["a", "b", "c"])
len(pl)      # 3
pl[0]        # "a"
pl[-1]       # "c"   — negative indexing comes free, because we delegated to a list
```

> 🎟️ **The hidden superpower of `__getitem__`.** Watch this:
> ```python
> for song in pl:       # we never defined __iter__ ... yet this works!
>     print(song)
> ```
> If a class has `__getitem__` but no `__iter__`, Python falls back to calling `obj[0]`, `obj[1]`, `obj[2]`, … until it gets an `IndexError`, which it treats as "stop." This is the **old iteration protocol**, and it means one well-written `__getitem__` gives you indexing *and* looping at once. 🪜 *Analogy:* it's like a staircase with no sign saying "this leads upstairs" — but if you keep stepping up one stair at a time and eventually hit a wall (`IndexError`), you've effectively toured the whole staircase.

---

## S2 — Operator overloading & iterators

### Arithmetic & comparison operators

Every operator maps to a dunder. You're not "redefining `+`" globally — you're teaching *your class* how to respond when it's on the left of a `+`.

| You write | Python calls | Returns |
|-----------|--------------|---------|
| `a + b` | `a.__add__(b)` | usually a **new** object |
| `a - b` | `a.__sub__(b)` | new object |
| `a * b` | `a.__mul__(b)` | new object |
| `a == b` | `a.__eq__(b)` | `bool` |
| `a < b` | `a.__lt__(b)` | `bool` |
| `abs(a)` | `a.__abs__()` | usually a number |

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __add__(self, other):
        return Money(self.cents + other.cents)   # NEW Money — don't mutate self!
    def __repr__(self):
        return f"${self.cents / 100:.2f}"

Money(150) + Money(350)   # $5.00
```

> 🧾 **The golden rule of operators: return a new object, never mutate.** When you write `c = a + b`, you expect `a` and `b` to be unchanged. Integers obey this (`5 + 3` doesn't alter `5`). Your classes must too. 🍪 *Analogy:* combining two cookie recipes to invent a third shouldn't *erase* the original two recipes. `a + b` creates a third thing; it doesn't consume its ingredients.

> 🪞 **Under the hood — reflected operators.** What about `2 * v` where `v` is your `Vector2D` and `2` is a plain int? Python first tries `int.__mul__(2, v)`. The int has no idea what a `Vector2D` is, so it returns `NotImplemented`. Python then tries the **reflected** operation: `v.__rmul__(2)` (note the `r`). If you define `__rmul__`, `2 * v` works. This two-step dance — "ask the left operand; if it shrugs, ask the right operand the reflected question" — is how Python lets your types interoperate with built-ins. (It's a stretch goal in today's homework.)

### Iterators: the protocol behind every `for` loop

This is one of the most important mechanics in Python, so let's build it carefully. There are two roles:

| Role | Has method | Job |
|------|-----------|-----|
| **Iterable** | `__iter__` | "I can *produce* an iterator." (a book that *can* be read) |
| **Iterator** | `__next__` | "I produce the next item, or raise `StopIteration`." (a bookmark tracking your place) |

When you write `for x in thing:`, Python does this under the hood:

```python
_it = iter(thing)          # calls thing.__iter__()  → get an iterator
while True:
    try:
        x = next(_it)      # calls _it.__next__()    → next value
    except StopIteration:  # the iterator's way of saying "I'm empty"
        break
    ...                    # loop body runs with x
```

> 🍬 **Analogy — a Pez dispenser.** An **iterable** is the candy box on the shelf: it *can* give you a dispenser. An **iterator** is the loaded Pez dispenser: each click (`__next__`) pops out the next candy, and when it's empty it… stops (`StopIteration`). The box knows how to *hand you a fresh dispenser* (`__iter__`); the dispenser knows how to *pop the next one* (`__next__`). Crucially, you can ask the box for *two* dispensers and click them independently — which is why the iterable and iterator are separate roles.

The full manual form:

```python
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):              # I'm iterable: hand back an iterator (myself, freshly reset)
        self.current = self.start
        return self
    def __next__(self):              # I'm also the iterator: pop the next value
        if self.current <= 0:
            raise StopIteration      # the official "I'm done" signal
        self.current -= 1
        return self.current + 1


for n in Countdown(3):
    print(n)        # 3, 2, 1
```

> 💡 **The shortcut you'll actually use 95% of the time — generators.** Writing `__next__` and managing `StopIteration` by hand is tedious. A **generator** (any function/method using `yield`) *is* an iterator automatically — Python writes the `__next__` and `StopIteration` machinery for you:
> ```python
> class Vector2D:
>     def __init__(self, x, y):
>         self.x, self.y = x, y
>     def __iter__(self):
>         yield self.x          # first next() returns x
>         yield self.y          # second next() returns y
>         # function ends → StopIteration raised automatically
> ```
> Now `for c in v:`, `list(v)`, and `x, y = v` (unpacking) all work. 📼 *Analogy:* a generator is like a cassette tape that remembers where the playhead is. Each `yield` is "play until here, then pause"; calling `next()` presses play again from the pause point. You'll use exactly this trick in today's `Vector2D` homework.

> 🦥 **Why iterators matter beyond looping — laziness.** An iterator produces values *one at a time, on demand*, rather than building the whole collection in memory. This is why you can loop over a 100 GB file line-by-line on a laptop with 8 GB of RAM: the iterator only ever holds one line at a time. 🏭 *Analogy:* a conveyor belt delivers one item when you reach for it, versus dumping the entire warehouse into your lap. In ML you'll lean on this constantly — PyTorch `DataLoader`s are iterators that stream batches of data so you never load the full dataset into memory at once.

---

## S3 — Math: matrices

> A **matrix** is a rectangular grid of numbers: `m` rows × `n` columns → an **m × n** matrix. But like vectors, it has a second identity: a matrix is also a **function that transforms vectors** (rotate, scale, project). Holding both pictures — "grid of numbers" and "transformation" — is the goal.

```text
        col0 col1 col2
A =   [  1    2    3  ]   row0      A is 2 × 3   (rows first, then columns — always)
      [  4    5    6  ]   row1      A[1][2] = 6  (row 1, col 2, zero-indexed)
```

> 📊 **Analogy — a spreadsheet.** A matrix is literally a spreadsheet: rows and columns of numbers. "2 × 3" is "2 rows, 3 columns." Addressing `A[1][2]` is clicking the cell at row 1, column 2. You already think in spreadsheets; matrices are spreadsheets that obey algebra.

### Transpose — flip rows and columns

```text
        [ 1  2  3 ]                [ 1  4 ]
A   =   [ 4  5  6 ]      Aᵀ  =     [ 2  5 ]        (Aᵀ)ᵢⱼ = Aⱼᵢ
   2×3                            [ 3  6 ]
                                     3×2
```

The transpose reflects the grid across its diagonal — row `i` becomes column `i`. A 2×3 becomes a 3×2.

> 🔄 **Analogy — rotating a class seating chart 90°.** Imagine a seating chart where rows are "table number" and columns are "seat number." Transposing swaps the axes: now rows are seats, columns are tables. Same students, same data — just viewed with the axes swapped. You'll do this constantly to make matrix shapes line up for multiplication.

### Matrix × vector — the operation that *is* a neural network layer

An `m × n` matrix times an `n × 1` vector produces an `m × 1` vector. **Each output entry is the dot product of one matrix row with the vector** (yesterday's dot product, reused!):

```text
[ 1  2 ] [ 5 ]   [ 1·5 + 2·6 ]   [ 17 ]
[ 3  4 ] [ 6 ] = [ 3·5 + 4·6 ] = [ 39 ]
  2×2      2×1                      2×1

  row0 · vector = 17
  row1 · vector = 39
```

There are two equally valid ways to read this, and switching between them is real mathematical fluency:
- **Row picture:** each output = (a row) · (the vector) — a stack of dot products.
- **Column picture:** the output is a *linear combination of the matrix's columns*, weighted by the vector's entries: `5·[1,3] + 6·[2,4] = [17,39]`. (This connects directly to Day 5's "linear combinations & span.")

> 🚀 **Why this is the most important operation in your entire roadmap.** A single neural-network layer computes `output = W·x + b` — a matrix `W` times an input vector `x`, plus a bias `b`. That's it. A "deep" network is just many of these stacked: `layer2(layer1(x))`. Every forward pass you run from Week 8 onward, every Transformer attention block in Week 10, is built from matrix × vector. The 3-4-5 triangle of Day 2 and this matrix-vector product of Day 3 are the literal atoms of deep learning. **You are not doing throwaway math; you are assembling the pieces.**

**Practice (by hand, then check):**
1. Transpose `[[1, 2, 3]]` (a 1×3). What shape results, and what does it look like?
2. `[[2, 0], [0, 2]] · [3, 5]` = ? *(What did multiplying by this matrix* do *to the vector, geometrically?)*
3. What does multiplying any vector by `[[1,0],[0,1]]` (the identity) do? Why is it called "identity"?
4. **Stretch:** compute `[[0, -1], [1, 0]] · [1, 0]` and `· [0, 1]`. This matrix rotates vectors 90°. Can you see it?

---

## S4 — Frontier: install PyTorch ✅

> Today's frontier is **environment setup**, not reading. Goal: a working PyTorch you can `import`. You laid the groundwork (the `pythonlearning` conda env) on D1; today you furnish it with the library you'll live in from Week 8 to Week 13.

> 🧰 **Analogy — stocking the workshop before the job.** You don't wait until you're mid-repair to discover you don't own a wrench. Installing PyTorch now, weeks before you train your first network, means that when the ML weeks arrive, the tool is on the bench, tested, and ready. Frontier-slot installs are *runway-building* — boring today, priceless later.

```bash
conda activate pythonlearning

# CPU build is perfectly fine for now — you won't train large models for weeks.
pip install torch torchvision

# Verify the install:
python -c "import torch; print('torch', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```

**Expected output (CPU machine):**
```text
torch 2.x.x
CUDA available: False
```

> 🎮 **If you have an NVIDIA GPU:** install the CUDA build instead — visit <https://pytorch.org/get-started/locally/>, use the selector (OS / pip / your CUDA version), and run the command it generates. Then `torch.cuda.is_available()` prints `True`. For Week 1 it genuinely doesn't matter which you have; the only goal today is that `import torch` succeeds.

**Your first tensor — and notice it speaks today's math:**

```python
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(x)                                   # a 2×2 matrix
print(x.T)                                 # transpose — the S3 operation, one attribute away
print(x @ torch.tensor([5.0, 6.0]))        # matrix × vector → tensor([17., 39.])
```

Look closely: `x.T` is the transpose you did by hand, and `@` is matrix multiplication. **PyTorch is the data model from S1 + the linear algebra from S3, fused into one library.** A tensor implements `__matmul__` (that's the `@` hook), `__add__`, `__getitem__`, `__repr__` — the exact dunder methods you're studying today. You are, right now, learning the two halves (objects + matrices) that PyTorch welds together. When it stops feeling like coincidence and starts feeling inevitable, the week has done its job.

---

## 🧠 Cheat-sheet

```python
__repr__    # repr(x), REPL, debugging, inside containers — ALWAYS define this
__str__     # print(x), str(x), f-strings — define only when user form differs
__eq__      # x == y    (defining it makes the object unhashable — add __hash__ if immutable & needed)
__len__     # len(x)
__getitem__ # x[i]      (bonus: also enables for-loops via the old iteration protocol)
__add__     # x + y     (return a NEW object; never mutate self)
__rmul__    # 2 * x     (reflected: called when the LEFT operand doesn't know your type)
__iter__    # for ... in x   →  easiest implementation: a generator using `yield`
__next__    # one step of an iterator; raise StopIteration when done
```

| Term | One-liner | Analogy |
|------|-----------|---------|
| **data model** | built-in syntax → dunder method calls | piano keys → hammers |
| **`__repr__`** | dev-facing, unambiguous; always write it | government ID |
| **`__str__`** | user-facing, friendly; optional | party nametag |
| **`__eq__`/`__hash__`** | define together for immutable types | equal coats need equal coat-check tickets |
| **operator overloading** | give `+ == []` meaning for your class | install your own hammers |
| **reflected op** | right operand handles it via `__rXXX__` | "left shrugged, ask the right" |
| **iterable vs iterator** | "can give a reader" vs "is the bookmark" | candy box vs loaded Pez dispenser |
| **generator** | `yield`-function that *is* an iterator | cassette tape that remembers the playhead |
| **matrix × vector** | stack of row·vector dot products | the atom of a neural-net layer |

---

## ⚠️ Common pitfalls

1. **No `__repr__`** → objects show as `<...object at 0x...>` in lists and debuggers. Always define it first.
2. **Defining `__str__` but not `__repr__`** → containers and the REPL still show the ugly default. `__repr__` is the one with a fallback role; `__str__` is not.
3. **Mutating `self` in `__add__`** → `a + b` should never change `a`. Return a *new* object.
4. **Forgetting `__hash__` after `__eq__`** → `TypeError: unhashable type` when you put the object in a set. Add `__hash__` (immutable) or accept unhashability (mutable).
5. **Hand-writing `__next__` when a generator would do** → more code, more bugs. Reach for `yield` first.
6. **Returning the wrong type from `__eq__`** → return `NotImplemented` (not `False`) when the other operand is an unknown type, so Python can try the reflected comparison.

➡️ **Next:** [`HOMEWORK.md`](./HOMEWORK.md) — build a `Vector2D` that prints, compares, adds, scales, indexes, and iterates. As you go, ask of each method: *"Does this make my object behave more like a built-in?"*
