---
signal_id: SIG-W-20260618-007
dispatched: 2026-06-19T00:20:00Z
origin: Will Telegram intake (msg 2379, 2026-06-19 ~00:15 UTC)
source: Fitch Ratings — "U.S. CMBS Delinquency Rate Ticks Upward in May; Office, Lodging Rates Decline" (May 2026 monthly index)
signal_type: data
domain: BANK_CRE
cluster: BANK_COLLATERAL
signal_role: cluster_mediating
precedence: PRIORITY
to: REGINALD
info: [BROCK, LIQUID, RED]
confidence: 0.90
verify_verdict: SKIP-VERIFY (Fitch Ratings primary — its own monthly index report)
verify_method: none needed — Fitch primary; numbers are Fitch's own May index
---

# Fitch May CMBS delinquency +3bps to 3.31% — headline near-flat, but the FLOWS are deteriorating (maturity-wall-driven)

## Substance (Fitch Ratings primary, SKIP-VERIFY)

Fitch overall US CMBS delinquency rate **3.31% in May, +3bps from 3.28% April**. Property-type results MIXED — **office, hotel, mixed-use all posted monthly DECLINES** — but new delinquency volume (large-balance office + regional malls) outpaced resolutions.

**The flow dynamics are the signal, not the +3bps headline:**
- **New 60+ day delinquency $1.73B in May, UP +29% from $1.34B April.** Composition: office 33% ($562M), retail 28% ($474M), multifamily 20% ($339M).
- **Resolutions DOWN −25% to $1.54B (from $2.04B April)** — $1.05B brought current + $422M liquidations + $69M cured-to-30-day.
- **Net: inflows accelerating + outflows slowing.** The rate is only flat because the base is large; both legs are moving the wrong way.
- **64% of new delinquencies are MATURITY defaults ($1.11B)** vs 36% term defaults ($618M) = the **refi-wall mechanism** (loans failing to refinance at maturity), not cashflow/term stress. This is the maturity-wall biting, consistent with a no-cut/now-hiking rate regime.

## Why it matters — cluster_mediating, headline-vs-flow

This **mediates "CRE is stabilizing" vs "CRE flows deteriorating":**
- **Stabilizing read (headline):** +3bps to 3.31% is near-flat; office/hotel/mixed-use RATES declined on a property-type basis. Surface reading = CRE distress contained.
- **Deteriorating read (flows):** new delinquency +29% MoM, resolutions −25%, 64% maturity-driven. The pipeline is filling faster while the drain slows — a flat rate today that the flows are pushing higher. Office *led* fresh inflows (33%) even as office's headline rate ticked down (a base/resolution artifact, not improving fundamentals).

**REGINALD (action):** CRE/CMBS is your lane. Two direct ties to your tracked vectors: (a) **multifamily 20% of new delinquency ($339M)** → your **multifamily-CMBS +56bps / GSE-MF-SDQ-near-2010-peak** vector (6/8); (b) **office leading new inflows + maturity-wall 64%** → the office-CMBS-distress thread (WAL life-science office B1 fire SIG-W-20260521-007, KREF, the $875B 2026 maturity wall you flagged). The headline-flat / flow-deteriorating split is the read to carry — don't let +3bps read as stabilization.
**Threshold note:** REG-T-07 (OFFICE-CMBS-DQ >15% sustain 3) NOT fired — overall 3.31% and office rate declined; office-specific DQ not given in this release but is well under 15%. REG-T-07 remains absent from the FORGE dashboard pull (standing gap) — this Fitch print is the manual proxy.

**BROCK (info):** CMBS/CRE overlap with your BDC-CRE + the distressed-CRE pricing thread (pairs AVB/EQR SIG-W-20260522-008 — strongest operators consolidating rather than buying distressed; resolutions slowing fits that "buyers not stepping in" read).

**LIQUID (info):** CRE-credit/funding — maturity-wall refi failures are a funding-availability tell.

**RED (info, auto-cc cluster_mediating):** the headline-vs-flow bifurcation — steelman both (is +3bps genuine containment via resolutions, or a flat number masking an accelerating pipeline?).

## Source framing

Fitch Ratings primary (its own May monthly CMBS index) — no verify needed, no extraordinary claim. Will pasted the Fitch text verbatim. SKIP-VERIFY 0.90 (calibration ceiling on a single-month print — needs the June print to confirm the flow-deterioration trend; one month of inflow-up/resolution-down is direction, not yet trend).

## AIGs / cross-refs

- BOARD: SIG-W-20260521-007 (WAL life-science office B1 fire), SIG-W-20260522-008 (AVB/EQR multifamily consolidation), SIG-W-20260526-007 (condo deflation)
- REGINALD STATUS 6/8 (multifamily-CMBS +56bps vector; GSE MF SDQ near-2010-peak; $875B 2026 maturity wall; KREF mREIT distress)
- REG-T-07 OFFICE-CMBS-DQ threshold (>15%) — not fired; not in dashboard (manual-proxy gap)

## Provenance

- Intake: Telegram msg 2379, 2026-06-19 ~00:15 UTC (Fitch text pasted)
- Pipeline: BOARD-grep novel (no prior Fitch monthly CMBS-DQ signal; the one Fitch-CMBS kill_log entry was 4/20 R&W boilerplate) → Fitch primary, SKIP-VERIFY → dispatch
