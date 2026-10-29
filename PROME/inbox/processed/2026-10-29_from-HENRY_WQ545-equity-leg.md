# HENRY → PROME: WQ-545 equity leg — the energy cluster did not reach equity vol

**Written 2026-10-29 16:4x ET.** Claude Code, Opus 5.5. Commission: prome-5c 15:34 ET (Will "ok go", WQ-545), corrections at 15:37 ET (TTF is €, settle not established; VLO cause) and 16:00 ET (AAPL 11/02). This is a read only: no trade construction, no threshold or band change. All closes are vendor (yfinance) daily bars pulled 16:06 ET 10/29, with the file at `AGENTS/HENRY/research/2026-10-29_catchup/closes_1021_1029.txt`, unless another source is named.

**Answer, equity side:** in equities I see **no single shock transmitting**. Equity vol fell on every session of the cluster (VIX 18.39 → 17.52 → 16.91 → 16.50, 10/26–10/29), and the broad tape rose (SPX +0.60%, +0.28%, −0.30%). The only equity footprint of energy was a **refiner selloff with airlines rallying**. That is the signature of *falling* diesel and margins, the opposite sign to an energy-cost shock. Oil volatility moved on its own: OVX +5.68% on 10/28 while VIX fell 3.48%. Credit agrees with the equity read (HY 330 → 318 → 314bp, FRED 10/26–10/28).

## (1) Equity transmission, 10/27–10/29

| Close (vendor) | 10/26 | 10/27 | 10/28 | 10/29 | Read |
|---|---:|---:|---:|---:|---|
| SPX | 7,676.77 | 7,722.60 (+0.60%) | 7,743.98 (+0.28%) | 7,720.39 (−0.30%) | no energy-led move; 10/29 drop was GOOGL −12.64% / AMZN −4.25% |
| VIX / OVX | 18.39 / 58.71 | 17.52 / 55.44 | 16.91 / **58.59 (+5.68%)** | 16.50 / 56.63 | OVX up alone on 10/28 |
| XLE (energy) | 69.64 | 68.21 (−2.05%) | 68.45 (+0.35%) | 68.71 (+0.38%) | flat-to-down |
| VLO / MPC / PSX | 426.76 / 470.64 / 288.85 | **387.34 (−9.24%) / 435.98 (−7.36%) / 268.53 (−7.03%)** | 388.48 / 440.77 / 273.76 | 384.77 / — / — | refiners down hard 10/27 |
| JETS (airlines, diesel/jet "losers") | 26.43 | 27.02 (+2.23%) | 26.97 (−0.19%) | 27.49 (+1.93%) | rallied: fuel-cost relief, not pain |
| XLU (utilities, PJM channel) | 42.55 | 42.85 (+0.71%) | 42.49 (−0.84%) | 43.15 (+1.55%) | no power-shock footprint |
| HO=F diesel (front, $/gal, futures bar) | 4.91 | 4.78 (−2.79%) | 4.82 | 4.59 (−4.58%, bar after 14:30 ET, not a settle) | diesel falling |

⚠️ The gas leg is "TTF **traded above €100/MWh** intraday 10/28". No official ICE Endex settle above 100 is established (HANS addendum). The PJM spike lasted 15 minutes (WATT). Neither has a US-equity line I can find.

## (2) Put-wall grade and the next session

- **Grade:** the 7,700 put wall was clean at both horizons (gamma `--both`, 16:06 ET). SPX low 7,690.94, close **7,720.39** ⇒ **TESTED, HELD on the close**, 20 points over the wall.
- **Regime:** dealer gamma **NEGATIVE at both horizons**: 14d flip ~7,739 (−$19.4B per 1%), 35d flip ~7,741 (−$25.7B). Spot is 19–21 points under the flip. Free-tier proxy: the sign and flip are robust, the $B amounts are not.
- **What it implies into AMZN tonight (AAPL is 11/02 per the vendor calendar, Apple IR not read, so tonight is AMZN only):** below the flip, dealer hedging adds to the move in either direction, so the cushion that held SPX near 7,740 last week is gone.
  - VIX 16.50 implies a one-day 1-standard-deviation move of about **±1.04% ≈ ±80 points** (7,640–7,800). That is arithmetic, not a forecast, and negative gamma argues realized moves can exceed it.
  - The AMZN 10/30 straddle prices 7.92% (VIOLET).
  - **Levels to watch:** 7,700 (put wall; a close under it intensifies downside feedback) and 7,739–7,741 (the flip; a close back over it restores the cushion).
- Vol is not pricing stress: VIX9D 14.65 < VIX 16.50 < VIX3M 18.96 (contango steeper).

## (3) QQQ Nov-20 690/670 put spread — distance only, a read not a recommendation

| Strike | Distance from QQQ close $715.34 (10/29) | Rough SPX equivalent (60-session beta ~1.55, own calc) |
|---|---:|---:|
| 690 | −3.54% | ~7,544 |
| 670 | −6.34% | ~7,405 |

**Dealer picture on the path to 690:** reaching 690 needs SPX through the 7,700 put wall and the 50-day average (7,698.3). Both sit within about 25 points of the close, and both lie inside a negative-gamma regime. That is the mechanism by which a move can extend. But the 10/23 break of the 7,650 wall reversed within three sessions, and credit and vol are not confirming stress. ⚠️ HENRY has no QQQ-chain gamma read: these are SPX dealer levels mapped by beta, and the beta is unstable around a single-name shock like GOOGL. TERRY owns the card.

## (4) Energy lines — equity-tape reads only (BRENT owns the crack, TERRY the card)

- **USO:** $168.09 close on 10/29 (+0.91%). That is $5.09 over 163 and $3.09 over 165; 170 is 1.1% above. Brent's front-month futures bar fell 3.25% the same day.
- **VLO (3 shares):** $384.77 close on 10/29, −9.8% from $426.76 on 10/26.
  - **The 10/27 −9.24% was sector-wide, not Valero-specific:** MPC fell 7.36% and PSX 7.03% the same day.
  - It **gapped at the open**: the first 30-minute bar closed at $405.11, already −5.1%, then the stock ground down to $387.34. Diesel futures fell 2.79%.
  - **It was not earnings.** Valero reported 10/22 pre-market and is not ex-dividend until 11/23.
  - **Cause NOT established at a primary.** Secondary reports (24/7 Wall St., Benzinga, Trefis, Yahoo/TIKR, 10/28) attribute it to the refining-margin outlook, more Russian diesel heading to the US (OFAC General License 135, 10/9; an Energy Secretary statement reported 10/28) and easing US–Iran tension. MPC issued no filing.
  - Follow-through: 10/28 +0.29%, 10/29 −0.96%. No rebound.

**WILL_NEEDS:** none from HENRY. **ASK:** none.
