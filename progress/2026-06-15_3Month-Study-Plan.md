# 3-Month AI Career Study Plan & Progress Record

- **Owner:** Career-changer (science/engineering background, 9 yrs since graduation, strong engineering thinking, no prior programming work experience)
- **Target role:** Industrial large-model (大模型) fine-tuning + Agent development
- **Geography:** Phase 1 — China first-tier cities (Beijing / Shanghai / Guangzhou / Shenzhen); Phase 2 (long-term) — Germany, related field
- **Plan window:** 2026-06-16 → 2026-09-12 (13 weeks; Week 1 starts Monday 2026-06-16)
- **Cadence:** 6 days/week (Mon–Sat), Sunday off. **Default target now = 6 h focused learning + 2 h project/application buffer/day**; 10 h/day is an optional sprint ceiling, not the baseline.
- **Created:** 2026-06-15  | **Last updated:** 2026-06-26  | **Status:** 🟢 Active — recalibrated to a portfolio-first plan; Week 1 Day 5 homework pending

> This file is BOTH the study plan AND the live progress record. As you complete exercises,
> send them to me and I update the tracking table + completion log below. See **§7 Default
> Requirements** for the standing rules (completion updates + weekly frontier refresh).

---

## §0 — 2026-06-26 Recalibration: Evaluation & Revision Patch

**Verdict:** The original plan has the right strategic direction (industrial LLM applications,
RAG/Agents, PEFT/fine-tuning, production serving), but the old schedule tries to cover too many
fields before producing enough proof. For a career-changer with no programming work experience,
the strongest 13-week outcome is **3 credible portfolio artifacts + interview narrative**, not a
survey of MATLAB, C++, ML, DL, Transformers, RAG, agents, edge multimodal, video understanding,
vLLM, and TensorRT-LLM all at once.

**Keep as core:**
- Python engineering habits, Git, tests, pyright, notebook/script workflow.
- NumPy/pandas/data cleaning, but tied to real data and written reports.
- PyTorch + Hugging Face + PEFT/LoRA, but project-first rather than theory-first.
- RAG + Agent development as the main target-role skill, with evaluation and observability.
- vLLM/SGLang as practical serving options for the capstone.

**Downgrade or defer:**
- **MATLAB:** remove from the active 13-week plan. It may be useful in some engineering contexts,
  but it does not strengthen the target 大模型应用/Agent portfolio enough to justify a full week now.
- **C++:** move to a light "reading literacy" track only. Do not spend 2 weeks trying to look like a
  C++ engineer; revisit C++ after the first AI role or for inference-engine specialization.
- **TensorRT-LLM:** optional stretch only. It is valuable, but it is a hardware/deployment depth
  topic; use it only after a vLLM/SGLang baseline exists.
- **Edge multimodal and video understanding:** keep as elective showcase ideas, not required
  milestones. The primary job-search proof should be text/document industrial AI first.

**Add explicitly:**
- Linux/CLI and deployment hygiene: `uv`/conda, Git branches, `pytest`, `pyright`, `.env`, logs,
  FastAPI, Docker basics where useful.
- Evaluation loops: train/validation/test, error analysis, RAG faithfulness/relevance/context metrics,
  agent tool-call accuracy, latency/throughput notes.
- Portfolio writing: every milestone ends with a README, demo script, failure log, and 3-5 resume
  bullets in STAR/project-impact style.
- EU/Germany readiness: basic AI Act/GDPR/trusted-AI awareness for industrial deployments, especially
  logging, human oversight, documentation, and risk framing.

**Portfolio milestones now drive the plan:**

| Milestone | Target window | Must ship | Why it matters |
|-----------|---------------|-----------|----------------|
| **M1 — Python/data project** | by revised Week 4 | A tested Python package or notebook/script pair that cleans and analyzes a real industrial-ish dataset, with README + findings | Proves programming fundamentals, data literacy, Git, testing, and technical writing |
| **M2 — Fine-tune + deploy** | by revised Week 8 | A small open model fine-tuned with PEFT/LoRA, evaluated with error analysis, served via FastAPI or local API | Proves the core LLM application loop beyond prompt demos |
| **M3 — RAG + Agent system** | by revised Week 12 | RAG over technical docs + tool-using agent + eval harness + traces/logs | Directly matches 大模型应用/Agent job postings |
| **M4 — Serving/portfolio polish** | final week | vLLM or SGLang serving benchmark, optional TensorRT-LLM stretch, polished README/demo/resume bullets | Turns learning into interview-ready evidence |

**Conflict rule:** where this §0 conflicts with the older daily tables below, **§0 and the revised
§3/§5 milestone plan win**. The Month 1 tables remain useful as already-authored `/teach` lesson
material, but future expansion should follow the project gates above.

---

## §1 — Strategic Q&A (answers to the LearningPlan brief)

### Q1. Is automotive Germany's highest-potential AI sector? + Top 10

**Verdict:** No — not the *single* highest. Automotive is a **top-3 flagship** sector (autonomous
driving, ADAS, smart manufacturing; ~€1.8 B automotive-AI revenue in 2023; ~70 % AI adoption among
large automotive firms), but **Industrial / Manufacturing AI (Industrie 4.0)** has the higher growth
ceiling and is where Germany holds *global* leadership. The German manufacturing-AI market is
projected to grow from ~USD 2.14 B (2026) to ~USD 10.5 B (2030) at **~35.8 % CAGR**, and the
industrial sector leads national AI adoption at **58.7 %**.

**Why this matters for you:** Your stated direction — *industrial* large-model fine-tuning + agents —
maps directly onto Germany's strongest AI sector, not a side one. The same skill set (industrial
LLM/agent + on-prem/edge deployment) is portable from China's manufacturing/industrial AI scene to
Germany's. This is a strong, coherent China→Germany bridge.

**Top 10 highest-potential AI sectors in Germany (synthesized: growth × AI-intensity × strategic fit):**

