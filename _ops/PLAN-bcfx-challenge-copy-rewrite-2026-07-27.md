# PLAN.md — BootCampFX Challenge Page Copy Rewrite (+ homepage polish)

> Locked SPEC (verbatim from Phase 0):
> ```
> CORE DECISION THIS DRIVES:
> Finish the bcfx-copy-rewrite on the Challenge page so Free Week remains homepage front door, Challenge is the deadline/scoreboard upgrade with honest deposit math (no fake countdown, no franchise value stack), and homepage gets the two brief polish lines left open (1G $349 footer + letter P.P.P.S.). One path, three speeds, arithmetic a sharp prospect can't tear up.
>
> IN SCOPE:
> A) challenge/index.html — full Part 2:
>    - 2A Hero: deposit reframe; KILL countdown timer UI + JS; KEEP “of 20 spots left” real cap
>    - 2B NEW math block immediately after hero ($349 door; stay → $349 credits as $197 month-1 + $152 month-2; ~10 weeks framing adjusted to match; Free Week alternate door link home)
>    - 2C Truth section tightening pass (brief); honest only because countdown is dead
>    - 2D How it works — keep as written
>    - 2E Bio age → 20s–80s
>    - 2F Cut $624 value stack entirely; honest offer list; $19/session math; Text CHALLENGE CTA
>    - 2G Guarantee: refund OR membership credit, never both; condition = do the program
>    - 2H Fit age 20–80
>    - 2I Final CTA tighten (keep force of close)
>    - Part 3 on challenge: PT $75–$200 / $600–$2,400; delete $80–$100; Google count align to homepage truth (30+); age 20s–80s; entry path = upgrade not only door
> B) Homepage polish only (index.html):
>    - 1G `.under` footer → brief line with $349 + credits-back + Free Week link
>    - 1E letter add soft P.P.P.S. Challenge link per brief (only Challenge hard-ish mention in letter)
> C) Preserve byte-stable where possible:
>    - Challenge PayPal slot/plan IDs currently charging $349 — DO NOT change plan ID or charge amount without Chesty-supplied new plan
>    - Existing SMS challenge href pattern; inventory before/after
>    - 20-spot cap copy/logic that is real (seats-left) — keep; remove only countdown-to-date fake urgency
> D) Dead CSS/JS cleanup for removed countdown (two-ask trap)
> E) Delivery: SPEC → PLAN + COUNTERBATTERY → PLAN APPROVED → Fire → push main
> F) Files in ship: challenge/index.html + index.html only
>
> OUT OF SCOPE:
> - Homepage theme / wildlife / jackers / sunrise tokens (no revisiting 4c4490b architecture)
> - Repricing Challenge off $349 unless Chesty amends SPEC with new PayPal plan ID + amount
> - Grey Starter / Unlimited sandwich rebuild
> - Footer legal pages except optional one-line refund policy sync if you order it later (not this ship)
> - Fake scarcity timers, value-stack theater, franchise-style $624 tables
> - Changing membership $197 price
> - Feature branch unless ordered
>
> DATA SOURCES:
> - Brief: bcfx-copy-rewrite.md (cache doc + prior paste)
> - Live: /Users/macmini/sites/bootcampfx/challenge/index.html + index.html after git pull
> - Ground truth now: $349, PayPal challenge present (P-* ids), countdown #cd-days/hours/mins, seats-left, stack $624, bio 30s–70s, SMS CHALLENGE body
> - Homepage HEAD 4c4490b already has Free Week path; polish only 1G + P.P.P.S.
> - Phone CTAs: (657) 217-0820 / +16572170820 from file bytes (never tool-masked rewrite)
>
> SUCCESS CRITERIA:
> 1. Live /challenge/ has no cohort countdown timer (no cd-days/hours/mins ticking; dead CSS/JS removed or inert with markup gone)
> 2. Hero sells deposit reframe: $349 isn’t a fee — credits on stay; proof or money back
> 3. Math block present after hero; states stay credit as $197 + $152 (full $349) OR exact SPEC dollars; Free Week alternate linked
> 4. No $624 / fake value stack on challenge page
> 5. Guarantee states refund XOR credit, never both
> 6. Age 20s–80s / 20–80; PT prices $75–$200 and $600–$2,400 only (no $80–$100 as PT rate)
> 7. Google review count on challenge matches homepage (30+)
> 8. 20-spot cap retained; CTAs include Text CHALLENGE path; PayPal $349 path still works (same plan ID)
> 9. Homepage: 1G under-line has $349 + credit language; letter has P.P.P.S. to /challenge/
> 10. challenge + index only in commit; local MD5 == raw for both files; live string fingerprints
> 11. Challenge page still reads as challenge (orange) theme — copy/structure, not sunrise port
> 12. Eyes-on Chesty: no timer; deposit math readable on mobile
> ```

