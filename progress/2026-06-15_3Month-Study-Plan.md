# 3-Month AI Career Study Plan & Progress Record

- **Owner:** Career-changer (science/engineering background, 9 yrs since graduation, strong engineering thinking, no prior programming work experience)
- **Target role:** Industrial large-model (大模型) fine-tuning + Agent development
- **Geography:** Phase 1 — China first-tier cities (Beijing / Shanghai / Guangzhou / Shenzhen); Phase 2 (long-term) — Germany, related field
- **Plan window:** 2026-06-16 → 2026-09-12 (13 weeks; Week 1 starts Monday 2026-06-16)
- **Cadence:** 6 days/week (Mon–Sat), Sunday off. **7 h theory + 3 h homework = 10 h/day**
- **Created:** 2026-06-15  | **Last updated:** 2026-06-15  | **Status:** 🟢 Active — Week 0 (pre-start)

> This file is BOTH the study plan AND the live progress record. As you complete exercises,
> send them to me and I update the tracking table + completion log below. See **§7 Default
> Requirements** for the standing rules (completion updates + weekly frontier refresh).

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
| **3. Inference acceleration — vLLM / TensorRT-LLM** | ✅ **Yes — mainstream / near-required** | Explicitly listed among core skills for 2026 LLM-application roles ("production deployment incl. vLLM/TensorRT-LLM acceleration + vector-DB integration"). PagedAttention/vLLM and TensorRT-LLM are the default production-serving stack. | **Highest priority.** Core of the frontier slot from Week 9; introduced conceptually earlier. |
| **1. Edge-side multimodal deployment — MobileCLIP / TinyGPT-V** | 🟡 **Niche / bonus (growing)** | Not a universal requirement for mainstream 大模型应用 roles. Strong differentiator at terminal/IoT/automotive-cockpit teams (小米, 荣耀, vivo, OPPO, 地平线). Strategically aligned with your *industrial/edge* focus. | **Secondary, but strategically core for YOU** given industrial/edge target. Hands-on in Weeks 9–13. |
| **2. Video understanding — Video-LLaMA / TimeSformer** | 🟡 **Emerging / sector-specific** | Multimodal is increasingly mainstream; video-specific still emerging vs. image+text. Valued in short-video/content (字节, 快手), security/surveillance, autonomous driving. | **Tertiary / elective.** Conceptual coverage + one mini-project; deepen only if targeting content/AV sectors. |

**Net takeaway:** Make **vLLM/TensorRT-LLM inference deployment** a non-negotiable skill. Treat
**edge multimodal** as your *differentiator* (fits industrial/Germany direction). Treat **video
understanding** as an *elective* you can showcase with one project.

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
| **S1 — Core Theory A** | 2 h | Primary subject of the day |
| **S2 — Core Theory B** | 2 h | Primary subject continued / second subject |
| **S3 — Math** | 1 h | The week's math topic (focused) |
| **S4 — Frontier / Current Directions** | 2 h | Rotating cutting-edge content (the "2-hour daily slot"). **Friday S4 = Weekly AI Industry Digest** |
| **Homework** | 3 h | Daily coding/practice assignment (listed per day) |

**Totals:** Theory = S1+S2+S3+S4 = 7 h · Homework = 3 h · **= 10 h/day**.
Suggested clock: 08:30–10:30 (S1) · 10:45–12:45 (S2) · 14:00–15:00 (S3) · 15:15–17:15 (S4) ·
19:00–22:00 (Homework). Adjust to your chronotype; keep the block sizes.

### Frontier Track (the rotating S4 "most current directions" slot)
- **Phase 1 — Orientation & Tooling (W1–4):** Build conceptual literacy + working environment.
  Skim landmark material on the 3 directions; set up Python/conda, Git, CUDA-ready PyTorch,
  Docker; learn to read the AI news landscape. *No heavy coding yet — you're building the runway.*
- **Phase 2 — Applied Foundations (W5–8):** As ML/DL knowledge lands, do guided hands-on — run a
  CLIP/MobileCLIP demo, dissect attention behind Video-LLaMA/TimeSformer, benchmark a small model's
  inference latency/throughput.
