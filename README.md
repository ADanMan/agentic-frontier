# Agentic Frontier

> A learning-in-public log tracking **current** AI engineering — the models, tools,
> protocols, and harnesses that actually shipped in 2025–2026, not last year's hype.

I'm a Senior AI Engineer working on agentic infrastructure and AI governance. This
repo is where I take notes, write guides, and keep my own map of the fast-moving
AI stack up to date. Everything here is written to be useful to someone else picking
up the same tools.

## Why this exists

The AI space moves faster than any single blog post can keep up with. Frameworks
that were the default six months ago are already legacy. This repo is my attempt to
stay current *by writing things down* — the classic "learning in public" loop:

1. Read / try a new tool, model, or protocol.
2. Write a short note (`til/`) or a full guide (`guides/`) explaining it plainly.
3. Revisit and correct earlier notes as things change.

If a guide here is wrong or out of date, open an issue — that's the whole point.

## Scope

This isn't only agent frameworks. It tracks the full current stack:

- **Agents & orchestration** — Claude Agent SDK, LangGraph, CrewAI, multica, openworker
- **Protocols** — MCP, Agent Skills, agent-to-agent
- **RAG & retrieval** — LlamaIndex, Haystack, RAGAS, vector DBs (Milvus / Qdrant / Weaviate)
- **Inference & serving** — vLLM, Groq, Cerebras, on-device quantization
- **Fine-tuning** — Unsloth, LlamaFactory
- **Evals & observability** — DeepEval, RAGAS, tracing
- **Harness engineering** — the durable patterns behind all of it

See [ROADMAP.md](ROADMAP.md) for the full backlog.

## Guides

In-depth, plain-language explanations of current tech.

| Guide | Topic | Status |
|-------|-------|--------|
| [MCP explained](guides/mcp-explained.md) | Model Context Protocol — the USB-C of agent tools | ✅ |
| _Agent harness anatomy_ | The control-plane loop around a model | 🔜 |
| _vLLM in practice_ | High-throughput LLM serving | 🔜 |
| _RAG eval with RAGAS_ | Measuring retrieval quality | 🔜 |
| _Unsloth fine-tuning_ | Low-VRAM domain adaptation | 🔜 |

## TIL (Today I Learned)

Short daily notes live in [`til/`](til/). One small, real thing learned per entry.
New entries are scaffolded with `scripts/new_til.py` and then written by hand — no
filler.

## The daily routine

The honest way to keep a green contribution graph is to *actually do a little every
day and commit it*. This repo ships a tiny helper for exactly that:

```bash
python scripts/new_til.py "what I looked at today"
# → creates til/2026/YYYY-MM-DD.md from a template
# → open it, write 3–5 real sentences about what you learned
git add til/ && git commit -m "til: <topic>"
```

No bots, no empty commits — each square is backed by a real note you can stand behind.

## License

[MIT](LICENSE) — take anything useful.
