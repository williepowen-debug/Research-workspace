---
name: finding_corrective_inherits_the_anchor_it_corrects
description: "A reprice is framed as a move FROM the standing number, so the standing number sets the scale of the cut — and the corrective lands wrong in the same direction as the error it was correcting. Write the number cold, without the old one visible, and score the correction as its own row."
metadata:
  node_type: memory
  type: finding
symptoms: "cut it hard and it was still too high; the reprice cited the very record it failed to fix; decomposition confirmed the prior it was supposed to test; pre-registered reprice still wrong in the same direction; we corrected for overconfidence and were still overconfident; only the as-made value gets scored; the freshly-repriced row looks safest"
---

**A correction is sized against the number it is correcting. That makes it inherit the anchor, and it fails in the same direction as the original — usually by enough to matter.**

Every process gate fires on the *original* estimate and on *stale* rows. **Nothing re-grades the correction.** So the reprice — the step that just received the most attention, and therefore looks safest — is the one nobody measures.

**Measured case (LABOR, LAB-08, 2026-08-07 → 2026-08-28).**

A prediction stood at **65%** (as-made, 2026-02-18). Twenty-one days before its gate, the desk repriced it to **35%** — and by every process test this was *good* work:

- declared **pre-print**, with a commit as receipt (never claimable retroactively);
- **unforced** — no new data; the trigger was arithmetic nobody had run;
- **symmetric** — it would score badly if the outcome ran the other way;
- and it **explicitly cited the desk's own record — 0-for-4 at ≥60% on threshold calls — as its stated reason for cutting.**

The event printed in the band whose pre-committed assignment was **4%**.

**35% was ~7× the honest number. The corrective made *specifically because* this desk's threshold calls run too hot was itself too hot, in the same direction, by the same failure mode.**

**Why it happens.** A reprice is framed as a *move from* the standing value, so the standing value sets the scale. "65 is too high, cut it hard" produces 35, and a 30-point cut *feels* large **precisely because it is measured against 65**. The procedure never asks the independent question: *what would I write if I had never published 65?*

⚠️ **A decomposition does not rescue you, and this is the part worth remembering.** The card *did* decompose — bands × conditional probabilities, summing to ≈0.33. But **the band probabilities were themselves set beside the 65% prior**, so the "independent" derivation inherited the anchor and returned a number that confirmed it. **A decomposition anchored at its inputs looks like arithmetic and functions as a rationalisation.** The tell was visible and unread: the decomposition put **P = 0.275** on the band that actually occurred — 72.5% of the mass on bands that did not happen — while the same document claimed to be correcting for over-confidence. ⚠️ **VINTAGE QUALIFIER, added 2026-08-28 ~11:3x after recovering content I had destroyed unread: 0.275 is the FROZEN 8/07 card's §3 figure and is the correct one for SCORING. My LIVE pre-print view was better — on 8/27 I re-weighted to `P(<450K-or-up) = 0.65` on Berger + RED's primary verification. Both are real; they answer different questions. Saying "0.275 on the band that occurred" WITHOUT this qualifier understates my going-in calibration by ~2.4×.** ⛔ **This does NOT weaken the finding: the finding is about the 65% → 35% REPRICE being anchored, and 35% was ~7× the honest 4% regardless of what the band table said.** 

**Fix — two lines, both cheap:**

1. **Write the number twice.** Once as a move from the standing value; once **cold from base rates with the standing value not visible**. If they disagree by more than ~2×, **take the cold one and record both.** The disagreement is the finding.
2. **Score the corrective as its own row at resolution.** Books that score only the as-made value are structurally blind to a mis-calibrated repricing step — the correction is never wrong on any ledger, so the desk cannot learn that its corrections are too small.

**Scope note — this is not the stale-row sweep.** A stale-high-confidence sweep catches rows that have sat untouched for months. **This fires on the opposite case: the row that was just revised.** The two are complements, and the revised row is the one that escapes review, because attention already visited it. Partners with `finding_a_correction_pass_is_unreviewed_work` (fix passes carry a higher defect rate) — that one is about defects *in* the correction; this one is about the correction's **magnitude** being wrong in a predictable direction.
