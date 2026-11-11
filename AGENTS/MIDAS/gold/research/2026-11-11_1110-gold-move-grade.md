# Gold's Tuesday 11/10 fall, graded on MIDAS's own letters

**MIDAS · Wed 2026-11-11, from 09:25 ET · PROME prome-2b catch-up wake on Will's word (09:24 ET).** Research only. No trade, card, gate, band, threshold or score change.
**Bundle:** `gold/sources/2026-11-11_1110_grade/` (`capture.py` raw pulls at 09:3x ET 11/11, `access.json` hashes, `grade.py` → `grade_output.txt`, `wq451_applied.csv`, `bls_cpi_nr0.htm`).
**Instrument:** the frozen WQ-451 classifier (`gold/research/2026-10-23_WQ451-decomposition-letter.md`, commit `a35faa6f8`). Parameters copied, not re-fit: beta −0.1526 %/bp, residual sd 1.402%, stress = S&P ≤ −1.0% OR VIX +2.0 pts or more, DXY line −0.20%.

## Short answer

**Yes, Tuesday's fall was mostly a real-rate move on my instrument.** The 10-year real yield jumped 12 bp (2.66 → 2.78%, Treasury primary), its third one-day rise of 12 bp or more in 2026 (9/23 and 3/20 were +13 bp), and the frozen beta says that alone should take GLD down 1.83%. GLD fell 2.68%. The 0.85% left over is 0.61 of a standard deviation, inside the RATE band. Stocks barely moved (S&P −0.38%, VIX down), so it was not a stress or liquidation day, and the GLD trust lost only 0.29 t. **Class: RATE.** This is the opposite of 10/22, when gold fell while real yields fell (LIQUIDATION); Tuesday it fell because real yields rose, as it has done all year. The 2-year Treasury rose 17 bp (4.56 → 4.73%), which is what a hawkish repricing looks like; on 10/22 the 2-year had fallen 16 bp.

## The day, leg by leg

| Leg | 11/09 → 11/10 | Source |
|---|---|---|
| GLD close | $379.53 → **$369.36 (−2.68%)** | PRIMARY issuer archive |
| GLD trust | 1,042.51 → 1,042.22 t (**−0.29 t**) | PRIMARY issuer archive |
| Real 10Y | 2.66 → **2.78% (+12 bp)** | PRIMARY Treasury real par curve |
| Beta-implied GLD | **−1.83%** (68% of the move) | −0.1526 × 12 |
| Residual e | **−0.85% (−0.61 sd)** | computed |
| Nominal 2Y / 10Y | 4.56 → 4.73 (+17 bp) / 4.88 → 4.98 (+10 bp) | PRIMARY Treasury par curve |
| S&P / ΔVIX | −0.38% / −0.46 → no stress | MIRROR Yahoo |
| DXY | 101.65 → 102.23 (+0.57%) | MIRROR Yahoo |
| GCZ26 Dec 2026 | $4,114.50 → **$4,030.20 (−2.05%)** | MIRROR vendor Close, uncertified |
| Catalyst | October CPI: all items +0.4% SA, **core +0.3%** (as in Sep and Aug), released 8:30 ET 11/10 (USDL-26-1685) | PRIMARY BLS, read 11/11 |

Waller's reported December-hike remarks and futures hike pricing are PROME's relay; I have not read them at source, and BOND owns the rate level. My rate legs come from the Treasury curve, not from that relay.

## The two days before it

| Date | GLD | Real 10Y | Residual | Stress | Tonnes | Class |
|---|---|---|---|---|---|---|
| Fri 11/06 | −0.79% | +3 bp | −0.33% | no | +0.86 | RATE |
| Mon 11/09 | +1.88% | +3 bp | **+2.34% (1.67 sd)** | no (S&P +2.35%) | +1.14 | **DE-DOLLAR proxy** (DXY −0.64%) |
| Tue 11/10 | −2.68% | +12 bp | −0.85% | no | −0.29 | RATE |

Monday's rise ran against a small yield rise and with a weaker dollar and trust additions. That is the second DE-DOLLAR-proxy day since 10/22 (11/04, 11/09).

## Grades on my letters

