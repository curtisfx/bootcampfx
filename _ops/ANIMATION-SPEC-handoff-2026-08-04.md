# BootCampFX Animation Spec — Handoff Document
**Source of truth:** `/Users/macmini/sites/bootcampfx/index.html` (commit-level ground truth, 2026-08-04)
**Design system:** Sunrise tokens — `--day:#FBF7EE`, `--pine:#14291F`, `--ink:#14100A`, `--dawn:#E8933A`, `--gold:#F2B84B`, `--stone:#9A9284`, `--ease` custom easing var.

---

## 1. Visual Invariants (Curtis-approved, non-negotiable)

1. **Flat solid-color silhouettes only.** No faces, no photographic detail, no gradients on figures.
2. **CSS keyframes only** for all motion. No JS-driven animation of figures (JS is only scroll-trigger + count-up).
3. **Multi-stage loops**, not stiff loaders — each creature has enter → settle → ongoing micro-motion.
4. **Ground contact is mandatory** on light sections: tight shadow ellipse under feet, or the figure "floats" and gets rejected.
5. **Partners are never clones** — phase-offset (~2s delay), different micro-timing, slightly different angles/scale.
6. **`transform-origin` is the soul of the rig.** Every limb/body/wing pivots from a specific point; get it wrong and the motion reads wrong.
7. **Never two transform animations on one node** — nest: hop inside sway, waddle inside stroll, etc.
8. `aria-hidden="true"` on every decorative element.

---

## 2. Scroll-Trigger System (all wildlife)

- Ducks, hero rabbit, and ALL `.wild-rabbit` variants start **paused** (`animation-play-state:paused`) and **invisible** (`opacity:0`).
- JS (IntersectionObserver, `threshold:.05` for hero, `.06` for scenes) adds `.live` class to parent section: `.hero`, `.outside`, `.coach`, `.members`, `.sched`, `.freeweek`.
- CSS: `.hero.live .duck { animation-play-state:running; }` and `.live .wild-rabbit .wr-inner, .live .wild-rabbit .wr-ears { animation-play-state:running; }`.
- One-shot — `unobserve()` after fire.
- Reduced-motion users get `.live` immediately.

---

## 3. HERO Wildlife (all inside `<header class="hero">`, absolutely positioned)

### 3.1 Egret (`.egret`) — soaring cross-sky loop
**Markup:** `.egret > .egret-bob > svg` (viewBox `0 0 160 90`). SVG `transform:scaleX(-1)` faces right. `overflow:visible` on svg (wings extend past viewBox top).

**Container:** `position:absolute; top:0; left:0; z-index:2; width:200px; height:180px; display:flex; align-items:center; justify-content:center; pointer-events:none;`

**Layers:**
| Layer | Animation | Details |
|---|---|---|
| `.egret` (container) | `egretFly 34s linear 2s infinite` + `fill-mode:backwards` | Full crossing: -18vw → 118vw with vh-relative altitude |
| `.egret-bob` | `egretBob 4.6s ease-in-out infinite` | Gentle float: translateY 0 → -10px |
| svg | static `scaleX(-1)` | drop-shadow `0 2px 6px rgba(15,27,44,.35)` |
| `.wing-t` | `wingFlapT 1.05s ease-in-out infinite alternate` | `transform-origin:62px 34px`; rotate 16° → -24° |
| `.wing-b` | `wingFlapB 1.05s ease-in-out infinite alternate-reverse` | `transform-origin:62px 36px`; rotate -18° → 20° |

**`egretFly` keyframes** (the Y pattern — all use `calc(vh + 12px - 75px)` base):
```
0%   translate(-18vw, calc(17vh + 12px - 75px)) rotate(0deg);  opacity:0
4%   opacity:1
30%  translate(18vw, calc(9vh + 12px - 75px)) rotate(-1.5deg)
55%  translate(52vw, calc(13vh + 12px - 75px)) rotate(1deg)
80%  translate(84vw, calc(7vh + 12px - 75px)) rotate(-1deg);  opacity:1
96%  opacity:1
100% translate(118vw, calc(10vh + 12px - 75px)) rotate(0deg);  opacity:0
```
**CRITICAL:** If you nudge the flight path, change ALL five Y offsets + reduced-motion settle (`translate(60vw, calc(16vh + 12px - 75px))`) in one pass. Drift causes wobble.

