# Progress — 2026-06-27 · Day-5 homework (logkit FileLogger)

> Per-project progress log. Topic: Week-1 Day-5 errors/context-managers **homework** build + grade.
> Resumed from `progress/2026-06-25_HANDOFF.md`.

## Status: 🟡 in progress — callbacks graded; building interactive lesson upgrade (EAFP + context managers deep-dive)

## Detour (learner request 2026-06-27): /teach interactive lesson upgrade
Learner asked to go deeper on **context managers + EAFP** and **upgrade the whole Day-5 lesson except the math block**,
via /teach. Recall checkpoints already graded this session → upgrade trigger satisfied.
- Followed `/teach` SKILL.md (Method A: Claude authors HTML directly) + consulted **frontend-design** skill.
- Matching course visual system (day03/day04 `LESSON.interactive.html`: light cards + dark runtime console + bilingual EN/中文, vanilla JS, self-contained).
- Building `week01/day05_errors_context/LESSON.interactive.html` — interactive **runtime tracers**:
  try/except/else/finally stepper · exception-hierarchy isinstance matcher (+M15 ordering) ·
  **context-manager lifecycle** (signature: enter→body→exit, toggle raise / return True) · EAFP race (TOCTOU) · `__name__` toggle.
  Scope excludes S3 math/span + S4 digest per request. Cites docs.python.org primary anchors.
- After delivery: generation-effect guardrail (offer a ~60s predict/trace check); offer lesson-html-reviewer.

### ✅ Lesson upgrade shipped (2026-06-27)
- Built `week01/day05_errors_context/LESSON.interactive.html` (~560 lines, self-contained, vanilla JS, bilingual).
  Six sections: ① EAFP race (TOCTOU) · ② try/except/else/finally stepper · ③ hierarchy isinstance matcher (+M15/pyright) ·
  ④ context-manager lifecycle (signature; toggle raise / return True; live __exit__ args + file OPEN/CLOSED) ·
  ⑤ __name__ toggle · ⑥ cheat-sheet/pitfalls. Math (S3) + digest (S4) excluded per request.
- Self-review: `node --check` on extracted JS = OK; tags balanced (6/6 sections, 81/81 divs, 1/1 script/style).
  Fixed 2 logic bugs on review: except badge greened in KeyError mode (→ skip); CM greyed a ran body line (→ grey after() only on propagate).
- Opened in browser. Pending: offer ~60s retrieval check + optional lesson-html-reviewer pass.
- **Back to main track after this:** learner still needs to build `logkit` FileLogger (unstarted), then grade, then RECALL.

### ✅ Workflow convention change shipped (2026-06-27) — "video-teacher-first"
Learner directive + plan-mode approval → adopted 3 durable /teach conventions and wrote them across the
right scopes (general→global SKILL, Python→project). Plan file: `~/.claude/plans/i-d-like-to-change-mutable-quasar.md`.
1. **Video-teacher-first order:** each day builds `LESSON.interactive.html` FIRST (the "lecture", must embed
   predict-before-reveal + a quiz-with-feedback), then `LESSON.bilingual.md` (the "textbook"), then
   homework/recall/solutions, then code.
2. **Density floor:** every concept = 3 depth passes (intuition→mechanism→edge) + 3 examples easy→hard.
3. **Weekly `weekNN/CHEATSHEET.html`:** printable, one-page, EN+中文, at week completion.
Guardrail kept: RECALL.md + review-queue remain the cold spaced re-tests; context7 + pyright gate unchanged.
Files edited: global `/teach` SKILL.md (topic-agnostic: Lessons lecture/textbook, new "Depth and worked
examples" §, visual-first-must-carry-retrieval, Reference consolidate-at-unit-end); project `CLAUDE.md`
(new "Per-day build order, density & weekly cheat-sheet" §); `week01/MISSION.md §5b` (rewritten); global
`~/.claude/CLAUDE.md` (/teach trigger synced to interactive-first). Memory: updated
teach-lesson-bilingual-workflow + teach-html-upgrade-reminder (now legacy-only), added
teach-video-teacher-model (governing), refreshed MEMORY.md. Verified SKILL stayed topic-agnostic; docs consistent.
Rollout: NEW materials (Day 6 / Week 2 onward); D1–D5 not retro-rewritten; Day-5 already complies.

## Completed this session
- **Resumed from handoff** (`2026-06-25_HANDOFF.md`). Confirmed Day-5 lesson done, homework outstanding.
- **Graded the inline Spaced callbacks** the learner wrote in `LESSON.bilingual.md` (uncommitted change):
  - C2 (D3) `for`→`StopIteration` ✅ q4.
  - C1 (D1) *why raise immediately* — forgot → revealed **fail-fast** principle (q1, re-queued).
  - C3 (D4) mutable default *when* — "first instance" (wrong) → **def-time** on retry (q2, re-queued).
- **Graded 2 overdue cold re-tests** (were due 06-26, run cold today):
  - Generator → auto `StopIteration` ✅ **q4 graduated** (1d→6d, due 07-03).
  - Matrix × vector — shape+method ✓, entry-2 arithmetic slip (17→13) corrected on 1 nudge → **q2** (E2 edge), due 06-28.
- **Updated `week01/review-queue.md`**: new short-interval items (matrix×vector, C1 fail-fast, C3 mutable-when, all due 06-28); generator graduated to Scheduled; 2026-06-27 session-log block added; flagged the still-overdue 06-26 maintenance items (matrix×matrix, NotImplemented vs False, repr vs str, read-only @property, EXTEND vs REPLACE).

## Remaining (next steps, in order)
1. **Learner builds `logkit`** (their deliverable — I grade with hints, do NOT write it):
   - `logkit/errors.py` — `LogError(Exception)` → `LogLevelError(LogError)`.
   - `logkit/logger.py` — `FileLogger` ctx mgr: `__init__(path, allowed_levels=None)` (None-sentinel, no mutable default),
     `__enter__` opens append + returns self, `__exit__` closes always + returns False, `write(level,msg)` raises
     `LogLevelError` on bad level, `write` before `__enter__` raises `LogError`. 3 concept checks at file bottom.
   - `logkit/__init__.py` — re-export `FileLogger`, `LogError`, `LogLevelError`.
   - `main.py` — `from logkit import FileLogger, LogLevelError`; runs & writes a log.
   - `test_logkit.py` — 5 tests incl. **the proof**: file closed after `with` even when block raises.
2. **Grade** with the pyright gate (Day-5 uses `--gate-tests` — tests ARE the deliverable):
   `bash .claude/skills/grade-day/run_checks.sh week01/day05_errors_context --gate-tests`
   then hint-ladder spec grade + update `review-queue.md` / `misconceptions.md`.
3. **Day-5 RECALL** cold before Day 6.

## Key decisions / reminders
- Env = **base** (Python 3.13.9, pytest 8.4.2): `conda run -n base python -m pytest <path> -v`.
- DoD pyright gate: homework `.py` must be pyright-clean; for Day 5 also gate the tests (`--gate-tests`).
- Teaching discipline: learner generates the code; I grade with the **hint ladder** (point at the diagnostic, don't fix).
- Day-5 canonical traps to watch in grading: **M14** broad/bare except · **M15** except ordering specific→general ·
  **M16** subclass `Exception` not `BaseException` · **M17** `with` doesn't suppress unless `__exit__` returns truthy.
