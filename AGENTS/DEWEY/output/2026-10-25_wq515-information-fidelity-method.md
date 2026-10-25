# WQ-515: method for the one prospective information-fidelity batch

**Date:** 2026-10-25 | **Mode:** Cold (methods) | **Authority:** Will's WQ-515 A ruling, `PROME/proposals/2026-10-23_wq513-516-RULED.md`; DOCKET L828. **Status:** method delivered before sample selection; no transfers graded. **Confidence:** High on reproducibility of the definitions; untested as a measurement instrument.

## Key finding

Measure whether a recipient preserves the meaning and limits of an incoming finding. Score reasoned disagreement separately from information loss. This one batch can describe its observed transfers; it cannot establish a fleet-wide rate or a causal effect of additional handoffs.

## 1. Freeze the sample and evidence

WALTER owns selection: commit the selection rule before choosing a transfer; take the next ten qualifying ACTION dispatches from 2026-10-26 00:00 America/New_York, in dispatch order, stopping at ten or 2026-10-30 close. Eligibility requires a named ACTION owner and at least one source caveat in these four classes: contingent/current, inference/measurement, share/probability, base rate/predictor. No outcome-based skipping, replacement, or retrospective addition. WALTER specifies the exact close timestamp in its selection record. A smaller qualifying sample stays smaller. **Registration verified October 25:** `AGENTS/WALTER/outbox/2026-10-25_WQ515-prospective-selection-rule.md`, commit 046fd4ae5, adopts the rule before selection and explicitly excludes Sunday dispatches and Saturday's CATO example. Its "close" still needs an exact clock timestamp; no transfer or outcome was inspected to set this method.

For each selected dispatch, preserve signal ID, dispatch timestamp, source path and version, named owner, intermediate packet/BOARD paths and versions, destination record path/version once available, and the ordered handoff chain. A git commit plus path identifies committed text; for an uncommitted read, preserve the exact excerpt and SHA256 with its observation timestamp. A later correction is a separate version, not silently substituted for the source actually dispatched. Record missing provenance as UNKNOWN.

PROME commissions the one independent Sonnet reader under WQ-447 after WALTER's list and this note exist. The reader first inventories source qualifications and assigns their severities **without reading destination records**, then freezes that inventory before grading destinations. Historical examples below are calibration anchors only, never observations in this batch.

Read each destination no earlier than 24 hours after its dispatch, recording the actual read time. A late Friday dispatch may therefore require an October 31 read; October 30 closes selection, not necessarily grading. Acknowledgment, a packet's existence, and integration into a recipient record are distinct. No identifiable destination record is **not assessable**, not automatically a lost caveat. Report those transfers and the reason separately; retain their original sample positions.

## 2. Six-field comparison template

Use one transfer header and one row for each field. Quote the shortest sufficient source and destination excerpts; link exact artifact versions. Compare meaning, not identical wording. A precise, explicit citation to the bounding qualification can preserve it; a generic report link beside an unconditional claim cannot repair that claim.

| Field | Source inventory | Recipient test |
|---|---|---|
| Finding | Central proposition; object, scope, units, date and denominator | Same proposition, or an explicitly attributed disagreement? |
| Evidence | Supporting primary/secondary evidence and its limitations | Evidence traceable; inference not promoted to direct measurement? |
| Caveats | Each distinct bounding qualification, assigned C1, C2, etc. | Qualification retained with the claim, weakened, contradicted or omitted? |
| Confidence | Explicit confidence and its stated basis; UNKNOWN if unstated | Uncertainty preserved, reduced with reason, or inflated without new evidence? |
| Conditions | Preconditions, time horizon, population and counterfactual | Contingent/future shown as such; comparison basis preserved? |
| Implication | Source's warranted implication and named decision owner | Recipient's change justified by evidence, or disagreement explained? |

Field grades: **1** meaning preserved; **0.5** partly preserved; **0** lost or materially changed. UNKNOWN means unavailable evidence; N/A means the source contains no such field. Explain every 0 or 0.5. Do not average these six fields into the primary caveat metric: the same qualification can affect several fields, but is counted only once as a caveat.

Record recipient disposition independently: adopted; adopted with qualification; declined with reason; deferred; no record found; or UNKNOWN. A clearly labeled rejection that accurately represents the source and its uncertainty can receive full fidelity credit. New evidence or a new conclusion is not a loss if its basis and departure from the source are explicit.

## 3. Caveat severity and retention

Assign severity from the source before destination inspection. For each caveat, state the decision or interpretation that could change if it vanished. Merge overlapping formulations of the same qualification; do not multiply the denominator by splitting one limitation into several phrases.

| Severity | Weight | Operational definition |
|---|---:|---|
| 0: immaterial | 0 | Wording or detail whose loss cannot alter the object, inference, timing or intended decision. List it; exclude from the weighted denominator. |
| 1: minor | 1 | Useful precision lost; the proposition, direction, timing and warranted decision remain intact. |
| 2: material | 2 | Loss could change confidence, eligible population, magnitude, horizon or the warranted decision. |
| 3: reversal | 4 | Loss changes the kind or direction of the claim: contingent to current; inference to measurement; share to probability; descriptive base rate to actionable predictor. |

