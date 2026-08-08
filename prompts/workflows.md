# 生产工作流 Cookbook

> 可落地流水线。每条可按预算替换模型，但**分镜与身份锁定顺序**建议固定。

---

## 1. 静帧 → 可灵 I2V（最短路径）

1. **文生图**（Flux / MJ / 可灵生图）锁定构图与身份  
2. **可选放大**（Magnific / 官方超分）  
3. **Kling I2V**：提示词只写 **运镜 + 动作 + 光**（见 `i2v-from-x.md`）  
4. **负向**：手/脸/穿模（见 `negative-prompts.md`）  
5. **剪映 / CapCut**：多段拼接 + 配乐  

**I2V 最小提示：**
```text
Slow push-in, subtle natural motion, preserve identity and composition, photoreal, 4K
```

---

## 2. Kling 3.0 Omni 短剧钩子（竖屏）

1. 写 10–15s 时间轴（3 镜头：羞辱 → 反转 → 揭示）  
2. 角色 Elements 固定男主/女主  
3. 对白写在 `AUDIO` 块，口型冲突则分段  
4. 导出 9:16 → 加字幕  

模板见 `kling-3-omni.md` §4。

---

## 3. 广告：产品图 → 多镜头 T2V/I2V

1. 产品白底图 + 使用场景参考  
2. Seedance / Kling 用 **Scene 1–6** 时间码（咖啡机案见 `seedance-from-x.md`）  
3. 不稳镜头单独重掷，用「指定镜头替换」  
4. 统一调色 LUT  

---

## 4. Seedance 分镜 → 可灵复刻对照

1. 同一 prompt 先跑 Seedance 2.x 拿节奏  
2. 原样进 Kling 3.0，记录：人脸 / 口型 / 物理 / 指令遵循  
3. 弱项用 I2V 垫帧或 Motion Control 补  

适合做「同 prompt 横评」内容。

---

## 5. Motion Control 热点同款

1. 热点视频裁 3–5s 动作段（注意版权）  
2. 主体图 / 产品图作身份  
3. Kling Motion Control 迁移  
4. 换场景提示词，保留动作  

---

## 6. 批量 UGC（带货口播）

1. 一张创作者参考 + 一张产品图  
2. 口播稿 15s，拆 3 次景别切换  
3. Kling 原生音频或后期 TTS + 轻微对口型  
4. 批量换产品图，复用同一分镜骨架  

---

## 7. Visual Production Graph（多镜头连贯）

1. 拼一张控制图：角色条 + 场景条 + 分镜九宫格  
2. 文本只写 timing / camera / shot order  
3. Seedance 或 Kling Omni 执行  
4. 失败镜头用单镜 I2V 补  

来源思路：[@HBCoop_](https://x.com/HBCoop_/status/2050246433480020154)

---

## 工具链速查

| 步骤 | 工具 |
|------|------|
| 静帧 | Flux, MJ, 可灵生图 |
| 视频 | Kling 3.0 / Omni, Seedance 2.x |
| API | 官方 Open Platform, fal.ai, ComfyUI-KLingAI-API |
| 剪辑 | 剪映, CapCut |
| Agent | MCP Kling, vibeframe, AI SDK Kling provider |
