# 模型对照（简表）

> 非官方基准，便于选题。以各平台公开能力与社区横评为参考，会过时——以官网为准。

| 维度 | Kling 3.0 / Omni | Seedance 2.0 / 2.5 | Google Veo 3.x |
|------|------------------|--------------------|----------------|
| 厂商 | 快手可灵 | 字节即梦 | Google |
| 强项 | 运动物理、多镜头、Motion Control、人物质感 | 长分镜叙事、多参考、商用 UGC 节奏 | 指令遵循、电影感、原生对白 |
| 图生视频 | 强 | 强 | 强 |
| 原生音频 | 支持（Omni / 新版本） | 支持 | 强 |
| 参考资产 | Elements / 多图 / 运动参考 | 多参考（2.5 可很多） | 依入口而定 |
| 典型时长 | 短片多镜头（常见 ~5–15s+） | 可达更长连续分镜（2.5 宣传至 ~30s） | 短中片 |
| 适合 | 动作、时尚 I2V、角色一致性、中文短剧 | 广告分镜、档案片质感、旅行 vlog 长叙事 | 高遵从电影预告、英文对白 |
| 本仓库 | `prompts/kling-3-omni.md`, I2V, T2I | `prompts/seedance-from-x.md` | 外链对照 |

## 怎么选（经验法则）

- **要动作 / 运镜刺激 / 角色跟手** → 先 Kling  
- **要 20–30s 多 Scene 广告脚本一次成型** → 先 Seedance，再可灵补镜  
- **要英文对白遵从与「大片感」** → Veo 对照，Kling 做 B 镜  
- **同 prompt 横评** → 固定 10s 脚本 + 固定评分表（物理 / 脸 / 口型 / 指令）

## 延伸阅读

- [Anil-matcha/awesome-ai-video-models](https://github.com/Anil-matcha/awesome-ai-video-models)  
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance)  
- [Kling 3.0 vs Veo 3.1 社区文](https://www.bottlerocketcontent.com/kling-3-0-vs-veo-3-1-the-results-will-blow-your-mind/)（第三方）
