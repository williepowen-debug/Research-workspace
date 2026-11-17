# BRENT SCRATCH — November 16 (live session for PROME prome-6f, 16:19–16:3x EST Monday; closed on PROME's ask, from `date`)

> **November 17 interim (PROME prome-19 wake, 09:44 EST, held open, not closed out):** Hormuz tanker hits change no line or gate → `research/2026-11-17_hormuz-tankers/NOTE.md`. CFTC browser identity removed from `cot_grade.py`. Owed: BRT-33 window today after 14:30 ET; outside-audit items 1–3 (BRT-23, BRT-22/28, BRT-26 scoring; packet still in inbox) by 11/20; review of the other browser-UA uses (`instrument_check.py`, `thresholds.py`, Baker Hughes probe) and LESSONS L25 against the Blocked sites rule. The full SCRATCH rewrite is owed at closeout.

## CHANGES SINCE LAST SESSION
- **Oil fell.** BZF27's [14:28,14:30) ET window VWAP was 92.4300 on 11/16, against 95.7853 on 11/13. Brent continuous was $92.16 (−3.84%) at 16:23 ET [vendor, contract UNKNOWN, not a settle]. Reuters' headline (unread) credits recovering Middle East exports and a surplus outlook.
- **Bahrain and Bab el-Mandeb (FALCON verified).** Iranian drone attempts on US radar sites in Bahrain on 11/13 and 11/15 were both intercepted, with no damage. The Houthis hold the Bab el-Mandeb shore after a government pullback on 11/15. FALCON's gate did not fire: its lowest traffic reading was 72.5%, against a 65% line.
- **Russia-Ukraine refinery campaign continues.** OSPREY rowed Omsk (11/11) and Volgograd (11/13). Nizhnekamsk was hit 11/15. Bloomberg titled "Russian Diesel Exports Drop" again on 11/16. Ships were hit near a Romanian Black Sea canal.
- **PortWatch's public ArcGIS feed now requires a token** (error 499).
- **WQ-696 (Will, today):** a finding sent for a trade assessment must state its implication, horizon, invalidation and unknowns, or say it supports no investment implication.

## WHAT I DID THIS SESSION
- **Graded G:GATE-BRENT-COT-35B vintage #14 (as-of 11/10) at the CFTC raw file: JOINT NOT-SPENT, 8th consecutive.**
  - Shorts 122,378 (−3,276); share 6.3823% (−0.2008 points).
  - Two pulls matched to the digit. Write-up: `research/2026-11-16_cot14/NOTE.md`.
  - PROME set review_by to 11/20, and sent the grade and my WQ-696 line to TERRY at 16:30 ET.
- **BRT-33 window 11/16: +4.5200, valid 6 of 7**, none under +3.50 (`research/2026-11-16_brt33/NOTE.md`).
- **Drained the inbox:** 6 items, 6 board_log rows = 6 `git mv`.
  - Diesel-export headlines and the Omsk/Volgograd rows are logged on combo:diesel-buffer as capacity, not barrels; not met.
  - Bahrain and Bab are logged on combo:yanbu-bypass.
  - PortWatch is logged on combo:gulf-flow-basis.
  - COR-20261116-09 receipted NO-OP.
- **PortWatch:** no registered BRENT read uses it. The NEXUS C35 Aug 31–Sep 1 rows are now UNREADABLE-AT-SOURCE (NEXUS_BRIEF).
- **Delivered:** record commit 73b48100a2; PROME packet ec5cdee876, consumed by PROME at the artifact.
- **Closeout:**
  - TRACKER lines 8 and 11 refreshed, stamped SCOPED-PARTIAL.
  - NEXUS refreshed (MIXED-VINTAGE). The 11/14 as-of line was rotated to `archive/NEXUS_BRIEF_as-of-chain_2026-11-16.md`.
  - STATUS refresh line updated.
- **Not done:** TSA 11/13–11/15. The diesel and refining commission (DOCKET line 783) was not touched, by instruction.