### 3.2 Ducks (`.duck.d1`, `.duck.d2`) — waddle in from left, settle, forage
**Markup:** `.duck > span.waddle > svg` (viewBox `0 0 60 44`). SVG `transform:scaleX(-1)` faces right.

**Container:** `position:absolute; bottom:26px; left:0; z-index:3; opacity:0; animation-play-state:paused; will-change:transform;`
- `.d1` svg `width:52px`; `.d2` svg `width:42px` (trailing duck is smaller).

**Layers:**
| Layer | Animation | Details |
|---|---|---|
| `.duck.d1` | `duckStroll 20s var(--ease) 2s forwards, duckForage 3.5s ease-in-out 22s infinite` | Stroll once, then forage forever |
| `.duck.d2` | same but delays `4.5s` / `24.5s` | 2.5s behind d1 |
| `.waddle` | `waddle .55s ease-in-out 12 alternate, waddleCalm 1.6s ease-in-out 6.6s infinite alternate` | `transform-origin:50% 88%` |
| `.duck.d2 .waddle` | delays `.27s, 6.87s` | phase-shifted |

**Keyframes:**
```
duckStroll: 0% translateX(-8vw) opacity:0 → 4% opacity:1 → 100% translateX(var(--settle)) opacity:1
            (--settle: 15vw for d1, 22vw for d2)
waddle:      from rotate(-7deg) translateY(0)  →  to rotate(7deg) translateY(-2px)
waddleCalm:  from rotate(-1.2deg) → to rotate(1.2deg)
duckForage:  0%,100% translateX(var(--settle,15vw)) translateY(0)
             30%    translateX(var(--settle,15vw)) translateY(-3px)
             65%    translateX(var(--settle,15vw)) translateY(-1.5px)
```

### 3.3 Hero Rabbit (`.rabbit`) — hops in from right, stays
**Markup:** `.rabbit > span.hop > svg` (viewBox `0 0 52 48`). NOT flipped (faces left).

**Container:** `position:absolute; bottom:20px; left:0; z-index:3; opacity:0; animation-play-state:paused; will-change:transform;`
- svg `width:46px`.

**Layers:**
| Layer | Animation | Details |
|---|---|---|
| `.rabbit` | `rabbitIn 10s var(--ease) 6s forwards, rabbitForage 2.8s ease-in-out 16.5s infinite` | Enter once, forage forever |
| `.hop` | `rabbitHop 10s ease-in-out 6s forwards, rabbitIdle 3.2s ease-in-out 16.5s infinite` | `transform-origin:50% 100%` |
| `.ears` (g) | `earTwitch 2.6s ease-in-out infinite` | `transform-origin:24px 12px` |

**Keyframes:**
```
rabbitIn:   0% translateX(96vw) opacity:0 → 8% opacity:1 → 22% 86vw → 38% 79.5vw → 55% 76vw → 100% 74vw opacity:1
rabbitHop:  0%,6% Y:0 → 11% -14px → 16% 0 → 26% -14px → 31% 0 → 42% -14px → 47%,100% 0   (3 hops)
rabbitIdle: 0%,100% scaleY(1) → 50% scaleY(1.025)   (breathing)
earTwitch:  0%,88%,100% rotate(0) → 92% rotate(-9deg) → 96% rotate(5deg)
rabbitForage: 0%,100% translateX(74vw) Y(0) → 15% Y(-2px) → 35% Y(-4px) → 55% Y(-1.5px) → 75% Y(-3px)
```

---

## 4. Scene Rabbits (`.wild-rabbit.wr-*`) — the "extra rabbits"

**Shared base CSS:**
```css
.wild-rabbit { position:absolute; pointer-events:none; z-index:1; will-change:transform; }
.wild-rabbit svg { display:block; width:100%; height:auto; overflow:visible; }
.wild-rabbit .wr-inner { display:block; transform-origin:50% 100%; animation-play-state:paused; }
.wild-rabbit .wr-ears { transform-origin:50% 16%; animation-play-state:paused; }
.live .wild-rabbit .wr-inner, .live .wild-rabbit .wr-ears { animation-play-state:running; }
```

