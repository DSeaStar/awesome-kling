#!/usr/bin/env python3
"""One-shot: refresh Kling 4.0 launch status wording in README.md / README-en.md."""
from pathlib import Path

def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing {label}")
    return text.replace(old, new, 1)

cn_path = Path("README.md")
en_path = Path("README-en.md")
cn = cn_path.read_text(encoding="utf-8")
en = en_path.read_text(encoding="utf-8")

cn = replace_once(
    cn,
    '> **模型状态（2026-10）：** 可灵官方宣布 Kling 4.0 于 10 月正式上线，4.0 Flash 已于 9 月 28 日开放小范围体验。本仓库正在逐条补充 4.0 写法，见 [4.0 专区](#0-kling-40-专区)。',
    '> **模型状态（2026-10-09）：** 可灵官网已主推 All-New Kling 4.0；官方 X 以 "Following the launch of Kling 4.0" 表述。本仓库正在补 4.0 写法，见 [4.0 专区](#0-kling-40-专区)。',
    "CN IMPORTANT",
)
cn = replace_once(
    cn,
    '> **状态：** 骨架已就位，等待 4.0 正式上线后补实测提示词。规格数字引自官方公开信息（2026-09/10）；未实测处标「待实测」。**不编造提示词。**',
    '> **状态：** 官方已上线；可灵官网主推 All-New Kling 4.0。规格数字引自官方公开信息（2026-09/10）；提示词仍待补充（未实测处标「待实测」）。**不编造提示词。**',
    "CN §0 status",
)
en = replace_once(
    en,
    '> **Model status (Oct 2026):** Kling says Kling 4.0 launches in October; Kling 4.0 Flash opened to limited early access on Sept 28. 4.0-specific prompts are being added in the [Kling 4.0 section](#0-kling-40).',
    '> **Model status (2026-10-09):** Kling.ai now leads with All-New Kling 4.0; official @Kling_ai posted "Following the launch of Kling 4.0". 4.0 prompts are being added in the [Kling 4.0 section](#0-kling-40).',
    "EN IMPORTANT",
)
en = replace_once(
    en,
    '> **Status:** Skeleton only. Real prompts land after Kling 4.0 ships. Spec numbers cite public reports (Sep/Oct 2026); untested items are marked **待实测 / TBD**. **No invented prompts.**',
    '> **Status:** Official has launched; homepage leads with All-New Kling 4.0. Spec numbers cite public reports (Sep/Oct 2026); prompts still TBD (untested items marked **待实测 / TBD**). **No invented prompts.**',
    "EN §0 status",
)

cn_path.write_text(cn, encoding="utf-8")
en_path.write_text(en, encoding="utf-8")
print("status refresh applied")
