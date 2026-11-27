# D:L1113 backstop, 2026-11-27: MIDAS-11 HIT, MIDAS-17 MISS on the issuer row; 11/19 and 11/20 are LIQUIDATION days; the WQ-451 three-month trust line was crossed on 11/20

**Written:** 2026-11-27 13:0x ET (Fri), MIDAS (Claude Code, Opus 5.5), PROME prome-80 wake for DOCKET L1113. **Bundle:** `gold/sources/2026-11-27_backstop/` (probe.py + probe_access.json, capture.py + capture_access.json, grade.py + grade_output.txt, GLD_issuer_archive.xlsx, treasury_real.csv, treasury_nominal.csv, fetch_history.json, wq451_applied.csv). Frozen letters: `workbook/PREDICTIONS.tsv` MIDAS-11, MIDAS-17; `gold/research/2026-10-23_WQ451-decomposition-letter.md` (classifier parameters copied, not re-fit).

## 1. How the issuer row was obtained

| Date | Client | Result |
|---|---|---|
| 2026-11-23 17:07 UTC | Python urllib, default client string | HTTP 403, stopped, not retried |
| 2026-11-27 18:01 UTC | Python urllib, `User-Agent: research-bot/1.0` (the honest name Will approved under WQ-735 on 11/23) | **HTTP 200**, 544,904 B, sha256 `4e04cec2…28279`, one request |

PROME's task letter allowed one plain honest-client request, with a refusal as the stop. The request succeeded. No browser identity was used. Will's optional hand-download (WILL_QUEUE row 734) was not needed: no file was in `gold/sources/2026-11-23_1120_grade/` (the only place MIDAS named) at 13:00 ET. ⚠️ The 11/23 refusal may have been aimed at the default Python client string; that is an inference from one success, not a tested cause.

## 2. The two formal grades

