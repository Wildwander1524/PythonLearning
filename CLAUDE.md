# CLAUDE.md — PythonLearning workspace

Project-scoped workflow for this repo. Complements (does not replace) the global
`C:\Users\Admin\.claude\CLAUDE.md` and the `/teach` method captured in
`week01/MISSION.md`. Loaded automatically each session in this project.

## What this repo is
A `/teach`-method Python OOP + Linear Algebra learning workspace. Each `weekNN/dayNN_topic/`
holds `LESSON.bilingual.md` / `HOMEWORK.bilingual.md` / `RECALL.bilingual.md` /
`SOLUTIONS.bilingual.md`, plus the learner's `.py` and tests. Retrieval discipline (hint-ladder
grading, `week01/review-queue.md`, `week01/misconceptions.md`) governs how lessons are graded.

## Environment
- Run all tests in the **`base`** conda env (Python **3.13.9** — pytest lives here).
  - `conda run -n base python -m pytest <path> -v`
- pyright is pointed at base via repo-root `pyrightconfig.json` (`venvPath` D:/, `venv` ANACONDA).
- (Note: the old "use dl, not base 3.8.8" convention is retired — base was upgraded to 3.13.9.)

## Homework grading — Definition of Done (pyright gate)
> Added 2026-06-25 after installing the **pyright-lsp** plugin.

Before grading any day's homework `.py`, **run pyright type diagnostics** on the changed files and
fold the result into the Definition of Done. This makes growth-edge **E4 (Pythonic polish / hygiene)**
machine-checked instead of eyeballed.

- Get diagnostics via the LSP tool (`mcp__ide__getDiagnostics`, or the `LSP` tool) on each homework
  file before reading it for correctness.
- **A day's homework is not "done" until pyright is clean** (no errors): type hints present and
  correct, no unresolved names, no obviously-wrong signatures. Report any pyright findings to the
  learner as part of feedback — but per hint-ladder discipline, point at the diagnostic, don't fix it
  for them.
- Type-hint quality is now part of the rubric: e.g. `list[Song]`, `Optional[...]`, `-> None`, and
  flagging untyped public methods.

## /teach in this repo
- Interactive lesson HTML follows the `/teach` SKILL.md *Lessons* + *Visualization Upgrades* sections
  (`E:\Code\MyProjects\VSCode_Env\WorkFlow\skills\productivity\teach\SKILL.md`) — including consulting
  the **frontend-design** skill for visual direction.
- Progress logs live in this project's **`progress/`** directory (per global CLAUDE.md, updated
  2026-06-25 — the old `E:\Code\ClaudeCode_Context\` location is retired).

## Per-day build order, density & weekly cheat-sheet
> Added 2026-06-27 (learner request). Shifts this workspace to **video-teacher-first**: the interactive
> HTML lesson is *a teacher explaining by video* (go deeper, understand faster) and the lesson `.md` is
> *the textbook* beside it. Supersedes the old "markdown first, HTML-after-recall" order in
> `week01/MISSION.md §5b`. Applies to **new** materials (Day 6 / Week 2 onward); D1–D5 are not
> retro-rewritten. Day-5 already complies (HTML + md both exist).

**Per-day artifact order — build top to bottom:**
1. **`LESSON.interactive.html`** — the interactive HTML/3D lesson, built **first**, the primary teaching
   artifact. It **must embed retrieval**: ≥1 *predict-before-reveal* prompt and ≥1 *quiz-with-instant-
   feedback*, so it rewards effort instead of being watched passively. Match the established course visual
   system (light cards + dark runtime console + bilingual EN/中文, vanilla JS, self-contained) seen in
   `week01/day0{3,4,5}/LESSON.interactive.html`.
2. **`LESSON.bilingual.md`** — the *textbook* companion (reference text), authored second.
3. **`HOMEWORK.bilingual.md`** / **`RECALL.bilingual.md`** / **`SOLUTIONS.bilingual.md`**.
4. The learner's **`.py`** + tests.

`RECALL.md` + `week01/review-queue.md` + `misconceptions.md` remain the **cold spaced re-tests** — the
recall layer lives *outside* the lesson HTML; the embedded retrieval inside the HTML is in-the-moment.

**Density floor (both the HTML and the textbook md):** every concept gets **3 escalating depth passes**
(intuition/analogy → precise mechanism → under-the-hood/edge cases) **and 3 worked examples graded
easy → hard**. Keep within working memory — tight passes, not pages.

**Weekly:** when a week completes, produce **`weekNN/CHEATSHEET.html`** — one-page, print-clean, EN + 中文,
covering that week's concepts (D1–D6). Inherit the course visual tokens for consistency.

**Unchanged and still in force:** the **context7 primary-source rule** below (library content in the HTML
still cites primary URLs inline) and the **pyright Definition-of-Done gate** above.

## Sourcing library/technical content — context7 is the primary source
> Added 2026-06-25 after a before/after authority eval
> (`progress/2026-06-25_context7-authority-eval.md`): context7-grounded NumPy material scored ~100%
> primary-source-cited vs ~0% for the parametric baseline.

For any lesson or homework whose subject is a **library, framework, or API** — NumPy (Week 2)
onward: pandas, scikit-learn, PyTorch, Hugging Face, LangChain/LlamaIndex, MATLAB toolboxes, etc. —
the **primary source is the context7 MCP**:
1. `resolve-library-id` (prefer a **High** Source-Reputation, high Benchmark source — usually the
   official docs site), then `query-docs` for the specific topic;
2. **cite the returned primary URLs inline** in the lesson (version-pinned, e.g. NumPy 2.4) and add
   a Sources list. Do not assert library facts from parametric memory when context7 can source them.

**Scope boundary:** context7 indexes *documentation, not news*. It is **not** a source for the
**Weekly AI Industry Digest** (S4 frontier slot) — that keeps its own primary news/market sourcing
(web fetch/search + the Friday cloud routine). This rule strengthens, and never overrides, the
`/teach` principle *"never rely on parametric knowledge — cite high-trust sources."*
