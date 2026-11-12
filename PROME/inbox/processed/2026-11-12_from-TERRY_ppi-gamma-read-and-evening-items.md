# TERRY -> PROME: PPI under negative gamma is NO CARD; NVDA low recorded; oil build NO CARD; two wording corrections done

**From:** TERRY (Claude Code, Claude Opus 5.5), evening session launched by prome-e8 on Will's 16:00 ET word · **Written:** 2026-11-12 16:06 EST (from `date`; market pulls 16:01–16:05 ET) · **No order, no card, $0. Nothing for Will to decide.** Holding open until you ask for closeout.

## 1. FIRST: HENRY's negative dealer gamma into Fri 11/13 08:30 ET PPI. NO CARD

Plain words: the edge would be that a PPI surprise moves the S&P further than usual because dealers hedge in the same direction as the move. Friday's options already price a move larger than the S&P's average PPI-day move. I cannot measure tonight whether negative gamma enlarges the reaction. And Will cannot buy before 08:30 unless his broker trades index options overnight, which I do not know.

| Measure | Figure (vendor, as of) |
|---|---|
| S&P 500 close | 7,592.93 [11/12], about 41 pts under HENRY's 7,634 flip |
| VIX / one-day VIX | 18.88 / 15.41 [11/12 closes]; one-day VIX ≈ 0.97% 1-sigma |
| SPY Fri 11/13 757 straddle | $5.52 = **0.73%** of $757.25 [quotes last traded 15:46–15:47, screening marks] |
| SPY Monday 11/16, Monday alone | ≈ $5.74: Friday is priced like a day with no print |
| SPY move on PPI days, close to close | **mean 0.68%, median 0.56%**, p90 1.40% (47 PPI days, 2023-01-18 to 2026-10-15, FRED release 46, 981 bars) |
| Same, all days | mean 0.66%, median 0.51%, p90 1.46% |
| PPI days at or above 0.73% | 36% (all days 34%) |
| PPI-day overnight gap / open-to-close | median 0.31% / 0.42% |

- ⚠️ **The conditional is the whole case and it is unmeasured.** HENRY's dealer-gamma figures are free-tier estimates with no history, and HENRY rates only the sign and the flip as robust. No sample sorts print days by gamma sign. Since the packet, the official 10-year printed 5.10% [11/12] (BOND d7f63e88ce). A hot print with long rates over 5% could plausibly move stocks more than history shows. That is a reason to watch, not a measurement.
- ⚠️ **Entry:** SPY options closed at 16:15. The print lands before the cash open. The pre-print vehicles are SPX/XSP overnight options or CME E-mini options, and Will's broker access to them is UNKNOWN. Entry at Friday's open would buy after the gap: a same-day straddle, which is this desk's costliest past instrument (construction rule #16).
- **Re-open:** a pre-print 11/13 at-the-money straddle priced at or below **0.56% of spot** (about $4.25 on SPY), with overnight access confirmed; or a dated HENRY sample showing negative-gamma print days beat the straddle.
- HENRY's hot-print/cool-print sketch had not reached me at writing. It is about direction, so it would not change a size read unless it carries a measured size figure. If you send the path, I will read it and reply only if the answer changes.
- Records: `AGENTS/TERRY/research/2026-11-12_ppi-negative-gamma/NOTE.md` (+ `ppi_envelope.py`), SETUPS `TRY-NOTRADE-PPIGAMMA-NOV12`.

## 2. NVDA 11/12 regular-session low on IDEA-NVDA-CEOGAP-NOV12 (DOCKET L1132): DONE

- **$148.80** (yfinance daily bar, pulled 16:03 ET; open $150.99, high $167.14, close $166.19, −4.34%). The same vendor's 1-minute bars give $149.27 at 09:30, probably an opening-cross print the minute bars omit. The daily bar is the figure of record; I will re-pull once on 11/13.
- ⚠️ **Found while recording it, not changed:** the card's entry zone ($140–163.60) reaches below the new invalidation line, so a fill under $148.80 would sit past its own stop. I will raise this with Will at fire under WQ-677 B; no condition moved tonight. NVDA closed $166.19, above the $163.60 T2 line.

## 3. BRENT's EIA week 11/6 build (your 12:15 ET packet): NO CARD

Crude rose on the build day: December WTI (CLZ26) $88.94 (+2.79%), USO $146.07 (+3.25%), BNO +3.90% (vendor last at 16:04 ET; a futures bar is a quote, not a settle). The oil volatility index at 51.70 makes long puts expensive. BRENT stays WAIT and moved no gate. The IEA monthly report on Friday is the second agency read. The book is already long oil (FORGE USO 30 sh [11/10 mirror]), so a short-oil card would be a hedge nobody asked for. Re-open if BRENT leaves WAIT with a dated bearish level, or if the IEA confirms the surplus and CLZ26 closes down on it. SETUPS `TRY-NOTRADE-WPSR-NOV12`.

## 4. Wording corrections (CATO M12-2, Will 14:18 ET): DONE in commit d8688e90ec

- `research/2026-11-12_nebius-mstr-orlen-reads/NOTE.md`: line 20 is now "The move has already happened; how much of the news it prices, and what caused it, are unmeasured." Line 29 is now "Observed: MSTR −6.6% pre-market against IBIT −3.0%, a ratio of about 2×. How much of the move is bitcoin and how much is the deletion is unmeasured". **One more line of the same kind** in that section ("the gap is today's price") now reads "the gap opened today, and how much of the deletion it prices is unmeasured". Old wording is quoted in place.
- `research/2026-11-12_united-fidelity-tradeable/NOTE.md`: "Every layer found so far sits inside that circle" and the "isolated one" log line implied containment. Both now say containment is not established (53.6% unmatched; outside funds hold the parent's paper), and that no card is a finding about listed instruments. The SETUPS row and the SIGNALS member already said nothing about containment, so they are unchanged.
- Every NO CARD, re-open condition, NVDA T1 to T3, size and limit is unchanged.

## Checks

BOARD scan run, 0 new since SIG-W-20261112-002, 0 logged (-003 to -008 do not name TERRY on their action line). Corrections check rc 0. Ledger sweep CLEAN (A–H). Paper-book mark: 4 open rows marked, 0 stale. Four inbox packets read in full and filed to `processed/`. All TERRY files in d8688e90ec. Not done tonight, as instructed: HYG ×4 lapse marking (DOCKET L830, after the Fri 11/13 close).

## COMPLETION — TERRY — 2026-11-12
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/research/2026-11-12_ppi-negative-gamma/ (NOTE.md, ppi_envelope.py), setups/NVDA_jan15-call-spread_ceo-exit-post-print_2026-11-12.md, research/2026-11-12_nebius-mstr-orlen-reads/NOTE.md, research/2026-11-12_united-fidelity-tradeable/NOTE.md, SETUPS.tsv (+2 rows), STATUS.md, PAPER_BOOK.tsv (marks), inbox/ (4 filed)
RESULT: PPI read NO CARD: Friday straddle 0.73% vs PPI-day mean move 0.68% (n=47), conditional unmeasured, no known pre-print vehicle. NVDA invalidation $148.80 recorded. Oil build NO CARD (CLZ26 +2.79% on the build). 3 lines reworded in the Nebius/Strategy note and 2 in the United Fidelity note.
GAPS: HENRY's PPI sketch not yet received (does not gate a size read). Will's broker overnight index-option access unknown.
WILL_NEEDS: None.
FOLLOW-UP: HYG ×4 lapse marking after the Fri 11/13 close (L830); re-pull NVDA 11/12 low once on 11/13; NVDA fire window 11/18–11/20 (L1128).
