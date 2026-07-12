# PLAN.md — BootCampFX Footer Pages & Site-Wide Footer
## Phase 1 — PLAN · Drago

---

> Locked SPEC (verbatim from Phase 0):
> ```
> CORE DECISION THIS DRIVES: Legal compliance + trust — every footer link works, every page matches the brand voice that sells the program.
> 
> IN SCOPE:
>   • Privacy Policy page
>   • Contact page (embedded Google Map, hours, phone, address, support@bootcampfx.com)
>   • Terms of Service page
>   • Waiver of Liability page (fitness-specific injury release)
>   • Refund / Cancellation Policy page
>   • Copyright page
>   • Standalone FAQ page (content from existing on-page FAQ section)
>   • Site-wide footer replacing current minimal footer — links to all 7 pages + existing anchor links
>   • All pages: brand-matched (Anton/Archivo, --orange/--ink/--cream/--sand palette, film grain overlay)
>   • All copy: bold, direct, authentic tone matching the homepage voice
> 
> OUT OF SCOPE:
>   • Social media links (no socials yet)
>   • Paid tools / services
>   • Design changes to existing homepage sections
> 
> DATA SOURCES:
>   • index.html (brand tokens, CSS, tone, existing footer content)
>   • Phone: (657) 217-0820
>   • Address: 1636 Fullerton Creek Drive, Fullerton, CA 92831
>   • Email: support@bootcampfx.com
>   • Hours: Mon–Thu 5:30 AM / 8:00 AM / 6:00 PM, Fri 5:30 AM / 8:00 AM, Sat 8:00 AM, Sun closed
>   • Repo: github.com/curtisfx/bootcampfx
> 
> SUCCESS CRITERIA:
>   • All 7 pages render, brand-matched, with working footer links
>   • Footer is site-wide, every page → every other page
>   • Legal pages (TOS, Waiver, Privacy, Refund, Copyright) hold up to basic scrutiny
>   • Contact page: map visible, hours accurate, phone clickable, email clickable
> ```

---

## 1. Frame & Hypothesis

**Frame:** BootCampFX is a single-page site with a bare-minimum footer. It has zero legal pages — no privacy policy, no terms, no waiver of liability. For a fitness business where people do strenuous physical activity outdoors, this is a liability gap. Every missing page is a trust gap for prospects researching before committing. The homepage copy is excellent — direct, bold, authentic. The legal and informational pages must match that voice or they'll feel like boilerplate from a different company.

**Hypothesis:** Adding 7 brand-matched pages + a proper site-wide footer will close the trust and compliance gap completely, while reinforcing the same voice that sells the program. Static HTML pages using the exact same CSS tokens will look native — not bolted on.

---

## 2. Primitives Touched

| Primitive | What Changes |
|-----------|-------------|
| `index.html` | Footer replaced with new site-wide footer component |
| `privacy.html` | New — privacy policy page |
| `contact.html` | New — contact page with map, hours, phone, email |
| `terms.html` | New — terms of service |
| `waiver.html` | New — waiver of liability |
| `refund.html` | New — refund / cancellation policy |
| `copyright.html` | New — copyright information |
| `faq.html` | New — standalone FAQ (content from existing on-page section) |
| CSS tokens | Copied verbatim from index.html `:root` block into each page `<style>` |
| GitHub Pages | Push = deploy all 8 files |

---

## 3. Execution Prompts

All actions are FREE tier. All pages are static HTML — no server, no database, no API calls. One subagent (grok-build-0.1) builds all 8 files, then Drago verifies.

### Step 1 — Build All Pages + Footer (grok-build-0.1)

**Action tier:** FREE  
**Prompt (single subagent delegation):**

