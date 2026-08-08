#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

TOC_ZH = """## 📖 目录

> **排序规则：** 各类别内**新增提示词一律插到该节最前面**（最新优先）。本次从 X 爬取 I2V / Seedance 提示词已置顶。

1. [图生视频 I2V（X 精选）](#1-图生视频-i2vx-精选)
2. [Seedance 提示词（X 精选）](#2-seedance-提示词x-精选)
3. [文生图（T2I）](#3-文生图t2i)
4. [提示词公式（从这里开始）](#4-提示词公式从这里开始)
5. [电影风格](#5-电影风格)
6. [广告与商业品牌](#6-广告与商业品牌)
7. [社交媒体与病毒模因](#7-社交媒体与病毒模因)
8. [UGC 风格](#8-ugc-风格)
9. [动漫与动画风格](#9-动漫与动画风格)
10. [短剧与网剧](#10-短剧与网剧)
11. [视觉特效与实验风格](#11-视觉特效与实验风格)
12. [运动控制与角色一致性](#12-运动控制与角色一致性)
13. [资源 (API、SDK 与使用指南)](#13-资源)
14. [贡献指南](#14-贡献指南)
15. [Star 历史](#15-star-历史)

---
"""

TOC_EN = """## 📖 Table of Contents

> **Ordering rule:** New prompts always go first within each section. Latest X crawl (I2V / Seedance) is pinned to the top.

1. [Image-to-Video I2V (from X)](#1-image-to-video-i2v-from-x)
2. [Seedance Prompts (from X)](#2-seedance-prompts-from-x)
3. [Text-to-Image (T2I)](#3-text-to-image-t2i)
4. [Prompt Formula (Start Here)](#4-prompt-formula-start-here)
5. [Cinematic Film Styles](#5-cinematic-film-styles)
6. [Advertising & Commercial Branding](#6-advertising--commercial-branding)
7. [Social Media & Viral Memes](#7-social-media--viral-memes)
8. [UGC Style](#8-ugc-style)
9. [Anime & Animation Styles](#9-anime--animation-styles)
10. [Short-form Drama & Web Series](#10-short-form-drama--web-series)
11. [Visual Effects & Experimental Styles](#11-visual-effects--experimental-styles)
12. [Motion Control & Character Consistency](#12-motion-control--character-consistency)
13. [Resources (API, SDK & How-to-use)](#13-resources)
14. [Contributing](#14-contributing)
15. [Star History](#15-star-history)

---
"""

