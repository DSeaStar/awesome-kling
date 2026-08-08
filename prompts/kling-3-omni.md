# Kling 3.0 / Omni — 专区

> 面向 **Kling 3.0、Kling 3.0 Pro、Kling VIDEO 3.0 Omni** 的分镜、原生音频、多参考与运镜提示词。  
> **排序：** 最新收录在前。部分来自 X 公开帖与官方结构整理。

官方入口：
- [Kling VIDEO 3.0 Omni User Guide](https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide)
- [Kling AI Prompt Guide](https://kling.ai/blog/kling-ai-prompt-guide)
- 社区汇总的可灵 3.0 Omni 手册（第三方）：https://docs.qingque.cn/d/home/eZQDPQ5RCKYKpTbz1poE88YSp

---

## 1. 深夜排练室 vlog（原生对白 · 多机位自拍感）

*Source: [Alpha Mom (@YourAlphaMom)](https://x.com/YourAlphaMom) — [Post](https://x.com/YourAlphaMom/status/2085350644915765377)（同 prompt 横评含 Kling 3.0 Pro）· 2026-08-06*

```text
CAMERA:
DV 16mm tape camcorder handheld aesthetic. POV of a beautiful influencer-style woman filming herself directly by hand. Keep natural hand shake, slightly crooked framing, delayed focus pulls, awkward zooms, occasional moments where her face is partly cut off, and imperfect framing that briefly loses the subject. Every shot is filmed by the woman herself in selfie-cam or first-person style, except for one brief moment when she props the camera down. The camcorder itself never appears on screen.

LOOK:
Soft digital tape look with a subtle vintage camcorder feel. Slight blur, faint tape noise, softly blooming highlights in dim light, mild flicker in auto-exposure, low contrast, realistic skin tones.

STYLE:
Late-night post-practice vlog mood — tired, calm, a little out of breath, but clearly happy and satisfied. Quiet, natural, unposed energy. Handheld all the way through, slower and more intimate than a daytime gym vlog. Occasional heavy breathing between lines.

CHARACTER:
A beautiful Instagram-style brunette model in her 20s. Long dark brown hair tied back or slightly messy after rehearsal, attractive feminine features, glowing skin with a light sweat sheen, expressive eyes, slim fit build. Wearing a modest fitted long-sleeve athletic top, loose joggers or sweatpants, and sneakers. No jewelry.

SETTING:
An empty dance rehearsal studio late at night. Mirror wall on one side, wooden floor, a speaker in the corner, a towel and water bottle near the wall, dim overhead lighting, dark hallway visible outside the studio windows.

STORYBOARD:
(~2s, propped camera near the mirror, medium shot) She walks into frame catching her breath, wipes sweat from her forehead, gives a small exhausted smile. "Finally done… it's way too late."
(~2s, handheld, slow drift across the room and back to her) The camera loosely pans over the empty mirrors and quiet studio, then returns to her face. (softly, off-screen): "Whole studio's empty now."
(~2s, medium handheld near the wall) She grabs her water bottle, takes a long drink, lowers it, and exhales in relief. "I really needed that."
(~2s, propped camera facing the mirror, wider shot) She sets the camera down, steps back, does a short sharp dance combo, then laughs at herself when she finishes.
(~2s, arm's-length selfie close-up finish) She picks the camera back up, towel over her shoulder, cheeks flushed, still breathing a little heavy. She gives a small tired wave and a genuine smile. "Okay, I'm going home. Good night."
```

**Kling 3.0 调参提示：** 若口型与喝水冲突，拆成「只喝水无对白」+「只对白无瓶口」两段再剪；Omni 优先写清 **CAMERA / CHARACTER / STORYBOARD** 分块。

---

## 2. 健身结束日记（角色锁定 · 对白）

*Source: 同作者 Seedance 对照帖结构，可直接试 Kling 3.0 Omni — 结构参考 [status/2085035378151510274](https://x.com/YourAlphaMom/status/2085035378151510274)*

```text
CAMERA: Handheld DV 16mm vlog. Subject films herself at arm's length; occasional prop on bench/mat. Subtle hand movement, autofocus hunting, rushed reframing. Camera body never visible.

LOOK: Warm analog grain, soft halos on overhead lights, realistic skin.

STYLE: Intimate end-of-workout diary, mostly empty gym, casual unpolished humor.

CHARACTER: CHASE — fitness creator mid-20s, long wavy chestnut ponytail, slim athletic, fitted long-sleeve top, high-waisted leggings, white socks, sneakers, towel on shoulders.

SETTING: Boutique gym late evening — mats, mirrors, dumbbell racks, bag + protein shake.

SCENES (with dialogue):
- Drops onto mat, breath: "Okay… that session is officially over."
- Forward stretch, smile: "I definitely pushed that last set too far."
- Shoulder roll: "Tomorrow is going to be interesting."
- Sip shake, surprised: "Wait… this one is actually good."
- Overhead stretch: "I'd call today a solid eight and a half."
- Wave exit: "I'm calling it. See you at the next workout."
```

---

## 3. 美食俯拍 B-roll（一镜 · 3.0）

*Source: [@emberbuild](https://x.com/emberbuild/status/2085252050053435406) · Kling 3.0 · 2026-08-06*

```text
Overhead food B-roll, Kling 3.0, single continuous shot.
Batter hits a hot pan; edges crisp and bubble; steam rises in morning window light.
Slow subtle camera drift, shallow depth of field on the sizzle, natural sound of oil, photoreal, recipe-app ready, no text, no hands morphing.
```

---

## 4. Omni 多模态分块模板（推荐默认）

```text
[MODE] Kling 3.0 Omni · multi-shot · native audio on

[SUBJECT]
Who / wardrobe / identity lock notes (Elements refs if any)

[ACTION]
Primary verbs only — one main motion per shot

[SETTING]
Place, time of day, weather, key props

[CAMERA]
Shot size · angle · move · lens feel

[AUDIO]
Dialogue lines in quotes · SFX · ambience language

[TIMELINE]
[0-3s] Shot 1 — …
[3-7s] Shot 2 — …
[7-12s] Shot 3 — …

[QUALITY]
photoreal / film grain / 4K · stable identity · natural motion
```

---

## 5. 多参考一致性（Elements / 多图）

```text
Use element references: character @img1, product @img2, location @img3.
Keep face, outfit, and product packaging identical across all shots.
[0-4s] Wide establish in location.
[4-8s] Medium: character interacts with product.
[8-12s] Hero product close-up + soft smile to camera.
Native ambient room tone, optional short line: "Try this."
```

---

## 6. Motion Control 迁移（3.0）

```text
Motion reference: @video_motion (body timing + camera energy only).
Identity reference: @image_character (face, hair, clothes).
Retarget motion to identity. No limb break, no identity bleed from motion clip.
Cinematic key light, photoreal, 5–10s.
```

---

## 7. 官方向：镜头语言速查（3.0）

| 意图 | 英文短语 | 中文短语 |
|------|----------|----------|
| 建立空间 | extreme wide establishing | 极远景建立 |
| 情绪 | extreme close-up, shallow DOF | 极特写，浅景深 |
| 能量 | handheld tracking, whip pan | 手持跟拍，甩镜 |
| 质感广告 | slow dolly, product orbit | 慢推，产品环绕 |
| 一镜 vlog | arm's-length selfie POV | 手臂长度自拍 POV |

详见：[`prompt-formula.md`](./prompt-formula.md) · 负向：[`negative-prompts.md`](./negative-prompts.md)