| # | Sector | Why high-potential | Anchor players |
|---|--------|--------------------|----------------|
| 1 | **Industrial Manufacturing / Industrie 4.0** | Highest CAGR (~35.8 %); German global leadership; predictive maintenance, quality control, digital twins, robotics | Siemens, Bosch, NVIDIA×Deutsche Telekom industrial AI cloud |
| 2 | **Automotive & Autonomous Mobility** | ADAS, autonomous driving, in-cabin AI; €1.8 B (2023) | VW, Mercedes-Benz, BMW, Bosch, Continental |
| 3 | **Enterprise / B2B Software & Sovereign LLMs** | "Trustworthy, applied AI" niche; B2B focus | SAP, Aleph Alpha |
| 4 | **Healthcare & Pharma / Drug Discovery** | €850 M (2023), ~32 % CAGR; diagnostics + drug discovery | Bayer, BioNTech, Merck, Siemens Healthineers |
| 5 | **Logistics & Supply Chain** | €550 M (2023); route optimization, multi-agent supply chains | DHL, Deutsche Bahn, DB Schenker |
| 6 | **Defense & Security Tech** | Fast-growing post-2024; sovereign AI | Helsing, Rheinmetall |
| 7 | **Chemicals & Process Industry** | Process optimization, materials discovery | BASF, Covestro |
| 8 | **Energy / CleanTech / Climate Tech** | Grid optimization, ESG, climate modeling | E.ON, RWE, Siemens Energy |
| 9 | **Financial Services / Fintech & InsurTech** | Fraud, risk, underwriting (Frankfurt hub) | Deutsche Bank, Allianz, N26 |
| 10 | **AgriTech / AgriFood** | Precision agriculture (gov High-Tech Strategy priority) | Bayer Crop Science, Claas |

*Government High-Tech Strategy explicitly prioritizes automotive, chemicals, biotech, cleantech,
medicine, agrifood — consistent with the ranking above.*

### Q2. Are the 3 directions mainstream in China first-tier LLM job postings?

| Direction | Mainstream? | Assessment | How I weight it in your plan |
|-----------|-------------|------------|------------------------------|
| **3. Inference serving — vLLM / SGLang / TensorRT-LLM** | ✅ **Yes — mainstream / valuable** | Production LLM roles increasingly expect awareness of high-throughput serving, batching, KV-cache/memory tradeoffs, and OpenAI-compatible serving APIs. | **Required as a measured capstone skill, not an early deep dive.** vLLM or SGLang baseline required; TensorRT-LLM optional stretch. |
| **1. Edge-side multimodal deployment — MobileCLIP / TinyGPT-V-class** | 🟡 **Niche / bonus (growing)** | Not a universal requirement for mainstream 大模型应用 roles. Strong differentiator at terminal/IoT/automotive-cockpit teams (小米, 荣耀, vivo, OPPO, 地平线). Strategically aligned with your *industrial/edge* focus. | **Elective showcase.** Keep as a later branch only after M2/M3 are healthy. |
| **2. Video understanding — Video-LLaMA / TimeSformer-class** | 🟡 **Emerging / sector-specific** | Multimodal is increasingly mainstream; video-specific still emerging vs. image+text. Valued in short-video/content (字节, 快手), security/surveillance, autonomous driving. | **Elective.** Do not block core Agent/RAG/fine-tune portfolio work. |

**2026-06-26 recalibrated takeaway:** Make **RAG/Agent + PEFT/LoRA + evaluation + API deployment**
the non-negotiable center. Treat **vLLM or SGLang serving** as the final measured production skill.
Treat **TensorRT-LLM, edge multimodal, and video understanding** as stretch/elective topics that
must not crowd out portfolio evidence.

**General market note (both cities + base reality):** 2025–2026 大模型应用 roles cluster on:
LangChain/LlamaIndex for Agent/RAG pipelines · PEFT (LoRA/QLoRA) fine-tuning of open models
(Llama 3.x, Qwen, Mistral) · RAG with vector DBs · production serving (vLLM/TensorRT-LLM) ·
a portfolio project with real depth. "基座大模型" (pretraining) roles are few and demand
top-985 / published-paper profiles; **大模型应用 is the realistic entry path** for you — this plan
targets it.

*Sources at end of file.*

---

## §2 — Daily Template (every study day, Mon–Sat)

| Slot | Duration | Purpose |
|------|----------|---------|
| **S1 — Core Concept** | 2 h | The day's primary concept, sourced from authoritative material |
| **S2 — Guided Practice** | 2 h | Worked examples, small drills, or code reading tied to the concept |
| **S3 — Math / Recall** | 1 h | Focused math plus cold recall / spaced review |
| **S4 — Frontier / Docs / Industry** | 1 h | Current tools, official docs, or Friday AI Industry Digest |
| **Project / Homework Block** | 2 h | Code, tests, README, eval notes, or milestone artifact work |

**Default total:** 6 h focused learning + 2 h project/application = **8 h/day**.
**Optional sprint ceiling:** add up to 2 h for catch-up or deep project work, but do not make 10 h/day
the assumed baseline.

Suggested clock: 08:30–10:30 (S1) · 10:45–12:45 (S2) · 14:00–15:00 (S3) · 15:15–16:15 (S4) ·
19:00–21:00 (Project/Homework). Adjust to your chronotype; keep the block sizes.

### Frontier Track (the rotating S4 "most current directions" slot)
- **R1-R4:** Tooling, official docs literacy, Hugging Face orientation, embeddings/vector DB concepts.
- **R5-R8:** PyTorch/Transformers/PEFT applied to the fine-tune+API milestone.
- **R9-R12:** RAG, Agent workflow patterns, evaluation, tracing/logging, and reliability.
- **R13:** vLLM or SGLang serving benchmark; TensorRT-LLM only if the baseline is already healthy.
- **Every Friday:** S4 = **Weekly AI Industry Digest** with direct source links; use it to re-tune
  upcoming S4 content without derailing the current milestone.