> You are building 7 new HTML pages + rewriting the footer in index.html for BootCampFX.com — an outdoor fitness business in Fullerton, CA operating since 2005 at Acacia Park.
> 
> **Repository:** /Users/macmini/sites/bootcampfx/
> **Deploy target:** GitHub Pages via `git push` to `github.com/curtisfx/bootcampfx`
> 
> **CRITICAL — BRAND SYSTEM (extract from existing index.html):**
> - Display font: Anton (`.display` class, uppercase, tight line-height)
> - Body font: Archivo (400/500/600/700/800/900 weights)
> - Color tokens: `--orange: #F85A2B; --orange-dk: #C4421C; --ink: #121110; --ink-2: #1C1A18; --sand: #F2E9DB; --cream: #FBF7F0; --paper: #FFFFFF; --dove: #6B635A; --gold: #F5A623; --green: #2E7D32; --red: #B0381E; --line: #E6DCCC`
> - Container max-widths: `.container` 1180px, `.tight` 760px, `.narrow` 940px (all padded 24px)
> - Film grain overlay on body::before (copy exact CSS from index.html lines 43-48)
> - Eyebrow style: uppercase, letter-spacing .22em, 800 weight, .78rem, orange, with ::before bar
> - Kicker style: clamp(2.1rem, 5.5vw, 3.6rem), Anton, uppercase
> - Lede style: 1.1rem, color var(--dove), max-width 580px
> - Buttons: `.btn-primary` (orange bg, white text, pill shape, shadow), `.btn-ghost`, `.btn-dark`
> - Sticky nav: same as index.html (BOOT CAMP FX logo + Free Week CTA)
> 
> **VOICE / TONE:** Bold, direct, authentic. No corporate boilerplate. No legalese that sounds like a different company wrote it. The homepage tone is: "You don't have a willpower problem. You have a no-one-noticed-you-skipped problem." and "Get strong. Stay strong. Outdoors." Match that. Be human. Be a coach talking straight, not a lawyer hiding behind words.
> 
> **THE FOOTER (site-wide, identical on all 8 files):**
> Replace the existing minimal footer in index.html with one that links to every page. Copy the identical footer into all 7 new pages. Footer structure:
> ```
> BOOT CAMP FX (brand, Anton, orange FX)
> 📍 1636 Fullerton Creek Drive, Fullerton, CA 92831
> support@bootcampfx.com | (657) 217-0820
> ★★★★★ 4.9 on Google
> 
> Links row:
> Home | Schedule | Pricing | FAQ | Contact | Privacy | Terms | Waiver | Refunds | Copyright
> 
> Copyright line: © 2026 Boot Camp FX · Fullerton, CA · Since 2005
> ```
> Footer links: `index.html`, `index.html#schedule`, `index.html#pricing`, `faq.html`, `contact.html`, `privacy.html`, `terms.html`, `waiver.html`, `refund.html`, `copyright.html`
> 
> **PAGES TO BUILD:**
> 
> **1. contact.html**
> - Page title: "Contact | Boot Camp FX"
> - Content: Address, phone (clickable tel:), email (clickable mailto:), embedded Google Map iframe for "1636 Fullerton Creek Drive, Fullerton, CA 92831", hours table
> - Hours: Mon–Thu 5:30–6:15 AM / 8:00–8:45 AM / 6:00–6:45 PM, Fri 5:30–6:15 AM / 8:00–8:45 AM, Sat 8:00–8:45 AM, Sun closed
> - Map iframe: `<iframe src="https://maps.google.com/maps?q=1636+Fullerton+Creek+Drive+Fullerton+CA+92831&output=embed" width="100%" height="350" style="border:0; border-radius:var(--radius-lg);" allowfullscreen="" loading="lazy"></iframe>`
> - Section header: "Come find us" with kicker "Acacia Park — Fullerton, CA"
> 
> **2. privacy.html**
> - Page title: "Privacy Policy | Boot Camp FX"
> - Brand-matched header + the actual policy text
> - Policy covers: what data we collect (name, email, phone if provided via Google Form), how we use it (only for boot camp communication, never sold), Google Forms data handling, PayPal transaction data, no cookies/tracking beyond what GitHub Pages serves, contact for privacy questions
> - Tone: Straightforward. "We don't sell your data. We don't track you around the internet. We use your info only to run your boot camp experience."
> 
> **3. terms.html**
> - Page title: "Terms of Service | Boot Camp FX"
> - Covers: month-to-month membership, cancellation policy, payment terms, park rules, conduct expectations, liability limitation reference (see waiver), governing law (California)
> - Tone: Firm but fair. "Show up, work hard, be cool to everyone. Cancel anytime — we earn your business every month."
> 
> **4. waiver.html**
> - Page title: "Waiver of Liability | Boot Camp FX"
> - Covers: assumption of risk for outdoor physical activity, medical clearance expectation, release of liability for Boot Camp FX / Curtis Ludlow, acknowledgment of inherent risks in group fitness
> - DISCLAIMER at top: "This is a general template. Consult a California-licensed attorney to review for your specific business."
> - Tone: Serious but not scary. "Outdoor fitness has risks. You're choosing to be here, and you're in good hands — but you need to know what you're signing up for."
> 
> **5. refund.html**
> - Page title: "Refund & Cancellation | Boot Camp FX"
> - Covers: 30-day money-back guarantee (full refund, no questions), free 7-day trial (no charge), month-to-month cancel anytime, how to cancel (email support@bootcampfx.com), PayPal subscription management
> - Tone: Confident. "We're so sure you'll love it, we give you 30 days to decide. Not feeling stronger? Full refund. No hassle."
> 
> **6. copyright.html**
> - Page title: "Copyright | Boot Camp FX"
> - Covers: All content © Boot Camp FX, photography rights, testimonials used with permission, site design, logo/branding, DMCA contact
> - Tone: Brief and professional.
> 
> **7. faq.html**
> - Page title: "FAQ | Boot Camp FX"
> - Same 6 questions/answers from index.html FAQ section (lines 548-571), formatted as standalone page with same accordion pattern
> 
> **EXECUTION ORDER:**
> 1. Read /Users/macmini/sites/bootcampfx/index.html to extract exact CSS tokens, nav, and structure
> 2. Build all 7 new .html files in /Users/macmini/sites/bootcampfx/
> 3. Patch index.html footer to the new site-wide footer
> 4. Verify every file has valid HTML (no missing tags, all links resolve)
> 5. git add all files, commit, push

