#!/usr/bin/env python3
"""Generate one AI explainer post in a lively Russian tech-blog voice.

Runs unattended (from a GitHub Action) or by hand:

    ANTHROPIC_API_KEY=sk-... python3 scripts/generate.py

It picks a topic from ROADMAP.md (rotating by day so it doesn't repeat), asks the
Anthropic Messages API to write a post in the voice described below, and writes it
to posts/<year>/<YYYY-MM-DD>.md. It does NOT commit — the workflow does that.

This is an openly automated content pipeline. The repo README says so plainly; the
value is real explainers on current topics, not empty commits.

Only network call is to the Anthropic API. No user data is sent anywhere else.
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "posts"
ROADMAP = REPO_ROOT / "ROADMAP.md"

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"
MODEL = os.environ.get("GEN_MODEL", "claude-sonnet-5")
MAX_TOKENS = int(os.environ.get("GEN_MAX_TOKENS", "1600"))
HTTP_TIMEOUT = 90

# The voice. Lively Russian tech-blog register: witty, plain-language, skeptical of
# hype, addresses the reader directly, short paragraphs, no corporate/academic dryness,
# no profanity (public technical repo). Ends with a practical "why it matters".
SYSTEM_PROMPT = (
    "Ты — автор популярного русскоязычного техно-блога про ИИ. Пишешь живо, с иронией "
    "и здоровым скепсисом к хайпу, объясняешь сложное на пальцах, обращаешься к читателю "
    "на «вы». Короткие абзацы, уместные ремарки в скобках, ноль канцелярита и "
    "академической сухости. Без мата и пошлости — это публичный технический блог. "
    "Структура: цепляющий заголовок H1, затем объяснение по существу, в конце — раздел "
    "«Почему вам это важно» с практическим выводом. Пиши по-русски, 400–700 слов, markdown."
)


def pick_topic(today: _dt.date) -> str:
    """Rotate through ROADMAP bullet topics by day-of-year so posts don't repeat."""
    fallback = [
        "Что такое MCP и зачем он агентам",
        "vLLM: как обслуживать LLM без боли и с высоким throughput",
        "RAG на пальцах: почему ретрив важнее модели",
        "Оценка LLM: зачем нужны DeepEval и RAGAS",
        "Fine-tuning с Unsloth: адаптация модели без ферм видеокарт",
        "Векторные базы: Milvus vs Qdrant vs Weaviate",
        "Anatomy агентного харнесса: цикл управления вокруг модели",
        "Prompt injection: почему ответ инструмента — это данные, а не приказ",
    ]
    topics = fallback
    try:
        text = ROADMAP.read_text(encoding="utf-8")
        bullets = re.findall(r"^\s*-\s*\[[ x]\]\s*\*\*(.+?)\*\*\s*[—-]\s*(.+)$", text, re.M)
        parsed = [f"{name}: {desc}".strip() for name, desc in bullets]
        if parsed:
            topics = parsed
    except OSError:
        pass
    return topics[today.timetuple().tm_yday % len(topics)]


def generate(topic: str, api_key: str) -> str:
    body = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Напиши пост-объяснялку на тему: «{topic}». "
                    "Это должна быть цельная, законченная статья, которую не стыдно "
                    "показать инженерам. Начни сразу с заголовка H1."
                ),
            }
        ],
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": API_VERSION,
            "content-type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        data = json.loads(resp.read())
    parts = [b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"]
    return "".join(parts).strip()


def main() -> int:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY is not set — cannot generate.", file=sys.stderr)
        return 1

    today = _dt.date.today()
    out_path = POSTS_DIR / str(today.year) / f"{today.isoformat()}.md"
    if out_path.exists():
        print(f"Post already exists: {out_path}")
        return 0

    topic = pick_topic(today)
    try:
        article = generate(topic, api_key)
    except Exception as exc:
        print(f"Generation failed: {exc}", file=sys.stderr)
        return 1

    if not article:
        print("Model returned empty content — not writing a file.", file=sys.stderr)
        return 1

    frontmatter = (
        "---\n"
        f"date: {today.isoformat()}\n"
        f"topic: {topic}\n"
        "generated: true\n"
        "---\n\n"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter + article + "\n", encoding="utf-8")
    print(f"Wrote {out_path} ({len(article)} chars) on topic: {topic}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
