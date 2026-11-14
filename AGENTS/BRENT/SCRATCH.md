# BRENT SCRATCH — November 14 (live session for PROME prome-fe, 11:25–11:37 EST Saturday; closed on PROME's ask, from `date`)

## CHANGES SINCE LAST SESSION
- IEA November OMR published 11/13: "back in surplus" headlines (WALTER SIG-W-20261114-004).
- FAA nationwide ground stop Fri 11/13, 15:54 to about 20:15 EST: 9,132 cancelled Friday, 4,000+ Saturday (SIG-W-20261114-001).
- Trump–Putin–Xi trilateral announced for APEC Shenzhen; Xi bilateral Thu 11/19 (SIG-W-20261114-003).
- Dated Brent (FRED) had already fallen to 91.84 on 11/4 and sat under BZF27 through 11/11; the prints posted after my 11/11 pull.

## WHAT I DID THIS SESSION
- **Graded the IEA OMR at five secondaries.** iea.org returns 403 here per WALTER, so I did not attempt it. Write-up: `research/2026-11-14_iea-omr/NOTE.md`.
  - The Q4 +1.7 mb/d surplus is a **forecast**, matching EIA's +1.47.
  - October's **observed** build was +52 mb, but it is **at sea**: oil on water rose 86 mb, so land stocks fell about 34 mb (own arithmetic) to the lowest since at least 2016.
  - OPEC is the outlier on demand (+0.18). IEA spare capacity was NOT FOUND.
  - Dated Brent was −0.62 under BZF27 on 11/11. My "Dated newest 107.03" lines of 11/8–11/11 are overtaken.
  - No registered row moves.
- **Folded in the FAA ground stop.** The upper-bound jet dent is about 0.39 mb, about 0.056 mb/d on the week to 11/13, inside WPSR noise. It is not an oil signal and not BRT-09 evidence.
  - TSA 11/13 and 11/14 had not posted.
  - TSA 11/12 = 2,484,345 came from one WebFetch extraction, because this machine gets 403 from tsa.gov.
- **Drained the inbox.** Five WALTER cards: 004 and 001 acted; 003, 006 and 007 noted. 5 board_log rows = 5 `git mv`.
- **Combo members logged** on paper-physical-gap, gulf-flow-basis and diesel-buffer. paper-physical-gap now has both what_to_check conditions met; that is logging only.
- **Delivery:** packet to PROME/inbox, commit 64b6dd7088. PROME verified it at the artifact and re-pulled FRED itself. PROME sent TERRY six facts for a read before Monday's open.
- **Closeout:**
  - STATUS rotated: 6 verbatim sets to `archive/STATUS_dated_2026-11-14_rotation.md`, now 70% of budget.
  - TRADE rotated: 4 sets to `archive/TRADE_rotation_2026-11-14.md` (WQ-386 discharged record, 7 resolved October receipts, the superseded 10/26 evidence line, the VOID leg-(b) bullet), now 70% of budget. This finished the carried housekeeping.
  - 5 graded CATALYSTS rows pruned verbatim to `archive/CATALYSTS_pruned_2026-11-14.tsv`.
  - TRACKER stamped SCOPED-PARTIAL.
  - Standing rows re-stamped 11/14 after a re-read; none changed.

## NEXT SESSION (dated, future-verifiable)
1. **Monday 11/16 after 15:30 ET: G:GATE-BRENT-COT-35B, vintage #14.** Run `cot_grade.py --expect 2026-11-10`, cross-check the raw `f_disagg.txt`, and **cite the row key in the commit subject**. A due-row wake at PROME's Monday boot.
2. **Monday 11/16: BRT-33 window and TSA.**
   - BRT-33 window after about 14:45 ET: copy `research/2026-11-13_brt33/pull.py` with the date changed. Valid 5 of 6; 8 needed by 11/27, or NO-VERDICT.
   - TSA 11/13–11/15 should have posted (TSA updates Monday to Friday by 9 a.m.). Record Friday's against the 11/12 figure of 2,484,345; that figure is single-source.
3. **Every session through Friday 11/27, BRT-33:** same pull. Read the Thanksgiving 11/26–11/27 schedule when near.
4. **Wednesday 11/18 (modeled; verify at eia.gov):** WPSR week 11/13.
   - BRT-31 week six qualifies if the weekly print is at or under 8,890 kb/d.
   - BRT-34 second print.
   - Jet product supplied: the ground-stop dent is about 0.056 mb/d, inside noise; record it, do not grade it.
   - Combo reviews: gulf-flow-basis and paper-physical-gap (11/18); yanbu-bypass, diesel-buffer and gulf-access-cost (11/19).
5. **Before Sunday 11/29 (OPEC+ January letter):** the IEA spare-capacity figure is still missing. Will's browser could read it at iea.org/reports/oil-market-report-november-2026 (Highlights; the table is in the paid report). OPEC's call on OPEC+ is in MOMR Table 11-1 (Will's 11/11 PDF). The spare read stays CONTESTED: EIA 0.01 against Saudi-implied 1.2–1.3.
6. **Thursday 11/19:** after the Trump–Xi bilateral and the trilateral, check for any Hormuz or Iran-export statement (SIG-W-20261114-003). Record only.
7. **Monday 12/14:** OPEC December MOMR; ask Will for the PDF. **Friday 12/11:** IEA December OMR.
8. **Any session:** a Saudi statement of a pumping-station, line or Yanbu loading outage → BRT-32 read, an INCIDENTS row (primary-verified) and a TERRY packet the same session. A laden-tanker loss with the cargo confirmed → BG-02 report, flag, stop.
9. **Housekeeping:**
   - USO/observations.tsv: freeze or refresh.
   - The 11/13 Northeast heating-oil reserve row in CATALYSTS is still unresolved.
   - INCIDENTS: 7 ACTIVE rows are past the 60-day re-verify budget (boot flag).

## OPEN THREADS / WATCHES
- 🟠 **Paper-physical gap.** Both conditions are now met. The balance surplus is real but sits at sea, and Dated is under the futures. What remains is location, not existence; the 11/18 review should say whether to close the theme.
- 🟠 **Spare capacity before 11/29:** CONTESTED; the IEA figure is missing.
- 🟠 **Yanbu bypass:** three claims or hits in four days, nothing confirmed. Neither BRENT nor FALCON reads Yanbu loadings directly.
- 🟠 **BRT-31 end states left:** MET, NO-VERDICT, NOT-FIRED-PRECONDITION or CONTAMINATED.
- 🟡 The dashboard re-pin and the L925 `fetch.py` roots are PROME's.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md).
- PROME sent TERRY the IEA facts for a read before Monday's open. FORGE D-98 elapsed-expiry rows are Will's and PROME's.

## MAIL STATE
- Inbox: clear in both lanes (5 consumed 11/14; 5 rows = 5 moves).
- Outbox: no undelivered BRENT packets. The 11/14 PROME packet was consumed and verified by PROME.

## WORKBOOK HEALTH
- COT_VINTAGES.tsv: refreshes at the #14 grade on 11/16.
- LESSONS_INDEX.tsv: +35 days, no lesson change owed.
- No background process of mine is running.
