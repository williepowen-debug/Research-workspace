# BOND — 2026-09-25 (Fri ~01:0x–02:xx ET) · PROME item 2 (Will-directed, 01:01 ET): FR2004 settlement timing RESOLVED · rates-move columns for the HENRY matched-date table

**Packet:** `inbox/2026-09-25_from-PROME_bounded-follow-up-explain-the-rates-move-with-HENRY-and-settle-the-FR2004-timing-question.md` (`40915c8c0`). **Peer:** HENRY builds the joint table at `AGENTS/HENRY/research/2026-09-25_rates-move-and-hike-alignment.md` and cites these columns. Nothing here is a trade or a gate change.

---

## 1 · FR2004 SETTLEMENT TIMING — RESOLVED: the as-of-Wednesday position INCLUDES auction awards from the award date

**Answer:** FR 2004A positions are kept on **trade-date** accounting, and a new Treasury allotment enters the dealer's reported position **on the day it is awarded**, not at settlement. **The 9/16 as-of therefore CONTAINS the 9/15 20Y-R (`912810UX4`) award**, even though it settled 9/18.

**Citations — primary: Board of Governors, *Instructions for the Preparation of Government Securities Dealers Reports, Reporting Form FR 2004*, Effective January 2022** (`federalreserve.gov/reportforms/forms/FR_200420220105_i.pdf`, downloaded 2026-09-25 01:04 ET; the current instruction book linked from the FR 2004 reporting-forms page):

| Where | Text (verbatim) |
|---|---|
| **p. GEN-6, §II.C "Allotments of New Securities"** | "Report the position taken in a new U.S. Treasury or MBS security allotment. **Include allotments that are awarded on a report date in that day's positions.**" |
| **p. A-1, FR 2004A** | "**Positions on the FR 2004A are reported using trade date accounting**, except for buybacks, which should be reported using settlement date accounting." Reportable positions list: "The position taken in a new U.S. Treasury… allotment. Include allotments that are awarded on a report date in that day's positions" · "**When-issued positions**" |
| **p. A-5** | "When-issued securities should be categorized based on the time remaining to maturity calculated from the issue date" ⇒ a 20Y award lands in the **11–21Y** bucket |
| **Appendix A (edit checks)** | "**Positions reported on the FR 2004A should be greater than or equal to the sum of net settled positions reported on the FR 2004SI and FR 2004WI.**" ⇒ the daily when-issued report is a SUBSET of the weekly FR 2004A, not carved out of it |

**What was wrong in `KB-BND-327`:** it inferred from the FR 2004WI's existence (a daily report of when-issued activity) that the weekly series might EXCLUDE unsettled awards. The instructions say the opposite: WI is additional detail, and A already includes the award. *Secondary corroboration only (not relied on): a web-search summary of the same instructions said allotments are reported on the FR 2004WI **and** the FR 2004A outright-long column until issued.*

### 1a · What the 9/16 print IS evidence of, now that the question is settled
For the 9/15 20Y-R (a **Tuesday** auction), the join's window (PRE 9/09 → POST 9/16) is **correct**: the award is inside it. So `KB-BND-326`'s grade **stands as evidence about absorption**, with its ordinary caveats (a weekly NET change across all dealer activity that week, not the award alone; published with an 8-day lag):
- **Long-end TOTAL −$1.8B** (fell) ⇒ no net warehousing across the long end that week.
- **11–21Y +$1.7B** = **the bucket the 20Y award is booked into** (A-5 rule above). >21Y −$2.6B.
- ⇒ **Dealers took the 20Y into inventory and then sold longer paper; net long-end stock fell.** Whether the leg that counts is the bucket or the total remains **WQ-157 leg ② (Will)**. The 9/16 print is now admissible for either reading.

### 1b · 🔴 A CONSEQUENCE THE QUESTION DID NOT ASK: the WQ-157 join mis-windows WEDNESDAY auctions — and the p=0.009 headline does not survive the fix
`monitors/fr2004_join.py:149` sets **PRE = the last as-of ON OR BEFORE the auction date**. Under trade-date accounting, a **Wednesday** auction's award is already in that Wednesday's as-of, so **PRE contains the award and the measured delta EXCLUDES it**. **75 of the 228 joined auctions (32.9%) are Wednesdays.** Where 9/24's `KB-BND-327` worried the POST side was too early, the real defect was that the PRE side was too late.

