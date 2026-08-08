# X 提示词爬取日志

## 每周自动任务

| 项 | 值 |
|----|-----|
| **频率** | 每周一 01:00 UTC（约北京时间 09:00） |
| **Workflow** | [`.github/workflows/weekly-x-crawl.yml`](../.github/workflows/weekly-x-crawl.yml) |
| **脚本** | [`scripts/weekly_x_crawl.py`](../scripts/weekly_x_crawl.py) |
| **产物** | `docs/x-crawl-candidates/YYYY-MM-DD.md` + 自动 PR（有变更时） |
| **手动触发** | GitHub → Actions → **Weekly X Prompt Crawl** → Run workflow |

### 启用实时搜索（推荐）

在仓库 **Settings → Secrets and variables → Actions** 添加：

- `TWITTER_BEARER_TOKEN`（或 `X_BEARER_TOKEN`）= X/Twitter API v2 Bearer Token

无 Token 时仍会每周产出 **checklist 报告 / Issue**，需人工或 Agent 按查询补爬。

### 晋升规则（与全库一致）

1. 审阅 `docs/x-crawl-candidates/` 本周文件  
2. 完整 prompt **插到** `prompts/i2v-from-x.md` / `prompts/seedance-from-x.md` **最前面**  
3. 同步 `README.md` / `README-en.md` 对应章节最前  
4. 标注 Source：`@handle` + 原帖 URL  

## 规则

- **最新优先：** 新批次写入 `prompts/*-from-x.md` 顶部，并同步插入 `README.md` / `README-en.md` 对应章节最前。
- **必须标注 Source：** 作者 handle + 原帖 URL。
- **只收录公开可复述提示词**；无完整 prompt 的帖子只记工作流不硬编文案。
- **去重：** 与已有条目高度重复则合并引用，不重复粘贴。
- **自动爬取只产候选，不直接改精选正文**（避免未审核 prompt 污染主列表）。

## 爬取批次

| 日期 | 主题 | 工具/查询 | 入库文件 | 条数 |
|------|------|-----------|----------|------|
| 2026-08-08 | weekly auto | checklist-only (no token) | `docs/x-crawl-candidates/2026-08-08.md` | I2V=0, Seedance=0 |
| 2026-08-08 | Kling I2V | X keyword/semantic + thread fetch | `prompts/i2v-from-x.md` | 2 合集×10 + 3 模板 |
| 2026-08-08 | Seedance 2.0/2.5 | X keyword Latest | `prompts/seedance-from-x.md` | 8 条完整/结构提示词 |

## 代表性源帖

### I2V

- https://x.com/MayorKingAI/status/1927126460352893348 (Kling 2.1 I2V ×10)
- https://x.com/MayorKingAI/status/1914431899675869327 (Kling 2.0 I2V ×10)
- https://x.com/creatorslop/status/2085350375784378440 (细节强化模板)

### Seedance

- https://x.com/soumyattention/status/2085947512582721619 (Roswell 档案片)
- https://x.com/SadiaMalik182/status/2085947010293883115 (咖啡机 UGC)
- https://x.com/woleswoosh/status/2085947166678495452 (健身房自拍)
- https://x.com/AIwithSynthia/status/2085943905577734483 (通勤分镜)
- https://x.com/SimplyAnnisa/status/2085942757110288502 (日本旅行 vlog)
- https://x.com/iamahmedfaraz66/status/2085936538798506430 (练习生 DV)
- https://x.com/saniaspeaks_/status/2085932310923251950 (猫螺旋桨)
- https://x.com/HBCoop_/status/2050246433480020154 (Visual Production Graph)

## 下次建议查询

```
(Kling OR 可灵) ("image to video" OR I2V OR 图生视频) (prompt OR 提示词) min_faves:10
Seedance (Prompt OR 提示词 OR "Scene 1") min_faves:5
from:MayorKingAI Kling
```