- **Phase 3 — Specialization (W9–13):** Deploy an edge multimodal model; build a small
  video-understanding pipeline; serve an LLM with **vLLM** then accelerate with **TensorRT-LLM**;
  fold all three into the capstone.
- **Every Friday:** S4 = **Weekly AI Industry Digest** — I refresh this with the week's real
  developments and re-tune the upcoming week's frontier content (see §7).

---

## §3 — 13-Week Macro Plan

| Month | Week | Dates (Mon–Sat) | Core curriculum | Math | Frontier phase |
|-------|------|-----------------|-----------------|------|----------------|
| **1** | 1 | 06-16 → 06-21 | Python OOP deep-dive | Linear Algebra I | P1 Orientation |
| | 2 | 06-23 → 06-28 | NumPy | Linear Algebra II + Calculus I | P1 |
| | 3 | 06-30 → 07-05 | Pandas | Calculus II + Probability I | P1 |
| | 4 | 07-07 → 07-12 | MATLAB + C++ basics I | Discrete Math I | P1 |
| **2** | 5 | 07-14 → 07-19 | C++ basics II (OOP, STL) | Probability II | P2 Applied |
| | 6 | 07-21 → 07-26 | Machine Learning I (supervised) | Linear Algebra III (SVD/PCA, matrix calc) | P2 |
| | 7 | 07-28 → 08-02 | Machine Learning II (trees, ensembles, SVM, clustering, eval) | Optimization / Calculus III | P2 |
| | 8 | 08-04 → 08-09 | Deep Learning I (MLP, backprop, PyTorch) | Discrete Math II + Number Theory | P2 |
| **3** | 9 | 08-11 → 08-16 | Deep Learning II (CNN, RNN, regularization, training) | Applied stats review | P3 Specialization |
| | 10 | 08-18 → 08-23 | Deep Learning III → Transformers + NLP I | Math consolidation | P3 |
| | 11 | 08-25 → 08-30 | NLP II (pretrained models, fine-tuning, PEFT/LoRA) + LLM basics | — | P3 |
| | 12 | 09-01 → 09-06 | Agent development (LangChain/LlamaIndex, tools, planning) + RAG I | — | P3 |
| | 13 | 09-08 → 09-12 | RAG II (advanced retrieval, eval) + **Capstone** | — | P3 (integrate all) |

> **Detail policy:** Month 1 (Weeks 1–4) is written out block-by-block below. Months 2–3 are written
> at day-objective + session-topic + homework granularity and will be expanded to full block detail
> as we reach each week (and refreshed by the weekly frontier update). This is intentional: later
> weeks depend on your actual pace, and the frontier slot changes with live AI news.

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

### Week 4 (07-07 → 07-12) — MATLAB + C++ basics I + Discrete Math I
**Weekly goal:** MATLAB for numerical/matrix work + plotting; first C++ (compile, types, control flow,
functions, pointers intro); discrete-math foundations (logic, sets, proof).

| Day | Objective | S1 (2h) | S2 (2h) | S3 Math (1h) | S4 Frontier (2h) | Homework (3h) |
|-----|-----------|---------|---------|--------------|------------------|----------------|
| **D1 Mon** | MATLAB basics | Environment, variables, matrices, `:` operator | Element-wise vs matrix ops, indexing | Propositional logic, truth tables | Compare MATLAB vs NumPy for matrix work (notes) | MATLAB: implement matrix ops + solve a linear system |
| **D2 Tue** | MATLAB scripts & plots | Scripts, functions, control flow | 2D/3D plotting, `plot/surf`, subplots | Predicate logic, quantifiers | Read: GPU vs CPU for AI compute (concept) | MATLAB: plot functions + a small simulation |
| **D3 Wed** | C++ entry | Compile/build, `main`, types, I/O (`cin/cout`) | Control flow, loops, functions, scope | Sets, operations, Venn, cardinality | Toolchain: install g++/CMake; "hello world" | C++: temperature converter + FizzBuzz + factorial |
| **D4 Thu** | C++ functions & memory | Functions, pass-by-value/reference, overloading | Pointers & references intro; stack vs heap | Proof techniques: direct, contradiction, induction | Read: why C++ matters for inference engines | C++: array stats (min/max/mean) using functions |
| **D5 Fri** | C++ arrays & strings | Arrays, `std::vector` intro, `std::string` | Structs, basic file I/O | Relations, functions (math), mappings | **Weekly AI Digest #4** + Month-1 retro | C++: word-count program reading from file |
| **D6 Sat** | Month-1 capstone | Review all of Month 1 | Capstone build | Discrete-I recap + induction proofs | Plan Month 2; env check for ML | **Month-1 capstone:** data pipeline — Python(OOP)→NumPy→Pandas analysis, reproduced in MATLAB for one matrix step; README + push |

