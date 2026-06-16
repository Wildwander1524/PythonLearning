# 📘 Week 1 · Day 5 — Errors, Context Managers & Modules

> **Date:** Fri 2026-06-20  ·  **Curriculum:** Python OOP deep-dive  ·  **Math:** Linear Algebra I

| Slot | Duration | Topic |
|------|----------|-------|
| **S1** Core Theory A | 2 h | Exceptions · custom exceptions · `try`/`except`/`else`/`finally` |
| **S2** Core Theory B | 2 h | Context managers (`with`, `__enter__`/`__exit__`) · modules & packages |
| **S3** Math | 1 h | Linear combinations · span (intuition) |
| **S4** Frontier | 2 h | **📰 Weekly AI Industry Digest #1** (below) + reflect on direction fit |
| **Homework** | 3 h | Context-managed file logger + a small package → [`HOMEWORK.md`](./HOMEWORK.md) |

> 🧭 **Today is about robustness — code that survives contact with the real world.** Files fail to open, networks drop, users type nonsense. Amateur code assumes everything works; professional code plans for what happens when it doesn't. Exceptions and context managers are how Python handles failure *gracefully* instead of crashing or leaking resources.

---

## 📑 Contents

1. [S1 — Exceptions](#s1--exceptions)
2. [S2 — Context managers & modules](#s2--context-managers--modules)
3. [S3 — Math: linear combinations & span](#s3--math-linear-combinations--span)
4. [S4 — 📰 Weekly AI Industry Digest #1](#s4--weekly-ai-industry-digest-1)
5. [🧠 Cheat-sheet](#-cheat-sheet)
6. [⚠️ Common pitfalls](#️-common-pitfalls)

---

## S1 — Exceptions

### Two philosophies of error handling: LBYL vs EAFP

Before the syntax, the mindset. There are two ways to deal with things that might fail:

| Style | Stands for | Shape | Example |
|-------|-----------|-------|---------|
| **LBYL** | "Look Before You Leap" | *check first, then act* | `if key in d: use(d[key])` |
| **EAFP** | "Easier to Ask Forgiveness than Permission" | *act, handle failure if it comes* | `try: use(d[key]) except KeyError: ...` |

> 🍳 **Analogy — checking eggs.** *LBYL* cracks each egg into a separate bowl and inspects it before adding to the batter — cautious, but slow and verbose. *EAFP* cracks straight into the batter and deals with it only if one's bad — Python's preferred style, because it's cleaner and avoids race conditions (the egg can't go bad *between* your check and your use). **Python culture strongly favors EAFP.** Try the operation; catch the specific exception if it fails.

### The full structure

```python
try:
    risky()                    # the operation that might fail
except ValueError as e:        # handle a SPECIFIC failure (most specific first)
    print(f"bad value: {e}")
except (KeyError, IndexError): # group related failures
    print("lookup failed")
else:                          # runs ONLY if the try block raised nothing
    print("success")
finally:                       # ALWAYS runs — success, failure, or even a return mid-try
    print("cleanup")
```

| Clause | Runs when | Typical use |
|--------|-----------|-------------|
| `try` | always (the protected block) | the risky operation |
| `except` | a matching exception was raised | recover, log, re-raise |
| `else` | the `try` succeeded (no exception) | code that should run *only* on success |
| `finally` | **always**, no matter what | cleanup that must happen regardless (close files, release locks) |

> 🪂 **Analogy — `finally` is the parachute's automatic deploy.** Whether the jump goes perfectly or something goes wrong mid-air, the reserve chute deploys *no matter what*. `finally` is that guarantee: "run this cleanup whether we succeeded, failed, or bailed out early with a `return`." It's where you close files and release resources, because those must happen on *every* path out of the block.

> ⚠️ **Catch specific exceptions — never bare `except:`.** A bare `except:` is a net that catches *everything*, including `KeyboardInterrupt` (you pressing Ctrl-C) and genuine bugs you'd want to see. 🎣 *Analogy:* it's fishing with a net so fine it scoops up the fish, the seaweed, the boat anchor, and your own foot. Catch the *specific* thing you know how to handle (`except ValueError`), and let everything else propagate so real bugs stay visible.

### The exception hierarchy — exceptions are objects, related by inheritance

This is where Day 2 pays off: exceptions form an **inheritance tree**, and catching a parent catches all its children.

```text
BaseException
 └── Exception                 ← you almost always catch at this level or below
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── KeyError
      │    └── IndexError
      └── ValueError  ...
```

`except LookupError:` catches *both* `KeyError` and `IndexError`, because they're its subclasses. This is polymorphism (Day 2) applied to errors.

### Custom exceptions — your own error vocabulary

Define your own by subclassing `Exception`. This is inheritance in genuine, daily use:

```python
class BankError(Exception):
    """Base class for ALL banking errors."""

class InsufficientFundsError(BankError):
    def __init__(self, balance, requested):
        self.balance = balance
        self.requested = requested
        super().__init__(f"Need {requested}, only {balance} available")
```

Building a *hierarchy* (a base `BankError` with specific children) gives callers a choice of precision:

```python
try:
    account.withdraw(1000)
except InsufficientFundsError as e:   # catch the SPECIFIC problem
    offer_overdraft(e.balance, e.requested)
except BankError:                     # OR catch ANY banking error broadly
    log_and_alert()
```

> 🏷️ **Analogy — labeled fuse boxes.** A generic `Exception` is a single master breaker: when it trips, you know *something* failed but not what. A custom hierarchy is a labeled panel — "Kitchen," "Garage," "Upstairs." Now a caller can respond to *exactly* the circuit that tripped (`InsufficientFundsError`) or, if they don't care about specifics, just catch the whole "banking" section (`BankError`). Precise labels turn "something broke" into "*this* broke, and here's what I'll do about it."

> 💡 **Two professional habits:**
> - **"Raise early, catch late."** Validate inputs and `raise` the instant something's wrong (fail fast, close to the cause). Handle the exception higher up, at the layer that actually knows what to *do* about it (e.g. show the user a message). Don't catch an error two lines after raising it just to hide it.
> - **Let custom exceptions carry data** (like `balance` and `requested` above), not just a message. The handler can then make decisions from the structured data, not parse a string.

---

## S2 — Context managers & modules

### Context managers — guaranteed setup *and* teardown

Some resources *must* be released: an open file must be closed, a lock must be unlocked, a network connection must be shut. Forget, and you leak resources — eventually the program (or the machine) runs out of file handles, memory, or connections. A **context manager** guarantees the cleanup happens, even if an error explodes in the middle.

You've already used one: `with open(...)`.

```python
with open("data.txt") as f:     # __enter__ opens the file, binds it to f
    data = f.read()             # use it
# the instant we leave this block, __exit__ runs → file is CLOSED,
# even if f.read() raised an exception
```

> 📚 **Analogy — a library book with auto-return.** Borrowing a book obligates you to return it. A context manager is a magical library where the book *teleports back to the shelf the moment you stop reading* — whether you finished, got bored, or the fire alarm went off mid-chapter. You physically *cannot* forget to return it. `with` is that guarantee for files, locks, connections: enter the block, the resource is yours; leave the block *by any route*, it's automatically released.

> 🚗 **Analogy — a rental car that returns itself.** `__enter__` = picking up the keys (acquire the resource). The `with` block = your road trip (use it). `__exit__` = the car driving *itself* back to the lot and settling the bill — even if your trip ended in a breakdown. You never get charged for a car you forgot to return, because returning is automatic and unconditional.

Write your own with `__enter__` / `__exit__`:

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self                       # whatever you return is bound to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"took {self.elapsed:.4f}s")
        return False                      # False = "don't suppress exceptions" (the usual choice)

with Timer():
    sum(range(10_000_000))                # prints "took 0.xxxxs"
```

**Understanding `__exit__`'s parameters** — they're how the context manager *learns whether the block failed*:

| Parameter | If the block succeeded | If the block raised |
|-----------|------------------------|---------------------|
| `exc_type` | `None` | the exception's *class* (e.g. `ValueError`) |
| `exc_val` | `None` | the exception *instance* |
| `exc_tb` | `None` | the traceback object |

| `__exit__` returns | Effect on an exception from inside the block |
|--------------------|----------------------------------------------|
| `False` / `None` | the exception **propagates** normally (the right default) |
| `True` | the exception is **suppressed** (swallowed) — use rarely and deliberately |

> 🔬 **Connection to your ML future.** PyTorch's `with torch.no_grad():` is a context manager — inside the block it switches off gradient tracking (saving memory during inference), and `__exit__` switches it back on automatically when you leave, *even if inference errored*. When you write that line in Week 8, you'll recognize it as exactly the `Timer` pattern: enter → change a setting → guarantee it's restored on exit.

> 💡 **The shortcut — `contextlib.contextmanager`.** For simple cases you can skip the class and write a generator:
> ```python
> from contextlib import contextmanager
> @contextmanager
> def timer():
>     start = time.perf_counter()
>     yield                       # everything before yield = __enter__; after = __exit__
>     print(time.perf_counter() - start)
> ```
> Learn the class form first (you'll *see* `__enter__`/`__exit__` in real libraries), then enjoy the generator shortcut for your own quick ones.

### Modules & packages — organizing code as it grows

| Thing | What it is | Analogy |
|-------|-----------|---------|
| **module** | a single `.py` file you can `import` | one labeled tool |
| **package** | a folder of modules, marked by `__init__.py` | a labeled drawer of related tools |
| **library** | a collection of packages | the whole toolbox |

```text
mypackage/
├── __init__.py      # presence of this file = "this folder is a package"
├── core.py          # a module
└── utils.py         # another module
```

```python
# __init__.py — the package's "front desk": curate what `import mypackage` exposes
from .core import MainClass        # the leading dot = "from THIS package"

# elsewhere
from mypackage import MainClass        # clean: thanks to __init__.py re-exporting it
from mypackage.utils import helper     # or reach a specific module directly
```

> 🗄️ **Analogy — a well-organized workshop.** A loose pile of 200 tools on the floor is a single 5,000-line script. Sorting them into labeled drawers (`core.py`, `utils.py`) is splitting into modules. Grouping related drawers into a labeled cabinet with an index card on the front (`__init__.py`) is making a package. The index card says "here's what's inside and what you'll usually want" — that's `__init__.py` re-exporting the public API, so users grab `from mypackage import MainClass` without rummaging through every drawer.

> 🔁 **Under the hood — `import` runs once and caches.** The first time any file does `import mypackage`, Python *executes* the module top-to-bottom and stores the result in `sys.modules`. Every later `import` of the same module returns the *cached* copy instantly — the file is not re-run. 🍞 *Analogy:* the first person to want bread bakes a loaf; everyone after just takes a slice from the shared loaf rather than baking their own. This is why import-time side effects happen exactly once, and why heavy work at module top-level runs on first import.

> 🚪 **The `if __name__ == "__main__":` guard, finally explained.** When a file is *run directly* (`python core.py`), Python sets its `__name__` to `"__main__"`. When it's *imported*, `__name__` is the module's name (`"core"`). So `if __name__ == "__main__":` means "only run this block when executed as a script, not when imported." 🎭 *Analogy:* it's an actor who performs the monologue only when alone on stage (run directly), but stays silent and supporting when part of the ensemble (imported). It lets one file be *both* a reusable module *and* a runnable program.

---

## S3 — Math: linear combinations & span

### Linear combination — scale and add

Take some vectors, scale each by a number, add the results. Given vectors `v₁, v₂` and scalars `a, b`:

```text
a·v₁ + b·v₂        ← a linear combination of v₁ and v₂
```

Example: `2·[1,0] + 3·[0,1] = [2,0] + [0,3] = [2,3]`.

> 🎨 **Analogy — mixing paint.** `[1,0]` is pure red, `[0,1]` is pure blue. A linear combination `a·red + b·blue` is a paint mix — `2` parts red, `3` parts blue. By dialing the amounts `a` and `b`, you can mix *any* purple you like. The vectors are your base pigments; the scalars are how much of each you pour.

> 🍲 **Analogy — a recipe.** The base vectors are ingredients; the scalars are quantities. "2 cups flour + 3 eggs + 1 cup sugar" is a linear combination of your pantry's basis ingredients. Different quantities → different dishes. The *set of all dishes you could possibly make* from those ingredients is the next idea: span.

### Span — everywhere you can reach

> The **span** of a set of vectors = *every* point reachable by *some* linear combination of them.

- `span([1,0], [0,1])` = the **entire 2-D plane.** Any `[x,y]` is `x·[1,0] + y·[0,1]`. These two vectors are *enough* to build everything in 2-D — they're a **basis**.
- `span([1,1])` = just the **diagonal line** through the origin. One vector, scaled up and down, only ever traces a line. You can never leave it.
- `span([1,0], [2,0])` = only the **x-axis.** The second vector points the *same direction* as the first, so it adds nothing new — it's **linearly dependent** on the first. Two vectors, but only one direction's worth of reach.

> 🗺️ **Analogy — how far your two roads can take you.** Imagine you're at an origin with vehicles that only drive along fixed directions. With one road (one vector) you can only move back and forth along that line. Add a *second road pointing a genuinely different way*, and now you can reach **any** point on the map by combining trips ("go 3 along road A, then 2 along road B"). But if your "second" road points the *same way* as the first, you've gained nothing — you're still stuck on one line. **Span is the set of all destinations; linear independence is whether each new vector actually opens up a new direction.**

> 🚀 **Why this matters for AI.** Embeddings (Week 10+) live in high-dimensional vector spaces — a word becomes a point in, say, 768-dimensional space. "What concepts can this set of vectors represent?" is literally a *span* question. "Are these features redundant?" is a *linear-dependence* question — and it's the seed of **PCA** (Week 6), which finds the few directions that actually carry the information and discards the redundant ones. The "second road that adds nothing" is exactly the redundant feature PCA throws away.

**Practice:**
1. Write `[5, 7]` as a linear combination of `[1,0]` and `[0,1]`. (What are `a` and `b`?)
2. Can `[3, 3]` be reached from `span([1,1])`? Can `[3, 4]`? *(Hint: must lie on the diagonal line.)*
3. What is `span([0,0])`? *(Trick question — think about what scaling the zero vector can ever give you.)*
4. **Stretch:** do `[1,1]` and `[2,2]` span the plane? Why or why not? What about `[1,1]` and `[1,-1]`?

---

## S4 — 📰 Weekly AI Industry Digest #1

> **Prepared manually 2026-06-16** for your Friday slot. *(Your scheduled cloud routine also auto-posts a digest every Friday 09:00 CST — treat that as the canonical #1 when it lands; this is your preview so the material's ready early.)*
> **How to use it (≈2 h):** skim everything (~30 min), then spend the rest on the reflection at the end and a deeper read of whichever direction pulls you. Standing emphasis = your 3 directions: **inference acceleration (top priority) · edge multimodal (your differentiator) · video understanding (elective)**.

> 🧭 **Why a weekly digest at all?** The field moves weekly, not yearly. A working AI engineer's edge isn't knowing everything — it's *staying oriented*: knowing what shipped, what it means, and whether to change course. This slot trains that muscle. Read it the way a trader reads the morning market summary: fast, pattern-seeking, deciding "does this change what I'm building?"

### 🌍 Headlines (mid-June 2026)

- **Google Gemini 3.5 Flash** — first of the 3.5 line; ~4× faster than prior Gemini and beats Gemini 3.1 Pro on **coding + agentic** benchmarks. The "fast, cheap, still-smart" tier keeps advancing — efficiency is winning.
- **OpenAI GPT-5.5** (Pro / Instant variants) — continued push on the reasoning + speed frontier.
- **NVIDIA Nemotron 3.5 Content Safety** (June 4) — a customizable **multimodal safety** model for enterprise. Guardrail/safety models are becoming first-class infrastructure, not afterthoughts.
- **Anthropic** — Claude reported at a **$30 B revenue run-rate** (≈80× growth in Q1 2026); the story is *enterprise adoption*, not just consumer chat.
- **Meta ↔ AMD** — up to **$100 B** chip agreement (MI540 GPUs + CPUs) to diversify AI infrastructure beyond NVIDIA. Compute supply chains are now strategic geopolitics.

> 🔭 **The macro pattern to internalize:** multimodal is now *default* in frontier models; reasoning models trade speed for accuracy; and **efficiency** (same quality, far lower cost) is the relentless theme. That efficiency pressure is *precisely why your three directions exist* — inference acceleration, edge deployment, and compact video models are all answers to "do more with less compute."

### 🥇 Inference acceleration (your top-priority skill)

- 2026 production picture: **vLLM** = the flexible default (PagedAttention, fast startup); **TensorRT-LLM** = peak throughput/latency on NVIDIA (~**15–30% faster on H100**) at the cost of a ~28-min compile step and less flexibility; **SGLang** rising for structured/agentic serving.
- Anchor config people cite: **H100/H200 + TensorRT-LLM + FP8 quantization.**
- **For you:** the Week-9 plan (serve with vLLM → accelerate with TensorRT-LLM) matches what industry actually does. You're aimed correctly — yesterday's PagedAttention parking-lot analogy is the foundation for this whole skill.
- Skim: [Best LLM Inference Engines 2026 (Yotta Labs)](https://www.yottalabs.ai/post/best-llm-inference-engines-in-2026-vllm-tensorrt-llm-tgi-and-sglang-compared) · [H100 benchmarks (Spheron)](https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/)

### 📱 Edge multimodal (your strategic differentiator)

- **Small VLMs (<10B params)** are a defined 2026 trend — efficient, on-device, privacy-preserving.
- **Apple FastVLM** (CVPR 2025) — large accuracy/latency win via efficient vision encoding; **MobileCLIP / MobileCLIP2** (3–15 ms, 50–150M params) remain the latency-accuracy reference point.
- **Nota AI's Nota Vision Agent** won the **2026 Edge AI & Vision Product of the Year** (Edge LMM category) — commercial edge-multimodal is real, not just research.
- **For you:** this maps straight onto your industrial/edge + Germany direction. Keep it as your differentiator (hands-on in Week 11).
- Skim: [VLM on Edge (LearnOpenCV)](https://learnopencv.com/vlm-on-edge-devices/) · [FastVLM (Apple)](https://machinelearning.apple.com/research/fast-vision-language-models) · [MobileCLIP (Apple)](https://machinelearning.apple.com/research/mobileclip)

### 🎬 Video understanding (elective showcase)

- New long-video models (**UFVideo**, late 2025; **VideoLoom**, Jan 2026) use multi-scale feature fusion; **token-merge** + **memory-augmented streaming** keep the visual-token budget bounded on long clips.
- **VideoLLM-online** streams dialogue over **thousands of frames** with explicit temporal alignment.
- Open problems: long-context comprehension and **compositional hallucination** (entangled space-time concepts), tackled by methods like TriCD (Jan 2026).
- **For you:** still emerging vs. image+text — correct to keep it as your *elective* (one Week-12 mini-project).
- Skim: [Video LLM overview (EmergentMind)](https://www.emergentmind.com/topics/video-large-language-model-video-llm)

### ✍️ Reflection (30 min — actually write it)

1. After reading *real* 2026 developments, which of the 3 directions excites you most — and does it still fit your industrial/Germany goal?
2. The macro theme is **efficiency** (same quality, less compute). Explain in 2–3 sentences how that *strengthens* the case for your inference + edge focus.
3. One sentence: given this week's news, what would your Week-13 capstone demo?

> Sources: [llm-stats AI news](https://llm-stats.com/ai-news) · [June 2026 roundup (DEV)](https://dev.to/vjswamy/latest-ai-model-releases-june-2026-roundup-49j5) · [vLLM vs TensorRT-LLM 2026 (Medium)](https://medium.com/synthetic-futures/vllm-vs-tensorrt-llm-the-definitive-2026-comparison-for-llm-inference-ed0943fb81d2) · [Edge AI & Vision Award (Nota AI)](https://www.edge-ai-vision.com/2026/04/2026-edge-ai-and-vision-product-of-the-year-award-winner-showcase-nota-ai-edge-ai-large-multimodal-model/) · [Long-video understanding (arXiv)](https://arxiv.org/abs/2403.16998)

---

## 🧠 Cheat-sheet

```python
try: ...                          # risky code (EAFP: try first, handle failure)
except ValueError as e: ...       # SPECIFIC exception (never bare except:)
else: ...                         # ran only if NO exception
finally: ...                      # ALWAYS runs — cleanup (the parachute)

class MyError(Exception): ...     # custom exception = inheritance; build a hierarchy

class Resource:                   # context manager (guaranteed teardown)
    def __enter__(self): return self
    def __exit__(self, et, ev, tb): return False   # False = don't suppress exceptions

# package/  →  presence of __init__.py makes it importable
if __name__ == "__main__":        # runs only when executed directly, not when imported
    ...
```

| Term | One-liner | Analogy |
|------|-----------|---------|
| **EAFP** | try first, catch failure (Python's way) | crack the egg, deal with a bad one |
| **`finally`** | cleanup that always runs | auto-deploy parachute |
| **exception hierarchy** | catch parent → catch all children | labeled fuse box |
| **custom exception** | subclass `Exception`, carry data | precise circuit labels |
| **context manager** | guaranteed setup/teardown via `with` | self-returning library book / rental car |
| **`__exit__` returns True** | suppress the exception (rare) | — |
| **module / package** | a `.py` file / a folder + `__init__.py` | a tool / a labeled drawer |
| **import cache** | a module runs once, then is cached | one loaf, everyone takes a slice |
| **linear combination** | `a·v₁ + b·v₂ + …` | mixing paint / a recipe |
| **span** | all points reachable by combinations | all destinations your roads reach |

---

## ⚠️ Common pitfalls

1. **Bare `except:`** → swallows Ctrl-C and real bugs. Catch the *specific* exception you can handle.
2. **Using exceptions for normal control flow** → don't `raise StopShopping` to exit a loop; exceptions are for the *exceptional*. (Iteration's `StopIteration` is an internal exception — you rarely raise it yourself.)
3. **Cleanup in the `try` body instead of `finally`** → if the body raises before reaching your `f.close()`, the file leaks. Put cleanup in `finally`, or better, use a `with`.
4. **Forgetting `__init__.py`** → the folder isn't recognized as a package, and imports fail. (Namespace packages exist but are an advanced exception.)
5. **`return True` from `__exit__` by accident** → silently swallows every exception in the block, hiding bugs. Default to `return False`.
6. **Confusing "linearly dependent" with "useless"** → a dependent vector adds no *new direction* (no new span), but the concept (redundancy) is the very thing PCA exploits later.

➡️ **Next:** [`HOMEWORK.md`](./HOMEWORK.md) — a context-managed logger (prove the file closes even on error) packaged as a real importable `logkit`. As you build it, connect each piece back: custom exceptions = Day-2 inheritance; `__enter__`/`__exit__` = the rental car; `__init__.py` = the drawer's index card.
