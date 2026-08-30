# PLAN.md — BootCampFX.com Offer + Sales Copy Swap (Theme Locked)

> **Phase:** 1 — PLAN  
> **Date:** 2026-07-26  
> **Status:** Awaiting Actual approval  
> **Deploy target:** bootcampfx.com only (GH Pages `main`)  
> **Theme:** OUTDOORS SUNRISE — DO NOT TOUCH chrome  

> Locked SPEC (verbatim from Phase 0, as amended):
> ```
> CORE DECISION THIS DRIVES:
> Ship bootcampfx.com (GitHub Pages only) so the only rational paid path is
> $197 Unlimited — narrative + offer swap off $249/$299/$429 — outdoors theme
> unchanged.
>
> IN SCOPE:
> - index.html only → bootcampfx.com (GH Pages main)
> - COPY: Halbert letter / headline words inside existing outdoor hero shell
>   (H1 may become “Why I Turn Down $1,200-A-Month Clients” as text only)
> - Mechanism described without naming “The Frequency Effect”
> - Free Week CTA ABOVE pricing (not a tier); existing SMS + form hrefs unchanged
> - KEEP all existing Free Week buttons (SMS + form). Do not remove, restyle
>   off-brand, or change href/sms targets. May reposition block above pricing
>   sandwich only if needed so Free Week is not a tier card.
> - Offer sandwich only:
>   Starter $97 grey “Not available online”
>   Unlimited $197 “Most Popular” — only live checkout
>   PT $600–$1,200/mo grey “Waitlist only — text Curtis”
> - Grey click → scroll to Unlimited
> - Under $197: PayPal plan P-5LX… + SMS fallback + hosted PayPal backup URL
> - Post-pay: SMS to Curtis with name + phone
> - Letter facts per brackets (PT $75–$200/session, savings KEEP, cap N=12,
>   assessment CUT, Sienna CUT, dogs+wife KEEP, 40-vs-8 CUT)
> - Judi Heylek + Margaret Martinazzi review quotes on page
> - Remove $249 / $299 / $429 core offer cards
> - Verify: only $197 charges · raw MD5 = local · live greps · challenge/footer
>   files untouched in diff
>
> OUT OF SCOPE:
> - ANY theme/visual redesign (tokens, fonts, sun/wildlife/horizon, rail, nav skin)
> - Google Sites edit
> - /challenge/
> - Footer + legal pages
> - Killing $97 plan in PayPal admin
> - Naming “The Frequency Effect”
> - Porting Google Sites orange/Anton look
>
> DATA SOURCES:
> - Vlad v3 + Curtis brackets + theme order 2026-07-26
> - Judi Heylek (5★, ~4 days) + Margaret Martinazzi (5★, ~1 day) full text
> - Live main architecture as ground truth for chrome
>
> SUCCESS CRITERIA:
> 1. Outdoors sunrise theme visually intact (sun/wildlife/tokens/hero chrome).
> 2. Three-card sandwich; only $197 live checkout; greys non-charging.
> 3. Free Week above pricing; SMS/form targets unchanged.
> 4. New sales copy live; no $249/$299/$429 core offer.
> 5. Post-pay SMS path for name+phone; hosted PayPal backup + SMS under $197.
> 6. Judi + Margaret quotes present.
> 7. Local MD5 == raw main; live phrase greps; git diff = index.html only
>    (or index + minimal CSS for grey/disabled tier states if required).
> ```

---

## 1. Frame & Hypothesis

**Frame:** Live homepage still sells Foundation $249 / All-In $299 / Elite $429 with placeholder PayPal IDs and SMS joins. Curtis locked a single live offer ($197 Unlimited) with two grey decoys, Free Week buttons kept above the row, and Halbert-style sales copy — without touching the outdoors sunrise theme.

**Hypothesis:** If we swap only copy + membership offer mechanics inside the existing chrome, the page will (a) stop presenting three conflicting live prices, (b) make $197 the only chargeable path, and (c) keep the brand Curtis already likes — so conversion work does not cost a redesign fight.

---

## 2. Primitives Touched