SECS_ZH = """## 1. 图生视频 I2V（X 精选）

从 X 爬取的 **Kling 图生视频** 提示词（需上传参考静帧）。完整合集：[`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) · 日志：[`docs/x-crawl-log.md`](./docs/x-crawl-log.md)

> 本节遵循：**新提示词永远放在最前面**。

### 1.1. Kling 2.1 I2V 合集（精选）

*来源：[MayorkingAI (@MayorKingAI)](https://x.com/MayorKingAI) — [Thread](https://x.com/MayorKingAI/status/1927126460352893348)*

```text
Tracking shot following a warrior woman riding a massive white wolf running at high speed across a frozen tundra, snow flying up from paws, wind whipping her cloak, cold blue tones, dramatic atmosphere, cinematic realism
```

```text
Aerial tracking shot of two cars drifting around a neon-lit Tokyo highway curve, tire smoke rising, reflections shimmering on wet asphalt. Electric atmosphere, dynamic, intense
```

```text
Slow zoom in on the face of a Korean Man in an elegant tailored suit, looking directly into the camera, centred composition, smoking a cigarette, soft smoke rising, soft ambient light with green and red neon reflections, melancholic expression, cinematic lighting with vintage colour gradation, inspired by Wong Kar-wai's style
```

### 1.2. Kling 2.0 I2V 合集（精选）

*来源：[MayorkingAI](https://x.com/MayorKingAI/status/1914431899675869327)*

```text
FPV chase cam shot closely tailing a wingsuit flyer diving between narrow cliffs. Arms stretched, wings rippling, sharp mountain edges blur below, crisp sky, sun flaring through peaks, fast shutter, thrilling, adrenaline
```

```text
Slow-motion cinematic tracking shot, a massive whale breaches the ocean surface, glowing from the golden sunset behind. Water cascades off its body, birds scatter mid-air, mountains silhouette in the background. Rippling reflections shimmer. Majestic, awe-inspiring
```

### 1.3. 仙宫云海 I2V（极简运镜）

```text
缓慢推进运镜，云雾轻流动，人物缓步，保持空间纵深与高级克制色调，电影质感，4K
```

### 1.4. I2V 细节强化模板

*来源：[@creatorslop](https://x.com/creatorslop/status/2085350375784378440)*

```text
Generate a video of [your scene] and include these details: the texture of every major surface, the direction and temperature of the light source, the speed of any movement in the frame, what the background is doing while the subject is in focus, and whether shadows are sharp or soft. Every element should feel chosen, not random.
```

---

## 2. Seedance 提示词（X 精选）

从 X 爬取的 **Seedance 2.0 / 2.5** 提示词（分镜结构可对照迁移到可灵）。完整包：[`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md)

### 2.1. Roswell 1947 档案片风（Seedance 2.5）

*来源：[@soumyattention](https://x.com/soumyattention/status/2085947512582721619)*

```text
[Generation Goal] Recovered-archival 1947 Roswell military documentation film (B&W 16mm grain, scratches, degraded mono audio). Stages: (0-8s) ridge handheld + soldiers order camera off; (8-15s) debris inspection + stretcher; (15-27s) tent gurney alien thrashing; (27-30s) film leader fail. Lock uniforms, alien identity, no modern objects.
```

完整多 Stage 正文见 [`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md)。

### 2.2. 精品咖啡机 UGC 广告 30s（Seedance 2.5）

*来源：[@SadiaMalik182](https://x.com/SadiaMalik182/status/2085947010293883115)*

```text
Create a 30-second vertical AI UGC product commercial (9:16) for a premium coffee machine.
Style: Ultra-realistic, cinematic UGC, 4K HDR, natural lighting, smooth handheld.
Scene 1 (0-5s) creator enters kitchen with mug: "I finally tried this coffee machine."
Scene 2 (5-10s) beans, water, power button close-ups.
Scene 3 (10-17s) grind, crema, pour, golden morning light.
Scene 4 (17-23s) first sip smile: "This honestly tastes amazing."
Scene 5 (23-27s) product orbit showcase.
Scene 6 (27-30s) hero product + cup, creator smiles to camera.
```

### 2.3. 早晨通勤 15 分镜（Seedance 2.5）

*来源：[@AIwithSynthia](https://x.com/AIwithSynthia/status/2085943905577734483)*

```text
SHOT 1 ECU phone alarm on sheets → SHOT 2 jolt awake → face wash → toothbrush → fridge POV grab → egg/toast pan → rushed bite → outfit change → shoes lace → corridor rush → metro doors → office badge → keyboard OTS → collapse on bed. Match cuts + SFX per shot.
```

### 2.4. 猫螺旋桨头盔一镜（Seedance 2.0）

*来源：[@saniaspeaks_](https://x.com/saniaspeaks_/status/2085932310923251950)*

```text
Single continuous shot: woman places spinning propeller fan helmet on silver tabby cat, rides scooter; cat lifts and flies beside scooter with dangling legs and flowing fur; handheld smartphone track; photoreal; no cuts.
Negative: cartoon, extra limbs, floating without propeller, text, watermark.
```

### 2.5. Visual Production Graph 工作流

*来源：[@HBCoop_](https://x.com/HBCoop_/status/2050246433480020154)*

用一张「视觉制作图」压缩角色+世界+空间+镜头序列，文本只写 timing / camera / shot order。详见 Seedance 完整包。

---

"""

