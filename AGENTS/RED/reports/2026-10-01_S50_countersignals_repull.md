# RED counter-signals — RE-PULLED 2026-10-01 (S50), supersedes the 9/6 table

**Supersedes** `reports/2026-09-18_S46_status_countersignals_folded.md`. That file is kept as the dated 9/6 record and is never cited as current. Every value below is RED's own pull on 10/01: FRED (DGS30, DGS10, DFII10, T5YIFR, OVXCLS, DCOILBRENTEU, BAMLH0A0HYM2/H0A1HYBB/H0A3HYC, BAMLC0A0CM, VIXCLS, ICSA, PAYEMS, UNRATE, CIVPART, CES0500000003, CPILFESL), yfinance closes (KRE/WAL/OZK/TLT), CBOE `SKEW_History.csv` via boot.py, and the Cleveland Fed nowcast. **Row weights are re-set here** (P(bull read right) / P(bear read right)). **The six hypothesis weights are NOT re-derived here**: that pass runs after the Fri 10/2 jobs print (see the end).

| Signal | Value [date] | vs 9/6 table | Bull read | Bear read | RED Wt (was) |
|---|---|---|---|---|:--:|
| **10Y real / 30Y** | **2.93 / 5.64** [9/30] | 2.42 / 5.25 [9/3]: **+51bp / +39bp**; +30bp real since 9/22 | breakevens flat (5y5y 2.36), so this is real/term premium, not inflation; the Fed hiked 9/16, so some is policy, priced | **the bear's strongest row got materially stronger**: the price of money is the transmission channel, and it moved ~50bp in four weeks with no inflation scare to explain it | **20/80 bear** (30/70) |
| **HY OAS** | **312** [9/30]; BB 194 · B 316 · CCC 1,179 | 265 [9/11]: **+47bp** | still historically tight (full-sample P(>320 s=3) ≈ 24.5%); IG 84 lags (speed inside HY, not systemic) | direction + pace; FT-02 (>320 s=3) **8bp away**; the widening is broad-tier (BB+B 82% at the FT-01 exit) | **50/50** (60/40 bull) |
| **CCC OAS** | **1,179** [9/30] | 1,076 [9/11]: +103bp | bottom-tier, ~13% of index flow (KB-081) | >1000 every print since 7/27; FT-07 banked, now 249bp over | **35/65 bear** (40/60) |
| **Regional banks** | KRE **69.44** · WAL **75.10** · OZK **45.96** [9/30] | 74.87 / 81.00 / 50.17 [9/3]: **−7.3% / −7.3% / −8.4%** | cohort earnings benign on 7 surfaces; this is a rates move, not credit | a ~50bp real-rate shock hits bank securities books and CRE refi math directly; EGBN Q3 (~10/21) is CHG-027's deciding print | **55/45 bull** (70/30) |
| **Brent — paper vs physical** | front **102.46** (BZ=F 10/1 intraday) · Dated **113.96** [9/29], 119.97 [9/28] | paper 96.28 [9/4] | paper −8% off its peak; WL-11 (<95) did not fire | **an $11–17 physical premium over paper**: prompt tightness the futures curve is not carrying (CHG-042's paper/physical split, still live) | **40/60 bear** (50/50) |
| **OVX** | **52.24** [9/30] | 44.96 [9/4] | — | the first sub-45 print **reversed**; VX-RED-025's 3-leg flip is now 0-of-3 on OVX | **40/60 bear** (50/50) |
| **Core CPI 3-mo ann.** | **2.02** Table A / 1.97 index [Aug] | 1.61 [Jul] | still at/below target | **rising on base effects: a 0.3 Sept print fires FT-08 (P ≈ 25–35%)** | **65/35 bull** (75/25) |
| **5y5y breakeven** | **2.36** [10/01] | 2.33 [9/4] | anchored through the rate move, so the 30Y move is NOT inflation fear | a market price; anchors break late | **70/30 bull** (=) |
| **VIX** | **16.34** [9/30] | 14.53 [9/4] | sub-17; FT-06 banked | drifting up while the long end sells off, so equities are not pricing the rate shock (or are pricing it slowly) | **65/35 bull** (70/30) |
| **^SKEW (CBOE)** | **141.92** [9/30] | 154.49 [9/11] | FT-10 run broke 9/15; 8 below the line | >140 is still the modal state | **60/40 bull** (50/50) |
| **Initial claims** | **197K** [w/e 9/26] | — | FT-05 (>250) 53 away; layoffs not moving | low-fire/low-hire (LABOR): the margin is hiring, not firing | **75/25 bull** (new row) |
| **NFP / CPS** | Aug +162K · U-3 4.1 · LFPR 61.6 · AHE $37.75 [Aug, 1st/2nd print] | = | 3-mo +71K (first-print vintage), supply absorbed | added-worker read unheld; real wages falling | **65/35 bull — CARRIED, re-weight after Fri 10/2 08:30** |
| **USD/JPY** | **158.05** (10/1 intraday) | 156.22 [9/4] | SAM flat | WL-07 (>160) 1.95 away | **50/50** (=) |
| **Euro sovereigns** 🆕 | France 5y CDS at a 13-yr wide; IT/ES widened, Bunds rallied [10/01, WALTER SIG-W-20261001-009/-011] | — | one day, and a flight to quality *into* Bunds | a second sovereign-risk venue opening while US real rates spike | **50/50, WEAK (one day, secondary source)** |

## Balance, restated (not carried)
**The 9/6 table said the bear's structural pile was two rows. On 10/01 it is wider and heavier.** The **price of money** (real 10Y +51bp) is the strongest row on the board. **Credit has turned from bull to coin-flip** (HY +47bp, CCC +103bp). **Physical oil** carries a premium paper does not. **Banks gave back 7–8%.** The bull still owns **inflation expectations** (5y5y flat), **equity vol** (VIX/SKEW), and **layoffs** (claims 197K), and until tomorrow, payrolls.
⚠️ **Independence check (count once):** the real-rate row, the bank row and part of the HY row share ONE antecedent, the 9/22→9/30 long-end sell-off. That is roughly one event in three views, not three confirmations. The oil rows (paper/physical, OVX) are a separate antecedent.

## What this does NOT do
- **No hypothesis weight moves in this file.** The re-derivation runs after Fri 10/2 08:30 ET NFP, so the labour-sensitive weights (Soft Landing's growth leg, the S41 Stag −2) are set once on current data. **Deadline unchanged: 10/09**, before 10/14 CPI.
- No trigger fired. FT-02 is 8bp away.
