# Does credit transmission persist? — LIQUID, 2026-09-25 ~01:xx ET

**Asked by:** Will, item 3 of his 01:01 ET packet, relayed by PROME (`inbox/processed/2026-09-25_from-PROME_bounded-follow-up-does-credit-transmission-persist.md`).
**Instrument:** `scripts/transmission_check.py` (built for this; re-run after each FRED ICE BofA publication). Raw output: `reports/2026-09-25_transmission_check_output.txt`.
**Basis:** FRED, latest-revised (not as-first-published). ICE BofA OAS in bp. Repo rates minus IORB of the **same date** (KB-LIQ-126). H.4.1 series dated by their as-of Wednesday. yfinance raw closes (`auto_adjust=False`) as same-day proxies only. Book FLAT, $0. Nothing here is a trade or a gate change.

## Answer

**Transmission CONTINUES at the bottom rung. It has not broadened, and it has not reversed. The pace is ordinary on the base rate.** The 9/24 ICE cells are not published yet (FRED ~9/25 16:15 ET), so this grades the **9/23 set**, the latest. **The 9/25 16:15 ET publication is the next observation**, and the rule for grading it is pre-registered in §1c.

## 1. Credit — the quality ladder

### 1a. Levels and changes [FRED obs 9/23; d/d vs 9/22; 15-session vs 9/2]

History: 2023-10-02 → 2026-09-23. n = 779 daily changes and 765 fifteen-session changes. "≥" = how many past changes were at least this big.

| Tier | OAS 9/23 | d/d | d/d pct | ≥ (of 779) | 15-sess | 15-sess pct | ≥ (of 765) |
|---|---|---|---|---|---|---|---|
| IG | 77 | 0 | 73.4 | 514 | −4 | 31.1 | 569 |
| BBB | 95 | 0 | 71.4 | 495 | −4 | 34.6 | 529 |
| BB | 159 | +3 | 81.4 | 201 | +6 | 75.3 | 205 |
| B | 278 | +7 | 90.0 | 101 | +2 | 64.6 | 279 |
| CCC | 1,093 | +18 | 95.6 | 35 | +40 | 81.8 | 143 |
| HY index | 273 | +5 | 87.5 | 127 | +7 | 74.4 | 206 |
| **CCC−B gap** | 815 | +11 | 96.4 | 30 | **+38** | **85.9** | **109** |
| B−BB gap | 119 | +4 | 94.1 | 50 | −4 | 42.4 | 460 |

Last six prints (IG/BBB/BB/B/CCC/HY): 9/16 78/96/155/278/1076/270 · 9/17 78/95/156/277/1076/270 · 9/18 77/94/155/273/1083/268 · 9/21 77/95/153/270/1077/266 · 9/22 77/95/156/271/1075/268 · **9/23 77/95/159/278/1093/273**.

### 1b. Classification on the KB-LIQ-128 method (15-session change, ranked against its own history)

- **CONTINUES.** CCC +40bp over three weeks = 81.8th percentile. About 1 in 5 three-week windows is that big. The CCC−B gap +38bp = 85.9th percentile, about 1 in 7.
- **Not BROADENS.** No tier above CCC is unusual on the three-week window: B +2 (64.6th), BB +6 (75.3rd). BBB and IG *tightened* 4bp each.
- **Not REVERSES.** CCC and the CCC−B gap are at 2026 highs on 9/23.
- **The one-rung reach into B is a single day.** 9/23 B +7 = 90.0th percentile of days. CCC +18 = 95.6th, and the CCC−B gap +11 = 96.4th. It happened on a +15bp, real-yield-led 10Y day (DGS10 5.11, DFII10 +13 [9/23]). The three-week window does not show it (B +2).
- **Against last week's read, the dispersion signal is weaker, not stronger.** KB-LIQ-127/128 (window 8/26→9/16) had the CCC−B gap +49 at the 93.9th percentile. The window 9/2→9/23 has +38 at the 85.9th. CCC and CCC−BB set 2026 highs on 9/23, but three-week moves this size happen about one window in seven. Both are true.

### 1c. Pre-registered grade for the 9/24 cells (FRED ~9/25 16:15 ET) and each following print

Thresholds are the tiers' own daily p90/p95 over the same history (IG p95 +2 · BBB p95 +2 · BB p95 +9 · B p90 +7 · CCC p90 +11). The rules apply in this order:

