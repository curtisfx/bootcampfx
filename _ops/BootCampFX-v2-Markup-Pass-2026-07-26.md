# BootCampFX.com — Markup Pass Only
## Sales Copy v2 + Tier Restructure (Decision Doc)
**Date:** 2026-07-26  
**From:** Drago  
**To:** Curtis Ludlow  
**Status:** MARKUP ONLY — no site changes deployed  
**Sources:** Vlad email #47 (Halbert v2 + PayPal IDs) · live `bootcampfx.com` main · Google Sites ref `https://sites.google.com/view/bootcampfx/`  
**Your orders (Telegram):** Map $197 to most-popular tier · remove other live tiers · add greyed Starter $97 + greyed Personal Training decoys · adapt copy to these prices · markup pass only · email this doc · you answer by email reply  

---

## 1. Mission in one page

| Live now (bootcampfx.com) | Proposed after your YES |
|---|---|
| Foundation **$249** | **REMOVE** |
| All-In **$299** (unlimited) | **REMOVE** |
| Elite **$429** (capped 20) | **REMOVE** |
| PayPal plan IDs = placeholders; SMS join links carry sales | Wire **only** live $197 plan |
| Rhetoricians / sunrise multi-section copy | Keep architecture; adapt spine to **Frequency Effect + $197** |

**Proposed 3-card membership row (center is the only buy path):**

| Card | Price | Role | Checkout |
|---|---|---|---|
| **Starter** | **$97/mo** | Decoy / anchor low | **Greyed button** — not clickable, no charge |
| **Unlimited** (Most Popular) | **$197/mo** | Real offer | **Live PayPal** plan `P-5LX3921079692330VNGW67ZI` |
| **Personal Training** | **$[PT PRICE]/IES — see Q1]** | Decoy / anchor high | **Greyed button** — not clickable, no charge |

Google Sites today (reference only): 2 live cards — Starter $97 + Elite Unlimited $197 “Best Value”, both with live PayPal buttons. Your order **greys Starter** and **adds a PT decoy**, so bootcampfx.com will **not** mirror Sites 1:1 — it will be a 3-card anchor sandwich with one live middle.

---

## 2. How to answer this doc

Reply to this email with answers in this format (copy/paste):

```
Q1: ...
Q2: ...
...
APPROVED FOR BUILD: YES / NO / YES WITH EDITS
EDITS: ...
```

Anything still in `[BRACKETS]` after your reply gets cut or rewritten before publish.  
I will not push to `main` until you send **APPROVED FOR BUILD: YES**.

---

## 3. Tier architecture — proposed defaults

### 3A. Card 1 — Starter (decoy, greyed)

| Field | Proposed | Confirm |
|---|---|---|
| Name | Starter | [KEEP / RENAME: ______] |
| Price | $97/mo | Matches live PayPal plan + Google Sites |
| Subline | 2 sessions / week | [KEEP / CHANGE: ______] |
| Per-session math | ≈ $12 per session | [KEEP / CHANGE] |
| Bullets | • 2 coached sessions every week<br>• Nutrition framework included<br>• Month to month<br>• Same park, same coach | [EDIT FREE] |
| Badge | none | |
| Button state | **Greyed / disabled** | See §4 |
| Grey reason line (under button) | **Option A:** “Not available online”<br>**Option B:** “Currently full — choose Unlimited”<br>**Option C:** “Text Curtis if you only want 2×/week” | **[PICK A / B / C / WRITE YOURS]** |
| PayPal | Do **not** render live button. Plan ID `P-01R729078S772880RNGW6Y2Q` stays in appendix only (not charged from this page). | Confirm: **no live $97 checkout on homepage** [YES/NO] |

### 3B. Card 2 — Unlimited (MOST POPULAR — only live buy)

