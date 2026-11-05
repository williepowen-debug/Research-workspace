# Path A F2 audit: pre-registered specification

**Frozen:** 2026-11-05 10:41 ET, committed before any outcome was computed. Will's word 2026-11-05 10:37 ET ("A yes lets do this"). Research only: no threshold, gate, letter or trade changes on any result.

**Disclosure:** the author knows the broad history (2007, 2011, 2015, 2020) from the thesis. No outcome table for this definition has been computed.

## Claim under test

VIX_THESIS CENTRAL CLAIM: aggregate HY OAS leads VIX by 2-6 weeks at the tactical level (100bp widening -> VIX spike) when (1) VIX<20 at onset, (2) the shock originates in credit, (3) widening is cross-sector, (4) the curve is not inverted. Hit rate ~70%, false positive 25-30%, or 15-20% with the curve filter. Those figures are INHERITED and unreplicated.

## What this can and cannot test

- **Tested mechanically:** size, VIX<20, curve not inverted, and the 2-6 week lead.
- **NOT tested:** condition 2 (credit origin) and condition 3 (cross-sector). Neither has a mechanical historical definition here. This audit therefore tests a SUPERSET of Path A. A failure can be blamed on the missing filters, and a pass does not certify them.

## Data

- HY OAS: FRED BAMLH0A0HYM2. 1996-12-31 to 2023-12-11 from the web-archive snapshot of FRED's own data file (20231212182755), then the FRED API from 2023-11-06. FRED truncated the series to 3 years in April 2026, and ALFRED vintages also begin 2023-11-06. Authenticated: 26 of 26 overlap dates identical; thesis marks reproduced.
- VIX: Cboe VIX_History.csv closes. Holiday phantoms drop out by date-matching to HY observations.
- Curve: FRED T10Y2Y (10-year minus 2-year).
- ICE notice restricts reproduction: raw series stay in the session scratchpad, only derived results are committed.

## Primary definition

- **Signal:** HY OAS close at least 100bp above its minimum over the prior 63 trading days.
- **Gate:** VIX close <20 AND T10Y2Y >= 0 on the signal day.
- **Episode:** first qualifying day. A new episode needs at least 30 trading days since the prior one, so outcome windows do not overlap.
- **Hit:** highest VIX close in trading days t+10 to t+30 at least +50% above the signal-day close. That is the 2-6 week lead, and +50% is the KB-VIO-207 tail cell.
- **Era split:** 2018-01-01, same as KB-VIO-207/211.
- **Null:** same count of random days drawn from that era's days with VIX<20 and T10Y2Y >= 0. 4,000 sims, seed 7, one-sided p.

## Variants, all reported, none selected

- Size 75bp and 50bp (the live episode sits at +72bp).
- Lookback 42 and 126 days.
- Gate variants: no curve filter; VIX<20 at the trough day instead of the signal day.
- Outcome variants: window t+1 to t+30; hit +15%; hit VIX close >= 30.

## Decision rule, fixed now

1. **Post-2018 episodes in the primary cell under 5: NOT RUNNABLE.** Under KB-VIO-217/260 that resolves to NO GATE, never to F2-waived. Variants may describe, but cannot rescue it.
2. **At least 5:** F2 PASSES only if the post-2018 hit rate exceeds the era's null with p<0.05 and lift is at least 1.25x.
3. **Replication of ~70%:** compare the pooled primary hit rate. Any pooled rate under 50% means the inherited figure did not replicate on this definition.
4. **Consequence, any result:** a recommendation only. Changing the thesis claim, Path A's status or the 11/17 WATCH needs Will's word.
5. The live 2026 episode is excluded from all tallies and shown separately, because its outcome window is incomplete.

## Known limits

HY OAS publishes T+1, so the signal is known one session after t; the window starts at t+10, so this barely touches the result. The 63-day trough is one operationalization: the thesis does not define the window.
