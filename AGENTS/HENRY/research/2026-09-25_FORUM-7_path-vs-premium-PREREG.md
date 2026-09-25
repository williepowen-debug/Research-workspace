# FORUM-7 — PATH or PREMIUM: the 9/22→9/24 10Y rise · PRE-REGISTERED VERDICT RULE

**Convener/author:** HENRY · **Co-author:** BOND (§BOND, its own dated section) · **Consumer:** NEXUS · TERRY informed only · **Authority:** Will 02:20 ET 9/25 *"lets proceed with #1"*; PROME packet `08c4f5fb5`; DOCKET L475.
**Drafted:** 2026-09-25 02:25 EDT (`date`). **BLIND RECEIPT:** at draft time the NY Fed ACM file (`ACMTermPremium.xls`, sheet "ACM Daily", sha256 `75a5eda9c3cfc9a3…`) ends **2026-09-23 — the 9/24 cell is NOT published and was NOT read by HENRY.** KW (FRED `THREEFYTP10`) ends 9/18. Base-rate script dropped every date ≥9/24 before printing (`research/2026-09-25_FORUM-7_baserates.txt`). **Timing claim = this file's commit precedes the ACM-9/24 cell's first read** (checkable by git log).

## 1. The question and the premise
Of the 10Y's rise over **9/22 close → 9/24 close** (Treasury par 4.96 → 5.18, +22bp), how much was term premium? **Shared premise (ASSUMED, not OBSERVED):** an affine model's TP/path split is a valid attribution of a 2-session move. Every branch rests on it.

## 2. Instruments (grading basis)
| Leg | Series · unit | Observations read | Publishes | Status |
|---|---|---|---|---|
| **D1 (deciding)** | ACM Daily `ACMTP10`, `ACMY10` (percent → bp ×100) | 9/22 and **9/24** cells | NY Fed ≈T+1 (~9/25) | **UNKNOWN** |
| **D2 (divergence check)** | FRED `THREEFYTP10`, `THREEFY10` (percent → bp) | 9/22 and **9/24** daily cells | FRED weekly (~9/28–29) | **UNKNOWN** |
| D3 (qualifier, BOND) | FR2004 as-of 9/23, WQ-290 trade-date window | see §BOND | Thu 10/1 ~16:15 ET | UNKNOWN |
| K1 KNOWN | ACM 9/22→9/23: TP **+7.0**, zero-yield **+15.2** (share 0.46) | — | — | known; not deciding alone |
| K2 KNOWN | futures path 9/22→9/24: post-Oct/Dec EFFR +4.0, SR3Z27 +19.0, SR3Z28 +22.5 (`research/2026-09-25_rates-move-and-hike-alignment.md`) · 2s30s +2 · 5Y/7Y composition | — | — | **excluded from deciding legs — already seen** |

**Vintage (FROZEN-ON-REVISABLE, WQ-175):** each model cell resolves on the vintage FIRST pulled at its grade (download time + sha256 recorded). If a later vintage moves the 9/22 or 9/24 cell by >1bp before FINAL, grade on BOTH vintages and edit nothing; differing verdicts ⇒ INDETERMINATE-BY-VINTAGE.

## 3. Verdict rule (MECE; applied in this order; first match wins)
Let **s = ΔACMTP10 / ΔACMY10** over 9/22→9/24 (unrounded), and **g = |ΔACMTP10 − ΔTHREEFYTP10|** in bp, same dates.
1. **CANNOT-EVALUATE** — the ACM 9/24 cell is not published by FINAL, **or** ΔACMY10 < +10bp (denominator too small to form a share). *(Basis: instrument branch — LESSONS "a verdict set that classifies only the data cannot report a broken instrument".)*
2. **UNANSWERABLE** — **g > 18bp.** *Basis:* p90 of g over 2-session windows with ΔACMY10 ≥ +15bp, 2022–9/23, n=61 (p80 14.3 · p50 7.6); 1990+ p90 16.2, n=375. Percentiles on overlapping windows — dispersion valid, counts not. **The 6.9bp observed gap (9/15→9/18, a 3-session window) does NOT exceed X** (73rd pct of unconditional 3-session gaps, 2022+) — it is ordinary disagreement. If KW 9/24 is unpublished at FINAL, this test is **KW-UNCHECKED** and the verdict carries that tag.
3. **PREMIUM** — **s ∈ [0.50, ∞)**.
4. **INDETERMINATE** — **s ∈ [0.25, 0.50)**.
5. **PATH** — **s ∈ (−∞, 0.25)**.
Boundary owner: the lower bound of each half-open interval. **Thresholds 0.25 / 0.50: JUDGEMENT** (majority / quarter), with the base rate stated so the prior is visible: on ACM 2-session rises ≥15bp, **s ≥ 0.50 in 73%** (n=376, 1990+; 73% of n=62, 2022+), **s < 0.25 in 9–11%**. ⇒ **PREMIUM is ACM's ordinary answer on a big up-move; PATH would be unusual.** ⚠️ **KW is NOT a deciding share:** its share on the same class is pinned at **0.44–0.56** (p10–p90, n=225) — a 0.50 bar would be a coin flip inside its own structure, so KW enters only through g.
**Reachability (no leg is satisfied at registration):** with K1 fixed, PREMIUM needs the 9/24 ACM TP change ≥ ~+4bp on a ~+7bp day; PATH needs it ≤ ~−1.5bp. Both are open.

## 4. Consequence per consumer
| Verdict | NEXUS (real-rate leg, `GATE-NEXUS-T12S-DFII10`) | HENRY cyclical channel | BOND | Positions |
|---|---|---|---|---|
| PATH | attribution note only — the DFII10 level/regime read is unchanged in every branch (NEXUS decides) | "higher for longer 2027–28" stands for the burst; a real-yield letter may register as a PATH letter | §BOND | NONE |
| PREMIUM | same; attribution = duration compensation | **my preferred (A) is WRONG for 9/23–9/24**; (A) holds for the FOMC week only; axis-1 re-attributed | §BOND | NONE |
| INDETERMINATE | same | carry both; no attribution claim for the burst | §BOND | NONE |
| UNANSWERABLE / CANNOT-EVALUATE / BY-VINTAGE | same | record model-dependence; no attribution claim | §BOND | NONE |

## 5. Invalidation
Whole question VOID only if **NY Fed announces an ACM methodology change or discontinues the Daily sheet, or FRED discontinues `THREEFYTP10`, before FINAL** (named sources). **A later 10Y reversal does NOT invalidate** — it cannot change how a past window decomposed (considered and rejected; it changes only consumers' use of the answer).

## 6. Grade schedule (anchor types named)
**P1** ACM 9/24 cell — first pull after NY Fed posts (~9/25; publisher-controlled): provisional s, verdict tagged KW-UNCHECKED · **P2** KW 9/22–9/24 cells (~9/28–29; publisher-controlled): g · **FINAL = Thu 10/1 after FR2004 as-of 9/23** (~16:15 ET; publisher-controlled) → **verdict written by the 10/2 boot (CHOSEN: last useful date before NFP re-prices the path)**. HENRY grades, packets PROME; BOND co-grades D3. A leg not published by FINAL is graded per branch 1 / the KW-UNCHECKED tag — never waited on past 10/2.

## §BOND — co-author section
*(BOND writes: D3 bucket(s) + threshold + basis for the 9/23 5Y award, the PREMIUM-qualifier it implies, BOND's consequence column, named alternatives if it disagrees with §3, and its co-sign line.)*
