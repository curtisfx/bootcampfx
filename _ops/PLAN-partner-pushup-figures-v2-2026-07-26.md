# PLAN.md — Partner Push-Up Figures v2 (#standard)

> **Phase:** 1 — PLAN  
> **Date:** 2026-07-26  
> **Status:** Awaiting Actual approval  
> **Supersedes:** PLAN-partner-pushup-figures-2026-07-26.md (v1 — ship 6f3ea5f Undo'd as corpse balloons)

## LOCKED SPEC (verbatim)

```
CORE DECISION THIS DRIVES:
Add two animated human figures doing partner push-ups in #standard
(above "8:00 AM · Full daylight") using the same flat wildlife language as
egret/ducks/rabbit — without the corpse-balloon failure of the prior
rotated-standing-SVG approach — reinforcing real people train outdoors.

IN SCOPE:
- Two CSS/SVG figures, ~130px standing height, flat solid-color silhouettes
  (theme palette, no faces), side by side, partners not clones
- Technique: native plank SVG (hands on ground) + separate standing SVG;
  crossfade/swap on stand and lower — NO 87° rotation of a standing body
- Thin ground line / shadow under both so they read planted, not floating
- Infinite loop per figure:
  1) 10 push-ups (~2s/rep) with real vertical dip of the plank torso
  2) Transition plank → stand (SVG swap + smooth rise)
  3) ~8s standing rest: subtle weight-shift sway / ready-for-next-set motion
  4) Lower back to plank → loop
- Figure B: ~2s phase offset + different sway/rep micro-timing
- Placement: decorative band at top of #standard, above the clock text
- Engineering: wildlife pattern (wrapper + inner spans, keyframes only,
  will-change:transform, fill-mode backwards); no JS animation logic
- Mobile: ~25% smaller, still animated
- prefers-reduced-motion: join existing kill list; static standing fallback
- aria-hidden="true"; dead-CSS check; commit; push; MD5 + fingerprint verify

OUT OF SCOPE:
- Sales copy, offers, pricing, PayPal, SMS hrefs
- Theme tokens, fonts, sun, existing wildlife (ADD only)
- JS-driven animation; photographic/detailed humans; faces
- Hero placement; challenge/footer/legal pages
- Sound; 87° rotate-standing trick (explicitly banned)

DATA SOURCES:
- Live index.html wildlife patterns (duck multi-stage, kill list, mobile shrink)
- #standard section: var(--day) light background — figures must contrast
- Failed ship 6f3ea5f (reverted d94b5d6): corpse-balloon root cause = rotated
  standing SVG + float (no ground) + weak bob
- Answers: 1A placement, 2A dual-SVG native plank+stand, 3A ground contact,
  4A 130px flat, 5A 45s loop / mobile animate

SUCCESS CRITERIA:
1. Two figures visible above the #standard clock, side by side, ~130px stand scale.
2. At a glance they read as people doing push-ups (hands ground, body horizontal
   in plank) — NOT floating corpses or balloons.
3. Each: 10 push-ups → stand/sway ~8s → lower → loop; B offset ~2s + different sway.
4. Ground line/shadow present; no float.
5. No layout break; no text overlap; grid intact desktop + mobile.
6. Reduced-motion disables figure animation with existing kill list.
7. Copy/offer/theme fingerprints unchanged (headline, plan IDs, reviews, egret, $197).
8. raw.githubusercontent MD5 == local after push; live greps show new figure classes.
```

---

## 1. Frame & Hypothesis

**Frame:** v1 rotated a standing silhouette 87° into "plank." Arms pointed wrong, bob was a float, no ground contact — Curtis called it floating corpse balloons and Undo'd. The mission is unchanged; the technique is not.

**Hypothesis:** If each figure carries two native SVGs (plank drawn horizontal with hands on a ground plane; standing drawn upright with feet on that same plane), and CSS only opacity-swaps + translateY on the plank torso for reps, then the silhouettes will read as training partners at a glance — same fun language as the wildlife, without the rotate corpse failure.

---

## 2. Primitives Touched

- [ ] `/Users/macmini/sites/bootcampfx/index.html` ONLY
  - CSS: `.pushers` band, `.pusher`, `.p-plank` / `.p-stand` layers, ground pseudo, keyframes, mobile shrink, reduced-motion kill-list append
  - Markup: band as first child inside a restructured `#standard` wrap (see Step 3) — pushers above `.std-grid`, clock text unchanged in sticky column
- [ ] `_ops/PLAN-partner-pushup-figures-v2-2026-07-26.md` (this file — safety snapshot commit)
- [ ] Untouched: hero wildlife, tokens, copy, offers, PayPal, SMS, JS behavior, other pages

---

## 3. Execution Prompts

### Step 0: Safety snapshot
**Action tier:** FREE  
**Prompt:**  
```bash
cd /Users/macmini/sites/bootcampfx
git add _ops/PLAN-partner-pushup-figures-v2-2026-07-26.md
git commit -m "Phase 1 safety snapshot — push-up figures v2 plan (dual-SVG, no rotate)"
git rev-parse --short HEAD
```
Report hash to Actual before any `index.html` edit.  
**Verification gate:** Commit exists; HEAD short hash reported.

### Step 1: Draw two native SVGs (per figure color)
**Action tier:** FREE  
**Prompt:**  
Author flat single-fill SVG paths (no faces, no strokes required beyond silhouette):

**Plank SVG** (viewBox roughly `0 0 160 70`):
- Body horizontal, head left or right (both figures face same direction)
- Hands under shoulders on the baseline (y = ground)
- Feet on baseline; slight hip height
- Elbows slightly bent at rest plank so the dip has room
- Readable at ~70×30px rendered during plank phase

**Standing SVG** (viewBox roughly `0 0 70 140`):
- Head, torso, arms relaxed slightly forward (~20–30°), legs straight, feet on baseline
- Standing height target ~130px CSS height
- Same silhouette language as animals (blob limbs, no joints drawn as circles)

Colors: figure A `fill="var(--ink)"`, figure B `fill="var(--pine)"` or muted dusk (must contrast on `var(--day)` white — avoid pale gold alone; gold was OK for B on v1 but pine/ink pair is safer for "planted athlete" not balloon). If pine fails contrast check in browser, B uses a darkened dawn/ink mix via existing token only — no new CSS variables.

**Hard ban:** Do not rotate the standing SVG into plank. Do not reuse v1 paths as the sole asset.

**Verification gate:** Both SVGs exist in markup; plank silhouette has hands and feet on a shared baseline in path coordinates.

### Step 2: Structure + ground contact
**Action tier:** FREE  
**Prompt:**  
Restructure `#standard` only as needed:

```html
<section class="standard" id="standard" ...>
  <div class="wrap">
    <div class="pushers" aria-hidden="true">
      <div class="pusher a">...</div>
      <div class="pusher b">...</div>
    </div>
    <div class="std-grid">
      ... existing sticky + list unchanged ...
    </div>
  </div>
</section>
```

Each `.pusher`:
- Fixed-height stage (~150px) so layout is stable
- `position:relative`
- `::after` or child `.p-ground`: thin oval/line shadow at bottom (`background` or `box-shadow`, low opacity ink) — shared ground line under both partners in the band also acceptable as `.pushers::after`
- Inner stack:
  - `.p-plank` (absolute, opacity 1 during push phase) containing plank SVG + optional `.p-torso` wrapper for dip
  - `.p-stand` (absolute, opacity 0 during push phase) containing standing SVG
- `pointer-events:none`
- Band: `display:flex; gap:~28–36px; justify-content:flex-start; padding` so figures sit above the clock column, not on top of H2 text

**Verification gate:** SPEC #1 + #4 — figures above clock; ground mark present; no text overlap at desktop width.

### Step 3: Master 45s choreography (CSS only)
**Action tier:** FREE  
**Prompt:**  
One master timeline per figure (~45s, `ease-in-out`, infinite). Generate keyframe % with Python — do not hand-math 10 reps.

**Timeline (figure A):**
| Window | % of 45s | Motion |
|--------|----------|--------|
| Plank hold | 0–2% | plank visible, stand hidden |
| 10 reps | 2–46% | each rep ~4.4% (~2s): torso dip down ~12–16px then up; slight body angle ±2° optional on `.p-torso` |
| Rise transition | 46–56% | plank opacity → 0, stand opacity → 1; stand translateY from ~+20px → 0 (rise) |
| Stand rest | 56–74% | sway: translateX ±2–3px, rotate ±1–1.5°, subtle scaleY breath 1→1.012 |
| Lower transition | 74–82% | reverse of rise |
| Plank buffer | 82–100% | plank hold → seamless loop (100% == 0%) |

**Figure B:** `animation-delay: 2s` on all layered animations; alternate sway keyframes (different phase / amplitude); rep windows shifted ~0.3–0.5s equivalent so dips are visibly not clones.

Layers that need own keyframes (same duration, shared delay):
- `.pusher` or stage: optional micro ground settle
- `.p-plank` / `.p-stand`: opacity (+ stand rise translate)
- `.p-torso` (inside plank): push-up dip only during 2–46%

`animation-fill-mode: backwards` where delay is used. `will-change: transform, opacity` on animated layers only.

**Verification gate:** SPEC #2–3 — greps show 10 dip peaks in plank window; opacity swap windows; B delay 2s; loop endpoints match.

### Step 4: Mobile + reduced motion
**Action tier:** FREE  
**Prompt:**  
At existing `@media (max-width:640px)` (same breakpoint as animal shrink):
- `.pusher` / SVGs ~25% smaller (stand height ~98px)
- Band min-height shrinks; figures **stay animated**

In existing reduced-motion kill block (wildlife list), append:
`.pushers, .pusher, .p-plank, .p-stand, .p-torso` → `animation:none !important`  
Static fallback: both figures show **standing** SVG at opacity ~0.9, ground visible (mirrors animals parked settled).

**Verification gate:** SPEC #5–6 — kill-list contains pusher classes; mobile rules present; reduced-motion shows stand not mid-plank float.

### Step 5: Local verify (before push)
**Action tier:** FREE  
**Prompt:**  
Run checklist derived only from SPEC success criteria:

```bash
# structure
grep -c 'class="pusher' index.html   # expect 2
grep -c 'p-plank\|p-stand' index.html
grep -n 'pushers\|pushCycle\|p-ground\|8:00 AM' index.html | head -40
# ban rotate corpse path
grep -n 'rotate(87\|rotate(85\|rotate(90' index.html && echo FAIL_ROTATE || echo OK_NO_CORPSE_ROTATE
# fingerprints (counts must match pre-edit baseline — capture baseline BEFORE edit)
grep -c 'egret\|Judi Heylek\|Margaret Martinazzi\|MOST POPULAR\|\$197' index.html
# banned
grep -n 'Frequency Effect\|Sienna' index.html || true
```

Also: div balance sanity; `std-grid` still two-column desktop CSS; no new JS.

**Optional local visual:** open file:// or local server, screenshot #standard — if still corpse-like, STOP and report (do not push). Criteria: hands on ground in plank, body horizontal, feet/hands share ground line with shadow.

**Verification gate:** All SPEC greps green; no 87° rotate; baseline fingerprints unchanged.

### Step 6: Commit, push, live verify
**Action tier:** FREE (established BootCampFX main-deploy pattern)  
**Prompt:**  
```bash
cd /Users/macmini/sites/bootcampfx
git add index.html
git commit -m "Partner push-up figures v2 — dual native plank/stand SVGs in #standard (no rotate, ground contact)"
git push origin main
# wait ~30–60s
LOCAL=$(md5 -q index.html)
RAW=$(curl -sL "https://raw.githubusercontent.com/curtisfx/bootcampfx/main/index.html" | md5)
# compare LOCAL == RAW
curl -sL "https://bootcampfx.com/?v=$RANDOM" | grep -oE 'pushers|pusher a|p-plank|p-stand' | sort | uniq -c
```

**Verification gate:** SPEC #7–8 — raw MD5 match; live greps show figure classes; fingerprints still hold on raw.

### Step 7: SITREP + kaizen stub
**Action tier:** FREE  
**Prompt:** Report commit hash, MD5, visual read ("push-ups yes/no"), residual risks. Phase 4 kaizen append after Actual accepts.

**Verification gate:** Actual has enough to accept or Undo.

---

## 4. Constraints

- CSS-only animation; zero new JS
- Existing design tokens only (`--ink`, `--pine`, `--dawn`, `--day`, `--gold` as accent only if contrast holds)
- Single file: `index.html`
- Deploy = push `main` (no feature branch unless Actual orders)
- Explicit ban: rotate-standing-into-plank technique from v1
- No sales/theme/wildlife mutations beyond additive figure CSS/markup
- Loop must be seamless (100% state equals 0%)
- Undo path remains `git revert HEAD --no-edit && git push`

---

## 5. Risks & Mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Opacity crossfade still reads as morph glitch | M | H | Short transition window (10%); slight vertical rise on stand so it feels like a get-up, not a dissolve |
| Plank SVG still "balloon" if proportions wrong | M | H | Wide low viewBox; clear head/hips/feet; dip 12–16px not 4px; ground shadow mandatory |
| Gold/light fill disappears on `--day` | L | M | Prefer ink + pine; visual contrast check before push |
| Nesting wrap breaks `.std-grid` sticky | M | M | Only peel `std-grid` off outer wrap; leave grid CSS untouched; verify sticky at desktop |
| 45s keyframe soup drifts | M | M | Python-generated % tables pasted once |
| User Undo again without diagnosis | M | L | Local visual gate before push; SITREP asks "do they read as push-ups?" |

---

## 6. Owner Table

| Role | Who |
|------|-----|
| Gatekeeper / builder | Drago |
| SPEC lock / approve | Curtis (Actual) |
| Deploy | curtisfx/bootcampfx `main` → GH Pages |
| Verify | Drago (greps + MD5); Actual (eyes on motion) |

---

## 7. COUNTERBATTERY

### Fatal flaw

**Crossfade is not a get-up.** Two SVGs swapping opacity will still fail SPEC criterion #2 if the stand/plank silhouettes don't share a common ground anchor and silhouette mass. If the plank figure is drawn "floating" inside its viewBox (whitespace under hands) and the standing figure has different foot Y, the swap will look like a teleporting ink blot — corpse balloon 2.0, just without rotation. **This WILL fail if path baselines are not engineered to the same CSS ground pixel.**

### Attack per step

**Step 1 (SVG draw):**  
AI-drawn "simple human" paths default to cute blobs. At 130px they become balloons again. Hands-on-ground in the path file is not the same as hands-on-ground after CSS `height` scaling and absolute positioning. Failure condition: plank path has >15% empty viewBox under the body.

**Step 2 (structure):**  
Splitting `.wrap.std-grid` into `.wrap` > pushers + `.std-grid` is the same structural move that v1 made. If padding on `.pushers` is too tall, the sticky column starts lower and the section feels broken even if greps pass. Failure condition: clock no longer appears in the first viewport slice of #standard on laptop.

**Step 3 (choreography):**  
10 reps at 2s with only torso `translateY` on a rigid plank SVG can still read as a seesaw or a worm if the whole plank group dips including hands (hands must stay planted — dip only torso/hips, or dip whole body but keep a separate static hand/ground layer). **If the entire plank SVG translates down, hands leave the ground → float → corpse.** Failure condition: single transform on whole plank SVG for the bob.

**Step 4 (a11y/mobile):**  
Static reduced-motion fallback that leaves `opacity:0` on stand (because animation never runs to the stand keyframe) shows nothing or empty stage. Failure condition: kill-list without explicit standing opacity defaults.

**Step 5–6 (verify/push):**  
Grep cannot see "looks like push-ups." MD5 green + corpse on screen is exactly how v1 shipped. Failure condition: push without a human visual check against criterion #2.

### Mortal risks Section 5 soft-pedaled

1. **SPEC asked for partners "working with each other."** Phase offset alone does not sell partnership; if they're different colors and never face each other or share spacing language, they read as two unrelated GIFs. Spacing + shared ground line is doing more work than the 2s offset.
2. **Wildlife is in the hero; these are in a white content section.** Same "fun" bar is harder on `--day`. Flat ink figures can look like decorative dividers or error glyphs if motion is too subtle.
3. **Re-litigating v1 via cherry-pick.** Temptation to salvage v1 CSS and "just fix rotate" will reintroduce the ban. Plan must write fresh keyframes and fresh markup class names if needed (`pusher` OK to reuse).

### Verdict

**Survives COUNTERBATTERY?** YES — conditional.

We proceed because the dual native-SVG approach directly kills the proven v1 failure mode (rotate + float), **and** Step 3 requires hands-planted dip (torso layer, not whole-SVG translate), **and** Step 5 blocks push on visual fail of criterion #2.  

We accept residual risk that crossfade get-up is less fluid than a multi-joint rig — still within SPEC (2A chosen over multi-part). If Actual eyes still say balloon after v2, next iteration is Step 2B multi-part pivots — not another rotate.

---

**Gate:** `PLAN APPROVED` → execute · `HOLD` → wait · `COUNTERBATTERY FAIL` → attack harder.
