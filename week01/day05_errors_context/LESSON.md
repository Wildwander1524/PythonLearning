# 📘 Day 5 — Errors, Context Managers & Modules

> **Week 1 · Fri 2026-06-20** · Curriculum: Python OOP · Math: linear combinations & span
> Today is about **robustness** — code that survives contact with the real world (files fail,
> users type nonsense). Amateur code assumes success; professional code plans for failure.

## 🎯 Objectives & mastery bar
| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Build a custom **exception hierarchy** | Create | a caller can catch by category or specifics |
| Write a context manager (`__enter__`/`__exit__`) | Apply | the resource releases even when the block raises |
| Organize code into modules/packages | Understand | you explain `__init__.py` and the `__name__` guard |
| Math: linear combinations & span | Understand | you decide if a vector is reachable / independent |

## 🔁 Spaced callbacks (cold, first — re-tests D1, D3, D4)
C1 (D1) why raise `ValueError` on bad input *immediately*? C2 (D3) the data model — what fires on
`for x in obj`? C3 (D4) the mutable-default trap — what's shared and when is it created?

---

## S1 — Exceptions

### LBYL vs EAFP (the mindset before the syntax)
| Style | Shape | Example |
|-------|-------|---------|
| **LBYL** "look before you leap" | check first, then act | `if k in d: use(d[k])` |
| **EAFP** "easier to ask forgiveness" | act, handle failure | `try: use(d[k]) except KeyError: ...` |
> 🍳 LBYL inspects every egg in a separate bowl; EAFP cracks straight in and deals with a bad one.
> **Python favors EAFP** — cleaner, and no race condition between check and use.

```python
try:
    risky()
except ValueError as e:           # SPECIFIC (most specific first); never bare except:
    handle(e)
else:                             # runs only if try raised nothing
    on_success()
finally:                         # ALWAYS runs — cleanup on every path
    cleanup()
```
> 🪂 **`finally` = the auto-deploy parachute** — runs whether you succeeded, failed, or bailed
> with a `return`. Close files / release locks here.
> 🎣 **Never bare `except:`** — it scoops up `KeyboardInterrupt` and real bugs. Catch the specific
> thing you can handle; let the rest propagate.

### Exception hierarchy — exceptions are objects in an inheritance tree (Day 2 pays off)
```text
BaseException → Exception → LookupError → {KeyError, IndexError}
```
`except LookupError:` catches both children — polymorphism applied to errors.

### Custom exceptions — your own error vocabulary
```python
class BankError(Exception): ...                  # base for ALL banking errors
class InsufficientFundsError(BankError):
    def __init__(self, balance, requested):
        self.balance, self.requested = balance, requested      # carry DATA, not just a message
        super().__init__(f"need {requested}, have {balance}")
```
```python
try: account.withdraw(1000)
except InsufficientFundsError as e: offer_overdraft(e.balance, e.requested)   # specific
except BankError: log_and_alert()                                            # OR broad
```
> 🏷️ **Labeled fuse box.** A bare `Exception` is one master breaker ("something tripped"). A
> hierarchy is a labeled panel — catch *exactly* the circuit, or the whole "banking" section.
> **Two pro habits:** *raise early, catch late* (raise at the cause; handle where you know what to
> do); *let exceptions carry data* so handlers decide from structure, not string-parsing.

> ✍️ **Self-explain (interleave D2):** why is `class InsufficientFundsError(BankError)` a
> *correct* use of inheritance, when Day 4 warned against `Stack(list)`? *(It's genuine is-a — an
> `InsufficientFundsError` **is a** `BankError`, usable anywhere the base is caught. `Stack` is
> not a `list`.)*

---

## S2 — Context managers & modules

### Context managers — guaranteed setup *and* teardown
Some resources *must* be released (files, locks, connections). A context manager guarantees it,
even if the block explodes.
```python
class Timer:
    def __enter__(self):
        self.t = time.perf_counter(); return self      # bound to the `as` variable
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{time.perf_counter()-self.t:.4f}s")
        return False                                    # False = don't suppress exceptions (default)
with Timer():
    work()
```
> 🚗 **A rental car that returns itself.** `__enter__` = pick up keys; the block = your trip;
> `__exit__` = the car drives *itself* back and settles the bill — even after a breakdown.

| `__exit__` param | block succeeded | block raised |
|------------------|-----------------|--------------|
| `exc_type/val/tb` | all `None` | the class / instance / traceback |
| **returns** `False`/`None` | — | exception **propagates** (right default) |
| **returns** `True` | — | exception **suppressed** (rare, deliberate) |

