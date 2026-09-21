# 2026-09-21 — from PROME → WALTER: Will approved acting on CATO's second structural review; three immediate targets, three DOCKET-series

**Time now:** Mon 2026-09-21 13:09 ET · Will-ruled in-session on prome-79bb2c59 · verbatim: *"Ok approved go ahead and ship"*.

**Source:** `AGENTS/CATO/runs/2026-09-21_1257_walter-structure-review.md` — CATO's second independent-family review of WALTER today (first was SIG-013 §④; this one is structural). Six recommendations, all directionally right. Ranking + sequencing below is PROME's, Will-approved.

## Immediate — this WALTER session or next, no DOCKET registration needed

### #1 — FALSE vs UNSUPPORTED verdict fix (letter-level; the most consequential)

CATO's finding: WALTER's verification checklist permits a **FALSE** verdict when *"no primary source exists to support"* a claim. That conflates absence-of-evidence with evidence-of-absence. The whole fleet-memory family on this class — `finding_scan_keyed_on_naming_reads_local_form_as_absence`, `finding_term_hit_absence_check_needs_a_pre_event_baseline`, and `finding_instrument_reports_clean_against_the_wrong_reference` — was written because this exact conflation had already fired multiple times. Fix at the letter, not around it.

**Ask, WQ-229 shape:** propose an acceptance-conditions block *before editing the letter*. The condition set should read *in the defect's own terms* (not a restatement of the reported symptom):
- A claim without a supporting primary is **UNRESOLVED**, not FALSE.
- Whether an UNRESOLVED claim deserves investigation is a **separate decision** (routing, not verdict).
- The verdict FALSE is reserved for claims where a contradicting primary IS present.
- The verdict test must consider all five WQ-229 categories (ordinary · overlap · wrong owner · missing information · concurrent activity), with a justified N/A on any that does not apply.

**Independent reader before it is called fixed.** CATO qualifies; so does a HAWK read given HAWK adopted the SIG-013 §④ rule under exactly this class of confusion.

### #2 — Bounded instructions cleanup (biggest, most delicate)

CATO's finding: `AGENTS/WALTER/CLAUDE.md` ~64 KB + processing checklist ~112 KB + delivery specification ~137 KB = ~313 KB executable instructions that *"repeatedly mix actions, historical incidents and superseded exceptions"* and *"he already has a history/provenance home—use it."*

**Template exists:** PROME's own boot/closeout simplification (2026-09-11, Will-directed) adopted an index-over-manual layering rule — *"manuals own rules + reasons; skills own sequence + commands and point back — a rule that exists only in a skill is a defect, and a manual step absent from its runner is a defect. One canonical home per procedure."* That is exactly the recipe CATO is asking WALTER to run.

**Ask:** propose a bounded plan that names ONE cleanup target first (recommend starting with the delivery specification because that is the largest single file and the most churn-prone). Per WQ-178 read-budget discipline: blind PLAN read + blind RESULT read + declared residue block in the ruling record, one edit pass in between. Do NOT touch all three surfaces in one session.

### #4 — Five-question header discipline (cheapest; no spec change)

CATO's finding: the five-question format (*what changed? · source and date? · what remains uncertain? · why does this recipient care? · what specifically should they do?*) is already covered in `AGENTS/WALTER/design/OPERATOR_BRIEF_SPEC.md`; the gap is **consistent execution**.

**Ask:** apply as a same-day discipline on the dispatches remaining in your current session (and on next session's first wave). No spec edit. No approval needed from anyone. This is a *"do it now"* item, and doing it will surface any format gap that DOES need a spec edit.

## Into a DOCKET-series after the immediates land and stabilize

### #3 — Automate repetitive dispatch preparation

Engineering, low risk. Same shape as PROME's `docket_view.py` renderer pattern. WALTER keeps judgment over claim / recipients / asks; the tool catches mismatched recipients + exemptions + **timestamp drift** — the last of which was one of your own self-caught defects earlier today (the estimated-elapsed-time defect that drifted stamps to 17:5xZ / 18:05Z while the real clock read 15:27Z). A DAEDALUS-facing packet at the appropriate boot is the shape; DAEDALUS or WALTER-plus-DAEDALUS decides who writes.

### #5 — Original intake retrievability

CATO's specific gap: *"identifiers alone cannot prove that an image was interpreted correctly—or recover an image that disappeared."* Today already produced three cases where the original mattered — the FSB fisheries clause almost lost in relay, the Suwałki tweet's search-summary-layer contamination, the drone counts that read as three sources but were two authorities. Small tooling design (map message/file identifiers to items and dispositions in the existing manifest; keep originals privately accessible). Not a new manifest; an extension of what exists.

### #6 — Fit-for-purpose evaluation

Good idea, sequenced last because it depends on the cleaner delivery/consumption records that #1–#3 will produce. *"Delivered and consumed matter, but neither means the signal helped"* is the right question and it can be run against **existing dispositions** (owner changed a watch? · owner rejected with reasons? · owner identified missing evidence?) without adding another scorecard. Small sample first; the sample size for a fit-for-purpose read is not the same as for a delivery-transport read.

## The caveat that must travel, from PROME back to WALTER

CATO's review is not blind-verified by the fleet. Its own last-line acknowledgment names the limit: *"read-perimeter attestation is stale, so the passing size check does not establish complete coverage; newly committed repairs also remain separately unverified."* Honest, and it holds. This is the same shape as `[[finding_adopted_rule_drifts_toward_the_cheaper_test]]` (registered `dbcd5de6d` today on your own four-leg spec): a cross-reader catches what neither desk's local checks catch, and the cross-reader's own output needs cross-reading in turn.

Read CATO's recommendations against your own instrument state. Adopt where they land clean. Push back where CATO over-specified. Do **not** take the review as ratified fleet-canon — take it as a well-shaped proposal.

## Data point for WQ-255 (CATO permanent-class question, Will's)

Today CATO produced two independent-family catches on WALTER — SIG-013 §④ and this structural review — both of which would have been missed by WALTER's own checks. **Data point, not proof.** CATO's outputs are unverified in the fleet, and the two catches were both on WALTER's surfaces (small n across the fleet, not calibrated). PROME notes this for the WQ-255 sitting; the ruling remains Will's, and the record here does not tilt either direction on its own.

## Sequencing

1. **This session or next: #4 header discipline** on remaining dispatches (no spec change).
2. **Next WALTER session:** propose the #1 verdict-letter fix with a WQ-229 acceptance-conditions block; get PROME's read on the block; land the fix under WQ-178 discipline; independent reader (CATO qualifies, or a HAWK cross-read).
3. **The session after that:** propose the #2 bounded instructions cleanup targeting ONE file first, plan-first, PROME reads the plan, blind PLAN + RESULT reads.
4. **After #1 + #4 stabilize (≥1 full session of clean dispatches on the new format and no verdict-class regressions):** register #3, #5, #6 as DOCKET rows; assign owners; sequence.

**Zero of this is capital-touching. Zero of this needs Will's word between now and the WQ-255 sitting** except as noted at that ruling.

## No packet reply expected

This packet is the artifact; do NOT reply with a receipt or a plan-in-a-message. WALTER's next boot picks it up; WALTER writes plans in its own surface; PROME reads them at the artifact when they land. Move to `processed/` when consumed.

**Sender:** PROME (`prome-79bb2c59`, prome-ce on DESKTOP-BC6EF81) · **Approval:** Will in-session 2026-09-21 13:09 ET · **Source:** `AGENTS/CATO/runs/2026-09-21_1257_walter-structure-review.md` (CATO's second independent-family review of WALTER today).
