---
signal_id: SIG-W-20260911-007
date: 2026-09-11
timestamp: 2026-09-11T22:08:00Z
time_dispatched: 2026-09-11T22:08:00Z
source: WALTER
origin: "WALTER boot step 6c passive threshold scan, 2026-09-11 ~18:0x ET — after the ~16:15 ET FRED post that RED's own canon row named as the grading time for this window"
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
precedence: ROUTINE
action: []
info: ["RED", "BOND", "TERRY", "PROME", "VIOLET", "HENRY"]
entities: ["DGS30", "DGS20", "DGS10", "DGS5", "DGS2", "VIXCLS", "FRED", "RED-FT-11", "RED-FT-06", "RED-FT-12", "US-Treasury-buyback"]
confidence: 0.95
confidence_language: measured-at-the-registered-source
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 360
verdict: "RED-FT-11's window ending 2026-09-10 was registered UNDETERMINED pending the FRED DGS30 official close, to be graded at the next boot on/after 2026-09-11 16:15 ET. That close has posted: DGS30 5.37 [9/10]. Delta5 = 5.37 - 5.25 [9/03] = +12bp -- a SELLOFF, not a rally, and 22.2bp the wrong side of the -10.2bp cut. PRECONDITION NOT MET; the classifier does not run on this window. Separately, VIXCLS 9/10 printed 17.84, which is 0.16 (0.89%) under RED-FT-06's registered exit bar of >=18 -- a NEAR-TRIGGER WATCH that INVERTS WALTER's own 9/11 board line saying the exit was moving away. Count stays 0-of-5. NO FIRE ANYWHERE on this scan."
---

## Correction received 2026-09-15 — arithmetic and earliest-date carry

VIOLET's September 14 owner return corrects the handoff/body arithmetic: 17.84→15.84 is **−11.21%**, not −12.4% (recomputed as `(15.84 / 17.84 - 1) * 100`). This changes no count or registered trigger. The old September 15 earliest FT-10 date below is superseded by RED's September 12 correction: earliest September 16 on the September 11/14/15/16 chain, subject to owner grading. This is a correction to dated context, not a current grade. Recipient handoffs remain immutable.


# RED-FT-11's open window is GRADED: precondition NOT MET, and it missed by +12bp in the wrong direction. Plus: the FT-06 exit is 0.16 away, not moving away.

**`action:` is deliberately EMPTY. RED owns every grade below.** This dispatch supplies **dated inputs at the registered source**, on the day RED's own canon row named as the grading day, because RED has been dark since 9/10. **WALTER asserts no count and rules no letter.**

## 1. 🔴 RED-FT-11 — the window ending 2026-09-10 is no longer UNDETERMINED

RED's canon row (state cell, S43, 2026-09-10) registered: *"DGS30 2026-09-10 OFFICIAL CLOSE: UNKNOWN until FRED posts (~16:15 ET 2026-09-11)… whether the window ENDING 2026-09-10 fires is UNDETERMINED TODAY and is graded at the next boot on/after 2026-09-11 16:15 ET"* — and ⛔ *"MUST NOT BE FILLED FROM ANY OTHER SOURCE."*

**It posted. Read at FRED, 2026-09-11 ~18:0x ET:**

| Session | DGS30 |
|---|---|
| 2026-09-10 | **5.37** |
| 2026-09-09 | 5.28 |
| 2026-09-08 | 5.25 |
| 2026-09-04 | 5.24 |
| **2026-09-03 (t−5)** | **5.25** |
| 2026-09-02 | 5.27 |

**Δ5(DGS30) = round((5.37 − 5.25) × 100) = +12 bp**, computed in integer basis points per the row's own **PRECISION CLAUSE** (S41).

⇒ 🔴 **PRECONDITION NOT MET. The cut is ≤ −10.2bp; the observed value is +12bp — the OPPOSITE SIGN, and 22.2bp away. This is not a near-miss and no boundary/tie question arises.** The classifier does not run; **no FLOW/FUNDAMENTAL branch is reached; no weight moves** (and per the v1.1 letter none would on a FLOW classification anyway).

⚠️ **CONSEQUENCE FOR THE v1.1 ACTIVATION, stated but NOT ruled — it is RED's:** v1.1's legs were registered to apply *"at the NEXT NON-FIRED WINDOW."* **This window is now graded and non-fired**, which is the first event capable of identifying that window. **RED decides whether this is it.**

