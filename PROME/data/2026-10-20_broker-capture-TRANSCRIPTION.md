SUPERSEDED 2026-10-22 — history, not the current book — the 10/22 11:01 ET capture (PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md, FORGE ec5a7058b, $39,876.06) is the latest accepted broker evidence; every figure below is the 10/20 record.
# 2026-10-20 broker capture — TRANSCRIPTION (Fidelity Traditional IRA)

**Received:** 2026-10-20 ~10:43 ET (image files Capture1.JPG / Capture2.JPG on Will's Desktop; file times are NOT capture/quote/fill clocks — those are UNKNOWN). Will to TERRY: "getting crushed currently but sold one of the QQQ puts this morning". **Intraday session marks [10/20], not closes, not executable quotes.**

**Account:** Fidelity Traditional IRA — identifier obscured in the capture (last four on file •1326; continuity INFERRED). No Robinhood evidence.

**Transcription basis:** TERRY's visual read `AGENTS/TERRY/research/2026-10-20_broker-receipt/source.json` (commit ef82d240d), INDEPENDENTLY re-read by PROME from the same two images 11:1x ET 10/20 — all 23 rows and 5 activity rows agree. Image sha256: Capture1 `86238c32f62467f4531a97fad4b267b61b82d9267daae4c763be9680dafef344` · Capture2 `6f011c952c550381bfc92f43da7d1f2ee5a837d5b3dd54cf9da72cfff604c865`. Images not committed.

## ① Account summary

| Cash (money market) | Pending activity | Account total | Today's G/L | Total open G/L |
|---|---|---|---|---|
| $17053.29 (45.07%) | -83.00 | $37840.91 | -2480.70 (-6.15%) | -2340.98 (-10.09%) |

**To-the-cent check (PROME, 10/20):** Σ positions $20,870.62 + cash $17,053.29 + pending −$83.00 = **$37,840.91** = displayed account total ✓ · Σ row today G/L = −$2,480.70 ✓ · Σ row open G/L = −$2,340.98 ✓ · every row value − basis = open G/L ✓. Cash continuity: 10/19 mirror cash $18,574.21 − 10/19 pending $1,520.92 = $17,053.29 ✓.

## ② Positions (23 rows, capture order)

| Symbol | Type | Expiry | Strike | Qty | Value | Cost basis total | Today G/L | Open G/L |
|---|---|---|---|---|---|---|---|---|
| USO | Call | 2026-10-30 | 165 | 2 | $370.00 | $586.32 | -280.66 | -216.32 |
| WAL | Put | 2026-12-18 | 65 | 4 | $320.00 | $682.65 | -280.00 | -362.65 |
| QQQ | Put | 2026-10-20 | 719 | 1 | $98.00 | $277.66 | -241.00 | -179.66 |
| KRE | Put | 2026-11-27 | 67 | 4 | $268.00 | $510.65 | -240.00 | -242.65 |
| WAL | Put | 2026-12-18 | 70 | 2 | $340.00 | $551.33 | -210.00 | -211.33 |
| ZION | Put | 2026-11-20 | 62.5 | 2 | $220.00 | $435.33 | -210.00 | -215.33 |
| QQQ | Put | 2026-10-20 | 715 | 1 | $37.00 | $200.66 | -161.00 | -163.66 |
| USO | Stock | -- | -- | 35 | $5470.15 | $4266.43 | -158.20 | 1203.72 |
| QQQ | Put | 2026-10-22 | 715 | 1 | $299.00 | $432.66 | -133.66 | -133.66 |
| USO | Call | 2026-10-23 | 163 | 1 | $82.00 | $289.66 | -133.00 | -207.66 |
| USO | Call | 2026-10-28 | 165 | 1 | $139.00 | $335.66 | -128.00 | -196.66 |
| OZK | Put | 2026-11-20 | 40 | 4 | $40.00 | $322.65 | -88.00 | -282.65 |
| KRE | Put | 2026-12-31 | 65 | 2 | $210.00 | $337.33 | -64.00 | -127.33 |
| CRWV | Put | 2026-10-23 | 56 | 1 | $45.00 | $179.66 | -51.00 | -134.66 |
| APO | Put | 2026-12-18 | 95 | 1 | $135.00 | $1184.67 | -45.00 | -1049.67 |
| KRE | Put | 2026-12-18 | 60 | 3 | $105.00 | $878.02 | -30.00 | -773.02 |
| KRE | Put | 2026-12-18 | 60 | 2 | $70.00 | $513.34 | -20.00 | -443.34 |
| VLO | Stock | -- | -- | 3 | $1282.02 | $1296.73 | -17.91 | -14.71 |
| TBT | Stock | -- | -- | 5 | $198.60 | $172.01 | -4.50 | 26.59 |
| CMG | Put | 2026-10-30 | 28 | 1 | $41.00 | $54.66 | -4.00 | -13.66 |
| AAPL | Stock | -- | -- | 4 | $1368.98 | $94.58 | -2.78 | 1274.40 |
| APD | Stock | -- | -- | 2 | $597.47 | $589.57 | 0.17 | 7.90 |
| GLD | Stock | -- | -- | 24 | $9134.40 | $9019.37 | 21.84 | 115.03 |

Last prices / avg cost per row: see the image read in `source.json` and Capture1; e.g. USO $156.29, VLO $427.34, GLD $380.60, AAPL $342.245, APD $298.735, TBT $39.72; QQQ 719P $0.98, 715P Oct20 $0.37, 715P Oct22 $2.99.

## ③ Activity — Pending panel (Capture2, all dated 2026-10-20, fill clocks UNKNOWN)

| # | Order | Status | Amount |
|---|---|---|---|
| 1 | BTO 1 USO Oct-30-2026 165C, limit $3.17 Day | Filled at $3.15 | −$315.66 |
| 2 | BTO 1 USO Oct-30-2026 165C, limit $3.15 Day | Verified Canceled | — |
| 3 | BTO 1 QQQ Oct-22-2026 715P, limit $4.32 Day | Filled at $4.32 | −$432.66 |
| 4 | BTO 1 QQQ Oct-22-2026 715P, limit $4.26 Day | Verified Canceled | — |
| 5 | STC 1 QQQ Oct-20-2026 720P, limit $6.44 Day | Filled at $6.66 | +$665.32 |

Net 665.32 − 432.66 − 315.66 = **−$83.00** = displayed pending ✓. The panel is a crop; it is not a complete working-order census.

## ④ Deltas FROM THE MIRROR (`git show HEAD:FORGE/STATUS.md`, 10/19 reconcile; parsed by `positions_from_forge.py`)

- **GONE:** QQQ Oct-20 720P ×1 — sold STC $6.66, net $665.32 (activity row 5). Realized DERIVED +$474.66 vs $190.66 basis (TERRY).
- **NEW:** QQQ Oct-22 715P ×1 — BTO $4.32, net $432.66 (row 3).
- **QTY CHANGE:** USO Oct-30 165C 1→2 — BTO $3.15, net $315.66 (row 1); basis $270.66 + $315.66 = $586.32.
- **MARK ONLY:** the other 21 Fidelity rows (corrected from "20" — ANVIL caught it: 23 − 1 new − 1 qty change = 21). Mirror 23 rows → capture 23 rows.
- Still displayed despite approved sales (no closing fill in this crop): WAL 65P ×4 (WQ-429 window ended 10/19) · OZK 40P ×4 (WQ-428 backstop 15:30 ET 10/20) · TBT ×5 (WQ-357).
- QQQ 719P basis $277.66 vs $276.66 on 10/19 (+$1.00 display change; TERRY flags, not certified).