---

## §3 — Revised 13-Week Macro Plan (Portfolio-First)

> **Calendar note (2026-06-26):** The learner is behind the original date grid because Week 1 is being
> taught in a deeper `/teach` format. From here, the plan is **gate-based**: do not compress the
> portfolio projects to preserve a calendar illusion. If a gate slips, move the target date.

| Phase | Target window | Core learning | Math/stat focus | Frontier/production focus | Gate to pass |
|-------|---------------|---------------|-----------------|---------------------------|--------------|
| **Recovery + Week 1 close** | 06-26 → 06-29 | Finish W1 D5 homework + D6 consolidation; clean progress/status | LA I recap | None unless time remains | Day 5 homework graded; Day 6 mini-project scoped |
| **P1 — Python/data foundation** | 06-30 → 07-19 | Python engineering, NumPy, pandas, notebooks/scripts, testing, Git | Linear algebra, derivatives, probability basics | Hugging Face orientation; embeddings/vector DB concepts | **M1 shipped:** real dataset analysis + README + tests/checks |
| **P2 — ML/DL + fine-tune/deploy** | 07-20 → 08-15 | scikit-learn basics, PyTorch fundamentals, Transformers, PEFT/LoRA | Metrics, optimization, error analysis | FastAPI inference service; model cards; experiment logs | **M2 shipped:** LoRA fine-tune + evaluation + API |
| **P3 — RAG + Agent core** | 08-17 → 09-05 | RAG pipeline, chunking/retrieval/reranking, tool-calling agents, LangGraph/LlamaIndex patterns | Retrieval metrics, faithfulness, latency/quality tradeoffs | RAGAS-style eval, tracing/logging, prompt/version control | **M3 shipped:** industrial-doc RAG + tool agent + eval report |
| **P4 — Serving + portfolio polish** | 09-07 → 09-12 | Capstone integration, README/demo/resume bullets, mock interviews | Metrics consolidation | vLLM or SGLang benchmark; TensorRT-LLM optional stretch | **M4 shipped:** public portfolio package + interview script |

### Priority Stack After Recalibration

| Priority | Skill/theme | Decision |
|----------|-------------|----------|
| P0 | Python, Git, tests, pyright, CLI, project structure | Non-negotiable; every milestone must use it |
| P0 | RAG + Agent + evaluation | Main job-search target; gets the most project depth |
| P0 | PEFT/LoRA + model evaluation + API deployment | Required for "fine-tuning + application" credibility |
| P1 | vLLM or SGLang serving | Use in final project as a measured production-serving comparison |
| P1 | Docker/Linux basics | Add as needed for reproducible demos, not as a separate theory week |
| P2 | TensorRT-LLM | Stretch only after a working vLLM/SGLang baseline |
| P2 | Edge multimodal/video understanding | Elective showcase only; do not block core portfolio |
| Deferred | MATLAB | Removed from active 13-week plan |
| Deferred | C++ | Reading-literacy only; no standalone 2-week block |

> **Detail policy:** Month 1's existing daily tables remain as authored learning material. Future
> weeks should be expanded only when the next milestone is near, using Context7 for library/API
> sources and DeepWiki for reading complex repos such as `vllm`, `transformers`, or `sglang`.

---

## §4 — MONTH 1 (Weeks 1–4): full daily detail

### Week 1 (06-16 → 06-21) — Python OOP + Linear Algebra I + Orientation
**Weekly goal:** Solid object-oriented Python (classes, inheritance, dunder methods, composition);
comfortable with vectors/matrices and core linear-algebra operations; dev environment fully set up.

| Day | Objective | S1 (2h) | S2 (2h) | S3 Math (1h) | S4 Frontier (2h) | Homework (3h) |
|-----|-----------|---------|---------|--------------|------------------|----------------|
| **D1 Mon** | Classes & objects | Classes, `__init__`, attributes, methods, `self` | Instance vs class attributes; encapsulation, properties | Vectors: notation, addition, scalar mult | Install conda, Git, VS Code; create `pythonlearning` env; clone repo | Build a `BankAccount` class (deposit/withdraw/history) + tests |
| **D2 Tue** | Inheritance & polymorphism | Single/multi inheritance, `super()`, MRO | Polymorphism, method overriding, abstract base classes (`abc`) | Dot product, vector norm, distance | Read: "What is an LLM" + the 3 directions overview (skim, take notes) | Model an `Animal→Dog/Cat` hierarchy + a `Shape` ABC with area() |
| **D3 Wed** | Dunder & data model | `__str__`, `__repr__`, `__eq__`, `__len__`, `__getitem__` | Operator overloading; `__add__`, iterators, `__iter__`/`__next__` | Matrices: definition, transpose, matrix×vector | Set up CUDA-ready PyTorch (CPU ok); verify `torch.__version__` | Build a `Vector2D` class with full operator overloading + iteration |
| **D4 Thu** | Composition & design | Composition vs inheritance; dataclasses; `@dataclass` | Type hints, `typing`, mutability, `__slots__` | Matrix multiplication; identity/inverse intuition | Read vLLM intro (PagedAttention concept, no code) | Refactor D1 account into a composed `Bank`+`Account`+`Ledger` |
| **D5 Fri** | Errors, context, modules | Exceptions, custom exceptions, `try/except/finally` | Context managers (`with`, `__enter__/__exit__`), modules/packages | Linear combinations, span (intuition) | **Weekly AI Digest #1** (I provide) + reflect on direction fit | Write a context-managed file logger + a small package with `__init__.py` |
| **D6 Sat** | Consolidate + mini-project | Review week; quiz yourself | Mini-project build | Week-1 math recap + 10 practice problems | Catch-up / re-read weak spots | **Mini-project:** CLI contact book (OOP, persistence to JSON, custom exceptions) — push to GitHub |

