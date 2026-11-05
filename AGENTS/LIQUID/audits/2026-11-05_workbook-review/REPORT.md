# LIQUID workbook review, 2026-11-05

**Stamp:** 2026-11-05T10:50:32-05:00. **Trigger:** Will in LIQUID's window, "Okay lets look at workbook. Please review it and see if anything should be updated?" **Scope:** what the last 24 hours made stale, on top of the November 4 audit of 23 files (`audits/2026-11-04_workbook-sweep/REPORT.md`). Not a re-read of every row.

**No gate letter, threshold, operator, frozen row or pinned prediction changed.** LIQ-04 is Kernel-pinned, FLOW and VX stay frozen, and nothing changed in `PREDICTIONS.tsv` or `GATE079_CALENDAR_EXCLUDED.tsv`.

## Updated

| Surface | Change | Why |
|---|---|---|
| `CATALYSTS.tsv` + `CALENDAR.md` | Seven forward rows added: 3Y Nov 9, 10Y Nov 10, 30Y Nov 12, TIC Nov 18 and Dec 15, FOMC Dec 9, year-end turn Dec 31 | Forward docket had 10 rows and no auction, TIC or FOMC. Dates read from TreasuryDirect, Treasury TIC and Fed pages, not memory |
| Same | Q3 BDC row retitled | Q2 fields are closed |
| `KB.tsv` | KB-LIQ-136 Q3 verdict graded late: NOT PERSISTENT, re-rated n=11 | Owed October 8; no earlier grade located |
| `KB.tsv` | KB-LIQ-144 month-turn re-check: −11 bp, base rate restated | Due November 2 |
| `KB.tsv` | New KB-LIQ-151 (ICE timing) and KB-LIQ-152 (XCCC route); 069 and 076 review cells | Durable findings from today |
| `BDC_MARK_CONVERGENCE_MONITOR.md` | Header state, ARCC baseline 0.9890 | Header still said Q2 fields were open; baseline said unmeasured |
| `REFERENCE_TABLES.md`, `OPEN_MONITORS.md` | Removed "CLI WITHHELD"; frontier moved to November 4 | Overtaken today |

## Left alone, on purpose

| Item | Reason |
|---|---|
| `DEALER_POSITIONING_NEXUS_WATCH.md`, `OPEN_MONITORS.md` basis row | "November 5 pending" is still true until tonight's dealer release |
| 076 CATALYSTS row | Same |
| KB review dates past on 084, 087, 095, 096, 097, 127 and others | Conditional re-checks with no trigger met, or method rows. Dates not rewritten: a bumped date over an unread row certifies nothing |
| ES01, ES05, Test B/T4, Test C | No recoverable definition or result; recorded in STATUS §3 |
| `AUCTION_FRAMEWORK.md` | Titled for 20Y and last touched October 14; usable, but no 3Y/10Y/30Y baselines. Decision below |

## Needs a decision

1. **`CLAUDE.md` line 191** still says FRED ICE publishes ~16:15 ET. That is Will's word to change; `transmission_check.py` and the 9/25 report carry the same claim.
2. **`boot.py` countdown** shows two ✅ RESOLVED LIQ-07 rows (Nov 6, Nov 10) as imminent. A small fix to skip ✅ rows would clear noise.
3. **Refunding auction read:** the 3Y, 10Y and 30Y settle 25B on November 16, and `AUCTION_FRAMEWORK.md` has no baseline for them. Comparing each to its last six auctions is a bounded prep; not started.

## Limits

TreasuryDirect shows only announced auctions, so 20Y and the late-November 2Y/5Y/7Y are not yet rows. TIC data months are read from the page's rule, not stated. KB-LIQ-136 is on latest-revised FRED. `NEXUS_BRIEF.md` still carries the withheld wording and BROADENS; it is refreshed at closeout under its own step.
