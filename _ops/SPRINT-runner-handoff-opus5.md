# BootCampFX SPRINT — Handoff Brief

**To:** Opus 5
**From:** Drago (Mac mini / Hermes)
**Date:** 2026-08-20
**Purpose:** Full technical context for the endless-runner game on bootcampfx.com, so you can review, extend, or modify it without breaking the live site or the visual system.

---

## 1. What it is

A single-file, zero-dependency endless runner game — **BootCampFX SPRINT** — hosted at `bootcampfx.com/runner.html`. Pure HTML + inline CSS + one inline `<script>` on a `<canvas>`. No build step, no framework, no external JS. It is linked from the main site nav ("Play the Runner") and footer.

It is a marketing/engagement piece for Curtis Ludlow's outdoor boot-camp business, **not** a standalone product. It must always look like a page of bootcampfx.com, not a third-party game.

---

## 2. File & hosting facts

| Field | Value |
|---|---|
| File | `runner.html` (single self-contained file, ~32 KB) |
| Repo | `curtisfx/bootcampfx` — https://github.com/curtisfx/bootcampfx |
| Host | **GitHub Pages** (static only — see §7 Limitations) |
| Pages source | Branch `main`, folder `/` |
| Custom domain | `bootcampfx.com` |
| Live URL | https://bootcampfx.com/runner.html |
| Deploy model | Push `main` → Pages auto-build → live (~30–120 s CDN propagation) |
| Fonts | Google Fonts CDN: Fraunces, Instrument Sans, Spline Sans Mono |

**Deploy rule:** editing `runner.html` and pushing `main` IS the deploy. There is no staging. Verify before you push.

---

## 3. Design tokens (must not change)

The game draws its palette and type from the site's **sunrise system**. These are locked — do not introduce new colors or fonts.

```css
--predawn:   #0F1B2C   /* 5:20 AM sky — game background top */
--predawn-2: #16273D   /* sky gradient mid */
--pine:      #14291F   /* tree line / ground */
--dawn:      #E8933A   /* first light — accent/CTA/rope/ball */
--gold:      #F2B84B   /* highlights, perfect pops, banner */
--day:       #FBF7EE   /* page cream — text on dark, ball body */
--day-2:     #F3ECDC   /* cream alt */
--ink:       #14100A   /* primary text / silhouette fills */
--mist:      #9FB0C4   /* secondary text / muted UI */
--stone:     #6A6255   /* daylight secondary */
```

Fonts:
- **Fraunces** (display) — title, big banner, score numerals
- **Instrument Sans** (body) — HUD, labels, buttons
- **Spline Sans Mono** (mono) — uppercase micro-labels, hints, control keys

**Visual language (locked):** flat solid-color silhouettes, no faces, no photographic detail, capsule limbs, soft oval ground shadows ("ground contact or they float"). Athlete is **all-black ink**, no facial features.

---

## 4. Game logic (mechanics — do not regress)

### Canvas & viewport
- Canvas fills viewport, `devicePixelRatio` capped at 2.
- `GROUND = H * 0.78` — the running surface.

### Player
- Hitbox `w:34, h:58`. Spawns at `x = max(70, W * 0.22)`.
- `GRAV = 2350`, `JUMP_V = -820`, `FAST_FALL_V = 1150`.
- **Jump**: `Space` / `↑` / tap. One buffered jump max (`jumpBuf`, cap 1 — no double-jump).
- **Slide**: `↓` / swipe-down. `slideHeld` holds the slide; releasing un-slides after `slideT > 0.2`. Air-slide = fast-fall (`vy = max(vy, FAST_FALL_V)`).
- **Slide-release is critical**: `releaseSlide()` must fire on `keyup` (ArrowDown) AND `pointerup`/`pointercancel`. A previous bug left the athlete permanently slid because touch never released — this is now fixed and must not be reintroduced.

### Obstacles (three types)
| Type | Spawn dims | Clear |
|---|---|---|
| `ball` (soccer ball) | `w:40, h:40` | jump over |
| `block` (cinderblock) | `w:44, h:46` | jump over |
| `bar` (overhead) | `w:110, h:34, gap:42` | slide under |

- Spawn at `x = W + 60`, move left at `speed()`, removed when off-screen left (`x + w < -80`).
- Spawn probability ramps density over time via `rollGap()` (gap tightens over 90 s of play, with a floor so it stays winnable).
- Bar collision uses the top edge (`GROUND - gap`); ball/block use the bottom edge vs `GROUND - o.h`.

### Scoring
- **Distance**: `score += speed() * dt * 0.018` (continuous).
- **Clear**: `+1` combo; base points `25 + combo * 5`.
- **PERFECT**: if clearance margin `minGap < 16`, points **double** and the pop is gold.
- **Combo** resets on hit. `bestCombo` tracked. `best` high score tracked.
- HUD: Score (left), COMBO ×N (center, appears at combo > 1), Best (right).

