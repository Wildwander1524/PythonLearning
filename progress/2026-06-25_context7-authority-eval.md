# 2026-06-25 — context7 MCP as a learning-material source: authority before/after eval

**Topic:** Does routing lesson generation through the **context7** MCP measurably raise the
*authority* (share of claims backed by a primary, citable source) of PythonLearning materials —
and should it become a primary source for the materials? User asked for a concrete before/after.

**Status:** ✅ Eval complete. Verdict: **big, real authority gain — but only for the content
category context7 actually serves (library/API docs). It does NOT apply to the AI Industry Digest.**

---

## What was compared

| | "Before" baseline | "After" (context7) |
|---|---|---|
| Artifact | **Weekly AI Industry Digest #1** (condensed), `week01/day05_errors_context/LESSON.bilingual.md` §S4 | **Week 2 Day 1 NumPy lesson**, `week02/day01_numpy_basics/LESSON.md` (generated this session) |
| Content category | AI **industry news / market intel** (vLLM throughput, model trends, job market) | **Library documentation** (NumPy `ndarray` basics) |
| Source used | model parametric knowledge (digest is "condensed"; points to a canonical sourced version that is **not present in the repo** yet) | context7 → `/websites/numpy_doc_2_4` (NumPy 2.4 official docs) |

context7's own metadata for the NumPy source it served:
**Source Reputation = High · Benchmark Score = 79.29 · 16,778 code snippets.** Every snippet carried
a primary `numpy.org/doc/2.4/...` URL.

---

## Authority metric (defined)

> **authority % = (atomic factual claims backed by an inline citation to a primary/official source)
> ÷ (total atomic factual claims).** Counted claim-by-claim, by hand, on each artifact.

### BEFORE — Digest #1 (10 atomic frontier claims, all inline-uncited)

1. "multimodal is now default" · 2. "reasoning models trade speed for accuracy" ·
3. "efficiency is the relentless theme" · 4. "vLLM = flexible default (PagedAttention)" ·
5. "TensorRT-LLM ~15–30% faster on H100" · 6. "~28-min compile" · 7. "SGLang rising" ·
8. "small VLMs (<10B) a defined trend" · 9. "Apple FastVLM/MobileCLIP the latency reference" ·
10. "long-video models … still emerging".

- Inline primary-source citations: **0 / 10 → authority ≈ 0%.**
- Caveat (fairness): the study-plan §8 Sources list (12 links) backs the **Germany/China market
  Q&A** (§1–§2), *not* these frontier-tech numbers. The digest itself ships with the specific
  numbers (15–30%, 28-min) uncited. The "canonical, sourced" digest the routine was meant to post
  to a `Weekly AI Industry Digests` section **does not exist in the repo** (routine's GitHub-access
  prerequisite likely unmet — see study-plan §7.2).

### AFTER — W2D1 NumPy lesson (21 atomic technical claims, all inline-cited)

Creation/metadata (`arange`,`reshape`,`array`,`zeros`,`.shape/.ndim/.dtype/.itemsize/.size`,
`type`); `shape` is a tuple + in-place-assignment-discouraged Warning; `reshape` "same data" +
`-1` inference; **view-vs-copy** (basic slicing→view, mutation propagates; advanced/boolean
indexing→copy; `copy()` recommendation); slicing mechanics (`start:stop:step`, `Ellipsis`,
`newaxis`, zero-based, negative-from-end, N-integers→array scalar).

- Inline primary-source citations: **21 / 21 → authority ≈ 100%** (each tagged `[S1]`–`[S8]` to a
  `numpy.org/doc/2.4` URL).
- The lesson also **refuses to pad**: it explicitly fences the Math + Frontier slots as
  "not covered by context7," instead of inventing uncited filler. That discipline *is* the
  `/teach` "never rely on parametric knowledge" rule in action.

**Measured delta: ~0% → ~100% inline-cited primary-source authority.**

---

## The honest caveat (why the headline number is necessary but not sufficient)

The 0%→100% jump is **real**, but it compares two *different content categories*. context7 scored
100% because it was asked about a **library** (its home turf) and 0% was the digest's score because
the digest is **news** — context7 indexes documentation, **it has no "what happened in AI this
week" corpus**. So the experiment proves *context7 is excellent for library/technical content*; it
does **not** prove context7 can source the industry digest (it structurally cannot).

A stricter, apples-to-apples test (same category, with/without context7): "NumPy lesson from
parametric memory" vs "NumPy lesson via context7." That would also land ~0%→~100% on citations and
adds version-pinning (NumPy **2.4**) + an official **deprecation Warning** I would not reliably have
recalled from parametric memory. So the gain holds up under the fair test too — for **library content**.

---

## Verdict on the user's 3 asks

1. **Eval requested** → done above. Authority gain is large and real *for library/technical content*.
2. **"Make context7 a primary source for the Frontier / AI Industry Digest section"** →
   ❌ **Not recommended — category mismatch.** context7 = docs index, not a news source; it cannot
   author or authenticate weekly industry news. Wiring it there would add nothing.
   ✅ **Counter-recommendation (serves the real goal better):** make context7 the **primary source
   for the technical lesson sections** (S1/S2 core + any library-using homework) **from Week 2
   (NumPy) onward** — that is exactly where the curriculum now lives, and where the 0%→100% gain is
   captured. Keep the **AI Industry Digest** sourced from primary **news/market** sources (web
   fetch/search + the Friday cloud routine), still honoring "cite high-trust sources."
3. **Keep `/teach`'s "never rely on parametric knowledge — cite high-trust sources"** → ✅ unchanged.
   context7 adoption *strengthens* this rule for library content; the digest keeps its own
   high-trust (news) sourcing. Nothing about the principle changes.

---

## Proposed workflow change (pending user OK)

Add to project `CLAUDE.md` (and/or the `/teach` method): *"For any lesson/homework whose subject is
a library, framework, or API (NumPy W2 onward: pandas, PyTorch, scikit-learn, LangChain, …), the
**primary source is context7** (`resolve-library-id` → `query-docs`); cite the returned primary
URLs inline. context7 is **not** a source for the Weekly AI Industry Digest (news) — that keeps its
own primary news/market sourcing."*

## Files
- Demonstrator lesson: `week02/day01_numpy_basics/LESSON.md` (context7-grounded, 21/21 cited).
- Baseline digest: `week01/day05_errors_context/LESSON.bilingual.md` §S4.
- This eval: `progress/2026-06-25_context7-authority-eval.md`.

## Next steps
- [ ] User decides: adopt the scoped workflow change (context7 → library lessons only)?
- [ ] If yes: add the rule to project `CLAUDE.md`; optionally expand W2D1 to the full /teach 4-file
      set (LESSON/HOMEWORK/RECALL/SOLUTIONS) + DeepSeek bilingual.
- [ ] Commit decision (W2D1 lesson + this eval are currently untracked).