## NEXT SESSION (dated, future-verifiable)
1. **Every session through Friday 11/27, BRT-33:** copy `research/2026-11-16_brt33/pull.py` with the date changed. Valid 6 of 7; 8 needed by 11/27, or NO-VERDICT. Read the Thanksgiving 11/26–11/27 schedule when near.
2. **Wednesday 11/18 (modeled; verify at eia.gov):** WPSR week 11/13.
   - BRT-31 week six qualifies if the weekly print is at or under 8,890 kb/d.
   - BRT-34 second print.
   - Jet product supplied: the ground-stop dent is about 0.056 mb/d for week 11/13 and about 0.04 for Saturday in week 11/20, both inside noise; record only.
   - Combo reviews: gulf-flow-basis and paper-physical-gap (11/18); yanbu-bypass, diesel-buffer and gulf-access-cost (11/19).
3. **Friday 11/20:**
   - After 15:30 ET: COT #15 (as-of 11/17). Run `cot_grade.py --expect 2026-11-17` (plain client string since 11/17), cross-check the raw file with a second plain-string pull or CFTC Socrata 72hh-3qpy, and cite the row key in the commit subject. ⛔ Never a browser identity: a challenge or block means stop, use Socrata, tell PROME (root Blocked sites rule, WQ-701 G).
   - Same day: the diesel and refining commission, DOCKET line 783.
4. **Any session:** TSA 11/13–11/15 against the single-source 11/12 figure of 2,484,345. This machine gets 403 from tsa.gov.
5. **Thursday 11/19:** after the Trump–Xi bilateral and the trilateral, check for any Hormuz or Iran-export statement. Record only.
6. **Before Sunday 11/29 (OPEC+ January letter):** the IEA spare-capacity figure is still missing. Will's browser can read iea.org; OPEC's MOMR Table 11-1 is in Will's 11/11 PDF. The spare read stays CONTESTED: EIA 0.01 against Saudi-implied 1.2–1.3.
7. **Monday 11/30:** COT #16 (Thanksgiving delay; re-verify at the CFTC schedule).
8. **IEA December OMR Friday 12/11; OPEC MOMR Monday 12/14** (ask Will for the PDF).
9. **Any session:**
   - A Saudi statement of a pumping-station, line or Yanbu loading outage → BRT-32 read, an INCIDENTS row (primary-verified) and a TERRY packet the same session.
   - A laden-tanker loss with the cargo confirmed → BG-02 report, flag, stop.
   - A Houthi act at Bab against shipping → yanbu-bypass review.
10. **Housekeeping (carried):**
    - USO/observations.tsv: freeze or refresh.
    - The 11/13 Northeast heating-oil reserve CATALYSTS row is unresolved.
    - 7 INCIDENTS ACTIVE rows are past the 60-day re-verify budget.
    - The morning routine flagged a DXY basis break (futures page 404, spot used); re-source DXZ6 or re-base.

## OPEN THREADS / WATCHES
- 🟠 **COT Leg A is 4,052 above the NOT-SPENT floor** and has fallen four weeks running. A fall of 4,053 or more gives NO-VERDICT, which carries the same consequence. SPENT needs shorts at or under about 94,128 at the current OI (Leg B gating).
- 🟠 **Bab el-Mandeb shore under Houthi control.** This is a risk to Yanbu's Asia-bound exit, not a closure.
- 🟠 **Paper-physical gap.** Both conditions are met; the 11/18 review should say whether to close the theme.
- 🟠 **Spare capacity before 11/29:** CONTESTED.
- 🟠 **BRT-31 end states left:** MET, NO-VERDICT, NOT-FIRED-PRECONDITION or CONTAMINATED.
- 🟡 **PortWatch token:** whether to obtain one is noted by PROME for Will. I don't recommend it for C35 alone.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md). TERRY holds the #14 grade.

## MAIL STATE
- Inbox: clear in both lanes (6 consumed 11/16; 6 rows = 6 moves).
- Outbox: no BRENT packets outstanding. The 11/16 PROME packet was consumed by PROME at the artifact.

## WORKBOOK HEALTH
- COT_VINTAGES.tsv refreshed 11/16 (#14).
- LESSONS_INDEX.tsv +36 days, no lesson change owed. USO observations and INCIDENTS are stale (boot flag).
- No background process of mine is running.