### Week 2 (06-23 → 06-28) — NumPy + Linear Algebra II + Calculus I
**Weekly goal:** Vectorized thinking in NumPy (arrays, broadcasting, indexing, linear algebra ops);
matrix operations and determinants; derivatives and the idea of gradients.

| Day | Objective | S1 (2h) | S2 (2h) | S3 Math (1h) | S4 Frontier (2h) | Homework (3h) |
|-----|-----------|---------|---------|--------------|------------------|----------------|
| **D1 Mon** | ndarray basics | Creating arrays, dtypes, shape, reshape | Indexing, slicing, fancy/boolean indexing | Determinants (2×2, 3×3), meaning | Env: Jupyter/notebook workflow; first notebook | NumPy drills: build arrays 10 ways; reshape/slice exercises |
| **D2 Tue** | Broadcasting & vectorization | Broadcasting rules, axis operations | Vectorization vs loops; `np.where`, masking | Matrix inverse; solving Ax=b | Skim MobileCLIP/edge-CLIP idea (concept only) | Re-implement 5 loop-based functions as vectorized NumPy |
| **D3 Wed** | Linear algebra in NumPy | `@`, `np.linalg` (dot, matmul, inv, solve) | Eigenvalues/eigenvectors via `np.linalg.eig` (intuition) | Eigen-intuition: what eigenvectors mean | Read TimeSformer/Video-LLaMA overview (concept) | Implement PCA-by-hand on toy 2D data with NumPy |
| **D4 Thu** | Numerical computing | Random, statistics (`mean/std/var`), `axis` | Stacking, splitting, `concatenate`, `meshgrid` | Derivatives: limit definition, rules | Benchmark numpy vs python loop timing | Vectorized image-as-array manipulation (grayscale, flip, crop) |
| **D5 Fri** | Performance & I/O | Views vs copies, memory layout, `np.save/load` | `np.einsum` intro; practical perf tips | Chain rule (intuition + examples) | **Weekly AI Digest #2** + re-tune frontier | Speed-optimize a slow numeric function; report before/after |
| **D6 Sat** | Consolidate + mini-project | Review | Mini-project | Calc-I recap + problems | Catch-up | **Mini-project:** k-NN classifier from scratch in pure NumPy on a toy dataset |

### Week 3 (06-30 → 07-05) — Pandas + Calculus II + Probability I
**Weekly goal:** Real data wrangling (Series/DataFrame, joins, groupby, time series, cleaning);
integrals & partial derivatives; probability foundations.

| Day | Objective | S1 (2h) | S2 (2h) | S3 Math (1h) | S4 Frontier (2h) | Homework (3h) |
|-----|-----------|---------|---------|--------------|------------------|----------------|
| **D1 Mon** | Series & DataFrame | Construction, indexing, `loc/iloc`, dtypes | Reading CSV/Excel/JSON; inspecting data | Partial derivatives; gradient vector | Hugging Face Hub tour (datasets/models) | Load a real Kaggle CSV; profile it (shape, nulls, dtypes) |
| **D2 Tue** | Cleaning & transforming | Missing data, `fillna/dropna`, `astype`, `apply/map` | String ops, datetime parsing, categoricals | Integrals: definite/indefinite, area | Read: tokenization basics (BPE) | Clean a messy dataset end-to-end; document each step |
| **D3 Wed** | Aggregation | `groupby`, agg, transform, pivot tables | `merge/join/concat`; reshaping (melt/pivot) | Gradient & directional derivative | Embeddings intuition (vectors for text) | Answer 5 analytical questions on a dataset via groupby/merge |
| **D4 Thu** | Time series & viz | Datetime index, resample, rolling windows | Plotting with pandas/matplotlib basics | Probability: sample space, events, axioms | Vector DB concept (FAISS/embeddings) skim | Build a time-series report (resample + rolling avg + plot) |
| **D5 Fri** | Real workflow | EDA workflow on a real dataset | Performance, `category` dtype, method chaining | Conditional probability, Bayes' theorem | **Weekly AI Digest #3** + re-tune | Full EDA notebook on a chosen dataset (push to GitHub) |
| **D6 Sat** | Consolidate + mini-project | Review | Mini-project | Prob-I recap + Bayes problems | Catch-up | **Mini-project:** end-to-end data analysis (clean→group→visualize→insights) write-up |

### Week 4 / R4 (07-07 → 07-12 target) — M1 Data Portfolio Polish + ML Bridge
**Weekly goal:** Turn NumPy/pandas work into the first portfolio artifact: a reproducible data
analysis project with clean code, checks, README, findings, and resume bullets. MATLAB is removed;
C++ is deferred to reading literacy after the core portfolio is healthy.

| Day | Objective | S1 (2h) | S2 (2h) | S3 Math/Recall (1h) | S4 Frontier/Docs (1h) | Project/Homework (2h) |
|-----|-----------|---------|---------|----------------------|------------------------|------------------------|
| **D1 Mon** | Project framing | Pick industrial-ish dataset; define 5 analysis questions | Repo structure, data dictionary, reproducibility checklist | Probability recap: events, conditional probability | Dataset provenance + licensing notes | Create project skeleton + first data profile |
| **D2 Tue** | Cleaning pipeline | Missing values, types, outliers, duplicate rules | Script/notebook split; repeatable cleaning | Distributions, mean/variance, z-score intuition | Read model/data-card examples | Build `clean_data.py` or notebook section + checks |
| **D3 Wed** | Analysis depth | Groupby/joins/time windows; visualization choices | Turn charts into claims with evidence | Correlation vs causation; leakage awareness | Embeddings/vector DB concept recap | Draft findings with plots + caveats |
| **D4 Thu** | Code quality | Tests/checks for data assumptions; pyright where applicable | README structure: problem, data, method, findings, limits | Metric selection and baseline thinking | Hugging Face datasets tour | Clean repo, run checks, write README first draft |
| **D5 Fri** | Portfolio packaging | Failure log: what broke, what changed, what remains | Resume bullets in STAR/project-impact style | Month-1 math recap | **Weekly AI Digest #4** + M1 relevance check | Polish README + prepare short demo script |
| **D6 Sat** | M1 gate review | Final project review against M1 rubric | Retrospective + next-phase setup | Cold recall from Weeks 1-3 | Plan R5 ML baseline dataset/task | **Ship M1:** reproducible analysis + README + demo notes |

