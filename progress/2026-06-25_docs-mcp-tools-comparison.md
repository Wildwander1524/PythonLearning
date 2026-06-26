# 2026-06-25 — Docs/context MCP tools compared: Context7 vs Docfork vs Deepcon vs DeepWiki

**Topic:** The user asked how the **Context7** MCP (just adopted as the primary source for
library lessons — see `2026-06-25_context7-authority-eval.md`) compares to three similar tools:
**Docfork**, **Deepcon**, and **DeepWiki**. Goal: decide whether to switch/add any of them.

**Status:** ✅ Comparison done. Verdict: **keep Context7 as the library-lesson default; DeepWiki is
additive (different category) — install it for the later repo-reading phase.** DeepWiki installed
this session.

> Note on naming: "Deepcon" = **deepcon.ai** (a docs-search MCP). A *different* tool, **DeepContext**
> by Wildcard, does codebase semantic search — not what was meant, excluded.

---

## Two categories, not one

| | **Library-docs servers** | **Repo-understanding server** |
|---|---|---|
| Tools | Context7 · Docfork · Deepcon | **DeepWiki** |
| Indexes | Official docs sites of thousands of *published libraries* | *Any single GitHub repo's* source code |
| Answers | "Current API for `pandas.merge`?" | "How does *this codebase* implement X?" |

DeepWiki is **not** a Context7 competitor — it's complementary. Context7/Docfork/Deepcon = "how do I
use NumPy"; DeepWiki = "explain the architecture of the vLLM repo I'm reading."

---

## The three library-docs tools head-to-head

| Feature | **Context7** (Upstash) | **Docfork** | **Deepcon** |
|---|---|---|---|
| Coverage | ~50k+ libraries | 9,000+ | 10,000+ official docs |
| Retrieval | Indexed docs served on prompt | RAG: semantic + BM25 fused (RRF), AST-aware chunking | Semantic search + "Query Composer" extracts only relevant parts |
| Calls/query | ~2 | ~1 (claims ~500 ms p95) | — (claims ~1k tokens/response) |
| Stack scoping | No | **Yes — "Cabinets"** version-pin a team to a verified stack | Stack-aware |
| Cost | Free tier + paid | Open-source (MIT), free tier | Freemium ~$8–20/mo |
| Community | ~53,500 GitHub stars | ~463 stars | New (Show HN launch) |
| License | Source-available | **Open-source (MIT)** | Proprietary |

### ⚠️ Benchmark honesty
Headline numbers are **vendor self-reported**, not independent:
- Deepcon advertises "90% accuracy vs Context7's 65%" on 20 scenarios — *Deepcon testing Deepcon*.
- Docfork's "~500 ms p95" and "1 call vs Context7's 2" are self-reported.
- The trustworthy signal: **Context7 is the most adopted/battle-tested (~100× Docfork's community)**;
  the newer tools compete on token-efficiency and stack-scoping.

---

## Verdict for the PythonLearning workflow

- **Keep Context7 as the default for library lessons.** It already exposes the
  **Source-Reputation + Benchmark** metadata and **primary `numpy.org/doc` URLs** that powered the
  0%→100% authority jump. No alternative is documented to expose that provenance — which is the
  whole point of the `/teach` "cite high-trust sources" rule.
- **Docfork** — only useful for version-pinning a multi-lib stack (Cabinets); overkill for
  one-library-at-a-time lessons.
- **Deepcon** — optimizes token cost; irrelevant here (we *want* full doc context to cite).
- **DeepWiki** — the genuinely additive one. For the LLM/CV phases when reading real repos
  (vLLM, transformers), it does a job Context7 can't: explain a *specific codebase's* architecture.
  → **Installed this session** for that later stage.

---

## DeepWiki install (this session)
- Remote MCP server by **Cognition** (makers of Devin). Free for public GitHub repos; private repos
  need a Devin account + GitHub connection.
- Endpoints: `https://mcp.deepwiki.com/mcp` (streamable HTTP) and `https://mcp.deepwiki.com/sse`.
- Tools provided: `ask_question`, `read_wiki_contents`, `read_wiki_structure`.
- Installed via `claude mcp add` (remote URL — nothing downloaded to disk, so the D:\Code\MCP\
  install-path convention doesn't apply; this is a URL registration only).
- Coverage: 50,000+ top public repos pre-indexed (MCP spec, LangChain, etc.).

## DeepWiki verification (after session restart) — ✅ PASSED
Freshly-added MCP tools only surface after a Claude Code restart (server was Connected before
restart, but its tools weren't in the session's tool registry). After restart, real in-session
tool calls succeeded against `vllm-project/vllm`:
- `read_wiki_structure` → full 13-section tree with sub-pages (e.g. 3.3 Scheduler & Resource
  Allocation, 3.4 KV Cache Management & Prefix Caching, 8 Attention Backends → FlashAttention/MLA).
- `ask_question` ("how does the scheduler decide what to batch?") → code-grounded answer:
  `Scheduler.schedule()` uses a token budget (`max_num_batched_tokens`), prioritizes decode then
  chunked prefill; queries `KVCacheManager` (`get_computed_blocks`, `allocate_slots`, preemption).
  Notably corrected that **PagedAttention is the memory layout, not part of the batching decision**,
  and flagged `docs/design/paged_attention.md` as a historical doc no longer matching current code.
- Tool schemas: `read_wiki_structure(repoName)`, `ask_question(repoName, question)`,
  `read_wiki_contents(repoName)`. repoName is `owner/repo` (ask_question accepts up to 10 repos).
- Lesson learned: **a newly-added MCP server needs a session restart before its tools are callable.**

## Files
- This comparison: `progress/2026-06-25_docs-mcp-tools-comparison.md`
- Related authority eval: `progress/2026-06-25_context7-authority-eval.md`

## Sources
- Neuledge — Top 7 MCP Alternatives for Context7 (2026): https://neuledge.com/blog/2026-02-06/top-7-mcp-alternatives-for-context7-in-2026/
- ChatForest — Best Documentation MCP Servers 2026: https://chatforest.com/guides/best-documentation-mcp-servers/
- Docfork GitHub: https://github.com/docfork/docfork
- Deepcon: https://deepcon.ai/ · Show HN: https://news.ycombinator.com/item?id=45839378
- DeepWiki (Cognition): https://cognition.com/blog/deepwiki · MCP server: https://cognition.com/blog/deepwiki-mcp-server · GitHub: https://github.com/CognitionAI/deepwiki
