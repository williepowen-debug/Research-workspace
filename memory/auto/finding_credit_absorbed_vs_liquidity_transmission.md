---
name: finding_credit_absorbed_vs_liquidity_transmission
description: "For a guaranteed/insured asset, \"credit loss is federally/insurance-absorbed\" does NOT mean the channel is dead — classify transmission on BOTH the credit-loss axis and the servicer-liquidity/advance-drain axis before killing it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a71c3ae8-fff8-4adf-ac9f-1e29fcbcfb03
  modified: 2026-07-24T15:02:28.099Z
---

When asked whether distress in a **guaranteed or insured asset** (FHA/VA loans, GSE MBS, monoline/insurance-wrapped credit, deposit-insured funding) transmits to tradeable credits, classify the channel on **TWO independent axes** before ruling:

1. **Credit-loss locus** — who eats the principal loss. For a wrapped asset this is usually the federal/insurance fund (FHA MMI, VA guaranty, GSE, monoline), NOT the bank/investor. This axis often reads "absorbed → dead to banks."
2. **Servicing-liquidity / advance-carry locus** — who funds the *carry* while the loss resolves (P&I advances to bondholders, delinquent-loan buyouts at par, non-reimbursable curtailment/holding costs). This usually lands on the **leveraged nonbank intermediary** (the servicer/issuer) and, second-order, its **warehouse/advance financier**.

**The trap:** killing the channel on axis 1 ("MMI Fund at record 11.47% capital → absorbed") while ignoring axis 2 gives a false "absorbed / all-clear." The distress is real and tradeable — it just expresses as a *liquidity* event on nonbank-servicer credit (+ its bank/PE financier), not a *credit-loss* event on the guarantor or the originating banks.

**Why:** 2026-07-24 DEWEY PROMPT-15 (FHA/VA loss waterfall). Verdict was SPLIT: FHA/VA credit loss federally absorbed (kill REGINALD's "regional bank eats the loan loss" leg), BUT the servicing-advance drain is live and lands on nonbank Ginnie servicers (Freedom/loanDepot/Lakeview) + Apollo/Atlas SP as warehouse financier — NOT the regionals. The two axes gave opposite answers; reporting only axis 1 would have wrongly killed the whole channel.

**How to apply:** for any wrapped/insured/guaranteed-asset transmission question, explicitly answer "who eats the loss?" AND "who funds the carry until resolution, with what leverage and what backstop?" — the second is where a leveraged nonbank without a Fed/FHLB backstop breaks first. Related: [[finding_decouple_idiosyncratic_from_systemic_leg]], [[finding_proxy_segment_masks_trigger_series]], [[finding_blended_index_masks_bifurcation]] (the blended servicer DQ masks the FHA sub-book — same run).