SECS_EN = """## 1. Image-to-Video I2V (from X)

Kling **image-to-video** prompts crawled from public X posts. Full pack: [`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) · Log: [`docs/x-crawl-log.md`](./docs/x-crawl-log.md)

> **Newest first** in this section and repo-wide.

### 1.1. Kling 2.1 I2V Collection (highlights)

*Source: [MayorkingAI (@MayorKingAI)](https://x.com/MayorKingAI) — [Thread](https://x.com/MayorKingAI/status/1927126460352893348)*

```text
Tracking shot following a warrior woman riding a massive white wolf running at high speed across a frozen tundra, snow flying up from paws, wind whipping her cloak, cold blue tones, dramatic atmosphere, cinematic realism
```

```text
Aerial tracking shot of two cars drifting around a neon-lit Tokyo highway curve, tire smoke rising, reflections shimmering on wet asphalt. Electric atmosphere, dynamic, intense
```

```text
Slow zoom in on the face of a Korean Man in an elegant tailored suit, looking directly into the camera, centred composition, smoking a cigarette, soft smoke rising, soft ambient light with green and red neon reflections, melancholic expression, cinematic lighting with vintage colour gradation, inspired by Wong Kar-wai's style
```

### 1.2. Kling 2.0 I2V Collection (highlights)

*Source: [MayorkingAI](https://x.com/MayorKingAI/status/1914431899675869327)*

```text
FPV chase cam shot closely tailing a wingsuit flyer diving between narrow cliffs. Arms stretched, wings rippling, sharp mountain edges blur below, crisp sky, sun flaring through peaks, fast shutter, thrilling, adrenaline
```

```text
Slow-motion cinematic tracking shot, a massive whale breaches the ocean surface, glowing from the golden sunset behind. Water cascades off its body, birds scatter mid-air, mountains silhouette in the background. Rippling reflections shimmer. Majestic, awe-inspiring
```

### 1.3. Cloud palace I2V (minimal camera)

```text
Slow push-in, light cloud drift, figure walks slowly, preserve depth and restrained palette, cinematic, 4K
```

### 1.4. Detail-forcing I2V template

*Source: [@creatorslop](https://x.com/creatorslop/status/2085350375784378440)*

```text
Generate a video of [your scene] and include these details: the texture of every major surface, the direction and temperature of the light source, the speed of any movement in the frame, what the background is doing while the subject is in focus, and whether shadows are sharp or soft. Every element should feel chosen, not random.
```

---

## 2. Seedance Prompts (from X)

**Seedance 2.0 / 2.5** prompts crawled from X (shot structure ports well to Kling). Full pack: [`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md)

### 2.1. Roswell 1947 archival film (Seedance 2.5)

*Source: [@soumyattention](https://x.com/soumyattention/status/2085947512582721619)*

```text
[Generation Goal] Recovered-archival 1947 Roswell military documentation film (B&W 16mm grain, scratches, degraded mono audio). Stages: (0-8s) ridge handheld + soldiers order camera off; (8-15s) debris inspection + stretcher; (15-27s) tent gurney alien thrashing; (27-30s) film leader fail. Lock uniforms, alien identity, no modern objects.
```

### 2.2. Premium coffee machine UGC 30s (Seedance 2.5)

*Source: [@SadiaMalik182](https://x.com/SadiaMalik182/status/2085947010293883115)*

```text
Create a 30-second vertical AI UGC product commercial (9:16) for a premium coffee machine.
Style: Ultra-realistic, cinematic UGC, 4K HDR, natural lighting, smooth handheld.
Scene 1 (0-5s) creator enters kitchen with mug: "I finally tried this coffee machine."
Scene 2 (5-10s) beans, water, power button close-ups.
Scene 3 (10-17s) grind, crema, pour, golden morning light.
Scene 4 (17-23s) first sip smile: "This honestly tastes amazing."
Scene 5 (23-27s) product orbit showcase.
Scene 6 (27-30s) hero product + cup, creator smiles to camera.
```

### 2.3. Morning commute 15-shot table (Seedance 2.5)

*Source: [@AIwithSynthia](https://x.com/AIwithSynthia/status/2085943905577734483)*

```text
SHOT 1 ECU phone alarm on sheets → SHOT 2 jolt awake → face wash → toothbrush → fridge POV grab → egg/toast pan → rushed bite → outfit change → shoes lace → corridor rush → metro doors → office badge → keyboard OTS → collapse on bed. Match cuts + SFX per shot.
```

### 2.4. Cat propeller helmet one-take (Seedance 2.0)

*Source: [@saniaspeaks_](https://x.com/saniaspeaks_/status/2085932310923251950)*

```text
Single continuous shot: woman places spinning propeller fan helmet on silver tabby cat, rides scooter; cat lifts and flies beside scooter with dangling legs and flowing fur; handheld smartphone track; photoreal; no cuts.
Negative: cartoon, extra limbs, floating without propeller, text, watermark.
```

### 2.5. Visual Production Graph workflow

*Source: [@HBCoop_](https://x.com/HBCoop_/status/2050246433480020154)*

Compress character + world + layout + shot sequence into one control image; text only handles timing / camera / shot order. See full Seedance pack.

---

"""