| Row | Letter | Reading now | State |
|---|---|---|---|
| WQ-451 daily class 11/10 | §2 classifier | e −0.85%, no stress | **RATE** |
| WQ-451 daily class 11/06, 11/09 | §2 classifier | as table above | RATE; DE-DOLLAR proxy |
| WQ-451 L2 (haven) | 10 stress days after 10/22, falsified if GLD up on 6+ | none added 11/06–11/10 | **2 of 10** (10/30 down, 11/05 up), unchanged |
| WQ-451 L3 daily proxy | 3+ proxy days before 11/30 AND tonnes up over the period | 2 days (11/04, 11/09); tonnes −3.42 t since 10/22 | **2 of 3**; legs not yet agreeing |
| WQ-451 §5 one-month lines | GLD < $360.71 or > $391.08 | $369.36 | neither crossed now (down line crossed 10/30 on record) |
| WQ-451 §5 three-month lines | trust < 1,035.70 t; real 10Y ≥ 3.00 ×5; DXY ≥ 105 ×5 | 1,042.22 t; max 2.78; max 102.85 | none crossed; **real 10Y now 22 bp from the 3.00 line** |
| M1 flip rule | certified settle < $4,050 with real 10Y ≥ 2.40 → M1 2 | vendor GCZ26 $4,030.20, real 2.78 | **fired side on the vendor bar, UNRESOLVED** (no certified settle); M1 stays 4 |
| M1 kill-cond #3 | gold up with real yields up, 3 weekly intervals | 10/30→11/06 joint-up True; prior two False | NOT FIRED (1 of 3) |
| MIDAS-13 | any issuer close ≥ $378.95, 10/26–11/20 | **$379.53 on 11/09** | **HIT condition met**; formal resolution at first retrieval 11/23 per the letter |
| MIDAS-11 | GLD 11/20 ≤ $379.69 | $369.36 | on the HIT side today; resolves 11/20 |
| MIDAS-17 | GLD beats real-yield-implied path from 10/22 | running residual +2.23 | on the HIT side today; resolves 11/20 |

MIDAS-13 is a max-over-window letter, so the 11/09 close cannot be undone short of an issuer revision; the row stays OPEN in the ledger until the 11/23 retrieval it names.

## Other metals at the 11/10 close (MIRROR)

| Metal | Named contract 11/10 | Fund 11/10 | d200 band leg | Level |
|---|---|---|---|---|
| Silver | SIZ26 $51.225 (−2.79%) | SLV $46.48 (−3.45%) | −25.99% | 4, unchanged |
| Platinum | PLF27 $1,538.40 (−1.49%) | PPLT $13.94 (−2.11%) | −17.13% | 3, unchanged |
| Palladium | PAZ26 $1,020.80 (−0.07%) | PALL $18.67 (−0.74%) | −25.59% | 4, 0.59 pt below the −25% line |
| Copper | HGZ26 $6.234 (−1.73%) | CPER $37.74 | LME 316,625 t, +35.7% vs median | yellow, I1 1 |

Composite stays **13/20** (4+4+1+4), one shared root. GSR 78.68, benign.

**This morning (11/11, live quotes about 09:30 ET, excluded from every grade):** GCZ26 about $4,038, SIZ26 $52.59, PLF27 $1,560.50, **PAZ26 $1,074.50 (about +5.3%)**. PROME's "about 4,040" for gold matches my vendor. I found no sourced driver for palladium's jump; it is a live quote, not a close.

## What this changes

- **The read:** last session's question was whether gold had stopped behaving like a rate asset (10/22 LIQUIDATION, 10/29–10/30 UNEXPLAINED-DOWN). Since 11/05 three of four days are RATE and one is DE-DOLLAR proxy. **Gold is back to trading on real yields**, and a hawkish inflation print hurts it the ordinary way. That is a regime point, not a forecast.
- **The risk to watch:** real 10Y 2.78% is 22 bp from the WQ-451 3.00% line (five prints at or above it withdraw my positive three-month lean). At the frozen beta another 22 bp is about −3.4% on GLD.
- **No score, band, threshold, forecast, trade or card change.** GLD held 25 sh is Will's; the hedge finding (GLD is not book protection) stands from 10/23 and is already TERRY's. Nothing here is a new tradeable finding beyond it.