For each caveat and observed destination, retention is **1** if the limitation's operative meaning survives, **0.5** if some substantive protection survives but is incomplete, and **0** if absent or contradicted. Brief wording alone earns no partial credit. Source ambiguity is flagged UNKNOWN rather than resolved against the recipient.

**Historical anchors, not batch scores:**

- NVIDIA: the September 10 report's $164.5B scale marker combines contingent maximum exposure and commitments; the $105B SB Energy guarantee was contingent/unfunded, with first phase FY2029. Turning that into a present loss or funded liability is severity 3. Preserving contingency but losing the operative start horizon can be severity 2. This example identifies possible losses; it does not assert that VULCAN made them.
- Charged-off borrowers: "stopped paying" is an inference; Encore's above-forecast collections are counter-evidence. Relabeling the inference as measured is severity 3; dropping the counter-evidence is severity 2. CARL KB-CARL-402/403 instead retained uncertainty and rejected the survivor-pool explanation for a stated falsifiability reason: **declined with reason, not caveat loss**.
- A 39% share of loans priced at or below 80 cents is not a 39% default probability. Likewise a historical reserve-coverage base rate is not automatically a short-term predictor. Either conversion is severity 3.

These anchors reference the dated cases in the corrected `2026-10-23_dewey-research-history-meta-review.md`, §§2/4, and CARL's KB402/403. Their historical numbers are not refreshed market readings.

## 4. Calculations and denominators

For transfer i and caveat c, let w_ic be its fixed source severity weight, and r_ich its retention at observed hop h. Baseline source is h=0, r=1. A hop is one actual sender-to-recipient transfer of content: source → WALTER is one, WALTER → owner is two. Rewrites within one desk and repeated notifications are not extra hops. Record the actual chain; do not invent an upstream hop when WALTER originated the source.

**Primary end-to-end weighted retention:**

`100 × sum(w_ic × r_ic,last) / sum(w_ic)`

Use the last assessable recipient record on each selected transfer's documented chain. Include only caveats whose source and endpoint can be assessed. Report included transfers, included caveats, total weight, exclusions and missing weight. A zero denominator is NOT COMPUTABLE. Report unweighted fully/partly/lost counts, material/reversal losses, and assessable transfers / all selected transfers beside the percentage. Never present missing records as 100% retention or as demonstrated loss. No extrapolation beyond this batch.

**Per-handoff slope:** use only chains with at least two observed post-source hops and the same caveats assessable at those hops. For each transfer compute `R_ih = sum(w_ic × r_ich) / sum(w_ic)` over that fixed set. Estimate the within-transfer least-squares slope of R on observed hop number, with one intercept per transfer. Let n_i be its number of observed post-source hops. Give each observation weight `1/n_i`, so each transfer's observations total weight one. Demean h and R within each transfer, then `beta = sum_i[(1/n_i) × sum_h((h-h_mean_i) × (R-R_mean_i))] / sum_i[(1/n_i) × sum_h((h-h_mean_i)^2)]`. Report `100 × beta` in percentage points retained per additional handoff, with the number of transfers, observations and hop range. Use post-source observations only: the definitionally perfect source must not manufacture a downward slope.

If there are no such chains or the slope denominator is zero, report NOT COMPUTABLE. Endpoint-only records support endpoint retention, not a slope. Also show each adjacent observed edge's change in retention; an increase is a recorded restoration, not erased. Branches are separate named paths, reported separately rather than multiplying one transfer's weight in the pooled slope. No p-value or causal interpretation is warranted by approximately ten selected transfers; topic and routing complexity can confound the comparison.

## 5. Reader delivery and acceptance

The reader returns: sample/provenance table; frozen source inventory; six-field comparison with excerpts; recipient dispositions; caveat weights and retention scores; calculations with all denominators; missing/ambiguous cases; and a short contrary-evidence section. Any retrospective examples remain outside the sample and rate. PROME verifies the artifact; DEWEY consumes the result as a new dated addendum to the meta-review, preserving this method version. Neither author silently changes the rubric after seeing outcomes. If an ambiguity requires a revision, retain original scores and label the sensitivity result separately.

## Counter-evidence and limitations

Reasoned rejection, a deliberately narrower decision scope, an explicit source citation and later source correction can explain apparent differences without loss. Missing records can reflect delayed integration. Source-inventory judgment and partial-credit grading remain subjective; one reader does not establish inter-rater reliability. The source caveat types and ACTION selection constrain the population. This test does not authorize a fleet rule, new collector, standing audit or another research run.

## References and process report

Repository primary governance: WQ-515 ruling above; `inbox/2026-10-23_from-PROME_WQ515-516-RULED-A.md`; `AGENTS/WALTER/inbox/2026-10-23_from-PROME_WQ515-RULED-A-fidelity-test-name-ten-transfers.md`; PROME DOCKET L828. Correction evidence: `inbox/2026-10-23_from-PROME_meta-review-two-corrections-table-and-CARL-case.md`; CARL KB402/403 read directly October 25.

**Work:** targeted repository reads; no web searches or delegated readers. **Gap:** WALTER's sample and future recipient records do not yet exist for this window; no result is claimed. **Confidence:** reproducible rules, untested rubric. **Source frustration:** no external source needed. **Improvement:** no safeguard proposed until the approved batch produces evidence.
