# CRL-17 CONTEST RULING — 2026-10-01 (Thu, ~16:2x ET; typed "16:4x" corrected 16:30 at `date`)

**Session:** Will-launched catch-up (Will 10/01 "ok approved go ahead"). **Owed:** STATUS dated board, 10/02 (CARL packet `8e93b6dda`, disposition row 15 of `runs/2026-10-01_INBOX_DISPOSITIONS.md`). **Read whole at the artifact:** `AGENTS/CARL/thesis/PREDICTIONS.tsv` rows CRL-16 and CRL-17 (header vintage "Last real data refresh: 2026-10-01"); `FORGE/PREDICTION_DISCIPLINE.md` lines 12, 31, 37, 41, 42, 50.

## Ruling
**CRL-17 NO-VERDICT-BY-INSTRUMENT STANDS. DAEDALUS does not contest. CARL re-tokens nothing.** CRL-17 stays excluded from Brier.

## Why (canon first, judgement second)
| # | Rule (ratified) | Applied to CRL-17 | Verdict |
|---|---|---|---|
| 1 | WQ-162 (Will 9/02, PD:31; restated at PD:37): an unnamed grading basis is graded NO-VERDICT, **never on a series chosen after the data** | Instrument cell = `CARL composite estimate :: small-business owner income destruction (annualized) :: >$100B`, which is a source type, not a published series. CARL's dated search on 10/01 found no dollar series. Grading it on NFIB or Sub-V now would be choosing a series after seeing the data. | NO-VERDICT |
| 2 | WQ-288 (Will 9/24, PD:37): a registered Invalidation that is MET at its primary resolves the row at the fire | Invalidation = tariff costs −50% **AND** NFIB >100 **AND** Sub-V <+30% YoY. NFIB printed 97.4 / 99.8 / 98.7 (Jun/Jul/Aug, per CARL's cell; secondaries, not primary-verified), so the AND is **not met**. No route to MISSED through the kill clause. | not MISSED |
| 3 | WQ-161 ① (Will 9/10, PD:42) + `finding_resolvability_defect_is_status_not_confidence` (PD:41) | Non-resolution is a STATUS, never a mass or a confidence move. CARL's 8/15 trim 40→25 was priced on adverse observables alone, with the defect explicitly not priced (cell (b)). | consistent |
| 4 | Negative-resolution dated-search convention (Will 8/17, PD:50) | Dated search 2026-10-01 is recorded in the Notes cell. | satisfied |

**Why CRL-16 differs (CARL's distinction, tested and accepted):** CRL-16's Invalidation ("SB provision declines AND classified loan migration reverses") ran at its named observables (ZION provision +$3M vs −$1M; HBAN criticized-asset ratio declining). Its MISSED is the WQ-288 shape: the kill clause fired. CRL-17's kill clause did not fire. These are two different rules, and the outcomes are consistent with each other. *(CRL-16's 8/10 grade predates WQ-162. Whether its link-grading would survive today's canon is not this ruling's question; Will approved its 9/24 re-grade, and DAEDALUS does not reopen it.)*

## The forfeit concern, measured rather than argued
On the 9/24 record's basis (`runs/2026-09-24_CARL_BRIER_RESCORE_AND_CRL08_RULING.md:48`, n=10, Σ 4.2703, mean **0.4270**, with CRL-08 at 28%):

| CRL-17 treatment | Brier | n | mean |
|---|---|---|---|
| Excluded (this ruling) | — | 10 | **0.4270** |
| MISSED at first-call 55% | 0.3025 | 11 | 0.4157 |
| MISSED at last mark 25% | 0.0625 | 11 | 0.3939 |

**Scoring the miss would have IMPROVED CARL's mean.** The exclusion does not flatter the desk; it costs it 0.011 to 0.033. The escape-hatch worry ("an author writes an ungradeable instrument and dodges a miss") is real as a class but does not operate on this row. It is answered by counting registration defects, not by a Brier entry: CARL's own cells name the unpublished-instrument class at least three times (CRL-16, POP-P04, CRL-17; CRL-16's cell also cites CRL-22 v2 and Fitch ATR, so the two cells number it differently, and reconciling that is CARL's job). That count belongs to the registration-quality layer (WQ-162's basis line at registration), not to calibration.

*Arithmetic: `python3 -c` from the 9/24 Σ in this session; the aggregate's own vintage is the 9/24 record plus CRL-08, and any CARL change since (CRL-27 retired unscored, CRL-31 OPEN) does not enter the scored set.*

## Not done, stated
- NFIB levels are CARL's secondaries (nfib.com 403s), **not primary-verified here**. The ruling does not depend on them: rule 1 alone decides it, and the Invalidation would need all three legs.
- CRL-19 `MIXED` is held for Will (9/24 record line 49); untouched.