**Dollar lock (from SPEC):** Sticker **$349** unchanged (PayPal `amount.value = '349.00'`). On stay, credit **full $349** = **$197 month-1 Unlimited + $152 toward month-2**. Not “first month only” when $349 > $197.

---

## 1. Frame & Hypothesis

**Frame:** Homepage Free Week path shipped (`4c4490b`). Challenge page still runs a countdown the truth section mocks, a $624 value stack, PT at $80–100, age 30s–70s, review “20+”, and credit copy that claims “entire $349 → first month” (impossible against $197/mo). Those holes are Problem 2–3 from the brief.

**Hypothesis:** If we kill the timer, promote deposit+split credit math, replace the value stack with honest coverage, lock refund XOR credit, fix Part 3 strings, and close homepage 1G + letter P.P.P.S., Challenge becomes a coherent *upgrade door* without breaking the $349 PayPal capture or the orange page shell.

**Ground truth (disk):**
- PayPal: one-time `capture` order `349.00` (not subscription plan ID) + `#paypal-challenge`
- Countdown: `#cd-days/hours/mins` + `tick(); setInterval(tick, 30000)`
- Seats: `SPOTS_LEFT = 8`, `SPOTS_TOTAL = 20` — **keep**
- Cohort date labels: keep Monday auto-calc for final CTA
- SMS challenge body already present — preserve from file bytes

---

## 2. Primitives Touched

- [ ] `/Users/macmini/sites/bootcampfx/challenge/index.html`
- [ ] `/Users/macmini/sites/bootcampfx/index.html` (1G + P.P.P.S. only)
- [ ] Brief + this PLAN under `_ops/`
- [ ] git main push; raw + live verify both URLs

---

## 3. Execution Prompts

### Step 0: Prefire inventory
**Action tier:** FREE after Fire  
**Prompt:** `git pull --ff-only`. Snapshot bak of both HTML files. Inventory from **file bytes**: all `sms:` hrefs, tel hrefs, PayPal client-id + `349.00` createOrder block, form URLs, counts of `.stack`, `cd-days`, `SPOTS_`, wildlife N/A on challenge. Record MD5s.

