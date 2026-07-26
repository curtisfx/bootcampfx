# PLAN.md — Partner Push-Up Figures for #standard Section

> **Phase:** 1 — PLAN  
> **Date:** 2026-07-26  
> **Status:** Awaiting Actual approval

## LOCKED SPEC (verbatim)

```
CORE DECISION THIS DRIVES:
Add two animated human figures doing partner push-ups to the #standard
(8:00 AM · Full daylight) section — same flat-SVG wildlife language as the
egret/ducks/rabbit — reinforcing "real people train here outdoors" without
touching sales copy, offers, or theme tokens.

IN SCOPE:
- Two CSS/SVG human figures (no JS animation logic), ~130px standing height,
  flat single-tone silhouettes per figure (theme palette — e.g. ink/dawn tones),
  no facial detail (matches animals)
- Animation sequence per figure, infinite loop:
  1) 10 push-ups (torso lowers/rises, ~2s per rep, slight body angle change
     at bottom, subtle head bob)
  2) Transition: push-up → kneel → stand (smooth rise)
  3) ~8s standing rest: subtle weight-shift sway, small arm/breath motion
     ("ready for next set")
  4) Lower back to plank → loop repeats
- Figures offset in phase (~2s apart) and slightly different motion patterns
  (different rep timing, different sway pattern) so they're clearly partners,
  not clones; side by side, facing same direction
- Placement: #standard section, in the open space above the
  "8:00 AM · Full daylight" clock text (inside section top, decorative band)
- Same engineering patterns as wildlife: wrapper div + inner animation span,
  keyframes only, will-change:transform, animation-fill-mode:backwards
- Mobile: figures shrink proportionally (~25% smaller like animals), still
  animated
- prefers-reduced-motion: figures join the existing no-animation kill switch
- aria-hidden="true" (decorative)
- Dead-CSS check + verify pass, commit, push, live MD5/grep verification

OUT OF SCOPE:
- Sales copy, headline, letter, offers, pricing — untouched
- Theme tokens/fonts/sun/wildlife changes — untouched (only ADD figures)
- JS-driven animation
- Realistic human rendering (photographic, faces, muscle detail)
- Any other section; /challenge/; footer/legal
- Sound

DATA SOURCES:
- Existing wildlife implementation in index.html (duck multi-stage loop as
  closest pattern: entrance → infinite behavior)
- Section: #standard, background var(--day) (white) — figures must read on
  light background, unlike hero animals which sit on sky gradient
- User answers: 1=above "8:00 AM · Full daylight", 2A=~130px, 3A=flat style,
  4A=mobile shrink+animate, 5A=~2s/push-up, ~8s rest, ~45s loop, 2s offset

SUCCESS CRITERIA:
1. Two figures visible in #standard above the clock text, side by side,
   ~130px standing-equivalent scale.
2. Each does 10 push-ups (~2s/rep), stands, sways subtly ~8s, loops.
3. Figures visibly out of sync (~2s offset) with different sway patterns.
4. No layout shift of existing content; no text overlap; grid intact on
   desktop and mobile (figures resize on small screens).
5. prefers-reduced-motion disables figure animation with existing kill list.
6. Sales copy/offer/theme fingerprints unchanged (greps: headline, plan id,
   Judi, Margaret, egret, $197 counts).
7. raw.githubusercontent MD5 == local MD5 after push; live greps confirm
   new figure classes present.
```

## 1. Frame & Hypothesis

The #standard section is currently text-only on a white `var(--day)` background. Two flat-SVG figures doing partner push-ups above the clock text turn the "8:00 AM" moment into a visual: real people training at full daylight. Hypothesis: pure-CSS keyframe choreography can fake the full push-up→stand→rest→plank loop convincingly IF the figure is built from animated sub-spans (torso group, arm group, head) with transform-origin pivots, the same way the duck uses a `.waddle` inner span.

## 2. Primitives Touched

- `index.html` ONLY:
  - New markup: `<div class="pushers">` band at top of `#standard .wrap` containing two `.pusher` figures (each: wrapper div + inner `<span class="p-anim">` + inline SVG)
  - New CSS: `.pushers`, `.pusher`, `.p-anim`, keyframes: `pushupCycle` (master per figure), `pushupBob`, `standSwayA`, `standSwayB` + media-query shrink + reduced-motion kill-list additions
- Untouched: all sales copy, hero, tokens, other sections, JS

## 3. Execution Prompts

**Step 0 — Snapshot (mandatory safety gate):**
`git add _ops/PLAN-partner-pushup-figures-2026-07-26.md && git commit` → report hash.

**Step 1 — SVG figure construction.**
Design ONE flat human silhouette SVG that reads in both plank and standing poses. Technique: the SVG is a **standing** figure; the push-up pose is achieved by wrapping it in a rotated container (rotate ~85deg so the standing figure lies horizontal in plank position) — same trick as flipping the duck with scaleX(-1). Arms shown straight in SVG; a second inner span overlays slight "arm bend" via a small path swap or elbow-crook overlay that fades in/out via keyframes at rep bottom. If overlay proves fiddly: accept straight-arm plank with torso dip only (bob of 8-10px) — still reads as push-up at 130px scale.

