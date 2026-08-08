# 负向提示词库（Kling / 通用视频）

> 按场景选用，**宁少勿滥**。可灵部分界面支持 negative；不支持时把约束改写成正向（“keep five fingers”, “correct left-right orientation”）。

---

## 通用解剖与身份

```text
extra fingers, missing fingers, fused fingers, deformed hands, extra limbs, missing limbs,
warped face, face morph, identity drift, age change, gender swap,
asymmetric eyes, crossed eyes, bad teeth, melting features
```

中文：
```text
多指，缺指，融指，手部畸形，多余肢体，缺肢，脸崩，身份漂移，五官扭曲，眼神不对齐
```

---

## 左右与接触（时尚 / 姿势）

```text
mirrored, left-right flip, reversed laterality,
hand detached from knee, floating limbs, broken contact,
deformed toes, broken sandal straps, cloth clipping through body
```

中文：
```text
左右翻转，镜像，左右颠倒，手与膝盖分离，肢体悬浮，脚趾畸形，鞋带崩坏，衣服穿模
```

---

## 产品 / 商业

```text
wrong logo, unreadable text, gibberish typography, brand morph,
bottle shape change, label melt, extra bottles, product disappear,
heavy beauty filter, plastic skin, exaggerated HDR
```

中文：
```text
错误 logo，乱码文字，品牌变形，瓶身形变，标签融化，产品消失，过度磨皮，塑料皮肤，夸张 HDR
```

---

## 运动与物理（I2V）

```text
jitter, frame stutter, teleporting, rubber hose limbs,
ignore physics, floating objects, sliding on ice without cause,
camera clipping through body, background warping
```

中文：
```text
画面抖动撕裂，瞬移，橡皮管肢体，无视物理，物体悬浮，镜头穿模，背景扭曲
```

---

## 视频伪影

```text
watermark, stock overlay, subtitle burn-in, UI chrome,
low resolution, heavy compression blocks, oversmoothed,
flicker identity, sudden outfit change mid-shot
```

中文：
```text
水印，台标，烧录字幕，界面元素，低分辨率，色块压缩，过平滑，身份闪烁，中途换装
```

---

## 风格误触

```text
cartoon, anime (unless requested), CGI plastic look, uncanny valley doll,
3D render artifact, video game screenshot
```

---

## 正向改写示例（无 negative 槽时）

| 负向 | 改写成正向 |
|------|------------|
| mirrored | correct orientation, not mirrored |
| extra fingers | natural five-fingered hands |
| face morph | stable face identity throughout |
| product melt | consistent bottle geometry and label |
