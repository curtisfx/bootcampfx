# PLAN.md — BootCampFX Copy v4 Markup Pass (No Deploy)

> **Phase:** 1 — PLAN  
> **Date:** 2026-07-26  
> **Status:** Awaiting Actual approval  
> **Mode:** MARKUP / EMAIL ONLY — zero live push  

> Locked SPEC (verbatim):
> ```
> CORE DECISION THIS DRIVES:
> Upgrade bootcampfx.com homepage sales narrative to Vlad Copy v4 Halbert craft
> (headline, lead order, section rhythm, math-before-trial, one-step close) without
> changing locked product/offer decisions or the outdoors theme — deliver as
> MARKUP PASS (email) first; no live push until Curtis second-approves.
>
> IN SCOPE:
> - Markup document(s) only in this phase (email to Curtis; optional Cc Vlad)
> - Map v4 letter structure onto live page section order (re-flow plan):
>   headline+sub → lead/checkbook → frequency story (UNNAMED) → twelve-days line
>   up front → math table BEFORE free week → free week CTA block → cheap objection
>   → what $197 gets → guarantee → catch (cap 12) → one-step close + P.S./P.P.S.
> - Hero H1/sub text → v4 headline B + sub “(And the $197 plan he talks them into
>   instead — that works faster)” inside existing outdoor hero shell
> - Preserve Free Week buttons/hrefs (SMS + form targets unchanged)
> - Preserve live offer sandwich: Starter $97 grey · Unlimited $197 Most Popular
>   live PayPal · PT $600–$1,200 grey · post-pay SMS · hosted backup
> - Judi Heylek + Margaret Martinazzi quotes retained (place where v4 wants proof)
> - Apply locked facts: PT $75–$200/session; year savings $4,800–$12,000; cap 12;
>   assessment CUT; Sienna CUT; dogs+wife KEEP; 40-vs-8 CUT; no “Frequency Effect”
>   proper name (describe mechanism only)
> - Note any live HTML anchors that must move for re-flow (for later build)
> - After markup approve: separate PLAN + APPROVED FOR BUILD before index.html push
>
> OUT OF SCOPE (this phase):
> - Any git push / live deploy / PayPal admin
> - Theme/visual redesign (sun, wildlife, tokens, fonts, rail, nav skin)
> - /challenge/, footer/legal pages, Google Sites
> - Reopening product brackets (prices, greys, cap, assessment, naming)
> - Killing $97 plan in PayPal
> - Changing Free Week SMS/form href targets
>
> DATA SOURCES:
> - Vlad email #50 Copy v4 full letter + Halbert notes
> - Locked SPEC from v3 session (product + theme + Free Week buttons)
> - Live main index.html (commit 600d0f1 ground truth for chrome + offers)
> - Judi + Margaret review text already on page
>
> SUCCESS CRITERIA:
> 1. Curtis receives markup email with: v4-adapted copy (locks applied), proposed
>    DOM/section order vs live, explicit do-not-touch list, and open issues = none
>    on product (or only copy nits).
> 2. Markup never uses name “Frequency Effect”; never includes Sienna; never
>    restores assessment or 40-vs-8; uses $75–$200 and cap 12.
> 3. Headline in markup = v4 option B; Free Week + $197 CTAs called out with
>    existing live hrefs/plan id preserved.
> 4. No site files changed until Curtis replies APPROVED FOR BUILD (or equivalent)
>    after reviewing markup.
> 5. Optional: short Drago notes on Halbert craft / twelve-days placement as Vlad asked.
> ```

---

## 1. Frame & Hypothesis

**Frame:** Live site already sells the locked offer sandwich under a first-pass Halbert letter (v3). Vlad shipped v4 craft improvements (headline, order, rhythm). Curtis wants those craft wins without reopening product or deploying yet.

