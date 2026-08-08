# Contributing

Thanks for contributing to [awesome-kling](https://github.com/DSeaStar/awesome-kling)!  
中文版：[CONTRIBUTING.md](./CONTRIBUTING.md).

## Golden rule: newest first

- Insert new prompts **at the top** of the matching section (`X.1`, shift older items down).
- Update **`README.md` (Chinese homepage)** and **`README-en.md`** together.
- Keep long-form packs under `prompts/*.md`; READMEs hold highlights + links.

## What to contribute

| Type | Where |
|------|--------|
| Kling I2V | `prompts/i2v-from-x.md` + README I2V section |
| Kling 3.0 / Omni | `prompts/kling-3-omni.md` |
| Seedance cross-ref | `prompts/seedance-from-x.md` |
| T2I | `prompts/t2i-*.md` |
| Negatives / workflows | `prompts/negative-prompts.md`, `prompts/workflows.md` |
| Weekly candidate review | Promote from `docs/x-crawl-candidates/` |

## Quality bar

1. **Reproducible** full prompt text when possible.  
2. **Structure**: duration, shots, camera, aspect (T2I).  
3. **Source**: `@handle` + post URL, or `Original`.  
4. **Rights**: no unauthorized media binaries; link out instead.  
5. **Safety**: no illegal or CSAM content.

## Promote weekly candidates

See [docs/PROMOTE_CHECKLIST.md](./docs/PROMOTE_CHECKLIST.md) and run:

```bash
python scripts/dedupe_candidates.py docs/x-crawl-candidates/YYYY-MM-DD.md
python scripts/weekly_x_crawl.py
```

## Code of Conduct

[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
