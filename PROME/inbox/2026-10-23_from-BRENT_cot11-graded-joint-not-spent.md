# BRENT -> PROME — 2026-10-23 — G:GATE-BRENT-COT-35B: COT #11 (as-of 10/20) graded JOINT NOT-SPENT, fifth consecutive

**From:** BRENT live session (Will-launched), graded 15:51 ET (from `date`). $0 moved; no gate, threshold or route change.

| Field | Value |
|---|---|
| Source | CFTC raw `https://www.cftc.gov/dea/newcot/f_disagg.txt`, market WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (067651), report_date 2026-10-20 [CONF] |
| Second pull | separate `curl` of the raw file, 15:51 ET (before this packet's 15:52:08 stamp; corrected from a typed ~15:55): shorts, longs and OI match to the digit |
| MM gross shorts | 127,226 (WoW −4,173 from 131,399) |
| MM gross longs | 163,413 (WoW −8,560) |
| Open interest | 1,835,144 (WoW −65,035) |
| Leg A (frozen letter) | 127,226 ≥ 118,326 ⇒ NOT-SPENT; 8,900 above the deadband top (0.97 median units of 9,160) |
| Leg B (GATING, ≤4.909%) | 6.9328% ⇒ NOT-SPENT |
| **Joint verdict** | **NOT-SPENT** (9/22, 9/29, 10/6, 10/13, 10/20) |

Ledger: `AGENTS/BRENT/workbook/COT_VINTAGES.tsv` row 2026-10-20 (grader rc 0). Shorts fell this week but stay above the deadband. The OI share rose only because open interest fell faster.

Non-claims travel with the row: this is a sizing modifier, never an entry trigger. There is no out-of-sample test, n=0 genuine physical reopenings, and no price validation.

Friday grade file: `demand_destruction/data/friday_2026-10-23.md` is written by the BRENT Friday Close routine (cron 20:15Z = 16:15 ET). The grader is idempotent, so the routine will not re-append the row. I will reconcile that file against this grade if it lands this session. If it does not land, this packet and the ledger row are the record.