---

## §5 — MONTHS 2–3 (Weeks 5–13): revised milestone plan

> Block-by-block detail for each week will be expanded when the next milestone is near. Each day
> still uses the §2 rhythm, but the standing rule is now: **project artifact first, theory in service
> of the artifact**. The older subject-tour outline below is archived after this revised plan and is
> superseded where conflicts exist.

### Revised execution map

| Revised week | Focus | Build target | Daily emphasis |
|--------------|-------|--------------|----------------|
| **R1 — Finish Week 1** | D5/D6 closeout | `logkit` FileLogger + Week-1 mini-project/readme cleanup | Cold recall, homework grading, pyright/pytest, progress sync |
| **R2 — NumPy + data project start** | Array thinking, vectorization, notebook hygiene | Dataset profile + first clean notebook/script | Context7-sourced NumPy; math = matrix ops + derivatives |
| **R3 — pandas + analysis report** | Cleaning, joins, groupby, time series/basic viz | Full EDA report on industrial-ish data | Error log, method chaining, data-quality notes |
| **R4 — M1 polish** | Turn analysis into portfolio artifact | **M1:** cleaned repo, README, findings, reproducibility notes | Resume bullets + short demo script |
| **R5 — ML fundamentals** | scikit-learn, metrics, splits, baselines | Baseline classifier/regressor + error analysis | Metrics > algorithm zoo; avoid deep SVM/tree theory |
| **R6 — PyTorch fundamentals** | tensors, autograd, `nn.Module`, training loop | Small PyTorch model with tracked experiments | Training loop, overfitting, debugging |
| **R7 — Transformers + PEFT** | tokenization, pretrained models, LoRA/QLoRA | Domain text dataset + first LoRA run | Hugging Face, PEFT, eval set, model card notes |
| **R8 — M2 deploy** | API + evaluation + packaging | **M2:** LoRA fine-tune served via FastAPI/local API | Latency, error cases, README, demo |
| **R9 — RAG foundations** | embeddings, chunking, vector DB, retrieval | Document ingest + baseline RAG Q&A | Retrieval quality, source attribution, failure cases |
| **R10 — RAG evaluation** | reranking, query rewrite, eval harness | RAG quality report with test questions | RAGAS-style metrics, faithfulness/relevance |
| **R11 — Agent workflows** | tool calling, state, planning, guardrails | Tool-using agent over the RAG system | LangGraph/LlamaIndex patterns; logs/traces |
| **R12 — M3 integration** | Industrial assistant | **M3:** RAG + tool agent + eval report | Reliability, observability, risk notes |
| **R13 — M4 polish/serving** | Portfolio + serving comparison | vLLM or SGLang benchmark; optional TensorRT-LLM stretch | README, demo video, interview stories |

### Revised frontier rules for Months 2-3

- **Friday S4 remains the Weekly AI Industry Digest**, but digest claims must carry direct source
  links. If the cloud routine fails, produce the digest manually before changing next week's S4.
- **vLLM/SGLang:** teach as "serve and measure" in R13, with a small baseline comparison against
  Hugging Face/FastAPI. Do not deep-dive scheduler/KV-cache internals unless the capstone is already
  healthy.
- **TensorRT-LLM:** optional stretch only; use if GPU/tooling is ready and the baseline deployment is
  complete.
- **Edge multimodal/video:** optional single-demo branch after M3, not a blocker.
- **AI governance:** add one lightweight section to M2/M3 READMEs covering data provenance, privacy,
  eval limits, human oversight, and deployment risk.

### Archived original outline (superseded by the revised execution map above)

### Week 5 (07-14 → 07-19) — C++ II (OOP, STL) + Probability II
**Goal:** C++ classes, RAII, STL containers/algorithms; random variables & distributions.
- **D1** C++ classes, constructors/destructors, RAII → *HW: implement a `Matrix` class.*
- **D2** Operator overloading, `const`-correctness, references → *HW: extend `Matrix` with operators.*
- **D3** STL containers (`vector/map/set/unordered_map`) → *HW: word-frequency with `map`.*
- **D4** STL algorithms, iterators, lambdas → *HW: sort/filter/transform pipeline.*
- **D5** Templates intro; smart pointers (`unique_ptr/shared_ptr`) → **Digest #5** → *HW: templated stack.*
- **D6** Consolidate → *Mini-project: small CLI tool in modern C++ (push).*
- **Math:** random variables, expectation/variance, Bernoulli/Binomial/Normal.
- **Frontier (P2 start):** run a CLIP/MobileCLIP inference demo; understand image-text embeddings.

### Week 6 (07-21 → 07-26) — Machine Learning I + Linear Algebra III
**Goal:** Supervised learning core: linear/logistic regression, gradient descent, regularization,
train/val/test, scikit-learn workflow.
- **D1** ML framing, data splits, scikit-learn API → *HW: load dataset, baseline model.*
- **D2** Linear regression (closed form + gradient descent) → *HW: implement GD regression in NumPy.*
- **D3** Logistic regression, decision boundary, sigmoid → *HW: binary classifier from scratch.*
- **D4** Regularization (L1/L2), bias-variance, feature scaling → *HW: compare Ridge/Lasso.*
- **D5** Cross-validation, metrics (accuracy/precision/recall/ROC) → **Digest #6** → *HW: full CV experiment.*
- **D6** Consolidate → *Mini-project: end-to-end regression on real data (push).*
- **Math:** SVD, PCA derivation, matrix calculus (gradients of vector/matrix expressions).
- **Frontier:** benchmark a small model's latency/throughput; intro to quantization concepts.