| Field | Proposed | Confirm |
|---|---|---|
| Name | **Unlimited** (drop “Elite” unless you want it) | [Unlimited / Elite Unlimited / Other: ______] |
| Flag badge | **Most Popular** (Sites used “Best Value” 🔥) | [Most Popular / Best Value / Other] |
| Price | **$197/mo** | LOCKED per your order |
| Subline | Unlimited coached sessions | |
| Per-session math | ≈ $9–12/session at 4–5×/week · “as low as ~$6–9 at high frequency” | **[PICK ONE MATH LINE — see Q2]** |
| Bullets (adapted from Vlad + Sites) | • Train as often as you want (15 coached sessions/week on the board)<br>• Every movement scaled to you<br>• Priority coaching & check-ins<br>• Advanced nutrition framework<br>• Group that notices when you’re gone<br>• 30-day Love It Or Leave It guarantee | [EDIT FREE] |
| Optional premium line | [Private 45-min onboarding assessment — include / cut / paid add-on] | **[Q3]** |
| Cap line under card | New Unlimited spots capped at **[N]/ies]/IES]/IES]** / month | **[Q4]** |
| PayPal | **LIVE** · plan_id `P-5LX3921079692330VNGW67ZI` · gold pill subscribe · onApprove → intake form | |
| SMS fallback | Keep a text join link under/near button if PayPal fails? | [YES keep SMS / NO PayPal only] |
| Featured styling | Center card, dawn/gold border, “Most Popular” flag (reuse `.tier.featured`) | |

### 3C. Card 3 — Personal Training (decoy, greyed)

| Field | Proposed | Confirm |
|---|---|---|
| Name | Personal Training | [KEEP / Private Coaching / 1-on-1] |
| Price display | **Option A:** $1,200/mo<br>**Option B:** From $600–$1,200/mo<br>**Option C:** $150/session<br>**Option D:** $75–$150/session | **[Q1 — PICK]** |
| Subline | 2× / week · one-on-one | |
| Bullets | • Private sessions with Curtis<br>• Fully customized programming<br>• Schedule around your calendar<br>• Highest touch, lowest frequency | |
| Honest footer on card | “I usually talk people out of this — see the letter above.” | [KEEP / CUT / REWRITE] |
| Button state | **Greyed / disabled** | |
| Grey reason line | **Option A:** “Not taking new PT clients”<br>**Option B:** “I turn most of these down — take Unlimited”<br>**Option C:** “Waitlist only — text Curtis” | **[PICK]** |
| PayPal | No live button. No plan ID. | |

### 3D. Removed from homepage

- Foundation $249 card + SMS “Join Foundation”
- All-In $299 card + SMS “Join All-In”
- Elite $429 card + “Limited to 20 members” + SMS “Join Elite”
- Placeholder plan IDs `REPLACE_WITH_249/299/429_PLAN_ID`
- Any copy that prices the core offer at $249 / $299 / $429

**Challenge page ($349 / cohort):** untouched unless you say otherwise.  
**[Q5] Leave `/challenge/` alone?** YES / NO

---

## 4. Greyed button UX (decoy pattern)

**Intent:** Look like a real checkout so $197 feels like the smart middle. Never charge. Never soft-404.

**Proposed implementation (for build phase — not done yet):**

```text
Visual:
- Button shell matches PayPal pill shape/size
- Opacity ~0.45, grayscale filter
- cursor: not-allowed
- Label examples:
  Starter: "Unavailable" or "Sold out online"
  PT: "Not available" or "Not taking new clients"
- Small muted line under button (reason from §3)

Behavior:
- <button disabled> or <a aria-disabled="true" tabindex="-1">
- No paypal.Buttons().render() on decoy slots
- No href to PayPal for decoys
- Optional: click on grey → smooth-scroll to #membership Unlimited card
  [Q6] Scroll-to-Unlimited on grey click? YES / NO
```

**Accessibility:** `aria-disabled="true"` + visible reason text (not color alone).

---

## 5. PayPal / forms — tech decisions

| Item | Proposed | Confirm |
|---|---|---|
| Client ID | Keep existing (already on site + Sites) | |
| Live plan only | `P-5LX3921079692330VNGW67ZI` = $197 Unlimited | **[Q7] You verified in PayPal: $197 USD / monthly / auto-renew?** YES / NO / WILL CHECK |
| Starter plan ID | `P-01R729078S772880RNGW6Y2Q` = $97 — **not rendered live** on homepage under this plan | Confirm |
| onApprove redirect | **Option A (Sites form):** `https://docs.google.com/forms/d/e/1FAIpQLSeZ_onENyU4z6EucKiYs_nv4KazwAb5DML_ffNWdYwHiVgucA/viewform` + `sub=` subscription ID<br>**Option B (current bootcampfx.com form):** `https://docs.google.com/forms/d/e/1FAIpQLSdgpBGX2zRrKjjnEgKHbOF-KaRD6mmCx71qQ0Y9Iag8tPYGLA/viewform` | **[Q8] A or B?** |
| onCancel / onError | Add handlers (Vlad Option B) — cancel silent log; error alert + support@ | [YES/NO] |
| Hosted subscribe URL (Option A backup) | `https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-5LX3921079692330VNGW67ZI` as text link under smart button | [YES add backup link / NO] |
| Free week CTA | Keep **SMS Pattern A** on bootcampfx.com (current), not only Google Form | [KEEP SMS / SWITCH TO SITES FORM / BOTH] |
| Double-load SDK | Do not load PayPal SDK twice | |

