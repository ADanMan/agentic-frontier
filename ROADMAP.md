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
- 2026-09-22 — Measuring the Checker: mutation analysis scores GPU-kernel checkers, not just the code → *Proving it works*
- 2026-09-22 — Srijika: restyles glyph outlines on shaping-complete templates, skips full from-scratch font generation → *The churn watch*
- 2026-09-22 — OpenStock (18k★, #3, +385): README opens on a Solana token address, before the project name → *Proving it works*
- 2026-09-22 — Skill Synthesis paper: fuller excerpt reveals 2nd limitation, document-derived skills "may lac[k]..." → *Where the training signal comes from*
- 2026-09-22 — Open ASR Leaderboard adds its first Global South language, symptom of benchmark coverage gap → *Proving it works*
- 2026-09-22 — Mutation testing explainer: a checker with 40% mutation score passes broken code as often as correct → *Proving it works*
- 2026-09-23 — anthropics/financial-services (#1, 36.5k★, +216): real MCP read access to FactSet/Moody's, but the output gate is a disclaimer, not code → *The authorization boundary*
- 2026-09-23 — deepseek-harness (232.8k★, +1,024): "developer preview... breaking changes" openly stated next to quarter-million stars → *The churn watch*
- 2026-09-23 — agent-substrate (3.1k★, #2, +164): "30x+ oversubscription" via suspend/resume, no benchmark methodology shown → *Serving under real load*
- 2026-09-23 — Univer (15.7k★, #3, +406): "isolated draft collaboration" + verification is a technical gate, not just a disclaimer → *The authorization boundary*
- 2026-09-23 — SkillSpec paper: mirror question to prior skill-synthesis papers — not where a skill comes from, but is it correct → *Proving it works*
- 2026-09-24 — google/ax (#2, +284): window-diff vs "stars today" mismatch, 3rd confirmed instance of this pattern → *Proving it works*
- 2026-09-24 — claude-code-templates (#3, 31.5k★): configures permissions/hooks AND monitors execution, both sides of one boundary → *The authorization boundary*
- 2026-09-24 — Schrödinger's Code Repository paper: SWE-bench repos overlap pretraining data, correct patch could be memorized not solved → *Proving it works*
- 2026-09-25 — hindsight (27.8k★, #2): +77 window vs 1,668 claimed stars today, 4th mismatch instance → *Proving it works*
- 2026-09-25 — LatentPort paper: hands a 4B model's live state to a 9B sibling, skips context reread → *Context economy*
- 2026-09-25 — ai-engineering-from-scratch (56.6k★, #1): +103 window vs 347 claimed stars today, 5th mismatch instance → *Proving it works*
- 2026-09-26 — paperclip (84.9k★, #1): +270 window vs 2,109 claimed stars today, 6th mismatch instance → *Proving it works*
- 2026-09-26 — claude-plugins-official (36.9k★, #2): "managed" curated directory, card doesn't say review vs. link-list → *The authorization boundary*
- 2026-09-26 — hello-agents (80.8k★, RAG #10): general agent-building textbook filed under a narrower "RAG" category → *The churn watch*
- 2026-09-26 — RewardVerse paper: rubric of explicit criteria proposed to replace one unstable scalar reward for video RL → *Where the training signal comes from*
- 2026-09-26 — crawl4ai (84.2k★, RAG new entry #9): "clean, LLM-ready Markdown" from any site, open-core + paid cloud → *Retrieval as a first-class design*
- 2026-09-26 — Spatial-Interactor paper: spatial reasoning reframed as tracking local state transitions from object motion, not static scenes → *The churn watch*
- 2026-09-26 — AgentKernel paper: names 4 concrete trust-boundary crossings (untrusted content, mixing, memory persistence, tool calls) → *Untrusted tool output*
