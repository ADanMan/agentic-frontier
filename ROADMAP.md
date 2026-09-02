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

- 2026-08-22 — genoffice (3.5k★): open-source office suite, agents write .docx/.xlsx/.pptx → *The authorization boundary*
- 2026-08-22 — phone-harness (2k★): agent taps/swipes your phone, no built-in action gate → *The authorization boundary*
- 2026-08-22 — Vercel Labs Foreman: eve Software Factory template, full dev pipeline agent → *The churn watch*
- 2026-08-22 — Lilian Weng, "Harness Engineering for Self-Improvement": scaffolding as the improvement lever → *Where the training signal comes from*
- 2026-08-22 — Liquid AI LFM2.5-DSpark: up to 3.2x faster inference, edge-focused → *Serving under real load*
- 2026-08-22 — IBM Research: how much memory does an agent actually need? → *Context economy*
- 2026-08-23 — Stampli/OpenAI: ChatGPT Work claims 68% faster customer launch → *Proving it works*
- 2026-08-23 — DeepMind retrospective: Atari to EVE Online, environments getting more open → *The churn watch*
- 2026-08-23 — Raschka on Claude watermarking: statistical token bias as provenance signal → *Untrusted tool output*
- 2026-08-23 — Raschka on reasoning effort: a per-step dial, not a global switch → *Serving under real load*
- 2026-08-23 — Fuxi (1.7k★): terminal coding agent, cost-aware multi-provider routing → *Serving under real load*
- 2026-08-23 — DeepMind sign language AI: lab prototype to daily-use product for real users → *Proving it works*
- 2026-08-24 — Anthropic's top model losing users to cheaper tools: benchmarks ≠ adoption → *Proving it works*
- 2026-08-24 — Anthropic "Building Effective Agents": workflows fix control flow, agents let the model own it → *The authorization boundary*
- 2026-08-24 — Anthropic Contextual Retrieval: LLM-annotate chunks before indexing to fix lost context → *Retrieval as a first-class design*
- 2026-08-24 — SWE-bench Verified + Sonnet: the score is model + harness, not model alone → *Proving it works*
- 2026-08-24 — Raschka's AI text detector from scratch: provenance is a heuristic score, not fact → *Untrusted tool output*
- 2026-08-24 — HF on ASR benchmark optimization: low WER on LibriSpeech ≠ real-world quality → *Proving it works*
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