- [ ] `/Users/macmini/sites/bootcampfx/index.html` (only intended content file)
- [ ] Git: `curtisfx/bootcampfx` `main` (pull → commit → push)
- [ ] PayPal JS SDK already on page (client-id unchanged; wire plan `P-5LX3921079692330VNGW67ZI` only)
- [ ] Existing Free Week `sms:` hrefs + existing Google Form href(s) — read/preserve, do not rewrite targets
- [ ] Hosted PayPal backup URL: `https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-5LX3921079692330VNGW67ZI`
- [ ] Post-pay SMS: `sms:+16572170820` body requesting name + phone (encodeURIComponent; Pattern A `?&body=`)
- [ ] Review quotes (paste-ready): Judi Heylek, Margaret Martinazzi
- [ ] Verify: `md5` local vs `raw.githubusercontent.com/curtisfx/bootcampfx/main/index.html`; live `curl` phrase greps
- [ ] `bash scripts/verify-index.html.sh` if present and still valid
- [ ] Optional minimal CSS only: `.tier.disabled` / grey button states (still inside current token system — no new palette)

**Explicitly not touched:** `challenge/`, footer legal HTML set, `review.html` unless a one-line cross-link exists (default: leave), PayPal admin, Google Sites.

---

## 3. Execution Prompts

### Step 0: Snapshot + ground truth
**Action tier:** FREE  
**Prompt:**  
`cd /Users/macmini/sites/bootcampfx && git pull --ff-only origin main`. Record HEAD SHA. Grep current Free Week SMS hrefs, Google Form hrefs, PayPal client-id, tier prices, wildlife/sun markers. Save pre-edit fingerprints of every Free Week button href (exact strings) for post-edit equality check.  
**Verification gate:** Clean tree on latest main; Free Week href inventory captured; sun/wildlife strings present.

### Step 1: Membership offer rebuild (#membership)
**Action tier:** ASK (Actual already approved plan = go; single content commit at end)  
**Prompt:**  
Replace three paid tiers ($249/$299/$429) with sandwich:

| Card | Price | State | Copy |
|---|---|---|---|
| Starter | $97/mo · 2×/week | Grey disabled | Reason: “Not available online” |
| Unlimited | $197/mo · unlimited | Featured + badge **Most Popular** | Live PayPal only |
| Personal Training | $600–$1,200/mo · 1-on-1 | Grey disabled | Reason: “Waitlist only — text Curtis” |

- Remove Foundation/All-In/Elite join SMS for old prices.  
- Grey cards: no `paypal.Buttons().render`; disabled control + muted reason; click → `scrollIntoView` on Unlimited card (`#membership` featured tier).  
- Unlimited: `#paypal-unlimited` (or keep one slot id); plan_id `P-5LX3921079692330VNGW67ZI`; gold pill; under button: (1) SMS fallback join for Unlimited, (2) hosted subscribe backup link.  
- `onApprove`: do **not** use alert; do **not** require Google Form. Redirect/open SMS to Curtis with body asking for name + phone (include subscription id in body if available). `onCancel` log; `onError` user-safe alert + support@bootcampfx.com.  
- PLANS map: only unlimited live; starter/PT never render.  
- Strip REPLACE_WITH_249/299/429 placeholders and old TODO comment.  
- Lede copy under #membership retuned to $197 Frequency math (no “Frequency Effect” name); no $249/$299/$429.

**Verification gate (SC2, SC5):** Grep shows single live plan id P-5LX…; no $249/$299/$429 offer amounts in membership; grey cards have disabled + reason strings; SMS fallback + hosted backup present under Unlimited.

### Step 2: Free Week position (buttons kept)
**Action tier:** FREE (after plan approve)  
**Prompt:**  
Ensure Free Week CTAs are **above** the pricing sandwich and are **not** a third/fourth tier card. **Keep every existing Free Week button** — same visible labels where possible, **exact same href targets** as Step 0 inventory (SMS Pattern A + existing Google Form). Do not invent new form IDs. `#freeweek` section may move or a thin Free Week strip may sit immediately above `#membership`; do not delete Free Week from nav/sticky/mobile bar if already present.  
**Verification gate (SC3):** Diff of all Free Week href attribute values == pre-edit inventory; Free Week appears above tier grid in DOM order; buttons still present.

### Step 3: Hero + letter copy (theme shell untouched)
**Action tier:** FREE  
**Prompt:**  
Inside existing `.hero` chrome (stars/sun/horizon/wildlife/`hero-in` structure stays):

- Replace **text only** of H1 stack with Halbert headline:  
  **Why I Turn Down $1,200-A-Month Clients**  
  Sub: and what I tell them to do instead — $197, unlimited, and it works faster.  
- Keep clock / next-session ticker / outdoor meta if present.  
- Add or rewrite long-form sales letter section(s) using Vlad v3 structure adapted to brackets:
  - PT story with **$75–$200**/session; dogs + wife; **no Sienna**
  - Mechanism **described**, never named “The Frequency Effect”
  - Math table vs Unlimited $197; year savings **$4,800–$12,000** KEEP
  - No “40 vs 8” line
  - What you get (no private assessment)
  - Guarantee 30-day
  - Catch: cap **12**/month
  - Judi + Margaret quotes (full text from SPEC data)
