#!/usr/bin/env python3
"""Draft a daily AI digest from public sources for you to curate.

Usage:
    python3 scripts/digest.py

Sources (each is best-effort — a blocked or dead source is skipped, never fatal):
  - RSS/Atom feeds listed in feeds.txt — the industry pulse. IMPORTANT: the cloud
    post-routine runs in a sandbox whose egress proxy blocks most hosts (arXiv, vendor
    blogs, Hacker News, huggingface.co directly). What DOES get through is
    `raw.githubusercontent.com`, so feeds.txt leads with community RSS *mirrors* hosted
    there (HF trending papers, GitHub trending/ranking, HF blog) that are rebuilt daily.
    Those mirrors are what keeps the digest current from inside the sandbox. Vendor feeds
    and arXiv stay in feeds.txt below the mirrors: they enrich the digest when this script
    runs on an open network, and cost nothing when they're blocked.
  - arXiv API (expanded CS + stat.ML categories) — recent papers (open-network only);
  - recently-created high-star AI repos via the `gh` CLI (best-effort; needs a token).

For each feed item we keep a short text summary (real grounding for the write-up) and
try to extract the source page's og:image URL, so a post can embed the real source image.

Writes a DRAFT to digests/<year>/<YYYY-MM-DD>.md. It does NOT commit, and it does NOT
overwrite an existing draft for the day. Only reads public data; sends nothing anywhere.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from html import unescape
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "digests"
FEEDS_FILE = REPO_ROOT / "feeds.txt"

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_CATEGORIES = [
    "cs.AI", "cs.LG", "cs.CL", "cs.MA", "cs.IR",
    "cs.SE", "cs.DC", "cs.CR", "cs.NE", "stat.ML",
]
ARXIV_MAX = 10
HTTP_TIMEOUT = 20
UA = "agentic-frontier-digest/1.0 (+https://github.com/ADanMan/agentic-frontier)"
ATOM = "{http://www.w3.org/2005/Atom}"

MAX_PER_FEED = 3     # newest N entries kept per feed
MAX_FEED_ITEMS = 30  # overall cap across all feeds
MAX_IMAGES = 14      # how many feed items to probe for an og:image URL

# og:image / twitter:image, both attribute orders.
OG_PATTERNS = [
    rb'property=["\']og:image(?::url)?["\'][^>]*?content=["\']([^"\'>]+)["\']',
    rb'content=["\']([^"\'>]+)["\'][^>]*?property=["\']og:image(?::url)?["\']',
    rb'name=["\']twitter:image["\'][^>]*?content=["\']([^"\'>]+)["\']',
]


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        return resp.read()


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
    try:
        root = ET.fromstring(_get(f"{ARXIV_API}?{params}"))
    except Exception as exc:  # network/parse — degrade gracefully
        print(f"[arxiv] skipped: {exc}", file=sys.stderr)
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


def read_feed_urls() -> list[str]:
    """Read feeds.txt: one URL per line, ignoring blanks, comments, inline # notes."""
    try:
        lines = FEEDS_FILE.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    urls = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        url = line.split()[0]  # URL is the first token; drops any inline comment
        if url.startswith("http"):
            urls.append(url)
    return urls


def fetch_one_feed(url: str) -> list[dict]:
    """Parse one RSS or Atom feed; return newest entries as dicts, [] on failure."""
    try:
        root = ET.fromstring(_get(url))
    except Exception as exc:
        print(f"[feed] skipped {url}: {exc}", file=sys.stderr)
        return []

    source = urllib.parse.urlparse(url).netloc
    items = []
    for e in root.iter():
        if e.tag.split("}")[-1] not in ("item", "entry"):  # RSS item / Atom entry
            continue
        title = link = summary = None
        for child in e:
            tag = child.tag.split("}")[-1]
            if tag == "title" and child.text and not title:
                title = child.text.strip()
            elif tag == "link":
                if child.text and child.text.strip():           # RSS: text link
                    link = child.text.strip()
                elif child.get("href") and (                    # Atom: href attr
                    not link or child.get("rel") in (None, "alternate")
                ):
                    link = child.get("href")
            elif tag in ("description", "summary", "content") and not summary:
                summary = "".join(child.itertext()).strip()
        if title and link:
            items.append({
                "title": title,
                "url": link,
                "source": source,
                "image": None,
                "summary": _clean_summary(summary),
            })
        if len(items) >= MAX_PER_FEED:
            break
    return items


