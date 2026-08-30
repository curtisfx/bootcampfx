# BootCampFX "Go" Game — Handoff Brief

**To:** Kimmy k3
**From:** Drago (Hermes · Mac mini)
**Date:** 2026-08-21
**Subject:** Build a new **Go** game page for bootcampfx.com — context on the site's theme, the current Mahjong game, and the animation language you need to match.

---

## 0. The assignment in one line

Build a **Go** game (the classic black-stone / white-stone board game) as a new single-file page for bootcampfx.com, in the same sunrise theme and animation language as the existing games. You design the game itself; this brief is the *style and system* context so it lands on-brand.

## 1. The site & ground rules

- **Site:** bootcampfx.com — an outdoor fitness business in Fullerton, CA. Primarily a direct-response marketing site, now also hosting small free-to-play games (a runner, and Mahjong) as engagement.
- **Host:** GitHub Pages. Repo `curtisfx/bootcampfx`, branch `main`, folder `/`. A new page = a new file/folder (e.g. `go/index.html`).
- **Single-file, zero dependencies.** Inline CSS + JS in one HTML file. Google Fonts is the ONLY external request. No libraries, no build step, no canvas unless you choose to for the board.
- **Theme lock (non-negotiable).** You may use ONLY the tokens and fonts below. Do not invent colors. Do not import new fonts.

## 2. Design system (the sunrise theme)

### Color tokens
```css
--predawn:  #0F1B2C;   /* pre-dawn sky — page background */
--predawn-2:#16273D;   /* lighter pre-dawn */
--pine:     #14291F;   /* tree line — dark green */
--dawn:     #E8933A;   /* first light — accent / CTA orange */
--gold:     #F2B84B;   /* warm gold highlight */
--day:      #FBF7EE;   /* 8 AM — cream / light */
--day-2:    #F3ECDC;   /* light warm */
--ink:      #14100A;   /* near-black text */
--mist:     #9FB0C4;   /* secondary text — cool gray-blue */
--stone:    #6A6255;   /* secondary text — warm gray */
```

### Fonts
```css
--display: 'Fraunces', serif;            /* headings, big numbers */
--body:    'Instrument Sans', sans-serif; /* body copy */
--mono:    'Spline Sans Mono', monospace; /* labels, HUD, small caps */
```
Load exactly:
```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Spline+Sans+Mono:wght@500;600&display=swap" rel="stylesheet">
```

### The silhouette language (critical — "match the site" means THIS, not just the palette)
The site's decorative figures are **flat, faceless silhouettes** — not cartoon, not clip-art:
- **Humans:** all-black (`--ink`) with capsule limbs and a soft oval ground shadow.
- **Animals:** stone rabbits `#9FB0C4` · dawn ducks `#E8933A`/`#F2B84B` · white egrets `#FBF7EE` with a dawn beak · pine trees `#14291F` · a turtle (pine shell `#14291F` + stone body `#9FB0C4`).
- Pull actual SVG path anatomy from `index.html` rather than redrawing approximations.

### Motion
- Easing everywhere: `cubic-bezier(.22,.7,.25,1)`.
- Prefer `transform`/`opacity` animations (GPU-friendly). The one allowed `filter` use is the golden-hour tint, and it must be removed when that state ends.
- **`prefers-reduced-motion` is mandatory.** Every animation is gated; reduced-motion users get static/instant states and the game stays fully playable.

## 3. The Mahjong game — current state (your reference)

URL `bootcampfx.com/mahjong/` · file `mahjong/index.html`.

It is **Mahjong Solitaire**: 144 tiles stacked in a layered "turtle" shape; match pairs of free, identical tiles until the board is empty.

### Structure
- Header: brand wordmark + HUD (Tiles left / Matches / Time / Best).
- Center: the tile board, responsive via CSS `transform: scale()`.
- Footer: Rules / Undo / Hint / Shuffle / New Game buttons.
- "How to Play" overlay that auto-shows on first visit (localStorage flag) + a persistent "? Rules" button.
- Victory overlay on board clear.

### The animations (all additive CSS + JS class toggles on top of game state)
1. **Tile sunrise dissolve on match** — matched tiles glow predawn → dawn → gold, then rise and fade (`translateY(-14px) scale(1.12)`). State marks them `removed` immediately; the visual is a `.dawn-out` class + ~780ms timer to hide.
2. **Golden-hour combo** — a 3-match streak adds a warm `sepia/saturate/brightness` filter over the board + gold tile glow + gold "ghost" afterimages. Clears 1.5s after the streak breaks.
3. **Sky-gradient progress** — a `--clearance` custom property (0→1) drives a `color-mix()` warm-up of the page background as tiles clear. Registered via `@property` for a smooth 1.2s transition.
4. **Wildlife on layer clear** — clearing a full tile layer spawns a rabbit/duck/egret silhouette that crosses the board and auto-removes.
5. **Victory full sunrise** — a gold sun rises from the bottom, 8–12 gold particles drift up, "Victory" breathes in (letter-spacing animation).
6. **Turtle mascot** — a pine-shell turtle walks in on load, then *persistently* slow-wanders all session with an opposite-phase leg gait cycle (±13° rotation, hip pivot via `transform-box: fill-box`) and a dip-to-graze head motion.
7. **Hint fireflies** — pressing Hint emits a burst of gold fireflies from each clue tile (16/tile, staggered ~1.6s, drift 1.8–3s).

### Game-logic pattern worth stealing (Mahjong-specific, but the idea generalizes)
**Solvable-deal generation by pair-peeling:** instead of dealing a random board (usually unsolvable), build the board by *un-solving* — repeatedly remove two simultaneously-free tiles from a full board, then assign matching values to each removed pair. Forward play is the reverse, so it's solvable by construction. If the Go game ever needs "generate a winnable/balanced setup," prefer *construct-a-solution* over *generate-random-then-check*.

## 4. Copy rules (learned the hard way)

- **No jargon in player-facing copy.** Mahjong originally said "clear the turtle" (tile-layout jargon). The client didn't know what it meant and asked. Rewrote to "clear the board" / "clear all 144 tiles." Keep copy plain; decorative mascots stay mascots only.
- **Phone-first.** Every control must be tappable and legible on a phone. Test both viewports.

## 5. Mapping Go onto the theme (your design space — suggestions, not mandates)

- **Stones:** black = `--ink` (or `--predawn`), white = `--day`. The natural in-token mapping.
- **Board:** `--pine` grid lines on a `--day-2` / `--predawn-2` field; `--dawn`/`--gold` for the last move / ko marker / captured territory highlight.
- **Theme the game as a "day" arc:** reuse the sky-progress idea — warm the board background from predawn toward dawn as the game advances (move count, captured territory, or phase). A rising sun on the winning capture is the natural victory beat.
- **Silhouettes for flair:** an idle rabbit/duck/turtle critter foraging at the board edge while the player thinks; stones capture with a dissolve-glow.

## 6. Delivery bar (same as Mahjong)

1. Single self-contained file, Google Fonts the only external request.
2. `node --check` the script; zero console errors on load AND a full playthrough.
3. Banned-token grep returns 0: `#e11d2e`, `Impact`, `Segoe`, `rope`.
4. `prefers-reduced-motion`: fully playable with zero animation.
5. Desktop + phone viewport both work (tap targets, scaling).
6. Deploy = push `main` (or GitHub Contents API). Verify live via the MD5 chain (local == raw == live), not by refresh.

---

— Drago
