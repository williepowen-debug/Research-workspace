REJECT — 1 blocking finding (❌), 3 non-blocking (⚠️)

# Independent read 2: forecast scorer fix diff only (6348385696 to c5aec45139)

Reader: the same independent, read-only Opus reader as read 1. Date 2026-11-17 (ET). Scope: `git diff 6348385696 c5aec45139 -- PROME/tools/forecast_report.py`, which is is_decided, same_call/current_call, and skipping a version with no status or confidence column. The seven read-1 residue flags are not re-raised.

Read-1 findings now: ❌1 is fixed (CRL-21 is back in the forward table: 23 BEFORE, 249 closed). ❌2 is fixed for every real case (restarted: BRENT BRT-27, BRT-28, LABOR LAB-01, LAB-02; first-logged values 0.70, 0.85, 0.65 now belong to the call scored). ❌3 is fixed (fx1 BR-1 now reads BORN-DECIDED). Over all 272 scored rows, old against new, 11 rows change. All 11 are explained by the three fixes (scratchpad/probe5.py).

## ❌ 1. A terminal status that does not begin RESOLVED is now read as open, and a real born-decided row flips to BEFORE
- **Claim:** is_decided docstring: an UNMAPPED status "counts as decided only when its token begins RESOLVED". Acceptance A1: a row whose earliest record is already decided is BORN-DECIDED.
- **Exact artifact:** forecast_report.py, is_decided (new lines about 225 to 229), used at the file_history append. Real row: ZHAO ZHA-09. Its first committed version is c1ea0e3244 (2026-07-09 17:35 ET), with Status "LIKELY MISSED", Date_Resolved 2026-07-04, a filled Outcome cell, and Notes "BACKFILLED 2026-07-09 … never written to this workbook". This is the audit's own case: the row was logged after its outcome. The live row's owner date is now 2026-08-21. Fixture fx3 row Z-9 has the same shape: committed 2026-11-10 already "LIKELY MISSED" with its own resolved date 2026-11-07, then regraded "RESOLVED NO" 2026-11-14 with the owner date moved to 2026-11-14.
- **Verification command:** scratchpad/probe5.py (old and new timing() over every scored row, plus a variant that counts terminal-looking UNMAPPED tokens as decided). For fx3: `FORECAST_REPORT_ROOT=/tmp/tmp.AMnMa22CRv/fx3 python3 PROME/tools/forecast_report.py` run from inside fx3, plus scratchpad/dump.py.
- **Observed result:** ZHA-09 was BORN-DECIDED (known 2026-07-09) under 6348385696 and is BEFORE (known 2026-08-21) under c5aec45139. It sits in the closed population, so today's printed table is not affected. fx3 Z-9 is in the forward window and prints as BEFORE. The correct class is BORN-DECIDED, and BEFORE rows are not listed. Terminal tokens of this shape are in current ledgers (read 2026-11-17): VIOLET KILLED ×2, HENRY GRADED-MIXED, HAWK DEFECTIVE-INSTRUMENT.
- **Proposed change (tested on real history, read only):** in a committed version, also count an UNMAPPED status as decided when that version's own resolved-date cell holds a date. Over the real history this splits cleanly. Open-type tokens never carry a date in the resolved-date column: STUCK (19 versions), AT-RISK, RESOLVING, UNQUANTIFIED, and FROZEN-PENDING in REG-09 all have an empty cell. Terminal ones do: LIKELY MISSED (9), GRADED-MIXED (51), WRONG, CORRECT, DEFECTIVE-INSTRUMENT. The one ambiguous token is FROZEN-PENDING with a date (44 versions, REGINALD REG-02 and others), which the earlier tool also counted as decided. Separately, make the known date the earlier of the live owner date and the earliest resolved date any committed version carried. ZHA-09 then has known date 2026-07-04, which is before its first record. Add fx3's Z-9 as a selftest case.

