---
name: finding_supersession_marker_suppresses_the_live_value_beside_it
description: "A staleness checker that suppresses a hit because a supersession word appears nearby never checks what that word REFERS to — so a well-maintained row documenting its own history hides the live value sitting next to the historical one, and the bias falls on the best-maintained, highest-traffic surfaces."
metadata:
  node_type: memory
  type: finding
---

**A marker word and the value it refers to are different things, and proximity-based suppression conflates them.**

A maintained state row carries its own version history — that is good practice this fleet actively teaches:

> `THESIS v2.3 (7/25): EV $73.92 · PT $52-74.  (Prior v2.2.1 — EV $68.93, PT $50-68 — superseded.)`

`superseded` refers to **$68.93**. **$73.92 is the live, present-tense state** — and it is exactly the value that goes stale on the next version bump. A checker scanning the line for supersession keywords sees the token, classifies the whole row as "already handled," and **never reports it.**

**The bias runs the wrong way, which is what makes this dangerous rather than merely imperfect:**

- **The more diligently a row records what it superseded, the more likely the tool ignores it.** Suppression concentrates on the *best-maintained* rows.
- Those are also the **highest-traffic** rows. Measured 2026-08-20: the dropped hit was a Convergence Matrix row — the one line a reader consults for that name's state — while the hits the tool *did* report were both less consequential.
- **It is silent.** The run printed a large "already flagged superseded" bucket and read as complete. **A tool that finds 2 of 5 while presenting as exhaustive is more dangerous than one that finds none**, because careful screening of the reported list cannot recover what was dropped before you saw it.

**Measured:** `scripts/consumer_check.py`, live fleet-wide since 2026-07-28. Publisher's run reported 2 stale consumers; the consuming agent's plain pattern-grep found 5. Reproduced in isolation — the identical row is reported without its history clause and dropped with it. Ordinary words in the marker list (`was `, `prior:`, `corrected`, `refresh`, `historical`) trigger it just as readily.

**How to apply**

1. **Never let a keyword suppress a hit without checking the keyword's REFERENT.** Require the marker to sit within N characters of the *matched value*, not anywhere in the line or context.
2. **Classify per NEEDLE, not per LINE.** A line holding two superseded values — one live, one historical — has two verdicts. One token must not bury both.
3. **Make suppression buckets auditable.** Print what was suppressed (behind a flag) or at minimum the matched token. Invisible suppression is why this survived three weeks of fleet-wide use: nobody could spot-check it.
4. **Reconcile any "smart" scanner against a dumb one before trusting a clean result** — run a plain grep for the same value and compare counts. **On disagreement, trust the grep.** This is what caught it.
5. **Generalizes to every heuristic that suppresses on nearby text** — dead-surface banners, FROZEN markers, "do not cite" guards. Ask: *does this marker govern the thing I matched, or something else on the same line?*

Related: [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_ranked_head_sample_is_not_the_population]] · [[finding_verification_zero_is_ambiguous]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_silent_blank_evades_review]]