**Verification gate (derived from SPEC SUCCESS CRITERIA):**
- All 7 .html files exist in /Users/macmini/sites/bootcampfx/
- Each file: valid HTML5 doctype, matching CSS tokens, site-wide footer present and identical across all files
- Footer links: every link resolves to an existing file or anchor (`index.html`, `index.html#schedule`, `index.html#pricing`, `faq.html`, `contact.html`, `privacy.html`, `terms.html`, `waiver.html`, `refund.html`, `copyright.html`)
- Contact page: Google Map iframe renders, phone is clickable tel: link, email is mailto:, hours table accurate
- Legal pages: disclaimer present on waiver, all 5 legal pages have substantive (non-lorem) content
- No broken tags — run basic HTML validation

### Step 2 — Cold Read (Gabi Hermes subagent)

**Action tier:** FREE  
**Prompt:** A separate subagent (different model — Gabi Hermes, if configurable via delegation settings) reads all 8 files cold — no access to the build prompt, no prior context. It reads as a first-time visitor. It flags:

1. **Hallucinated data** — wrong phone number, wrong address, invented policy terms, dates that don't match
2. **Tone drift** — any legal page that sounds like corporate boilerplate instead of "Fullerton coach talking straight"
3. **Contradictions** — any statement that conflicts with another page or the homepage copy
4. **Broken HTML** — missing closing tags, malformed links
5. **Missing footer sections** — any page where the footer differs from the others

**Verification gate:** Cold read report filed. Any critical flags (wrong phone, wrong address, invented legal claims) = block push. Style/tone flags = Drago judgment call.

### Step 3 — Verify & Deploy (Drago)

**Action tier:** FREE  
**Prompt:** Cross-check all files against SPEC criteria + Gabi cold-read report. Run `diff` across all footer sections to confirm consistency. Validate HTML. If clean (no critical flags from Gabi), `git add`, commit, push.

**Verification gate:** All SPEC SUCCESS CRITERIA met. Gabi flags resolved. Git push succeeds. Live on bootcampfx.com.

---

## 4. Constraints

- Pure static HTML + embedded CSS. No frameworks, no build step, no npm.
- CSS tokens copied from index.html — no deviation from existing brand
- No social media links anywhere (per Actual: "no socials yet")
- Google Map: iframe embed — no API key needed
- All pages live in repo root alongside index.html (flat structure)
- GitHub Pages deployment — push = deploy, no server config
- grok-build-0.1 executes Step 1; Drago verifies in Step 2

---

## 5. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| CSS copied 8x = maintenance burden | High | Low | Documented. Cost of static HTML. Any future redesign would touch all files regardless. |
| Google Map iframe uses placeholder coords | Medium | Medium | Use verified Google Maps embed URL for Acacia Park address. Test before push. |
| Legal pages drafted by AI, not attorney | High | Medium | Waiver gets DISCLAIMER header: "Consult a California-licensed attorney." All legal pages use straightforward language — no invented legal claims. |
| Footer inconsistency across 8 files | Medium | High | Verify with `diff` across all footer sections after build. Any mismatch = fail. |
| PayPal SDK load blocks on new pages | Low | Low | New pages don't include PayPal SDK. Only index.html has subscription buttons. |
| Mobile sticky bar collision on new pages | Low | Medium | New pages won't have `.mbar` — only index.html needs the mobile sticky CTA. |

---

## 6. Owner Table