def shift_sections(text: str, delta: int = 2, max_n: int = 13) -> str:
    for n in range(max_n, 0, -1):
        text = re.sub(rf"(## )\s*{n}\. ", rf"\1__OLD{n}__. ", text)
        text = re.sub(rf"(### )\s*{n}\.", rf"\1__OLD{n}__.", text)
    for n in range(1, max_n + 1):
        text = text.replace(f"__OLD{n}__", str(n + delta))
    return text


def replace_toc(text: str, toc: str, is_zh: bool) -> str:
    if is_zh:
        pat = r"## 📖 目录\n.*?\n---\n"
    else:
        pat = r"## 📖 Table of Contents\n.*?\n---\n"
    out, n = re.subn(pat, toc, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"TOC replace failed for {'zh' if is_zh else 'en'}: {n}")
    return out


def insert_after_toc(text: str, body: str, marker_prefix: str) -> str:
    # Find first ## N. after TOC that is the old section 1 shifted to 3
    m = re.search(rf"^## 3\. {re.escape(marker_prefix)}.+$", text, re.M)
    if not m:
        # list headers for debug
        headers = [l for l in text.splitlines() if l.startswith("## ")]
        raise SystemExit(f"marker not found for {marker_prefix!r}: {headers[:12]}")
    idx = m.start()
    return text[:idx] + body + text[idx:]


def add_resource_links(text: str, is_zh: bool) -> str:
    if is_zh:
        needle = "- 本仓库：[`prompts/t2i-fashion-portraits.md`](./prompts/t2i-fashion-portraits.md) — T2I 时尚肖像"
        add = (
            needle
            + "\n- 本仓库：[`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) — X 爬取 I2V"
            + "\n- 本仓库：[`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md) — X 爬取 Seedance"
            + "\n- 本仓库：[`docs/x-crawl-log.md`](./docs/x-crawl-log.md) — 爬取日志"
        )
    else:
        needle = "- In-repo: [`prompts/t2i-fashion-portraits.md`](./prompts/t2i-fashion-portraits.md) — T2I fashion portraits"
        add = (
            needle
            + "\n- In-repo: [`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) — I2V from X"
            + "\n- In-repo: [`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md) — Seedance from X"
            + "\n- In-repo: [`docs/x-crawl-log.md`](./docs/x-crawl-log.md) — crawl log"
        )
    if "i2v-from-x.md" in text:
        return text
    if needle not in text:
        raise SystemExit("resource needle not found")
    return text.replace(needle, add, 1)


def bump_intro(text: str, is_zh: bool) -> str:
    if is_zh:
        old = "本仓库专注于**高保真 Kling 提示词**：T2I 肖像、电影感、广告、UGC、动漫、短剧、特效"
        new = "本仓库专注于**高保真 Kling 提示词**：I2V / Seedance（X 精选）、T2I 肖像、电影感、广告、UGC、动漫、短剧、特效"
    else:
        old = "This repository focuses on **high-fidelity Kling prompts** for T2I portraits, cinematic film"
        new = "This repository focuses on **high-fidelity Kling prompts** for I2V & Seedance (from X), T2I portraits, cinematic film"
    return text.replace(old, new, 1)


def main() -> None:
    zh_path = ROOT / "README.md"
    en_path = ROOT / "README-en.md"

    zh = zh_path.read_text(encoding="utf-8")
    zh = shift_sections(zh, delta=2, max_n=13)
    zh = replace_toc(zh, TOC_ZH, is_zh=True)
    zh = insert_after_toc(zh, SECS_ZH, "文生图")
    zh = add_resource_links(zh, is_zh=True)
    zh = bump_intro(zh, is_zh=True)
    zh_path.write_text(zh, encoding="utf-8", newline="\n")

    en = en_path.read_text(encoding="utf-8")
    en = shift_sections(en, delta=2, max_n=13)
    en = replace_toc(en, TOC_EN, is_zh=False)
    en = insert_after_toc(en, SECS_EN, "Text-to-Image")
    en = add_resource_links(en, is_zh=False)
    en = bump_intro(en, is_zh=False)
    en_path.write_text(en, encoding="utf-8", newline="\n")

    for p in (zh_path, en_path):
        print("===", p.name)
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                print(line)


if __name__ == "__main__":
    main()