**Hypothesis:** If we deliver a single markup doc that (a) rewrites the letter to v4 craft with locks applied and (b) maps exact DOM re-flow against live anchors, Curtis can approve copy offline and only then authorize a thin build — avoiding another live thrash.

---

## 2. Primitives Touched

- [ ] Read-only: `/Users/macmini/sites/bootcampfx/index.html` (live structure)
- [ ] Read-only: git HEAD / raw main for ground truth (no write)
- [ ] Write: `/Users/macmini/sites/bootcampfx/_ops/BootCampFX-Copy-v4-MARKUP-*.md`
- [ ] Himalaya send → `curtis.ludlow@gmail.com` (+ Cc `gobootcampfx@gmail.com` recommended)
- [ ] Source text: Vlad email #50 body (already read this session)
- [ ] Locked quotes: Judi Heylek, Margaret Martinazzi
- [ ] Live constants: FW SMS href, form URL, plan `P-5LX…`, hosted subscribe URL

**Forbidden this phase:** `git commit` / `git push` on site · editing `index.html`

---

## 3. Execution Prompts

### Step 0: Ground-truth snapshot (read-only)
**Action tier:** FREE  
**Prompt:** Confirm HEAD short SHA; grep live order of `#top` hero, `#letter`, `#freeweek`, `#membership`, proof, members; inventory Free Week href strings and PayPal plan id (do not mutate).  
**Verification gate:** Snapshot recorded in markup appendix; no file writes to index.html.

### Step 1: Build adapted v4 master copy
**Action tier:** FREE  
**Prompt:** Produce full letter text applying v4 craft with locks:

| v4 | Lock override |
|---|---|
| Headline B | Use as written |
| Frequency Effect section title | Rename to neutral (e.g. “How often you train”) — mechanism yes, name no |
| Sienna | CUT |
| dogs/wife | KEEP (no Sienna) |
| PT rates | $75–$200 / card $600–$1,200 |
| Assessment bullet | CUT |
| 40 vs 8 | CUT |
| Cap | **12** |
| Client proof | Judi + Margaret full quotes |
| Free week / subscribe | Reference **existing** live SMS, form, PayPal plan/hosted link — no new URLs |
| Year savings | KEEP $4,800–$12,000 |

Include P.S. / P.P.S. from v4 adapted to locks.  
**Verification gate (SC2, SC3):** Grep markup file: zero “Frequency Effect”, zero “Sienna”, zero assessment-as-included, zero “40 Unlimited”; has headline B, $75–$200, cap 12, both reviews, plan id / FW patterns.

### Step 2: DOM re-flow map (live → v4 order)
**Action tier:** FREE  
**Prompt:** Table mapping current anchors to target order for a **future** build (not executed now):

Proposed narrative spine inside outdoor chrome:
1. Hero H1/sub (copy only)  
2. Proof strip KEEP  
3. Optional compress outside/standard/coach or leave as social proof shoulders (state recommendation: keep chrome sections; letter becomes main sales spine)  
4. `#letter` rewritten in v4 beat order  
5. Free Week block **inside/after math, before close** per v4 (may mean moving `#freeweek` relative to letter subsections — document)  
6. `#membership` sandwich KEEP as-is (product) — ledes may get light voice match in future build notes only  
7. Schedule / FAQ / footer KEEP  

Call out conflicts: live has Free Week above full membership already; v4 wants Free Week after math inside letter. Resolve in markup: **letter-internal Free Week CTA strip using same buttons**, membership sandwich remains below for checkout chrome.  
**Verification gate (SC1):** Markup has before/after order table + explicit “do not touch” chrome list.

### Step 3: Drago craft notes (Vlad ask)
**Action tier:** FREE  
**Prompt:** Short section: twelve-days placement (agree up-front after Frequency beats), headline B vs #6 (Curtis picked B), any weak spots (e.g. “Dear Friend” vs site voice; desktop SMS intake still weak — out of scope this pass).  
**Verification gate (SC5):** Notes present, ≤1 page.

