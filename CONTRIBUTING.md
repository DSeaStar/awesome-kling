# 贡献指南 · Contributing

感谢为 [awesome-kling](https://github.com/DSeaStar/awesome-kling) 贡献！  
English: see [CONTRIBUTING-en.md](./CONTRIBUTING-en.md).

## 核心规则：最新优先

- 新提示词**一律插到对应分类最前面**（成为 `X.1`，旧条目顺延）。
- 同步更新 **`README.md`（中文主页）** 与 **`README-en.md`**。
- 完整长文放 `prompts/*.md`，README 只放精选 + 链接。

## 可贡献什么

| 类型 | 放哪里 |
|------|--------|
| Kling I2V | `prompts/i2v-from-x.md` + README §I2V |
| Kling 3.0 / Omni | `prompts/kling-3-omni.md` + README 对应节 |
| Seedance 对照 | `prompts/seedance-from-x.md` |
| T2I | `prompts/t2i-*.md` |
| 负向 / 工作流 | `prompts/negative-prompts.md`, `prompts/workflows.md` |
| 工具 / API 链接 | README 资源节 |
| 周更候选审核 | 从 `docs/x-crawl-candidates/` 晋升 |

## 提示词质量标准

1. **可复现**：尽量完整正文，不要只写「prompt in comments」。  
2. **结构**：时长 / 分镜 / 运镜 / 画幅（T2I）写清。  
3. **Source**：`@handle` + 原帖 URL；原创写 `Original`。  
4. **版权**：不上传无授权媒体文件；可链 X/官网。  
5. **安全**：不收录违法、性剥削未成年人等内容。

### 条目模板

```markdown
### X.1. 标题
*一句话说明。*

**提示词：**
```text
...
```

*来源：名字（[@handle](https://x.com/handle)）— [原帖](https://x.com/handle/status/...)*
```

## 从周更候选晋升

1. 打开 `docs/x-crawl-candidates/YYYY-MM-DD.md`  
2. 跑 `python scripts/dedupe_candidates.py docs/x-crawl-candidates/YYYY-MM-DD.md` 看重复  
3. 按 [docs/PROMOTE_CHECKLIST.md](./docs/PROMOTE_CHECKLIST.md) 勾选  
4. 开 PR（会带 PR 模板）

## 本地命令

```bash
# 周更爬取（可选 Token）
python scripts/weekly_x_crawl.py

# 候选去重对照仓库已有 URL/文本
python scripts/dedupe_candidates.py docs/x-crawl-candidates/YYYY-MM-DD.md
```

## PR 流程

1. Fork → 分支 → 修改  
2. 确保中英 README 同步、最新优先  
3. 填写 PR 模板  
4. 等待维护者合并  

## 行为准则

参与即表示遵守 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。
