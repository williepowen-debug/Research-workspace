# CRUISE -> PROME: L502 CRU-11 ratio-form successor to CRU-05 drafted (returns to WQ-242)

**Dispatched: 2026-10-02 ~11:5x ET · CRUISE under PROME Tier-1 spawn (prome-96 → cruise-02a) · $0 · no trade, no threshold moved**

## ACTION — none; this is a Will-approval close on WQ-242

**WHAT:** CRU-11, the ratio-form successor to CRU-05 (FAILED 2026-09-13 on a two-absolute-levels construction), is registered as a prospective row at `AGENTS/CRUISE/workbook/PREDICTIONS.tsv` line 12 in this commit (append-only). Returns WQ-242 to Will's queue for one approve.

**ONE-LINE PREDICATE:** NCLH underperforms RCL on cumulative total return from 2026-10-02 close by **AT LEAST 5 PERCENTAGE POINTS** at the 2026-11-14 window close. Confidence 50%. Status OPEN.

## WQ-162 SIX ELEMENTS (frozen in the cell at registration)

| # | Element | Value |
|---|---------|-------|
| 1 | Series | NCLH (NYSE:NCLH), RCL (NYSE:RCL) daily closes from the repo-pinned Yahoo Finance pull (python .venv yfinance, `download(auto_adjust=False)["Adj Close"]`), with `FORGE/tools/market-data/fetch.py` as the cross-check at window close only. Same source family as CRU-05, WQ-215, WQ-222. |
| 2 | Window | 2026-10-02 close (base) through 2026-11-14 close inclusive — 30 trading sessions. |
| 3 | Price type | **ADJUSTED** daily closes (total return — dividend reinvested on the ex-date). WQ-215 / WQ-222 basis, same as VX-CRU-06. |
| 4 | Sampling | Every in-window trading session close; **grade on the single window-close reading** (persistence reading, not path-max — same as CRU-05 was). |
| 5 | Basis | Cumulative TR of each name from its own 2026-10-02 close in pp: `TR_cum_i(t) = AdjClose_i(t)/AdjClose_i(2026-10-02) − 1`. Graded quantity: `NCLH_TR_cum(window_close) − RCL_TR_cum(window_close)` in pp. |
| 6 | Resolver | **≤ −5pp = CONFIRMED** (dispersion holds); **> −5pp = FAILED** (dispersion closes); both pinned sources unreadable for a traded in-window close = NO-VERDICT (not FAILED). |

## WHY A RATIO FORM, WRITTEN BEFORE THE GRADE

CRU-05's letter wrote dispersion as TWO ABSOLUTE per-name level conditions (RCL ≥ its own 3-mo mean AND NCLH ≤ its own 3-mo mean). Under a common-mode sector drawdown both names fell below their own means and the row read FAILED while the relative dispersion the prediction was actually about remained intact: NCLH -22.04% vs RCL -14.71% over 8/14→9/11 — value still 7.33pp worse than premium. `[[finding_spread_metric_blind_to_common_mode]]`

CRU-11 replaces the two-levels construction with **a single spread quantity** (NCLH_TR_cum − RCL_TR_cum). The spread is well-defined under any common-mode shock by construction — a sector drawdown moves both legs' TRs down the same amount, leaving the difference unchanged. So the row **cannot** read FAILED on a common-mode shock that the thesis is agnostic to; it reads FAILED only when the dispersion itself closes, which is the thesis.

## DISTINCT FROM VX-CRU-06 (asked explicitly in L502)

- VX-CRU-06 subject: **CCL-over-RCL** excess drawdown (high-cost vs premium), 2026-09-03 base, through the CCL Q3 FY26 print (2026-09-29). CLOSED window; graded at the print (NOT TRIPPED, max 1.8387pp).
- CRU-11 subject: **NCLH-over-RCL** cumulative TR difference (fragile vs premium), 2026-10-02 base, through 2026-11-14. OPEN window; forward test, post-print.

Different pair, different window, different direction of the dispersion. Both carry the 5pp magnitude from WQ-222 for threshold consistency, but neither subsumes the other.

## WHY 50% AND NOT HIGHER

CRU-05's prior was 50% (calibration-neutral on a FAILED). CRU-11 inherits that prior; a ratio form that resolves TRUE on the same tape CRU-05 resolved FALSE on indicates the instrument, not the prior. The 5pp threshold is tighter than the actually-observed 7.33pp dispersion at the CRU-05 grade, but the 30-session window post-print cuts across the typical analyst-reaction phase, the NCLH Q3 print (expected early-November), and the RCL Q3 print (historically ~late October), each of which can compress dispersion toward zero.

## PRE-REGISTERED, NOT GRADED, RECORDED ONLY

Base = both legs at their own 2026-10-02 close. By construction `NCLH_TR_cum(2026-10-02) − RCL_TR_cum(2026-10-02) = 0`. First in-window close is 2026-10-02 itself. The prior STATUS pulls (NCLH $14.12, RCL $245.81) are 2026-09-18 closes and are not the window base — fresh closes at 2026-10-02 end-of-day set the base.

## TWO KNOWN TAIL RISKS, DELIBERATELY NOT RE-TUNED OUT

- **NCLH buyback or similar RoC inside the window** can tighten its spread to RCL without K-shape convergence. Not an exclusion — the row grades the SPREAD, not the mechanism, and if NCLH buys back aggressively enough to close the dispersion that IS the dispersion closing on its own terms.
- **Big-3 M&A event or an NCLH-specific event** that flips both legs: resolver NO-VERDICT clause does NOT cover this; it covers only unreadable closes. Grade on the letter if that happens.

## WHAT I AM NOT DOING

- **NOT retro-applying CRU-11 to CRU-05's data.** CRU-05 is FAILED on its letter, scored FAILED, calibration-neutral at 50% — stays untouched. [[finding_rebased_metric_check_made_date]]
- **NOT re-opening CRU-05.** The letter is what was committed, the letter is what graded.
- **NOT amending CRU-11's cell after Will's approval.** Any later edit to any of the six elements is a NEW row (CRU-09 precedent).

## RECEIPTS

- `AGENTS/CRUISE/workbook/PREDICTIONS.tsv` — row CRU-11 appended as line 12. Full six elements inlined.
- `AGENTS/CRUISE/workbook/KB.tsv` — KB-CRU-140 (CRU-11 registered, this file).

## WILL CLOSE

WQ-242 moves off ⛔ waits: CRUISE and back to Will's queue — one approve or reject on the predicate / threshold / window / resolver as a package. If Will asks for a different window or a different magnitude threshold, that's a NEW row; the one above is what I registered on this commit.

— CRUISE
