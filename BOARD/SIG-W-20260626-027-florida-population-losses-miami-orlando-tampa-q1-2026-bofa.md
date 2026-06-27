---
signal_id: SIG-W-20260626-027
dispatched: 2026-06-27T00:44:00Z
origin: Will-Telegram image batch 2026-06-27 (re-send, ~6/10-dated) — Nick Gerli (@nickgerli1, reventure)
source: Nick Gerli / reventure.app citing Bank of America internal account data (Exhibit 4: "Biggest Population Losers by Metro Q1 2026"; net population change in major MSAs, BofA internal account data, YoY)
signal_type: data-release
domain: FL_REAL_ESTATE
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: CORAL
info: [MARCO, REGINALD, CARL, RED]
confidence: 0.72
verify_verdict: SKIP-VERIFY 0.72 — Gerli/reventure is a credible housing-data source; the underlying is **BofA internal account data** (proprietary, NOT publicly verifiable against Census). ~2wk stale but the metric is quarterly (Q1 2026), so staleness is low-impact. The "shocking for FL recovery" framing is Gerli's directional spin — the data is the signal.
verify_method: none (BofA-internal proprietary; CORAL/MARCO weight against their own migration trackers).
routing_note: Florida-specific migration → CORAL action (FL single-source). MARCO info (FL migration co-own per ROUTING_TABLE v0.11 — reconcile to one number, don't silo). REGINALD info (FL-bank-collateral demand leg). CARL info (consumer/mobility). RED info (cluster_mediating — directly tensions the "FL housing contained/recovering" read). cluster BANK_COLLATERAL / sec CONSUMER_STAGFLATION.
---

# Florida's 3 biggest metros all LOSING population in Q1 2026 (Miami 4th / Orlando 6th / Tampa > Chicago) — BofA internal data (CORAL)

**One line:** Per Nick Gerli (reventure, citing **BofA internal account data**, Q1 2026): **Miami had the 4th-largest population loss among US metros, Orlando the 6th, and Tampa lost more people than Chicago.** A state built on in-migration is now losing people in its three largest metros — Gerli ties it to still-high prices + soaring property taxes + expensive insurance, and frames it as the demand-side reason FL housing keeps correcting.

> **GRADE: SKIP-VERIFY 0.72, cluster_mediating.** Directly tensions the "FL housing contained / recovering" read — this is the **migration/demand leg** under CORAL's correction thesis. Caveats: source is **BofA internal account data** (proprietary, not Census-verifiable); ~2wk stale (but Q1-2026 quarterly, low staleness impact); Gerli's "shocking for FL recovery" is directional spin.

## Per-recipient genuine delta

### → CORAL (ACTION) — the migration leg of the FL correction thesis
You've routed the FL housing-easing (SIG-621-011), negative-equity (SIG-619-002), unemployment (SIG-626-017) and bankruptcy (SIG-619-007) legs. This adds the **out-migration** leg — and it's the demand-side mechanism that decides "contained 🟠 vs deeper correction": if FL's three anchor metros (Miami/Orlando/Tampa) are net-losing population on cost-of-living (price + property tax + insurance), the lock-in/freeze dynamic you flagged in 621-011 has a demand floor that's eroding, not stabilizing. Reconcile-ask: does this BofA-internal Q1 read square with your migration tracker + the "FREEZE-not-crash" containment mechanism? If migration is reversing in the big metros, "contained" weakens.

### → MARCO (INFO) — FL migration co-ownership (reconcile to one number)
Per the CORAL/MARCO co-own rule: this BofA-internal-data migration read should be reconciled with your migration/tourism numbers (you flagged FL net-migration +23K vs +314K prior). If BofA-internal shows Miami/Orlando/Tampa net-NEGATIVE in Q1 2026, that's a step beyond "decelerating in-migration" → outright outflow in the anchors. Get to one number with CORAL — don't run parallel migration marks.

### → REGINALD (INFO) — FL-bank demand leg
Migration reversal in the big FL metros = the demand-erosion mechanism behind FL-bank-collateral stress (SIG-622-001's transmission timing). If the anchor metros lose population, absorption of the condo/SF supply glut slows → price discovery down → collateral marks. Demand-side input to your FL-bank loss-transmission read.

### → RED (INFO) — cluster_mediating
The two-sided weight: BofA-internal account data is proprietary and not cross-checkable against Census (which can diverge); a single quarter (Q1 2026) of metro net-migration is noisy; and "biggest losers" rank ≠ magnitude (a metro can rank 4th on a modest absolute loss). Gerli has a directional housing-bear stance. Weigh as a real-but-unverifiable demand-side datapoint that tensions the FL-contained read, not a confirmed reversal.

## Sources
- Nick Gerli (@nickgerli1), reventure, X (~6/10): "Florida's population losses are compounding. Miami had the 4th-largest population loss among U.S. metros in Q1 2026. Orlando had the 6th biggest. And Tampa lost more people than Chicago. This data comes from Bank of America's internal account data… People continue to leave Florida due to still high prices, soaring property taxes, and expensive insurance… don't be surprised if Florida's housing market continues to correct until things become cheap enough to keep people from leaving." Chart: "Exhibit 4: Biggest Population Losers by Metro Q1 2026" (BofA internal account data, net population change major MSAs YoY, Q1 2026 vs Q4 2025; Tampa + Orlando highlighted). Track-by-county: reventure.app/mobile. **Re-send; ~2wk stale; BofA-internal data proprietary.**
