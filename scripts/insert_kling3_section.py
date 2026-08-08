#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

TOC_ZH = """## 📖 目录

> **排序规则：** 各类别内**新增提示词一律插到该节最前面**（最新优先）。Kling 3.0 / Omni 专区已置顶。

1. [Kling 3.0 / Omni 专区](#1-kling-30--omni-专区)
2. [图生视频 I2V（X 精选）](#2-图生视频-i2vx-精选)
3. [Seedance 提示词（X 精选）](#3-seedance-提示词x-精选)
4. [文生图（T2I）](#4-文生图t2i)
5. [提示词公式（从这里开始）](#5-提示词公式从这里开始)
6. [电影风格](#6-电影风格)
7. [广告与商业品牌](#7-广告与商业品牌)
8. [社交媒体与病毒模因](#8-社交媒体与病毒模因)
9. [UGC 风格](#9-ugc-风格)
10. [动漫与动画风格](#10-动漫与动画风格)
11. [短剧与网剧](#11-短剧与网剧)
12. [视觉特效与实验风格](#12-视觉特效与实验风格)
13. [运动控制与角色一致性](#13-运动控制与角色一致性)
14. [资源 (API、SDK 与使用指南)](#14-资源)
15. [贡献指南](#15-贡献指南)
16. [Star 历史](#16-star-历史)

---
"""

TOC_EN = """## 📖 Table of Contents

> **Ordering rule:** New prompts always go first within each section. **Kling 3.0 / Omni** is pinned to the top.

1. [Kling 3.0 / Omni](#1-kling-30--omni)
2. [Image-to-Video I2V (from X)](#2-image-to-video-i2v-from-x)
3. [Seedance Prompts (from X)](#3-seedance-prompts-from-x)
4. [Text-to-Image (T2I)](#4-text-to-image-t2i)
5. [Prompt Formula (Start Here)](#5-prompt-formula-start-here)
6. [Cinematic Film Styles](#6-cinematic-film-styles)
7. [Advertising & Commercial Branding](#7-advertising--commercial-branding)
8. [Social Media & Viral Memes](#8-social-media--viral-memes)
9. [UGC Style](#9-ugc-style)
10. [Anime & Animation Styles](#10-anime--animation-styles)
11. [Short-form Drama & Web Series](#11-short-form-drama--web-series)
12. [Visual Effects & Experimental Styles](#12-visual-effects--experimental-styles)
13. [Motion Control & Character Consistency](#13-motion-control--character-consistency)
14. [Resources (API, SDK & How-to-use)](#14-resources)
15. [Contributing](#15-contributing)
16. [Star History](#16-star-history)

---
"""

SECS_ZH = """## 1. Kling 3.0 / Omni 专区

面向 **Kling 3.0 / Pro / VIDEO 3.0 Omni** 的分镜、原生音频、多参考与 Motion Control。完整包：[`prompts/kling-3-omni.md`](./prompts/kling-3-omni.md) · 负向：[`prompts/negative-prompts.md`](./prompts/negative-prompts.md) · 工作流：[`prompts/workflows.md`](./prompts/workflows.md) · 对照：[`docs/model-comparison.md`](./docs/model-comparison.md)

> **新提示词永远放在最前面。**

### 1.1. 深夜排练室 vlog（原生对白）

*来源：[@YourAlphaMom](https://x.com/YourAlphaMom/status/2085350644915765377)（同 prompt 横评含 Kling 3.0 Pro）*

```text
CAMERA: DV 16mm handheld selfie vlog; natural shake; imperfect framing; camera body never visible.
LOOK: Soft tape look, mild grain, realistic skin.
STYLE: Late-night post-practice, tired but happy, intimate.
CHARACTER: Brunette model mid-20s, athletic long-sleeve + joggers, light sweat.
SETTING: Empty dance studio at night, mirrors, wooden floor, water bottle + towel.
STORYBOARD (~2s each): enter out of breath "Finally done… it's way too late." → pan empty studio → drink water "I really needed that." → short dance combo laugh → selfie wave "Okay, I'm going home. Good night."
```

### 1.2. 美食俯拍 B-roll（一镜）

*来源：[@emberbuild](https://x.com/emberbuild/status/2085252050053435406)*

```text
Overhead food B-roll, Kling 3.0, single continuous shot. Batter hits a hot pan; edges crisp; steam in morning light; slow drift; photoreal; no text.
```

### 1.3. Omni 多模态分块模板

```text
[MODE] Kling 3.0 Omni · multi-shot · native audio on
[SUBJECT] …  [ACTION] …  [SETTING] …
[CAMERA] shot · angle · move
[AUDIO] "dialogue" · SFX · ambience
[TIMELINE] [0-3s] Shot 1 — …  [3-7s] Shot 2 — …
[QUALITY] photoreal, stable identity, 4K
```

官方指南：[Omni User Guide](https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide) · [Prompt Guide](https://kling.ai/blog/kling-ai-prompt-guide)

---

"""