**Shared keyframes:**
```
wrHop:      0%,100% translateY(0) scaleY(1) → 45% translateY(-12px) scaleY(1.04) → 55% translateY(0) scaleY(.98)
earTwitch:  0%,88%,100% rotate(0) → 92% rotate(-9deg) → 96% rotate(5deg)
```

**The pattern per rabbit:** *Enter-once* keyframe (translateX from off-screen + opacity fade + a landing dip) then *wrHop* infinite + *earTwitch* infinite. Delays stagger the entry.

| Variant | Position | Size | Color | Enter (forwards) + loop | Ear delay |
|---|---|---|---|---|---|
| `.wr-hero2` | `left:6%; bottom:16px` | 40px | `var(--stone)` | `wrHero2Enter 9s var(--ease)` + `wrHop 2.5s 9s` | `earTwitch 2.4s .6s` |
| `.wr-air` | inside card: `right:10px; bottom:6px` | 34px | `#C9BCC0` | (no enter) `wrHop 2.6s .8s` | `earTwitch 2.5s 1.2s` |
| `.wr-outside` | `right:4%; bottom:6px` | 44px | `#C9BCC0` | `wrOutsideEnter 10s 1.2s` + `wrHop 2.8s 11.2s` | `earTwitch 2.7s 1s` |
| `.wr-coach` | `left:4%; bottom:12px` | 38px | `var(--stone)` | `wrCoachEnter 9.5s .6s` + `wrHop 2.4s 10.1s` | `earTwitch 2.5s 2s` |
| `.wr-schedule` | `left:5%; bottom:8px` | 40px | `var(--stone)` | `wrScheduleEnter 9s .3s` + `wrHop 2.6s 9.3s` | `earTwitch 2.8s 1.5s` |
| `.wr-freeweek` | `right:6%; bottom:6px` | 36px | `#9A9284` | `wrFreeEnter 9s 2s` + `wrHop 2.5s 11s` | `earTwitch 2.6s .8s` |
| `.rabbit-reviews` | inline after Google link in `.m-more` | normal (38px) | `currentColor` | `reviewsRabbitEnter` + forage | `earTwitch` |

**Enter keyframes** (all: translateX from side, opacity fade, dip at 40-45%, land by 60-65%, hold to 100%):
```
wrHero2Enter:  0% translateX(-140%) opacity:0 → 10% opacity:1 → 40% translateX(0) translateY(-14px) → 60% Y(0) → 100% Y(0) opacity:1
wrOutsideEnter: 0% translateX(120%) opacity:0 → 12% opacity:1 → 45% translateX(0) translateY(-16px) → 65% Y(0) → 100% Y(0) opacity:1
wrCoachEnter:  0% translateX(-140%) opacity:0 → 10% opacity:1 → 42% translateX(0) translateY(-12px) → 62% Y(0) → 100% Y(0) opacity:1
wrScheduleEnter: 0% translateX(-140%) opacity:0 → 10% opacity:1 → 40% translateX(0) translateY(-13px) → 60% Y(0) → 100% Y(0) opacity:1
wrFreeEnter:   0% translateX(120%) opacity:0 → 12% opacity:1 → 45% translateX(0) translateY(-11px) → 65% Y(0) → 100% Y(0) opacity:1
```

**Rabbit SVG anatomy (viewBox 52×48):**
- `.wr-ears` group: two paths, origin `50% 16%`, second ear `opacity:.75`
- Body path `M18 22 C12 24 ... Z` (fill currentColor)
- Head circle `cx16 cy22 r6`, eye `cx14 cy20.5 r1.3 fill #14100A`
- Tail `circle cx45 cy40 r4 fill #F3ECDC`
- Whiskers/legs: `M12 46 L8 46 M34 46 L40 46` stroke currentColor width 3
- Hero rabbit uses hard hex fills (`#9FB0C4` body/ears, `#8B9DB4` inner ear); scene rabbits use `currentColor` so they inherit section color.

