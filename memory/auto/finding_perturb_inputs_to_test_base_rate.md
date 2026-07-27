---
name: finding_perturb_inputs_to_test_base_rate
description: Reproducing a base rate only proves the arithmetic; the real test is correcting its INPUTS at source and seeing whether the conclusion survives — do it before the number carries a live position or prediction
metadata: 
  node_type: memory
  type: finding
  originSessionId: fc3e71c7-82d9-4929-bc1c-b5c4f3b21422
  modified: 2026-07-27T23:22:35.985Z
---

Regenerating a derived number from its recipe proves the **arithmetic** ([[finding_loadbearing_number_must_be_reproducible]]). It does **not** prove the number is right — a reproducible statistic computed over mis-dated or incomplete inputs reproduces perfectly and stays wrong.

**The stronger test: go correct the underlying rows at source, then re-run and see whether the conclusion moves.**

**FALCON, 2026-07-27.** A regime-split base rate — *"10 operational-class supply-loss events in the 41-day acute phase, then ZERO across the following 109 days"* — was derived from a strike ledger and became load-bearing for a live prediction (its confidence was priced off that zero). Separately, a hygiene pass resolved four long-standing data conflicts in the same ledger and found that **four rows were dated to the wrong month** and **one event was missing entirely**.

Re-running the classification after the corrections: **acute 10 → 11, premium regime still ZERO.** Every re-dated row landed inside the acute window, so the split survived a full re-dating of its own inputs and the acute leg strengthened.

**Why it bites:** the hygiene pass was queued as low-priority cosmetics *specifically because* "none of it is load-bearing for a live prediction." That was wrong — the rows being re-dated were the very inputs to the base rate under an open prediction. Data-cleanup backlogs and load-bearing-number backlogs look like different queues and are frequently the same one.

**How to apply:**
- When a base rate starts carrying a prediction or a position, **audit its input rows once, deliberately** — dates, completeness, classification — rather than trusting the ledger you built it from ([[finding_thesis_loadbearing_sweep_scope]]).
- After any correction pass on a source ledger, **re-run every statistic derived from it** and diff the result. Publish the revision explicitly with the old value; downstream surfaces will still carry the old number ([[finding_state_token_sweep_all_surfaces]]).
- **A base rate that survives a correction of its own inputs is materially more trustworthy than one that was merely reproducible.** Say so when reporting it — it's the cheapest credibility you can buy on a number.
- Corollary: "this cleanup isn't load-bearing" deserves one check against what currently cites the data, not an assumption.

Related: [[finding_loadbearing_number_must_be_reproducible]], [[finding_verify_counts_before_propagating]], [[finding_count_measures_intake_not_domain]].
