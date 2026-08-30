# PLAN.md — BootCampFX Homepage Copy Rewrite (bcfx-copy-rewrite)

> Locked SPEC (verbatim from Phase 0):
> ```
> CORE DECISION THIS DRIVES:
> Ship the BootCampFX homepage sales-copy rewrite from bcfx-copy-rewrite.md so Free Week is the clear front door, Unlimited ($197) is the destination, entry path is consistent, and the Halbert letter converts above the testimonials — without touching theme, nature, wildlife, or workout animations. Challenge page held for a later pass.
>
> IN SCOPE:
> - Homepage only: /Users/macmini/sites/bootcampfx/index.html (local clone) → main → bootcampfx.com
> - 1A Hero: new primary headline + subhead + CTAs per brief
>   "The Best Shape Of Your Life. About $11 A Session. *Outdoors In Fullerton Since 2005.*"
> - 1B Sky section body tighten (cards 01/02/03 stay)
> - 1C Rewrite third "KEPT"/stay card — Free Week first; no $349 ambush
> - 1D Curtis bio — age 20s–80s; lead sentence per brief
> - 1E Letter: MOVE above testimonial grid; delete duplicate hero-style claim from wrong slot; apply marked body changes; Judi + Margaret mid-letter stay
> - 1F Fit/Not Fit — name Chuze on "save your money" first bullet
> - 1G Membership intro — one path stated once; soft Challenge mention only under Unlimited footer
> - 1H FAQ — new first entry "What does starting actually look like?"
> - Part 3 data consistency ON HOMEPAGE ONLY:
>   PT price → $75–$200/session, $600–$2,400/mo everywhere on index
>   Google review count → one true number (verify live/source before write)
>   Member age → 20s–80s
>   Entry path copy: Free Week default; Challenge = soft opt-in only
> - Preserve byte-stable Free Week SMS/form hrefs (inventory before/after)
> - Preserve PayPal slots, plan IDs, theme tokens, sun/stars/horizon, wildlife, jackers, jump-rope, rail, nav structure (href targets may get soft Challenge links only where already natural)
> - Delivery: full planner — SPEC LOCKED → PLAN + COUNTERBATTERY → PLAN APPROVED → Fire → edit + push
> - Markup path: not required unless you order it later
>
> OUT OF SCOPE:
> - challenge/index.html entire page (countdown, math block 2B, value stack, guarantee, final CTA, etc.)
> - Theme / design tokens / fonts / outdoors sunrise shell
> - Nature / wildlife / decorative sun / scene trees
> - Workout animation elements (jackers, roper, etc.)
> - New Challenge push copy (no hard CTAs, no P.P.P.S. Challenge hard-sell, no "claim 20 spots" from homepage)
> - Footer legal pages (contact, privacy, terms, waiver, refund, copyright, faq.html) unless a single shared number forces a one-line sync you explicitly order
> - PayPal plan ID changes / tier sandwich rebuild / grey Starter reintroduction beyond what live already has
> - Branch workflow — ship to main on Fire unless you order a feature branch
> - Any redesign, section deletion beyond letter re-order, or animation work
>
> DATA SOURCES:
> - Brief: ~/.hermes/cache/documents/doc_046d08b3b496_bcfx-copy-rewrite.md (and user paste)
> - Live + git ground truth: /Users/macmini/sites/bootcampfx after git pull --ff-only origin main
> - bootcampfx-website skill: copy-swap.md, offer-markup-pass only if prices collide
> - Verify on disk: current section order, letter location, hero H1, PT price strings, review count, Free Week href inventory, PayPal placeholders
>
> SUCCESS CRITERIA:
> 1. Live index reflects brief homepage sections 1A–1H (copy + letter above testimonials)
> 2. Hero headline is the primary 13-word Best Shape / $11 / since 2005 line (or natural HTML equivalent inside existing hero chrome)
> 3. Free Week is the default start story; no contradictory "you start with Challenge" / $349 ambush on homepage
> 4. Letter sits above testimonial grid; body matches brief marked changes; Halbert voice preserved
> 5. Challenge appears only as soft mention (membership footer / existing soft paths) — no new hard Challenge funnel copy
> 6. PT price strings consistent: $75–$200/session, $600–$2,400/mo; age 20s–80s; one Google count
> 7. Theme fingerprints intact: sun/stars/horizon + wildlife + jackers/roper greps unchanged in character
> 8. Free Week SMS/form hrefs byte-equal before/after
> 9. PayPal Unlimited path still present and functional (no broken slots)
> 10. Local MD5 == raw.githubusercontent main index.md5; live string fingerprints for new hero + letter lead + FAQ opener
> 11. Visual: outdoors sunrise still reads as outdoors sunrise — eyes-on / your call on "theme untouched"
> 12. No challenge/index.html diff in the ship commit
> ```

