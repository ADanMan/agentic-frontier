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

## How it runs (openly automated)

This repo is fed by an **openly automated daily routine** — I'll say that plainly
rather than pretend each post is hand-typed at dawn. A scheduled cloud agent runs
every morning, picks a roadmap topic that hasn't been covered yet, writes one
explainer in the plain-language, slightly-ironic voice you can see in the guides,
saves it under `posts/`, and commits it. The content is real and on-topic; the
automation is the point, not a disguise.

### Prefer to run it yourself?

Everything the routine does can also be run by hand — plus there's an optional
GitHub Action ([daily.yml](.github/workflows/daily.yml)) and local scripts:

```bash
python3 scripts/generate.py          # one post via the Anthropic API (needs ANTHROPIC_API_KEY)
python3 scripts/new_til.py "topic"   # scaffold a dated note in til/
python3 scripts/digest.py            # draft a digest from arXiv + trending repos
```

## License

[MIT](LICENSE) — take anything useful.