## ⚠️ 2. A reused ID whose two calls share a template still reads BEFORE (not blocking)
- **Claim:** same_call: a different call needs the first 12 words to have similarity under 0.5.
- **Exact artifact:** same_call (new lines about 236 to 250). Fixture fx3 row T-1: "The 5Y auction on 2026-11-04 … at or above 2.40", Date_Made 2026-11-01, OPEN 60%. It is overwritten in place on 2026-11-12 by "The 7Y auction on 2026-11-10 … at or above 2.50", Date_Made 2026-11-12, already HIT, owner date 2026-11-10.
- **Verification command:** fx3 run as above. On the real repository I took same-desk pairs of different live IDs and computed their first-12-word similarity.
- **Observed result:** T-1 is not restarted and reads BEFORE (value date 2026-11-01, known 2026-11-10), although the scored call was logged two days after its outcome. Among real same-desk pairs of different calls, 120 of 8,556 score 0.5 or more. Examples: BOND BND-15 against BND-22 score 1.0, and BND-18 (5Y auction) against BND-20 (7Y auction) score 0.67. No real reuse is missed today.
- **Proposed change:** also treat the row as a different call when the text changes at all and Date_Made moves. On the real repository this restarts exactly the same 4 rows and no others: the SAM and BROCK Date_Made corrections keep identical text, and the FALCON pointers keep their Date_Made. It would catch T-1. Alternatively, declare the limit in the "Row ID reused" line.

## ⚠️ 3. A same call can be listed as "reused" and read BORN-DECIDED (safe direction, not blocking)
- **Exact artifact:** fx3 row P-1: "Fed cuts in December" at 40%, decided HIT 2026-11-10. On 2026-11-12 its text is replaced by an archive pointer and the value is re-marked to 60% in the same commit.
- **Observed result:** P-1 is restarted, listed under "Row ID reused or call rewritten", and reads BORN-DECIDED. It is the same call, so both labels are false, though the timing flag still fires. No real row has this shape today: the restart list is the 4 true rows.
- **Proposed change:** none required. Optionally, do not count a pointer-style text ("RESOLVED HISTORY", "archive/") as a different call.

## ⚠️ 4. A version with no confidence column is skipped even when the probability is in the prediction text (safe direction, not blocking)
- **Exact artifact:** the skip at the file_history header check. fx3 row C-1 (CYPHER) is logged 2026-11-01 with "P(TRUE) = 0.60" in its Prediction cell and no Confidence column. The column is added in the decision commit on 2026-11-12.
- **Observed result:** C-1 reads BORN-DECIDED although the call was committed 11 days before. A whole ledger with no confidence column would read NO-GIT-RECORD for every row; that is listed, never counted as BEFORE. Real effect today: 0 rows (probe5: no class change from this cause; NO-GIT-RECORD over all history is 0). This follows the acceptance's own neighbour rule, so I note it only.

## fx1 and fx2 against c5aec45139 (each row now reads)
- **fx1:**
  - A-1 SAME-DAY
  - A-3 BEFORE in the forward table (was closed population): fixed
  - A-4 BORN-DECIDED (listed twice: same-file repeat, residue)
  - A-5 BEFORE (restored value, residue)
  - A-7 AFTER
  - A-8 BEFORE (committer date, residue)
  - X-9 AEOLUS BEFORE
  - X-9 WATT BORN-DECIDED
  - BR-1 BORN-DECIDED (was BEFORE): fixed
  - B-1 BEFORE (live wins)
  - B-2 BEFORE
  - B-3 BORN-DECIDED
  - Restarted: none (correct)
- **fx2:** R-1 BORN-DECIDED, restarted and listed (was BEFORE): fixed.

**Ran:** selftest (PASS 40, rc 0); live run (rc 0; 23 BEFORE, 249 closed, 4 restarted, LOOK 2); fx1, fx2 and the new fx3 (/tmp/tmp.AMnMa22CRv/fx3); probe5 (old against new over all 272 scored rows); the same-desk template similarity scan; the scan of resolved-date cells by status token; the tighter same_call variant on real history.

**Only read:** the restart covers only versions after the last change (current_call walks back over adjacent versions only), and the selftest cases for the new functions; I read these, and the fixtures exercised them only indirectly.

No repository file was edited, staged or committed except this ledger. Other desks' uncommitted work seen in `git status` (FALCON, LIQUID) is not mine.