**Theme / animation lock (reconfirmed 2026-07-27):** Outdoor sunrise shell, tokens, fonts, stars/sun/horizon, wildlife, jackers, jump-rope, rail reveals — **zero CSS/HTML structure change**. Copy + DOM order of `#letter` only.

---

## 1. Frame & Hypothesis

**Frame:** Live homepage already runs the $197 Unlimited offer and a full Halbert letter, but still leads with the old 24-word $1,200 hero, keeps the letter *below* testimonials + Honest Filter, and the KEPT card still says visitors start with the 6-Week Challenge. Those three contradictions cost more than missing micro-copy. Challenge page stays dark this pass.

**Hypothesis:** If we (a) replace the hero with the Best Shape / $11 line, (b) fix KEPT + membership + FAQ entry path to Free Week default, and (c) move the letter above `#members` with brief-marked tightening — while freezing theme/animations and Soft-only Challenge mentions — then the homepage will read as one path (Free Week → Unlimited) and convert without a theme risk or challenge-page scope leak.

**Ground truth (pulled main `b866859`, 2026-07-27):**
- Order now: hero → proof → marquee → `#outside` → `#standard` → `#coach` → `#members` → `#honest` → gold marquee → **`#letter`** → `#freeweek` → `#membership` → `#schedule` → `.faq`
- Hero H1 still: “Why This Fullerton Trainer / Keeps Talking People Out Of / Paying Him $1,200 A Month”
- KEPT card still: “You start with the 6-Week Challenge…”
- Letter already largely v4-craft; review count live string “30+” on members link
- Membership: PT decoy $600–$2,400 + Unlimited $197 PayPal live
- Prior ops files exist (`_ops/PLAN-BootCampFX-v4-markup…` etc.) — this plan converges on homepage copy only; does not re-open offer sandwich rebuild

**Target DOM order after move:**
hero → proof → marquee → outside → standard → coach → **`#letter`** → members → honest → gold marquee → freeweek → membership → schedule → faq  
(Coach stays before letter for trust; coach was not deleted.)

---

## 2. Primitives Touched

- [ ] `/Users/macmini/sites/bootcampfx/index.html` — **only file in ship commit**
- [ ] Brief: `~/.hermes/cache/documents/doc_046d08b3b496_bcfx-copy-rewrite.md`
- [ ] Free Week href inventory (re-capture pre/post; known good phone `+16572170820`)
- [ ] `git` main on `curtisfx/bootcampfx`
- [ ] Verify: local MD5, `raw.githubusercontent.com/.../main/index.html`, live string greps
- [ ] Ops log: this PLAN under `_ops/` (optional commit with index or leave untracked)

**Not touched:** `challenge/index.html`, footer legal pages, CSS token blocks, wildlife/jacker/roper markup, PayPal plan IDs, theme.

---

## 3. Execution Prompts

### Step 0: Pre-Fire snapshot + inventory
**Action tier:** FREE (after PLAN APPROVED + Fire)  
**Prompt:**  
`cd /Users/macmini/sites/bootcampfx && git pull --ff-only origin main`. Capture:
1. Full Free Week SMS + form href list via Python (unmasked from file bytes — do not trust tool-masked output).
2. Counts: `egret|duck|wild-rabbit|jacker|roper|hero-stars|id=\"horizon\"|paypal-unlimited|P-5LX3921079692330VNGW67ZI` (or whatever plan ID is on disk).
3. Section start line map for `#letter`, `#members`, `#honest`, `#coach`, `#standard`.
4. Git commit safety snapshot of working tree if dirty only on `_ops` (leave untracked ops alone).

