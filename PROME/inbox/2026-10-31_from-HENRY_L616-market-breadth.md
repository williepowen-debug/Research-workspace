# L616 — US equity market breadth through Friday October 30 (HENRY → PROME)

**From:** HENRY · **To:** PROME (session prome-34) · **Written:** 2026-10-31 13:25 EDT · **Commission:** C9 research commission (WQ-538 class; receipt WQ-567), DOCKET L616, Will's request of 2026-10-07 (*"One thing I want us to investigate at some point is the breadth of the market"*) · **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`); session id not exposed · **Data:** Friday 10/30 closes (markets shut Saturday) · **Desk commit:** `1704c924b`.

## The answer

**Broad or concentrated? Concentrated at the start of October; broad and broadening by its end.** The S&P 500's record close on 10/6 (7,818.93) had only 29.5% of its members above their 50-day average and 46.6% above their 200-day: the lowest of any of 2026's 28 record closes on both counts (the previous record, 8/13, had 68.7% and 73.6%). Since then the index has fallen 3.05% while the typical stock rose. Over October (9/30 to 10/30) the median S&P 500 member returned **+7.20%** while SPY returned **−0.91%**; the equal-weight fund RSP beat SPY by **5.91 points**, a 99.5th-percentile month since 2003; 9 of 11 sector funds rose (only tech and communication services fell); members above their 50-day average went from 20.9% to 60.2%. The concentration that remains is among the losers: chips, AI hardware and the mega-caps.

**Improving or deteriorating? Improving over one week and one month; the three-month damage is only partly repaired.** Members above the 200-day average are 59.2% (73.6% on 8/13, 40.4% on 9/30). The S&P 500 advance-decline line has recovered about two-thirds of its August–September fall but not its 8/14 peak. Small and mid caps are still down over three months (IJR −3.21%, MDY −2.31%, IWM −3.83% against SPY +1.41%), and only about half their members are above the 200-day average, down from about three-quarters on 8/13.

**Friday 10/30: a narrow break, not broad deterioration.** Twenty-six tickers (the Magnificent Seven, both Alphabet classes, plus 18 other chip makers) produced **79%** of the S&P 500's −1.82%. Only **55%** of S&P 500 members fell: on the 32 days since January 2025 when SPY lost at least 1.3%, the median share was 76% and only three days were narrower. RSP beat SPY by 1.00 point, a margin bettered on only 4 of 321 days of similar size since May 2003, and all four were chip-led selloffs like this one (SOXX −5.3% to −7.9% each). **42** S&P 500 members set 52-week highs and **5** set 52-week lows. Two qualifications: inside tech the selling was broad (80% of the 75 S&P 500 tech members fell, median −4.34%; QQEW −3.26% vs QQQ −3.47%, an ordinary breadth reading for a Nasdaq down day of that size); and beneath the index there was a mild risk-off tilt (industrials, consumer discretionary, health care and small caps mostly fell, 69% of S&P 600 members down; staples, energy, utilities and materials rose).

**So what:** since 10/6 the market has been repricing the AI, chip and mega-cap group while most stocks rallied, the opposite of a broad retreat. Both verdicts were tested (§ 2); the evidence that would turn this into broad deterioration (§ 3) was not present on Friday. This is an equity-only read: credit's one lead is the high-yield spread, +12bp to 326bp on 10/29 [FRED], a session before the break.

## 1. Figures

**Bases and sources (apply to every figure unless the row says otherwise).** Membership: State Street (SSGA) daily holdings files "As of 29-Oct-2026": S&P 500 = 503 members (SPY file), S&P 400 = 400 (MDY), S&P 600 = 603 (SPSM), S&P 1500 = 1,506; GICS sector for S&P 500 members from the 11 Select Sector SPDR files of the same date. Prices: yfinance daily bars, pulled 2026-10-31 13:07–13:10 ET. Returns are total returns on dividend-adjusted closes; "price" marks a price-only figure. Friday ETF closes cross-checked with `FORGE/tools/market-data/fetch.py` (10/31 ~13:0x ET): SPY $755.72 −1.77% · RSP $218.31 −0.79% · QQQ $690.49 −3.47% · QQEW $151.32 −3.26% · IWM $279.33 −1.65% · MDY $668.88 −1.18% · IJR $140.29 −1.21% · SOXX $471.51 −8.24% · S&P 500 7,580.07 −1.82%.

### 1a. ETF proxies — relative return in percentage points (ratio basis: (A/B) at 10/30 ÷ (A/B) at the reference − 1)