### Week 7 (07-28 → 08-02) — Machine Learning II + Optimization/Calculus III
**Goal:** Trees, ensembles, SVM, clustering, dimensionality reduction, model selection.
- **D1** Decision trees, entropy/gini → *HW: train + visualize a tree.*
- **D2** Ensembles: Random Forest, Gradient Boosting (XGBoost/LightGBM) → *HW: tune a GBM.*
- **D3** SVM (margins, kernels) → *HW: SVM on non-linear data.*
- **D4** Unsupervised: k-means, hierarchical, PCA applied → *HW: cluster + PCA-visualize.*
- **D5** Model selection, pipelines, hyperparameter search → **Digest #7** → *HW: `GridSearchCV` pipeline.*
- **D6** Consolidate → *Mini-project: Kaggle-style tabular competition entry (push).*
- **Math:** convex vs non-convex, gradient/SGD/momentum/Adam intuition, Lagrange multipliers.
- **Frontier:** edge-deployment concepts — quantization (INT8), distillation, ONNX export.

### Week 8 (08-04 → 08-09) — Deep Learning I + Discrete Math II + Number Theory
**Goal:** Neural nets from scratch, backprop, PyTorch fundamentals, training loop.
- **D1** Perceptron→MLP, activation functions → *HW: forward pass by hand + NumPy.*
- **D2** Backpropagation derivation → *HW: 2-layer net backprop in pure NumPy.*
- **D3** PyTorch tensors, autograd → *HW: re-implement the net in PyTorch.*
- **D4** `nn.Module`, optimizers, loss functions, training loop → *HW: train MLP on MNIST.*
- **D5** Overfitting, dropout, batchnorm, data loaders → **Digest #8** → *HW: improve MNIST acc.*
- **D6** Consolidate → *Mini-project: full PyTorch classifier with logging (push).*
- **Math:** graphs/trees, combinatorics; number theory (modular arithmetic, GCD, primes) — ties to hashing/crypto/positional encodings.
- **Frontier:** dissect attention math behind Video-LLaMA / TimeSformer (concept + diagrams).

### Week 9 (08-11 → 08-16) — Deep Learning II + Frontier Specialization begins
**Goal:** CNNs, RNNs/LSTMs, regularization, transfer learning.
- **D1** CNNs: convolution, pooling, architectures → *HW: CNN on CIFAR-10.*
- **D2** Transfer learning, fine-tuning pretrained CNNs → *HW: fine-tune ResNet.*
- **D3** RNN/LSTM/GRU for sequences → *HW: char-level text generator.*
- **D4** Regularization, schedulers, mixed precision → *HW: training-tricks ablation.*
- **D5** Experiment tracking (W&B/TensorBoard) → **Digest #9** → *HW: tracked experiment.*
- **D6** Consolidate → *Mini-project: image classifier deployed as a script (push).*
- **Frontier (P3):** **serve a small LLM with vLLM**; measure throughput vs naive HF generate.

### Week 10 (08-18 → 08-23) — DL III → Transformers + NLP I
**Goal:** The Transformer architecture end-to-end; tokenization, embeddings, attention, NLP basics.
- **D1** Attention & self-attention math → *HW: implement scaled dot-product attention.*
- **D2** Multi-head attention, positional encoding → *HW: build a mini multi-head block.*
- **D3** Full Transformer (encoder/decoder), the "Attention Is All You Need" architecture → *HW: annotate a reference implementation.*
- **D4** Tokenization (BPE/WordPiece), embeddings, NLP preprocessing → *HW: train a BPE tokenizer.*
- **D5** Hugging Face `transformers` basics → **Digest #10** → *HW: run inference with a pretrained model.*
- **D6** Consolidate → *Mini-project: text classifier with a pretrained transformer (push).*
- **Frontier:** **accelerate the Week-9 model with TensorRT-LLM**; compare vLLM vs TensorRT-LLM.

### Week 11 (08-25 → 08-30) — NLP II + LLM basics + PEFT/LoRA
**Goal:** Pretrained-model fine-tuning, PEFT (LoRA/QLoRA), prompt engineering, LLM mechanics.
- **D1** Pretraining vs fine-tuning vs in-context learning → *HW: prompt-engineering exercises.*
- **D2** Full fine-tuning vs PEFT; LoRA/QLoRA theory → *HW: LoRA fine-tune a small open model.*
- **D3** Datasets for fine-tuning, instruction tuning → *HW: build an instruction dataset.*
- **D4** Evaluation of LLMs (perplexity, task metrics, LLM-as-judge) → *HW: evaluate your fine-tune.*
- **D5** Quantization (GPTQ/AWQ/GGUF) for deployment → **Digest #11** → *HW: quantize + serve.*
- **D6** Consolidate → *Mini-project: a LoRA-fine-tuned domain assistant (push).*
- **Frontier:** **edge multimodal hands-on** — deploy MobileCLIP / a TinyGPT-V-class model; measure footprint.

### Week 12 (09-01 → 09-06) — Agent development + RAG I
**Goal:** Build agents (tools, planning, memory) and a working RAG pipeline.
- **D1** Agent concepts: ReAct, tool-calling, planning loops → *HW: a tool-using agent (calculator+search).*
- **D2** LangChain / LlamaIndex frameworks → *HW: multi-tool agent.*
- **D3** RAG architecture: chunking, embeddings, vector DB (FAISS/Chroma) → *HW: ingest docs → retrieve.*
- **D4** Retrieval + generation wiring; prompt templates → *HW: end-to-end RAG Q&A.*
- **D5** Agent memory, multi-step workflows → **Digest #12** → *HW: stateful agent.*
- **D6** Consolidate → *Mini-project: a RAG assistant over your own notes (push).*
- **Frontier:** **video-understanding mini-project** (Video-LLaMA/TimeSformer-class) — clip → caption/QA.

