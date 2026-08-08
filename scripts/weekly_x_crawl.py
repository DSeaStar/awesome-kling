#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weekly X (Twitter) prompt crawl for awesome-kling.

- Requires TWITTER_BEARER_TOKEN (or X_BEARER_TOKEN) for live search.
- Without a token, writes a checklist-only report so the workflow still produces output.
- Does NOT auto-merge into curated packs; writes candidates under docs/x-crawl-candidates/
  for human/agent review (newest-first rule when promoting to prompts/*).

Usage:
  python scripts/weekly_x_crawl.py
  python scripts/weekly_x_crawl.py --days 7 --max-results 20
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES_DIR = ROOT / "docs" / "x-crawl-candidates"
LOG_PATH = ROOT / "docs" / "x-crawl-log.md"

# Twitter recent-search queries (API v2; no min_faves operator — filter client-side)
QUERIES = {
    "i2v": [
        '(Kling OR 可灵 OR "Kling AI") ("image to video" OR I2V OR 图生视频) (prompt OR Prompt OR 提示词) -is:retweet lang:en',
        '(Kling OR 可灵) (prompt OR 提示词) ("image to video" OR 图生) -is:retweet',
    ],
    "seedance": [
        'Seedance (prompt OR Prompt OR 提示词 OR "Scene 1" OR "SHOT 1") -is:retweet',
        '("Seedance 2" OR "Seedance 2.0" OR "Seedance 2.5") (prompt OR Prompt) -is:retweet',
    ],
    "kling3": [
        '("Kling 3" OR "Kling 3.0" OR "Kling Omni" OR "Kling 3.0 Pro" OR 可灵3 OR "可灵 3.0") (prompt OR Prompt OR 提示词 OR STORYBOARD OR CAMERA) -is:retweet',
    ],
}

STATUS_RE = re.compile(r"status/(\d+)")

PROMPTISH = re.compile(
    r"(prompt|提示词|scene\s*\d|shot\s*\d|\[0[-–]\d|duration:|camera:|negative)",
    re.I,
)


def bearer_token() -> str | None:
    return os.environ.get("TWITTER_BEARER_TOKEN") or os.environ.get("X_BEARER_TOKEN")


def search_recent(query: str, max_results: int = 20) -> list[dict]:
    token = bearer_token()
    if not token:
        return []

    params = {
        "query": query,
        "max_results": str(min(max(10, max_results), 100)),
        "tweet.fields": "created_at,public_metrics,author_id,lang,entities",
        "expansions": "author_id",
        "user.fields": "username,name",
    }
    url = "https://api.twitter.com/2/tweets/search/recent?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-kling-weekly-crawl/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[warn] HTTP {e.code} for query={query!r}: {body[:500]}", file=sys.stderr)
        return []
    except Exception as e:  # noqa: BLE001
        print(f"[warn] search failed: {e}", file=sys.stderr)
        return []

    users = {
        u["id"]: u for u in (payload.get("includes") or {}).get("users", [])
    }
    out = []
    for tw in payload.get("data") or []:
        uid = tw.get("author_id")
        user = users.get(uid, {})
        metrics = tw.get("public_metrics") or {}
        likes = int(metrics.get("like_count") or 0)
        out.append(
            {
                "id": tw["id"],
                "text": tw.get("text") or "",
                "created_at": tw.get("created_at"),
                "username": user.get("username") or "unknown",
                "name": user.get("name") or "",
                "likes": likes,
                "url": f"https://x.com/{user.get('username', 'i')}/status/{tw['id']}",
            }
        )
    return out


def score_tweet(t: dict) -> float:
    text = t.get("text") or ""
    score = float(t.get("likes") or 0)
    if PROMPTISH.search(text):
        score += 25
    if len(text) > 280:
        score += 10
    if "```" in text or "Scene" in text or "SHOT" in text:
        score += 15
    return score


def dedupe(tweets: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for t in sorted(tweets, key=score_tweet, reverse=True):
        if t["id"] in seen:
            continue
        seen.add(t["id"])
        out.append(t)
    return out


def known_status_ids() -> set[str]:
    ids: set[str] = set()
    for pattern in ("README.md", "README-en.md", "prompts/**/*.md", "docs/**/*.md"):
        for path in ROOT.glob(pattern):
            if not path.is_file() or "x-crawl-candidates" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            ids.update(STATUS_RE.findall(text))
    return ids


def filter_known(tweets: list[dict], known: set[str]) -> tuple[list[dict], list[dict]]:
    fresh, skipped = [], []
    for t in tweets:
        if t["id"] in known:
            skipped.append(t)
        else:
            fresh.append(t)
    return fresh, skipped


def render_report(
    date: str,
    i2v: list[dict],
    seedance: list[dict],
    kling3: list[dict],
    has_token: bool,
    skipped_n: int,
) -> str:
    lines = [
        f"# X crawl candidates — {date}",
        "",
        f"> Generated by `scripts/weekly_x_crawl.py` (UTC). Live API: **{'yes' if has_token else 'no (checklist only)'}**. "
        f"Skipped already-in-repo URLs: **{skipped_n}**.",
        "",
        "## Review checklist",
        "",
        "- [ ] Open high-signal posts; extract full prompts (follow threads if needed)",
        "- [ ] Run `python scripts/dedupe_candidates.py docs/x-crawl-candidates/"
        + date
        + ".md`",
        "- [ ] Insert **at the top** (newest first):",
        "  - I2V → `prompts/i2v-from-x.md`",
        "  - Seedance → `prompts/seedance-from-x.md`",
        "  - Kling 3.0 → `prompts/kling-3-omni.md`",
        "- [ ] Mirror highlights into `README.md` + `README-en.md`",
        "- [ ] Follow [docs/PROMOTE_CHECKLIST.md](../PROMOTE_CHECKLIST.md)",
        "- [ ] Credit Source: `@handle` + post URL",
        "",
        "## Suggested queries",
        "",
        "```",
        '(Kling OR 可灵) ("image to video" OR I2V OR 图生视频) (prompt OR 提示词)',
        '("Kling 3" OR "Kling Omni" OR 可灵3) (prompt OR STORYBOARD OR CAMERA)',
        'Seedance (Prompt OR 提示词 OR "Scene 1" OR "SHOT 1")',
        "from:MayorKingAI Kling",
        "```",
        "",
    ]

    def section(title: str, items: list[dict]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("_No tweets returned this week (or API unavailable)._")
            lines.append("")
            return
        for i, t in enumerate(items, 1):
            preview = (t["text"] or "").replace("\n", " ").strip()
            if len(preview) > 400:
                preview = preview[:400] + "…"
            lines.append(f"### {i}. @{t['username']} · {t['likes']} likes")
            lines.append("")
            lines.append(f"- URL: {t['url']}")
            lines.append(f"- Created: {t.get('created_at')}")
            lines.append(f"- Score: {score_tweet(t):.0f}")
            lines.append("")
            lines.append("```text")
            lines.append(preview)
            lines.append("```")
            lines.append("")

    section("Kling 3.0 / Omni candidates", kling3)
    section("I2V / Kling candidates", i2v)
    section("Seedance candidates", seedance)

    lines.extend(
        [
            "## Promote template",
            "",
            "```markdown",
            "### X.Y. Title",
            "*One-line description.*",
            "",
            "**Prompt:**",
            "```text",
            "...",
            "```",
            "",
            "*Source: Name ([@handle](https://x.com/handle)) — [Post](url)*",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def append_log_row(
    date: str, i2v_n: int, seed_n: int, k3_n: int, mode: str
) -> None:
    if not LOG_PATH.exists():
        return
    text = LOG_PATH.read_text(encoding="utf-8")
    row = (
        f"| {date} | weekly auto | {mode} | "
        f"`docs/x-crawl-candidates/{date}.md` | I2V={i2v_n}, Seedance={seed_n}, K3={k3_n} |"
    )
    marker = "## 爬取批次\n\n"
    if marker not in text:
        return
    # Insert after table header block: find first data row or end of header
    table_header = (
        "| 日期 | 主题 | 工具/查询 | 入库文件 | 条数 |\n"
        "|------|------|-----------|----------|------|\n"
    )
    if table_header in text and row not in text:
        text = text.replace(table_header, table_header + row + "\n", 1)
        LOG_PATH.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-results", type=int, default=20)
    parser.add_argument("--min-likes", type=int, default=0)
    parser.add_argument("--date", default=None, help="UTC date stamp YYYY-MM-DD")
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    has_token = bool(bearer_token())

    i2v_raw: list[dict] = []
    seed_raw: list[dict] = []
    k3_raw: list[dict] = []

    if has_token:
        for q in QUERIES["i2v"]:
            i2v_raw.extend(search_recent(q, args.max_results))
        for q in QUERIES["seedance"]:
            seed_raw.extend(search_recent(q, args.max_results))
        for q in QUERIES["kling3"]:
            k3_raw.extend(search_recent(q, args.max_results))
    else:
        print("[info] No TWITTER_BEARER_TOKEN / X_BEARER_TOKEN — checklist-only mode.")

    known = known_status_ids()

    def filt(items: list[dict]) -> tuple[list[dict], int]:
        items = dedupe(items)
        if args.min_likes:
            items = [t for t in items if t["likes"] >= args.min_likes]
        fresh, skipped = filter_known(items, known)
        return fresh[:30], len(skipped)

    i2v, sk1 = filt(i2v_raw)
    seed, sk2 = filt(seed_raw)
    kling3, sk3 = filt(k3_raw)
    skipped_n = sk1 + sk2 + sk3

    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CANDIDATES_DIR / f"{date}.md"
    report = render_report(date, i2v, seed, kling3, has_token, skipped_n)
    out_path.write_text(report, encoding="utf-8", newline="\n")
    print(
        f"[ok] wrote {out_path.relative_to(ROOT)} "
        f"(i2v={len(i2v)}, seedance={len(seed)}, k3={len(kling3)}, skipped={skipped_n})"
    )

    mode = "Twitter API v2 recent search" if has_token else "checklist-only (no token)"
    append_log_row(date, len(i2v), len(seed), len(kling3), mode)

    # Machine-readable summary for CI
    summary = {
        "date": date,
        "has_token": has_token,
        "i2v_count": len(i2v),
        "seedance_count": len(seed),
        "kling3_count": len(kling3),
        "skipped_known": skipped_n,
        "path": str(out_path.relative_to(ROOT)).replace("\\", "/"),
    }
    summary_path = CANDIDATES_DIR / f"{date}.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