| Pair (what it measures) | 1 day (ref 10/29) | 1 week (10/23) | October (9/30) | 3 months (7/31) | YTD (12/31/25) | 12 months (10/30/25) |
|---|---:|---:|---:|---:|---:|---:|
| RSP/SPY — S&P 500 equal vs cap weight | +1.00 | +1.38 | **+5.91** | +0.50 | +3.26 | +5.27 |
| QQEW/QQQ — Nasdaq-100 equal vs cap weight | +0.22 | −0.25 | −0.38 | −3.03 | −5.59 | −4.61 |
| OEF/SPY — S&P 100 mega vs S&P 500 | −0.23 | −0.49 | −1.39 | −0.04 | −1.86 | −2.56 |
| MDY/SPY — S&P 400 mid vs S&P 500 | +0.61 | +1.89 | +2.78 | −3.67 | 0.00 | +2.11 |
| IJR/SPY — S&P 600 small vs S&P 500 | +0.57 | +2.07 | +4.07 | −4.56 | +5.38 | +7.54 |
| IWM/SPY — Russell 2000 vs S&P 500 | +0.13 | +1.87 | +1.44 | −5.17 | +2.29 | +2.56 |
| SOXX/SPY — semiconductors vs S&P 500 | −6.59 | −0.84 | −16.32 | −7.85 | +40.43 | +37.84 |
| *SPY absolute* | −1.77 | −0.56 | −0.91 | +1.41 | +11.69 | +12.36 |
| *RSP absolute* | −0.79 | +0.82 | +4.95 | +1.92 | +15.33 | +18.28 |

- **Sector SPDRs rising (of 11):** 1 day 6 · 1 week 9 · October 9 (only XLK −8.30% and XLC −9.98% fell) · 3 months 5 · YTD 9 · 12 months 8.
- **Rarity of October:** +5.91pp is the 99.5th percentile of 5,892 22-session windows since May 2003. Larger distinct episodes: 2009-05 (+9.38), 2020-06 (+8.32), 2021-03 (+6.00), 2024-08 (+6.75).
- **VULCAN reconciliation (one number per metric):** VULCAN's S1 breadth leg (RSP/SPY 63-session, `mag7.py` basis) reproduces exactly at 10/29: −0.50pp, 39.1 percentile. On the same method 10/30 reads **+0.94pp** (67.7 percentile); 10/1 was −5.07pp (3.7 percentile); the 2026 low was −8.22pp on 5/15. RSP/SPY ratio 52-week low 0.27097 on 10/7; 10/30 0.28888. Mag-7 = 33.2351% of SPY fund weight [VULCAN, holdings 10/29; highest in its series 34.7494%, holdings 10/8]: cited, not recomputed.

### 1b. Constituent breadth — computed directly from each member's own closes (share of members, %)

| Date (S&P 500 close) | S&P 500 above 50-day | S&P 500 above 200-day | S&P 400 above 200-day | S&P 600 above 200-day | S&P 1500 above 50-day | S&P 1500 above 200-day |
|---|---:|---:|---:|---:|---:|---:|
| 7/31 (7,489.72) | 62.4 | 66.7 | 70.7 | 72.0 | 62.2 | 69.9 |
| 8/13 record (7,798.99) | 68.7 | **73.6** | 72.2 | 74.7 | 64.0 | 73.7 |
| 9/30 (7,651.54) | **20.9** | **40.4** | 35.0 | 46.2 | 19.0 | 41.3 |
| 10/6 record (7,818.93) | 29.5 | 46.6 | 42.5 | 48.7 | 27.7 | 46.3 |
| 10/23 (7,623.68) | 58.0 | 55.8 | 46.0 | 48.8 | 49.9 | 50.4 |
| 10/29 (7,720.39) | 64.9 | 63.6 | 51.5 | 54.0 | 59.7 | 56.5 |
| 10/30 (7,580.07) | 60.2 | 59.2 | 49.8 | 51.8 | 55.1 | 53.7 |

Denominators at 10/30 (a full 50- or 200-session window is required): S&P 500 502 / 500, S&P 400 400 / 400, S&P 600 602 / 598, S&P 1500 1,504 / 1,498. 2026 range for the S&P 500: above 50-day 19.4% (3/30) to 72.8% (1/15); above 200-day 40.4% (9/30) to 73.6% (8/13).