**Verification gate:** Inventory JSON written; PayPal still 349.00 baseline (SUCCESS #8).

### Step 1: Kill countdown (2A structure)
**Action tier:** FREE after Fire  
**Prompt:** Remove countdown markup (`.count` / `#cd-days` / `#cd-hours` / `#cd-mins`) from cohort aside. Remove `tick` + `setInterval` JS. Keep `#cohort-date`, seats bar, c-list. Grep CSS for `.count` countdown rules — if unused after removal, delete dead CSS (two-ask trap). Do **not** remove seats logic.

**Verification gate:** SUCCESS #1 — no cd-* ids; no setInterval(tick); seats-left still updates.

### Step 2: Hero deposit copy (2A)
**Action tier:** FREE after Fire  
**Prompt:** Replace H1/lede with brief deposit reframe:
- H1: Six weeks from now you'll have proof. *Or you won't have paid a thing.* (minor punct. OK)
- Sub-block: **Your $349 isn't a fee. It's a deposit on your membership.** + 18 sessions, measured day 1/42, money back if no move, **and if you stay entire $349 credits** as **$197 first Unlimited month + $152 toward month two** (SPEC math — not “first month” alone).
- Hero proof: 4.9★ · **30+** Google reviews
- CTAs unchanged targets (#enroll / #how)

**Verification gate:** SUCCESS #2, #7.

### Step 3: Math block (2B)
**Action tier:** FREE after Fire  
**Prompt:** Insert new section immediately after `</header>` (before proof strip or after proof — SPEC says after hero; **prefer after header, before proof strip** for “right after hero”). Content per brief + SPEC dollars:
- $349 for six weeks / 3× week measured both ends
- Stay → $349 covers month 1 ($197) + $152 to month 2
- What $349 buys list including first membership month credit path
- Compare to ~$460 for ~10 weeks membership framing **adjusted** so arithmetic matches $197+$152+$349 path honestly (do not claim false $460 if numbers don't line up — prefer: six weeks Challenge + month 1 + partial month 2 covered by the same $349)
- Free Week alternate → `https://bootcampfx.com` or `/`
- Minimal CSS: reuse `.truth`/`.wrap` or light `.math-block` class matching challenge tokens (orange theme) — **no sunrise port**

**Verification gate:** SUCCESS #3, #11.

### Step 4: Truth tighten (2C)
**Action tier:** FREE after Fire  
**Prompt:** Apply brief 2C wording pass. Keep countdown *as indictment of franchises* only — page no longer runs one.

**Verification gate:** SUCCESS #1 + truth still strong.

### Step 5: Bio + fit ages (2E, 2H)
**Action tier:** FREE after Fire  
**Prompt:** Bio 30s–70s → **20s–80s**. Fit “30–65 (or a young 74)” → **20 to 80** per brief.

**Verification gate:** SUCCESS #6.

### Step 6: Offer — cut value stack (2F)
**Action tier:** FREE after Fire  
**Prompt:** Delete `.stack` / stack-total / was $624. Replace with honest list from brief. Price row: **$349** one payment. Per session **~$19** (or $19). PT comparison **$75 to $200** — delete $80–100. Credit line must match SPEC split ($197 + $152), not “first month” only. Keep `#paypal-challenge` + SMS enroll-fallback **href byte-stable** from inventory. Keep createOrder `349.00`.

**Verification gate:** SUCCESS #4, #6, #8.

### Step 7: Guarantee (2G)
**Action tier:** FREE after Fire  
**Prompt:** Rewrite seal per brief: do the program; **either refund or credit forward, never both**, reader choice. Align FAQ guarantee answer if it contradicts.

**Verification gate:** SUCCESS #5.

### Step 8: Final CTA (2I) + Part 3 sweep
**Action tier:** FREE after Fire  
**Prompt:** Tighten final close per brief; keep cohort Monday dynamic date if still used. Sitewide on challenge file: 20+ → 30+ reviews; any remaining $80–100 PT; $624 gone.

**Verification gate:** SUCCESS #6–7, #12 readiness.

### Step 9: Homepage polish (1G + 1E P.P.P.S.)
**Action tier:** FREE after Fire  
**Prompt:** `index.html` only:
1. `.under` → brief: Free Week link (existing FW sms href from file) + **6-Week Challenge $349**, guaranteed in writing, credits back when you stay (mention credit consistently with challenge: full $349 as $197+$152 or short “credits to membership”).
2. After letter P.P.S., add **P.P.P.S.** with link `/challenge/` per brief.
3. No theme/animation touches. Architecture counts for wildlife/jackers/paypal-unlimited must match preflight.

**Verification gate:** SUCCESS #9; homepage arch counts unchanged.

### Step 10: Commit, push, verify
**Action tier:** FREE after Fire  
**Prompt:**
- Diff allowlist: `challenge/index.html` + `index.html` only
- Commit: `Challenge copy rewrite — deposit math, kill countdown, cut value stack; homepage 1G+P.P.P.S.`
- Push main
- MD5 local==raw both files
- Live greps challenge: deposit / no cd-days / no $624 / $75 / 30+ / 20s / either refund or credit
- Live greps home: P.P.P.S. / $349 credits
- PayPal createOrder still 349.00

**Verification gate:** SUCCESS #1–11 automated; #12 Chesty eyes-on.

### Step 11: SITREP
**Action tier:** FREE  
**Prompt:** SHA, what died (timer/stack), dollar story, PayPal intact, undo path. Kaizen append.

**Verification gate:** Phase 3 close.

---

## 4. Constraints

- $349 PayPal capture amount immutable without new SPEC
- Credit copy must be **$197 + $152**, not “$349 = first month” alone
- Countdown dead; 20-spot real cap live
- Orange challenge theme only — no homepage sunrise port
- SMS/tel hrefs from file bytes only
- index.html polish only — no hero/KEPT regression
- Main push on Fire after PLAN APPROVED

---

## 5. Risks & Mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Removing .count CSS breaks unrelated counters (countup proof) | M | H | Scope CSS delete to countdown cohort only; keep `.countup` |
| Math block arithmetic still challengeable | M | M | Use SPEC split only; avoid false $460 if inconsistent |
| Homepage P.P.P.S. fights soft-Challenge prior SPEC | L | L | This SPEC explicitly adds it |
| PayPal SDK race after script edit | L | H | Keep DOMContentLoaded wrapper; don't touch client-id |
| seats JS null-refs if IDs removed by mistake | M | H | Only remove cd-*; test seats-left present |

---

## 6. Owner Table

| Role | Name | Responsibility |
|------|------|----------------|
| Plan Author | Drago | PLAN + gates |
| Approver | Chesty | PLAN APPROVED + Fire |
| Executor | Drago | Edit + push |
| Verifier | Drago + Chesty eyes-on | SPEC criteria |
| Logger | Drago | kaizen |

---

## 7. COUNTERBATTERY

### Fatal Flaw

**The credit story is still easy to attack in operations even if copy is clean.** Live membership is $197/mo via PayPal subscription. Promising “$152 toward month two” requires Curtis to *actually apply* a manual credit/discount in PayPal or cash handling. If ops only ever waived month one, the page lies. The plan ships marketing math without an ops runbook or refund-policy page update (explicitly OUT OF SCOPE). **This WILL fail trust if the first convert asks for the $152 and the desk only knows “first month free.”**

### Attack Per Step

**Step 0:** Masked SMS rewrite corrupts challenge enroll href — page texts wrong body.  
**Step 1:** Deleting `.count` CSS kills proof strip or other counters → visual breakage. `getElementById('cd-days')` left in JS → console errors every 30s if markup gone but tick remains (partial edit).  
**Step 2:** Hero becomes a wall of deposit math on mobile — brief warned about mobile walls; stuffing $197+$152 into hero+sub duplicates math block and bounces thumbs.  
**Step 3:** “After hero” placement before proof strip pushes authority stats down; or after proof weakens “do not skip math.” Either way wrong for someone. Ten-week / $460 framing from brief **conflicts** with $197+$152 split — executor who pastes brief verbatim reintroduces bad arithmetic (COUNTERBATTERY: brief 2B and SPEC dollars are not identical).  
**Step 6:** Removing stack without redesign leaves empty `.offer-card` padding; “first month” credit string left in FAQ while offer says split → internal contradiction.  
**Step 7:** “Refund or credit never both” vs PayPal already captured — credit path is operationally undefined on a one-time capture.  
**Step 9:** P.P.P.S. hard-sells Challenge on a homepage that just trained Free Week-first — reopens two-door confusion if wording is greedy.  
**Step 10:** CDN lag on `/challenge/` path differs from home; false fail → double push.

### Mortar Rounds (extra)

1. **SPOTS_LEFT = 8 hardcoded** is also a trust landmine if unmaintained — plan keeps it as “real cap” without verifying Curtis updates it.  
2. **Existing credit line already overclaims** (“entire $349 → first month”). Fixing it to $197+$152 is more honest and **less** sexy than the lie — conversion may drop while integrity rises.  
3. Challenge page already has sunrise-ish hero-sun/horizon — “don't port sunrise” is fine, but large CSS deletes can still shift orange layout.

### Verdict

**Survives COUNTERBATTERY?** YES — with eyes open.

We proceed because the timer/value-stack/PT-price contradictions are on-disk facts and cheaper to fix than another week of smart prospects bouncing; we accept **ops credit discipline** as Chesty's desk problem and state $197+$152 explicitly so the page stops promising impossible “$349 = one $197 month.” Math block will follow **SPEC dollars over brief $460 paste** when they conflict. Seats + PayPal 349.00 frozen. No push until **PLAN APPROVED + Fire**.

---

## Approval gate

Reply **PLAN APPROVED** then **Fire** (or both).  
**COUNTERBATTERY FAIL** → I attack harder, no defense.

No HTML edits until **Fire**.