**Verification gate:** Inventory file written; architecture counts recorded for post-diff equality (SUCCESS #7–9).

### Step 1: Hero (1A)
**Action tier:** FREE after Fire  
**Prompt:** Inside existing `.hero-in` chrome only:
- Replace H1 line-stack with brief primary (preserve `.lm`/`.lmi` animation wrappers if present — **text only inside**, do not remove line-mask CSS):
  - Line ideas that fit chrome: “The Best Shape Of Your Life.” / “About $11 A Session.” / em “Outdoors In Fullerton Since 2005.”
- Subhead per brief: fifteen sessions, same coach since 2005, first week free, no card/contract/script.
- Add primary Free Week CTA using **exact existing** Free Week `sms:` href from inventory (Pattern A). Secondary text line under button: text FREE WEEK to (657) 217-0820.
- Do **not** put $1,200 in the hero. Do not rebuild stars/sun/horizon/wildlife.

**Verification gate:** SUCCESS #2; hero no longer contains “Paying Him $1,200”; Free Week href byte-equal to inventory (SUCCESS #8).

### Step 2: Outside lede (1B)
**Action tier:** FREE after Fire  
**Prompt:** Tighten `#outside` `.sec-lede` to brief 1B body. Keep three why-cards (ELEMENTS / PEOPLE / CLIMATE or live equivalents) **structure and any nested wildlife (e.g. wr-air) untouched** — text nodes only.

**Verification gate:** New lede greppable; `wr-air` / why-grid structure count unchanged.

### Step 3: KEPT card (1C) — highest revenue path fix
**Action tier:** FREE after Fire  
**Prompt:** Replace KEPT card body with brief Free Week stay copy. **Must remove** “You start with the 6-Week Challenge” and any $349 ambush. Optional one soft clause that Challenge exists via nav/membership only if it stays soft — prefer brief text that does not hard-sell Challenge.

**Verification gate:** SUCCESS #3 — `grep -n 'start with the 6-Week\|\$349' index.html` → zero on homepage (or only soft membership under line if any).

### Step 4: Coach bio (1D)
**Action tier:** FREE after Fire  
**Prompt:** Align bio to brief: lead with “Two decades…”, keep 20s–80s, guarantee sentence. **Do not touch** `.wild-rabbit.wr-coach` or coach layout CSS.

**Verification gate:** Age range 20s–80s present; coach rabbit count unchanged.

### Step 5: Move letter above testimonials (1E structure)
**Action tier:** FREE after Fire  
**Prompt:** DOM-move entire `<section class="letter" id="letter" …>…</section>` to sit **immediately after** `</section>` of `#coach` and **before** `#members`. Do not move gold marquee with it unless required for spacing; preferred final order per Frame. Use Python slice move — not rewrite from scratch — to preserve letter internals as baseline, then apply Step 6 text patches.

**Verification gate:** SUCCESS #4 structural — `index.html` order: coach … letter … members … honest. No duplicate `#letter`.

### Step 6: Letter copy tighten (1E body)
**Action tier:** FREE after Fire  
**Prompt:** Apply brief-marked letter changes on the moved block:
- H2 → “I Talk People Out Of Paying Me $1,200 A Month” (or exact brief)
- Sub → “(And into a $197 plan that works faster.)”
- Body patches per brief (math table, frequency, cheap/why, guarantee, cap 12/mo, CTAs)
- Keep Judi Heylek + Margaret Martinazzi mid-letter blocks if present
- **P.P.P.S. Challenge hard-sell: OMIT** per SPEC (soft Challenge only). No “Want a deadline… 6-Week Challenge” hard close unless reduced to one soft clause matching membership under — prefer omit.
- Free Week interrupt CTA: reuse inventory SMS href only
- Do not invent PayPal buttons inside letter; existing `#membership` subscribe link OK

**Verification gate:** SUCCESS #4–5; letter H2 greppable; no new hard Challenge CTA strings from brief P.P.P.S.

### Step 7: Honest Filter Chuze (1F)
**Action tier:** FREE after Fire  
**Prompt:** First “Save your money” bullet → name Chuze per brief. Leave other bullets.

**Verification gate:** `Chuze` present once in `#honest`.

### Step 8: Membership intro + soft footer (1G)
**Action tier:** FREE after Fire  
**Prompt:** Rewrite membership lede to brief “One offer / one honest comparison” path (Free Week → $197). Under Unlimited / `.under`: soft Challenge link OK as already live (`/challenge/`). No new spots/countdown language. **Do not** change tier prices, grey decoy structure, or PayPal render JS.

**Verification gate:** SUCCESS #5–6, #9; PayPal slot + plan ID strings unchanged.

### Step 9: FAQ first entry (1H)
**Action tier:** FREE after Fire  
**Prompt:** Insert as **first** `.fqi` (or live FAQ item pattern) “What does starting actually look like?” per brief. Preserve accordion JS classes (`.fq`/`.fa`).

**Verification gate:** SUCCESS #1 FAQ opener greppable as first question.

### Step 10: Sitewide homepage data pass (Part 3)
**Action tier:** FREE after Fire  
**Prompt:** Grep index for PT prices, ages, review counts. Normalize:
- PT: `$75–$200` / `$600–$2,400` only (delete any `$80–100` or lone `$1,200/mo` as the only PT figure outside letter rhetorical $1,200 attack lines — letter may keep “$1,200” as rhetorical contrast per brief)
- Age: 20s–80s / 20–80 as appropriate
- Google count: keep live truth (currently **30+** on members link) — do not invent 20+
- Session length: leave Margie quote; elsewhere 45 min

**Verification gate:** SUCCESS #6.

### Step 11: Architecture equality + commit + push
**Action tier:** FREE after Fire (push is the ship)  
**Prompt:**
1. Re-run architecture counts vs Step 0 — must match for wildlife/jackers/roper/sun/horizon/paypal.
2. Free Week href set equality (Python bytes).
3. `git diff --stat` → **only** `index.html` (plus this PLAN only if you elect to add `_ops` — default **index.html only**).
4. Commit message: `Homepage copy rewrite — Free Week path, letter above testimonials, hero $11 (theme locked)`
5. `git push origin main`
6. Wait ~30–60s; MD5 local == raw; live greps:
   - `Best Shape Of Your Life` or `$11 A Session`
   - `I Talk People Out Of Paying Me` (letter H2)
   - `What does starting actually look like`
   - `Chuze`
   - NOT `You start with the 6-Week Challenge`
7. Confirm `git show --stat HEAD` has no `challenge/`

**Verification gate:** SUCCESS #7–12.

### Step 12: SITREP + eyes-on handoff
**Action tier:** FREE  
**Prompt:** Report commit SHA, what moved, theme lock confirmation, soft Challenge only, ask Chesty for hard-refresh eyes-on (SUCCESS #11). No self-fix theme if he flags visual drift — ⚠️ report only.

**Verification gate:** Phase 3 VERIFY uses SPEC criteria word-for-word.

---

## 4. Constraints

- **Theme lock absolute** — no token, font, sun keyframe, wildlife, jacker, roper, or decorative sun edits
- **Homepage only** — zero `challenge/index.html`
- **Soft Challenge only** — no brief P.P.P.S. hard Challenge CTA; no 20-spot / countdown language on homepage
- **Free Week hrefs byte-stable**
- **PayPal Unlimited untouched** (markup/plan ID/render)
- **No offer sandwich rebuild** — live $197 + PT decoy stays; this is copy-swap class not offer-markup-pass unless prices collide mid-edit (they should not)
- **Main only on Fire** — no feature branch unless ordered
- **PII:** never paste live SMS with wrong masked phone; write known `+16572170820` from standing knowledge when constructing, verify via Python on file bytes
- **One approval = Fire** unlocks Steps 0–12 as a single execution batch

---

## 5. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Letter DOM move breaks CSS adjacent siblings / reveal order | M | M | Move whole section node; keep classes; visual check after push |
| Hero line-mask `.lm` expects 3 short lines; new headline wraps ugly on mobile | M | M | Keep 3-span stack matching brief periods; mobile clamp already on `.hero h1` |
| Soft Challenge vs brief P.P.P.S. conflict during letter edit | L | M | SPEC wins: omit hard P.P.P.S. |
| Accidental wildlife/rabbit delete when slicing DOM | M | H | Step 0 counts; abort push if counts drop |
| Free Week href drift via copy-paste mask | M | H | Byte inventory equality gate |
| Scope leak into challenge page “while we’re here” | L | H | Diff allowlist index.html only |
| Letter content already close to brief → over-edit damages Halbert voice | M | M | Prefer surgical patches; unmarked body stays |

---

## 6. Owner Table

| Role | Name | Responsibility |
|------|------|----------------|
| Plan Author | Drago | Plan, gates, COUNTERBATTERY |
| Approver | Chesty (Actual) | PLAN APPROVED + Fire |
| Executor | Drago (on-box) | index.html edit + push |
| Verifier | Drago + Chesty eyes-on | SPEC criteria + theme call |
| Logger | Drago | kaizen after verify |

---

## 7. COUNTERBATTERY

### Fatal Flaw

**The plan treats “move the letter” as a pure cut-paste, but the live page’s conversion spine was built *around* letter-after-honest.** Testimonials + Honest Filter currently pre-load skepticism *before* the long argument. Moving the letter up may put 1,400 words on mobile screen two — exactly the casualty Vlad’s half-right advice risked — while the brief claimed shortening above the letter would fix that. **This plan does not shorten proof/marquee/outside/standard/coach enough to guarantee the letter arrives early without a mobile wall.** If mobile bounce spikes, the structural win becomes a structural loss, and the theme-lock constraint prevents the usual “add sticky jump / collapse letter” escape hatches without another SPEC.

### Attack Per Execution Step

**Step 0 (inventory):** Will fail if tool-masked phones get written back into hrefs, silently breaking SMS. Condition: any path that copies from `read_file` tool output instead of raw file bytes.

**Step 1 (hero):** The `.lm`/`.lmi` staggered line mask was designed for the long $1,200 accusation headline. Forcing “Best Shape / $11 / Since 2005” into the same three masks can look like three orphan fragments, not one thesis — and the brief’s “13 words one pass” dies inside animation chrome. Also: adding a CTA that isn’t there today changes hero density; Chesty may read that as “theme” even if CSS is untouched.

**Step 2–4 (outside/KEPT/coach):** KEPT rewrite is the real money move — and it’s a one-paragraph replace. If the executor “softens” Challenge so hard that long-stay social proof dies, you trade one contradiction for a bland card. Coach is already mostly on-brief; touching it risks rabbit DOM collateral for near-zero gain.

**Step 5 (DOM move):** Highest mechanical kill-shot. A single off-by-one slice duplicates the letter, drops `#members`, or orphans the gold marquee. Regex HTML move on a 128KB file **will** fail if comments/wildlife inside coach aren’t bounded by exact `</section>` for `#coach`. Guaranteed fail condition: non-greedy match on nested divs inside coach rabbit SVG paths mis-identified as section end.

**Step 6 (letter body):** Live letter is already v4-craft. “Apply marked changes” without a line-by-line diff against live will either no-op (false success) or overwrite Judi/Margaret placement. Omitting P.P.P.S. per SPEC while the brief calls it “the only place Challenge should appear” creates brief-vs-SPEC dissonance the executor may “fix” by adding Challenge back — SPEC violation.

**Step 7–9:** Chuze name-drop can read as petty or local-only; FAQ insert can break accordion if wrapper class wrong. Low kill risk, medium embarrassment risk.

**Step 10 (data pass):** Rhetorical `$1,200` in letter H2 vs “normalize PT prices” is easy to over-correct — wiping the letter’s attack line while “fixing consistency,” gutting the Halbert turn.

**Step 11 (push):** CDN lag produces false “not live” and triggers a second panicked push that includes accidental challenge edits. Raw MD5 gate mitigates only if executor waits.

### Mortal Risks Not Captured in Section 5

1. **Convergence debt:** Multiple `_ops` v2/v3/v4 markup plans already argued offer geometry. Shipping “copy rewrite” without Curtis eyes on a rendered preview may reopen the offer war (“why didn’t you grey Starter / change sandwich?”). This plan explicitly refuses sandwich work — Chesty must accept live tiers as-is.
2. **Hero without dual CTA history:** Sticky mobile CTA already exists; hero CTA add may duplicate Free Week noise.
3. **Success criterion #11 is subjective.** Greps can all pass while Chesty says “you changed the feel” because headline tone shifted from fight-club accusation to price-forward fitness claim — **inside the same sunrise chrome**. That is not a theme break by SPEC, but it can still earn an Undo.
4. **No A/B.** Primary headline ships cold. Alternate (21 Years…) was designed for warm traffic and might have been safer; SPEC locked primary anyway.

### Verdict

**Survives COUNTERBATTERY?** YES — with eyes open.

We proceed because the three revenue killers (hero contradiction, KEPT Challenge ambush, letter buried) are confirmed on disk at `b866859` and are copy/order fixes inside a frozen shell; we accept mobile-letter-length risk and subjective “feel” risk as the cost of not leaving the two front doors fighting. Mitigation baked in: whole-section DOM move only, architecture count gates, SPEC-omit hard Challenge P.P.P.S., index.html-only diff, and **no push until PLAN APPROVED + Fire**.

---

## Approval gate

Reply **PLAN APPROVED** to accept this plan.  
Reply **Fire** (after or with approval) to execute Steps 0–12.  
**COUNTERBATTERY FAIL** if the self-attack was too weak — I rewrite harder, no defense.

I will not edit `index.html` or push until **Fire**.
