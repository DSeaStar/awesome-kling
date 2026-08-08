#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare a crawl candidate markdown/json against URLs and prompt snippets
already present in the repo.

Usage:
  python scripts/dedupe_candidates.py docs/x-crawl-candidates/2026-08-08.md
  python scripts/dedupe_candidates.py docs/x-crawl-candidates/2026-08-08.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_GLOBS = [
    "README.md",
    "README-en.md",
    "prompts/**/*.md",
    "docs/**/*.md",
]

URL_RE = re.compile(r"https?://(?:x|twitter)\.com/[^/\s]+/status/(\d+)", re.I)
STATUS_RE = re.compile(r"status/(\d+)")


def load_repo_status_ids() -> set[str]:
    ids: set[str] = set()
    for pattern in SCAN_GLOBS:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            if "x-crawl-candidates" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            ids.update(URL_RE.findall(text))
            ids.update(STATUS_RE.findall(text))
    return ids


def load_repo_blobs() -> str:
    chunks: list[str] = []
    for pattern in ("prompts/**/*.md", "README.md", "README-en.md"):
        for path in ROOT.glob(pattern):
            if path.is_file():
                chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(chunks).lower()


def extract_ids_from_text(text: str) -> list[str]:
    return list(dict.fromkeys(URL_RE.findall(text) + STATUS_RE.findall(text)))


def snippet_overlap(candidate: str, corpus: str, min_len: int = 48) -> bool:
    c = re.sub(r"\s+", " ", candidate.lower()).strip()
    if len(c) < min_len:
        return False
    # sliding windows of 48 chars
    step = 24
    for i in range(0, min(len(c) - min_len, 400), step):
        win = c[i : i + min_len]
        if win in corpus:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, help="candidate .md or .json")
    args = parser.parse_args()
    path: Path = args.path
    if not path.is_file():
        print(f"not found: {path}", file=sys.stderr)
        return 2

    known = load_repo_status_ids()
    corpus = load_repo_blobs()
    raw = path.read_text(encoding="utf-8", errors="ignore")

    print(f"repo known status ids: {len(known)}")
    print(f"scanning: {path}")

    dup_urls = 0
    new_urls = 0
    text_hits = 0

    if path.suffix.lower() == ".json":
        data = json.loads(raw)
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0

    # Markdown: per ### block
    blocks = re.split(r"(?=^### )", raw, flags=re.M)
    for block in blocks:
        if not block.startswith("### "):
            continue
        title = block.splitlines()[0]
        ids = extract_ids_from_text(block)
        is_dup = any(i in known for i in ids)
        # code preview
        codes = re.findall(r"```(?:text)?\n(.*?)```", block, flags=re.S)
        overlap = any(snippet_overlap(c, corpus) for c in codes)
        flag = []
        if is_dup:
            flag.append("URL_DUP")
            dup_urls += 1
        else:
            if ids:
                new_urls += 1
        if overlap:
            flag.append("TEXT_SIMILAR")
            text_hits += 1
        mark = ",".join(flag) if flag else "NEW"
        id_s = ",".join(ids) if ids else "-"
        print(f"[{mark}] {title[:80]} | ids={id_s}")

    print("---")
    print(f"summary: new_url_blocks≈{new_urls}, url_dup={dup_urls}, text_similar={text_hits}")
    print("Promote only NEW (and review TEXT_SIMILAR manually).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
