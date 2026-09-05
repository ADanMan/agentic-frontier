# Roadmap — search vectors, not a shopping list

A list of tools rots in months (whatever was the default six months ago is already
legacy). So this file isn't a checklist of technologies — it's a set of durable
**search vectors**: lenses to point at whatever the daily digest drags in.

When a new paper or repo shows up, don't ask "is it on the list?" — ask **which vector
it belongs to**. That's how you stay current without chasing names. The concrete names
live at the bottom, dated, under *Recent signals* — the vectors above them stay put.

Think of it the way the *humanizer* skill names writing tells (inflated symbolism, rule
of three, negative parallelisms…): stable, named patterns — not a catalogue of instances.

## Search vectors

Each vector = a name, the question it asks, and what to look for.

- **Context economy** — *What does the system choose to put in the model's window, and
  what does it throw away?* Look for: retrieval triggers, compaction, memory scoping,
  cache-aware ordering.
- **The authorization boundary** — *Where does "the model proposed X" turn into "X
  actually happened"?* Look for: tool schemas, permission gates, draft-vs-commit,
  sandboxing.
- **Where the training signal comes from** — *What actually teaches the model, and does
  that source scale?* Look for: self-play / synthetic environments, distillation, data
  attribution, reward design.
- **Retrieval as a first-class design** — *What is the unit of retrieval, and why that
  unit?* Look for: chunking, hybrid search, graph-vs-vector, freshness.
- **Serving under real load** — *What breaks when N users hit it at once?* Look for:
  batching, paged attention, quantization, latency-vs-throughput tradeoffs.
- **Adapting a model cheaply** — *When is changing weights worth it over changing the
  prompt?* Look for: LoRA / QLoRA, low-VRAM finetuning, and when NOT to finetune.
- **Proving it works** — *How do you know it's good, not just vibes?* Look for: eval
  harnesses, hallucination detection, offline-vs-online, regression.
- **Untrusted tool output** — *Where could injected text hijack the agent?* Look for:
  prompt-injection boundaries, provenance, least privilege.
- **The churn watch** — *What was the default six months ago that's now legacy, and why
  did it lose?* Look for: framework migrations, deprecations, "we replaced X with Y".

## How this file stays fresh

The daily routine maps each digest item to the vector it touches and appends a dated
one-liner under *Recent signals*. The vectors don't move; the evidence under them
accumulates. Concrete tool names belong there — dated — never in the vectors themselves.

## Recent signals

*(auto-appended by the daily routine; newest at the bottom, trimmed to the latest ~30)*

- 2026-09-01 — OpenAI cuts Cursor's model contract after its SpaceX acquisition → *The churn watch*
- 2026-09-01 — deepseek-harness (205k★): "Everything is a Plugin" core/extension split → *The authorization boundary*
- 2026-09-01 — Tencent Hy4 Preview: 770B total/49B active MoE, 2.5x Hy3's size → *Serving under real load*
- 2026-09-01 — PULSAR: vision-first late-interaction RAG skips OCR for pitch decks → *Retrieval as a first-class design*
- 2026-09-01 — minimind (472★/day): readable 64M-param LLM pretrain pipeline, 2h on one GPU → *Where the training signal comes from*
- 2026-09-01 — pgbot (840★): schema/stats-aware Postgres layer for agents, not just text-to-SQL → *The authorization boundary*
- 2026-09-01 — OCaml maintainer: a bare bug rumor is now enough for LLMs to find an exploit → *Untrusted tool output*
- 2026-09-01 — Survey of Optimizers: coordinates→matrices, fixed horizon→policies, rule→state → *Where the training signal comes from*
- 2026-09-01 — Logos harness: capabilities formally carry a tracked inverse (undo) → *The authorization boundary*
- 2026-09-02 — ponytail (119k★): agent prompt trained to prefer writing no code at all → *Context economy*
- 2026-09-02 — openclaude (31k★, #1 trending): "runs anywhere, uses anything" harness pitch → *The churn watch*
- 2026-09-02 — HF "State of Open Models" Summer 2026: "open" splits into weights/data/code/license axes → *The churn watch*
- 2026-09-02 — academic-research-skills (45k★): 5-step research→write→review→revise→finalize skill → *Proving it works*
- 2026-09-02 — Quivr (new #10, Chatbot): "opiniated RAG", any LLM/any vectorstore, defaults vs. flexibility → *Retrieval as a first-class design*
- 2026-09-02 — Sentence Transformers adds late-interaction multi-vector embeddings (ColBERT-style) → *Retrieval as a first-class design*
- 2026-09-02 — Dharma-AI: +33 points GPU cluster utilization from job scheduling order alone → *Serving under real load*
- 2026-09-02 — SHAPE: decomposes math-reasoning accuracy into separate measurable skills → *Proving it works*
- 2026-09-02 — InternReviewer/InternAdvocate: objective reward for subjective peer-review/rebuttal RL → *Where the training signal comes from*
- 2026-09-03 — TimesFM (30k★, #2): one pretrained model replaces per-series ARIMA/Prophet, zero-shot → *The churn watch*
- 2026-09-03 — RECAP-Forcing: long video memory organized by content appearance, not just recency → *Context economy*
- 2026-09-03 — ponytail (122k★, #3 overall, day 2): a second consecutive trending day beats one, still isn't adoption proof → *Proving it works*
- 2026-09-03 — deepseek-harness (209k★, day 3): "everything is a plugin" needs a permission model, not just extensibility → *Untrusted tool output*
- 2026-09-03 — Quivr "NEW ENTRY #10" two days running: trending snapshots are noisy, not stable rankings → *The churn watch*
- 2026-09-03 — fmtlib/fmt #1 in "AI trends": a plain C++ lib, feed labels aren't content filters → *The churn watch*
- 2026-09-03 — Institutional Newspapers Pipeline: billions of tokens need layout parsing before OCR reading order → *Where the training signal comes from*
- 2026-09-03 — IBM Research "How Much Memory Does Your Agent Actually Need": working/episodic/long-term have separate costs → *Context economy*
- 2026-09-04 — mattpocock/skills (248k★, #2): one dev's .agents folder, stars track fame not proven quality → *Context economy*
- 2026-09-04 — hermes-agent (241k★, #3, Nous Research): "grows with you" names no mechanism at all → *The churn watch*
- 2026-09-04 — Entity-Aligned Retrieval for KB-VQA: CLIP similarity finds "looks like", not "is the same entity" → *Retrieval as a first-class design*
- 2026-09-05 — Conditional Experience Transfer: autonomous post-training learns when NOT to reuse past runs → *Where the training signal comes from*
