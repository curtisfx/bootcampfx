# PLAN.md — BootCampFX Website Optimization
## Phase 1 — PLAN · Drago + Vlad

---

## LOCKED SPEC (verbatim)

```
CORE DECISION THIS DRIVES: More prospects → more paid clients
IN SCOPE: All 5 changes above. New pages if justified. Vlad + Drago collaborate.
OUT OF SCOPE: Paid advertising. Spending money on tools/services.
DATA SOURCES: Live site (bootcampfx.com), index.html source, critique report above
SUCCESS CRITERIA: More inquiries. More paid clients. (Track via Google Form submissions + PayPal conversions)
```

---

## 1. FRAME & HYPOTHESIS

**Frame:** BootCampFX has a solid 7.1/10 website with exceptional testimonials, strong copy, and 21 years of credibility — but it's a passive brochure. Every visitor who leaves without signing up is a lost prospect with no way to re-engage. The gap between "good local business site" and "lead-generating machine" is ~3 hours of work.

**Hypothesis:** Five no-cost changes — SEO schema, email capture, a workout video, performance fixes, and trust signal reinforcement — will measurably increase Google Form submissions and paid conversions within 30 days. These changes compound: schema brings more visitors, email capture retains them, and video/trust signals convert them.

---

## 2. PRIMITIVES TOUCHED

| Primitive | What Changes |
|-----------|-------------|
| `index.html` | All 5 changes are edits to the existing single-page site |
| GitHub Pages | Push updated `index.html` → auto-deploy |
| Google Form | Remains as post-email-capture destination; no changes needed |
| Google Business Profile | Linked from "4.9 on Google" text (no profile changes) |
| DNS/GitHub Pages HTTPS | Already configured, no changes |

---

## 3. EXECUTION PROMPTS

### Change 1 — JSON-LD Schema (Drago)
**Goal:** Add LocalBusiness + FAQ + AggregateRating JSON-LD to `<head>`.
**Verification gate:** Google Rich Results Test shows valid schema with star rating, address, FAQ accordions.
**Command:** Edit `index.html` — insert JSON-LD block before `</head>`. Push via API.

### Change 2 — Email Capture (Drago)
**Goal:** Replace all Google Form CTA hrefs with an on-page email capture step. Name + email fields. On submit, redirect to Google Form. Store emails (initially: log to a simple endpoint or email to Curtis).
**Verification gate:** Click any CTA → name/email form appears inline → submit → redirected to Google Form. Email received by Curtis.
**Command:** Edit `index.html` — add inline form markup + minimal JS for the capture. Push via API.

### Change 3 — Workout Video (Curtis + Drago)
**Goal:** Add a 30-60 second authentic workout video from Acacia Park embedded in the hero section.
**Verification gate:** Video plays inline on mobile and desktop. No autoplay with sound.
**Command:** Curtis records video on phone → sends to Drago → Drago hosts (YouTube unlisted or direct MP4 in repo) → embed via `<video>` tag in hero.

### Change 4 — Performance Fixes (Drago)
**Goal:** Add `loading="lazy"` + `width`/`height` to coach image. Add `async` to PayPal SDK. Add `&display=swap` to Google Fonts URL. Add `preconnect` for fonts and PayPal.
**Verification gate:** Lighthouse score improves (target: +10-15 performance). No CLS from coach image.
**Command:** Four targeted string replacements in `index.html`. Push via API.

### Change 5 — Trust Signals (Drago)
**Goal:** Link "4.9 on Google" to Google Business Profile reviews. Add circular headshot placeholder images next to top 3 testimonials (use initials as fallback until real photos provided).
**Verification gate:** Click "4.9 on Google" → opens Google reviews. Testimonial cards show headshot circles.
**Command:** Edit `index.html` — add href to rating pill + add CSS avatar circles to top testimonials.

---

## 4. CONSTRAINTS

- **No paid tools.** All changes use free/included resources.
- **Pure static HTML + CSS + vanilla JS.** No frameworks, no build step, no npm.
- **GitHub Pages deployment.** Push = deploy. No server config needed.
- **Video: phone footage only.** No production, no editing, no budget.
- **Email capture: lightweight.** Initially log to Drago's email or simple endpoint. No Mailchimp/ConvertKit unless Curtis wants it later (ASK tier).
- **Drago executes Changes 1-2-4-5 independently.** Change 3 (video) requires Curtis to record footage.

---

## 5. RISKS & MITIGATIONS

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| HTTPS cert not yet provisioned | Medium | Low | Already waiting on GitHub; site serves on HTTP fine |
| Email capture JS breaks mobile layout | Low | Medium | Test in Chrome DevTools mobile view before push |
| Video file too large for GitHub Pages (1GB limit) | Low | Medium | Host on YouTube unlisted; embed iframe |
| Google Rich Results rejects schema | Low | Low | Validate before push; iterate if needed |
| PayPal async breaks subscription buttons | Low | High | Test buttons after change; revert if broken |