SECS_EN = """## 1. Kling 3.0 / Omni

Prompts for **Kling 3.0 / Pro / VIDEO 3.0 Omni** — multi-shot, native audio, Elements, Motion Control. Full pack: [`prompts/kling-3-omni.md`](./prompts/kling-3-omni.md) · Negatives: [`prompts/negative-prompts.md`](./prompts/negative-prompts.md) · Workflows: [`prompts/workflows.md`](./prompts/workflows.md) · Comparison: [`docs/model-comparison.md`](./docs/model-comparison.md)

> **Newest first.**

### 1.1. Late-night rehearsal vlog (native dialogue)

*Source: [@YourAlphaMom](https://x.com/YourAlphaMom/status/2085350644915765377) (same-prompt bake-off including Kling 3.0 Pro)*

```text
CAMERA: DV 16mm handheld selfie vlog; natural shake; imperfect framing; camera body never visible.
LOOK: Soft tape look, mild grain, realistic skin.
STYLE: Late-night post-practice, tired but happy, intimate.
CHARACTER: Brunette model mid-20s, athletic long-sleeve + joggers, light sweat.
SETTING: Empty dance studio at night, mirrors, wooden floor, water bottle + towel.
STORYBOARD (~2s each): enter out of breath "Finally done… it's way too late." → pan empty studio → drink water "I really needed that." → short dance combo laugh → selfie wave "Okay, I'm going home. Good night."
```

### 1.2. Overhead food B-roll (one shot)

*Source: [@emberbuild](https://x.com/emberbuild/status/2085252050053435406)*

```text
Overhead food B-roll, Kling 3.0, single continuous shot. Batter hits a hot pan; edges crisp; steam in morning light; slow drift; photoreal; no text.
```

### 1.3. Omni block template

```text
[MODE] Kling 3.0 Omni · multi-shot · native audio on
[SUBJECT] …  [ACTION] …  [SETTING] …
[CAMERA] shot · angle · move
[AUDIO] "dialogue" · SFX · ambience
[TIMELINE] [0-3s] Shot 1 — …  [3-7s] Shot 2 — …
[QUALITY] photoreal, stable identity, 4K
```

Official: [Omni User Guide](https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide) · [Prompt Guide](https://kling.ai/blog/kling-ai-prompt-guide)

---

"""


def shift_sections(text: str, delta: int = 1, max_n: int = 15) -> str:
    for n in range(max_n, 0, -1):
        text = re.sub(rf"(## )\s*{n}\. ", rf"\1__OLD{n}__. ", text)
        text = re.sub(rf"(### )\s*{n}\.", rf"\1__OLD{n}__.", text)
    for n in range(1, max_n + 1):
        text = text.replace(f"__OLD{n}__", str(n + delta))
    return text


def replace_toc(text: str, toc: str, is_zh: bool) -> str:
    pat = r"## 📖 目录\n.*?\n---\n" if is_zh else r"## 📖 Table of Contents\n.*?\n---\n"
    out, n = re.subn(pat, toc, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"TOC replace failed zh={is_zh} n={n}")
    return out


def insert_body(text: str, body: str, marker_re: str) -> str:
    m = re.search(marker_re, text, re.M)
    if not m:
        raise SystemExit(f"marker not found: {marker_re}")
    return text[: m.start()] + body + text[m.start() :]


def patch_resources(text: str, is_zh: bool) -> str:
    if is_zh:
        needle = "- 本仓库：[`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) — X 爬取 I2V"
        add = (
            "- 本仓库：[`prompts/kling-3-omni.md`](./prompts/kling-3-omni.md) — Kling 3.0 / Omni\n"
            "- 本仓库：[`prompts/negative-prompts.md`](./prompts/negative-prompts.md) — 负向提示词库\n"
            "- 本仓库：[`prompts/workflows.md`](./prompts/workflows.md) — 生产工作流 Cookbook\n"
            "- 本仓库：[`docs/model-comparison.md`](./docs/model-comparison.md) — 模型对照\n"
            "- 本仓库：[`CONTRIBUTING.md`](./CONTRIBUTING.md) — 贡献指南（最新优先）\n"
            "- 站点：[`docs/site/`](./docs/site/) — GitHub Pages 导航页\n"
            + needle
        )
    else:
        needle = "- In-repo: [`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) — I2V from X"
        add = (
            "- In-repo: [`prompts/kling-3-omni.md`](./prompts/kling-3-omni.md) — Kling 3.0 / Omni\n"
            "- In-repo: [`prompts/negative-prompts.md`](./prompts/negative-prompts.md) — negatives\n"
            "- In-repo: [`prompts/workflows.md`](./prompts/workflows.md) — workflows cookbook\n"
            "- In-repo: [`docs/model-comparison.md`](./docs/model-comparison.md) — model comparison\n"
            "- In-repo: [`CONTRIBUTING-en.md`](./CONTRIBUTING-en.md) — contributing (newest-first)\n"
            "- Site: [`docs/site/`](./docs/site/) — GitHub Pages nav\n"
            + needle
        )
    if "kling-3-omni.md" in text:
        return text
    if needle not in text:
        raise SystemExit("resource needle missing")
    return text.replace(needle, add, 1)


