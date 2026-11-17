# LIQUID — evening grade, 2026-11-16 (PROME prome-c4 doorbell, Will's word 20:56 ET)

**Written:** 2026-11-16T20:59:48-05:00 (laptop, Claude Code / Opus 5.5). **Basis:** FRED ICE `output_type=4` (first-published) read 20:58 ET; CFTC TFF raw files via `scripts/cftc_tff_rates.py` 20:59 ET; `scripts/gate069_legs.py` and `scripts/transmission_check.py` 20:59 ET; yfinance raw closes 20:59 ET.

**Bottom line:** No grade changed state. The one new input is the **November 10 ICE cell, now published (HY 330, CCC 1,331)**, absent at 10:09 ET. It extends the prior >320 run to 9 observations and does not touch the November 12 reset or tonight's run (1 of 3, November 13). Gate 076 W1 as-of November 10 is **NOT MET**. Funding is unstressed. The November 16 cell (about 10:10 ET 11/17) is the next input that can move anything.

## 1. ICE cells, first-published (bp)

| Obs | HY | IG | BBB | BB | B | CCC | Note |
|---|---|---|---|---|---|---|---|
| Nov 9 | 334 | 91 | 113 | 200 | 350 | 1,311 | |
| **Nov 10** | **330** | 90 | 112 | 193 | 347 | **1,331** | **NEW since 10:09 ET 11/16**; FRED vintage stamps equal the obs date, so the posting time is unknown |
| Nov 11 | 330 | 90 | 112 | 193 | 347 | 1,330 | unchanged row; Veterans Day, not an observation (D:L342); not re-dated |
| Nov 12 | 320 | 89 | 111 | 183 | 339 | 1,314 | >320 reset (WQ-444) |
| Nov 13 | 323 | 89 | 111 | 186 | 344 | 1,316 | verified: matches the 10:09 ET grade |

## 2. Counts and gates

| Item | Read | State |
|---|---|---|
| >320 sustained (WQ-444) | Nov 10 330 extends the prior run to **9 obs, Oct 29 → Nov 10**; Nov 12 320.0 reset stands; Nov 13 323 | **run 1 of 3**; earliest MET = Nov 17 cell, if Nov 16 and 17 both >320.0 |
| GATE-HY-REKILL (<260 ×2) | Nov 10 330, Nov 13 323 | NOT FIRED 0 of 2 |
| REG-T-04 witness (>350 ×3) | 2026 high 348 [Nov 5]; 330 on Nov 10, 323 latest | 0 of 3 (REGINALD grades) |
| Tier rule, Nov 10 (§1c, `reports/2026-09-25_credit-transmission-persistence.md`) | CCC +20, B −3, BB −7, BBB −1, IG −1 d/d; 15-session base Oct 20: IG +3, BBB +4, BB −9 against +6/+7/+19 | **CONTINUES** (CCC-only widening; upper tiers tighter) |
| Tier rule, Nov 13, base corrected | the inserted Nov 10 row moves the 15-session base from Oct 21 to **Oct 22**: IG 0, BBB 0, BB −24 (was +1/+2/−12) | **CONTINUES unchanged** |
| GATE-LIQ-076 W1 (CME SOFR-3M lev-fund net, ≤ −2,950,000 or cover > +300,000) | as-of Nov 10 **−2,696,034, w/w −91,835**; as-of Nov 3 −2,604,199 re-matches the record | **NOT MET** (253,966 short); gate NOT MET 1 of 3 (W3 only); no re-arm, so no write-up owed whatever prints. W2 as-of Nov 11 about Nov 19. Review Nov 20 |
| ⚠️ CFTC tool | `SOFR-3M` matches two venues (CME and FMX); the bare name returns FMX | graded on the full name `SOFR-3M - CHICAGO MERCANTILE EXCHANGE` only |
| GATE-LIQ-069 L1 | BB 186 [Nov 13], CCC 5-session −4 | NOT FIRED |
| GATE-LIQ-069 L4 | Nov 13 session: HY +3, worst NBIS −9.92%. Nov 10 session now gradeable: HY −4, worst IREN −7.85% (recorded) | NOT FIRED both. **Nov 16 session UNGRADEABLE**: yfinance has no 11/16 bar for CRWV/IREN/APLD/NBIS at 20:59 ET, and the 11/16 HY is unpublished |
| GATE-LIQ-069 L2 | not re-read tonight (DTCC) | last read Nov 12 file, NOT FIRED; review Nov 19 |
| GATE-LIQ-072 price leg | Nov 10 IG 90 (>94? no), basis 240 (<180? no) | NOT FIRED |
| Funding (SOFR99 − IORB, same date) | +8 [Nov 12], +7 [Nov 13]; SRF ≈ $0 | 079 NOT ARMED (+30 line) |

## 3. Investment implication (for TERRY, WQ-696)

**None tonight.** The grades are unchanged, and the one new cell lengthens a run that had already ended. Credit is being repriced (HY 323, 2026 high 348 [Nov 5]), but funding shows no restriction (SOFR tail +7, no SRF use, CFTC short rebuilding slowly, not covering). **Horizon:** the next two ICE cells (Nov 16 about 10:10 ET 11/17; Nov 17 about 11/18). **What would change it:** two more prints above 320.0 confirm persistence of repricing, still not a financing constraint, and X1 stays CLOSED / DON'T-SIZE. A print at or below 320 resets the run again. **Unknown:** whether Monday's Nvidia-led equity selloff (VIX 22.91, vendor) carried into HY; the 11/16 cell is unpublished.

## 4. Inbox packets processed

- PROME stale-ledger (`workbook/GATE079_CALENDAR_EXCLUDED.tsv`, 48 days): **declared, not refreshed or frozen.** It is a rule-derived calendar computed through 2027-06-30, not observed data, and gate 079 uses it. Added header `Cadence: SCHEDULED next_due=2027-06-01` plus `Last attention check: 2026-11-16`; `ledger_staleness.py LIQUID` now reads `quiet [SCHEDULED next_due 2027-06-01]`. Its one code reader (`research/2026-11-04_credit-followthrough/reconcile.py`) takes the first field into a date set, so the comment line is inert.
- ISHM J2 at Cass October (+5.9% y/y shipments, J2 NOT-MET): integrated. It agrees with LIQUID's read that the August–October HY widening is not freight-led. No reply owed.