Colors on white bg: figure A = `var(--ink)` (#1a2332-ish), figure B = `var(--dawn)` (orange) or muted slate — two distinct silhouettes, clearly partners not clones.

**Step 2 — Choreography via single master keyframe per figure.**
One ~45s `pushupCycle` keyframe timeline:
- 0–2%: plank hold
- 2–46%: 10 reps — each rep = 2 keyframe pairs (down at X%, up at X+2.2%); torso translateY dip ~9px + slight rotation ~2deg at bottom; head counter-bob ~3px via `.p-head` inner span with inverse keyframe
- 46–56%: transition to stand — container rotation eases 85deg→0deg, translateY shifts ground anchor (feet stay planted)
- 56–74%: standing rest — `standSwayA` keyframe: translateX ±2px, rotate ±1.2deg, small scaleY breath (1→1.015)
- 74–80%: lower back to plank (reverse of stand transition)
- 80–100%: plank hold/buffer → loop

Figure B: same structure, `animation-delay: 2s`, plus alternate sway keyframe (`standSwayB`: different amplitude/timing) and rep timing variance (reps at 2.1s intervals).

Ground line: a thin `box-shadow` or pseudo-element grass line under figures, matching park feel.

**Step 3 — Placement.**
Insert `<div class="pushers" aria-hidden="true">` as first child inside `.standard .wrap`, above `.std-grid`. CSS: `display:flex; justify-content:flex-start; gap:26px; padding:8px 0 26px; pointer-events:none;`. Height ~140px band. It adds vertical space at section top only — std-grid untouched.

**Step 4 — Mobile.**
Media query (same breakpoint as animal shrink): `.pusher svg{ width:98px; }` (~25% smaller), band height shrinks, figures stay animated.

**Step 5 — Reduced motion.**
Add `.pushers, .pusher, .p-anim, .p-head` to the existing `animation:none !important` kill block. Static fallback: figures shown standing upright (opacity .85) — mirrors animals' static mobile behavior.

**Step 6 — Verify (derives from SPEC success criteria).**
Local greps:
- `.pusher` ×2 in markup; `@keyframes pushupCycle`, `standSwayA`, `standSwayB` present
- Kill-list contains `.pusher`
- Fingerprints unchanged: `Why This Fullerton Trainer`, `P-5LX3921079692330VNGW67ZI`, `Judi Heylek`, `Margaret Martinazzi`, `egret`, `$197` count, `MOST POPULAR`
- No `Frequency Effect`, no `Sienna`, no Starter refs
- Keyframe timing math: 10 down/up pairs within 2–46% window; delay 2s on `.pusher.b`

Then commit/push, MD5 raw == local, live greps.

**Step 7 — SITREP.**

## 4. Constraints

- CSS-only animation; zero JS changes
- Palette: existing tokens only
- Single-file edit; deploy = git push main (no PR dance — established pattern)
- Figures must not overlap clock text or grid at any viewport width
- Loop must be infinite and seamless (100% state == 0% state)

## 5. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Rotated-stand trick looks wrong (feet pivot visibly) | transform-origin set at feet; transition window slow (10% of loop); verify in browser screenshot before push |
| White bg makes figure invisible at dawn palette | use `--ink` for figure A (guaranteed contrast); figure B darker dusk tone |
| 45s single keyframe is unwieldy to author | generate keyframe percentages programmatically in Python during build (write once, paste into file) |
| Section top band shifts layout on mobile | fixed-height band; grid unaffected; verify at 390px width |

## 6. Owner Table

| Role | Who |
|---|---|
| Gatekeeper / builder | Drago |
| SPEC lock / approval | Curtis |
| Deploy target | curtisfx/bootcampfx main → GH Pages |

## 7. COUNTERBATTERY

**Fatal flaw candidate: the rotated-standing-figure trick.** A standing SVG rotated 85° into plank will look WRONG in one specific way: arms. A standing figure's arms hang at its sides; rotated, they point at the sky, not the ground. A push-up figure with arms pointing up is a corpse, not a partner. **This WILL fail the "obviously doing push-ups" test** unless the SVG itself is drawn with arms extended forward/down (T-pose-ish) so rotation places hands on the ground — or the figure is drawn natively in plank and the STAND phase is the rotation. Native plank + rotate-to-stand has the same problem inverted: arms off ground when standing.

**Resolution before build:** draw the SVG in a **compromise pose**: arms slightly forward and down (~30° below horizontal). Rotated to plank: hands near ground — reads fine at 130px. Standing: arms look naturally relaxed-forward — reads fine. One SVG, both poses acceptable. If it still fails visual check, fall back to TWO SVGs (plank figure + standing figure) cross-faded during the 10% transition windows — opacity swap, same wrapper, no timing change. Fallback is cheap and guaranteed.

**Failure mode 2: 45s of keyframe soup.** A single 45s cycle with 10 reps × 2 direction changes + transitions + sway is ~60 keyframe stops. Hand-authored, it will drift — rep 7 will land inside the stand transition, or the loop seam will jump. Mitigation: generate the keyframe block with a Python loop (rep i at 2% + i×4.4%, down/up pairs), paste deterministic output. No hand math.

**Failure mode 3: "partners not clones" reads as "one broken figure."** The 2s offset + different sway amplitude means for ~4% of the loop one figure is standing while the other is mid-push-up. At a glance this could look like a glitch rather than partnership. Mitigation: offset small (2s on 45s = 4.4%), and both figures share the plank→stand transition window closely enough that observers see them rise within ~2s of each other — coordinated, not synchronized. Same-direction facing sells "together."

**Plan proceeds** because all three failure modes have mechanical mitigations available before any pixel ships, and the fallback (two-SVG crossfade) bounds the worst case to one extra markup span.

---

**Gate:** `PLAN APPROVED` → execute · `HOLD` → wait · `COUNTERBATTERY FAIL` → attack harder.