- Light retune `#honest`, FAQ items that mention old prices, membership ledes — copy only.  
- **Do not** edit `:root` tokens, sun keyframes, wildlife keyframes, fonts, rail, nav skin.

**Verification gate (SC1, SC4, SC6):** Grep H1/letter strings; grep -i “frequency effect” → 0; Sienna absent; Judi/Margaret present; `$249|$299|$429` absent as offer prices; wildlife/sun class strings still present unchanged in CSS.

### Step 4: Dead CSS / consistency pass
**Action tier:** FREE  
**Prompt:**  
After HTML removals, grep for orphaned old tier join classes only if unused; add minimal disabled-tier CSS using existing tokens (`opacity`, `pointer-events`, `cursor`, muted `color: var(--stone)`). No new brand colors. Ensure PayPal SDK still single-load + DOMContentLoaded guard.  
**Verification gate:** No double SDK; disabled styles use existing vars; no Anton/orange port.

### Step 5: Local verify
**Action tier:** FREE  
**Prompt:**  
Run structural greps checklist:

```
# theme intact
grep -c 'hero-stars\|\.sun\|egret\|duck\|rabbit' index.html  # >0 each family

# offers
grep -E '\$249|\$299|\$429' index.html   # expect 0 (or only historical testimonial if any — should be 0)
grep -F 'P-5LX3921079692330VNGW67ZI' index.html
grep -F 'Not available online' index.html
grep -F 'Waitlist only' index.html
grep -F 'Most Popular' index.html
grep -F 'Judi Heylek' index.html
grep -F 'Margaret Martinazzi' index.html
grep -i 'frequency effect' index.html   # 0

# free week href equality vs inventory file
# paypal: only one createSubscription plan id
```

Optional: open file in browser locally if available — not required if greps clean.  
**Verification gate:** All checklist rows pass before commit.

### Step 6: Commit + push main
**Action tier:** ASK → on plan approve becomes authorized single deploy  
**Prompt:**  
```
git add index.html
git status  # must NOT include challenge/ or footer pages
git commit -m "Sales copy + $197 Unlimited sandwich; outdoors theme unchanged"
git push origin main
```
Record commit SHA.  
**Verification gate (SC7):** `git show --stat` = index.html only (+ negligible if any); push succeeds.

### Step 7: Live verify
**Action tier:** FREE  
**Prompt:**  
Wait 15–60s.  

```
md5 -q index.html
curl -sL "https://raw.githubusercontent.com/curtisfx/bootcampfx/main/index.html" | md5
curl -sL "https://bootcampfx.com/?v=$RANDOM" | grep -oE 'Why I Turn Down|Most Popular|P-5LX3921079692330VNGW67ZI|Judi Heylek|Margaret Martinazzi|Not available online' | sort -u
```

Confirm raw MD5 match. Live greps may lag CDN — raw is authoritative; recheck live up to 2 min.  
**Verification gate (SC1–7):** Report SHA + MD5 match + live phrase table to Actual. Fail → ⚠️ stop, no silent fix beyond one verified CDN wait.

### Step 8: SITREP + kaizen
**Action tier:** FREE  
**Prompt:** SITREP to Curtis (what moved / what untouched / SHA / verify). Append planner kaizen one line.  
**Verification gate:** Actual has standing.

---

## 4. Constraints

- Theme/visual chrome is sacred — copy + offers only  
- Free Week button hrefs byte-stable vs pre-edit inventory  
- Single file intent: `index.html`  
- No PayPal admin changes; $97 plan remains in PayPal but not rendered live  
- No “Frequency Effect” proper name  
- No challenge/footer/legal edits  
- Phone/SMS: use real number already on site (tool masking pitfall — verify with known-good Pattern A, do not copy masked `****` from tool output into file)  
- One deploy commit after local verify green  
- STOP/Hold from Actual halts immediately  

---

