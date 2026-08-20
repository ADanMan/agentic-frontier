#!/usr/bin/env python3
"""Draft a daily AI digest from public sources for you to curate.

Usage:
    python3 scripts/digest.py

What it does:
  - pulls recent papers from the public arXiv API (cs.AI / cs.LG / cs.CL);
  - best-effort pulls recently-created, high-star AI repos via the `gh` CLI
    (skipped silently if `gh` is not installed or not authenticated);
  - writes a DRAFT to digests/<year>/<YYYY-MM-DD>.md.

It intentionally does NOT commit. The point of this repo is curated, real notes:
open the draft, delete what's noise, add a sentence of your own take, then commit.

Only reads public data. Sends nothing anywhere.
"""

from __future__ import annotations

import datetime as _dt
import json
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "digests"

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL"]
ARXIV_MAX = 8
HTTP_TIMEOUT = 20
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch_arxiv() -> list[dict]:
    """Return recent arXiv papers as dicts, or [] on any failure."""
    cat_query = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    params = urllib.parse.urlencode(
        {
            "search_query": cat_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": ARXIV_MAX,
        }
    )
    url = f"{ARXIV_API}?{params}"
    try:
        with urllib.request.urlopen(url, timeout=HTTP_TIMEOUT) as resp:
            raw = resp.read()
    except Exception as exc:  # network/DNS/timeout — degrade gracefully
        print(f"[arxiv] skipped: {exc}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        print(f"[arxiv] parse error: {exc}", file=sys.stderr)
        return []

    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        title = (entry.findtext(f"{ATOM}title") or "").strip().replace("\n", " ")
        summary = (entry.findtext(f"{ATOM}summary") or "").strip().replace("\n", " ")
        link = (entry.findtext(f"{ATOM}id") or "").strip()
        authors = [
            (a.findtext(f"{ATOM}name") or "").strip()
            for a in entry.findall(f"{ATOM}author")
        ]
        papers.append(
            {
                "title": title,
                "authors": authors[:4],
                "url": link,
                "summary": summary[:280] + ("…" if len(summary) > 280 else ""),
            }
        )
    return papers


def fetch_trending_repos() -> list[dict]:
    """Best-effort recent high-star AI repos via `gh`. Returns [] if unavailable."""
    since = (_dt.date.today() - _dt.timedelta(days=30)).isoformat()
    query = f"topic:ai created:>{since}"
    try:
        out = subprocess.run(
            [
                "gh", "api", "-X", "GET", "search/repositories",
                "-f", f"q={query}",
                "-f", "sort=stars",
                "-f", "order=desc",
                "-f", "per_page=6",
            ],
            capture_output=True,
            text=True,
            timeout=HTTP_TIMEOUT,
        )
    except Exception as exc:
        print(f"[gh] skipped: {exc}", file=sys.stderr)
        return []

    if out.returncode != 0:
        print(f"[gh] skipped: {out.stderr.strip()[:120]}", file=sys.stderr)
        return []

    try:
        items = json.loads(out.stdout).get("items", [])
    except json.JSONDecodeError:
        return []

    return [
        {
            "name": it.get("full_name", ""),
            "stars": it.get("stargazers_count", 0),
            "url": it.get("html_url", ""),
            "desc": (it.get("description") or "").strip(),
        }
        for it in items
    ]


def render(today: _dt.date, papers: list[dict], repos: list[dict]) -> str:
    lines = [
        "---",
        f"date: {today.isoformat()}",
        "topic: Daily AI digest (DRAFT — curate before committing)",
        "tags: [digest]",
        "---",
        "",
        f"# AI digest — {today.isoformat()}",
        "",
        "> Draft auto-generated from public sources. Delete the noise, keep what",
        "> matters, and add one line of your own take per item before committing.",
        "",
        "## Recent papers (arXiv cs.AI / cs.LG / cs.CL)",
        "",
    ]
    if papers:
        for p in papers:
            authors = ", ".join(p["authors"]) + (" et al." if len(p["authors"]) >= 4 else "")
            lines.append(f"- **[{p['title']}]({p['url']})** — {authors}")
            lines.append(f"  - {p['summary']}")
            lines.append("  - _My take:_ ")
    else:
        lines.append("_(arXiv fetch skipped — add papers manually.)_")

    lines += ["", "## Recently trending AI repos", ""]
    if repos:
        for r in repos:
            lines.append(f"- **[{r['name']}]({r['url']})** — ⭐{r['stars']}")
            if r["desc"]:
                lines.append(f"  - {r['desc']}")
            lines.append("  - _My take:_ ")
    else:
        lines.append("_(gh fetch skipped — add repos manually.)_")

    lines += ["", "## One thing worth a full guide later", "", "- [ ] ", ""]
    return "\n".join(lines)


def main() -> int:
    today = _dt.date.today()
    out_path = DIGESTS_DIR / str(today.year) / f"{today.isoformat()}.md"

    if out_path.exists():
        print(f"Draft already exists: {out_path}")
        return 0

    papers = fetch_arxiv()
    repos = fetch_trending_repos()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(today, papers, repos), encoding="utf-8")

    print(f"Drafted {out_path}")
    print(f"  papers: {len(papers)}  repos: {len(repos)}")
    print("Curate it, then:")
    print(f'  git add digests/ && git commit -m "digest: {today.isoformat()}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
