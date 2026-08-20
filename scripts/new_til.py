#!/usr/bin/env python3
"""Scaffold a dated "Today I Learned" note from a template.

Usage:
    python scripts/new_til.py "short topic of what I looked at today"

This creates til/<year>/<YYYY-MM-DD>.md pre-filled with a template you then write
into by hand. It intentionally does NOT commit anything and does NOT generate
content — the point of this repo is real notes backed by real learning, not filler.

If today's file already exists, it is left untouched (so re-running is safe) and its
path is printed so you can keep editing it.
"""

from __future__ import annotations

import datetime as _dt
import sys
from pathlib import Path

# Repo root is the parent of the scripts/ directory this file lives in.
REPO_ROOT = Path(__file__).resolve().parent.parent
TIL_DIR = REPO_ROOT / "til"

TEMPLATE = """---
date: {date}
topic: {topic}
tags: []
---

# {date}

## What I did

<!-- What did you actually touch today? One or two lines. -->

## What I learned

<!-- 3-5 real sentences. If you can't fill this in, you didn't learn something
     today worth committing — that's fine, skip the commit. -->

## Next

- [ ] <!-- one concrete follow-up -->
"""


def build_note_path(today: _dt.date) -> Path:
    """Return the path til/<year>/<YYYY-MM-DD>.md for the given date."""
    return TIL_DIR / str(today.year) / f"{today.isoformat()}.md"


def main(argv: list[str]) -> int:
    topic = " ".join(argv[1:]).strip() or "(fill in a topic)"
    today = _dt.date.today()

    note_path = build_note_path(today)

    if note_path.exists():
        print(f"Already exists, leaving it be: {note_path}")
        print("Open it and keep writing, then:")
        print(f'  git add til/ && git commit -m "til: {topic}"')
        return 0

    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(
        TEMPLATE.format(date=today.isoformat(), topic=topic),
        encoding="utf-8",
    )

    print(f"Created {note_path}")
    print("Now open it, write 3-5 real sentences, then:")
    print(f'  git add til/ && git commit -m "til: {topic}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
