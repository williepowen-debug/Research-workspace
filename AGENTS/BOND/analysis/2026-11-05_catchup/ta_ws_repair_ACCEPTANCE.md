# ta_ws_schema repair: acceptance conditions, written before any edit

DOCKET L859, WQ-229. Reader HOLD: `inbox/2026-11-05_from-PROME_ta-ws-schema-read-HOLD.md` (85a57fec0). Findings verified at the code by BOND before writing this. No level, operator or bar moves. No new tool or checker: the guards go into the three existing files.

The defect in its own terms: **the tools can reach an answer from a feed whose meaning has changed.** The 10/29 repair closed one door (no row has a date). Every door below must refuse.

| # | Finding | Property that must hold after the repair |
|---|---|---|
| AC1 | F1 | `docket_check` returns rc 2 whenever any row lacks `securityType` or carries a value outside {Bill, Note, Bond}, with a real undocketed coupon in the payload. A bills-only week stays rc 0. |
| AC2 | F2 | `docket_check` returns rc 2 when any Note or Bond row has an absent, empty or non-ISO date, or a date more than 7 days past, even when bill rows keep good dates. No coupon row is ever dropped silently. |
| AC3 | F3 | When old and new names are both non-empty and differ, neither value is used. Docket: rc 2. Grader: the print refuses, rc 2, never CLEAN. A row where they agree proceeds. A conflict on another CUSIP does not block the graded CUSIP and leaves every pool, named. |
| AC4 | F4 | An old key that is present and empty is filled from a good new key, for every rename. |
| AC5 | F5, F6, F7 | Grader refuses, rc 2, when an `auctioned` coupon row has `tips`, `floatingRate` or `reopening` other than Yes or No, a non-ISO date, a `securityType` outside the vocabulary, or the payload holds zero coupon rows. The same checks apply to the upcoming target. FRN CUSIPs are excluded from TA_WS rows by list as well as by field, and an empty FRN pull warns. |
| AC6 | F8 | Deleting any rename, or disabling any new guard, fails a selftest. Selftest counts are computed. The regression suite exercises the repair. |
| AC7 | F5, F9 | The docstring says what is true: no "exactly as before", and the outside amount reads "empty or 0". |
| AC8 | O1 | Display only. A registered print with I′ fired can never end on a line reading CLEAN. Operators unchanged. |
| AC9 | all | No answer moves on today's feed: live docket rc 0 with coupon set 3; rolling bars for the three refunding CUSIPs equal the 11/2 snapshots at 2dp; the 10/21 and 10/22 registered grades reproduce; the reader's controls still fire. |

## Neighbours

| Category | Test |
|---|---|
| Ordinary | Live 11/5 payloads through the real `main()` of both tools; AC9. |
| Overlap | Old and new both present: agreeing, disagreeing, old empty, date equal with a different time part, number equal with different formatting. |
| Wrong owner | A conflict or odd value on a bill row or another CUSIP must not refuse the graded print through the row-level path; a type vocabulary break refuses, because membership is then unknowable. `buyback_f2.py` reads FiscalData, not TA_WS: N/A, not touched. |
| Missing information | Absent, empty and None for each key; empty payload; zero coupon rows; bills-only week; empty FRN pull. |
| Concurrent activity | N/A for the guards: each tool reads one fetch in one process and nothing shared is written beyond the existing FRN cache. Rerun in a scratch copy so the live cache is not touched by tests. |

## Named residue, not fixed here

F7's pre-print line when a target stays in `upcoming` after its results exist: reachable only if `auctioned` still has coupon rows but not the target; depends on same-day feed behaviour that no one has observed. First real look: 11/9 after 13:00 ET.

## Outcome, read 2 (2026-11-05): ACCEPT-WITH-RESIDUE, L859 closed by PROME

Bounded to the diff of 3036cea01, no ❌, last read under the review budget. Ledger: `inbox/processed/2026-11-05_from-PROME_ta-ws-reread-ACCEPT-WITH-RESIDUE.md`.

**Operating caveat for 11/9, 11/10, 11/12: a PRE-PRINT line after the print means not graded, whatever the rc.**

| Residue | What remains | Reaches the registered grades? |
|---|---|---|
| R1 | Bill row with disagreeing old and new dates: docket rc 0 with a false coverage claim | No. Needs both names in the feed; 0 of 8 today. Named one-line fix, not taken: it would ship unreviewed |
| R2 | Reopened CUSIP with a disagreeing date older than an earlier print: audit grades the older print at rc 0 | No. Frozen path refuses; November refunding CUSIPs are new issues |
| R3 | `--date` mode can print GAP, then grade at rc 0 | No. Registered form is `--cusip` |
| R4 | F7 widened: target left in `upcoming` prints PRE-PRINT at rc 0, also under unknown types | No grade results; caveat above governs |
| R5 | One blank Yes/No on any coupon row refuses every grade in the run, no override | Yes, as a refusal. The one route to a false refusal. 0 blanks in 162 live and 2,800 history rows; same-day state unobserved |
| R6 | "Only adds refusals" was too broad: F4 also turns empty-old-key refusals into grades on the new-name values; the FRN list can drop a bystander unnamed | No false registered grade found |

**Corrections to my disposition:** AC3's "docket rc 2" holds on coupon rows only (R1). "Unknown types refuse" holds on the `auctioned` path, not pre-print (R4). A false GAP can be re-graded the same day only if the feed heals (R5). "Only adds refusals" is replaced by R6's wording.