| Row | Letter | Inputs | Result |
|---|---|---|---|
| **MIDAS-11** | issuer GLD 11/20 close ≤ $379.69 = NONPOSITIVE = HIT; STUCK only if the close is unavailable by 11/27 or a structural basis change | issuer close **$322.87** (11/20); issuer 10/19 close in the same file $379.69 = the frozen baseline; ounces per share 0.09165907 → 0.09162304, fee accrual only | **HIT** (−$56.82, −14.96%). Qualitative call, no probability |
| **MIDAS-17** | residual = 100×(GLD/369.00 − 1) − (−0.1526 × 100 × (real10Y − 2.64)) > 0 = HIT | issuer $322.87; issuer 10/22 $369.00 = baseline; PRIMARY Treasury real 10Y 11/20 **2.77** as first published (11/23 capture; unchanged in today's) | GLD −12.50%, rate-implied −1.98%, **residual −10.52 → MISS**. P(HIT) was 0.55; Brier 0.3025 |

Both graded inside the 11/27 backstop on the first resolving capture, so neither is STUCK or NOT-RESOLVED, and the late-grade question does not arise. For the record: after 11/27 neither letter allows a grade (MIDAS-11 goes STUCK, MIDAS-17 NOT-RESOLVED, and both forbid a fallback source or a later regrade). The MIRROR close (FORGE fetch.py) equalled the issuer close to the cent on all 6 sessions 11/18–11/25, as on the 19 before.

**MIDAS-17's if-falsified action:** gold kept lagging its rate support for the month, so the flows and liquidation story outweighed rates. M1 reads lean less on the rate beta from now (residuals 11/18–11/24: −3.36, −1.76, −5.35, +3.45, −2.27%). Reported to PROME and TERRY today.

## 3. WQ-451 classes with the issuer tonnes (11/18–11/25)

| Date | GLD | Tonnes (Δ) | Real 10Y (Δ bp) | Residual e | S&P | ΔVIX | Stress | Class |
|---|---:|---|---|---:|---:|---:|---|---|
| 11/18 | 341.19 (−3.20%) | 1,044.12 (−4.56) | 2.88 (−1) | −3.36 | −0.23% | −0.90 | no | UNEXPLAINED-DOWN (unchanged) |
| 11/19 | 335.18 (−1.76%) | 1,038.14 (−5.98) | 2.88 (0) | −1.76 | −2.02% | +3.88 | yes | **LIQUIDATION** (was candidate) |
| 11/20 | 322.87 (−3.67%) | 1,034.43 (−3.71) | 2.77 (−11) | −5.35 | −3.70% | +7.45 | yes | **LIQUIDATION** (was candidate) |
| 11/23 | 333.02 (+3.14%) | 1,031.30 (−3.13) | 2.79 (+2) | +3.45 | +4.73% | −9.27 | no | UNEXPLAINED-UP |
| 11/24 | 325.45 (−2.27%) | 1,027.31 (−3.99) | 2.79 (0) | −2.27 | −0.50% | −0.26 | no | UNEXPLAINED-DOWN |
| 11/25 | 327.45 (+0.61%) | 1,027.88 (+0.57) | 2.73 (−6) | −0.30 | −0.25% | +1.93 | no | RATE |

Sources: issuer close and tonnes PRIMARY (SPDR archive 11/27); real 10Y PRIMARY Treasury; S&P, VIX, DXY MIRROR (fetch.py). 11/26 US holiday. Five sessions in a row of trust outflows (11/18–11/24), −21.37 t from 11/17, then +0.57 t on 11/25. The 11/23 rebound came with stocks (+4.73%) and still no inflow.

## 4. What changes in the WQ-451 lines

| Line | Rule (frozen 10/23) | Reading | State |
|---|---|---|---|
| § 5, 3 months, trust | GLD trust < 1,035.70 t: "the accumulation premise has failed" | **1,034.43 t on 11/20**, first issuer row below; 1,027.88 t on 11/25 | **CROSSED 11/20.** By the letter, MIDAS withdraws the positive three-month lean to neutral and reports to PROME and TERRY (done today) |
| § 5, 3 months, real 10Y ≥ 3.00 × 5 | | 0 prints, max 2.92 | not crossed |
| § 5, 3 months, DXY ≥ 105 × 5 | | 0 closes, max 104.32 (11/23) | not crossed |
| § 5, 3 months, 2nd LIQUIDATION by 11/05 and ≤ −20 t since 9/30 | | second and third LIQUIDATION days came 11/19–11/20, after the 11/05 date | not crossed on its date (the trust line carries the event) |
| L2 haven | 6 or more GLD-up days of the next 10 stress days falsifies "not a hedge" | 6 stress days, GLD up 1; 11/23–11/25 were not stress days | decided, falsifier unreachable; formal at day 10 |
| L3 daily proxy | 3+ DE-DOLLAR days before 11/30 and tonnes rising | 2 proxy days; tonnes −17.76 t since 10/22; 11/27 has the dollar up | decided: daily and monthly legs NOT AGREEING; formal on the 11/27 issuer row |

**What this does not change:** MIDAS-12 (the registered three-month sign call to 2027-01-20) resolves on its own letter, untouched. No level, operator, instrument or consequence moved; the withdrawal is the letter's own stated consequence. M1 stays 4, composite 13/20.

## 5. Today (Fri 11/27, half-day session, vendor about 13:04 ET, NOT closes; vs the 11/25 close)

| Instrument | Level | Move |
|---|---:|---:|
| Gold GCG27 (Feb, now the most traded month) | $3,663.0 | +2.76% |
| Gold GCZ26 (Dec, in delivery) | $3,635.0 | +2.81% |
| GLD | $334.26 | +2.08% |
| Silver SIH27 (Mar) | $43.60 | +7.55% |
| Platinum PLF27 (Jan) | $1,304.4 | +4.99% |
| Palladium PAH27 (Mar) | $889.5 | +5.58% |
| Copper HGH27 (Mar) | $5.59/lb | +3.14% |
| Dollar index DXY | 104.03 | +0.35% |
| US 10Y nominal (^TNX) | 4.93% | +8 bp |
| USD/JPY | 159.50 | +0.18% vs 11/26 |
| S&P 500 | 7,297.49 | +1.60% |
| VIX | 24.66 | −3.63 pts |

Gold rose today against a firmer dollar and higher nominal yields, with stocks. On the rate model that is a large positive residual, the opposite of 11/18–11/24, and it is one half-day. Real 10Y for today is not yet published (latest PRIMARY 2.73 on 11/25). A WALTER card (India Infoline 10:33 UTC) put gold +4% to $3,708 earlier in the day, so part of the morning gain had faded by 13:04.

## 6. Forward view

**Expected (two to four weeks, to the 12/09 Fed):** gold stays a risk-asset trade, not a hedge: it rises on days stocks rise and falls with them on stress days, while GLD holders keep trimming. Reason: five straight outflow days (11/18–11/24) that ran through a rebound, one small inflow since, a speculative long already cut to 40.74% of open interest (11/17), and four of the last five residuals off the rate model by more than 1 sd. **Meaningful alternative (about one in three):** the flush is done; outflows stop and the trust adds metal on up-days, which would show as two or more inflow days in the next issuer rows. **What would change my mind:** an equity-stress day with GLD up and tonnes up (a HAVEN day; none since 2026-03-27), or real 10Y at 3.00% for five prints (the rate route down). This is an unscored outlook; it moves no score or gate.
