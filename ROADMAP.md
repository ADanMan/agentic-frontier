# Roadmap

The backlog of guides and deep-dives across the **full** current AI stack, not just
agent frameworks. Each item becomes a file under `guides/` when written. Checked off
only when the guide actually exists.

## Protocols & standards

- [x] **MCP (Model Context Protocol)** — how agents discover and call external tools
- [ ] **Agent Skills** — progressive-disclosure capability packaging
- [ ] **Agent-to-agent (A2A)** communication patterns
- [ ] **Code execution with MCP** — calling MCPs as typed APIs instead of raw tool calls

## Agent frameworks & orchestration (current, 2025–2026)

- [ ] **Claude Agent SDK** — Anthropic-native production agents
- [ ] **LangGraph 1.0** — stateful multi-step workflows
- [ ] **CrewAI** — role-based multi-agent prototypes
- [ ] **LlamaIndex Workflows** — RAG-grounded agents
- [ ] **openworker** (andrewyng/openworker) — open-source AI coworker teardown
- [ ] **multica** (multica-ai/multica) — fan-out issues to 20+ coding agents
- [ ] **openclaw** — self-hosted personal assistant + gateway model

## RAG & retrieval

- [ ] **LlamaIndex** — data-centric agent development
- [ ] **Haystack** — production RAG orchestration
- [ ] **Vector DBs compared** — Milvus vs. Qdrant vs. Weaviate
- [ ] **Hybrid search** — vector + structured filtering
- [ ] **Knowledge graphs without a vector store** — deterministic AST/parse approaches

## Inference & serving

- [ ] **vLLM** — high-throughput serving, paged attention
- [ ] **Groq / Cerebras** — ultra-fast hosted inference (LPU / wafer-scale)
- [ ] **On-device inference** — X-bit quantization, edge/private LLMs
- [ ] **Serving on Apple Silicon** — tiny vLLM + small models

## Fine-tuning & adaptation

- [ ] **Unsloth** — up to 80% less VRAM
- [ ] **LlamaFactory** — unified fine-tuning across many models
- [ ] **LoRA / QLoRA** — when adaptation beats prompting

## Evals & observability

- [ ] **DeepEval** — unit-testing LLM apps
- [ ] **RAGAS** — retrieval quality metrics
- [ ] **Tracing & production monitoring** — what to log, what to alert on
- [ ] **Hallucination detection** — automated + human-in-the-loop

## Harness engineering (the durable knowledge)

- [ ] **Anatomy of an agent harness** — the control-plane loop
- [ ] **Tool design** — narrow, typed, validated, auditable contracts
- [ ] **Permissions & approval gates** — draft vs. commit for risky actions
- [ ] **Context engineering** — retrieval, memory, compaction, cache-aware ordering
- [ ] **Planning & goals** — planning mode, checkpoints, stopping conditions
- [ ] **Prompt caching & cost** — stable-prefix design, telemetry
- [ ] **Prompt-injection boundaries** — treating tool output as untrusted data

## Staying current (sources to mine)

- [ ] Follow trend digests (e.g. `duanyytop/agents-radar` open-source trend issues)
- [ ] Primary engineering blogs (Anthropic, OpenAI) + framework changelogs
- [ ] arXiv agent-engineering papers (memory, eval, workflows)

---

**Rule:** check items off only when the guide is written. Every guide links its sources.