### Step 4: Email delivery
**Action tier:** FREE  
**Prompt:** Himalaya MML attachment to Curtis, Cc Vlad. Subject clear: MARKUP ONLY — no deploy. Body: how to reply (`APPROVED FOR BUILD` later vs copy nits now).  
**Verification gate (SC1, SC4):** Send succeeds; index.html git status clean of new commits from this work; working tree may still have untracked `_ops/` only.

### Step 5: SITREP in chat
**Action tier:** FREE  
**Prompt:** Confirm email sent, path to markdown, wait for Curtis. No plan for build until he orders.  
**Verification gate:** Actual knows HOLD on deploy.

---

## 4. Constraints

- **No deploy** until explicit second approve after markup review  
- Product locks immutable this pass  
- Theme chrome immutable  
- Free Week hrefs immutable  
- Markup is the deliverable — not a partial HTML edit “for convenience”  
- STOP/Hold honored immediately  

---

## 5. Risks & Mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Markup accidentally becomes a silent index.html edit | M | H | Step gates forbid write; verify `git status` / no commit |
| Re-flow map over-promises ripping outdoors/proof sections | M | M | Default keep proof/outside/members; letter re-flow only |
| “Frequency” wording drifts into banned name | M | M | Final grep before send |
| Curtis thinks email = approval to build | M | H | Subject + body + SITREP scream MARKUP ONLY |
| v4 “Dear Friend” clashes with site tone | L | L | Note in craft section; keep unless Curtis nits |

---

## 6. Owner Table

| Role | Name | Responsibility |
|------|------|----------------|
| Plan Author | Drago | PLAN + COUNTERBATTERY |
| Approver | Curtis | PLAN APPROVED → markup; later BUILD approve |
| Executor | Drago | Steps 0–5 markup/email only |
| Verifier | Drago | SC1–5 greps + send confirm |
| Cc | Vlad | Optional craft visibility |

---

## 7. COUNTERBATTERY

### Fatal Flaw

**Re-flow scope (4C) can explode the markup into a second homepage redesign doc.** “Full page re-flow to match v4 letter order” WILL collide with live multi-section story (outside/standard/coach/members/honest). If the markup tries to renumber the whole day-arc, Curtis gets a redesign he already forbade thematically — death by scope, not by copy.

### Attack Per Step

**Step 0:** Read-only still fails if agent “helpfully” pulls and dirty-checks out a branch.  

**Step 1:** Merging v4 + locks produces Frankenstein — v4’s best lines depend on naming Frequency Effect and Sienna pathos; stripping both MAY weaken the Halbert punch. Twelve-days line without Sienna still works; “talking out of money” headline without personal grit may feel corporate.

**Step 2:** Dual Free Week (inside letter + `#freeweek` + sticky) creates three CTAs — v4 wanted one path; live SPEC wants buttons kept. Markup must own the duplication honestly or build will thrash.

**Step 3:** Craft notes become another debate loop (headline already locked B).

**Step 4:** Email to wrong party / missing attachment (prior himalaya lessons).

### Mortal Risks

1. Curtis replies “looks good” without `APPROVED FOR BUILD` and agent deploys — process violation.  
2. Vlad treats markup as orders to change product brackets again.  
3. Live site already converts; delaying for perfect letter has opportunity cost — accepted by 5B.

### Verdict

**Survives COUNTERBATTERY?** YES  

We proceed because SPEC 4C is satisfied by a **letter-spine re-flow map** that keeps day-arc chrome and offer sandwich fixed, documents Free Week duplication explicitly, and hard-stops at email. Fatal scope explosion is contained by “letter + CTA order, not theme rebuild” in Step 2.

---

## Approval gate

- **`PLAN APPROVED`** → execute markup + email (no deploy)  
- **`PLAN APPROVED WITH EDITS:`** …  
- **`HOLD`**
