# G:GATE-BRENT-COT-35B — vintage #14 (as-of Tuesday 2026-11-10), graded Monday 2026-11-16

**Release:** CFTC Commitments of Traders, as-of 11/10, moved by the Veterans Day delay to Monday 11/16 15:30 ET (CFTC 2026 schedule, read 11/13). It was posted: raw file `Last-Modified: Mon, 16 Nov 2026 20:33:41 GMT` = 15:33:41 ET.

**Source:** the CFTC's own raw file `https://www.cftc.gov/dea/newcot/f_disagg.txt`, DISAGGREGATED FUTURES-ONLY, market `WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`, code 067651. No secondary source used.

## Two independent pulls

| Pull | Time (ET, from `date`) | Method | Result |
|---|---|---|---|
| 1 | 16:22:21 | `scripts/cot_grade.py --expect 2026-11-10` (urllib, browser User-Agent), rc 0, ledger row appended | report_date 2026-11-10 in the row; shorts 122,378; longs 148,092; OI 1,917,473 |
| 2 | 16:22:36 | separate `curl` with a browser User-Agent, HTTP 200, file sha256 prefix `3d3bf9ffda18a6b6` | **identical to the digit**: 2026-11-10, 067651, OI 1,917,473, MM long 148,092, MM short 122,378 |

A first `curl` with curl's default User-Agent got HTTP 403 (a "Just a moment..." challenge page, not data). That is the LESSONS L25 pattern: the host is up, the client was refused. Saved: `pull2_headers.txt`, `pull2_wti_row.csv`.

## Grade by the row's own letter (REGISTRY COT-FUEL-35B; PROME/GATES.tsv G:GATE-BRENT-COT-35B)

| Leg | Definition | #14 value | Band | Verdict |
|---|---|---|---|---|
| A | MM gross shorts vs frozen base 122,904.5 | **122,378** | ≤109,164 SPENT · 109,165–118,325 NO-VERDICT (deadband decisive; 113,745 is its centre, not a boundary) · ≥118,326 NOT-SPENT | **NOT-SPENT** (4,052 above the 118,326 floor) |
| B (gating) | field 15 ÷ field 8 × 100 (M_Money_Positions_Short_All ÷ Open_Interest_All) | **6.3823%** (122,378 ÷ 1,917,473) | ≤4.909% SPENT | **NOT-SPENT** (1.4733 points above) |
| Joint | both legs agree, or NO-VERDICT | | | **JOINT NOT-SPENT, 8th consecutive** (9/22 through 11/10) |

Consequence by the row: NOT-SPENT (and NO-VERDICT) ⇒ base-case sizing within the cap. The fuller-size branch stays not arguable.

## What changed from vintage #13 (as-of 11/3)

| | #13 | #14 | Change |
|---|---|---|---|
| MM gross shorts | 125,654 | 122,378 | **−3,276** |
| MM gross longs | 147,382 | 148,092 | +710 |
| Open interest | 1,908,732 | 1,917,473 | +8,741 |
| OI share | 6.5831% | 6.3823% | −0.2008 points |
| Leg A cushion over 118,326 | 7,328 | 4,052 | −3,276 |

- Shorts have fallen four weeks running (131,399 on 10/13, then 127,226, 126,305, 125,654, 122,378). This is the lowest reading since 121,362 on 9/22, the first of the eight NOT-SPENT prints.
- **A fall of 4,053 or more next week puts Leg A in the deadband. The joint verdict would then be NO-VERDICT, which carries the same consequence (base-case sizing).** Only a joint SPENT changes anything.
- **Leg B is the binding leg.** At this week's open interest, the 4.909% share requires shorts at or under about 94,128 (1,917,473 × 4.909%), roughly 28,250 below today. Leg A's SPENT line (109,164) is 13,214 below. Open interest rose, which pushes the share bar further away for any given short count.

## Next

#15 (as-of Tue 11/17) is due Fri 11/20 at 15:30 ET. #16 (as-of 11/24) is due Mon 11/30 under the Thanksgiving delay (CFTC schedule as recorded 11/13; re-verify at cftc.gov before relying on it). Owner-recommended review_by: **2026-11-20**.

⚠️ Non-claims travel with the row. No out-of-sample test. n=0 genuine physical reopenings. No price validation. This is a positioning descriptor and a sizing modifier only, never an entry trigger.
