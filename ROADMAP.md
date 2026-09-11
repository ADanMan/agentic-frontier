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
- 2026-09-05 — deepseek-harness (211k★, 3rd reading): star growth decelerates while forks keep climbing steadily → *Proving it works*
- 2026-09-05 — ponytail (126k★, #2): daily stars keep falling but overall rank keeps climbing → *The churn watch*
- 2026-09-06 — sglang (35.5k★, +1,237/day, 8,563 forks): fork count is a more honest usage signal than stars → *Serving under real load*
- 2026-09-06 — ECC (250k★, #2): "security" across 4 different harnesses is a claim, not a verified boundary → *The authorization boundary*
- 2026-09-07 — ECC ranked #1 while trailing #2 on stars, growth, and "today" count → *The churn watch*
- 2026-09-07 — Motion-Omni: speech and co-speech motion still ship as two models with no shared context → *The churn watch*
- 2026-09-07 — diagram-design (32.6k★, #3): "no Mermaid slop" names auto-generated Mermaid as the new legacy default → *The churn watch*
- 2026-09-08 — hyperframes (46.4k★, #1): "Write HTML. Render video." trades pixels for markup, same bet as diagrams → *The churn watch*
- 2026-09-08 — markitdown (180.5k★, #2): the doc-to-text step sets the ceiling for every RAG chunk after it → *Retrieval as a first-class design*
- 2026-09-08 — context-mode (21k★, #3): claimed 98% tool-output reduction is a README number, not a benchmark → *Context economy*
- 2026-09-09 — i-have-adhd (31k★, #1, +819): a skill that forces the answer before the reasoning → *Context economy*
- 2026-09-09 — openai/skills (26.6k★, #3): Codex ships an official skills catalog, format now cross-harness → *The churn watch*
- 2026-09-09 — ECC (253k★, +1,315): forks (38k) are the more honest usage signal, stars aren't proof → *Proving it works*
- 2026-09-09 — On-Policy Self-Distillation critical review: dense IL signal + on-policy RL needs a second teacher model → *Where the training signal comes from*
- 2026-09-10 — superpowers (284k★, #3): "methodology that works" claimed with zero benchmark or case study attached → *Proving it works*
- 2026-09-10 — teamai-cli (Tencent, #2, +327): "AI native" names a state, not shared-CLI/memory/permissions mechanism → *The churn watch*
- 2026-09-10 — Recognition-Refusal Misalignment: models answer malformed questions — recognition fails, or routing to refusal does? → *Proving it works*
- 2026-09-10 — deepseek-harness (216.8k★): fork/star ratio flat at 11.8% for days despite rising stars, permission model still unclear → *The authorization boundary*
- 2026-09-11 — gods-eye-view (24.9k★, #2): "+916" window growth vs "1,762 stars today" on the same card, ~2x gap → *Proving it works*
- 2026-09-11 — OreoLook: three-layer cache filters expensive live-crawl+synthesis path on commodity CPU → *Serving under real load*
- 2026-09-11 — AutoResearch via world models: cheap simulated outcomes replace real experiments, accuracy on novel hypotheses unstated → *Where the training signal comes from*
- 2026-09-11 — HyQuant: same low bit-width is fine for MLP weights, large error inside attention, hence hybrid precision → *Serving under real load*
