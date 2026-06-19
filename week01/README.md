# Week 1 — Object-Oriented Python + Linear Algebra I

> Part of the [3-Month AI Career Study Plan](../progress/2026-06-15_3Month-Study-Plan.md).
> This week is built as a **`/teach` workspace**: not notes to read, but a system to *learn
> with* — retrieval practice, spaced review, and an explicit mastery bar. Start at
> **[`MISSION.md`](./MISSION.md)**.

## The week at a glance

| Day | Folder | Core topic | Math (LA I) | Frontier | Build |
|-----|--------|-----------|-------------|----------|-------|
| D1 | [`day01_bankaccount`](./day01_bankaccount/) | Classes, encapsulation, properties | Vectors: notation, add, scale | Env + Git + repo | `BankAccount` |
| D2 | [`day02_inheritance`](./day02_inheritance/) | Inheritance, polymorphism, ABCs, MRO | Dot product, norm, distance | What is an LLM | `Animal` tree + `Shape` ABC |
| D3 | [`day03_dunder`](./day03_dunder/) | Dunder methods & the data model | Matrices, transpose, matrix×vector | Verify PyTorch | `Vector2D` |
| D4 | [`day04_composition`](./day04_composition/) | Composition, `@dataclass`, type hints | Matrix×matrix, identity, inverse | vLLM / PagedAttention | Refactor → `Bank`+`Account`+`Ledger` |
| D5 | [`day05_errors_context`](./day05_errors_context/) | Exceptions, context managers, modules | Linear combinations, span | Weekly AI Digest #1 | Context-managed logger + package |
| D6 | [`day06_miniproject`](./day06_miniproject/) | Consolidate + capstone | Week-1 recap + problems | Catch-up / reflect | **CLI contact book → GitHub** |

## Files in each day
- `LESSON.md` — the lesson (active: stop at every ✍️ Self-explain / 🔮 Predict prompt).
- `HOMEWORK.md` — the 3-hour build; specs are exact and tested.
- `RECALL.md` — retrieval-practice quiz; do the *spaced* part cold each morning.
- `SOLUTIONS.md` — worked answers; open **only after** a real attempt.
- `*.py` — your code + the provided tests. `REVIEW.md` — feedback when you submit.

## Week-level files
- [`MISSION.md`](./MISSION.md) — objectives, your ability boundary, mastery bar, Spaced-Review Map.
- [`RESOURCES.md`](./RESOURCES.md) — authoritative sources (Fluent Python, CS61A, 3B1B, MIT 18.06, papers).
- [`learning-records/`](./learning-records/) — per-session memory that powers spaced repetition.

## How to run
```bash
cd week01/day0X_topic
python <file>.py          # smoke-test
python test_*.py          # the day's tests (or: pytest)
```

## The one habit that makes this work
Every day, **before** new material, do the spaced callbacks in today's `RECALL.md` from
memory. Blanking is expected and useful — it's the signal that tells the system (and you)
what to reinforce. Reading feels like progress; *retrieving* is progress.