| Outcome | Rule, on the new print's d/d |
|---|---|
| **REVERSES** | CCC ≤ −9 **and** B ≤ −4 (gives back at least half of 9/23) |
| **BROADENS** | B or CCC wider **and** any of IG ≥ +2 · BBB ≥ +2 · BB ≥ +9 (each tier's own p95). Also BROADENS if any of IG/BBB/BB's 15-session change reaches its p90 (IG +6 · BBB +7 · BB +19) |
| **CONTINUES** | B or CCC wider, and not BROADENS |
| **STALLS** | none of the above. The three requested buckets are not exhaustive, so this fourth one is named rather than forced into one of the three |

**Side finding, GATE-LIQ-069 L4 (checked while grading; no gate change):** HY +5bp [9/23] meets the L4 "credit underperforming" leg (the ≥5bp PROPOSED definition) for the first time in the prospective window; the prior max was +4 [9/9]. The equity leg failed on the same session: worst cohort name on 9/23 was APLD −4.6% (IREN −3.1 · NBIS −4.0 · CRWV +0.2, raw closes) against −15% ⇒ **NOT FIRED.** `gate069_legs.py` pairs the T+1 HY obs with the latest equity session (a cross-date pair). Its repair is owed.

**Same-day proxy, NOT a grade:** raw closes 9/23→9/24: HYG 78.10→77.89 (−0.27%) · JNK 93.97→93.68 (−0.31%) · LQD 103.89→103.15 (−0.71%), with ^TNX 5.114→5.162 (+4.8bp). ETF prices mix duration and spread and cannot split the tiers. They show **no reversal**, and nothing more. ⚠️ yfinance returned **no 9/22 bar** for any of these tickers, the same missing-bar fault as DX-Y.NYB (T3 `INSTRUMENT-FAULT`).

## 2. Funding — the gauges I actually observe, date-matched

| Date | SOFR−IORB | SOFR75−IORB | SOFR99−IORB | TGCR−IORB | SRF (RPONTTLD) | RRP |
|---|---|---|---|---|---|---|
| 9/16 | −3 | +2 | +5 | −5 | $0.001B | $5.38B |
| 9/17 (IORB 3.65→3.90) | −5 | 0 | +3 | −7 | $0.001B | $0.28B |
| 9/18 | −5 | 0 | +3 | −7 | $0.001B | $0.58B |
| 9/21 | −5 | +1 | +3 | −7 | $0.002B | $0.58B |
| 9/22 | −3 | +2 | +5 | −5 | $0.002B | $0.45B |
| **9/23** | **−3** | **+2** | **+5** | **−5** | **$0.001B** | **$0.46B** |

Reserves (WRESBAL, as-of Wed, $B): 8/26 2,924.9 · 9/2 2,894.5 · 9/9 2,991.3 · 9/16 3,013.8 · **9/23 2,930.2 (−83.6)**. TGA (WTREGEN): 9/16 877.0 → **9/23 977.1 (+100.1)**, from the 9/15 tax date, which more than covers the reserve drop. Cushion to the <$2.8T line: **$130B**.

**Read:** credit widened at the bottom on 9/23, and nothing moved in the overnight rate complex. SOFR99−IORB +5 sits 25bp under the GATE-LIQ-079 ARM line (+30). The SRF was unused. **There is no funding leg to the credit move in anything I observe.**

**⚠️ What I do NOT observe. A clean read above means "not visible in overnight rates, SRF, RRP and reserves", never "no funding strain":**
- **Tri-party repo:** I see the TGCR *rate* only. No volumes, haircuts or collateral mix.
- **Sponsored repo** (FICC/DTCC sponsored volumes): not pulled.
- **Dealer balance sheets** (NY Fed Primary Dealer statistics): last pulled for as-of **8/19** (8/28 session), not re-pulled. GATE-LIQ-076 W2 rests on that pull.
- **GCF repo**, **MMF flows** (ICI weekly), **FHLB advances**, **term repo**, intraday: not pulled.
- **FX swap / EUR cross-currency basis:** dark on both LIQUID and HANS (`HANS-T-12`).
- **SOFR and percentiles for 9/24:** publish 9/25 ~08:00 ET. Not in this read.

## 3. Quarter-end 9/30 — the normal pattern, then the test

### 3a. The normal pattern, from the last 10 quarter-ends (2024-Q1 → 2026-Q2)

Excess = the print minus that quarter's baseline (median of the 10 business days ending 5 days before the quarter-end), in bp.

| Q-end | base | QE-1 | **QE** | QE+1 | QE+2 | QE+3 | QE+5 | SOFR99 base | 99 QE | 99 +1 | 99 +2 | SRF on QE ($B) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-03-28 | −9 | +2 | +3 | +4 | +3 | +1 | +1 | −1 | +9 | +12 | +11 | 0.00 |
| 2024-06-28 | −8 | +2 | +1 | +8 | +3 | +1 | 0 | +2 | +4 | +8 | +8 | 0.00 |
| 2024-09-30 | −7 | +1 | +13 | +22 | +9 | +2 | 0 | +3 | +52 | +35 | +16 | 2.60 |
| 2024-12-31 | −3 | 0 | +12 | +3 | −6 | −10 | −8 | +7 | +28 | +9 | −4 | 0.00 |
| 2025-03-31 | −10 | +4 | +11 | +8 | +7 | **+8** | **+3** | −1 | +18 | +7 | +6 | 0.00 |
| 2025-06-30 | −12 | +10 | +17 | +16 | +12 | **+6** | **+5** | −2 | +27 | +16 | +12 | 11.07 |
| 2025-09-30 | −1 | −1 | +10 | +6 | +6 | +4 | 0 | +9 | +13 | +4 | +4 | 6.00 |
| 2025-12-31 | +3 | +3 | +20 | +7 | +3 | −1 | −3 | +12 | +23 | +10 | +2 | **74.60** |
| 2026-03-31 | −1 | −1 | +4 | +1 | +2 | +1 | −5 | +8 | +5 | +2 | +2 | 0.00 |
| 2026-06-30 | −2 | 0 | +6 | +4 | +2 | 0 | −4 | +6 | +9 | +2 | +2 | 0.00 |

- **Normal:** SOFR−IORB peaks on the date or the day after, a **median +10bp** above baseline (range +1 to +22). It is down to a median **+3 by QE+2** and **~0 by QE+3 to QE+5**. The SOFR99 tail spikes harder (median +15.5 on the date, max +52 in 2024-Q3) and is back to a median +5 by QE+2.
- **2026's two turns were small:** +4 and +6 on the date, gone by QE+2, with zero SRF use. That is the post-QT regime, with the Fed adding reserves through bill purchases (KB-LIQ-070).
- **SRF after the date is rare.** On QE+1 to QE+3, take-up was ≤$0.75B in 9 of 10 quarters. The exception is **$22.8B on 2026-01-02**, the day after the $74.6B 2025 year-end.
- **The only turns that did not decay** were 2025-Q1 and 2025-Q2 (excess still +8/+6 at QE+3 and +3/+5 at QE+5). That was the late-QT drift, while reserves were being drained, before QT ended.

### 3b. What would separate persistent pressure from the turn — the test Will can watch

Baseline for this quarter (median 9/9–9/22, date-matched across the 9/17 IORB change): **SOFR−IORB −3bp · SOFR99−IORB +5bp.** **A spike on 9/30 or 10/1 is the NULL (KB-LIQ-051).** SOFR for 9/30 publishes Thu 10/1 ~08:00 ET. About $183B of 2Y/5Y/7Y coupons settle on 9/30.

| # | Observation | Date observed (published) | Persistent pressure if | Historical hits (of 10) |
|---|---|---|---|---|
| P1 | SOFR−IORB | **Mon 10/5** = QE+3 (pub Tue 10/6) | **≥ +1bp** (excess ≥ +4) | 3: 2025-Q1, Q2, Q3 |
| P2 | SOFR−IORB | **Wed 10/7** = QE+5 (pub Thu 10/8) | **≥ 0bp** (excess ≥ +3) | 2: 2025-Q1, Q2 |
| P3 | SOFR99−IORB | **Fri 10/2** = QE+2 (pub Mon 10/5) | **≥ +22bp** (excess > +16, beyond every prior quarter) | 0 |
| P4 | SRF take-up (RPONTTLD) | **10/1, 10/2, 10/5** | **> $1B** on any of them | 1: 2025-Q4 (2026-01-02) |
| P5 | Reserves (WRESBAL) | as-of Wed 9/30 (H.4.1 Thu 10/1) · as-of Wed 10/7 (Thu 10/8) | **< $2.8T** on either | 0 (line never crossed) |

**Verdict rule, registered before the data:** **PERSISTENT = (P1 and P2) or P3 or P4 or P5. SEASONAL = none of them by the 10/8 publications.** P1+P2 together match exactly the two turns that did not decay. P1 alone also fired in 2025-Q3, which then decayed, so P1 alone is a warning, not a verdict. **GATE-LIQ-079 (ARM at SOFR99−IORB ≥ +30, ≥2 consecutive non-calendar days) is not meant to arm on a quarter-end print.** But its `non-calendar` list is itself still owed to DAEDALUS by 9/30, so that exclusion has not been written down yet. P3 is a watch line, not the gate.

## 4. Coverage gaps (preserved, standing)

1. **FRED ICE BofA history is a rolling ~3 years** (earliest obs returned: 2023-09-25). Every percentile in §1 is ranked against a calm window with **no 2020 or 2022 stress in it**. The same move would rank lower against a full cycle.
2. **Every figure here is latest-revised**, not as-first-published (`fetch.py` sends no `realtime_*`). The exception is the GATE-HY-REKILL watcher.
3. **HY-Energy OAS permanently unmeasured.** **HY breadth** (TRACE, ICE sector sub-indices) is terminal-gated, so breadth reads are tier-derived.
4. The funding blind spots in §2: tri-party volumes and haircuts · sponsored repo · dealer balance sheets (last pulled for as-of 8/19) · GCF · MMF flows · FHLB · FX-swap/cross-currency basis · SOFR 9/24 not yet published.
5. The quarter-end base rate has n=10 quarter-ends across two regimes (QT to 2025-12, then reserve-adding purchases). Two 2026 observations describe the current regime.
6. yfinance missing 9/22 bars (the same fault as T3's DX-Y.NYB).
