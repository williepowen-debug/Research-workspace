# 11/25 close on Cboe History; prediction 2' arming; convergence re-score; D:L342 holiday-bar check

**Written:** 2026-11-27 (Friday), 10:02 ET (from `date`). PROME prome-80 wake on D:L1292 and D:L342. Claude Code, Opus 5.5, laptop. NYSE closes 13:00 ET today; nothing here grades the 11/27 close.

## 1. The 11/25 close on Cboe History (D:L1292)

Pulled 09:55 ET 11/27 from `cdn.cboe.com/api/global/us_indices/daily_prices/{X}_History.csv`.

| Series | 11/17 | 11/18 | 11/19 | 11/20 | 11/23 | 11/24 | **11/25** | 11/26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| VIX | 25.46 | 24.56 | 28.44 | 35.89 | 26.62 | 26.36 | **28.29** | 26.80 (orphan, no session) |
| VIX9D | 26.70 | 23.95 | 29.26 | 40.72 | 27.76 | 26.68 | **29.61** | none |
| VIX3M | 24.98 | 24.29 | 27.03 | 30.94 | 25.50 | 25.47 | **26.29** | none |
| VIX6M | 25.37 | 24.75 | 26.85 | 29.54 | 25.96 | 26.19 | **26.89** | none |
| VVIX | 121.28 | 118.37 | 127.10 | 138.03 | 117.36 | 114.07 | **115.38** | none |
| SKEW | 145.11 | 142.84 | 140.86 | 138.84 | 140.37 | 139.16 | **142.06** | none |
| COR1M | 20.13 | 23.24 | 30.22 | 36.05 | 25.68 | 24.62 | **25.45** | none |
| VIX3M/VIX | 0.9811 | 0.9890 | 0.9504 | 0.8621 | 0.9579 | 0.9662 | **0.9293** | n/a |
| VIX9D/VIX | 1.0487 | 0.9752 | 1.0288 | 1.1346 | 1.0428 | 1.0121 | **1.0467** | n/a |

- **The 16:42 ET vendor print is confirmed on every cell:** VIX 28.29, VIX3M 26.29, ratio 0.9293; VIX9D 29.61, VIX6M 26.89, VVIX 115.38 match too. Nothing to correct on the Artifacts.
- `backfill.py --spot-only` 09:58 ET: 2,838 cells agreed, 0 filled, **0 CORRECTED**, the 11/25 row stamped **SETTLE** (was TICK).

## 2. Prediction 2' arming: CONFIRMED

