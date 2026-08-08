# Kling 3.0 Prompt Formula

> Distilled from official Kling guides and community best practices. Use this structure for text-to-video, image-to-video, multi-shot, native-audio, and **text-to-image (T2I)** workflows.

For full T2I fashion briefs (JP / CN / EN), see [`t2i-fashion-portraits.md`](./t2i-fashion-portraits.md).

## T2I fashion brief structure

For stills (Kling Image / 可灵生图), a sectioned brief often beats a single paragraph:

```
1. Theme      — short title / mood keyword
2. Subject    — who, where, overall shot intent
3. Face       — gaze, features, makeup, hair
4. Wardrobe   — garments + exact pose / limbs
5. Background — place, props, light direction
6. Camera     — aspect, angle, lens, DOF split
7. Texture    — photoreal tags, color grade
8. Negative   — flips, contact breaks, deformations
```

---

## Five-Layer Structure (video)

Write prompts in this order:

```
1. Subject   — who / what is on screen (appearance, wardrobe, age, emotion)
2. Action    — what they do (verbs, pace, physical interaction)
3. Setting   — where + when (location, time of day, weather, props)
4. Camera    — shot size, angle, movement, lens feel
5. Style     — lighting, color grade, mood, film reference, quality tags
```

### Template

```text
[Subject], [Action], in [Setting].
Camera: [shot type], [movement], [lens / DOF].
Lighting: [key light], [mood].
Style: [cinematic reference], photorealistic, high detail, 4K.
Audio (optional): [dialogue / SFX / ambience].
```

## Multi-Shot Scripting (Kling 3.0)

Kling 3.0 handles multi-shot sequences well when you timestamp or label shots clearly:

```text
Duration: 10s. Multi-shot cinematic sequence.

[0-3s] Shot 1 — Extreme wide establishing:
...

[3-7s] Shot 2 — Medium tracking:
...

[7-10s] Shot 3 — Extreme close-up:
...
```

Tips:
- Keep each shot's action simple (one primary motion).
- State continuity cues: same wardrobe, same weather, same time of day.
- Prefer concrete verbs over abstract mood words.

## Image-to-Video

```text
Animate the subject in the reference image.
Motion: [specific motion].
Camera: [push-in / pan / orbit / static].
Keep face identity, clothing, and background layout consistent.
Natural motion blur, realistic physics, photorealistic.
```

## Motion Control

```text
Use the motion reference video for body dynamics and camera energy.
Apply that motion to the character in the image reference.
Preserve identity and clothing from the image; ignore the motion video's identity.
Smooth retargeting, no limb distortion, cinematic lighting.
```

## Native Audio / Dialogue

```text
Character says: "Exact dialogue line here."
Clear lip-sync, natural pauses, [language].
Ambient sound: [rain / city / room tone].
Optional SFX: [footsteps / door / glass].
```

## Product / Commercial

```text
Hero product: [product description].
0-3s: macro beauty shot, shallow DOF, soft key light.
3-7s: hand interaction / usage moment.
7-12s: lifestyle context, brand color palette.
12-15s: product lockup, clean background, logo-safe frame.
Hyper-realistic product commercial, 8K feel.
```

## Negative / Avoid Hints (when supported)

```text
Avoid: morphing face, extra fingers, text artifacts, jitter, over-smoothing, cartoon look.
```

## Camera Language Cheat Sheet

| Intent | Phrase |
|--------|--------|
| Establish space | extreme wide, aerial, establishing shot |
| Emotion | close-up, extreme close-up, shallow DOF |
| Power | low angle, Dutch angle |
| Intimacy | eye-level, medium close-up |
| Energy | handheld, whip pan, tracking shot |
| Prestige | slow dolly, crane rise, steadicam |
| Action | crash zoom, over-shoulder chase, POV |

## Quality Tags (use sparingly)

```text
photorealistic, cinematic lighting, natural skin texture, film grain, 4K, coherent motion, stable identity
```

Do **not** spam dozens of tags — Kling responds better to clear cinematic direction than keyword soup.