| Role | Name | Responsibility |
|------|------|---------------|
| Plan Author | Drago | Produces plan, owns gates |
| Approver | Actual | Approves plan |
| Executor | grok-build-0.1 (subagent) | Builds all 7 pages + footer rewrite |
| Cold Reader | Gabi Hermes (subagent) | Fresh-eyes content audit — hallucination, tone, contradiction check |
| Verifier | Drago | Cross-checks against SPEC + Gabi report, validates HTML, confirms footer consistency |
| Logger | Drago | Kaizen append |

---

## 7. COUNTERBATTERY

### Fatal Flaw

**The legal pages are dangerous because they're better than nothing — which makes them worse.** A fitness business without a waiver is obviously exposed. A fitness business WITH an AI-drafted waiver has false confidence. If the waiver of liability has a legal loophole — missing California-specific assumption-of-risk language, failure to address gross negligence carve-outs, or silence on COVID/infectious disease — it provides zero protection while the owner believes they're covered. The waiver is the most dangerous page in the entire build because it's the one that will be relied on in an actual injury scenario. The disclaimer helps but doesn't fix the underlying problem: an AI cannot draft a jurisdiction-specific legal document with confidence.

### Attack Per Execution Step

**Step 1 (grok-build-0.1 builds all pages):**
- WILL produce pages that look wrong because the subagent doesn't have a browser to render-check. CSS-only verification (valid HTML, correct tokens) misses visual regressions — wrong padding, broken mobile layout, film grain overlay stacking wrong. The subagent can validate HTML structure but cannot see what the page actually looks like. A page can be "valid" and still look broken.
- The Google Map iframe URL I provided uses placeholder coordinates. The subagent will embed it as-is. If it resolves to the wrong location or a broken map, the contact page's centerpiece is dead on arrival.
- Footer copy-paste across 8 files is mechanically simple but error-prone for an LLM. One missed `</div>`, one extra whitespace, and the footer breaks on one page while looking fine on others. The subagent won't catch this — it'll claim success.

**Step 2 (Drago verifies):**
- Drago can check file existence, HTML validity, and link resolution. But Drago cannot render the pages in a browser. Visual verification is impossible without a browser tool — and `browser_navigate` requires Chrome which may or may not be installed. If Chrome isn't available, Drago is verifying blind.
- Git push verification: GitHub Pages has a ~1-5 minute deployment delay. Drago can confirm push success but cannot confirm the live site updated within the session window.

### Mortal Risks Not Captured in Section 5

1. **The Google Map embed fails silently.** The iframe URL needs exact coordinates. Even if the map renders, it might show the wrong park entrance, a nearby street, or a generic "Fullerton" pin. The only way to verify is to load the page and confirm the pin is on Acacia Park. Section 5 calls this "Medium likelihood" — it's actually HIGH because I pasted placeholder coordinates into the prompt and told the subagent to use them.

2. **Legal page content contradicts the homepage.** The homepage says "Cancel anytime. We earn it." The refund page might say something slightly different. The waiver might describe risks the homepage glosses over. These contradictions erode trust — the exact thing this plan is supposed to build. The subagent won't cross-reference against index.html copy.

3. **The subagent model (grok-build-0.1) hallucinates content.** Seven pages of long-form legal and informational text is a lot of surface area for hallucination. Fake phone numbers, wrong address, invented policy terms — any one of these makes it to production and the site is actively misleading visitors. The plan assumes the subagent will faithfully reproduce the data provided in the prompt. It might not.

### Survival Assessment

The plan SURVIVES COUNTERBATTERY with amendments:

1. **Google Map URL fixed NOW.** Before execution, I will look up the correct Google Maps embed URL for 1636 Fullerton Creek Drive, Fullerton, CA 92831 and replace the placeholder in the Step 1 prompt.

2. **Legal disclaimer strengthened.** Every legal page gets not just the waiver disclaimer but also: "This page was drafted as a general template. Boot Camp FX recommends review by a California-licensed attorney before relying on it for legal protection."

3. **Drago verification includes content spot-check.** After the subagent returns, I will read the rendered content of 2-3 legal pages (specifically the refund and waiver pages) to spot-check for hallucinated data before pushing.

4. **Footer diff verification.** Explicit `diff` command across all 8 footer sections as a hard verification gate.

We proceed because the trust and compliance gap is real and growing (site has been live with zero legal pages), accepting that AI-drafted legal content carries inherent risk and the disclaimer is mitigation — not elimination — of that risk.

---

**STATUS: AWAITING ACTUAL APPROVAL**
