# 候选晋升清单 · Promote Checklist

用于把 `docs/x-crawl-candidates/*.md` 里的条目晋升为精选。

## 必做

- [ ] 已打开原帖 / 串帖，**完整 prompt** 可复述（非「prompt below」空壳）
- [ ] `python scripts/dedupe_candidates.py <candidate.md>` 无高重复 URL
- [ ] 写入正确文件 **最前面**（最新优先）
  - [ ] I2V → `prompts/i2v-from-x.md`
  - [ ] Seedance → `prompts/seedance-from-x.md`
  - [ ] Kling 3.0 → `prompts/kling-3-omni.md`
  - [ ] T2I → 对应 t2i 文件
- [ ] `README.md` + `README-en.md` 对应节最前增加精选（或链接到完整包）
- [ ] Source：`@handle` + status URL
- [ ] `docs/x-crawl-log.md` 批次表补一行（可选但推荐）

## 可选

- [ ] 负向提示可复用 → 抽到 `prompts/negative-prompts.md`
- [ ] 可复用流水线 → `prompts/workflows.md`
- [ ] 预览图（自有授权）→ `assets/`

## PR 标题建议

```
feat(prompts): promote N candidates from X crawl YYYY-MM-DD
```
