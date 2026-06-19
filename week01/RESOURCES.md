# 📚 Week 1 — RESOURCES (the authoritative knowledge base)

> The `/teach` "Knowledge layer." When a lesson makes a claim, this is where it's *grounded* —
> the same primary sources Stanford/Berkeley/MIT courses use. Read the **★ must** items; the
> rest are for when you want to go deeper or see it explained a second way (a second
> explanation of the same idea is itself a *desirable difficulty* — it forces re-encoding).

---

## A · Object-Oriented Python & the data model

| ★ | Source | Use it for | Link |
|---|--------|-----------|------|
| ★ | **Ramalho, *Fluent Python* (2e), Ch. 1 "The Python Data Model"** | THE canonical treatment of dunder methods — read the `FrenchDeck` example; it's the template for Day 3. | [O'Reilly overview](https://www.oreilly.com/content/fluent-python/) · [book](https://www.thoughtworks.com/en-us/insights/books/fluent-python-2nd-edition) |
| ★ | **Berkeley CS61A — *Composing Programs*, Ch. 2 (Object Abstraction)** | The clearest free treatment of classes, inheritance, and "what is an object" at Ivy rigor. | [composingprograms.com](https://www.composingprograms.com/) |
| ★ | **Python docs — Data model** (`object.__special__`) | The spec itself. Bookmark it; you'll grep it weekly. | [docs.python.org/3/reference/datamodel.html](https://docs.python.org/3/reference/datamodel.html) |
|  | Stanford CS106A/B (Programming Abstractions) | Methodology & abstraction mindset (C106B is C++, but the *abstraction* lessons transfer). | [cs106b.stanford.edu](https://cs106b.stanford.edu/) · [SEE](https://see.stanford.edu/course/cs106b) |
|  | `abc` module docs; `dataclasses` docs | Day 2 (ABC contracts) and Day 4 (`@dataclass`). | [abc](https://docs.python.org/3/library/abc.html) · [dataclasses](https://docs.python.org/3/library/dataclasses.html) |
|  | Real Python — "Python's data model / dunder methods" | A friendly second pass if the spec is dense. | [realpython.com](https://realpython.com/python-magic-methods/) |

**The one idea to carry all week (Ramalho):** *Python's power is that built-in syntax —
`len(x)`, `a + b`, `for i in x` — is sugar over special-method calls (`__len__`, `__add__`,
`__iter__`). Learn the protocol once; every type, including yours, plays along.*

---

## B · Linear Algebra I (the math hour)

| ★ | Source | Use it for | Link |
|---|--------|-----------|------|
| ★ | **3Blue1Brown — *Essence of Linear Algebra*** (video series) | Build the *geometric* intuition first. Ch.1 vectors, Ch.3 matrices-as-transformations, Ch.9 dot-product-as-duality. Watch the matching chapter the night before each math hour. | [3blue1brown.com/topics/linear-algebra](https://www.3blue1brown.com/topics/linear-algebra) · [Class Central](https://www.classcentral.com/course/youtube-essence-of-linear-algebra-511830) |
| ★ | **MIT 18.06 — Gilbert Strang** (OCW) | The rigorous companion to 3B1B's intuition. Lectures 1–3 cover exactly Week 1's matrix material. | [ocw.mit.edu 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) |
|  | 3B1B "Dot products and duality" (the deep one) | *Why* `a·b = ‖a‖‖b‖cosθ` and the algebraic form are the same thing. | [3blue1brown.com/lessons/dot-products](https://www.3blue1brown.com/lessons/dot-products/) |

**The through-line:** dot product (D2) → matrix×vector (D3) → matrix×matrix (D4). By Day 4
you'll see a neural-net layer `Wx + b` is *literally* this week's math. The dot product is also
**cosine similarity**, the engine of every RAG/semantic-search system you'll build later.

---

## C · Pedagogy — *why this workspace is shaped the way it is*

> You don't need to study these, but knowing the mechanism makes you trust the (occasionally
> uncomfortable) method — the cold-recall mornings are a *feature*.

| Source | The idea it gives you | Link |
|--------|------------------------|------|
| **Brown, Roediger & McDaniel — *Make It Stick*** | Retrieval practice & spaced practice beat re-reading; "fluency" is a trap. | [book](https://www.hup.harvard.edu/books/9780674729018) |
| **Bjork — "desirable difficulties"** | Effortful recall (struggling to remember) *strengthens* memory; easy review doesn't. | [Springer review](https://link.springer.com/article/10.1007/s10648-022-09677-2) |
| Interleaving research | Mixing problem types (this week's Spaced-Review Map) outperforms blocking. | [Eton CIRL summary](https://cirl.etoncollege.com/strategies-for-making-learning-last-retrieval-practice-spaced-practice-and-interleaving/) |

Mapped to this workspace: `RECALL.md` = retrieval practice · the **Spaced-Review Map** in
[`MISSION.md`](./MISSION.md) §4 = spacing + interleaving · the `✍️ Self-explain` prompts =
the *self-explanation effect* · `learning-records/` = the spacing scheduler's memory.

---

## D · Frontier (the S4 orientation slot)

| ★ | Source | Use it for | Link |
|---|--------|-----------|------|
| ★ | **Karpathy — "Intro to Large Language Models"** (1-hr talk) | Your single best mental model of what an LLM *is*: next-token prediction, scale, emergence. | search the title (YouTube) · [audio](https://creators.spotify.com/pod/profile/jack1505/episodes/Intro-to-Large-Language-Models---Andrej-Karpathys-Tech-Talk-Learning-e2uqdc4) |
| ★ | **Kwon et al. 2023 — "Efficient Memory Management for LLM Serving with PagedAttention"** | Your #1 career direction (vLLM). Read the abstract + §1; the parking-lot analogy is the whole idea. 2–4× throughput vs prior systems. | [PagedAttention (Wikipedia)](https://en.wikipedia.org/wiki/PagedAttention) · [vLLM docs](https://docs.vllm.ai/) |
|  | MobileCLIP (Apple) — abstract only | Edge-multimodal differentiator: CLIP maps image+text to one space (compared via — yes — a dot product); "mobile" = small enough to run on-device. | search "MobileCLIP Apple arxiv" |
|  | Video-LLaMA — abstract only | Elective: video = frames + audio; the hard part is *temporal* reasoning. | search "Video-LLaMA paper" |

**Plan priority (from study-plan §1):** vLLM/TensorRT-LLM inference accel = *mainstream /
near-required* (top priority) · edge-multimodal = your strategic differentiator ·
video understanding = elective showcase. All three share one DNA: **doing more with less
compute.**

---

## E · Your environment (so the frontier installs "just work")

From `E:\Code\ClaudeCode_Context\2026-06-13_EnvSetup.md` — already installed & verified:
- **`ml` conda env** (Py 3.12): numpy, pandas, scikit-learn, matplotlib, jupyter — Week 2+.
- **`dl` conda env** (Py 3.12): **torch 2.12 + CUDA 12.6** on your GTX 1660, transformers,
  peft — Week 3's "install PyTorch" frontier is *already done*; just `conda activate dl` and
  `import torch`.
- Ollama (`qwen2.5:7b`, `llama3`), C++ toolchain, 5 MCP servers — for later weeks.

> 💡 For Week 1 you only need a plain Python to run your `.py` files. When Day 3's frontier
> says "install PyTorch," you instead just *verify* it: `conda activate dl` →
> `python -c "import torch; print(torch.__version__, torch.cuda.is_available())"` → expect
> `2.12.0+cu126 True`.

---

## How to cite while you learn
When `learning-records/` notes a struggle, link the resource that fixed it, e.g.
`Confused by reflected operators → Fluent Python Ch.1 cleared it`. Over the 13 weeks this
becomes *your* annotated bibliography — a real asset.
