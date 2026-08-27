Last updated on 2026-08-27 21-23-49

# Awesome Kling AI 🎬

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE) [![GitHub stars](https://img.shields.io/github/stars/DSeaStar/awesome-kling?style=social)](https://github.com/DSeaStar/awesome-kling/stargazers)

| [简体中文](./README.md) | [English](./README-en.md) |

> **可灵 Kling AI / Kling 3.0** 优质提示词、**文生图（T2I）** 时尚肖像、视频生成技巧、运动控制工作流与开发者资源的精选集合（快手可灵）。

本仓库专注于**高保真 Kling 提示词**：Kling 3.0 / Omni、I2V / Seedance（X 精选）、T2I 肖像、电影感、广告、UGC、动漫、短剧、特效，以及 **API / SDK / 生产工作流**，帮助你把可灵真正用到产品和内容流水线里。

结构与风格参考 [awesome-seedance](https://github.com/ZeroLu/awesome-seedance)（**sibling 互链**）。欢迎阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [周更日志](./docs/x-crawl-log.md)。

---

## 📖 目录

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

## 1. Kling 3.0 / Omni 专区

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

## 2. 图生视频 I2V（X 精选）

从 X 爬取的 **Kling 图生视频** 提示词（需上传参考静帧）。完整合集：[`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) · 日志：[`docs/x-crawl-log.md`](./docs/x-crawl-log.md) · **每周一自动爬取候选**

> 本节遵循：**新提示词永远放在最前面**。

### 2.1. Kling 2.1 I2V 合集（精选）

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

### 2.2. Kling 2.0 I2V 合集（精选）

*来源：[MayorkingAI](https://x.com/MayorKingAI/status/1914431899675869327)*

```text
FPV chase cam shot closely tailing a wingsuit flyer diving between narrow cliffs. Arms stretched, wings rippling, sharp mountain edges blur below, crisp sky, sun flaring through peaks, fast shutter, thrilling, adrenaline
```

```text
Slow-motion cinematic tracking shot, a massive whale breaches the ocean surface, glowing from the golden sunset behind. Water cascades off its body, birds scatter mid-air, mountains silhouette in the background. Rippling reflections shimmer. Majestic, awe-inspiring
```

### 2.3. 仙宫云海 I2V（极简运镜）

```text
缓慢推进运镜，云雾轻流动，人物缓步，保持空间纵深与高级克制色调，电影质感，4K
```

### 2.4. I2V 细节强化模板

*来源：[@creatorslop](https://x.com/creatorslop/status/2085350375784378440)*

```text
Generate a video of [your scene] and include these details: the texture of every major surface, the direction and temperature of the light source, the speed of any movement in the frame, what the background is doing while the subject is in focus, and whether shadows are sharp or soft. Every element should feel chosen, not random.
```

---

## 3. Seedance 提示词（X 精选）

从 X 爬取的 **Seedance 2.0 / 2.5** 提示词（分镜结构可对照迁移到可灵）。完整包：[`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md)

### 3.1. Roswell 1947 档案片风（Seedance 2.5）

*来源：[@soumyattention](https://x.com/soumyattention/status/2085947512582721619)*

```text
[Generation Goal] Recovered-archival 1947 Roswell military documentation film (B&W 16mm grain, scratches, degraded mono audio). Stages: (0-8s) ridge handheld + soldiers order camera off; (8-15s) debris inspection + stretcher; (15-27s) tent gurney alien thrashing; (27-30s) film leader fail. Lock uniforms, alien identity, no modern objects.
```

完整多 Stage 正文见 [`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md)。

### 3.2. 精品咖啡机 UGC 广告 30s（Seedance 2.5）

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

### 3.3. 早晨通勤 15 分镜（Seedance 2.5）

*来源：[@AIwithSynthia](https://x.com/AIwithSynthia/status/2085943905577734483)*

```text
SHOT 1 ECU phone alarm on sheets → SHOT 2 jolt awake → face wash → toothbrush → fridge POV grab → egg/toast pan → rushed bite → outfit change → shoes lace → corridor rush → metro doors → office badge → keyboard OTS → collapse on bed. Match cuts + SFX per shot.
```

### 3.4. 猫螺旋桨头盔一镜（Seedance 2.0）

*来源：[@saniaspeaks_](https://x.com/saniaspeaks_/status/2085932310923251950)*

```text
Single continuous shot: woman places spinning propeller fan helmet on silver tabby cat, rides scooter; cat lifts and flies beside scooter with dangling legs and flowing fur; handheld smartphone track; photoreal; no cuts.
Negative: cartoon, extra limbs, floating without propeller, text, watermark.
```

### 3.5. Visual Production Graph 工作流

*来源：[@HBCoop_](https://x.com/HBCoop_/status/2050246433480020154)*

用一张「视觉制作图」压缩角色+世界+空间+镜头序列，文本只写 timing / camera / shot order。详见 Seedance 完整包。

---

## 4. 文生图（T2I）

可灵生图 / Kling Image 提示词。完整多语言包见 [`prompts/`](./prompts/)。

> 本节（及全库各分类）遵循：**新提示词永远放在最前面**。

### 4.1. 青空を踏む白 / 踏蓝天的白

*极端低角度盛夏十字路口时尚肖像——纯白装束、鲜烈蓝天、广角腿部前景。画幅 **3:4**。*

![踏蓝天的白](./assets/t2i-aozora-wo-fumu-shiro.jpg)

**提示词（中文结构版）：**
```text
主题：踏蓝天的白

主体：盛夏的城市十字路口，20多岁的女性在路面积水边缘的相机前单膝跪地，对侧膝盖高高抬起，摆出纵向构图的实拍时尚肖像。纯白装束、鲜烈的蓝天、近景中大幅逼近的腿部与凉鞋。

人物・表情：脸庞微微侧倾，平静目光俯视低位相机。柔和轮廓、细长棕色眼眸、自然泪袋、明亮棕色眉毛、整齐鼻梁、珊瑚粉唇。浅粉米色眼妆与淡雅腮红，日系精致自然妆。肩下中长亮棕发、薄透视刘海、脸周层次、发梢随风轻摆。

服装・姿势：白色细肩带罗纹裁剪吊带背心（胸口与肩带蕾丝镶边）；白色高腰裹式迷你裙（一侧褶皱与细抽绳）；白色厚底系带凉鞋。右膝（画面左）贴地，左膝（画面右）高抬向前突出。左手轻置于抬起左膝上，右手自然垂向路面。

背景・光线：日本都市宽阔十字路口；中层办公/商业楼、街树、电线杆、变压器、错综电线、人行横道、远处渺小行人；上部大面积鲜艳蓝天与立体白云。强烈夏日高位阳光，白衣与肌肤明亮，柏油路轮廓分明的阴影。

构图・相机：纵向3:4。相机降至柏油路高度的极端低角度广角近拍。人物居中大幅呈现；头在上部中央；抬起左腿与白凉鞋大幅逼近右下前景。广角远近感强调前景腿脚；建筑与电线向天空收束。面部与前景腿锐利，远景略柔。

质感・风格：高精度实拍。自然肌理与适度光泽；罗纹、蕾丝、褶皱、凉鞋系带、粗糙柏油清晰。蓝白主调，保留肌肤暖色。避免过度美肌与夸张HDR。
```

**负面提示：**
```text
左右翻转；抬起左膝与左手的接触不可脱离；脚趾或凉鞋系带的变形
```

**完整包（日文 / 中文 / 英文 + I2V 续写）：**  
[`prompts/t2i-fashion-portraits.md`](./prompts/t2i-fashion-portraits.md)

---

## 5. 提示词公式（从这里开始）

Kling 3.0 更吃**分镜式导演语言**，而不是关键词堆砌。完整说明见：[`prompts/prompt-formula.md`](./prompts/prompt-formula.md)。

### 核心模板

```text
[主体], [动作], 场景在 [环境]。
镜头：[景别], [运镜], [焦距/景深]。
光影：[主光], [氛围]。
风格：[电影参考], 写实, 高细节, 4K。
音频（可选）：[对白 / 音效 / 环境音]。
```

### 多镜头模板（Kling 3.0 强项）

```text
时长：10 秒。多镜头叙事。服装与天气全程一致。

[0-3s] 镜头 1 — 极远景建立：
...

[3-7s] 镜头 2 — 中景跟拍：
...

[7-10s] 镜头 3 — 极特写：
...
```

### 图生视频模板

```text
根据参考图中的主体进行动画。
动作：[具体动作]。
运镜：[推进 / 横移 / 环绕 / 固定]。
保持人脸身份、服装与构图一致。
自然运动模糊，真实物理，写实质感。
```

商用玩法合集：[`prompts/commercial-use-cases.md`](./prompts/commercial-use-cases.md)

---

## 6. 电影风格

面向 **Kling 3.0** 多镜头与原生音频优化的专业电影提示词。

### 6.1. 好莱坞夜雨赛车

**提示词：**
```text
风格：好莱坞专业赛车电影，电影感夜雨，高风险竞技。
时长：12 秒。多镜头。

[0-4s] 镜头 1 — 车内特写：老将戴头盔，雨水拍打挡风玻璃，仪表灯映在面罩，冷静点头，口型 "出发吧"。
[4-8s] 镜头 2 — 对手驾驶舱：年轻车手紧握方向盘，呼吸沉重，低语 "专注"。
[8-12s] 镜头 3 — 远景动作：绿灯亮起，两车在湿沥青上同步加速，水花溅镜头，体育场灯光拖成光轨。

写实，IMAX 感，人脸稳定，雨水物理真实，4K。
```

### 6.2. 维伦纽瓦式沙漠逃离

**提示词：**
```text
风格：IMAX 70mm，丹尼斯·维伦纽瓦，颗粒写实，低饱和，史诗规模。
时长：12 秒。

[0-4s] 极远景：数英里高沙尘暴吞没沙漠，小队装甲车狂奔逃离。
[4-8s] 驾驶舱：驾驶员尖叫 "走！快走！"，镜头剧烈晃动，沙打挡风玻璃，太阳被尘墙吞没。
[8-12s] 高潮：越野车冲上沙丘腾空慢动作，风暴剪影，尘云闪电，碎片掠镜头，切黑。

写实，灾难级规模，载具几何稳定。
```

### 6.3. 王家卫雨夜电话亭

**提示词：**
```text
电影风格：90 年代香港艺术电影，复古胶片颗粒，高 ISO，琥珀-绿色调，忧郁。

核心情感对白："如果记忆是一个罐头，我希望它永远不会过期。"
时长：10 秒。

[0-4s] 透过布满雨水的红色电话亭玻璃；风衣人紧握听筒，眼神空洞却深情；雨水扭曲面部如油画。
[4-7s] 唇部与半脸极特写；对着听筒轻声耳语；霓虹虚化光点流过皮肤。
[7-10s] 挂断电话走入雨中人群；背影抽帧拖影；城市车灯光轨。

手持，浅景深，情感浓烈，胶片写实。
```

### 6.4. 霓虹东京雨夜序列

**提示词：**
```text
[0-4s] 远景固定：霓虹东京小巷夜雨，湿沥青倒影，远处车流低语。
[4-8s] 中景慢推：黑风衣人撑红纸伞走向镜头，霓虹在脸上闪烁。
[8-12s] 跟拍特写：伞落下，雨打脸，抬头；雨声增强。
[12-15s] 极特写：雨点落入霓虹水洼慢动作，彩色涟漪，低音淡出至静。

写实，《银翼杀手 2049》光影，罗杰·迪金斯式布光。
```

### 6.5. 日落武士（时间码）

**提示词：**
```text
[0-4s] 仰角远景固定：孤独武士剪影立于血色日落山脊，长草被风吹弯，远雷。
[4-8s] 人脸推拉变焦（眩晕效果），背景拉伸，鼓点升起。
[8-12s] 急摇接升起摇臂：山谷千点火炬大军推进，号角与烟尘。
[12-15s] 极特写：手握刀柄指节发白，一滴汗慢动作，拔刀声后死寂。

写实，黑泽明摄影语言，8K 质感。
```

### 6.6. 爵士钢琴家（原生音频）

**提示词：**
```text
烟雾夜店中，爵士钢琴家双手在三角钢琴上飞舞的特写。每个琴键激起温暖琥珀色光纹。镜头缓缓拉远，露出低音提琴、刷子鼓、次中音萨克斯。乐手互视点头交换 solo。一束追光里烟雾卷曲。

写实，私密爵士吧氛围，4K。
音频：清晰钢琴起音、行走贝斯、刷军鼓、气声萨克斯、空间混响。
```

---

## 7. 广告与商业品牌

用 **Kling AI** 做产品展示、品牌片与高端广告。

### 7.1. 奢侈香水广告（时间码）

**提示词：**
```text
(0-3s)  macro：奢侈香水瓶与粉色牡丹，浅景深，暖午后光，花瓣漂浮，轻柔环境乐。
(3-7s) 镜头滑近；女性手从右侧入画轻触瓶身；丝绸摩擦声。
(7-12s) 慢动作喷雾：金色雾气，暗背景轮廓光，雾化器嘶声。
(12-15s) 拉出英雄定格，产品居中，体积光，奶油色极简背景，优雅静音。

写实时尚广告，产品几何稳定。
```

### 7.2. 运动饮料广告

**提示词：**
```text
为参考图中的运动饮料生成 12 秒高端广告。
[0-3s] 微距：冰珠沿瓶身滑落，侧逆光，浅景深。
[3-7s] 运动员拧开痛饮，慢动作水花，城市跑道虚化。
[7-10s] 快剪：冲刺、击掌、瓶身旋转 hero shot。
[10-12s] 产品定格，干净背景，预留 slogan 空间。

节奏明快，商业调色，4K，瓶身一致。
```

### 7.3. 极简品牌生活方式片

**提示词：**
```text
为极简家居品牌生成 15 秒生活方式宣传片。
自然室内日光，真实人物，无重滤镜。
产品自然出现在生活场景，不做硬广贴片。
运镜：缓慢推近 + 空镜过渡。
北欧/日系极简美学，平静旁白留白，柔和环境音。
```

### 7.4. 无人机广告复刻（产品替换）

**提示词：**
```text
模仿参考视频 @video1 的分镜与剪辑节奏。
将所有产品替换为参考图 @image1 中的无人机。
多角度展示机身、螺旋桨与飞行瞬间。
主色蓝黑。旁白与音乐改为介绍无人机性能。
全片产品身份保持一致。
```

更多商用玩法：[`prompts/commercial-use-cases.md`](./prompts/commercial-use-cases.md)

---

## 8. 社交媒体与病毒模因

短视频平台的注意力优先与 meme 向提示词。

### 8.1. 巨型橘猫城市 meme

**提示词：**
```text
风格：伪纪录片手机 vlog，超写实 CG + 真实城市，8K 毛发物理。
时长：15 秒。优先竖屏 9:16。

[0-5s] 繁忙街景，镜头上抬：哥斯拉级橘猫卡在两栋楼之间，可怜挥爪，巨型肉垫压弯玻璃幕墙。
[5-10s] 地面视角：车流中橘猫凑近嗅公交车，司机冷静摸它鼻子，它打喷嚏吹飞帽子树叶。
[10-15s] 挤出楼缝坐上跨江桥导致桥面微沉，懒洋洋舔毛堵住晚高峰；定格无辜大眼。

喜剧向，写实物理，巨型尺度光影成立。
```

### 8.2. 街头抬杠（强调口型）

**提示词：**
```text
雨中街角中景：两个怪人激烈争论。
风衣人大动作比划："这可不是普通椒盐卷饼——是酸面团椒盐卷饼！"
牛仔夹克回："谁在乎，卷饼就是卷饼！"
口型清晰，自然雨声，meme 构图，写实。
```

### 8.3. 一镜到底竖屏钩子

**提示词：**
```text
竖屏 9:16，8 秒，一镜到底。
创作者在凌乱卧室对镜头说话，说到一半突然僵住，眼睛瞪大，慢慢转向画外撞击声，然后冲出画面。
手机手持质感，自然噪声，最后一拍才出现卡点音。
```

---

## 9. UGC 风格

用户生成内容美学——手机摄影感 + 可控超现实。

### 9.1. 浴室镜子故障 vlog

**提示词：**
```text
风格：伪纪录片 vlog，超写实，固定机位实拍感，自然浴室光，轻度悬疑喜剧。
时长：15 秒。

[0-6s] 女生在浴室镜前刷牙做鬼脸，镜中倒影完全同步正常。
[6-11s] 吐掉泡沫转身离开；镜中倒影不动，坏笑挑眉停 2 秒，再慌张快进追上后消失。
[11-15s] 她在门口察觉不对回头；镜子已正常空镜；困惑看向镜头；定格。

必须像倒影「网络延迟」，写实，无血腥恐怖。
```

### 9.2. 产品开箱 UGC

**提示词：**
```text
手机自拍角度，略乱桌面，自然窗光。
创作者拆快递，真实惊喜反应，把产品凑近镜头旋转，边说边指 2 个卖点。
口语："等等——这包装也太夸张了吧。"
UGC 真实感，轻微手持晃动，真实肤质，9:16。
```

### 9.3. 参考角色念指定音频

**提示词：**
```text
把 [Image2] 的人物放入 [Image1] 的室内，保持 [Image2] 的造型风格与 [Image1] 的写实感。
人物说出 [Audio1] 的台词，口型清晰。
自然室内光，身份稳定，轻微头部动作，写实。
```

---

## 10. 动漫与动画风格

角色动作、风格一致性与动态运动测试。

### 10.1. 武道大会对决

**提示词：**
```text
Figure 1 与 Figure 2 在世界武道大会擂台对决。
动态动漫运镜，速度线，打击定格，尘土碎石。
两名角色造型与输入图一致。
在远景对撞、表情特写与最终一击之间快切。
```

### 10.2. 水獭机甲动漫战

**提示词：**
```text
动漫段落：水獭进入大型机甲，快速切换齿轮零件咬合特写。
水獭冷酷竖拇指，驾驶机甲起飞与大理石章鱼作战。
动态镜头，赛璐璐高光，动作有力，机甲设计连贯。
```

### 10.3. 梵高活油画

**提示词：**
```text
风格：梵高后印象派油画，厚涂，漩涡笔触，高饱和蓝黄对比。
时长：12 秒动画。

夜空中巨大黄色天体，星云如河流旋转。
前景柏树如黑色火焰扭曲；山谷小镇窗户暖黄光。
整个世界沿笔触方向缓慢流动呼吸。

绘画运动，非写实人脸，梦幻氛围。
```

### 10.4. 风格板动态图形

**提示词：**
```text
受传统动画技法启发，创作 motion graphics 动画。
根据参考图中的三组风格样例，输出短动画序列，保留经典动画节奏与现代流畅度。
造型大胆，时间点干脆，转场利落。
```

---

## 11. 短剧与网剧

竖屏情绪钩子与爽剧结构。

### 11.1. 雨夜情感短剧

**提示词：**
```text
风格：热门中文微短剧，极速剪辑，高吸引力滤镜，虐恋雨夜。
时长：15 秒。竖屏 9:16。

角色：深情霸总男主（黑风衣、湿发、红眼眶）vs 决绝女主（白裙、泪脸）。

[0-5s] 女主转身离开；男主抓住手腕；她回眸爱恨交织。口型："放开！我们结束了！"
[5-10s] 雨水顺脸流下；他掏出戒指/文件高举，手指颤抖。口型："你看清楚！我从没骗过你！"
[10-15s] 女主瞳孔震动捂嘴；男主猛然抱紧；镜头环绕。低声啜泣。

电影感雨戏，人脸稳定，口型清晰。
```

### 11.2. 竖屏霸总反转

**提示词：**
```text
风格：竖屏爽剧霸总，高饱和，极致面部特写。
时长：15 秒。

[0-5s] 婚礼现场：岳母把离婚协议砸到新郎胸口，宾客哄笑，指戳额头。口型："没车没房还想娶我女儿？拿着这点钱滚！"
[5-10s] 新郎冷笑撕纸；直升机轰鸣；风吹乱岳母发型；气场瞬间翻盘。口型："这门亲事，只有我说了算。"
[10-15s] 大门被踹开，保镖铺红毯；管家鞠躬递上黑卡。口型："少爷，资产已解冻，欢迎回家！"

戏剧光影，情绪节拍清楚，写实。
```

### 11.3. 10 秒舞台小品

**提示词：**
```text
10 秒综艺舞台小品：两位古装角色坐在现代脱口秀沙发上，背后新年红金 LED。
肩上视角快速喜剧切镜，夸张白眼，一只现代蓝牙耳机反差梗。
观众笑声灯光脉冲，撒金箔收尾，16:9 舞台镜头语言。
```

---

## 12. 视觉特效与实验风格

奇观、物理与超现实概念。

### 12.1. 天空拉链超现实

**提示词：**
```text
风格：超现实主义，巨物恐惧，好莱坞特效质感，极致写实光影。
时长：15 秒。

[0-5s] 晴朗城市蓝天，镜头上仰，地平线出现巨型金属拉链。
[5-10s] 半透明巨神之手拉开拉链，蓝天如布剥落，背后是霓虹赛博朋克飞车巨构世界。
[10-15s] 镜头急拉：整座城市其实是巨人桌上的玻璃微缩球，巨人俯身观察。

写实 VFX，尺度过渡成立。
```

### 12.2. 轨道空间站碰撞

**提示词：**
```text
两座巨型空间站在近地轨道灾难性碰撞。
金属慢动作撕裂；碎片螺旋；舱段压扁；大气在真空中结晶喷射。
镜头在残骸中翻滚，一名 EVA 宇航员失控飞过。
地球在背景中宁静巨大。

写实，轨道碎片逻辑，《地心引力》能量，8K 感。
```

### 12.3. 简单图生视频物理

**提示词：**
```text
以可信物理动画这张图。
先环境微动（风、布料、粒子），再主体主动作。
保持构图与身份。自然运动模糊。写实。
```

### 12.4. 多图流体变形

**提示词：**
```text
在所有参考照片之间创建流体变形。
身份过渡无硬切，镜头能量连续，梦幻但有结构。
```

---

## 13. 运动控制与角色一致性

可灵强项：**运动控制（Motion Control）**、**主体/Elements 绑定**、多图参考与身份锁定。

### 13.1. 运动控制重定向

**提示词：**
```text
使用参考视频的肢体动态、节奏与镜头能量。
将该运动迁移到参考图中的角色上。
保留参考图身份、面部与服装；忽略运动视频中的人物身份。
重定向平滑，无肢体崩坏，电影光影，写实。
```

### 13.2. 角色系列一致性

**提示词：**
```text
所有镜头保持 Elements/参考图中的同一角色身份。
镜头 A：教室窗边独白。
镜头 B：走廊追逐，手持紧迫感。
镜头 C：天台黄昏对峙。
同一服装、同一五官，年龄发型连贯。
按参考指定为动漫电影感或写实。
```

### 13.3. Elements 时尚 Lookbook

**提示词：**
```text
全程同一模特身份。
三套服装按参考图顺序卡点切换。
每套：中景走位 + 全身英雄姿势 + 面料细节特写。
干净影棚，柔和时尚光，竖屏 9:16。
```

### 13.4. 多参考拼场景

**提示词：**
```text
组合参考：角色来自 @image1，场景来自 @image2，产品来自 @image3。
角色走过场景，自然与产品互动，看向镜头微微一笑。
多主体稳定一致，写实，轻缓斯坦尼康跟随。
```

---

## 14. 资源

### 官方

- [Kling AI 国际站](https://kling.ai/) — 官方产品
- [可灵 AI（快手）](https://klingai.kuaishou.com/) — 国内入口
- [Kling VIDEO 3.0 使用指南](https://kling.ai/quickstart/klingai-video-3-model-user-guide) — 原生音频、多镜头、15 秒、AI Director
- [Kling VIDEO 3.0 Omni 使用指南](https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide) — 多模态、多镜头、原生音频
- [Kling VIDEO 3.0 运动控制指南](https://kling.ai/quickstart/motion-control-user-guide) — 参考视频驱动、面部绑定、朝向模式
- [Kling 官方提示词指南](https://kling.ai/blog/kling-ai-prompt-guide) — 镜头、光影、对白、多镜头
- [可灵开放平台 API 概览](https://kling.ai/document-api/quickStart/productIntroduction/overview) — 官方 API
- [文生视频 API（3.0 Omni）](https://kling.ai/document-api/api/video/3-0-omni/text-to-video) — T2V 文档
- [图生视频 API（3.0 Omni）](https://kling.ai/document-api/api/video/3-0-omni/image-to-video) — I2V 文档
- [运动控制 API](https://kling.ai/document-api/api/video/motion-control) — 官方动作迁移接口

### 提示词指南

- [Kling 3.0 Prompting Guide（fal.ai）](https://blog.fal.ai/kling-3-0-prompting-guide/) — 电影意图与结构
- [How to Use Kling 3.0 Pro in 2026（fal）](https://fal.ai/learn/tools/how-to-use-kling-3-0-pro) — 多镜头、运镜、Elements、定价
- [Kling 3.0 Prompt Guide（Atlabs）](https://www.atlabs.ai/blog/kling-3-0-prompting-guide-master-ai-video-generation) — 分层公式
- 本仓库：[`prompts/prompt-formula.md`](./prompts/prompt-formula.md)
- 本仓库：[`prompts/commercial-use-cases.md`](./prompts/commercial-use-cases.md)
- 本仓库：[`prompts/t2i-fashion-portraits.md`](./prompts/t2i-fashion-portraits.md) — T2I 时尚肖像
- 本仓库：[`prompts/i2v-from-x.md`](./prompts/i2v-from-x.md) — X 爬取 I2V
- 本仓库：[`prompts/seedance-from-x.md`](./prompts/seedance-from-x.md) — X 爬取 Seedance
- 本仓库：[`docs/x-crawl-log.md`](./docs/x-crawl-log.md) — 爬取日志（**每周一自动**）
- 本仓库：[`scripts/weekly_x_crawl.py`](./scripts/weekly_x_crawl.py) — 周更爬取脚本
- 候选目录：[`docs/x-crawl-candidates/`](./docs/x-crawl-candidates/) — 自动 PR，审核后晋升

### API、SDK 与工具

| 项目 | 说明 |
|------|------|
| [KlingAIResearch/ComfyUI-KLingAI-API](https://github.com/KlingAIResearch/ComfyUI-KLingAI-API) | ComfyUI 可灵 API 节点 |
| [199-mcp/mcp-kling](https://github.com/199-mcp/mcp-kling) | Kling 视频生成 MCP Server |
| [vargHQ/sdk](https://github.com/vargHQ/sdk) | JSX 视频 SDK，统一调用 Kling 等 |
| [vericontext/vibeframe](https://github.com/vericontext/vibeframe) | Agent 用视频生成 CLI + MCP（成本上限） |
| [gokayfem/ComfyUI-fal-API](https://github.com/gokayfem/ComfyUI-fal-API) | fal.ai ComfyUI 节点（含 Kling） |
| [ai-sdk Kling provider](https://ai-sdk.dev/providers/ai-sdk-providers/klingai) | Vercel AI SDK：T2V / I2V / 多图 / 运动控制 |
| [fal.ai Kling models](https://fal.ai/models) | 托管 Kling 3.0 / o3 |
| [yihong0618/klingCreator](https://github.com/yihong0618/klingCreator) | 非官方逆向客户端（有风险，优先官方 API） |
| [chenwr727/KLing-Video-WatermarkRemover-Enhancer](https://github.com/chenwr727/KLing-Video-WatermarkRemover-Enhancer) | 可灵视频去水印/增强 |

### 提示词合集与制作技能

- [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) — Veo / Kling / Hailuo 提示词
- [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts) — 广告向提示词
- [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) — 跨模型 AI 视频提示资源
- [jnMetaCode/ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) — 短片提示词 Skill
- [Anil-matcha/awesome-ai-video-models](https://github.com/Anil-matcha/awesome-ai-video-models) — 模型 / API / 价格对比
- [backblaze-labs/awesome-video-generation](https://github.com/backblaze-labs/awesome-video-generation) — 视频生成 API 全景

### 平台与聚合

- [fal.ai](https://fal.ai/) — Serverless 推理（含 Kling）
- [Replicate](https://replicate.com/) — 模型托管生态
- [Pollo AI](https://docs.pollo.ai) — 多模型视频 API 聚合
- [EvoLink Kling 文档](https://evolink.ai/docs/en/api-manual/video-series/kling/kling-v3-text-to-video) — 第三方 Kling API 手册

### 相关列表

- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) — Seedance 2.0 提示词合集（本仓库结构灵感来源）

---

## 15. 贡献指南

欢迎贡献！完整规范见 [CONTRIBUTING.md](./CONTRIBUTING.md)（**最新优先**、周更晋升清单、Issue/PR 模板）。

快速规则：

1. 新条目插到对应分类**最前面**（`X.1`）
2. 同步 `README.md` + `README-en.md`
3. 标注 Source；长文放 `prompts/`
4. 候选晋升：`docs/PROMOTE_CHECKLIST.md` + `scripts/dedupe_candidates.py`

---

## 16. Star 历史

<a href="https://star-history.com/#DSeaStar/awesome-kling&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=DSeaStar/awesome-kling&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=DSeaStar/awesome-kling&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=DSeaStar/awesome-kling&type=Date" />
 </picture>
</a>

---

## 许可证

[MIT](./LICENSE) — 可自由使用、分享与二次创作。引用他人提示词时请保留原作者署名。
