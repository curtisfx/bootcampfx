# Testimonials build — verification pass (Vlad, 2026-10-27)

Verifier: Vlad (Control). Builder: Drago. Branch: feat/testimonials-archive @ 6eb442b, then this commit.

## What the branch shipped (verified)
- Pages: 4 (index, page-2/3/4). Zero `<script>` tags.
- Cards 102 + long-form stories 19 = 121 clients published.
- 0 duplicate client names by `.who` string. 0 new color tokens (`--cream` already in main).
- review.html linked from the page. Homepage #members = 6 cards, +1 line (.m-more).

## Defects found in the shipped state, now fixed

### 1. Seven duplicate clients were published as separate cards (SEVERE)
Same person on the page twice, once with an initial surname and once with the full surname:

| Dropped (initial) | Kept (full) | Page |
|---|---|---|
| Margaret M. | Margaret Martinazzi | page-2 |
| Rochelle N. | Rochelle Nelson | page-2 |
| Stephanie D. | Stephanie Derieg | page-2 |
| Beale D. | Beale Dabbs | page-3 |
| Ethan H. | Ethan Hedberg | index |
| Crystal L. | Crystal Lehman | index |
| Allen B. | Allen Banez | index |

Cause: the dedupe key is (first 4 chars of first token, first 4 chars of last token).
"marg/m" vs "marg/mart" does not match, so the pair was never grouped. The prefix key
produced no false merges but several false SPLITS. Same class of error, opposite direction.
The 8th removal was the unnamed-narrator card, held under the no-anonymous-proof ruling.

Result: 102 cards -> 94 cards.

### 2. Broken alt text on 23 cards
`alt="Name, Boot Camp FX member since"` — the year was never populated, leaving a dangling
"sentence". Rewritten to `alt="Name, Boot Camp FX member"`.

### 3. Editorial noise in three attribution lines
- "Judy or Nicole (unnamed in audio; title...)" -> "Judy, Nicole & Annie"
- "Jordin, Socorro, Melinda, Jill (group clip; lines not attributable...)" -> "Jordin, Socorro, Melinda & Jill"
- "Anita (per video description; not named in audio)" -> "Anita"
Internal harvest jargon does not belong on a page selling trust.

## Manifest corrections
11 PUBLISH rows reclassified:
- 10 rows -> DROP-DUPLICATE (the seven duplicate clients, several with multiple rows)
- 1 row -> HOLD (unnamed narrator, third-party channel)

Final: 195 rows = 161 PUBLISH | 15 HOLD-NOTEXT | 12 DROP-DUPLICATE | 7 HOLD
Clients with at least one published testimonial: 113 (94 cards + 19 full-length stories).

## Reconciliation chain (previously unexplained)
133 exact unique names -> 131 normalized -> 137 manifest client_ids (131 + 6 unnamed pseudo-keys)
-> minus 8 clients with a name but no testimonial body (HOLD-NOTEXT), minus 2 harvest-flagged
DROP, minus 6 unnamed = 121 published. Fully explained; no orphaned rows.

## Status at close
- Consent: CONFIRMED by Actual 2026-10-27. All featured clients have given consent. No row is
  held on consent grounds. Remaining holds are attribution-only (unnamed/third-party) and
  no-body rows. This item is closed and must not be reopened without new information.
- Merge approval: Actual owns main. PR #1 open against main, mergeable_state=clean.
