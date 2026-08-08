#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post a tweet via X API v2 (OAuth 1.0a user context).

Requires env (never commit secrets):
  TWITTER_API_KEY
  TWITTER_API_SECRET
  TWITTER_ACCESS_TOKEN
  TWITTER_ACCESS_TOKEN_SECRET

Usage:
  python scripts/post_to_x.py --text "hello"
  python scripts/post_to_x.py --file docs/tweet-awesome-kling.txt
  python scripts/post_to_x.py --file docs/tweet-awesome-kling.txt --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from requests_oauthlib import OAuth1Session
except ImportError:
    print("Missing dependency. Install:\n  pip install requests requests-oauthlib", file=sys.stderr)
    raise SystemExit(2)

POST_URL = "https://api.twitter.com/2/tweets"


def require_env(name: str) -> str:
    val = os.environ.get(name, "").strip()
    if not val:
        raise SystemExit(
            f"Missing env {name}. See docs/x-mcp-setup.md\n"
            "Do not paste secrets into chat or git."
        )
    return val


def build_session() -> OAuth1Session:
    return OAuth1Session(
        client_key=require_env("TWITTER_API_KEY"),
        client_secret=require_env("TWITTER_API_SECRET"),
        resource_owner_key=require_env("TWITTER_ACCESS_TOKEN"),
        resource_owner_secret=require_env("TWITTER_ACCESS_TOKEN_SECRET"),
    )


def post_tweet(text: str, dry_run: bool = False) -> dict:
    text = text.strip()
    if not text:
        raise SystemExit("Empty tweet text")
    # X free/basic limits vary; hard cap soft-check
    if len(text) > 280 and "http" not in text:
        print(f"[warn] length={len(text)} (may fail if not Premium / long-form)", file=sys.stderr)

    payload = {"text": text}
    if dry_run:
        return {"dry_run": True, "payload": payload, "chars": len(text)}

    sess = build_session()
    resp = sess.post(POST_URL, json=payload)
    try:
        body = resp.json()
    except Exception:
        body = {"raw": resp.text}
    if resp.status_code >= 400:
        print(json.dumps(body, ensure_ascii=False, indent=2), file=sys.stderr)
        raise SystemExit(f"X API error HTTP {resp.status_code}")
    return body


def main() -> int:
    p = argparse.ArgumentParser(description="Post to X with OAuth 1.0a")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--text", help="Tweet text")
    g.add_argument("--file", type=Path, help="UTF-8 text file")
    p.add_argument("--dry-run", action="store_true", help="Print payload only")
    args = p.parse_args()

    if args.file:
        text = args.file.read_text(encoding="utf-8")
    else:
        text = args.text or ""

    result = post_tweet(text, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.dry_run:
        data = result.get("data") or {}
        tid = data.get("id")
        if tid:
            print(f"https://x.com/i/web/status/{tid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
