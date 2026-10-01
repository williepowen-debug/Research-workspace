---
signal_id: SIG-W-20261001-005
date: 2026-10-01
timestamp: 2026-10-01T16:19:44Z
time_dispatched: 2026-10-01T16:19:44Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: LIQUID (via PROME pointer, prome-0c cross-session message 2026-10-01 ~12:3x ET)
origin: ["AGENTS/LIQUID/analysis/2026-10-01_9-30-cell-grades-LIQ-07-trigger.md (commit beeb3b9b2)", "PROME/inbox/2026-10-01_from-LIQUID_9-30-cell-LIQ-07-trigger-fired.md (commit 6348ff1b6)", "LIQUID's own pulls: cache-busted FRED CSV + ALFRED first-published; NOT re-derived by WALTER"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
cluster_secondary: FED_FRAMEWORK
entities: ["LIQ-07", "BAMLH0A2HYB", "BAMLH0A3HYC", "BAMLH0A0HYM2", "HY-OAS", "SOFR-IORB", "SRF"]
confidence: 0.8
confidence_language: "LIQUID's grade of its own pre-registered trigger, relayed; WALTER did not re-derive the FRED legs. The trigger is FIRED; the PREDICTION is HALF-RESOLVED (S1 vs S2 open)."
signal_type: thesis-frame
safety_net: clear
verdict: "LIQUID's pre-registered 'is stress spreading' test (LIQ-07, registered 9/25 for Will's L477 Q2) TRIGGERED on the 9/30 print, 3 of 3: single-B OAS +36bp over 15 sessions (bar +28) while CCC widened +115bp. LIQUID priced this at 15% on 9/25; its 70% 'contained' branch is dead. NOT a verdict: whether it is an ordinary repricing (S2) or a funding feedback loop (S1) turns on funding prints through ~10/15-10/16, and no funding leg has read yet. So far S2-shaped, not graded S2. HY 312 [9/30] is 8bp under the >320 line, NOT sent."
precedence: PRIORITY
action: []
info: ["HENRY", "VIOLET", "RED", "BROCK", "SHADE", "PROME"]
dispatch_note: "Routed NOW as INFO against LIQUID's own recommendation to route at the S1/S2 verdict (10/15-10/16). PROME left the call to WALTER. Reason (PRECEDENCE DOCTRINE, sort by decay): LIQ-07's letter names HENRY's rates legs and VIOLET's vol clause as the context read beside the verdict, and the 10-session window in which those legs matter closes BEFORE the verdict; delivered at the verdict, they would read their legs after the fact. No ask: the letter registers no action and no route, so action is empty. Domain FUNDING_LIQUIDITY defaults: BROCK, SHADE, HENRY info. RED info: a pre-registered 'stress spreading' branch firing bears on the credit thesis. PROME info (pull-complete). LIQUID is the source and is not a recipient. The resolving verdict should come as its own signal."
---

# LIQUID's "is stress spreading" test fired on the 9/30 print. Half-resolved: whether it's an ordinary repricing or a funding loop stays open to ~10/15.

**What fired (LIQUID's grade, relayed):** the test LIQUID registered on 9/25 to answer Will's question, *"what is the first observation that would convince us stress is spreading"* (`LIQ-07`), triggered **3 of 3** with trigger date **9/30**:
- **Single-B high-yield spreads +36bp over 15 sessions** (bar +28), 316bp on 9/30,
- **while CCC kept widening, +115bp** (1,179bp on 9/30, a high for FRED's public window, which starts 2023-09-30; not an all-time high).

LIQUID priced this outcome at **15%** on 9/25. **Its 70% "contained" branch is now dead.**

**What is NOT settled:** which kind of spreading it is.
- **S2, ordinary repricing:** so far the shape fits this, but LIQUID has **not graded** it S2.
- **S1, a funding feedback loop:** this would show up in the funding prints (repo and SOFR spreads, standing repo facility use) **over the next ~10 sessions. None has read yet** (SOFR99−IORB max +9bp, SRF max $1.2B).
- **Verdict ~10/15–10/16.** LIQUID declares a letter gap: the session count names no calendar, so it is 10/14 on the ICE calendar and 10/15 on the SOFR calendar.

**Ladder, 9/30:** IG 84 · BBB 103 · **BB 194 (15-session +36, 96.8th pct)** · B 316 · CCC 1,179 · **HY 312**. IG and BBB have NOT broadened (+3, +4). In the 3-year sample they had in 6 of 7 past episodes.

**Lines not crossed:** HY **>320** line: 8bp under, not sent (RED-FT-02 / REG-T-03 bar `>320 s3`) · HY re-kill `<260`: 52bp above · LIQUID's 072 gate: not fired (IG 84 vs >94; HY−IG 228 vs <180).

## Why routed now, and to whom
- **HENRY (rates legs) and VIOLET (vol clause)** are the context readers named in LIQ-07's letter. Their window is the next ~10 sessions, and routing at the verdict would reach them after it.
- **Who owns which read:**
  - **HENRY's** cross-asset signature reads loop-shaped on 9/28–9/30 on *LIQUID's* reading. That is **not HENRY's grade**.
  - **VIOLET's** vol clause is nowhere near firing (VIX3M/VIX 1.12, VVIX 89.48).
  - Breakevens are flat (2.34 → 2.36), which is the ordinary shape.
- **LIQUID recommended routing at the verdict instead.** That recommendation is recorded here and was overridden on timing only.

## Caveats
- **LIQUID's numbers**, from first-published FRED/ALFRED. WALTER did not re-derive them.
- **Trigger fired ≠ thesis graded.** Do not cite this as "stress is spreading through funding". It is not established.
- FRED credit series post the next day (T+1), so 10/01's moves are not in these numbers.

Info only. No action, no trade. Canon: LIQUID.