**Warning already true on Google Sites:** Starter + Elite both live-charge today; onApprove is still `alert()` only (member can become a ghost). Bootcampfx.com build will fix onApprove redirect for the **$197** button only.

---

## 6. Sales copy adaptation — Frequency Effect @ $197

Philosophy locked from Vlad v2, **prices forced to your tier map**.  
Everything in `[BRACKETS]` needs your word before publish.

### 6A. Big Idea (hero or new lead block)

**Proposed H1 spine (options — pick one):**

1. **Why I Turn Down $1,200-A-Month Clients**  
   *(And what I tell them to do instead — it costs $197, it's unlimited, and it works faster.)*
2. Keep sunrise hero (*21 years. Same park. Same coach. / The sun isn't up yet. / We are.*) and put the Halbert letter **below proof** as a long-form section `#letter`
3. Hybrid: keep short sunrise H1; change `.sub` to Frequency one-liner; full letter later

**[Q9] Hero treatment: 1 / 2 / 3**

**Proposed hero sub (if hybrid/keep sunrise):**  
Coached outdoor group training at Acacia Park since **2005**. Your body changes from sessions attended — not dollars spent. **Unlimited coaching is $197/mo.** First week free.

### 6B. Named mechanism (use verbatim if true)

> **The Frequency Effect**  
> Your body does not change based on how much you pay per session. It changes based on how many sessions you actually show up to.  
> - Twice a week *maintains*. Four times a week *transforms*.  
> - The best program done twice a month loses to an average program done four times a week.  
> - Every client who fully changed had one thing in common: **frequency.**

**[Q10] Coin “The Frequency Effect” on the public site?** YES / NO / YES BUT RENAME: ______

### 6C. Core math block (adapted — no $249/$299/$429)

| | Personal Training (2×/week) | BootCampFX Unlimited |
|---|---|---|
| Monthly cost | **[$600 – $1,200]** | **$197** |
| Coached sessions/month | 8 | 17 – 26+ (your choice) |
| Cost per session | **[$75 – $150]** | **As low as ~$9** (at 5×/week) |
| Who programs / coaches | Curtis | Curtis |

**Killer line (adapted):**  
One hour of personal training costs the same as **[twelve days / ~2 weeks]** of unlimited BootCampFX.

**Year savings line:**  
Over a year, Unlimited at 4×/week vs 2× PT keeps **[$4,800 to $12,000]** in your pocket — more than double the coached reps.

**[Q11] PT rate band for public math:** $75–$150/session and $600–$1,200/mo — TRUE ENOUGH TO PRINT? YES / NO / USE THESE NUMBERS: ______  
**[Q12] Year savings figures:** KEEP / CUT / CHANGE TO: ______

### 6D. Confession frame (honest if true)

About once a month someone wants PT at **[$75–$150]/session]**. Most of the time I talk them out of it — not because I don’t want the money (three dogs, a wife, a 2008 Sienna with 171k miles) — because **two hours a week was never enough to change a body**, and life makes them miss sessions they already paid for.

**[Q13] Keep Sienna / dogs / wife personal details on homepage?** YES / NO / SOFTEN  
**[Q14] “I turn down $1,200/mo clients” — literally true often enough?** YES / NO / SOFTEN TO: ______

### 6E. What Unlimited is

- Not a gym membership. Not an app.  
- **15 coached group sessions a week** at Acacia Park — 5:30 AM, 8:00 AM, 6:00 PM (Mon–Thu pattern as live schedule), Fri mornings, Sat 8:00 AM.  
- Scaled to body and ability; 60-year-olds next to former athletes.  
- **The group notices when you’re gone** — that’s what people actually buy at $1,200/mo.

**[Q15] “15 coached sessions a week” still accurate on your real calendar?** YES / NO / REAL NUMBER: ______

### 6F. “Why so cheap?” objection

Group training is efficient. Coach 12 in the hour that used to be one. Price is low because delivery is smart — not because coaching is cheap. Prefer **[40]** Unlimited members for five years over **[8]** PT clients who quit in four months.

**[Q16] Public numbers 40 members / 8 PT — OK?** YES / NO / CHANGE: ______

### 6G. Everything in $197/mo (list)

- Unlimited coached sessions — full weekly board  
- Every movement scaled to you  
- Priority coaching and check-ins (Unlimited only)  
- Advanced nutrition framework  
- **[Q3 again] One private 45-minute onboarding assessment** — include free first month / cut / sell separate  
- Group accountability  
- 30-Day Love It Or Leave It guarantee  

### 6H. Guarantee (align with refund page)

Train 30 days. As many sessions as you can. If you’re not stronger, moving better, and looking forward to the next session — or it’s just not for you — tell me. Full refund. No forms, no exit interview, no retention specialist.

**[Q17] Guarantee text matches refund.html practice?** YES / NEEDS LEGAL TWEAK: ______

### 6H2. Scarcity

I cap new Unlimited memberships at **[N]** per month. Not theater — coaching dies in a crowd. 5:30 fills first.

**[Q4 again] Cap number N = ______** (required before publish)

### 6I. CTA stack

1. Free 7-day trial — no credit card (SMS and/or form — Q8/free-week choice)  
2. Skip the line — **Subscribe $197 Unlimited** (live PayPal)  
3. P.S. / P.P.S. from Vlad letter adapted to $197 only  

### 6J. Section map — what I will change on build (after your YES)

| Live anchor | Action |
|---|---|
| `#top` hero | Per Q9 |
| `.proof` | Labels only if needed; counters stay |
| Dark marquee | Optional Frequency one-liner |
| `#outside` | Light touch — accountability / air — keep structure |
| `#standard` | Weave Frequency into COACHED/MEASURED/KEPT or leave; **[Q18] rewrite standard?** LIGHT / FULL / LEAVE |
| `#coach` | Optional short confession line; keep signature |
| `#members` | **KEEP cards/photos** |
| `#honest` | Retune bullets to Unlimited@$197 + decoy logic; age 20–80 stays |
| Gold marquee | KEEP unless you want Frequency strip |
| `#membership` | **FULL REBUILD** to 3-card sandwich (§3) + PayPal §5 |
| `#schedule` | KEEP |
| `#freeweek` | Body tweak only; CTA pattern per your free-week choice |
| `.faq` | Add/adjust: Why so cheap? PT vs group? Out of shape? Greyed tiers? |
| footer / legal | KEEP; refund/terms still describe month-to-month |
| wildlife / sun / rail / nav / tokens / SMS attrs (except membership join SMS) | **NO-TOUCH** |

---

## 7. Adapted long-form letter (working draft)

*For review. Brackets = your call. Not live.*

---

**Why I Turn Down [$1,200]-A-Month Clients**

*(And what I tell them to do instead — it costs $197, it’s unlimited, and frequency does what two private hours a week never could.)*

From Curtis Ludlow  
BootCampFX — Acacia Park, Fullerton, California  

Dear Frustrated Fullerton Fitness Buyer,

About once a month, somebody sits across from me ready to buy personal training. One-on-one. Two sessions a week at **[$75–$150]** a session. They’re ready to pay **[$600 to $1,200]** a month right now.

And most of the time, I talk them out of it.

Not because I don’t want the money. **[I have three dogs, a wife, and a 2008 Sienna with 171,000 miles on it. I want the money.]**

I talk them out of it because I’ve been coaching in Fullerton for over 20 years, and I’ve watched this movie too many times:

A motivated person buys twice-a-week personal training. They make progress — for about six weeks. Then life happens. Work trip. Sick kid. Busy season. They miss sessions they already paid for. Progress stalls because **two hours a week was never enough to change a body in the first place.** They get discouraged. They quit. And they tell their friends, “I tried working with a trainer. It didn’t work.”

The training worked fine. The *math* didn’t.

Here’s the part nobody in the fitness industry wants to say out loud:

**Your body does not change based on how much you pay per session. It changes based on how many sessions you actually show up to.**

I call it **The Frequency Effect.** Once you see it, you can’t unsee it:

- Twice a week *maintains*. Four times a week *transforms*.  
- The best program in the world, done twice a month, loses to an average program done four times a week.  
- Every client I’ve ever seen completely change their body had one thing in common. Not genetics. Not money. **Frequency.**

So ask yourself: at **[$75 to $150]** a session, how much frequency can *you* afford?

Two sessions a week? That’s eight a month. Meanwhile, the person paying **$197 a month** for Unlimited BootCampFX is showing up four, five, even six times a week. Seventeen to twenty-six coached sessions a month.

They’re not getting 3× the coaching ego. **They’re getting 3× the reps.** And they’re paying a fraction of private-training money for the privilege.

That is why I turn down **[$1,200]**-a-month clients. The honest thing to say is:

**“Don’t hire me for two hours a week. Come train with me for $197, as often as you want, and let frequency do what frequency does.”**

### What BootCampFX Unlimited actually is

Not a gym membership. A gym sells access to equipment and hopes you never show up.

Not an app. An app doesn’t know your name.

This is **[15]** coached group sessions a week at Acacia Park in Fullerton — early, mid-morning, and evening blocks — programmed and coached by me, in person, outdoors, rain or shine.

You show up as often as you want. Every session is coached. Every movement scales to your body — I’ve got people rebuilding bad knees training next to former athletes in the same class, different versions of the same workout. That’s not generic. That’s *scalable.* Twenty years is what makes the difference invisible.

And the part that matters more than the programming:

**The group notices when you’re gone.**

That is what people are actually paying four figures a month for when they hire a personal trainer. Accountability. Expectation. A reason to show up when motivation is asleep.

You can have that for **$197**.

### The math (the whole point)

| | Personal Training (2×/week) | BootCampFX Unlimited |
|---|---|---|
| Monthly cost | **[$600 – $1,200]** | **$197** |
| Coached sessions/month | 8 | 17–26+ (your choice) |
| Cost per session | **[$75 – $150]** | **As low as ~$9** |
| Who programs it | Me | Me |
| Who coaches it | Me | Me |

One hour of personal training with me costs the same as **[about twelve days]** of Unlimited BootCampFX.

Over a year, the Unlimited member training 4× a week instead of paying for 2× personal training keeps **[$4,800 to $12,000]** in their own pocket — and gets more than double the coached reps.

### “Why is it so cheap? What’s wrong with it?”

Fair question. Group training is efficient. I can coach a small group in the same hour I used to coach one person. I pass that efficiency to you.

I’d rather have **[40]** Unlimited members who show up for five years than **[8]** personal-training clients who quit in four months. Stable business for me. Price that doesn’t make you wince for you.

### What you get for $197/month

- Unlimited coached sessions on the weekly board  
- Every movement scaled to you  
- Priority coaching and check-ins  
- The advanced nutrition framework  
- **[Private 45-minute onboarding assessment — CONFIRM]**  
- A group that notices when you’re gone  
- 30-Day “Love It Or Leave It” Guarantee  

### The guarantee

Train with us for 30 days. Come as often as you can. If you aren’t stronger, moving better, and looking forward to the next session — or you decide it isn’t for you — tell me. Every penny back. No retention specialist. The risk is mine.

### The catch

I cap new Unlimited memberships at **[N]** per month. Groups stay small on purpose. When the month’s spots are gone, you wait. The 5:30 AM session fills first.

### What to do right now

**Step 1:** Claim your free 7-day trial. No credit card.  
**[FREE WEEK = SMS and/or FORM — your Q]**

**Step 2:** If you already know, lock in Unlimited at $197/mo.  
**[LIVE PAYPAL — Most Popular card]**

Either way, do something. The Frequency Effect doesn’t care about intentions. It only counts sessions.

See you at the park,  
Curtis Ludlow  
BootCampFX  
Acacia Park — 1636 Fullerton Creek Drive, Fullerton, CA  
support@bootcampfx.com  

**P.S.** — Unlimited access. Coached every time. 30-day guarantee. $197 a month. The only fitness plan in Fullerton that costs more is the one you’re currently not using.

**P.P.S.** — Already paying a trainer $600+ a month? Keep your money. Take the frequency. I’d rather coach you twenty times a month at $197 than eight times a month at $1,200 — because the first version of you actually changes.

---

## 8. FAQ adds/edits (proposed)

1. **I’m really out of shape. Will I survive?** — Keep Sites/Vlad answer (scale everything).  
2. **Why is Unlimited only $197?** — Efficiency + Frequency Effect; decoy PT card explains the alternative.  
3. **Why is Starter greyed out?** — **[depends on Q3A reason line]**  
4. **Can I still get personal training?** — Mostly no / waitlist; Unlimited is what I recommend; **[your PT grey reason]**.  
5. **Is there a contract?** — Month-to-month; free week; 30-day guarantee.  
6. **Where / when?** — Keep schedule truth from `#schedule`.  

**[Q19] Any FAQ you want forced in or killed?** ______

---

## 9. Honest Filter retune (proposed bullets)

**Thrive if**  
- You’re 20–80 and done starting over  
- You can give frequency a chance (2–3+ sessions/week, ideally more)  
- You want a coach who knows your name  
- Outdoors > fluorescents  
- Numbers > mirror selfies  

**Save your money if**  
- You want a $10 keycard you’ll never use  
- You only want 2×/month and a clear conscience  
- You need it to be easy (it’s simple; it isn’t easy)  
- You’re shopping for the cheapest logo, not the most sessions  

---

## 10. Build sequence (AFTER you approve — not started)

1. `git pull` main  
2. Rebuild `#membership` → 3 cards (grey / live / grey)  
3. Wire PayPal $197 only + onApprove + error/cancel  
4. Apply approved copy section-by-section (architecture no-touch list)  
5. Local verify script + raw.githubusercontent MD5 + live phrase greps  
6. Push main only after your **APPROVED FOR BUILD: YES**  
7. SITREP with commit SHA  

**Out of scope until ordered:** challenge page, footer legal rewrite, Google Sites edit, killing the $97 PayPal plan in PayPal admin.

---

## 11. Decision checklist (reply block)

Copy everything below the line into your reply and fill it.

---

**Q1 PT decoy price display:** A $1,200/mo / B $600–$1,200/mo / C $150/session / D $75–$150/session / OTHER: ______  

**Q2 Unlimited per-session math line (public):** ______  

**Q3 Private onboarding assessment on Unlimited:** INCLUDE FREE / CUT / SEPARATE PAID $______  

**Q4 Monthly new-Unlimited cap number N:** ______  

**Q5 Leave /challenge/ untouched:** YES / NO  

**Q6 Grey button click scrolls to Unlimited:** YES / NO  

**Q7 PayPal plan P-5LX… verified $197/mo in your PayPal:** YES / NO / WILL CHECK  

**Q8 onApprove intake form:** A Sites form / B current bootcampfx.com form  

**Q9 Hero treatment:** 1 full Halbert H1 / 2 letter below proof / 3 hybrid  

**Q10 Public name “The Frequency Effect”:** YES / NO / RENAME: ______  

**Q11 PT rate band $75–$150 & $600–$1,200 printable:** YES / NO / NUMBERS: ______  

**Q12 Year savings $4,800–$12,000:** KEEP / CUT / CHANGE: ______  

**Q13 Dogs / wife / Sienna line:** YES / NO / SOFTEN  

**Q14 “Turn down $1,200 clients” claim:** YES / NO / SOFTEN: ______  

**Q15 Sessions/week on the board:** 15 / OTHER: ______  

**Q16 “40 Unlimited vs 8 PT” line:** YES / NO / CHANGE: ______  

**Q17 30-day guarantee text OK vs real policy:** YES / TWEAK: ______  

**Q18 #standard section:** LIGHT / FULL / LEAVE  

**Q19 FAQ forced in/out:** ______  

**Starter grey reason:** A / B / C / OTHER: ______  

**PT grey reason:** A / B / C / OTHER: ______  

**Unlimited display name:** Unlimited / Elite Unlimited / OTHER: ______  

**Unlimited badge:** Most Popular / Best Value / OTHER: ______  

**Free week CTA:** KEEP SMS / SITES FORM / BOTH  

**SMS fallback under live $197 button:** YES / NO  

**Hosted PayPal backup link under button:** YES / NO  

**APPROVED FOR BUILD:** YES / NO / YES WITH EDITS  

**EDITS:**  
______  

---

## 12. Drago notes (cost / risk)

1. **Decoy ethics:** Grey labels must not imply a broken checkout or a false “sold out” if you’re still selling Starter off-page. Prefer honest scarcity/availability language (Q Starter grey reason).  
2. **Price whiplash:** Anyone who saw $249/$299/$429 yesterday will see $197 Unlimited tomorrow. Have a one-line story (“simplified the menu; Unlimited is the offer”) ready for members who ask.  
3. **$97 plan still exists in PayPal.** Greying the page does not cancel the plan. If you want it truly unbuyable, disable/hide the plan in PayPal too — separate action.  
4. **Google Sites still sells $97 live** with alert-only onApprove. This markup is for **bootcampfx.com** only unless you order Sites parity.  
5. **No deploy until your email reply.** Markup pass complete.

---

*— Drago*  
*Standing by for your answers on this thread.*
