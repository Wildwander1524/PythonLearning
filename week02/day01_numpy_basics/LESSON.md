# Week 2 · Day 1 — NumPy `ndarray` basics

> **Source policy (per `/teach` rule "never rely on parametric knowledge — cite high-trust
> sources"):** every technical claim below is grounded in the **official NumPy 2.4 documentation**,
> retrieved via the **context7** MCP from source `/websites/numpy_doc_2_4`
> (context7 Source Reputation: **High**, Benchmark **79.29**). Inline tags like `[S1]` point to the
> **Sources** list at the bottom — each is a primary `numpy.org/doc/2.4/...` URL. No claim here rests
> on model parametric memory.

---

## 0. Where this sits

You spent Week 1 building objects by hand (`Vector2D`, `Bank`). NumPy is the moment that work
becomes *vectorized*: one `ndarray` replaces a list-of-lists plus the loops over it. Today is the
ground floor — **create arrays, read their metadata, reshape them, and index them** — with one
sharp idea that bites everyone exactly once: **slices are views, fancy indexing is a copy.**

---

## 1. Creating arrays + reading their metadata

The canonical first array and its metadata attributes `[S1]`:

```python
import numpy as np

a = np.arange(15).reshape(3, 5)   # 0..14 laid into a 3×5 grid
a.shape       # (3, 5)   — dimensions as a tuple
a.ndim        # 2        — number of axes
a.dtype.name  # 'int64'  — element type
a.itemsize    # 8        — bytes per element
a.size        # 15       — total elements
type(a)       # <class 'numpy.ndarray'>
```

From a Python list `[S1]`:

```python
b = np.array([6, 7, 8])   # type(b) -> numpy.ndarray
```

`np.zeros(shape)` builds an array of a given shape filled with zeros `[S2]`:

```python
np.zeros((2, 3, 4)).shape   # (2, 3, 4)  — a 3-D array
```

> ✍️ **Self-explain:** `a.size` vs `a.shape` — one is a single integer, the other a tuple. Say in
> one sentence how you'd compute `size` from `shape`. *(product of the tuple's entries)*

---

## 2. `shape` — read it, and the *discouraged* way to write it

`ndarray.shape` is **a tuple of ints**, one per axis `[S3]`:

```python
np.array([1, 2, 3, 4]).shape          # (4,)
np.zeros((2, 3, 4)).shape             # (2, 3, 4)
```

You *can* reshape in place by assigning to `.shape`, but the docs **explicitly discourage it** —
in-place assignment can fail when a copy would be required, and `ndarray.reshape` is the
recommended approach `[S3]`:

```python
y = np.zeros((2, 3, 4))
y.shape = (3, 8)   # works here, but discouraged — prefer y.reshape(3, 8)
```

> ⚠️ **Trap (cite, don't guess):** the docs carry a standing **Warning** that "setting `arr.shape`
> is discouraged and may be deprecated in the future" `[S3]`. Use `.reshape(...)`.

---

## 3. `reshape` — same data, new shape (and the `-1` trick)

`ndarray.reshape` returns an array with the **same data** arranged in a new shape `[S4]`. One axis
may be `-1`, meaning "infer this from the total size" `[S1]`:

```python
a = np.arange(30)
b = a.reshape((2, -1, 3))   # -1 means "whatever is needed"
b.shape                     # (2, 5, 3)   — 30 / (2*3) = 5
```

> 🔮 **Predict:** `np.arange(24).reshape(2, -1, 4).shape` → ? *(answer: `(2, 3, 4)`, since
> 24 / (2·4) = 3.)*

---

## 4. The one idea that bites everyone: **view vs copy**

This is *the* Day-1 concept. Get it wrong and you "mysteriously" corrupt arrays you thought you'd
left alone.

**Basic indexing (slicing) creates a _view_** — a window onto the *same* memory. Writing through
the view writes through to the original `[S5]`:

```python
x = np.arange(10)
y = x[1:3]        # a VIEW, not a copy
x[1:3] = [10, 11]
y                 # array([10, 11])  — y sees the change
```

```python
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1            # mutates a's first two elements too  [S6]
# a == [2, 3, 3, 4, 5, 6]
```

**Advanced indexing (integer-array or boolean indexing) _always_ returns a copy** — changes to the
result never touch the original `[S5][S7]`:

```python
x = np.arange(10)
mask = x % 2 == 0
evens = x[mask]   # boolean indexing -> a COPY
evens[0] = 999    # x is untouched
```

> ✍️ **Self-explain (the rule in one line):** *basic slicing → view (shares memory); advanced
> (fancy/boolean) indexing → copy.* If you need an independent array from a slice, call
> `.copy()` explicitly — the docs recommend this when keeping a small portion of a large array `[S8]`.

---

## 5. Slicing & striding mechanics

NumPy extends Python slicing to N dimensions using `slice` objects (`start:stop:step`), integers,
`Ellipsis`, and `newaxis`. All indices are **zero-based**; **negative indices count from the end**.
Indexing with **N integers** (one per axis) returns an **array scalar**, not a sub-array `[S8]`:

```python
m = np.arange(12).reshape(3, 4)
m[0, 0]      # 0   — N integers -> a scalar
m[-1, -1]    # 11  — negative indices from the end
m[:, 1]      # column 1 (a view)
m[::2, :]    # every other row (a view)
```

> 🔮 **Predict:** for `m = np.arange(12).reshape(3,4)`, what does `m[1]` give, and is it a view or a
> copy? *(answer: row 1 = `[4,5,6,7]`; basic indexing ⇒ a **view**.)*

---

## Recall hooks (cold tomorrow)

1. State the view-vs-copy rule in one sentence (which indexing gives which).
2. What does `-1` mean in `reshape`, and how is the missing axis computed?
3. Why does the official doc discourage assigning to `arr.shape`?

---

## Sources (all primary, retrieved via context7 → `/websites/numpy_doc_2_4`, NumPy 2.4)

- **[S1]** NumPy Quickstart — array creation, `shape`/`ndim`/`dtype`/`itemsize`/`size`, `reshape(-1)`:
  https://numpy.org/doc/2.4/user/quickstart.html
- **[S2]** `numpy.zeros` shape behavior (via `ndarray.shape` examples):
  https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.shape.html
- **[S3]** `ndarray.shape` reference — tuple of dims; in-place assignment discouraged (standing Warning):
  https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.shape.html
- **[S4]** `ndarray.reshape` — "same data with a new shape":
  https://numpy.org/doc/2.4/reference/arrays.ndarray.html
- **[S5]** Copies and views — basic indexing creates views; advanced indexing creates copies:
  https://numpy.org/doc/2.4/user/basics.copies.html
- **[S6]** Slicing creates a view, not a copy (mutation example):
  https://numpy.org/doc/2.4/user/basics.creation.html
- **[S7]** Advanced indexing always returns a copy:
  https://numpy.org/doc/2.4/user/basics.indexing.html
- **[S8]** Slicing & striding — `start:stop:step`, `Ellipsis`, `newaxis`, zero-based / negative
  indices, N-integer indexing returns an array scalar, `copy()` recommendation:
  https://numpy.org/doc/2.4/user/basics.indexing.html

> **Not covered by context7 / out of scope for this tool:** the S3 *Math* slot (determinants) and
> the S4 *Frontier / AI Industry Digest* slot. context7 indexes **library documentation**, not math
> pedagogy or industry news — those sections must be sourced elsewhere (see the evaluation note in
> `progress/2026-06-25_context7-authority-eval.md`).
