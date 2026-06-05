---
name: finding-thin-liquidity-prediction-market-discipline
description: "Thin-liquidity binary prediction-market single-print moves are not \"holds\"; require cross-source verification + ≥3-day re-check + earned-discount calibration before any mark update"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f7f596c8-aff4-452c-857a-cb95382ad168
---

Thin-liquidity binary prediction-market prints (Polymarket BOJ-hike contracts, Kalshi event markets, equivalent venues) can move 5-10pp on a single trade in low-volume contracts. A single-print move is **NOT a "holds."** Operating rule before any mark update from a prediction-market signal:

1. **Require pricing to hold** at the new level on a re-check ≥3 trading days later.
2. **Cross-verify against an independent source** — swap pricing (OIS), dealer-desk read (e.g. MUFG, Goldman desk), Bloomberg consensus, equivalent secondary.
3. **Where prior failures on the same mechanism establish an earned-discount calibration, hold below market until both gates pass.**

**Why:** Polymarket and Kalshi liquidity is thin enough on most macro contracts that a single $5-50K bet can move the printed probability 5-10pp; that move can fully retrace within 24-48 hours when liquidity normalizes. Consuming the raw print as if it were a calibrated probability ships volatility-as-signal to whoever's downstream. Worst case is rebalancing a position size on a price tag that wasn't sustained.

**How to apply:** When any agent (SAM, LIQUID, HENRY, BROCK — anyone) sees a Polymarket/Kalshi mark move > 3-5pp inside 24 hours on a low-volume contract:
- Don't move the agent's own mark on that single print.
- Pre-register the mechanical trigger condition: "if pricing holds ≥{threshold} on {re-check date} AND {cross-source confirms} → +{N}pp mark move."
- Cite earned-discount basis from prior failure cluster on the same mechanism (e.g. SAM-08 + SAM-20 on Takaichi 0.75% ceiling — held below market because that ceiling has cost twice).

**Worked example (SAM, Jun 3 2026):** Polymarket BOJ Jun 16 hike: 87.6% (Jun 2 Tue) → 94.8% (Jun 3 Wed). +7pp/24h on a USDJPY 160 tag day. SAM-21 mark **HELD at 70%** (vs market 94.8%, gap 24.8pp). Pre-registered mechanical trigger: "if Polymarket ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75%." Earned-discount basis: SAM-08 (90% too-hawkish FAIL on April hike) + SAM-20 (60% too-hawkish FAIL on April hike) on the same Takaichi 0.75% ceiling mechanism. Gap to market is not a directional disagreement (SAM agrees with the direction); it's earned calibration on the specific mechanism.

**Sibling references:** Related tool-class methodology rows in agent-local KBs (SAM KB-183 fxy-proxy vol read; SAM KB-058 stop discipline conjunction). The auto-memory routing decision: tool-specific methodology stays in agent-local KB; cross-agent transferable rules (this one) live here.

See also: [[finding_catalyst_vs_consequence_conflation]] — both findings concern over-treating volatile inputs as authoritative; this one is prediction-market-input-specific, the other is catalyst-probability-conflation.