> 🔬 PyTorch's `with torch.no_grad():` is exactly this — disables gradient tracking on enter,
> restores it on exit even if inference errors. You'll recognize it in Week 8.
> 💡 Shortcut: `@contextlib.contextmanager` + a generator (`yield` splits enter/exit). Learn the
> class form first (you'll *see* `__enter__`/`__exit__` in libraries).

### Modules & packages
| Thing | What | Analogy |
|-------|------|---------|
| module | one `.py` file | a labeled tool |
| package | a folder + `__init__.py` | a labeled drawer |
```python
# mypackage/__init__.py — the "front desk": curate the public API
from .core import MainClass
# elsewhere:  from mypackage import MainClass
```
> 🍞 **Import runs once, then caches** (`sys.modules`): the first import executes the file
> top-to-bottom; later imports take a slice of the same loaf. Side effects happen once.
> 🎭 **`if __name__ == "__main__":`** runs a block only when the file is *executed directly*
> (`__name__ == "__main__"`), not when imported (`__name__ == "core"`). One file = reusable
> module *and* runnable script.

---

## S3 — Math: linear combinations & span

**Linear combination** = scale each vector, add: `a·v₁ + b·v₂`. e.g. `2·[1,0]+3·[0,1]=[2,3]`.
🎨 Mixing paint: `[1,0]`=red, `[0,1]`=blue; dial `a`,`b` to mix any purple.

**Span** = every point reachable by *some* linear combination.
- `span([1,0],[0,1])` = the whole plane (a **basis**).
- `span([1,1])` = just the diagonal line.
- `span([1,0],[2,0])` = only the x-axis — `[2,0]` adds no new direction (**linearly dependent**).
> 🗺️ Two roads pointing genuinely different ways reach anywhere; a "second" road parallel to the
> first adds nothing. **Span = all destinations; independence = does each vector open a new
> direction.**
> 🚀 Embeddings (Week 10) live in high-D spaces — "what can these vectors represent?" is a *span*
> question; "are these features redundant?" is *linear dependence* — the seed of **PCA** (Week 6),
> which keeps the informative directions and drops the redundant ones.

> 🔮 ① write `[5,7]` as a combo of `[1,0]`,`[0,1]`. ② is `[3,4]` in `span([1,1])`? ③ do `[1,1]`
> and `[2,2]` span the plane? *(① `5·[1,0]+7·[0,1]`. ② no — not on the diagonal. ③ no — dependent,
> they span only the diagonal line.)*

---

## S4 — 📰 Weekly AI Industry Digest #1 (condensed)

> Your Friday frontier slot trains *staying oriented* — read like a trader skims the morning
> market summary: fast, deciding "does this change what I'm building?" *(A cloud routine
> auto-posts the canonical Digest #N to the study plan every Friday 09:00 CST; treat that as
> authoritative when it lands. Full version: study-plan §"Weekly AI Industry Digests".)*

**Macro pattern (mid-2026):** multimodal is now *default*; reasoning models trade speed for
accuracy; **efficiency** (same quality, far less compute) is the relentless theme — which is
*precisely why your 3 directions exist*.

| Your direction | 2026 snapshot | Takeaway |
|----------------|---------------|----------|
| 🥇 **Inference accel** | vLLM = flexible default (PagedAttention); TensorRT-LLM = peak NVIDIA throughput (~15–30% faster on H100, ~28-min compile); SGLang rising | Week-9 plan (vLLM → TensorRT-LLM) matches industry; you're aimed right |
| 📱 **Edge multimodal** | small VLMs (<10B) a defined trend; Apple FastVLM/MobileCLIP the latency reference | your industrial/Germany differentiator; hands-on Week 11 |
| 🎬 **Video understanding** | long-video models (token-merge, memory-streaming); still emerging | correct as your *elective* (one Week-12 project) |

> ✍️ **Reflection (write it):** ① which direction excites you most, and does it still fit your
> industrial/Germany goal? ② in 2–3 sentences, how does the *efficiency* theme strengthen your
> inference+edge focus? ③ one sentence: what would your Week-13 capstone demo?

---

## 🧠 Cheat-sheet
```python
try: ...
except ValueError as e: ...     # specific; never bare except:
else: ...                       # only if no exception
finally: ...                    # always (the parachute)
class MyError(Exception): ...   # custom = inheritance; build a hierarchy, carry data
class Resource:
    def __enter__(self): return self
    def __exit__(self, et, ev, tb): return False   # don't suppress
if __name__ == "__main__": ...  # runs only when executed directly
# linear combo: a·v₁+b·v₂ ;  span = all reachable combos ;  dependent = adds no new direction
```
| Term | One-liner | Analogy |
|------|-----------|---------|
| EAFP | try first, catch failure | crack the egg, handle a bad one |
| `finally` | always-run cleanup | auto-deploy parachute |
| exception hierarchy | catch parent → catch children | labeled fuse box |
| context manager | guaranteed setup/teardown | self-returning rental car |
| `__exit__` → True | suppress the exception (rare) | — |
| package | folder + `__init__.py` | labeled drawer + index card |
| import cache | module runs once | one loaf, many slices |
| span | all reachable combinations | all destinations your roads reach |

## ⚠️ Common pitfalls
1. **Bare `except:`** → swallows Ctrl-C and bugs. Be specific.
2. **Exceptions for normal control flow** → they're for the *exceptional*.
3. **Cleanup in the `try` body** → leaks if it raises first. Use `finally` or `with`.
4. **Missing `__init__.py`** → folder isn't a package; imports fail.
5. **Accidental `return True` from `__exit__`** → silently hides every error.
6. **"linearly dependent" = "useless"** → it adds no new *direction*, but redundancy is exactly what PCA exploits.

## ✅ Storage-strength check (cold, tomorrow)
Write a 3-level exception hierarchy + a `with`-managed resource that closes on error; explain the
`__name__` guard; decide if `[1,2]`,`[2,4]` span the plane. Shaky → log it.

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — a context-managed `FileLogger` (prove it closes
the file *even on error*) shipped as an importable `logkit` package. Connect each piece:
custom exceptions = D2 inheritance; `__enter__`/`__exit__` = the rental car; `__init__.py` = the
drawer's index card.