def patch_contrib_section(text: str, is_zh: bool) -> str:
    if is_zh:
        # Expand short contributing section pointer
        old = "## 15. 贡献指南\n"
        # after shift it will be 15 before insert... after full process sections are 15/16
        pass
    return text


def patch_intro(text: str, is_zh: bool) -> str:
    if is_zh:
        text = text.replace(
            "本仓库专注于**高保真 Kling 提示词**：I2V / Seedance（X 精选）、T2I 肖像",
            "本仓库专注于**高保真 Kling 提示词**：Kling 3.0 / Omni、I2V / Seedance（X 精选）、T2I 肖像",
            1,
        )
        if "awesome-seedance" in text and "互链" not in text:
            text = text.replace(
                "结构与风格参考 [awesome-seedance](https://github.com/ZeroLu/awesome-seedance)。",
                "结构与风格参考 [awesome-seedance](https://github.com/ZeroLu/awesome-seedance)（**sibling 互链**）。欢迎阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [周更日志](./docs/x-crawl-log.md)。",
                1,
            )
    else:
        text = text.replace(
            "for I2V & Seedance (from X), T2I portraits",
            "for Kling 3.0 / Omni, I2V & Seedance (from X), T2I portraits",
            1,
        )
        text = text.replace(
            "Inspired by [awesome-seedance](https://github.com/ZeroLu/awesome-seedance).",
            "Inspired by [awesome-seedance](https://github.com/ZeroLu/awesome-seedance) (sibling list). See [CONTRIBUTING-en.md](./CONTRIBUTING-en.md) and the [weekly crawl log](./docs/x-crawl-log.md).",
            1,
        )
    return text


def patch_contributing_body(text: str, is_zh: bool) -> str:
    if is_zh:
        text = re.sub(
            r"(## 15\. 贡献指南\n\n)([\s\S]*?)(\n---\n\n## 16\. Star)",
            r"\1欢迎贡献！完整规范见 [CONTRIBUTING.md](./CONTRIBUTING.md)（**最新优先**、周更晋升清单、Issue/PR 模板）。\n\n"
            r"快速规则：\n\n"
            r"1. 新条目插到对应分类**最前面**（`X.1`）\n"
            r"2. 同步 `README.md` + `README-en.md`\n"
            r"3. 标注 Source；长文放 `prompts/`\n"
            r"4. 候选晋升：`docs/PROMOTE_CHECKLIST.md` + `scripts/dedupe_candidates.py`\n"
            r"\3",
            text,
            count=1,
        )
    else:
        text = re.sub(
            r"(## 15\. Contributing\n\n)([\s\S]*?)(\n---\n\n## 16\. Star)",
            r"\1Contributions welcome! Full guide: [CONTRIBUTING-en.md](./CONTRIBUTING-en.md) "
            r"(**newest-first**, weekly promote checklist, issue/PR templates).\n\n"
            r"Quick rules:\n\n"
            r"1. Insert at the **top** of the section (`X.1`)\n"
            r"2. Update `README.md` + `README-en.md`\n"
            r"3. Credit Source; long-form under `prompts/`\n"
            r"4. Promote via `docs/PROMOTE_CHECKLIST.md` + `scripts/dedupe_candidates.py`\n"
            r"\3",
            text,
            count=1,
        )
    return text


def main() -> None:
    zh_path = ROOT / "README.md"
    en_path = ROOT / "README-en.md"

    zh = zh_path.read_text(encoding="utf-8")
    zh = shift_sections(zh, 1, 15)
    zh = replace_toc(zh, TOC_ZH, True)
    zh = insert_body(zh, SECS_ZH, r"^## 2\. 图生视频")
    zh = patch_resources(zh, True)
    zh = patch_intro(zh, True)
    zh = patch_contributing_body(zh, True)
    zh_path.write_text(zh, encoding="utf-8", newline="\n")

    en = en_path.read_text(encoding="utf-8")
    en = shift_sections(en, 1, 15)
    en = replace_toc(en, TOC_EN, False)
    en = insert_body(en, SECS_EN, r"^## 2\. Image-to-Video")
    en = patch_resources(en, False)
    en = patch_intro(en, False)
    en = patch_contributing_body(en, False)
    en_path.write_text(en, encoding="utf-8", newline="\n")

    for p in (zh_path, en_path):
        print("===", p.name)
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                print(line)


if __name__ == "__main__":
    main()
