# PLAN.md — Partner Jumping-Jack Figures (#standard) v3

> **Phase:** 1 — PLAN  
> **Date:** 2026-07-26  
> **Status:** Awaiting Actual approval  
> **Supersedes:** push-up v1/v2 plans (both Undo'd — visual fail)

## LOCKED SPEC (verbatim)

```
CORE DECISION THIS DRIVES:
Add two animated human figures doing partner jumping jacks in #standard
(above "8:00 AM · Full daylight") — flat wildlife language — reinforcing
real people train outdoors. Push-up approaches abandoned (v1 corpse /
v2 still failed visual).

IN SCOPE:
- Two CSS/SVG figures, ~130px standing, flat solid silhouettes (theme
  colors, no faces), side by side, partners not clones
- Motion: JUMPING JACKS only
  1) 10 jumping jacks (~2s/rep): arms out+up / legs out, then arms in /
     legs together — reads clearly as jacks, not a bob or rotate gimmick
  2) ~8s standing rest: subtle weight-shift sway (ready for next set)
  3) Loop repeats (~45s full cycle)
- Figure B: ~2s phase offset + different sway/micro-timing
- Technique: dual pose SVGs (jack-open + jack-closed) OR simple multi-part
  limbs on one standing figure — whichever reads cleaner; NO plank, NO
  87° body rotate, NO push-up choreography
- Thin ground line/shadow — feet planted / jump clears ground slightly
- Placement: decorative band top of #standard above clock text
- Wildlife engineering patterns; CSS-only; mobile ~25% smaller still
  animated; reduced-motion kill list + static standing fallback
- aria-hidden; verify; commit; push; MD5 + fingerprints

OUT OF SCOPE:
- Push-ups (any form)
- Sales copy, offers, PayPal, SMS, theme tokens, existing wildlife edits
- JS animation; faces/detail; hero; challenge/footer; sound

DATA SOURCES:
- Live index.html wildlife + #standard structure (clean post-e318ce2)
- Failed ships: 6f3ea5f, c802c24 — do not revive
- Prior locks that still hold: placement 1A, scale 4A, style 3A, mobile 5A tempo shape

SUCCESS CRITERIA:
1. Two figures above #standard clock, ~130px, side by side.
2. At a glance: jumping jacks (arms/legs open-close), NOT push-ups, NOT
   floating corpses, NOT random bobbing.
3. 10 jacks → ~8s rest sway → loop; B offset ~2s.
4. Ground contact; jump can leave ground briefly mid-jack.
5. No layout break / text overlap.
6. Reduced-motion disables animation.
7. Copy/offer/theme fingerprints unchanged.
8. raw MD5 == local; live greps show new classes.
```

---

## 1. Frame & Hypothesis

**Frame:** Two push-up ships failed the eye test. Mission stays: decorative partners in `#standard` above the daylight clock. Motion is now jumping jacks — a vertical standing exercise that matches a single upright silhouette language (same as wildlife scale).

**Hypothesis:** A **multi-part standing figure** (torso+head fixed; left/right arms and legs as separate spans with `transform-origin` at shoulders/hips) will read as jumping jacks at ~130px if open pose is extreme (arms ~150–160° from down, legs wide) and closed pose is clear (arms at sides, feet together), with a small vertical hop on each open. Dual full-body SVG crossfade is fallback only if multi-part looks broken.

**Chosen primary technique:** multi-part limb rig (SPEC allows either; multi-part is stronger for continuous jack motion without opacity flicker).

---

## 2. Primitives Touched

- [ ] `index.html` ONLY
  - CSS: `.j//ackers` band (class name `jackers` / `jacker` — fresh names, no reuse of failed `pusher` keyframes)
  - Markup: band first child under `#standard .wrap`, then `.std-grid` (same peel as v2 structure — content unchanged)
  - Keyframes: `jackCycle` pose windows, `jackHop`, `armL/R`, `legL/R`, `standSwayA/B`
  - Mobile 640px shrink; reduced-motion kill + static closed stance
- [ ] `_ops/PLAN-partner-jumping-jacks-2026-07-26.md` (this file)
- [ ] Untouched: hero wildlife, copy, offers, tokens, JS, other pages
- [ ] Explicit delete/avoid: any leftover `pusher`/`pushup`/`p-plank` strings (site should already be clean post-revert)

---

## 3. Execution Prompts

### Step 0 — Safety snapshot
**Action tier:** FREE  
```bash
cd /Users/macmini/sites/bootcampfx
git pull --ff-only origin main
git add _ops/PLAN-partner-jumping-jacks-2026-07-26.md
git commit -m "Phase 1 safety snapshot — jumping-jack figures plan"
git rev-parse --short HEAD
```
Report hash before `index.html` edit.

**Verification:** commit hash reported; working tree plan file tracked.

### Step 1 — Figure construction (multi-part)
**Action tier:** FREE  

Each `.jacker` (~62×130px stand box inside ~140px stage):

```
.jacker
  .j-ground
  .j-body (hop + sway root)
    .j-head     (ellipse / circle span or mini SVG)
    .j-torso    (rounded rect / path)
    .j-arm.l    (origin top-center of arm = shoulder)
    .j-arm.r
    .j-leg.l    (origin top = hip)
    .j-leg.r
```

Flat fills only: A `var(--ink)`, B `var(--pine)`. No faces. Limbs = simple thick rounded bars (border-radius capsules) or tiny path SVGs — must match duck/rabbit “blob” simplicity.

**Closed pose (rest / jack in):** arms ~10–15° from vertical down, legs ~4° from vertical.  
**Open pose (jack out):** arms ~150° outward-up (nearly V above head), legs ~28–35° each side.

**Hard bans:** plank SVG, body rotate to horizontal, push-up bob keyframes, resurrecting v1/v2 CSS blocks.

**Verification:** markup has 2× jacker; 2 arms + 2 legs each; no `pusher`/`p-plank` classes.

### Step 2 — 45s choreography
**Action tier:** FREE  

Python-generate keyframe % (no hand soup).

| Window | % | Behavior |
|--------|---|----------|
| Jacks | 0–44% | 10 reps × ~2s: each rep 50% open / 50% closed; hop up ~8–12px on open peak |
| Settle | 44–50% | ease to closed standing |
| Rest | 50–72% | ~10s sway (SPEC ~8s — use ~10s rest inside 45s after 10×2s=20s jacks + transitions; **adjust:** 10×2s=20s jacks → 0–44% is 19.8s ≈ 10 reps; rest 50–68% = 8.1s; buffer/transitions fill remainder) |
| Buffer | 68–100% | closed hold → seamless loop |

Per-limb animations share 45s duration; figure B `animation-delay: 2s` + slightly different arm amplitude or hop height.

Arms: `rotate()` from shoulder origin.  
Legs: `rotate()` from hip origin.  
Hop: `translateY` on `.j-body` only (ground shadow stays put).

**Verification:** 10 open peaks in arm keyframes; hop peaks aligned; B delay 2s; 100% == 0% closed pose.

### Step 3 — Placement + ground
**Action tier:** FREE  

```html
<section id="standard" class="standard">
  <div class="wrap">
    <div class="jackers" aria-hidden="true">...</div>
    <div class="std-grid"> ... existing ... </div>
  </div>
</section>
```

Band: flex, gap ~32px, min-height ~150px, above clock. Ground: per-figure oval + optional band shadow. Must not cover H2/clock.

**Verification:** SPEC #1,#4,#5 — greps + div balance; clock still first text in sticky column.

### Step 4 — Mobile + reduced motion
**Action tier:** FREE  

640px: ~25% smaller, still animated.  
Kill list append: `.jackers, .jacker, .j-body, .j-arm, .j-leg, .j-head, .j-torso`.  
Static fallback: closed stance, opacity ~0.9, arms/legs at rest transforms.

**Verification:** SPEC #6.

### Step 5 — Local verify (before push)
**Action tier:** FREE  

```
- class="jacker" ×2; @keyframes for arms/legs/hop/sway
- zero matches: pusher, p-plank, pushup, rotate(87
- fingerprints baseline unchanged (capture before edit)
- div balance in #standard
```

**Visual gate (mandatory after two Undos):** write `/tmp/jackers-preview.html`; attempt Safari/screenshot if available; if no browser, still **do not push until** a 3-point self-check on keyframe values is written in the commit body:
1. Open arm angle ≥ 140° from down  
2. Open leg angle ≥ 25° each side  
3. Hop ≥ 8px on open  

If any fail, fix before push.

**Verification:** SPEC #2 checklist signed in SITREP.

### Step 6 — Commit, push, live verify
**Action tier:** FREE  

Commit message: `Partner jumping-jack figures — multi-part silhouettes in #standard (CSS-only, 45s loop)`  
Push main; MD5 local==raw; live greps `jackers|jacker|j-arm`.

**Verification:** SPEC #7–8.

### Step 7 — SITREP
Report hash, MD5, “reads as jacks?” ask. Kaizen after Actual accepts.

---

## 4. Constraints

- CSS only; tokens only; `index.html` only  
- No push-up code paths  
- Fresh class namespace `jacker*`  
- Main deploy; Undo = revert HEAD  
- Loop seamless  

---

## 5. Risks & Mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Capsule limbs look like sticks not wildlife | M | M | Match duck thickness; slightly tapered paths if capsules fail |
| Jacks too subtle at 130px | H | H | Exaggerate open angles; test % of stage width at open |
| Hop + arm rotate desync | M | M | One generator script emits all keyframe series from same rep clock |
| std-grid peel breaks sticky | L | M | Same proven structure as v2 (content was fine; motion was wrong) |
| Third Undo | M | L | Mandatory angle/hop checklist; shorter ship if needed (preview path) |

---

## 6. Owner Table

| Role | Who |
|------|-----|
| Builder / gates | Drago |
| Approve | Curtis |
| Deploy | main → GH Pages |
| Visual accept | Curtis |

---

## 7. COUNTERBATTERY

### Fatal flaw

**Jumping jacks fail the same way push-ups did if “motion” is only a vertical bounce with arms glued.** A multi-part rig that only rotates arms 20° reads as a person shivering, not jacks. **This WILL fail SPEC #2 if open angles are timid.** The plan’s entire credibility is the open-pose extremeness checklist in Step 5 — without it we ship bob-v3.

### Attack per step

**Step 1:** CSS capsules with wrong `transform-origin` (center of limb instead of shoulder) make arms orbit like propellers. Failure = origin not at top 50% 0% of arm element.

**Step 2:** 10 reps in 44% of 45s is correct math, but rest window that still runs arm keyframes at mid-rotate will leave figures stuck mid-jack during “rest.” Failure = arm keyframes not held at closed during 50–100%.

**Step 3:** Band height too short clips raised arms (overflow hidden on section). Failure = arms cut off at open peak.

**Step 4:** Reduced-motion without resetting arm `transform` leaves random mid-keyframe freeze. Failure = no explicit rest rotates in RM block.

**Step 5–6:** After two Undos, greps-green is worthless. Pushing without exaggerated angles repeats the humiliation. Failure = skip checklist.

### Mortal risks underweighted

1. **Partners “working together”** still undersold by delay alone — shared ground line + matching height matter more.  
2. **Pine on day background** may be low-contrast for figure B — ink/dusk backup.  
3. **Wildlife is cute animals; humans doing PT can look corporate-clipart** if too geometric — keep blobs, not gym-bro vectors.

### Verdict

**Survives COUNTERBATTERY?** YES.

Proceed because jacks are an upright exercise that fits one standing rig, multi-part limbs are the only pure-CSS way to get real open/close without crossfade flicker, and Step 5 hard-gates exaggerated angles after two visual failures. Accept risk that capsule limbs need one polish pass after Actual’s eyes.

---

**Gate:** `PLAN APPROVED` → execute · `HOLD` · `COUNTERBATTERY FAIL`