- **Advance-decline line** (cumulative adv − dec, S&P 500 members, based 2025-01-02; only differences are meaningful): peak 8,160 on 8/14 → 5,946 on 9/30 → 6,434 at the 10/6 record → **7,393** on 10/30 (65% of the fall recovered; peak not regained). S&P 1500: 15,890 (8/14) → 9,058 (9/30) → 12,062 (10/30).
- **New 52-week highs / lows** (intraday basis, S&P 1500, daily counts summed by week, so a name counts each day it qualifies): week to 10/2 **72 / 410** · 10/9 124 / 234 · 10/16 205 / 177 · 10/23 289 / 160 · 10/30 **282 / 112**. Friday alone, S&P 500: 42 highs (health care 11, financials 8, energy 6, industrials 6, staples 4, tech 3, utilities 2, materials 1, discretionary 1) / 5 lows (RDDT, APP, COIN, TTWO, CHRW).

### 1c. S&P 500 participation by horizon (member total returns; cap weight = SPY shares held × price at the reference date)

| Horizon | SPY | Cap-weighted members | Equal-weighted | Median member | Members up | Mag-7 contribution | 18 other chip makers | All other members |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 day | −1.77% | −1.81% | −0.83% | −0.29% | 45.3% | −0.68pp | −0.76pp | −0.38pp |
| 1 week | −0.56% | −0.56% | +0.85% | +1.33% | 64.2% | −1.06pp | −0.09pp | +0.60pp |
| October | −0.91% | −0.88% | +5.12% | **+7.20%** | **72.1%** | −1.84pp | −1.67pp | **+2.64pp** |
| 3 months | +1.41% | +1.56% | +2.13% | +1.00% | 53.0% | +0.48pp | −0.68pp | +1.75pp |
| YTD | +11.69% | +12.73% | +16.61% | +10.73% | 68.2% | +2.29pp | +3.10pp | +7.35pp |

The chip set is the 19 S&P 500 members Yahoo labels "Semiconductors" or "Semiconductor Equipment & Materials" (NVDA sits in the Mag-7 column). Cap-weighted members track SPY within 0.04pp (1 day) and 0.15pp (3 months); about 1pp at YTD, so YTD contributions are approximate.

### 1d. Friday 10/30 decomposition (price returns)

| Universe | Members down (share of advancers + decliners) | Median member | Equal-weighted | Comparable-day norm: median share down on SPY ≤ −1.3% days, 1/2025–10/29 (n = 32) | Friday's rank, narrowest first |
|---|---:|---:|---:|---:|---:|
| S&P 500 | 277 of 503 (**55.1%**) | −0.32% | −0.85% | 75.8% | 4th of 33 |
| S&P 400 | 239 of 400 (59.8%) | −0.51% | −0.91% | 81.8% | 3rd of 33 |
| S&P 600 | 412 of 598 that moved (68.9%) | −0.85% | −1.20% | 82.2% | 9th of 33 |
| S&P 1500 | 928 of 1,501 that moved (61.8%) | −0.60% | −1.01% | 79.3% | 6th of 33 |

- **Index arithmetic (S&P 500, cap weights at 10/29):** reconstructed −1.818% vs actual −1.82%. Mag-7 −0.676pp + 18 other chip makers −0.757pp = −1.433pp (**79%**); the other 476 members −0.384pp (52.8% of them down, median −0.16%). By sector: information technology −1.63pp (80% of 75 members down, median −4.34%); industrials −0.13pp (66% down); communication services −0.09pp; financials −0.09pp; discretionary −0.08pp; staples +0.07pp, energy +0.07pp, health care +0.04pp (Eli Lilly), utilities +0.01pp.
- **Largest drags:** NVDA −0.33pp, INTC −0.20pp (−28.58%), AMD −0.15pp, AVGO −0.14pp, AAPL −0.09pp, MSFT −0.09pp, MU −0.08pp. Outside the 26 tickers the heaviest fallers were AI hardware and earnings reactions: RDDT −29.2%, ILMN −18.6%, TWLO −15.2%, SNDK −13.5%, DDOG −11.5%, COHR −11.3%, DELL −10.8%, COIN −10.6%, APP −10.4% (22 of the 37 "other" members down more than 5% were tech).
- **RSP−SPY base rate:** on the 321 days since May 2003 with SPY between −2.3% and −1.3%, the median RSP−SPY gap was −0.03pp; Friday's +1.00pp ranks 5th (98.8 percentile). The four larger: 2025-01-27 (+1.50), 2026-06-23 (+1.13), 2024-07-24 (+1.12), 2024-07-17 (+1.01); SOXX fell 7.84%, 7.88%, 5.32% and 7.11% on those days.
- **Inside the Nasdaq-100:** QQEW−QQQ +0.22pp on Friday vs a median +0.25pp on the 198 days since 2006 when QQQ fell at least 2.5% (48.5 percentile): an ordinary-breadth Nasdaq-100 down day.

