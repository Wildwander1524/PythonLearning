---
name: grade-day
description: Grade a PythonLearning homework day against the full Definition-of-Done — pyright clean, pytest green in the dl conda env, spec-precision check — then update review-queue.md and misconceptions.md. Use when grading a dayNN homework submission.
disable-model-invocation: true
argument-hint: "which day folder, e.g. week01/day05_errors_context"
---

# grade-day — homework Definition-of-Done gate

Grades one day's homework with **retrieval discipline**. Never hand over fixes — surface the
diagnostics and apply the hint-ladder (one nudge per turn, wait for the learner's retry). Work the
steps in order.

## 1. Locate + re-read the spec
The day folder is `$ARGUMENTS` (e.g. `week01/day05_errors_context`). If missing, ask which day.
Read that day's `HOMEWORK.bilingual.md` **first, twice** — the learner's growth edge **E1** is spec
precision, so grade against the literal Definition of Done, not a paraphrase.

## 2. Run the automated checks
```bash
bash .claude/skills/grade-day/run_checks.sh <day_folder>                # gates homework code only
bash .claude/skills/grade-day/run_checks.sh <day_folder> --gate-tests   # when writing tests IS the homework
```
Runs **pyright** (type/hygiene gate) + **pytest** in the **`base`** conda env (Python 3.13.9).
- **Default: pyright gates only the homework code** (`test_*.py` excluded from the type gate).
- Add **`--gate-tests`** only when the day's spec makes writing the tests part of the deliverable
  (e.g. a Part C "write the tests" — like Day 5's `test_logkit.py`).
- pytest **executes** the tests either way — that's the behavior check.

The day is **not done** until pyright reports **0 errors** (on the gated targets) AND every test passes.

## 3. Grade against the spec (hint-ladder)
For each Definition-of-Done checkbox in the HOMEWORK spec, verify the code satisfies it. For any
miss or pyright finding:
- **Diagnose** the specific gap → name the **prerequisite** → **nudge** at the approach. Do *not*
  write the fix. Only confirm once the learner produces it.
- Cross-reference `week01/misconceptions.md`: if a miss matches a logged trap (M1–M17), name it
  ("that's M17 — `with` doesn't suppress unless `__exit__` returns truthy").
- Prefer reconstruction checks ("predict the output", "trace the close-on-error path") over yes/no.

## 4. Update spacing + traps
- `week01/review-queue.md` (SM-2-lite): add/update each graded concept — `q(0–5) | ease | interval
  | next-due`. `q≤2` → reset to 1-day, knock ease −0.2 (floor 1.3); `q=3` → ×1.2, ease unchanged;
  `q≥4` → grow `1 → 6 → round(interval × ease)`, ease +0.1 (cap 2.8).
- `week01/misconceptions.md`: if a genuinely new classic trap surfaced, append it
  (**Trap → Counterexample → Correct**, tagged to the relevant edge E1–E4).

## 5. Report + offer the upgrade
Summarize: pyright status · pytest status · per-DoD-item verdict · what landed vs needs a retry ·
updated next-due dates. If a recall checkpoint was hit, offer the lesson HTML upgrade (and route its
generation through the `lesson-html-reviewer` subagent + the `frontend-design` skill).

> Progress log lives in `E:\Code\ClaudeCode_Context\` (global convention) — update it after grading.