### Speed ramps
- `BASE_SPEED = 250` (was 330 — slowed on request).
- Tiers `[1, 1.35, 1.7, 2.1]`, one every 25 s of play, capped at the last tier.
- On ramp: "SPEED RAMP ×N" banner + "Keep the pace, Marine" sub, plus a brief spawn pause so the ramp never feels like a cheat.

### Game over / restart
- Hit → dying state (knockback, screen shake, particle burst, hit-flash) → game over overlay.
- Score / Best Combo / Best board + NEW RECORD badge when `score > best`.
- Restart via RESTART button, `Space`, `Enter`, or tap.

### Persistence
- `localStorage` key **`bootcampfxRunnerHighScore`**.
- Wrapped in try/catch — private-mode / storage-denied must not crash the game.

### Background décor (non-interactive, decorative only)
- **Trees** (pine, layered canopy) — parallax at `speed * 0.5`.
- **Egrets** (1–2, small scale 0.35–0.5, wing flap) — parallax `speed * 0.16`.
- **Ducks** (1, ground waddle) — `speed * 0.62`.
- **Rabbits** (1, foreground hop) — `speed * 0.82`.
- **Clouds** (4, faint cream) — `speed * 0.07`.
- Density was **reduced on request** (was 2 ducks + 2 rabbits). Keep it sparse.

---

## 5. State machine

```
menu → play → dying → over → (restart) → play
```

- `STATE` is one of `menu | play | dying | over`.
- Input routes differently per state (e.g. `Space`/`Enter` on `over` restarts; jump input on `menu` starts).

---

## 6. Rules of engagement (non-negotiable)

1. **Theme lock.** Do NOT change the sunrise palette, fonts, or silhouette language. "We're just changing the sales copy and the offers" applies in spirit here too — the game's visual system is part of the brand.
2. **Single-file, zero dependencies.** Do not introduce a build step, npm packages, or external JS. Google Fonts is the only external resource.
3. **No audio** unless explicitly ordered (explicitly cut from original scope).
4. **Storage key is fixed.** Do not rename `bootcampfxRunnerHighScore` — it would wipe every visitor's high score.
5. **Logic regressions are the worst failure.** Rendering/styling edits are cheap; breaking input, collision, or the state machine is not. Verify with the headless harness (§8) before pushing.
6. **Deploy = push `main`.** There is no staging or feature-flag path for this file. If you're uncertain, ask before you push.

---

## 7. Limitations (GitHub Pages — hard constraints)

- **Static hosting only.** No server-side code, no databases, no APIs, no backend leaderboards.
- **Persistence is `localStorage` only.** Per-browser, per-device. High scores do **not** sync across devices and are lost if the user clears browser data. This is accepted — do not build around it.
- **No server-side scoring validation.** Scores are client-trusting; anyone can edit localStorage. Acceptable for a marketing game; do not promise anti-cheat.
- **CDN propagation lag.** After push, `bootcampfx.com` can serve stale bytes for 30–120 s. `raw.githubusercontent.com/curtisfx/bootcampfx/main/runner.html` is the authoritative post-commit source; live catches up.
- **CNAME required** at repo root (already present — leave alone).
- **Mobile/desktop both supported** via pointer + keyboard; verify both after changes.
- **No build/minification.** The file is served as-is.

---

## 8. Verification (the bar for "done")

1. **Syntax**: extract the `<script>` and run `node --check`.
2. **Headless loop**: stub DOM/canvas, drive the frame loop with a monotonic clock. Confirm: start → score accrual → collision → dying → game over → high-score persistence → restart.
3. **Slide-lock regression**: simulate keyboard hold/release AND touch swipe-down/release; both must un-slide.
4. **Token hygiene**: `grep` for banned legacy values — old red `#e11d2e`, Impact/Segoe fonts, and the word `rope` (replaced by `ball`). All must return zero.
5. **Deploy proof**: local MD5 == `raw.githubusercontent` MD5 == live MD5 after CDN settles.

---

## 9. Known history (so you don't rediscover it)

- **v1** (Vladimir): near-black + bright red + Impact font + grey city skyline. Cartoon athlete (flesh face, red headband).
- **v2** (Drago, 2026-08-20): full restyle to sunrise site language — predawn gradient sky, pine tree line, wildlife décor, all-black silhouette athlete, dawn/gold accents, Fraunces/Instrument Sans. Logic byte-identical to v1.
- **v2.1** (Drago, 2026-08-20): six polish fixes — egrets shrunk, wildlife density reduced, scroll slowed (330→250), **touch slide-lock fixed**, rope obstacle → soccer ball, start-page instructions restructured.

---

## 10. What Curtis will judge you on

- Does it look like *his* site, not a generic game? (silhouettes, sunrise, wildlife)
- Does it play clean on his phone? (tap/swipe are the primary controls)
- Did you break scoring, collision, or the state machine? (the unforgivable sin)
- Did you keep it one file and dependency-free?

If in doubt about scope, ask before building. This is a live marketing asset, not a sandbox.

— Drago
