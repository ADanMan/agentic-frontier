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

- 2026-09-11 — OreoLook: three-layer cache filters expensive live-crawl+synthesis path on commodity CPU → *Serving under real load*
- 2026-09-11 — AutoResearch via world models: cheap simulated outcomes replace real experiments, accuracy on novel hypotheses unstated → *Where the training signal comes from*
- 2026-09-11 — HyQuant: same low bit-width is fine for MLP weights, large error inside attention, hence hybrid precision → *Serving under real load*
- 2026-09-12 — Prompt-Engineering-Guide (78.2k★, #9→#10) swaps ranks same day/category with an agent-tutorial repo → *The churn watch*
- 2026-09-12 — hello-agents (78.4k★, #10→#9): near-tied stars with its rival, but +1,146 forks → *Proving it works*
- 2026-09-13 — system_prompts_leaks (65.5k★, #3): extraction across 4 vendors proves prompts are text, not an enforced boundary → *Untrusted tool output*
- 2026-09-13 — DeskcommCRM (1.9k★, #2): AI agent wired into live WhatsApp sends, "MCP-ready" says nothing about propose-vs-send → *The authorization boundary*
- 2026-09-14 — colibri (30.3k★, #1, pure C): MoE experts stream from disk since only 1-2 of N are active per token → *Serving under real load*
- 2026-09-15 — open-code-review (25.5k★, #2): "battle-tested at Alibaba's scale" ships with no benchmark → *Proving it works*
- 2026-09-15 — YuE2 (8.3k★, #3): "frontier" tagline bundles 3 claims, zero samples given → *The churn watch*
- 2026-09-15 — PLC-DPO: posterior label correction targets DPO's assumption that preferences are reliable → *Where the training signal comes from*
- 2026-09-15 — TempCloze: video-LLM benchmark isolates language shortcuts from real temporal reasoning → *Proving it works*
- 2026-09-16 — Sparse decision trees via transformer VAE: discrete tree search reframed as continuous latent optimization → *Proving it works*
- 2026-09-16 — Thai OCR-Zero: synthetic labels train the base, unlabeled real pages close the domain gap → *Where the training signal comes from*
- 2026-09-16 — Fixed-voice Thai TTS from synthetic speech: compact single-voice model trades flexibility for cheap inference → *Serving under real load*
- 2026-09-17 — graphify (118.2k★, +1,313): "no vector store" — AST-parsed graph edges vs embedding similarity, different retrieval units → *Retrieval as a first-class design*
- 2026-09-17 — security-audit-skill (7.3k★, #2): +310 window gain vs "927 stars today" on the same card, same gods-eye-view pattern → *Proving it works*
- 2026-09-17 — Grouped Value Attention: title implies keys reconstructed on demand, only values stay cached, past GQA's grouping → *Serving under real load*
- 2026-09-17 — Long-horizon memorization: stretches the forgetting check from 1 update to N, tests if CL mechanisms compose → *Where the training signal comes from*
- 2026-09-18 — "The Last AI Built by Humans": RSI defined as persistent changes that also improve the improvement process itself → *Where the training signal comes from*
- 2026-09-18 — "Never Giving Up" RL paper: RL fine-tuning measurably improves easy problems far more than hard ones → *Proving it works*
- 2026-09-18 — agent-skills (addyosmani, 95.8k★): +65 window gain vs "680 stars today" on the same card, ~10x gap, third time this pattern appears → *Proving it works*
- 2026-09-18 — open-code-review (34.7k★, #1, up from 25.5k on 09-15): "deterministic pipelines + LLM Agent" — unclear if rules gate the agent's comments or both publish directly → *The authorization boundary*
- 2026-09-19 — claude-code (146.4k★, #2, +94): steady daily gain, not a spike, but README doesn't detail the propose-vs-commit boundary → *The authorization boundary*
- 2026-09-19 — lobehub (82.6k★, NEW ENTRY #9): "Chief Agent Operator" tagline maps to 4 real subsystems, zero benchmark for the orchestration claim itself → *Proving it works*
- 2026-09-19 — SpectralShift: reparameterizes trained weights to extend Gated DeltaNet's context instead of continued pretraining → *Serving under real load*
- 2026-09-19 — RelateAnything: relation prediction is the last vision task still trained on a fixed taxonomy, unlike detection/segmentation → *The churn watch*
- 2026-09-20 — trycua/cua (24.6k★, #2, +295): Driver names "explicit action boundaries" for OS-level control, no benchmark on how tight → *The authorization boundary*
- 2026-09-21 — ECC (264k★, #1, +353): skills load on demand, instincts+summary persist, raw transcript doesn't → *Context economy*
- 2026-09-21 — Grounded Skill Synthesis paper: proposes learning skills from code, not just traces; abstract excerpt cuts off before naming 2nd limitation → *Where the training signal comes from*
- 2026-09-21 — agent-native (5.4k★, #2): one Action definition shares validation+permissions across UI/agent/HTTP/MCP/A2A/CLI → *The authorization boundary*
- 2026-09-21 — cc-switch (NEW ENTRY #10, 134k★): meta-manager for 9 competing coding-CLI config formats → *The churn watch*