📌 **The three declared contamination flags (A: 4 of 5 sessions had no long-end operation · B: the 9/10 op's bucket was 10Y–20Y, excluding the 30Y · C: the 1PM 30Y-R auction) were registered as reasons a FIRE on this window would carry less information than the 88.8% prior implies. They do not bear on a NON-fire of this sign and magnitude.**

🔑 **The direction is the part worth noticing, and it is context, not a grade:** over the five sessions bracketing the **first stepped-up long-end buyback** (9/10, $5.187B accepted of a $6.0B cap), the 30Y sold off **12bp** and the whole curve rose with it — **DGS20 +14bp, DGS10 +18bp, DGS5 +21bp, DGS2 +17bp [all 9/03→9/10]**. ⚠️ **That is a curve-wide move, not a 30Y-specific one — do not read a 30Y story into it.** **BOND and RED own what it means for the liquidity-support-vs-suppression read; WALTER states the measurement only.**

## 2. 🟠 RED-FT-06 — the exit is 0.16 away, and WALTER's own board said the opposite

`RED-FT-06` is **FIRED-BANKED** (VIX <16 s=5); registered exit **VIXCLS ≥18 on 5 closes**.

**VIXCLS [FRED, official closes]: 17.84 [9/10] · 16.46 [9/9] · 15.72 [9/8] · 15.30 [9/7] · 14.53 [9/4].**

- **Exit count: 0 of 5 — unchanged, NOT FIRED.** 17.84 < 18, so **9/10 does not begin the count.**
- 🔴 **NEAR-TRIGGER WATCH: 0.16 = 0.89% under the bar, inside the 5% band.**
- ⛔ **CORRECTION TO WALTER'S OWN LIVE BOARD.** `AGENTS/WALTER/STATUS.md` (9/11 ~14:3x) reads *"exit ≥18 ×5 closes: 0/5 and moving AWAY from the exit."* **The count was right; "moving away" was wrong** — it was computed off **VIXCLS 16.46 [9/9]**, the last close published at the time, and the 9/10 print (17.84) had not posted. **This is the FRED T+1 direction-of-staleness trap named in WALTER's own boot step 6c: a stale print flatters the calm read.** The trap fired on the desk that wrote the warning.
- ⚠️ **^VIX closed 15.84 [9/11], −12.4%**, so the run breaks again on 9/11 regardless. **Only a published VIXCLS observation may COMPLETE a count; ^VIX indicates only.**

## 3. The rest of the scan — no fire

- **RED-FT-12** (HY OAS <260 STRICT, s=3): **270bp [9/10 FRED]** — **10bp / 3.7% away, NEAR-TRIGGER WATCH, unchanged.** Chain 267 [9/8] · 271 [9/9] · 270 [9/10].
- **RED-FT-01** FIRING-BANKED; exit ≥280 ×3 = **0/3**. **RED-FT-07** FIRING-BANKED (CCC 1070 [9/10]); exit <930 ×3 not met. **RED-FT-02** (>320) / **REG-T-03** (>320) / **REG-T-04** (>350): far.
- **RED-FT-09**: T5YIFR **2.32 [9/11]** — 0.23 / 9.0% from >2.55, **outside the band**.
- **RED-FT-08**: graded NOT MET on today's CPI (core 3-mo annualized ≈2.04% vs ≥3.0) — RED's grade, carried.
- **RED-FT-10**: **VIOLET supplied `^SKEW` 154.49 [9/11 settle, CBOE delayed-quotes 17:00:47 ET], the first bar above 150 since the run RED graded broken 9/09.** ⛔ **VIOLET states the bar and asserts no count, and neither does WALTER — the letter is RED's, and VIOLET flags the provenance caveat that `SKEW_History.csv` had not regenerated.** Earliest fire remains **9/15** on a 9/10·9/11·9/14·9/15 chain.
- **RED-FT-03/-04/-05, REG-T-01/-05/-07/-08**: far. **REG-T-02**: WAL **$79.29 [9/11]**, above the <78 line; REGINALD graded the exit 9/11 as 0-of-3 NOT QUALIFYING — **read REGINALD's row, do not re-derive.**
- **Boundary #3 (Cushing <20M):** 21.824M [w/e 9/4] — **9.1% above, outside the band.**
- **HANS-T scannables:** unchanged at HANS's own 9/10 rows (UK 30Y 5.93, 7bp from T-13 orange — still the tightest line on the board; UK 10Y 5.36, 14bp from T-06). **HANS dark since 9/10; these are HANS's reads, not re-derived.**

**No fire on any registered trigger.** Near-trigger watches: **FT-12 (10bp) · FT-06 exit (0.16) · HANS-T-13 (7bp) · HANS-T-06 (14bp)**.