---

## 6. OWNER TABLE

| Change | Owner | Tier | Dependency |
|--------|-------|------|------------|
| #1 JSON-LD Schema | Drago | FREE | None |
| #2 Email Capture | Drago | FREE | None |
| #3 Workout Video | Curtis (record) / Drago (embed) | ASK (Curtis for footage) | Curtis records video |
| #4 Performance Fixes | Drago | FREE | None |
| #5 Trust Signals | Drago | FREE | None |
| Push & Deploy | Drago | FREE | Token access confirmed |
| Verification | Drago + Vlad | FREE | All changes pushed |

**Vlad's role:** Vlad reviews the plan, validates the execution approach, and independently verifies each change post-deployment. Vlad can also generate alternative copy variants for the email capture form and new sections.

---

## 7. COUNTERBATTERY

### Fatal Flaw
**The email capture step breaks the conversion flow.** Right now, clicking "Free Week" goes directly to a Google Form — one click, one destination. Adding an intermediate step introduces a new drop-off point. If the email capture form is poorly designed, slow, or feels like a bait-and-switch, it could *reduce* Google Form submissions instead of increasing them. The critique flagged this as the #2 highest-ROI change — but that assumes the form is *better* than the current direct-to-Google-Form flow. It might not be.

### Attack Per Execution Step

**Change 1 (Schema):** WILL fail to produce rich results if Google's algorithm decides the site doesn't have enough authority. Schema markup alone doesn't guarantee rich snippets — it's a prerequisite, not a guarantee. The site has no backlinks, no Google Business Profile link, and minimal domain authority. Schema might be invisible.

**Change 2 (Email Capture):** WILL increase bounce rate if the form has any friction. Users on mobile will have to type their email on a phone keyboard. Many will abandon. The Google Form at least auto-fills if they're logged into Google. An email capture form demands a value exchange — "give us your email" without immediate payoff is a harder ask than "fill out this Google Form to claim your free week."

**Change 3 (Video):** WILL slow page load. Adding a video embed adds 500KB-2MB of payload. If hosted on YouTube, the iframe is render-blocking. If self-hosted as MP4, it's a bandwidth hog on GitHub Pages. Either way, the performance gain from Change 4 is partially negated by Change 3.

**Change 4 (Performance):** WILL have minimal real-world impact if the site already loads fast on the target audience's devices. Core Web Vitals matter for SEO but local fitness searchers on 5G iPhones won't notice the difference between a 1.2s and 0.9s LCP. The effort-to-impact ratio is overstated.

**Change 5 (Trust Signals):** WILL backfire if the Google Business Profile link reveals any negative reviews. "4.9 on Google" is a claim — linking to the actual profile lets prospects read all reviews, including any 1-star ratings. If there are bad reviews, the link becomes a liability.

### Three Strongest Failure Modes

1. **Email capture kills conversions.** Direct-to-form currently works. Adding friction reduces total submissions. Net effect: fewer clients, not more. The critique is wrong about this being high-ROI because it assumes form abandoners = lost forever, when in fact Google auto-fill may produce *higher* completion rates than a custom email form.

2. **None of these changes move the needle on search traffic.** SEO schema doesn't help if there are no backlinks, no content strategy, and no domain authority. The site needs ongoing content (blog posts, workout tips) to rank — not just schema markup. This plan optimizes a brochure but doesn't add the engine that drives traffic to it.

3. **Video degrades the clean design.** The site's current aesthetic is polished, dark, and premium. A raw iPhone video of a 5:30 AM park workout — however authentic — may look jarring next to the Anton/Archivo typography and film-grain overlay. Authenticity can read as amateurish if not framed properly.

### Survival Assessment

The plan survives COUNTERBATTERY with one amendment:

- **Change 2 (Email Capture) is downgraded from FREE to ASK tier.** Before implementing, we A/B test: deploy Changes 1+4+5 first, measure the baseline Google Form submission rate for 7 days, THEN add email capture. If submissions drop, revert. If they hold or increase, keep it. This prevents the fatal flaw scenario.

- **Change 3 (Video) is gated on Curtis providing footage that fits the brand.** If the footage doesn't work visually, we use a still photo instead or skip entirely.

The other attacks are valid concerns but not plan-killers. Schema markup is table stakes even without guaranteed rich results. Performance fixes are cheap and correct. Trust signal linking is reversible if reviews are bad. The plan proceeds with the email capture gated behind a measurement period.

---

**STATUS: AWAITING ACTUAL APPROVAL**
