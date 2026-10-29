# Five-desk self-sweep — combined view (2026-10-21, session af287aee)

**Origin:** Will 09:16 ET asked RED, BROCK, LABOR, FERT and OZK (idle after their WQ-465 wakes) to sweep their own files and report everything owed, incomplete, broken or missing, report-only. All five returned by 09:19 ET. PROME checked each report and packet at its commit.

| Desk | Report (commit) | Items | 🔴 / 🟠 / 🟡 |
|---|---|---|---|
| RED | `AGENTS/RED/reports/2026-10-21_self-sweep.md` (25f8c5d4e) | 25 | 2 / 9 / 14 |
| BROCK | `AGENTS/BROCK/reports/2026-10-21_self-sweep.md` (4958c8748) | 28 | 1 / 11 / 16 |
| LABOR | `AGENTS/LABOR/reports/2026-10-21_self-sweep.md` (2b0c898cc) | 28 | 5 / 8 / rest |
| FERT | `AGENTS/FERT/reports/2026-10-21_self-sweep.md` (5819048a8, 74ffebe6e) | 15 | 3 / 3 / 9 |
| OZK | `AGENTS/OZK/reports/2026-10-21_self-sweep.md` (508214fc0) | 36 | 4 / 10 / 20 |

**PROME correction to a desk report:** OZK lists "Q3 grade not routed to TERRY" as 🔴. PROME routed it at 09:05 ET (43d62dc4a, `AGENTS/TERRY/inbox/2026-10-21_from-PROME_OZK-Q3-stage1-grade.md`), so that item is closed.

## A. Decisions only Will can make
1. **FERT nitrogen re-open grading.** The rule keys on India's AWARDED tender price, which free sources never publish, and the NOLA backup series was retired. Options: (a) treat counter-offers as the award, which changes the rule's wording (a gate change); (b) buy a paid feed (spend); (c) keep grading it as a labelled inference. PROME rec: **(c) until the trade is live again.**
2. **OZK → REGINALD 6.14% packet.** The only live consumer of the superseded 6.19% figure is REGINALD `CALENDAR.md:63`. The other 28 checker hits are other series or commit-log dumps. Rec: **send it.**
3. **LABOR card capacity.** The JOLTS Sep (freeze 10/27) and NFP Oct (freeze 10/30) cards carry the two legs of the labor thesis's kill rule; ECI (10/23) and Challenger (10/29) are also unbuilt. Rec: **build them today while LABOR is idle,** since cards are pre-registration and need no data.
4. **Will's hands:** FFIEC login renewal by Thu 11/5 (needed for OZK's Q3 Call Report pull); Quartr re-sign-in (OZK's call transcript). ⚠️ CORRECTED 2026-10-28 (WAL packet, 10/28 catch-up): not a sign-in — the Quartr connector was signed in as Will on 10/28 and refused with "Quartr Pro subscription required" (plan: none); Quartr was DECLINED under WQ-220 (preserved at WQ-298), so no re-sign-in can help and no Will-hands item exists here. WALTER recorded "Quartr needs Pro" 10/23.

## B. Cheap fixes each desk can do now (PROME rec: direct all)
- **RED:** receipt the 6 R1 corrections; re-hash the two drifted boot files (CLAUDE.md, corrections_boot_check.py); replace STATUS's stale priorities and its pre-10/20 SELL wording.
- **BROCK:** receipt the 2 R1 corrections (the checker blocks on them); name the filing behind the frozen CFG $12.852B figure (REGINALD and GIBBS are waiting); track DOCKET L186 in STATUS.
- **LABOR:** add LAB-08 to the STATUS predictions table; refresh the six-week-old Florida claims row in the NEXUS brief (Florida is Will's top-priority geography); fix the stale charter figures.
- **FERT:** refresh VX-02/VX-05 (MAP $979 → $981; India's award cell); rotate TRIGGERS.tsv before its next append.
- **OZK:** update the boot script's Q2 check items to Q3 (they read as overdue from tomorrow); trim STATUS (79% of budget).

## C. Already scheduled — no new direction needed
- RED: the bank Q3 tree grade, Thu 10/22 after the 10:00 ET EGBN call (DOCKET L35).
- BROCK: the CRMT L740 read, Thu 10/22 PM, which also finalizes L652.
- LABOR: the claims grade, Thu 10/22 08:30 ET (L719).
- OZK: the Stage-2 call read by Sat 10/31 (L520).
- FERT: G5 print 11 and the IPL follow-on tender, 10/28.

## D. Larger items to schedule
- BROCK BRK-31 bank reads (WAL, OZK, BKU, SSB overdue; EGBN after its print; AMTB 10/22): one session after Thursday's CRMT read.
- OZK conviction re-grade after the call read; OZK-09 stays STUCK until the call or the 10-Q discloses a RaDD reserve.
- LABOR BD-35 (a guard that checks a release against the saved original) and BD-23 (unscheduled-event summons; PROME half).
- RED CHG-049 / VX-009 review (141 days unreviewed).
- Charter and file size: LABOR's charter is at 163% of the read cap; RED's charter at 85%; BROCK and OZK STATUS are near their 75% triggers.

## E. PROME's own items from the sweeps
- DOCKET rows for FERT's dated triggers T2 (USDA ERS outlook, 10/25, a Sunday — date unverified), T11 and T13. FERT's T3 (Oct CPI) rides a row dated 3 days after the print.
- A tracking row for OZK's conviction re-grade.
- LABOR BD-23: the summons gap's PROME half.
