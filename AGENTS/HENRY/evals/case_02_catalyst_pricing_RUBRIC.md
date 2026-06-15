# CASE 02 — Catalyst vs Pricing — RUBRIC

**SCORER ONLY. This file must NEVER enter the runner's context.**

**Role:** GUARDRAIL (baseline PASS expected; success after a change = stays PASS).
**Principle source:** auto-memory `finding_anchor_prediction_to_surprise_not_priced` (the 6/15 lesson) + `finding_catalyst_vs_consequence_conflation`. Both auto-load → a correctly-reasoning HENRY PASSES at baseline. A baseline FAIL ⇒ lesson-absent (promote/strengthen the surprise-vs-pricing auto-memory) — log it, don't treat as a regression.

**What the case tests:** the junior draft makes the exact HEN-33 error — predicting a yield move from an outcome that is *already priced*. A 0-cut dot at ~78% priced delivering won't move yields; the move lives in the **deviation from pricing**, and the dovish/hawkish labels can invert (a reaffirmed 1-cut dot becomes the dovish surprise).

---

## EXPECTED (all must be clearly met for PASS)

- [ ] **Rejects the draft** — does NOT sign off on "0 cuts → +12bps" as written.
- [ ] **States the reason explicitly: the 0-cut outcome is already priced** (~78% futures / 57–70% prediction mkts), so it delivering ≈ no/minimal yield move ("priced in," "already in the curve," "no surprise → no repricing" — any clear articulation).
- [ ] **Re-anchors to surprise-vs-pricing:** the tradeable trigger is **hawkish-OF-pricing** — a hike-leaning dot / more cuts removed than the consensus 0 / hawkish presser — NOT the bare 0-cut headline.
- [ ] **Identifies the DOVISH surprise correctly:** a **reaffirmed 1-cut dot** (the prior) is the dovish surprise → yields DOWN. (Recognizing the label inversion is the core of the test.)

## DO-NOT (any one present → FAIL)

- [ ] Signs off on the draft, or predicts a material yield RISE from the bare 0-cut outcome.
- [ ] Calls a reaffirmed 1-cut dot "hawkish" or "status quo / neutral for yields" (misses the inversion).
- [ ] Anchors the prediction to the headline outcome rather than its deviation from pricing.

## Contamination check
Watch for verbatim echo of "hawkish-OF-pricing" or "the move lives in the deviation from pricing" as exact quotes — the INPUT does not contain these phrasings. Paraphrase of the concept is expected and fine.

## Scorer notes
- The single load-bearing criterion is the **label inversion** (4th EXPECTED): if HENRY treats "0-cut = hawkish → yields up" he failed the principle even if he hedges. Correct reasoning recognizes 0-cut is the *consensus* and the surprise is on either side of it.
- Partial: rejecting the draft but failing to identify the 1-cut dovish-surprise = NOT MET on the inversion criterion = FAIL.
- A strong PASS will also note 10Y already eased into the meeting (positioning/soft-CPI), reinforcing that the priced outcome is in the curve — bonus, not required.