## 2. Both verdicts tested

| Verdict | Evidence for it | Evidence against it |
|---|---|---|
| **Concentrated / deteriorating** | 10/6 record on 29.5% of members above the 50-day (lowest of 28 record closes); RSP/SPY ratio 52-week low on 10/7; Mag-7 33.2351% of SPY [VULCAN, 10/29]; 3 months: IWM/SPY −5.17pp, IJR/SPY −4.56pp, MDY/SPY −3.67pp; above-200-day 59.2% vs 73.6% (8/13) and S&P 400/600 ~50% vs ~73%; A/D line below its 8/14 peak; Nasdaq-100 equal weight behind cap weight YTD (−5.59pp); YTD median member +10.73% below cap-weighted members +12.73% | October RSP/SPY +5.91pp (99.5 pctile); October median member +7.20% vs SPY −0.91%, 72.1% of members up; above-50-day 20.9% → 60.2%; S&P 1500 weekly highs above lows three weeks running; Friday 55.1% down vs a 75.8% norm; 42 highs vs 5 lows on a −1.82% day |
| **Broad / improving** | The right-hand column above; plus YTD RSP/SPY +3.26pp and 12 months +5.27pp, YTD equal-weighted members +16.61% vs cap-weighted +12.73%, "all other members" contributed +7.35pp of +12.73pp YTD | The left-hand column above; plus S&P 1500 still 112 new-low name-days in the week to 10/30; Friday's small-cap decline broader (68.9%) than large-cap (55.1%) |

**Weighing by horizon:** 1 week and October are clearly broad and improving; 3 months is mixed (large caps fine, small and mid caps damaged); YTD and 12 months are broad for the S&P 500 (equal weight ahead) and concentrated for the Nasdaq-100 (equal weight behind). The structural index-weight concentration (Mag-7 at a third of SPY) is VULCAN's S1 measure and is unchanged by this study.

## 3. What would change the read

*Descriptive comparison points from this study only — not registered thresholds, monitors or gates; nothing here is armed.*

- **Toward broad deterioration:** (a) down days on which the share of falling members returns to the comparable-day norm (~76% for the S&P 500, ~82% for the S&P 600) instead of Friday's 55% / 69%; (b) S&P 1500 weekly new lows overtaking new highs again, as in the week to 10/2 (410 vs 72); (c) equal weight no longer cushioning down days (RSP failing to beat SPY when SPY falls); (d) members above the 200-day sliding back toward the 9/30 low (40.4%); (e) credit confirming. The high-yield spread widened a session before the break (326bp, 10/29); by my credit-leads-equities rule a broad-deterioration verdict needs credit with it.
- **Toward re-concentration:** an index rebound led by chips and mega-caps while RSP/SPY turns down: the mid-August-to-10/6 pattern that produced the narrow record.
- **Toward confirmed broad strength:** the S&P 500 A/D line above its 8/14 peak (8,160 on this construction; 7,393 on 10/30) and members above the 200-day back near August's 73.6% (59.2% now).

## 4. Data limits

- **Exchange-wide series not reached.** NYSE/Nasdaq advance-decline and new-high/new-low tallies for 10/30: two free web searches found no 10/30 market wrap; Barchart's page returned empty to the fetcher; Yahoo carries no such series. The constituent counts above are computed directly and are **not** the exchange series.
- **"% above 50/200-day" is not validated** against a published series (none reachable free). The price panel underneath is: reconstructed cap-weighted S&P 500 −1.818% vs actual −1.82% on Friday; equal-weighted members track RSP (−0.85% vs −0.79% Friday; +5.12% vs +4.95% October).
- **Survivorship.** Today's (10/29) members are applied back to 2024–25: names added for strength are in, names removed for weakness are out, so historical breadth and the comparable-day norms read slightly strong. Size not measured.
- **Cap weights** are SPY shares held on 10/29 × price with constant shares: good to 0.04pp at 1 day and 0.15pp at 3 months, about 1pp at YTD and 12 months.
- **Classification.** Sectors are GICS via Select Sector SPDR membership. Chips are Yahoo industry labels (19 names): FSLR, which GICS counts as a semiconductor, is labelled Solar and excluded; storage, networking and optical AI hardware (SNDK, COHR, DELL, ANET, LITE, NTAP, HPQ) sit in "other", so 79% understates the AI group's share of Friday.
- **Nasdaq-100 and Russell 2000 member lists were not obtained** (Invesco returned HTTP 406; iShares served a web page): those two are ETF proxies only (QQEW/QQQ, IWM).
- **New highs/lows** use an intraday 52-week definition with 252 sessions of history required (recent listings excluded). This is my definition, not an exchange's.
- **Friday confounds not instrumented:** month-end rebalancing, the 10/30 options expiry, and a tech earnings cluster (INTC, RDDT, TWLO, DDOG, ILMN).
- **Vendor:** yfinance free daily bars, not exchange-certified. 19 S&P 400/600 names timed out on the first pull and were recovered on retry; 0 missing.
- **Checked before shipping:** "narrowest record close on every measure" was false (10/6 is lowest on members above the 50- and 200-day, 2nd on the RSP/SPY ratio, 12th of 28 on new highs minus new lows), so the claim above is limited to the two averages. Script: `verify_claims.py`.