## 5. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Hero H1 text change feels like “theme change” to Curtis | M | M | Only text nodes in `.hero-in`; zero CSS token/sun/wildlife edits; screenshot-ready before push if asked |
| Free Week href accidentally rewritten | M | H | Step 0 inventory + Step 2 equality assert; fail build if mismatch |
| Post-pay SMS on desktop does nothing useful | H | M | Hosted PayPal backup link + SMS fallback both present; body includes sub id when available |
| Grey decoys look broken (not intentional) | M | M | Explicit reason lines; disabled styling; scroll-to-Unlimited |
| CDN lag false-fail verify | H | L | raw.githubusercontent MD5 authoritative; live greps secondary |
| Old prices left in FAQ/honest/marquee | M | M | Repo-wide grep on index for $249/$299/$429 before commit |
| PayPal SDK race | L | H | DOMContentLoaded + existing defer pattern; single SDK tag |
| Scope creep into challenge “for consistency” | M | H | Hard OUT OF SCOPE; git status gate |

---

## 6. Owner Table

| Role | Name | Responsibility |
|------|------|----------------|
| Plan Author | Drago | Gates, PLAN, COUNTERBATTERY |
| Approver | Curtis (Actual) | SPEC LOCKED ✓ · plan approve next |
| Executor | Drago (local clone) | Steps 0–8 on Mac Mini |
| Verifier | Drago + raw/live greps | SC1–7 |
| Logger | Drago | Kaizen |

---

## 7. COUNTERBATTERY

### Fatal Flaw

**Post-pay SMS is a weak intake.** Curtis ordered SMS after PayPal instead of a form redirect. On many desktop browsers `sms:` links fail or open nothing; paid members can still become ghosts — the exact failure Vlad flagged on Google Sites `alert()`. If the only recovery is “they’ll text later,” money can clear without a name. The plan’s backup hosted link does not fix identity capture. **This WILL fail for a non-trivial % of desktop checkouts** unless Curtis monitors PayPal for bare subscription IDs and chases them manually.

### Attack Per Execution Step

**Step 0:** Inventory can miss dynamically built SMS URLs in JS (`encodeURIComponent` bodies). Equality check then “passes” while a JS path still drifts.

**Step 1:** Rebuilding `#membership` is the highest-blast-radius edit. One bad replace can delete PayPal client-id, break tier CSS grid, or leave a second hidden $299 path. Grey “buttons” that still call `paypal.Buttons` will charge $97 — catastrophic vs SPEC.

**Step 2:** “Reposition Free Week above sandwich” invites accidental restyle or duplicate CTAs (sticky + section + hero). Duplicate SMS buttons are OK; **changed bodies** are not. Moving `#freeweek` can break `data-rail` / nav jump links.

**Step 3:** Full Halbert H1 inside a short hero may overflow mobile layout or collide with next-session ticker — pressure to “just tweak hero CSS,” which violates theme lock. Letter length can push membership below fold hard; bounce risk. Judi’s wildlife list is long — fine for proof, weak as a “most recent” conversion hammer if buried.

**Step 4:** “Minimal CSS” is how theme drift starts (`filter: grayscale` + new grays).  

**Step 5:** Grep for `$249` can false-pass if prices written as “249/mo” without `$`, or “two hundred forty-nine.”

**Step 6:** Push to main is instant public. No staging. Wrong PayPal plan id = wrong charge in production with no dress rehearsal.

**Step 7:** CDN lies; declaring victory on raw MD5 while live still shows $299 confuses Actual.

### Mortal Risks Not Captured Above

1. **Legal/refund page still describes old tier names** — OUT OF SCOPE this pass, but customers who click Refund footer get cognitive dissonance. Curtis accepted this lag.  
2. **Existing members on $249/$299/$429** see public site contradict their plan — support load, not a code bug.  
3. **Starter $97 still buyable via old Google Sites or bookmarked PayPal link** — SPEC allows this; decoy honesty is page-local only.  
4. **Headline “turn down $1,200 clients”** with PT decoy at $600–$1,200 is fine only if Curtis truly redirects PT demand; if he still takes PT off-menu, grey “waitlist” is the right door — ensure SMS waitlist body doesn’t promise a date.

### Verdict

**Survives COUNTERBATTERY?** YES

We proceed because the SPEC explicitly chose SMS post-pay and page-local greys, accepting manual PayPal↔human matching as the cost of avoiding form changes; theme lock + href inventory + single-file diff gates prevent the failure modes that actually destroy brand trust. Fatal intake weakness is **accepted and named**, not hidden — SITREP will remind Curtis to watch new PayPal subs the first 72 hours.

---

## Approval gate

Reply:

- **`PLAN APPROVED`** → I execute Steps 0–8  
- **`PLAN APPROVED WITH EDITS:`** … → I patch PLAN then execute  
- **`COUNTERBATTERY FAIL`** → I attack harder / revise  
- **`HOLD`** → stop  

No file edits on `index.html` until one of the approve lines.
