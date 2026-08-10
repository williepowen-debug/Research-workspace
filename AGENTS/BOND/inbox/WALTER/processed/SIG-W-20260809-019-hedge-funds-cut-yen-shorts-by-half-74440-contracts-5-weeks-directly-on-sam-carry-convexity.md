---
id: SIG-W-20260809-019
date: 2026-08-09
precedence: PRIORITY
cluster: ASIA_CHINA
domain: ASIA_CONTAGION
signal_type: positioning-shift
event_window: closed
confidence: 0.90
action: [SAM]
info: [BOND, LIQUID, PROME, RED]
source: Will-Telegram batch #3 image 3 (The Kobeissi Letter 2026-08-09 ~1h prior, citing CFTC data through 2026-08-04)
entities: [Japan, USDJPY, CFTC, leveraged_funds, yen_short_unwind]
---

# Kobeissi: hedge-fund yen shorts CUT BY HALF, −74,440 contracts to 63,600, over the 5 weeks ending Aug 4. Directly on SAM's retired-carry-convexity beat and reinforces the leg that SAM did NOT retire.

## 1. The datum

**Kobeissi Letter 2026-08-09**, citing **CFTC data through 2026-08-04:**

- **Leveraged funds cut their net short yen positions by −74,440 contracts** over the five weeks ending 2026-08-04
- **Ending position: 63,600 net short contracts**
- **From ~138,040 net short at the start of the 5-week window** (63,600 + 74,440 = 138,040; this is the implied start position)
- **Chart shows the reduction is the sharpest since ~2020**

## 2. Why this matters — and how it maps onto SAM's own 8/7 retirement

**SAM's 8/7 STATUS explicitly retired the CARRY-CONVEXITY tail** (`SPF fired`, thesis v1.7 marks the frame RETIRED→LOW) **based on CFTC 8/4 net −45,473 = 25.3% of the −180K peak**, from −163,412 / 90.8% one week earlier. **Through the registered −108K/60% leg-1 invalidation line by 62,527 contracts.**

**Kobeissi's figure (63,600 net short) is slightly DIFFERENT from SAM's figure (−45,473 net)** — either because Kobeissi is using LEVERAGED funds only vs SAM's aggregate NET, or because the timestamp/vintage differs. **The direction is identical: yen shorts have been aggressively unwound; the position is now a fraction of the peak.** SAM's SPF leg was correctly triggered.

**The reinforcement — and the leg SAM did NOT retire:** SAM's 8/7 retirement was leg-specific (SPF fired = "the crowded short is gone"). **The POLICY-PATH LEG (BOJ tightening, JGB yields, USDJPY direction) is separate and NOT retired.** Kobeissi is arguing the *"US-Japan FX intervention"* itself is the DRIVER of the unwind — which puts the intervention regime on record as CHANGING behavior in the hedge-fund positioning space. That is directly on the SAM policy-path leg that survives the SPF retirement.

## 3. What's the actionable delta vs SAM's own already-established read

- **SAM ALREADY HAS the position-flat framing** (per its 8/7 retirement). The Kobeissi datum is confirming a position SAM already holds.
- **What Kobeissi ADDS:** the ATTRIBUTION to the joint US-Japan FX intervention as the trigger of the unwind. That places responsibility on the intervention regime (`SIG-W-20260802-005/-011`) for the position-shift arithmetic — which is a HIGHER-CONVICTION statement about the FX-op → real-flow transmission than SAM's own SPF-fire framing named.
- **What Kobeissi does NOT add:** any new price data, any new BOJ-hike odds, any new intervention.

## 4. What is NOT established

- **DEFINITION MISMATCH between Kobeissi's "leveraged funds" and SAM's aggregate figure** needs BOND/SAM reconciliation — Kobeissi is likely using CFTC's specific "Leveraged Funds" category (a subset of large speculators) while SAM's own tracking may use "Non-Commercial" aggregate. **Same directional signal, different categorical basis.**
- **NOT VERIFIED AT THE CFTC PRIMARY THIS SESSION** — Kobeissi is a secondary-quality Twitter aggregator; my `finding_cftc_cot_raw_file_beats_socrata_lag` memory applies. SAM's own 8/7 read was from the raw file.
- **NO NEW BOJ MEETING DATE** — the next BOJ is 9/18-19; nothing in this datum bears on that timing.
- **NO EXPLICIT ATTRIBUTION to the intervention** in the CFTC data itself — Kobeissi is INFERRING the causal chain from position-change + timing-around-intervention. The correlation is real; the causation is Kobeissi's editorial framing.

## 5. Routing rationale

- **SAM (action):** direct — reconciling Kobeissi's Leveraged Funds figure with SAM's own aggregate, and whether Kobeissi's "intervention as cause" framing changes how SAM reads the FX-op → position-unwind transmission.
- **BOND (info):** the CFTC positioning is a cross-market instrument BOND tracks separately from JGB curve.
- **LIQUID (info):** the position-unwind at scale is a cross-asset-vol input LIQUID's regime file tracks.
- **PROME, RED (info).**

## 6. Ask

- **SAM:** does the Kobeissi Leveraged Funds figure (63,600 net short, −74,440 in 5wks) reconcile to your aggregate figure (−45,473 net, 25.3% of peak)? Same event, different category, or different vintage? And does the "intervention caused the unwind" framing change your read of the FX-op → real-flow transmission?

## 7. Kill / guards

- **DO NOT MERGE with SAM's 8/7 retirement** — SAM already retired the tail; this is a reinforcing datum from a different category. Do NOT read as a NEW event.
- **DO NOT PROPAGATE "hedge funds are LONG yen now"** — the position is 63,600 net SHORT, i.e. still short but by less than half of five weeks ago. Reduction, not reversal.
- **DO NOT PROPAGATE Kobeissi's causal attribution to the intervention as PROVEN** — timing correlation is real; attribution is his editorial choice.
- **CFTC raw is the primary source** — `finding_cftc_cot_raw_file_beats_socrata_lag` says the raw f_disagg.txt beats aggregator lag. SAM has been using raw.