def _clean_summary(text: str | None) -> str:
    """Strip HTML tags/entities from a feed summary and trim to a short snippet."""
    if not text:
        return ""
    text = unescape(re.sub(r"<[^>]+>", " ", text))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:280] + ("…" if len(text) > 280 else "")


def fetch_feeds() -> list[dict]:
    """Fetch every feed in feeds.txt, dedup by URL, cap the total."""
    seen, out = set(), []
    for url in read_feed_urls():
        for item in fetch_one_feed(url):
            if item["url"] in seen:
                continue
            seen.add(item["url"])
            out.append(item)
            if len(out) >= MAX_FEED_ITEMS:
                return out
    return out


def fetch_og_image_url(page_url: str) -> str | None:
    """Return the source page's og:image (absolute URL), or None. Best-effort."""
    try:
        html = _get(page_url)
    except Exception:
        return None
    for pat in OG_PATTERNS:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            raw = unescape(m.group(1).decode("utf-8", "ignore").strip())
            url = urllib.parse.urljoin(page_url, raw)
            if url.startswith("http"):
                return url
    return None


def attach_images(feeds: list[dict]) -> None:
    """Probe the first MAX_IMAGES feed items for an og:image URL (in place)."""
    for item in feeds[:MAX_IMAGES]:
        item["image"] = fetch_og_image_url(item["url"])


def fetch_trending_repos() -> list[dict]:
    """Best-effort recent high-star AI repos via `gh`. Returns [] if unavailable."""
    since = (_dt.date.today() - _dt.timedelta(days=30)).isoformat()
    query = f"topic:ai created:>{since}"
    try:
        proc = subprocess.run(
            [
                "gh", "api", "-X", "GET", "search/repositories",
                "-f", f"q={query}", "-f", "sort=stars",
                "-f", "order=desc", "-f", "per_page=6",
            ],
            capture_output=True, text=True, timeout=HTTP_TIMEOUT,
        )
    except Exception as exc:
        print(f"[gh] skipped: {exc}", file=sys.stderr)
        return []
    if proc.returncode != 0:
        print(f"[gh] skipped: {proc.stderr.strip()[:120]}", file=sys.stderr)
        return []
    try:
        items = json.loads(proc.stdout).get("items", [])
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


def render(today, papers, feeds, repos) -> str:
    lines = [
        "---",
        f"date: {today.isoformat()}",
        "topic: Daily AI digest (DRAFT — curate before committing)",
        "tags: [digest]",
        "---",
        "",
        f"# AI digest — {today.isoformat()}",
        "",
        "> Draft auto-generated from public sources. Every item carries its real source",
        "> URL; feed items may also carry an `image:` (the source's og:image).",
        "",
        "## Recent papers (arXiv)",
        "",
    ]
    if papers:
        for p in papers:
            authors = ", ".join(p["authors"]) + (" et al." if len(p["authors"]) >= 4 else "")
            lines.append(f"- **[{p['title']}]({p['url']})** — {authors}")
            lines.append(f"  - source: {p['url']}")
            lines.append(f"  - {p['summary']}")
    else:
        lines.append("_(arXiv fetch skipped — add papers manually.)_")

    lines += ["", "## Industry / news & blogs", ""]
    if feeds:
        for f in feeds:
            lines.append(f"- [{f['title']}]({f['url']}) — _{f['source']}_")
            lines.append(f"  - source: {f['url']}")
            if f.get("image"):
                lines.append(f"  - image: {f['image']}")
            if f.get("summary"):
                lines.append(f"  - {f['summary']}")
    else:
        lines.append("_(no feed items — feeds.txt empty or all fetches failed.)_")

    lines += ["", "## Recently trending AI repos", ""]
    if repos:
        for r in repos:
            lines.append(f"- **[{r['name']}]({r['url']})** — ⭐{r['stars']}")
            lines.append(f"  - source: {r['url']}")
            if r["desc"]:
                lines.append(f"  - {r['desc']}")
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
    feeds = fetch_feeds()
    attach_images(feeds)
    repos = fetch_trending_repos()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(today, papers, feeds, repos), encoding="utf-8")

    with_img = sum(1 for f in feeds if f.get("image"))
    print(f"Drafted {out_path}")
    print(f"  papers: {len(papers)}  feed items: {len(feeds)} ({with_img} w/ image)  repos: {len(repos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