### Week 13 (09-08 → 09-12) — RAG II + Capstone
**Goal:** Production-minded RAG + a portfolio capstone integrating Agent + RAG + a frontier direction.
- **D1** Advanced retrieval: hybrid search, re-ranking, query rewriting → *HW: add re-ranker.*
- **D2** RAG evaluation (faithfulness, relevance, RAGAS-style) → *HW: eval harness.*
- **D3** Serving the capstone with vLLM/TensorRT-LLM → *HW: deploy behind an API.*
- **D4** Capstone build day → *HW: integrate Agent+RAG+inference acceleration.*
- **D5** Capstone polish + docs + demo → **Digest #13** → *HW: write README + record demo.*
- **D6** **Final review + portfolio** → *Publish capstone + résumé bullets mapping skills to job requirements (push).*
- **Capstone target:** *An industrial-domain assistant: RAG over technical docs + a tool-using agent +
  served with vLLM (and one of: edge-multimodal OR video-understanding component) — the portfolio
  centerpiece for 大模型应用 / Agent roles.*

---

## §6 — Progress Tracking

**Legend:** ☐ not started · 🔄 in progress · ✅ done (exercises reviewed) · ⏭️ skipped/deferred

### Revised gate-level status
| Gate | Theme | Status | Notes |
|------|-------|--------|-------|
| R1 | Finish Week 1 + close D5/D6 | 🔄 | D4 fixed/graded; D5 lesson taught; D5 homework pending; D6 still to scope |
| R2 | NumPy + data project start | ☐ | W2D1 Context7-sourced demonstrator lesson exists; full 4-file `/teach` set deferred |
| R3 | pandas + analysis report | ☐ | |
| R4 / M1 | Python/data portfolio artifact | ☐ | Must ship README + reproducible analysis + resume bullets |
| R5 | ML fundamentals | ☐ | Metrics/error analysis > broad algorithm survey |
| R6 | PyTorch fundamentals | ☐ | |
| R7 | Transformers + PEFT | ☐ | |
| R8 / M2 | LoRA fine-tune + API deployment | ☐ | |
| R9 | RAG foundations | ☐ | |
| R10 | RAG evaluation | ☐ | |
| R11 | Agent workflows | ☐ | |
| R12 / M3 | Industrial RAG + tool agent | ☐ | |
| R13 / M4 | Serving benchmark + portfolio polish | ☐ | vLLM or SGLang required; TensorRT-LLM optional stretch |

### Completion log (newest first)
*(Each time you send completed exercises, I append a dated entry here: what you did, what was
correct, what to fix, and any pace adjustment.)*
- **2026-06-26** — **3-month plan evaluated and recalibrated.** Updated the plan from a
  subject-tour schedule into a portfolio-first roadmap with four gates: **M1 data project → M2
  LoRA fine-tune + API → M3 industrial RAG + tool agent → M4 serving benchmark + portfolio polish**.
  Key decisions: make 6h focused learning + 2h project buffer the baseline; remove MATLAB from the
  active 13-week plan; downgrade C++ to reading literacy; keep vLLM/SGLang as measured serving
  skills; make TensorRT-LLM optional; keep edge multimodal/video as elective showcases only. Added
  explicit evaluation/governance/readme/resume-bullet requirements. Current next step remains:
  **finish Week-1 Day-5 `logkit` homework, grade with `--gate-tests`, then scope D6 consolidation.**
- **2026-06-18** — **Week-1 materials redesigned to the `/teach` standard** (user request). Built the
  week shell (`MISSION.md` / `RESOURCES.md` / `learning-records/` / `README.md`) + all 6 days ×
  `LESSON`+`HOMEWORK`+`RECALL`+`SOLUTIONS`, calibrated to the D1–D2 submissions and grounded in
  Fluent Python / CS61A / 3B1B / MIT 18.06 / *Make It Stick*. Added retrieval practice + a
  spaced-review map. Began EN-ZH bilingual `*.bilingual.md` generation via DeepSeek (all four file
  types, separate files). Recorded the format + bilingual workflow as canonical (new standing rules
  §7.5–6). Detail → `E:\Code\ClaudeCode_Context\2026-06-18_Week1-Redesign.md`.
- **2026-06-16** — **W1 D1 (BankAccount): 9/10 tests pass.** ✅ Correct: encapsulation (read-only `balance` property, no setter), validation on all 4 invalid cases, copy-on-read `history()`, class-attribute counter via `BankAccount.account_count`. 🔧 To fix: implement tested-but-missing `transfer()` (→ 10/10); use `list` + `.append()` for history (not tuple `+=`); simplify to `amount <= 0`; remove dead `pass` after `return`; `:.2f` in `__str__`. Full review → `week01/day01_bankaccount/REVIEW.md`. Pace: on track. Next → D2 inheritance/ABC (materials in `week01/day02_inheritance/LEARNING.md` + `HOMEWORK.md`).
- **2026-06-15** — Plan created and saved as progress record. Pre-start (Week 0). Next: begin Week 1 D1 on Mon 06-16.

---

## §7 — Default Requirements (standing rules for this record)

These are now the permanent operating rules for this study plan. They apply every session:

1. **Completion-driven updates.** Whenever you send me completed exercises/homework, I:
   - review them (correctness, style, what to improve),
   - tick the relevant cells in §6 (☐→🔄→✅) and add a dated **Completion log** entry,
   - adjust upcoming pace/difficulty if you're ahead or behind,
   - commit & push the updated record so you can track it on GitHub.

