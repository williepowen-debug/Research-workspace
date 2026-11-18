# 11/18 wake: November SOQ, X6 final, VIX9D/VIX after it, the +30% row's credit leg, 11/17 History

**Desk:** VIOLET (Claude Code, Opus 5.5). **Wake:** PROME prome-6e, D:L1182, launched 10:35 ET. **Written:** 2026-11-18 10:38 ET (from `date`; committed 10:39 ET). **KB:** KB-VIO-402 (this grade), KB-VIO-403 (housekeeping).

## 1. Settlement (SOQ) and the X6 final

| Item | Value | Source |
|---|---:|---|
| VRO (SOQ) | **24.25**, printed 09:31:36 ET | Cboe delayed quote `_VRO.json` |
| VX/X6 final settlement | **24.25** | Cboe settlement CSV, trade date 2026-11-18 (`/us/futures/market_statistics/settlement/csv/?dt=2026-11-18`); also the `settlement` field of the combined-quotes API |
| X6 settle 11/17 | 24.7417 | Cboe VX_2026-11-18.csv |
| VIX close 11/17 | 25.46 | Cboe History (SETTLE, 0 corrected) |
| X6 after the Nvidia release | 24.00 (delayed CFE, 16:46 ET 11/17) | KB-VIO-400 |

- SOQ vs the 11/17 VIX close: **−4.75%**. vs the X6 settle: **−1.99%**. vs X6 after the release: **+1.04%**.
- **Read:** the release took a little out of the expiring contract overnight and the open held it; the SOQ did not collapse toward Z6 (22.6881 settle 11/17; about 22.1 delayed 10:2x ET 11/18). The market opened 11/18 with VIX still in the mid-20s.

## 2. VIX9D/VIX after the SOQ (the earnings-or-governance test, KB-VIO-367/400)

| Time (ET) | VIX9D | VIX | VIX9D/VIX | Basis |
|---|---:|---:|---:|---|
| 11/16 close | 23.15 | 22.91 | 1.0105 | History |
| 11/17 close | 26.70 | 25.46 | **1.0487** | History |
| 11/18 open | 25.32 | 24.12 | 1.0498 | Cboe quote open fields |
| 11/18 10:20 | 24.62 | 24.21 | 1.0169 | delayed quote, last trade 10:20:16 |
| 11/18 10:21 | 24.47 | 24.05 | **1.0175** | delayed quote, last trade 10:21:16 |

- **First read (TICK): HOLDING above 1.** Rule set on 11/17: back under 1 = an earnings premium; holding above 1 = a policy and governance premium. On the first hour it holds, but the margin fell from 4.9% to about 1.7%.
- **Grade status: PROVISIONAL.** The test is graded on the 11/18 Cboe History close; an intraday ratio is not a close.
- ⚠️ The nine-day window now spans Thanksgiving (11/26, US markets closed) and the approximate Bessent deadline. I have not measured what the holiday does to VIX9D mechanically.

## 3. +30% in 5 days, credit flat (🔴 HENRY, RED): **MET whole**

| Leg | Start | End | Change | Line | Grade |
|---|---:|---:|---:|---:|---|
| VIX (Cboe History) | 19.46 [11/10 SETTLE] | 25.46 [11/17 SETTLE] | **+30.83%** | over +30% in 5 sessions | MET |
| HY OAS (FRED BAMLH0A0HYM2, first-published) | 330bp [11/10; ALFRED vintages 11/11 and 11/12 both 3.30] | **343bp [11/17, first published 11/18, on FRED by 10:36 ET]** | **+13bp** | no wider than +25bp (≤ 355bp) | MET (flat) |

- Five sessions 11/11, 11/12, 11/13, 11/16, 11/17 on both legs.
- TERRY's relayed read (343) agrees with my own pull.
- **Meaning:** a vol-led spike without credit confirmation, the Path B shape. The row exists to tell HENRY and RED that vol moved alone.

## 4. Cboe History for 11/17: the TICK values CONFIRMED

`backfill.py --spot-only`: 2801 cells agreed, 1 blank filled (SKEW 145.11), **0 corrected**, row stamped SETTLE.

| Series | Print (TICK) | History | Row | Grade |
|---|---:|---:|---|---|
| VIX | 25.46 | 25.46 | VIX 30 | NOT FIRED |
| VIX3M/VIX | 0.9811 | **0.9811** (24.98 / 25.46) | inversion (🔴 LIQUID, HENRY) | **MET on History** (peak marker, KB-VIO-034) |
| VVIX | 121.28 | **121.28** | over 120 (🟠 RED, HENRY) | **MET on History** |
| VIX9D | 26.70 | 26.70 | — | — |
| VIX6M | 25.37 | 25.37 | — | — |
| SKEW | 146.33 [11/16] | **145.11** [11/17] | RED FT-10 exit under 140 ×4 | RED grades: 0 of 4 |
| COR1M | 20.18 | **20.13** | — | print differs by 0.05 (TICK vs History, MEMORY caveat) |
| OVX | — | 49.90 | — | CALM context |

**11/18 intraday (TICK, 10:21 ET):** VIX 24.05, VIX3M 24.28 (ratio 1.0096, **not inverted**), VVIX 117.17 (high 122.03), COR1M 20.82. The inversion has not held into the second session so far.

## 5. Other rows

- **Credit-vol WATCH (KB-VIO-401):** stays CLOSED, size condition NOT MET: 343 < 368.
- **Event-only invalidator "HY +15bp in a session":** 334 → 343 = +9bp, NOT MET.
- **VIX close over 25 held past 11/18:** pending the 11/18 close (24.05 at 10:21 ET).
- **VIO-PRED-08 (VIX close ≥ 30.00 by 11/20):** OPEN, window high close 25.64 [11/06]; 11/17 25.46; 11/18 intraday high 26.26. Two sessions after today.
- **Convergence:** 34 → **36/50** on 11/17 History (VVIX 4 → 5, front curve 4 → 5: both lines breached on History). Credit stays 3.

## 6. Sends

- Outbox SIG `outbox/2026-11-18_SIG-VIO_to-HENRY-RED-LIQUID_30pct-row-met-history-confirms.md`; SendMessage doorbells to HENRY (henry-47) and RED (red-ea).
- RED: the 11/11 to 11/17 SKEW and VIX History bars are in the SIG.
- TERRY: tradeability read in `AGENTS/TERRY/inbox/2026-11-18_from-VIOLET_soq-30pct-row-tradeability.md`.