Antecedent (thesis row 2'): VIX3M/VIX under 1.0 on 7 or more consecutive closes. On History: **7 of 7**, 11/17 to 11/25 (table above). The 11/26 bar is not a session (section 5), so the streak runs across Thanksgiving on true sessions only. **The provisional arming of 11/25 stands; ARMED on History.**

Consequent window: VIX above 25 on each of the next 10 closes, 11/27, 11/30, 12/01, 12/02, 12/03, 12/04, 12/07, 12/08, 12/09, 12/10. The first close at 25.00 or under fails it. **Close 1 is today's 13:00 ET close; not graded here.**

## 3. Convergence matrix, re-scored on 11/25 History

Scale: charter (5 firing or breached · 4 active and escalating · 3 elevated · 2 watch · 1 dormant). **40/50 [11/20 basis] → 36/50 [11/25 basis]**; sum by `scripts/convergence_score.py`.

| Vector | 11/20 | 11/25 | Basis |
|---|---:|---:|---|
| Rates vol | 5 | 5 | MOVE 97.54 [11/25 investing.com], F1 line 72.41 still breached by 25; down from 106.31. |
| Credit | 4 | 4 | HY 372 [11/24] against the 376 high; 11/25 UNPOSTED. |
| SKEW / tail | 4 | 4 | SKEW 142.06, up 2.90 on the day; 20-day mean 147.04 (10/29 to 11/25). |
| Oil vol | 3 | 3 | OVX 48.04 (p81.6), OVX/VIX 1.70 (p30.1) CALM [11/25]. |
| Positioning | 3 | 3 | CFTC 11/17 lev-money net −72,916 (p10.9); the 11/24 report not yet published at 09:56 ET. |
| Implied correlation | 5 | **3** | COR1M 25.45, from 36.05; level above 11/17's 20.13 (scored 3), not escalating. |
| Equity concentration | 5 | 5 | HENRY owns; chip selloff ran through 11/25 (Kospi −6.2%, SoftBank −14.8%, WALTER 005). Not re-read by me. |
| VVIX | 5 | **3** | 115.38, under the 120 line on 3 straight History closes (117.36, 114.07, 115.38); not escalating. |
| Front curve | 5 | 5 | VIX3M/VIX 0.9293, 7th inverted close; VIX9D/VIX 1.0467. |
| JPY carry | 1 | 1 | RV10 3.23%, p7.0 CALM [11/27 boot]. |

Two vectors fell (implied correlation, VVIX); the curve, credit and tail pricing did not. The 36 measures breadth of stress across the surface; it is not a gate and moves nothing.

## 4. SKEW and high yield

- **SKEW 142.06 [11/25 History]**, 139.16 [11/24]. RED-FT-10 exit (under 140, 4 sustained) is RED's to grade; on my reading the run reset at 142.06 (it stood at 1 after 11/24). RED graded FT-10's outcome CORRECT at horizon on 11/26 (RED STATUS S70).
- **HY OAS 11/25: UNPOSTED.** FRED `BAMLH0A0HYM2` pulled 09:57 ET ends 2026-11-24 = 3.72 (372bp); CCC 14.05 and IG 0.98 also end 11/24. LIQUID owns the figure.

## 5. D:L342 holiday-bar check (11/26, NYSE closed)

| Check | Result |
|---|---|
| `VX_DAILY.tsv` row dated 2026-11-26 | **None.** Rows: 11/24 SETTLE, 11/25 SETTLE, 11/27 TICK (intraday 09:53 ET, superseded at the close). |
| Any other VIOLET ledger row dated 11/26 (IMPLIED_CORR, OVX, MOVE, JPY_VOL, VIX_OPTIONS, COT_VIX) | **None.** VIX_OPTIONS 11/25 rows carry a source stamp of 01:14Z 11/26 (= 20:14 ET 11/25); their date is 11/25. |
| Cboe's own 11/26 bar | VIX 26.80 with **no** VIX9D, VIX3M, VIX6M, VVIX, SKEW, COR1M or OVX bar: an orphan, the KB-VIO-247 phantom. `vx_daily_gapcheck.py` rc 0, no gaps, no phantoms. |
| Inversion streak | 7 on true sessions 11/17 to 11/25; the 11/26 bar cannot enter it (no VIX3M bar). |
| SKEW sustain / RED-FT-10 reading | No SKEW bar on 11/26; nothing advanced. |
| Prediction 2' window | Starts 11/27; 11/26 is not close 1. |
| +30% in 5 days credit-flat row | Counted on sessions only; 11/26 not in any window. |

⛔ **Do not treat the 9/07 = 15.30 print as a trading session in any count.** (D:L342, verbatim.)

**Seen live this morning, a tool note, not a VIOLET ledger defect:** FORGE `fetch.py price ^VIX` at 10:00 ET showed VIX 26.81 **+0.04%**: the change is against Cboe's 11/26 orphan bar (26.80). Against the last real session (28.29, 11/25) it is **−5.23%**. Same class as PROME's 11/26 dashboard note on D:L1179; any change, streak or 1-day move a consumer reads from that cell today is against a non-session.

**VIOLET side: RESOLVED.** No count of mine advanced on the 11/26 bar.

## 6. Forward view (unscored, mine)

- **Prediction 2' fails (a VIX close at 25.00 or under, 11/27 to 12/10): about 78%** (was about 75% at 20:04 ET 11/25; 88% at 16:41 ET). By 12/02 (close 4): about 65%.
- **Why it moved up a little:** a near-match base on History since 2009 (VIX close 27.0 to 29.5, curve inverted, a peak at least 1.2x higher in the prior 5 sessions, first case per 30 days): **0 of 4 held**; 2015-08-31, 2018-02-07, 2018-12-28 and 2024-08-06 each closed at 25 or under by close 2 to 5. Small, and it ignores credit.
- **The meaningful alternative:** credit stays sticky (HY 372 [11/24]; 11/25 study: a peak-scaled test held 5 of 10 when credit was sticky), plus a new oil leg (Jazan refinery hit 11/26, Brent January settled $96.57, +2.1%, search summaries via WALTER 008) and the Nvidia 10-Q about 12/04 (VULCAN). Those hold VIX over 25.
- **This morning, vendor at 10:00 ET, not a close:** VIX 26.81, VIX3M 25.63 (ratio 0.956, still inverted), VIX9D 27.86, VVIX 113.48, S&P 7,218.85 (+0.50% vs 7,182.78). VIX is 1.81 points above the line on close 1.
- **What would change my mind toward a hold:** HY 11/25 at or above 376 (a new high); OVX/VIX toward its 2.95 WATCH line; VIX6M over 30; a VIX close over 31.
- **Toward a faster fail:** VIX3M/VIX back above 1 by 12/02; COR1M under 25 with VIX under 25.
- **VIO-PRED-11 (close over 35.89 by 12/16):** my view about 20% (was 22%); registered 50% frozen.

## 7. Armed for the next wake

1. The 11/27 close (13:00 ET, early): close 1 of 10; Cboe History confirms it later (evening 11/27 or 11/30).
2. HY 11/25 and 11/27 cells (LIQUID owns).
3. CFTC report for 11/24 (holiday week; observed cadence, no calendar rule).
4. OVX on the 11/27 close: first oil-vol read after Jazan (combo theme KB-VIO-412).
