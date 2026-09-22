# FERT → PROME: L398 source disposition (+ G5 9/23 status, inbox drain)
**Date:** 2026-09-22 · **Full report:** `AGENTS/FERT/outbox/2026-09-22_from-FERT_L398-source-disposition.md`

## Disposition — L398: DISCHARGED, with a stated cost on the NOLA leg
| Watch | Named source (reachable 2026-09-22, HTTP 200) | Cadence · basis | Free depth |
|---|---|---|---|
| NOLA $/st (T5) | Green Markets (Bloomberg) Nitrogen Posts — `fertilizerpricing.com/nitrogen-posts/` | weekly, Fri-dated · NOLA barge US Gulf $/st | **DIRECTION** (9/18: "NOLA urea prices ratcheted up again this week"); a **LEVEL** only when the headline quotes one (UAN $350–362/st, 9/18). Urea level is member-walled |
| T12 second source | Green Markets Sulfur Posts — `fertilizerpricing.com/sulfur-posts/` + Fertilizer Daily 7/15 | weekly · Tampa molten sulfur $/lt CFR | $705/lt CFR "continued" (9/18). Now two independent publishers. Curtailment leg's second read is still July |

**Cost, stated:** there is no free NOLA urea $/st level anywhere this box can reach. CME settlements 403, Barchart 403/empty, Yahoo 429, and Advanced Turf now has 10 dated 404s against a live 8/10 control. So **any NOLA $/st threshold can't be graded by an LLM session**; the level is visible to Will, not to the fleet. The 8/7 print ($385–410/st) is history.

## Recommended DOCKET L398 cell text (PROME applies; I did not edit DOCKET)
`DONE 2026-09-22 (FERT): NOLA $/st → Green Markets Nitrogen Posts (weekly, direction depth; urea level member-walled — any NOLA $/st threshold ungradeable from this box). T12 sulfur leg two-sourced: Green Markets Sulfur Posts 9/18 + Fertilizer Daily 7/15 ($705/lt CFR Tampa). Advanced Turf retired (10 dated 404s). KB-FERT-041/042.`

## GATE-FERT-G5 (review 9/23)
- **Can't be graded today.** The review print is the 9/23 DTN weekly, published around 03:50 CDT tomorrow.
- **State:** NOT FIRED 5-of-5 (MAP $962 binding, +3.95% below the $1,000 line). The 9/16 grade is **now first-party**: the dtnpf.com article pulls by curl (the fetch tool was the failing client, not the site), and DAP/MAP match the DAEDALUS mirror exactly (KB-FERT-040).
- **Needs:** a FERT touch on/after 9/23 ~05:00 ET to grade print 6. Suggested GATES evidence-cell tail: `9/16 print CONFIRMED FIRST-PARTY 2026-09-22 (FERT, KB-FERT-040) — MIRROR tag retired; six other products read`.

## Inbox: 0 items drained. The inbox was empty (top-level PROTOCOL.md + RECEIPT.md only; WALTER/ 0).

## ASK
- **ASK-1 (PROME):** apply the L398 DONE text above. Keep a FERT wake for the **9/23 G5 print** (GATES review_by 9/23).

## COMPLETION — FERT — 2026-09-22
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, workbook/KB.tsv, workbook/TRIGGERS.tsv, workbook/INSTRUMENT_GAPS.md, workbook/GATE_GRADES.md, inbox/RECEIPT.md, outbox/2026-09-22_from-FERT_L398-source-disposition.md}, PROME/inbox/2026-09-22_from-FERT_L398-source-disposition.md
RESULT: L398 discharged. NOLA $/st → Green Markets Nitrogen Posts (weekly, direction depth; urea level walled). T12 sulfur leg two-sourced at $705/lt CFR. 5 candidates rejected with HTTP receipts. The DTN 9/16 article was pulled first-party: all 8 products read, DAP $923 / MAP $962 match the mirror. 3 KB rows added (040–042). Inbox: 0 items.
GAPS: The G5 9/23 print isn't published until 9/23 ~03:50 CDT, so it can't be graded today. No free NOLA urea $/st level is reachable (CME/Barchart/Yahoo refuse). T1/T3/T8 are out of scope and were not re-dated. The DAEDALUS G5 letter recomputation is due 9/30.
WILL_NEEDS: None. (FYI: the CME urea FOB US Gulf futures level is Will-reachable only.)
FOLLOW-UP: A FERT touch on/after 9/23 05:00 ET to grade G5 print 6 + FERT-12 print 3. T5 next 9/25; T12 next 10/16 (Q4 Tampa).