---

## §5 — MONTHS 2–3 (Weeks 5–13): day-level plan

> Block-by-block detail for each week will be expanded when we reach it. Each day still = the §2
> template (S1/S2/S3 core + S4 frontier 2h + 3h homework).

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

### Week-level status
| Week | Theme | Status | Notes |
|------|-------|--------|-------|
| 1 | Python OOP + LA I | ☐ | starts 06-16 |
| 2 | NumPy + LA II/Calc I | ☐ | |
| 3 | Pandas + Calc II/Prob I | ☐ | |
| 4 | MATLAB + C++ I + Discrete I | ☐ | |
| 5 | C++ II + Prob II | ☐ | |
| 6 | ML I + LA III | ☐ | |
| 7 | ML II + Opt/Calc III | ☐ | |
| 8 | DL I + Discrete II + Num. Theory | ☐ | |
| 9 | DL II + vLLM serving | ☐ | |
| 10 | Transformers + NLP I + TensorRT-LLM | ☐ | |
| 11 | NLP II + PEFT/LoRA + edge multimodal | ☐ | |
| 12 | Agent + RAG I + video understanding | ☐ | |
| 13 | RAG II + Capstone | ☐ | |

### Completion log (newest first)
*(Each time you send completed exercises, I append a dated entry here: what you did, what was
correct, what to fix, and any pace adjustment.)*
- **2026-06-15** — Plan created and saved as progress record. Pre-start (Week 0). Next: begin Week 1 D1 on Mon 06-16.

---

## §7 — Default Requirements (standing rules for this record)

These are now the permanent operating rules for this study plan. They apply every session:

1. **Completion-driven updates.** Whenever you send me completed exercises/homework, I:
   - review them (correctness, style, what to improve),
   - tick the relevant cells in §6 (☐→🔄→✅) and add a dated **Completion log** entry,
   - adjust upcoming pace/difficulty if you're ahead or behind,
   - commit & push the updated record so you can track it on GitHub.

2. **Weekly frontier refresh (the "2-hour daily slot").** Each week I retrieve the latest AI-industry
   developments and **re-tune the S4 frontier content** for the coming week — keeping it pointed at
   the *currently* most relevant directions, with standing emphasis on:
   - **vLLM / TensorRT-LLM inference acceleration** (mainstream — top priority),
   - **edge-side multimodal deployment** (your industrial/Germany differentiator),
   - **video understanding** (elective showcase),
   - plus any newly-hot direction the week's news surfaces.
   The refresh lands as the **Friday "Weekly AI Industry Digest #N"** entry and updates the next
   week's S4 cells.
   - ⚠️ *Automation note:* I don't run autonomously between turns, so the weekly refresh happens when
     you check in (ideally each Friday/weekend). If you want it to fire on a fixed schedule without
     you prompting, say the word and I'll set up a scheduled routine (`/schedule`) to generate the
     digest automatically.

3. **Record discipline.** This file stays the single source of truth for the plan + progress. I keep
   §3–§5 aligned with reality as your pace shifts, and I never silently drop a subject — deferrals are
   marked ⏭️ with a reason.

4. **Honesty about pace.** 10 h/day × 6 days is intense. If reality diverges, I'll propose a realistic
   re-plan (e.g., stretch to 16 weeks) rather than pretend the original fits.

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
