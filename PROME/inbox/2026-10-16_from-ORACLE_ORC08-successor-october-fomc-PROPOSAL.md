# ORACLE → PROME — WQ-440 (b): a successor for the spent VX-ORC-08, for the October FOMC (10/28) — PROPOSAL for Will's word

**ORACLE · 2026-10-16 13:4x ET (from `date`) · PROME spawn prome-ac.** Asked by `inbox/processed/2026-10-15_from-PROME_WQ314b-WQ439-WQ440-RULED.md` item 3. VX-ORC-08 is retired as SPENT on `workbook/VX.tsv` (its Critical, "a 2026 hike prints", happened 9/16). Nothing below is encoded. $0, no trade.

## Current read (context)

| Venue | Market | Read | Depth | Time |
|---|---|---|---|---|
| Polymarket (trigger venue, WQ-440 a) | Fed HIKE at Oct mtg (meeting-specific) | **12.5%** (31.5 at 2026-10-15T12:39Z ⇒ −19.0 in 29h) | vol $10.0M · liq $352.8K | 2026-10-16T17:36Z |
| Polymarket | NO change at Oct mtg | 86.5% | liq $549.6K | same |
| Kalshi (corroboration only) | KXFED-26OCT >4.00 | 16.0% (Δprev −8.0) | OI 72.6K | 2026-10-16T17:39Z |

## Proposed row VX-ORC-09 "Fed HIKE at the October 2026 FOMC (10/28)"

| Cell | Proposed |
|---|---|
| Instrument | Polymarket meeting-specific "HIKE at Oct mtg" YES (as `polymarket.py pull --log` logs it). Kalshi KXFED-26OCT >4.00 is corroboration and never fires the row |
| Watch | a 48h move >10pp on a log-row pair ≤48h apart (WQ-439 grading) |
| **Alert** | **≥50.0% on 2 qualified reads on consecutive business days** (liq ≥$5K; one read = first pull per business day; band test at 0.1pp, as WQ-314 b O3/O4/O6). Meaning: the crowd prices a hike as more likely than not |
| Critical | the FOMC announces a hike on 2026-10-28 (statement) |
| Retires | at the 10/28 decision, either way; a December successor is a new ask |

**Why 2 reads, not 3:** the window is 8 business days (10/16–10/27); a 3-read run needs ≥3 of them and can arm only on day 3 at the earliest. 2 reads still blocks a one-print spike. **Why 50:** the old 66 level was set on the aggregate Fed-HIKE-2026 market (KB-ORC-046), a different object; a meeting-specific question has a natural midpoint.

⚠️ **It only works with a pull cadence.** DOCKET L729 already gives ORACLE one pull per business day to 10/30; the row would ride on those pulls. Without that cadence it cannot arm.

⚠️ Who owns the reality: LIQUID/HENRY own the Fed path; this row reads the crowd, nothing else.

**ASK (Will, via PROME):** approve VX-ORC-09 as written · amend the level or read count · decline (the October question then has no row).
