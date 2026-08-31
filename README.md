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

Short daily notes live in [`til/`](til/), one folder per day (`til/<date>/NN-slug/`).
One small, real thing learned per entry — no filler.

## How it runs (openly automated)

This repo is fed by an **openly automated daily routine** — I'll say that plainly
rather than pretend each post is hand-typed at dawn. A scheduled cloud agent runs
every morning, reads a fresh digest of **real current** sources (`scripts/digest.py`),
and writes across three streams, each grounded in and citing today's real sources:

- **`posts/<date>/NN-slug/`** — full **bilingual (RU + EN)** explainers of the day's
  most notable items, illustrated with the source's own image (else a generated diagram);
- **`til/<date>/NN-slug/`** — short "today I learned" notes on smaller items;
- **`guides/<date>/NN-slug/`** — deeper plain-language explainers of one concept.

Several folders per stream per day. The content is real and grounded in today's sources;
the automation is the point, not a disguise.

**Where the digest comes from.** The routine's cloud sandbox blocks outbound traffic to
almost everything (arXiv, vendor blogs, Hacker News). What it *can* reach is
`raw.githubusercontent.com`, so `feeds.txt` leads with community RSS **mirrors** hosted
there — HF trending papers (with abstracts), GitHub trending/ranking repos, HF blog —
that are rebuilt daily. `digest.py` fetches those in-sandbox; the arXiv API and vendor
feeds below them enrich the digest only when the script runs on an open network. No
GitHub Action and no API key are involved — the routine is fully self-contained.

Evergreen deep-dives stay at the top level of [`guides/`](guides/) (e.g.
[MCP explained](guides/mcp-explained.md)); the dated daily explainers land in
`guides/<date>/` alongside them.

### Run the digest yourself

The digest fetcher is the only moving part you'd run by hand; it needs no API key:

```bash
python3 scripts/digest.py   # fetch today's digest (arXiv + feeds.txt + trending repos)
```

## License

[MIT](LICENSE) — take anything useful.
