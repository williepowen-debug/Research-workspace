# BOND SCRATCH — 2026-11-25 standard closeout (laptop, PROME prome-77 due-row wake, DOCKET L1238)

> STATE AT WRITING (13:3x ET 11/25): Composite **18/35** (5+3+2+4+1+1+2; row 4 HY function 3 → 4). **Clean-nominal counter 1**; auction health 3. Outside composite: VX-BND-13=3 (from 2), 15=2, 16=4, 17=1, 18=2, 19=3, 20=2. **OPEN predictions 3 (BND-35 to 37), earliest resolution 12/17; BND-34 TRUE 11/19.** Position **FLAT** (FORGE 10/30; last broker capture 10/30). Latest cells: Treasury 2Y/10Y/30Y 4.63/4.91/5.30 [11/24]; real 10Y 2.79 [11/24]; 5Y5Y 2.13 [11/24]; HY/CCC/IG 372/1405/98 [11/24]; SOFR−IORB +4bp [11/24]; PMMS spread 229bp matched [11/25]; FR2004 long-end $150.4B [as-of 11/11]; FHLB ratio 3.6 [9/30]. THESIS v1.2.13, token unchanged.

## WHAT I DID

- **Boot:** root CLAUDE.md (4 pages), USER.md (3), AGENTS.md (1), BOND CLAUDE.md (6) read with `PROME/tools/boot_read.py` to eof; STATUS, SCRATCH, MEMORY, CLOSEOUT read. Claude Code `claude-opus-5-5`, laptop. No pull: the shared tree carries PROME's staged files and HOMER's uncommitted files, and origin had nothing new (local ahead 1, PROME's). docket_check rc=0 (verified through 12/1, blind span 12/2–12/16 UNVERIFIED; the 12/7 row exists). corrections rc=1 → four NO-OP receipts → rc=0. boot_recompute rc=1: FR2004 vintage drift (STATUS/NEXUS/SCRATCH fixed by rewrite; THESIS lines are dated history, left) and T5YIFR distance (fixed).
- **Grades (my grader, registered bars):** TIPS 11/19 CLEAN · 2Y 11/23 I′ FIRE −3.13pp · 5Y 11/24 I′ FIRE −5.14pp, OLD indirect −0.03pp, dealer not met (residual) · 7Y 11/25 CLEAN +0.77pp, cover +0.01. Shares re-derived from TA_WS raw fields, identical. Counter 2 → 0 → 0 → 1. KB-BND-592 to 596.
- **VX-BND-13 2 → 3** by its own written note (single auction below the 12-auction low → 3; 4 needs dealer above max): 3Y 11/9, 10Y 11/10, 5Y 11/24. The 3 applied from the 10Y grade and BOND missed it then; graded today. Its red text reads as met; conflict to PROME.
- **Closeout runner note:** the composite change 17 → 18 was first declared with `--superseded 17/35 18/35`; the scan matched only dated history (75 own hits in closeout transcripts, dated analysis files, KB rows, CHANGELOG; cross hits in logs and dated reports, plus DAEDALUS `FLEET_MAP.tsv` row dated 11/18). History is not rewritten, so the passing run does not declare it; disclosed here and in the PROME memo.
- **HY above 350** since 11/19 (352, 376, 363, 372): HY function 3 → 4, BND-34 TRUE, composite 17 → 18 (KB-BND-597). Late by six sessions (dark).
- **Clock check on the 2Y:** high 4.700 vs par close 4.63 both bracketing days; 2026 median gap 3.4bp; ZT=F rose about 3bp of yield after 13:00. No cheap-clearing claim made.
- **FR2004:** as-of 11/11 $150.4B (−0.3). Found the as-of 10/21 cell revised to 138.0 from 150.816 first-published. KB-BND-598.
- **WQ-735 (PROME packet):** switched 2 scripts (`monitors/rates_context.py` lines 373 and 491, `monitors/dm_cross_section.py` line 48) to `research-bot/1.0`; ran each once: Fed calendar page HTTP 200 and 56 meetings parsed (not re-recorded), ACM file parsed (0.6518 [11/24]), ECB, BoE and MoF legs parsed; rates_context selftest 57/57. Refusals: none.
- **TERRY ask (TRY-FIRE-004):** BOND's share graded MIXED (KB-BND-601), packet `AGENTS/TERRY/inbox/2026-11-25_from-BOND_try-fire-004-thesis-grade-and-auction-week.md` with a no-card read of the auctions and HY. PROME's brief named TRY-FIRE-006; the TLT 77P card is 004 (006 is the Kharg/USO card, BRENT/FALCON/RED).
- **Theme opened:** `combo:treasury-dealer-exits` (KB-BND-600), first member Commerzbank title (card 20261124-018 item 12).
- **Docket:** 13 fired rows archived with outcomes; new rows 11/27 (FR2004 as-of 11/18) and 12/3 (BOND wake: WQ-291 grade, December refunding bar freeze, F2 12/2 read, 12/9 curve-shape row); VX-BND-20 review re-dated 11/25 → 12/3.
- **Stale KB:** 10 rows past Stale_By flipped to STALE by their own date, 0 refreshed.

## NOT MOVED

No level, operator, instrument or consequence changed. Auction health held 3. Token unchanged. THESIS untouched (no thesis-level change; its FR2004 lines are dated history).

## NEXT SESSION (dated)

1. **12/3 after 16:15 ET (needs a PROME wake):** WQ-291 dealer leg on FR2004 as-of 11/25 (3–6Y, PRE as-of 11/18, MET iff +$8.6B) · freeze bars for 3Y 12/7, 10Y-R 12/8, 30Y-R 12/10 on announcement · F2 read of the 12/2 op · 12/9 curve-shape row with a base rate · VX-BND-20 review.
2. **About 11/27:** FR2004 as-of 11/18 (PRE cell; first with the refunding settlement).
3. **HY:** verify the pulled-deal leg (weekly HY primary count) now that HY is above 350.
4. 12/8 F2 read; 12/9 FOMC; 12/17 BND-36; 12/27 re-record the FOMC calendar.
5. Quiet session: blind span 12/2–12/16 against the Treasury QRA by hand; Bund and WQ400; VX-BND-06 proxy; rewrite VX-BND-13 so one text governs once Will rules.

## OPEN THREADS

VX-BND-13 red-vs-notes conflict (with PROME). FR2004 10/21 revision cause unchecked. Japan intervention funding (custody +$19.8B [11/18], LIQUID's pool −$19.4B: reallocation into Treasuries, inference). True CDX, pulled-deal census unchanged. WQ291 funding window UNGRADED.

## STATED NO-OPS

THESIS/CHANGELOG (no thesis-level change) · TRADE.md (no gate state or position change) · FLOW (no channel change) · MEMORY (no new BOND lesson: the late VX-BND-13 is the existing "audit surfaces by age" lesson).

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Sent: TERRY packet (above); WALTER signal `AGENTS/WALTER/inbox/2026-11-25_from-BOND_month-end-auction-grades-and-hy-350.md`; PROME memo `PROME/inbox/2026-11-25_from-BOND_l1238-auction-grades.md`. RED: no reply (agree with its FT-11 grade). LIQUID 11/20 custody figure reproduced. Not pushed (PROME pushes).
