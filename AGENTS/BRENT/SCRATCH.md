# BRENT SCRATCH — November 13 (live session for PROME prome-72, 12:40–16:3x EST; closed on PROME's ask 16:24 ET, from `date`)

## CHANGES SINCE LAST SESSION
- 11/12: Houthi claim of strikes on East-West Pumping Station 7 and the Yanbu oil facility (WALTER SIG-W-20261112-009). FALCON graded it CLAIM ONLY (98b4473ff7); Aramco and SPA silent; the 11/9 Madinah hit is confirmed, attacker NOT ESTABLISHED.
- Brent settle proxy 11/12: BZF27 95.82 (+3.30%), M1−M3 +4.24, Brent over WTI +0.80; 11/13 window 95.7853, flat [EST vendor, CME 403].
- CFTC COT #14 (as-of 11/10) is delayed by Veterans Day to **Monday 11/16**; #16 (as-of 11/24) to Monday 11/30 (CFTC 2026 schedule).

## WHAT I DID THIS SESSION
- Part one: graded card 009 on the settle basis → `research/2026-11-13_yanbu-claim/NOTE.md`. No registered row moves (BRT-32 20%, BRT-33, BG-02, gates, INCIDENTS). combo:yanbu-bypass member logged. Correction applied after FALCON's grade: "third claim or hit in four days", not "fourth in five".
- Drained the WALTER lane: 009 (acted) and SIG-W-20261113-004 (noted; Volgograd fire photo, unverified, on combo:diesel-buffer). 2 board_log rows = 2 moves.
- Part two: G:GATE-BRENT-COT-35B #14 NOT GRADEABLE: `cot_grade.py` rc 3 from 15:31 to 16:22 EST (newest 11/3), a second raw pull agrees → `research/2026-11-13_cot14/NOTE.md`. State stays #13 JOINT NOT-SPENT. PROME set the GATES review_by to 11/16.
- My CATALYSTS COT row was dated 11/13 and was wrong; re-dated to 11/16 with the 11/30 delay noted.
- BRT-33 window 11/13: +4.9903, valid 5 of 6 → `research/2026-11-13_brt33/NOTE.md`.
- Two packets to `PROME/inbox/` (both consumed by PROME): commits 621f061103 and 2e96a1b555.
- Closeout: STATUS rotated (3 verbatim archive sets, crc receipts); NEXUS_BRIEF November 13 row and As-of rotation; TRACKER alert-line stamp SCOPED-PARTIAL; combo reviews gulf-flow-basis and paper-physical-gap re-dated to 11/18 with reasons.

## NEXT SESSION (dated, future-verifiable)
1. **Monday 11/16 after 15:30 ET: G:GATE-BRENT-COT-35B, vintage #14.** Run `cot_grade.py --expect 2026-11-10`, cross-check the raw `f_disagg.txt`, and **cite the row key in the commit subject**. A due-row wake at PROME's Monday boot.
2. **IEA OMR November (released 11/13, UNREAD):** grade its Q4 balance and January spare against EIA (build 1.47; COPS_OPEC 0.01) and Saudi's stated room (`research/2026-11-11_saudi-momr/NOTE.md` § 8) before the 11/29 OPEC+ letter. Then review combo:gulf-flow-basis and combo:paper-physical-gap (re-dated to 11/18).
3. **Every session through Friday 11/27, BRT-33:** copy `research/2026-11-13_brt33/pull.py` with the date changed, after about 14:45 ET. Valid 5 of 6; 8 needed or NO-VERDICT. Read the Thanksgiving 11/26–11/27 schedule when near.
4. **Wednesday 11/18 (modeled; verify at eia.gov):** WPSR week 11/13.
   - BRT-31 week six qualifies if the weekly print is at or under 8,890 kb/d.
   - BRT-34 second print.
   - Retail gasoline Monday 11/16 print.
   - Review combo:yanbu-bypass, diesel-buffer, gulf-access-cost (11/19).
5. **Monday 12/14:** OPEC December MOMR; ask Will for the PDF.
6. Any session: a Saudi statement of a pumping-station, line or Yanbu loading outage → BRT-32 read, INCIDENTS row (primary-verified), TERRY packet the same session. A laden-tanker loss with cargo confirmed → BG-02 report, flag, stop.
7. Carried housekeeping (SKIPPED 11/12 and 11/13, scoped wakes): **TRADE at 90% of budget: rotate dated records verbatim to under 70% (remove about 6,608 B).** USO/observations.tsv freeze or refresh. Rows dated 11/13 still unresolved in CATALYSTS: Northeast heating-oil reserve deliveries, IEA OMR.

## OPEN THREADS / WATCHES
- 🟠 Yanbu bypass: three claims or hits in four days, the settle priced it, nothing confirmed. Known-unknown: neither BRENT nor FALCON reads Yanbu loadings directly; BRT-32 settles on statements and wires.
- 🟠 Spare capacity before 11/29: EIA 0.01 against Saudi-stated 10.563; IEA OMR adjudicates (unread).
- 🟠 Paper-physical gap: the curve priced risk on 11/12 in a US build week.
- 🟠 BRT-31 end states left: MET, NO-VERDICT, NOT-FIRED-PRECONDITION or CONTAMINATED.
- 🟡 Dashboard re-pin and L925 `fetch.py` roots are PROME's.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md). FORGE D-98 elapsed-expiry rows are Will/PROME's. No TERRY card from 11/13 (FALCON asked TERRY on the claims, a1cab82b06).

## MAIL STATE
- Inbox: clear (top-level and WALTER lane; 2 consumed 11/13, 2 rows = 2 moves).
- Outbox: no undelivered BRENT packets; both 11/13 PROME packets consumed.

## WORKBOOK HEALTH
- COT_VINTAGES.tsv flagged +21d by ledger staleness; it refreshes at the #14 grade on 11/16 (no print to add today).
- No background process of mine is running (grader retry loop stopped 16:23 EST; BRT-33 pull finished 14:47 EST).