2. **Weekly frontier refresh (the "S4 current directions" slot).** Each week I retrieve the latest
   AI-industry developments and **re-tune the S4 frontier content** for the coming week — keeping it
   pointed at the next portfolio gate, with standing emphasis on:
   - **RAG / Agent reliability / evaluation** (top priority for the target role),
   - **PEFT/LoRA and model evaluation** (core fine-tuning proof),
   - **vLLM or SGLang serving** (required in the final benchmark),
   - **TensorRT-LLM, edge multimodal, and video understanding** only as stretch/elective branches,
   - plus any newly-hot direction the week's news surfaces, if it helps the next milestone ship.
   The refresh lands as the **Friday "Weekly AI Industry Digest #N"** entry and updates the next
   week's S4 cells.
   - ✅ *Automation (live):* A scheduled cloud routine now generates the digest automatically every
     **Friday 09:00 Asia/Shanghai** and pushes it to this repo.
     - Routine ID: `trig_01DCx7PTmKXrwbJnUu5Xr9Ym` · Manage: https://claude.ai/code/routines/trig_01DCx7PTmKXrwbJnUu5Xr9Ym
     - First run: **Fri 2026-06-19**. The cloud agent appends a numbered `### Digest #N` (see the
       *Weekly AI Industry Digests* section it will create) and commits `update: weekly AI industry digest #N`.
     - ⚠️ **Prerequisite:** the cloud agent needs GitHub access to this repo. If digests don't appear,
       connect GitHub via `/web-setup` or install the Claude GitHub App, then re-run the routine from
       the link above.

3. **Record discipline.** This file stays the single source of truth for the plan + progress. I keep
   §3–§5 aligned with reality as your pace shifts, and I never silently drop a subject — deferrals are
   marked ⏭️ with a reason.

4. **Honesty about pace.** 10 h/day × 6 days is intense. If reality diverges, I'll propose a realistic
   re-plan (e.g., stretch to 16 weeks) rather than pretend the original fits.

5. **`/teach` lesson-format standard (adopted Week 1, 2026-06-18).** Every study day is authored as a
   **`/teach` workspace**, not flat notes:
   - week-level **`MISSION.md`** (Bloom-tagged objectives + the learner's *ability boundary* + a
     mastery bar + a **Spaced-Review Map**), **`RESOURCES.md`** (authoritative sources — e.g. Fluent
     Python, CS61A, 3Blue1Brown, MIT 18.06, primary papers), and **`learning-records/`** (per-session
     memory that powers spaced repetition);
   - per day **`LESSON.md`** + **`HOMEWORK.md`** + **`RECALL.md`** (retrieval-practice quiz) +
     **`SOLUTIONS.md`**.
   - Pedagogy spine = **retrieval practice + spaced/interleaved review + desirable difficulties**
     (*Make It Stick* / Bjork). Homework is **calibrated to the learner's demonstrated growth edges**.

6. **Bilingual workflow.** Author the **complete English** materials first, then pass each through
   **DeepSeek** to produce EN-ZH **`*.bilingual.md`** files *alongside* the English originals — for
   **all four** file types (LESSON/HOMEWORK/RECALL/SOLUTIONS). Superseded drafts are deleted. This
   assumes the **Markdown** teaching approach; for any **other format** (e.g. interactive HTML via
   `/teach`), confirm the choice first.

7. **Portfolio-gate discipline (adopted 2026-06-26).** Future planning is milestone-first:
   **M1 data project → M2 fine-tune+API → M3 RAG+Agent → M4 serving/portfolio polish**. A topic is
   added only if it helps the next gate ship. Every milestone must produce: working code, tests or
   checks, README, failure/error-analysis log, evaluation notes, and 3-5 resume/interview bullets.
   If schedule pressure appears, defer lower-priority topics (TensorRT-LLM, edge multimodal, video,
   C++ reading) rather than reducing project evidence.

---

## §8 — Sources
- [GTAI — AI Industry in Germany](https://www.gtai.de/en/invest/industries/digital-economy/artificial-intelligence)
- [MarketsandMarkets — Germany AI in Manufacturing](https://www.marketsandmarkets.com/ResearchInsight/germany-artificial-intelligence-manufacturing-companies.asp)
- [Trade.gov — Germany AI Manufacturing](https://www.trade.gov/market-intelligence/germany-ai-manufacturing)
- [IndexBox — Germany AI market 2026](https://www.indexbox.io/blog/germanys-ai-market-reaches-297-billion-in-2025-projected-to-grow-to-204-billion-by-2033/)
- [Deutschland in English — Over half of German companies adopt AI in 2026](https://deutschlandinenglish.com/p/over-half-of-german-companies-adopt-ai-in-2026-driven-by-industry-and-large-enterprises)
- [TSA — AI Job Market in Germany 2026](https://www.tsa-bildung.de/en/blog/the-ai-job-market-in-germany-skills-in-demand-for-2026-and-beyond)
- [eCommerce Germany — AI companies to watch 2026](https://ecommercegermany.com/blog/ai-companies-in-germany/)
- [CSDN — 2025 大模型工程师全岗位汇总](https://blog.csdn.net/WANGJUNAIJIAO/article/details/155749669)
- [devpress/CSDN — 大模型行业全景 2025-2026 人才需求](https://devpress.csdn.net/aibjcy/69ff35c654b52172bc72be4f.html)
- [知乎 — 2026 大模型(LLM)面试题库](https://zhuanlan.zhihu.com/p/1981387722473116577)
- [知乎 — 主流大模型推理部署框架 (vLLM/TensorRT-LLM/SGLang)](https://zhuanlan.zhihu.com/p/1937266323156607848)
- [腾讯云 — 2026 大模型与多模态部署四大热门框架](https://cloud.tencent.com/developer/article/2649716)
- **2026-06-26 recalibration source anchors**
  - [vLLM official docs](https://docs.vllm.ai/)
  - [SGLang official docs](https://docs.sglang.ai/)
  - [NVIDIA TensorRT-LLM official docs](https://nvidia.github.io/TensorRT-LLM/)
  - [LangGraph official overview](https://docs.langchain.com/oss/python/langgraph/overview)
  - [RAGAS official docs](https://docs.ragas.io/en/stable/)
  - [European Commission — AI regulatory framework / AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
  - [GTAI — Artificial Intelligence in Germany](https://www.gtai.de/en/invest/industries/digital-economy/artificial-intelligence)
  - [Qwen3 official release blog](https://qwenlm.github.io/blog/qwen3/)