## 5. Book implication — one line for TERRY (no trade view)

Breadth locates Friday's and October's damage in the Nasdaq-100 / AI-hardware group that QQQ tracks, while the broad market, regional banks included (KRE +3.70% in October vs SPY −0.91%, though −4.79% over three months; total return, yfinance 10/31), joined October's broadening, so as of 10/30 breadth offers no broad-deterioration support to either the QQQ or the KRE puts (positions per the `FORGE/STATUS.md` mirror, reconcile 10/30); TERRY's call whether that matters for either line.

## 6. Files and desk receipts

- **Research folder** `AGENTS/HENRY/research/2026-10-31_L616_breadth/` (commit `1704c924b`): `NOTES.md` (method, definitions, re-run order) · scripts `build_universe.py`, `pull_prices.py`, `retry_failed.py`, `semis_set.py`, `breadth_compute.py`, `breadth_extra.py`, `verify_claims.py` · data `universe.csv`, `semis.json`, `breadth_daily.csv` (daily breadth by universe, 2025-01-02 to 2026-10-30), `stock_snapshot.csv` (1,506 members at 10/30), `results.json` · outputs `report.txt`, `report_extra.txt`, `verify_claims.txt` · `downloads/` (14 SSGA holdings files, as of 29-Oct-2026). The price cache is not committed (size); `pull_prices.py` rebuilds it.
- **Desk write-back (same commit):** STATUS § MARKET BREADTH (new) and VIEW line; KB ML-HEN-194; MEMORY, LAST_COMPLETION, NEXUS_BRIEF (folded last).
- **WALTER lane:** SIG-W-20261031-001 acted (Russian diesel ban through 2027-01-31 now in STATUS), -002 noted, -006 noted; logged in `board_log.tsv` and moved to `processed/`. Corrections: COR-20261031-01 APPLIED, COR-20261031-02 NO-OP; `corrections_boot_check.py HENRY` now rc 0.
- **Not done (scope):** Monday's L888 gamma re-pull is separate; TERRY's L590 expression comparison was not repeated; no recurring breadth monitor was created.

## COMPLETION — HENRY — 2026-10-31
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/research/2026-10-31_L616_breadth/ (new, 32 files), AGENTS/HENRY/{STATUS.md, MEMORY.md, LAST_COMPLETION.md, NEXUS_BRIEF.md, workbook/KB.tsv, board_log.tsv, registry/corrections_receipts.tsv}, 3 WALTER cards → inbox/WALTER/processed/, PROME/inbox/2026-10-31_from-HENRY_L616-market-breadth.md
RESULT: Concentrated at the 10/6 record (29.5% of S&P 500 members above the 50-day, lowest of 2026's 28 record closes), broadening since: October RSP/SPY +5.91pp (99.5 pctile since 2003), median member +7.20% vs SPY −0.91%. Friday narrow: 55.1% of members down vs a 75.8% comparable-day norm, Mag-7 + 18 chip makers = 79% of −1.82%, 42 new highs vs 5 lows; broad only inside tech. Small/mid three-month damage only partly repaired (IWM/SPY −5.17pp; S&P 400/600 ~50% above the 200-day vs ~73% on 8/13).
GAPS: Exchange-wide NYSE/Nasdaq A/D and highs/lows not reachable free (S&P 1500 members counted directly instead); survivorship unmeasured; %-above-average not validated against a published series (none free); Nasdaq-100/Russell 2000 member lists not downloadable (Invesco 406, iShares HTML), so ETF proxies only.
WILL_NEEDS: None.
FOLLOW-UP: PROME consumes and closes L616; § 5 carries the one-line book note for TERRY (no trade view). No monitor created; the Monday L888 gamma re-pull is separate.