---

## 5. PEOPLE

### 5.1 Partner Jumping Jacks (`.jackers`, `#standard`) — the big rig
**Markup hierarchy (the load-bearing structure):**
```html
<div class="jackers" aria-hidden="true">
  <div class="j-tree t1">…svg…</div>   <!-- LEFT flank, optional -->
  <div class="j-tree t2">…svg…</div>
  <div class="jacker a">
    <div class="j-ground"></div>       <!-- shadow -->
    <div class="j-body">               <!-- REST SWAY ONLY -->
      <div class="j-hop">              <!-- VERTICAL HOP ONLY -->
        <span class="j-head"></span>
        <span class="j-torso"></span>
        <span class="j-arm l"></span>
        <span class="j-arm r"></span>
        <span class="j-leg l"></span>
        <span class="j-leg r"></span>
      </div>
    </div>
  </div>
  <div class="jacker b">…same, but animation-delay: 2s everywhere…</div>
</div>
```
**🔴 BANNED: rotate a standing figure into plank ("floating corpse balloons" — Undo'd twice). Upright multi-part rig only.**

**Container geometry:**
```css
.jackers { display:flex; justify-content:flex-start; align-items:flex-end; gap:20px;
           padding:8px 0 10px 0; min-height:450px; pointer-events:none; position:relative; overflow:visible; }
.jackers::after { /* ambient band shadow */ content:""; position:absolute; left:0; width:min(420px,95%);
           bottom:4px; height:6px; border-radius:50%; background:rgba(20,16,10,.1); filter:blur(1.5px); z-index:0; }
.jacker { position:relative; width:120px; height:150px; flex:0 0 auto; overflow:visible; z-index:1; }
```

**Body parts (absolute, all `background:currentColor`, `border-radius:999px` capsules for limbs):**
| Part | Size | Position | Pivot |
|---|---|---|---|
| `.j-ground` | `left:22%; right:22%; height:5px` | `bottom:3px` | ellipse shadow, `rgba(20,16,10,.2)` |
| `.j-body` | `64×130px` | `left:50%; bottom:5px; margin-left:-32px` | `50% 100%` |
| `.j-hop` | `inset:0` | — | `50% 100%` |
| `.j-head` | `22×24px` | `left:50%; top:0; margin-left:-11px` | circle |
| `.j-torso` | `24×42px` | `top:26px; margin-left:-12px` | rounded rect |
| `.j-arm` | `10×46px` | `top:28px` | `50% 6px` (shoulder) |
| `.j-arm.l` | — | `left:14px` | — |
| `.j-arm.r` | — | `right:14px` | — |
| `.j-leg` | `11×58px` | `top:64px` | `50% 4px` (hip) |
| `.j-leg.l` | — | `left:18px` | — |
| `.j-leg.r` | — | `right:18px` | — |

**Colors:** `.jacker.a { color:var(--ink); }` `.jacker.b { color:var(--pine); }` — parts use `currentColor`.

**Rotate sign convention** (y-down, pivot at top of limb, positive = clockwise):
| Limb | Closed | Open (jack) |
|---|---|---|
| Left arm | `+14°` | **`+155°`** |
| Right arm | `−14°` | **`−155°`** |
| Left leg | `+6°` | **`+34°`** |
| Right leg | `−6°` | **`−34°`** |

*Outward = left positive / right negative. Inward is the bug Curtis rejected.*

**Hop:** `translateY(-11px)` on open peak (figure A), `-9px` (figure B).

**45-second timeline** (both figures): 10 jacks (0–44%, ~2s/rep, limbs open/closed with hop on open), settle (44–50%), rest sway with weight shift (50–68%, limbs HOLD closed), buffer closed (68–100%).

**Keyframe generators — the % math per rep (figure A, 45s):**
Reps land at 0%, 4.4%, 8.8%, … 39.6%. Each rep: `closed at X%` → `open at X+1.98%` → `closed at X+4.4%`.
- **A arms:** closed 14°/−14°, open **155°/−155°** at 1.98% after each rep start; hold `44%,100%` closed.
- **A legs:** closed 6°/−6°, open **34°/−34°** same cadence.
- **A hop:** `translateY(0)` at rep start → `-11px` at +1.98% → `0` at +4.4%.
- **B:** same cadence but offsets +0.079%/+2.059% (slightly later within rep), arms 12°→148°, legs 5°→30°, hop `-9px`, whole figure `animation-delay:2s`.

**Sway (rest window):**
```
jSwayA: 0%,50%,68%,100% translateX(0) rotate(0)
        54% translateX(2.5px) rotate(1.2deg)
        59% translateX(-2px) rotate(-1deg)
        64% translateX(2px) rotate(0.8deg)
jSwayB: 0%,50%,68%,100% translateX(0) rotate(0)
        53% translateX(-3px) rotate(-1.4deg)
        58% translateX(2.2px) rotate(1deg)
        63% translateX(-1.5px) rotate(-0.7deg)
        66% translateX(1px) rotate(0.5deg)
```

**🔴 Banned techniques:**
1. `rotate(85-90°)` a standing human into plank — corpse balloons.
2. Two transform animations on one node — last series wins; nest hop inside sway.
3. Non-greedy regex `@keyframes X \{.*?\}` — truncates at first inner `}`; count braces.
4. Timid open angles (±20°) — reads as shivering, not jacks.
5. Absolute trees behind figures — overlaps people; use flex flank.
6. Grep/MD5-only verify for "reads as exercise" — needs Curtis eyes-on.

### 5.2 Jump-Rope Figure (`.ropers`, `#schedule`) — single figure
**Markup:**
```html
<div class="ropers" aria-hidden="true">
  <div class="roper">
    <div class="r-ground"></div>
    <div class="r-stage">            <!-- perspective:420px; perspective-origin:50% 22% -->
      <div class="r-hop">            <!-- 🔴 ROPE GOES INSIDE .r-hop (critical sync rule) -->
        <div class="r-rope"><svg viewBox="0 0 100 130"><path d="M12 60 Q50 218 88 60"/></svg></div>
        <span class="r-handle l"></span><span class="r-handle r"></span>
        <span class="r-head"></span><span class="r-torso"></span>
        <span class="r-arm l"></span><span class="r-arm r"></span>
        <span class="r-leg l"></span><span class="r-leg r"></span>
      </div>
    </div>
  </div>
</div>
```

**🔴 Sync rule (critical):** rope + handles + arms must live INSIDE `.r-hop`. If the rope is a sibling, the body jumps but the rope stays at ground level — broken illusion.

**Geometry:** `.roper` 110×140px, color `var(--ink)`. `.r-stage` 100×130px centered, `perspective:420px; perspective-origin:50% 22%`. Head 20×22px top 4px. Torso 22×38px top 28px. Arms 9×56px top 18px, pivot `50% 4px`, **static** `rotate(∓42deg)` reaching down-out to hand line. Legs 10×68px top 62px, static together. Handles 6×6px `var(--dawn)` at top 60px, left 12px / right 12px — **must match rope path endpoints (12,60 / 88,60)**.

**Rope:** `.r-rope` 100×130px centered `left:50%; margin-left:-50px`, `transform-style:preserve-3d`, `transform-origin:50% 60px` (hand line), `animation:ropeSwing .56s linear infinite`. Path `M12 60 Q50 218 88 60` — half-loop, `stroke:var(--dawn); stroke-width:2.75; stroke-linecap:round; opacity:.92`.

**Motion:**
```
ropeSwing: 0% rotateX(0deg) → 100% rotateX(360deg)   (.56s linear)
ropeHop:   0% translateY(-12px) → 25% 0 → 50% 0 → 75% -6px → 100% -12px   (.56s ease-in-out)
```
**Phase:** 0°/360° = rope under feet = airborne (Y=-12). 180° = rope over head = grounded. Hop duration == rope period (0.56s) — they stay locked.

**Reduce-motion / a11y:** `.ropers, .roper, .r-hop, .r-rope` in kill list. RM: freeze hop/rope transforms, `.ropers{opacity:.9}`.

---

## 6. Trees (`.j-tree.t1/.t2`, flanking the jackers)

**Layout rule:** flex row siblings with the figures — `trees left → gap → jackers`. Never absolute-positioned behind people.

```css
.jackers .j-tree { position:relative; flex:0 0 auto; align-self:flex-end; pointer-events:none;
                   transform-origin:50% 100%; will-change:transform; z-index:0; }
.j-tree.t1 { width:130px; animation:treeSwayA 7.5s ease-in-out infinite; margin-right:6px; }
.j-tree.t2 { width:100px; margin-left:4px; animation:treeSwayB 6.2s ease-in-out .4s infinite; }
.jacker.a { margin-left:28px; }   /* clear air between trees and people */
```

**Sway (gentle — Curtis rejected ±3-4.5° as "too much wind"):**
```
treeSwayA: 0%,100% rotate(-1.2deg) → 50% rotate(1.4deg)
treeSwayB: 0%,100% rotate(1deg) → 50% rotate(-1.6deg)
```

**Tree silhouette language:** flat SVG, `--pine` foliage / `--ink` trunk (t1) or `--stone` trunk (t2). Tall bare trunk (strip lower foliage tiers), narrow apex → wider base, foliage mass shifted leeward (right), opacity steps .95→.8 down the tiers. Ground shadow ellipse `var(--ink)` ~10-12% opacity.

---

## 7. Mobile (max-width:640px)

| Element | Desktop | Mobile |
|---|---|---|
| `.egret svg` | 150px | 104px |
| `.duck svg` | 52px / d2 42px | 40px / d2 33px |
| `.rabbit svg` | 46px | 36px |
| `.jacker` | 120×150px | 92×118px |
| `.j-body` | 64×130 | 50×100 (margin-left:-25px) |
| `.j-head` | 22×24 | 17×18 (margin-left:-8.5px) |
| `.j-torso` | 24×42 | 18×32 (margin-left:-9px) |
| `.j-arm` | 10×46 | 8×36 |
| `.j-leg` | 11×58 | 9×44 |
| `.ropers` | min-height:150px | min-height:120px |
| `.roper` | 110×140 | 88×112 |
| `.r-rope` | 100×130, origin `50% 60px` | 80×104, origin `50% 47px` (hand line moves!) |

Mobile figures remain ANIMATED (only reduced-motion kills them).

---

## 8. Reduced Motion (prefers-reduced-motion)

- Kill list: `.duck, .rabbit, .egret, .egret-bob, .wing-t, .wing-b, .waddle, .hop, .ears, .jackers, .jacker, .j-body, .j-hop, .j-arm, .j-leg, .j-head, .j-torso, .j-tree, .ropers, .roper, .r-hop, .r-rope` → `animation:none !important`.
- Static settles: egret `translate(60vw, calc(16vh + 12px - 75px)) opacity:.9`; ducks `left:15vw/22vw`; rabbit `right:14vw`; jackers `opacity:.9` with limbs at closed angles (`rotate(14deg)/-14deg/6deg/-6deg`), body/hop/trees `transform:none`; ropers `opacity:.9`, hop/rope `transform:none`.
- `.wild-rabbit` variants: `opacity:.7; transform:none !important`.
- Scroll-trigger JS: `if (reduced){ scenes.forEach(s => s.classList.add('live')); return; }`.

---

## 9. Verification Checklist (before shipping new figures)

1. Angle gate strings present: `rotate(155deg)` left-open / `rotate(-155deg)` right-open (not inverted).
2. 10 open peaks + 10 hops per jacker figure.
3. Zero `pusher` / `p-plank` / `rotate(87` remnants.
4. Rope path endpoints == handle positions == arm ends (hands visibly hold rope).
5. Local MD5 == GitHub Contents API body (raw.githubusercontent CDN can lag).
6. **Curtis eyes-on** — "reads as exercise" is the real test. Grep/MD5 is not proof.

---

## 10. What NOT to touch while adding figures

- `#proof` count-up stats, marquee, PayPal, nav, SMS hrefs, sunrise sun/stars/horizon.
- Challenge page (`challenge/index.html`) uses the same wildlife language but orange/ink theme — do not port sunrise tokens there without orders.
- Footer pages use the OLD brand system — leave them.