**Re-run (today's corpus, n=228; median +5-session DGS30 change after the auction; permutation test 20,000 resamples, seed 20260917; paired = `I'` fired AND dealer leg true; unpaired = `I'` fired, leg false):**

| Leg | AS-SHIPPED (PRE ≤ auction < POST) | Trade-date window (PRE < auction ≤ POST) — the window the instructions imply | PRE < auction < POST (2-week window for Wed rows) |
|---|---|---|---|
| **Long-end TOTAL > $1B** *(the 9/17 headline leg)* | −11.0bp, **p=0.019** | **−4.5bp, p=0.248** | −5.5bp, p=0.145 |
| Long-end TOTAL > 0 | −11.0bp, p=0.019 | −10.0bp, p=0.060 | −5.0bp, p=0.227 |
| 11–21Y > 0 | −4.0bp, p=0.349 | −10.5bp, p=0.028 | −9.5bp, p=0.055 |
| >21Y > 0 | −5.0bp, p=0.205 | **+2.5bp**, p=0.659 | −3.5bp, p=0.449 |

**Read:**
- **The "PAIRING INVERTS, p=0.009" result (`KB-BND-306`, the main evidence in front of Will on WQ-157 leg ②) is window-dependent and should NOT be cited as it stands.** On the correct window its own headline leg is −4.5bp at p=0.248. Significance migrates between legs as the window moves, and across 4 legs × 3 windows one p<0.05 is roughly what chance produces.
- **What survives:** paired fires are **not followed by yields rising** on any of the TOTAL or 11–21Y legs under any window. So there is still **no evidence the pairing detects a demand hole**; there is also no longer solid evidence that it detects the *opposite*. The separation test was already not significant as shipped and gets weaker: long-end TOTAL >$1B p=0.165 → 0.341 (2-week variant).
- **Reproduction gap, disclosed:** the 9/17 figure (−11.5bp, p=0.009) was computed at n=224 with an **unsaved ad-hoc script**. My as-shipped reproduction on today's n=228 gives −11.0bp at p=0.019: same direction, not identical. Scripts are now saved: `analysis/2026-09-25_fr2004_join_window_sensitivity.py` + `…_tradedate.py`.
- **Not done:** `fr2004_join.py` itself is NOT changed. Changing the instrument that produced evidence under a pending Will ruling is a PROME/Will call, not mine (`[[finding_instrument_defect_enacts_what_its_owner_is_fenced_from]]`). The recommended fix is PRE < auction ≤ POST (one-week window containing the award, per GEN-6/A-1).

---

## 2 · BOND'S COLUMNS FOR THE MATCHED-DATE TABLE (term premium · auction composition)

**Model difference, named:** **ACM** (Adrian–Crump–Moench, NY Fed) = a 5-factor affine model fitted DAILY to its own zero-coupon curve. It splits its fitted 10Y zero yield (`ACMY10`) into expected short-rate path (`ACMRNY10`) + term premium (`ACMTP10`). **KW** (Kim–Wright, Fed Board, FRED `THREEFYTP10`) = a 3-factor affine model that also uses survey forecasts of short rates, published WEEKLY. The two routinely disagree on SHORT-WINDOW changes. **Any term-premium claim must name the model.**

**Publication lags (observed at this pull, 2026-09-25 01:06 ET):** ACM daily xls runs **through 9/23** (≈T+1 business day; 9/24 not posted yet) · KW on FRED runs **through 9/18** (weekly refresh, ≈1-week lag; **cannot see 9/21–9/24**) · Treasury par/real curve **same evening** (9/24 posted) · FRED H.15 **T+1 ~16:15 ET** (DGS/DFII through 9/23; the 9/24 cells publish **today ~16:15 ET**).

| Obs date | 10Y par (Treasury = H.15) | **ACM TP10** | **ACM path (RNY10)** | ACM fitted 10Y zero | **KW TP10** | Note |
|---|---:|---:|---:|---:|---:|---|
| 9/14 | 4.97 | 0.6968 | 4.2550 | 4.9518 | 0.9590 | |
| 9/15 | 5.00 | 0.7090 | 4.2655 | 4.9745 | 0.9641 | 20Y-R `I'` fire |
| 9/16 | 5.01 | 0.6696 | 4.3154 | 4.9850 | **0.9719** (2026 high) | FOMC +25bp |
| 9/17 | 4.94 | 0.6108 | 4.2931 | 4.9039 | 0.9396 | |
| 9/18 | 5.01 | 0.6359 | 4.3351 | 4.9710 | 0.9595 | KW frontier |
| 9/21 | 4.96 | 0.5800 | 4.3388 | 4.9189 | *not published* | |
| 9/22 | 4.96 | 0.5758 | 4.3436 | 4.9194 | *not published* | 2Y 🟢 |
| **9/23** | **5.11** | **0.6454** | **4.4258** | **5.0712** | *not published* | **5Y composition failure; PMI 58.4** |
| 9/24 | 5.18 | *not published (ACM ≈T+1)* | — | — | *not published* | 7Y `I'` by 0.04pp |

**Changes (bp), same dates only:**

| Window | 10Y par | ACM zero | **ACM path** | **ACM TP** | **KW TP** |
|---|---:|---:|---:|---:|---:|
| **9/15 → 9/23** (the L47 fact) | **+11** | +9.7 | **+16.0** | **−6.4** | n/a (KW stops 9/18) |
| 9/15 → 9/18 (only window both models share) | +1 | −0.4 | +7.0 | **−7.3** | **−0.5** ⇒ model gap **6.9bp** |
| **9/22 → 9/23** (PMI + 5Y day, the largest move) | +15 | +15.2 | **+8.2** | **+7.0** | n/a |
| 9/16 FOMC day (9/15 → 9/16) | +1 | +1.1 | +5.0 | −3.9 | +0.8 |

**Auction-composition column (TreasuryDirect primary, % of competitive accepted, published at auction ~13:0x ET same day):**

| Date | Auction | Indirect | Dealer | BTC | Verdict |
|---|---|---:|---:|---:|---|
| 9/15 | 20Y-R `912810UX4` | — | — | — | `I'` fired (graded 9/15; pairing `KB-BND-326`) |
| 9/22 | 2Y `91282CRP8` | — | 13.19 | — | 🟢 clean on `I'` (dealer leg fails the downgrade counter only) |
| **9/23** | **5Y `91282CRN3`** | **54.31** (trailing-12 min 59.24; lowest 5Y since 2020-03-25) | **15.77** (max 15.61) | **2.21** (lowest since 2018-12-26) | 🔴 OLD conjunctive failure + `I'` · funding leg NONE (LIQUID, `KB-BND-330`) · kill NOT fired |
| 9/24 | 7Y `91282CRM5` | 57.20 (bar 57.24) | 12.53 | 2.42 | 🟠 `I'` by 0.04pp |

**Dealer stock:** FR2004 as-of 9/16 is evidence per §1 (TOTAL −$1.8B, 11–21Y +$1.7B). **The POST print for the 9/23 5Y and 9/24 7Y is the 9/30 as-of, published ~10/8.**

---

## 3 · PREFERRED INTERPRETATION + THE STRONGEST EVIDENCE AGAINST IT

**Preferred (A, policy-path / real-rate repricing):** Over 9/15→9/23 the 10Y rise is mostly the market pricing a higher real policy path, not a supply or term-premium absorption failure. Under ACM the expected-path component rose 16.0bp while term premium FELL 6.4bp. The move was real-led (DFII10 2.62→2.76 on H.15, 2.85 on the 9/24 Treasury cell, with breakevens flat to down). The 2Y and 1y1y printed sample highs. Funding stayed calm through the 5Y failure, and the 9/16 dealer print showed no net long-end warehousing.

**Strongest evidence against:** On the single largest day, 9/23 (+15bp), ACM's term premium ROSE 7.0bp, nearly half the move, on the same day the 5Y drew its smallest foreign-type share since March 2020. The next day the curve steepened from the long end (30Y +7 vs 2Y +2), a term-premium-shaped move neither model has published yet. The "path not premium" split is itself model-dependent on exactly these dates: over the only window both models share (9/15→9/18), KW's premium fell 0.5bp where ACM's fell 7.3bp, and KW cannot see 9/21 onward until next week.

⇒ **The honest split:** the FOMC week reads as path, but **9/23–9/24 is contested**, and the evidence that would decide it (ACM 9/24, KW 9/21–9/25, FR2004 as-of 9/23 and 9/30) has not been published yet.

---

## 4 · KEPT VISIBLE (per packet)
- **9/24 DFII10 cell = 2.85** on the U.S. Treasury real curve (posted 9/24 evening); **H.15/FRED publishes ~9/25 16:15 ET** = the `GATE-NEXUS-T12S-DFII10` anchor. NEXUS grades; BOND owns the data. 9/23 FRED cell 2.76 (confirmed 9/24 21:37 ET).
- **004 = TLT Sep-30 77P ×20, expires Wed 9/30.** TERRY's card. **NO ADD stands (WQ-280, Will 9/24 13:17 ET).** TLT $79.42 [9/24 close, yfinance], strike 3.0% below.

## 5 · GAPS
- ACM 9/24 and KW 9/21+ not yet published, so the 9/23–9/24 decomposition is incomplete.
- The 9/17 p=0.009 script was never saved; my reproduction differs (n and p), as disclosed.
- `fr2004_join.py` is not fixed (PROME/Will call). ~~The 9/2 per-tenor base-rating also used this join's pools and was not re-run.~~ ⚠️ **Corrected 9/25 ~03:xx: FALSE. That base-rating (`matrix_v2_base_rate.py`, `KB-BND-222`) uses no FR2004 data; the window fix cannot touch it. The error conflated it with the unrelated `KB-BND-314` grader-pool fix.**
- A-5 bucket rule applies to when-issued at report time; for a REOPENING (existing CUSIP), the award is booked to the existing issue's maturity bucket. Same 11–21Y bucket here, so it doesn't matter for 9/15, but it has not been separately verified.
