# Production Review #10 — Reader F (cohort: OTTO, CORAL, MARCO, AEOLUS, HOMER, CRUISE)

**Reader:** read-only subagent for DAEDALUS · **Written:** 2026-11-18 (started 10:29 EST by `date`) · **Pinned cutoff:** `208bd704ea5d8f6cf1561cd6f8d757c06db84339` (2026-11-17 22:41 ET, PROME evening closeout) · **Period:** 2026-11-02 00:00 to cutoff · **Working tree at read:** `29a370742c`. Post-cutoff commits touching the cohort: HOMER 1, others 0; no cohort path dirty in the working tree. All desk files read at the cutoff with `git show 208bd704ea:<path>`. Nothing edited, staged or committed except this file.

Ladder used: `AGENTS/DAEDALUS/OPERATIONS.md` § MATURITY LADDER (floor L0 skeleton, L1 STATUS plus a current-judgment section under reading B, L2 structured record accruing; Market L3 convergence matrix + exit rules + predictions resolving + dated falsification surface; Market L4 TRADE surface under reading A (feeds proposals, OR declared flat/frozen with an explicit unfreeze or re-arm condition, OR no book by charter and signals demonstrably reach a consumer); L5 clean closeouts, current, mechanical-QC leg N/A). All six desks are Market class.

---

## OTTO (Market, map L5 / M, last scored 2026-10-21)

### (a) Commits in period
**45** touching `AGENTS/OTTO/` (`git log --after='2026-11-02 00:00' 208bd704ea -- AGENTS/OTTO/`), of which about 25 are OTTO's own; the rest are WALTER card routes, PROME packets, BROCK and DAEDALUS fleet packets. Sessions s041 to s047. Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | THESIS v1.6 (target was October 30, six days late): Carvana sub-thesis DORMANT, borrower exit re-labelled an unverified hypothesis (CATO OT1), SDT noise limit | `4e765ec131`; `thesis/THESIS.md:3-4` |
| 11/05 | Matrix V5 moved 2 to 1 together with its named source cell (THESIS conviction LOWER to DORMANT); composite now 32/50 | `208aa62874` (V5 row diff) |
| 11/05 | OTTO-36 and OTTO-37 registered; OTTO-37 graded FALSIFIED 11/06 on Manheim 206.8 | `99ca8d3c5a`, `35f4848865` |
| 11/06 | WALTER cards 051 and 052 applied (Hertz Class B refusal at Ex. 10.2), corrections COR-20261106-35/-51/-52 receipted | `f04e92eca7`, `3042ad4ca0`, `02a9395268` |
| 11/11 | s044 closeout: research retirement scan, 15 files over 60 days moved to `archive/research_retired_2026-11-11/` with README; consumer check run, two reds dispositioned as false | `bdb6249406` |
| 11/12-11/13 | D:L1125 (EART 2026-5 absent, halt candidate not a halt) and D:L1098 (CRMT twelfth bridge, V9 held at 4 by rule) graded and delivered | `fa7277191c`, `4dfdf0f923`; `PROME/inbox/processed/2026-11-13_from-OTTO_L1098-crmt-v9-held-graded.md` |
| 11/13 | s046 closeout with checks listed (calendar mirror, weekday claim, brief pin, consumer, ledger nudge) | `4c95720b13` |
| 11/16 | s047 doorbell (PROME prome-c4): SDT second run NO VERDICT, First Brands sale hearing 12/09, SDART/BLAST October 5/5 worse YoY, STATUS rotation to STATUS_COLD §25 (24,291 B). Two packets delivered and consumed by PROME | `747b2e9b4c`, `c5a05d0f65`; `PROME/inbox/processed/2026-11-16_from-OTTO_*` (2 files) |
| 11/16 | PROME routes two outside-audit packets to OTTO (audit items; 8 stale KB rows), both unprocessed at cutoff | `303d5d1e20`, `7906bbcd10`; `AGENTS/OTTO/inbox/2026-11-16_from-PROME_*` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | OTTO-12 unlogged-October 1 premise superseded by October 19 forecast repair: OPEN subjective 25%, original 55% retained, VRM/private coverage gaps explicit | STILL-TRUE, but history; the row carries no current gap | `STATUS.md` PREDICTIONS OTTO-12 row (at cutoff) |
| G2 | §2 source-cell overlay exists since 10/14 | STILL-TRUE and now complete: all 10 matrix rows V1 to V10 name a `src:` cell first (count 10) | `git show 208bd704ea:AGENTS/OTTO/STATUS.md \| grep -c '\*\*src:'` = 10; matrix "One rule" header |
| G3 | s035 completed omitted closeout checks | OVERTAKEN — s041 to s046 closeouts record their checks in the commit body; s047 (11/16) is the open case (see d, L5) | `bdb6249406`, `4c95720b13` |
| G4 | October 30 thesis/cold read remains separate | OVERTAKEN — THESIS v1.6 landed 11/05 | `thesis/THESIS.md:3` |
| N1 | Retain L5/M bounded pending full source-cell transition verification | RESOLVED at structure (10/10 rows carry a source cell, scoring rule stated); each score against its source colour not re-checked row by row by this reader | G2 |
| N2 | Conf H needs a colour move with source and score together | MET ON ITS LETTER — V5 moved 2 to 1 on 11/05 in the same commit as its source cell moved LOWER to DORMANT | `208aa62874` V5 diff |
| N3 | Do not manufacture a missed-market-read finding from a bounded procedural closeout | STILL-TRUE as a caution; not a gap | — |

### (c) Proposed replacement cells

- **Gaps:** `All 10 convergence rows name their source cell; V5 moved 2 to 1 with its source on November 5 (THESIS v1.6, Carvana DORMANT). s041 to s046 closeouts recorded their checks; the November 16 s047 session delivered two packets to PROME but left LAST_COMPLETION, MEMORY and the NEXUS_BRIEF pin at s046. Two PROME outside-audit packets of November 16 (audit items including OTTO-06 and OTTO-09 scoring, and 8 stale knowledge-base rows) are unprocessed at the November 17 cutoff. STATUS PREDICTIONS rows OTTO-10, OTTO-11 and OTTO-12 carry glued words and numbers. TRADE.md FROZEN since July 4 with an unfreeze condition; signals reach BROCK, WALTER and PROME.`
- **Next_upgrade:** `Conf H needs a confirm-read after OTTO closes the s047 closeout surfaces and answers both November 16 audit packets; the colour-move condition is already met (V5, November 5). Profile needs a whole refresh (body September 5).`

### (d) Grade verdict — RETAIN L5 / M (Conf H condition met on its letter; raise withheld, confirm-read owed)

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `AGENTS/OTTO/CLAUDE.md` present |
| L1 STATUS + current judgment (reading B) | PASS | `STATUS.md` header Signal Status line and `## BOTTOM LINE` (s047, 11/16) |
| L2 structured record accruing | PASS | `workbook/ML.tsv` ML-388 to ML-394 added in period; `workbook/PANEL_10D.tsv` refreshed 11/16 (`747b2e9b4c`) |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS | matrix V1-V10 with up/down triggers; PREDICTIONS.tsv 5 CONFIRMED, 8 FALSIFIED, 7 OPEN, 1 STUCK, 1 NEEDS_VERIFY at cutoff; OTTO-37 graded 11/06; dated falsifiers (V1 "~8/2027", OTTO-36 resolves ~11/30) |
| L4 trade leg (reading A) | PASS | `TRADE.md:3,10` FROZEN 2026-07-04 with "Unfreeze only when a concrete OTTO auto trade re-emerges" (branch 2, a loose condition); branch 3 also holds: packets to BROCK, WALTER (`c5a05d0f65` correction to WALTER), PROME consumption |
| L5 clean closeouts, current | PASS WITH DEFECT, confirm-read owed | s041-s046 closeouts record checks (`bdb6249406`, `4c95720b13`). Defects at cutoff: s047 closeout surfaces stale (`LAST_COMPLETION.md` and `MEMORY.md` last touched `4c95720b13` 11/13; `NEXUS_BRIEF.md` pinned to s046 while STATUS changed 11/16 `747b2e9b4c`); glued text in STATUS PREDICTIONS rows OTTO-10/11/12 (e.g. "inH2-2026; resolve12/31", "OPEN25%") against the root Output Canon spacing rule |

### (e) Profile trigger
Profile body 2026-09-05 (§1-3, 6-8) and 2026-07-07 (§4-5), with bounded deltas 10/21 and 11/02 (`profiles/OTTO.md:1-11`). **Date-age: FIRED** (checkpoint 2026-10-20, `profiles/OTTO.md:11`). Content trigger "next post-CARL-sitting session": not checked (no CARL sitting found by a grep of CARL commit subjects since 9/05; ambiguous key). Content change since body: THESIS v1.6, Carvana DORMANT, STATUS_COLD now at §25, prediction set changed (OTTO-36/37), research retirement. **A bounded delta cannot carry it**; whole refresh owed, and the trigger itself should be re-cut (a CARL sitting is another desk's event with no stated occurrence check).

### (f) Cross-agent observations
- PROME: OTTO's two 11/16 audit packets (`AGENTS/OTTO/inbox/2026-11-16_from-PROME_outside-audit-items-verify-first.md`, `..._stale-KB-rows-retire-or-refresh.md`) are open at cutoff. On item 1 (OTTO-06 and OTTO-09 "scored though excluded"), the ledger rows keep their FALSIFIED / CONFIRMED status with an "EXCLUDED from calibration / NOT calibration-eligible" note (`thesis/PREDICTIONS.tsv` rows OTTO-06, OTTO-09); whether any scorer counts them was not checked here.
- OTTO: BROCK's 11/17 L1139 packet (thirteenth bridge) is in OTTO's inbox at cutoff; V9 re-colour waits on OTTO's next session (DOCKET L1186, WQ-709, due 11/18).
- OTTO / DAEDALUS: glued text persists in `thesis/PREDICTIONS.tsv` notes (OTTO-09: "February4,65%,Q1-Q2"), a WQ-560 class residue.

---

## CORAL (Market, map L4 / M, last scored 2026-10-21)

### (a) Commits in period
**63** touching `AGENTS/CORAL/`, of which **29** are CORAL's own (subjects `CORAL:` / `CORAL ->`); the rest are inbound packets (PROME 7, WALTER cards, MARCO 4, AEOLUS 2, REGINALD 2, CREED, FERT, DAEDALUS). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/06 | Four-row prediction ledger in use (CORAL-01 to -04, made 11/06); MSI #12 graded; seven FL bank 10-Qs grepped for association lending (zero disclosure); REGINALD BKU MIXED final carried | `cc1def0aea`, `e8d61dcfab`; `workbook/PREDICTIONS.tsv` |
| 11/09-11/16 | MSI readings #13 to #15 graded (4-of-5 each; Cape Coral 5.74 series low, re-fire fails) | `2a6252b7d8`, `8c9ef1ff6b`; `STATUS.md` § A State line |
| 11/16 | Falsify grade due 11/15 run one day late: 1.5 of 6, orange holds; WQ-690 A (any score below 2 reads orange) and WQ-691 A (downgrade candidate needs a full 4) encoded the same day | `b6c40d4565`, `648ac72436`, `3eaaa6439f`; `thesis/THESIS.md:4` |
| 11/16 | Stamp correction on the falsify grade (11:4x to 11:3x, clock read) | `e487a1b2f8` |
| 11/17 | **First forecast graded: CORAL-02 RESOLVED FALSE** at the first print (financed condo −8.34% vs SF −12.43%); WQ-704 financing research delivered; outside-audit item answered (section 3 of the reply) | `aa2ee5f29d`, `7c3aea3c26`; `PROME/inbox/processed/2026-11-17_from-CORAL_CORAL02-graded-WQ704-research-inbox.md:28-39` |
| 11/17 | Amendment 3 and floods impact read on Will's ask (REC 7/10 re-base); Palm Bay share corrected 66% to about 40-45% in a follow-up; CATO CR17-1 to CR17-4 adopted; NEXUS stamps corrected to wall clock | `e18a9fa73a`, `8870d4946a`, `4ca122d595`, `49dfc56c0a` |
| 11/17 | Two closeouts (afternoon on PROME's ask; evening) | `90fbe2e5e1`, `99be3d6dcf` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Forward log remains FROZEN | STILL-TRUE (banner FROZEN 2026-10-29, `CALENDAR.md` live) | `workbook/FL_Forward_Log.md:3` |
| G2 | Ocala row past date/value unread, owner follow-up | STILL-TRUE — owed item F "Ocala June-2026 metro UR ... 3 routes dead" | `STATUS.md` OWED TABLE row F |
| G3 | WQ-475 A logged and THESIS criteria 5/6 have dated pointers | STILL-TRUE, history; no current gap | `STATUS.md` § A2 |
| G4 | Criterion 6 November 15 read precedes November 17 certification and uses unofficial returns | STILL-TRUE and now sharper: the grade ran 11/16 on unofficial 61.98%, and certification was NOT CONFIRMED at 11/17 evening because the state results site blocks automated readers | `STATUS.md:4` header; § State fiscal pillar row |
| G5 | Four-row prediction ledger registered; no forecast graded | OVERTAKEN — CORAL-02 RESOLVED FALSE 2026-11-17; CORAL-01, -03, -04 OPEN (resolve 12/16 and 12/31) | `workbook/PREDICTIONS.tsv` Status column |
| N1 | Retain owner source tests and thesis-clock interpretation questions | STALE FORM — no named test or question; nothing a reader can check | — |
| N2 | PROME corrects forecast_report.py stale no-CORAL-ledger display note | RESOLVED at working tree — `PROME/tools/forecast_report.py` output lists CORAL with 4 rows, 1 resolved, and no CORAL ledger note (run at `29a370742c`, not at cutoff) | report line 49 |
| N3 | No new forward-log freeze request | STILL-TRUE, history; drop | G1 |

### (c) Proposed replacement cells

- **Gaps:** `First forecast graded: CORAL-02 FALSE on November 17 (first print); CORAL-01, -03 and -04 OPEN to December 16 and December 31. Falsify grade of November 15 ran a day late (1.5 of 6, orange holds) on unofficial Amendment 3 returns; certification not confirmed November 17 (state results site blocks automated readers). STATUS at 28,258 B (87% of budget) and MEMORY at 27,067 B (83%) are in the rotate tier; no READS.tsv declaration. Ocala June unemployment row still unread (three routes dead). Forward log FROZEN; CALENDAR is live.`
- **Next_upgrade:** `L5 requires clean, current closeouts verified by DAEDALUS: the November 16 and 17 sessions show a late grade, two stamp corrections and a same-day Palm Bay share correction (66% to 40-45%), so the window should start after STATUS and MEMORY are rotated below 70% of budget. Profile needs a whole refresh (body September 5).`

### (d) Grade verdict — RETAIN L4 / M

| Leg | Verdict | Basis |
|---|---|---|
| L0 | PASS | `AGENTS/CORAL/CLAUDE.md` (29,391 B) present |
| L1 (reading B) | PASS | `STATUS.md` `## BOTTOM LINE` dated 11/17 evening, with "What would change the read" |
| L2 | PASS | `workbook/PREDICTIONS.tsv` (4 rows, schema with Status/Date_Resolved/Outcome), MSI readings, `board_log.tsv` accruing |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS | GATE-CORAL-MSI-01 letter with re-fire/stand-down (`STATUS.md` § A); CORAL-02 resolved 11/17; dated falsify grade (next 2027-02-16, DOCKET L1156, `thesis/THESIS.md:4`). Convergence matrix form not re-checked by this reader (confirm-read owed) |
| L4 trade leg (reading A) | PASS | `TRADE.md:3` DECLARED FLAT 2026-09-28 with a trigger table (two FL banks in sync, or USCB association-loan deterioration; landfall reversing insurance easing) |
| L5 clean closeouts, current | NOT-ADJUDICATED, owner evidence leans not yet | closeouts recorded 11/06, 11/09, 11/16, 11/17 x2; but late falsify grade, stamp corrections (`e487a1b2f8`, `49dfc56c0a`), Palm Bay correction (`8870d4946a`), CATO CR17 corrections (`4ca122d595`), and two boot reads in the rotate tier (`scripts/read_cap_check.py --agent CORAL`: rotation_due=2) |

### (e) Profile trigger
Profile body refreshed 2026-09-05 (`profiles/CORAL.md:9`) with deltas 10/21, 11/02 and 11/07 stacked above the title. **Date-age: FIRED** (own 30-day clock, checkpoint 2026-10-05, `profiles/CORAL.md:11`), now 44 days past. Content: the 10/21 delta's "FL_Forward_Log still lacks FROZEN banner" is itself now false (banner since 10/29), and the 11/07 delta's "no forecast graded" is false since 11/17 — the stacked deltas now contradict each other and the desk. **A bounded delta cannot carry it**; whole refresh owed.

### (f) Cross-agent observations
- PROME: CORAL's STATUS and MEMORY are in the rotate tier and the desk has no `PROME/registry/READS.tsv` declaration (read_cap rc 0 is "clean within what the scan found"). CORAL STATUS is also read whole by NEXUS and REGINALD.
- MARCO: CORAL's 11/17 packet `AGENTS/MARCO/inbox/2026-11-17_from-CORAL_amendment3-figures-rebased.md` (REC 7/10 re-base) is unprocessed in MARCO's inbox at cutoff; the shared Amendment 3 revenue figure is a scoped CORAL/MARCO overlap metric.
- AEOLUS: CORAL's 11/17 St. Johns flood packet and 11/11 rain one-figure packet sit unprocessed in AEOLUS's inbox at cutoff.
- Will (via PROME): certification of Amendment 3 could not be read because the state results site blocks automated access; CORAL states it in its BOTTOM LINE. Under the root Blocked-sites rule the next route must be another source, never evasion.

---

## MARCO (Market, map L4 / M, last scored 2026-10-21)

### (a) Commits in period
**19** touching `AGENTS/MARCO/`, of which **10** are MARCO's own (sessions 39, 40, 41). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | Session 39 catch-up: Amendment 3 passed, Las Vegas and remittance grades; four new predictions MAR-28 to MAR-31 made 11/05; push blocked then cleared | `fd6995b9f1`, `df57bfb9d9`, `8ac21fa07b` |
| 11/11 | Session 40: ENR-02 SUSTAINED (October fares 2-yr +23.27%), Amendment 3 one figure 61.98% adopted from CORAL, STATUS rotation to `domain/sources/_archive/STATUS_rotated_s40_20261111.md` | `94fefe5a12`, `70d3fb82dc` |
| 11/12 | DAEDALUS packets in: WQ-678 harness lines (A approved) and VX oldest-row SFE-03 (Staleness #7) | `6a43711d27`, `1d8939b1b1` |
| 11/16 | Session 41 (doorbell, laptop restart mid-session, recovered): ID-01 IDENTIFIED on its pre-committed both-months letter; MAR-11 CONFIRMED (H-2A FY2026 435,980); VX refresh-or-freeze pass (SFE-03 re-based to CORAL, TAX-01 STALE BY DESIGN, two-clock header 10-10 to 10-21 = oldest live row) | `aa85089307`, `ab3278e9e5`; `workbook/VX.tsv:3` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Reading B PASS at new dated BOTTOM LINE 10/14 | STILL-TRUE as a pass, STALE FORM in detail: heading now reads "reviewed10/25" (glued) while bullets were edited 11/05 to 11/16; first bullet still carries the September Canadian figure (−28.72%, "11th month") beside the October figure (−26.88%, "12th month") in § Canadian Travel | `STATUS.md:6-7` vs `STATUS.md:41` |
| G2 | Reading A branch 2 PASS at TRADE DECLARED FLAT 10/10 with three explicit registered re-arm conditions | STILL-TRUE | `TRADE.md:3`, re-arm table (MIA two months plus CORAL bank rail; FL population decline; Channel 4 re-mark up) |
| G3 | Old missing current judgment / no re-arm claims are refuted | History; drop | — |
| N1 | DAEDALUS confirm-read may restore Conf H after remaining matrix/figure/header findings are checked | STILL-TRUE (not done), and the header finding is live again (G1); new figure-form defects: glued words and numbers in STATUS (`STATUS.md:6` "reviewed10/25"; `:51` "Aug4.93", "days-on-market81", "same-month2017–19 (Sep,NORMAL)") and THESIS (`thesis/THESIS.md:17` "throughQ3 certified349,867") | cited lines |
| N2 | No new summary or flat declaration needed | STILL-TRUE | G2 |

### (c) Proposed replacement cells

- **Gaps:** `BOTTOM LINE passes reading B but its heading says reviewed October 25 while its bullets were edited November 5 to 16, and its first bullet still cites the September Canadian stack (−28.72%, 11th month) where the dashboard has October (−26.88%, 12th month). Glued words and numbers remain in STATUS and THESIS line 17. TRADE DECLARED FLAT October 10 with three registered re-arm conditions. Predictions resolve on schedule (MAR-11 CONFIRMED November 16; 12 OPEN). WQ-678 harness-lines packet of November 12 not yet applied or recorded; November 16 outside-audit packet (MAR-25 95% written after the outcome; stale tables) and CORAL's November 17 re-base packet unprocessed at the November 17 cutoff.`
- **Next_upgrade:** `Conf H after MARCO re-dates or re-states its BOTTOM LINE heading against its current bullets, re-spaces the glued text, applies or declines WQ-678 Changelist A, and answers the MAR-25 audit item; then a DAEDALUS confirm-read. Profile needs a whole refresh (body September 5).`

### (d) Grade verdict — RETAIN L4 / M

| Leg | Verdict | Basis |
|---|---|---|
| L0 | PASS | `AGENTS/MARCO/CLAUDE.md` present |
| L1 (reading B) | PASS | `STATUS.md:6-15` BOTTOM LINE "the desk's judgment now", with "What would change it" |
| L2 | PASS | `workbook/KB.tsv`, `workbook/VX.tsv` (57 live vectors, two-clock header), `thesis/PREDICTIONS.tsv` accruing in period (`aa85089307`, `ab3278e9e5`) |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS, confirm-read owed | VX vectors with levels (`workbook/VX.tsv`); `thesis/THESIS.md` § EXIT / INVALIDATION RULES (line 63); predictions 15 CONFIRMED, 1 FALSIFIED, 15 RESOLVED, 12 OPEN, MAR-11 resolved 11/16; pre-registered letters (ENR-02, ID-01, SDL-01 rule for 12/04). No section titled convergence matrix found in STATUS or THESIS (grep); the VX ledger plays that role — form not re-adjudicated here |
| L4 trade leg (reading A) | PASS | branch 2, `TRADE.md:3` with three re-arm conditions |
| L5 clean closeouts, current | NOT-ADJUDICATED | closeouts 11/06, 11/11, 11/16 (`8ac21fa07b`, `70d3fb82dc`, `ab3278e9e5`); s41 was cut by a laptop restart and recovered (`SCRATCH.md:2`); WQ-678 packet sat through s41 undispositioned; BOTTOM LINE header/figure drift (G1) |

### (e) Profile trigger
Profile body refreshed 2026-09-05 (`profiles/MARCO.md:7`). **Date-age: FIRED** (>45d, checkpoint 2026-10-20, `profiles/MARCO.md:9`). Content changed since body: thesis v3.2 (9/24), TRADE declared flat 10/10, four new predictions, ID-01 identified. **A bounded delta cannot carry it** (body predates the flat declaration that the row's L4 rests on); whole refresh owed.

### (f) Cross-agent observations
- MARCO: three packets unprocessed in `AGENTS/MARCO/inbox/` at cutoff — DAEDALUS WQ-678 (11/12), PROME outside audit (11/16; item 1 says MAR-25 carries 95% written after the outcome, last pre-outcome mark 90%), CORAL Amendment 3 re-base (11/17). The CORAL one touches a scoped overlap figure (Amendment 3 local revenue) both desks must carry as one number.
- MARCO / LABOR: SDL-01 November CPS grade 2026-12-04 is MARCO's (MAR-29, 90%); LABOR's 11/05 packet (BLS population-control supplements have no nativity split) was consumed.

---

## AEOLUS (Market, map L4 / M, last scored 2026-10-21)

### (a) Commits in period
**37** touching `AGENTS/AEOLUS/`, of which **15** are AEOLUS's own, all dated 11/05 to 11/11; **no AEOLUS session after 11/11 09:45 ET** (`21515129a9`) through the cutoff. Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/04-11/05 | C5 (Rhine) FIRED on its 40/180 letter (first fire of the WQ-562 key), score 4 to 5; packets to TERRY, WATT, BRENT, PROME; same-day overclaim correction to WATT and BRENT | `6c5347bb19`, `0278bfbe93`, `981612f770`; `STATUS.md` C5 row and § C5 table |
| 11/05 | AEO-03 re-priced 55 to 90%, AEO-10 50 to 80%; water worker run adjudicated (Rhine cargo gap to CARL, HENRY, BRENT); closeout with THESIS, TRADE, VX, CALENDAR | `97c8168df9`, `ca652684f7`, `7fb738bb24` |
| 11/06 | AEO-14 to AEO-17 registered; seven combination themes; charter grows to 50,695 B | `576d7d44b2`; size by `git show <c>:AGENTS/AEOLUS/CLAUDE.md \| wc -c` (10/21 48,535 → 10/31 50,299 → 11/06 50,695) |
| 11/07 | UNG card ended by PROME; L906 and L1081 closed as overtaken | `b39f059ddb`; `STATUS.md` owed #12 |
| 11/11 | Catch-up wake: 12 inbox items drained, KB-269 to KB-278, no score moved; STATUS and SCRATCH rotated to archive | `21515129a9` |
| 11/16-11/17 | Inbound, unprocessed at cutoff: PROME WQ-701 A2 charter trim (Will ruling), WQ-704 research commission, stale-KB packet; CORAL St. Johns flood (11/17) and rain one-figure (11/11 evening); DAEDALUS WQ-678 (11/12) | `AGENTS/AEOLUS/inbox/` listing at cutoff (6 packets) |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Whole profile refreshed October 21; L4/M retained with TERRY October 11 NO-BUILD consumption | STILL-TRUE, history | `profiles/AEOLUS.md:5` |
| G2 | Owner THESIS/calendar/routing and worker-instruction contradictions remain | NOT RE-CHECKED by this reader (confirm-read owed); no commit in period names them | — |
| G3 | Water SERIES split row and guard clean-footer counterexample verified | History; drop | — |
| G4 | Full manifest unattested (read-cap rc2 assessed0) | OVERTAKEN — manifest now DECLARED in `PROME/registry/READS.tsv` (26 rows), `read_cap_check --agent AEOLUS` returns rc=1 assessed=1 over_budget=1 rotation_due=3 (run at working tree `29a370742c`; AEOLUS unchanged since cutoff) | READ-CAP-RESULT line |
| G5 | Charter 48,034 B | OVERTAKEN — 50,695 B at cutoff, over the 50,000 B charter ceiling (root `CLAUDE.md` § Data Hygiene, WQ-701); Will-ruled trim packet unprocessed; STATUS owed #14 still says 48,606 B and "PROME L470 still PENDING" | `AGENTS/AEOLUS/inbox/2026-11-16_from-PROME_WQ-701-A2-charter-ceiling-trim.md:7,19`; `STATUS.md` owed #14 |
| N1 | Bounded November 2 verification closes C4 verdict-label and C3 level-map asks; missing non-renewal instrument and C3 SERIES home remain OPEN | STILL-TRUE — C4 exit row "CANNOT-FIRE (the AND's leg 2 has no instrument)"; owed #16 observation home for C2/C3/coastal OPEN | `STATUS.md` EXIT row C4; owed #16 |
| N2 | Other October 21 findings require owner dispositions; no L5 or full-profile refresh inferred | STILL-TRUE as caution; the profile's own triggers have now fired (see e) | — |

### (c) Proposed replacement cells

- **Gaps:** `Charter 50,695 B, over the 50,000 B charter ceiling; Will's WQ-701 A2 trim packet (November 16) unprocessed, and STATUS owed #14 still cites 48,606 B. Read-cap rc 1 on the declared manifest; STATUS 26,308 B in the rotate tier. No AEOLUS session since November 11 while the C5 Rhine exit watch says re-grade every session and owed items are past due (C3 price level due November 1 MISSED; C2 cereals level by the November 10 WASDE; November 24-Month Study about November 15). Six inbox packets unprocessed at the November 17 cutoff. C4 exit leg 2 has no non-renewal instrument (CANNOT-FIRE); C2/C3/coastal observation home still open. STATUS self-level line reads L2.`
- **Next_upgrade:** `Bring the charter under 50,000 B per WQ-701 A2, drain the six packets, and re-grade C5 and the past-due owed items; then a DAEDALUS confirm-read for L5 (clean, current closeouts). Profile refresh owed: its own triggers fired (OPEN predictions 12 vs 9, KB rows 278 vs 205, C5 re-keyed to 40/180).`

### (d) Grade verdict — RETAIN L4 / M

| Leg | Verdict | Basis |
|---|---|---|
| L0 | PASS | `AGENTS/AEOLUS/CLAUDE.md` present (over ceiling, still readable) |
| L1 (reading B) | PASS, ageing | `STATUS.md` `## BOTTOM LINE` dated 11/11 09:45 ET; six days old at cutoff |
| L2 | PASS | `workbook/KB.tsv` 278 KB rows (KB-256 to KB-278 added in period), `workbook/PREDICTIONS.tsv` 17 rows, VX-47 to VX-49 |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS | CONVERGENCE MATRIX C1-C6 with composite conservation line; § EXIT / INVALIDATION with FIRED column; AEO-09 resolved 11/02; dated resolve dates (AEO-15, AEO-16 11/30) |
| L4 trade leg (reading A) | PASS | `TRADE.md:5-12` idea #1 STOOD DOWN with a pre-registered successor (LONG RNR arms on a Gulf/FL major landfall or credible track, same-session packet to TERRY); signals reached TERRY 11/05 (`0278bfbe93`) |
| L5 clean closeouts, current | NOT-ADJUDICATED, owner evidence leans FAIL now | closeouts 11/05, 11/06, 11/11 recorded; but currency lapsed: charter over the ruled ceiling, owed #7 marked MISSED by the owner, six-day dark window on an every-session exit watch, read-cap rc 1 |

### (e) Profile trigger
Profile vintage 2026-10-21, whole (`profiles/AEOLUS.md:5`). **Content trigger: FIRED on three named legs** (`profiles/AEOLUS.md:8`): OPEN predictions 12 (was 9; `workbook/PREDICTIONS.tsv` status 12 OPEN, 5 HIT), KB data rows 278 (was 205, +73), and threshold architecture changed (C5 re-keyed to Kaub 40 / Duisburg 180 under WQ-562, `a3b12fbe6e`). **Date floor 2026-11-04: FIRED.** AEO-12 still OPEN; workspace count not re-counted. The body is only four weeks old and its structure (root architecture, five workspaces, guards) is not defeated: **a bounded delta can carry it** (re-key, prediction set, charter size), whole refresh not required.

### (f) Cross-agent observations
- DAEDALUS (owner of `scripts/`): `scripts/read_cap_check.py --agent AEOLUS` grades `AGENTS/AEOLUS/CLAUDE.md` at "156% of budget" and prints "REMOVE 27,911 MORE B" against 22,785 B, though its own header says desk-charter rows are graded "of ceiling" (50,000 B). The charter-ceiling exemption appears not to apply when the charter is reached through a declared manifest row. Run at working tree, not cutoff. Needs a capable-case check before it is called a defect.
- PROME: AEOLUS STATUS owed #14 keys the charter split to "PROME L470 still PENDING"; WQ-701 (11/16) set the 50,000 B ceiling. Whether L470 is overtaken by WQ-701 should be closed at PROME's register, not the desk's.
- CORAL / AEOLUS: the 24.69 in Florida rain figure is one number at both desks (`STATUS.md` C4, CORAL dashboard); CORAL's 11/17 flood packet is unread by AEOLUS.

---

## HOMER (Market, map L4 / H, last scored 2026-11-02)

### (a) Commits in period
**41** touching `AGENTS/HOMER/` (plus 1 after cutoff, a WALTER card `e16e307cd6`), of which **15** are HOMER's own (sessions 11/05, 11/06, 11/11, 11/12, 11/16). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | HOM-03 to HOM-06 registered (WQ-596); combination watch with five themes adopted (WQ-622); 11/20 grade prep, thesis defects D2 and D4 closed, D11 logged; push blocked then cleared | `bd2d915cbb`, `a9d9cd9839`, `163ea05f5d`, `a4cbc0c8b2` |
| 11/11 | Catch-up: Trepp MF special servicing 9.22% new high; closeout on PROME's ask | `85b9717627`, `7c56715266` |
| 11/12 | **HOM-03 RESOLVED HIT** (NAR October EHS 3.75M vs 3.90M line); WQ-675 Arbor and multifamily holder answer; READS row filed (D:L985); United Fidelity wording narrowed; closeout | `4ff19c7ac7`, `a5608acfe2`, `8542ad2e13`; `STATUS.md:146` |
| 11/16 | Doorbell work (PROME prome-c4): "who pays to extend" 11 rows into MULTIFAMILY/PIPELINE; THESIS pre-grade input check and defect D12 (A1 cure conjunct has no reading); 10Y-FRM spread basis kept at 213bp vs BOND's 201bp; A1 question to Will. THESIS grows 30,570 to 33,312 B. No STATUS or SCRATCH update; no closeout commit | `6f27bc87f0`, `d9b75772fc`; sizes by `git show <c>:AGENTS/HOMER/thesis/THESIS.md \| wc -c` |
| 11/16 | Will's answer via PROME (WQ-700): A1 graded as D12 states, second conjunct UNGRADED; plus outside-audit and stale-KB packets — all three unprocessed at cutoff | `b6d80a9ad1`, `f445a7dcf1`, `f011f2477f`; `AGENTS/HOMER/inbox/` listing |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Bounded L4/H adjudication November 2: charter no-book clause plus actual CARL V3 consumption of October 28 evidence meets reading A3; L0-L3 retained | STILL-TRUE (no-book clause at `CLAUDE.md:11`; no TRADE.md at cutoff) | `git show 208bd704ea:AGENTS/HOMER/CLAUDE.md` line 11 |
| G2 | Prior October 28 L4-fail predicate is historical | History; drop | — |
| G3 | Other owner repairs / clean-closeout not universally verified | STILL-TRUE, and the 11/16 session adds a case (work committed and packets sent, no closeout record; SCRATCH still the 11/12 wake) | `SCRATCH.md:1`; last SCRATCH commit `8542ad2e13` |
| G4 | Frozen November 20 rail cadence unchanged | STILL-TRUE — DOCKET L545 PENDING; WQ-700 fixes how A1 is graded on 11/20 | DOCKET L545; `AGENTS/HOMER/inbox/2026-11-16_from-PROME_WQ-700-A1-kept-as-written.md:5` |
| N1 | L5 NOT-ADJUDICATED; verify current clean closeout and remaining owner dispositions | STILL-TRUE, reachable (DAEDALUS read after 11/20) | — |
| N2 | No TRADE file or repeat no-book clause is owed | STILL-TRUE | G1 |
| N3 | Next formal thesis grade November 20 remains frozen | STILL-TRUE | G4 |

### (c) Proposed replacement cells

- **Gaps:** `L4 passes reading A3 (charter no-book clause; CARL consumes HOMER evidence). HOM-03 HIT November 12; HOM-04 (NAHB print November 17) ungraded at the cutoff; MBA Q3 NDS (HOM-02 decider, expected about November 13 to 14) still listed as a forward catalyst with no read recorded. The November 16 doorbell session grew THESIS to 33,312 B (over the 32,550 B budget; the November 20 grade reads it whole) and left no closeout record. WQ-700 answer, outside-audit packet (tables 33 to 67 days behind) and stale-KB packet unprocessed at the November 17 cutoff.`
- **Next_upgrade:** `L5 needs a DAEDALUS read of the November 20 formal grade and its closeout: A1 graded per WQ-700 (second conjunct UNGRADED), THESIS rotated under budget, HOM-02 and HOM-04 dispositioned. Profile refresh is keyed to the same grade.`

### (d) Grade verdict — RETAIN L4 / H

| Leg | Verdict | Basis |
|---|---|---|
| L0 | PASS | `AGENTS/HOMER/CLAUDE.md` (41,649 B) present |
| L1 (reading B) | PASS | `STATUS.md:156-158` `## BOTTOM LINE` dated 2026-11-12 |
| L2 | PASS | `thesis/PREDICTIONS.tsv` (HOM-01 to HOM-06), `workbook/MULTIFAMILY.tsv` (+9 rows 11/16), `PIPELINE.tsv`, `RATES.tsv` accruing |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS | dashboard bands with rung rule (`STATUS.md` § SIGNAL DASHBOARD); HOM-03 resolved 11/12; dated kill rail GATE-HOMER-THESIS-KILL first grade 2026-11-20 (DOCKET L545) |
| L4 trade leg (reading A, branch 3) | PASS | carried from the 11/02 independent read (`profiles/HOMER.md:1`); HOMER → BOND packet 11/16 (`d9b75772fc`) and REGINALD/CREED packets 11/05 (`3238c184b1`) show output still reaching consumers |
| L5 clean closeouts, current | NOT-ADJUDICATED | closeouts recorded 11/06, 11/11, 11/12; 11/16 no closeout record; THESIS pushed over budget by the desk's own 11/16 commit (`read_cap_check --agent HOMER` rc=1, over_budget=2 at working tree); two forward catalysts past without a recorded read |

### (e) Profile trigger
Profile vintage 2026-10-28 whole, with an 11/02 delta (`profiles/HOMER.md:1-5`). Trigger (`profiles/HOMER.md:8`): "HOMER's 2026-11-20 formal grade or a material STATUS/thesis change". **Date leg: NOT FIRED** (11/20 after cutoff). **Content leg: arguably FIRED** — prediction set went from HOM-01/02 to six rows with one resolved, combination watch adopted, THESIS gained D11/D12 and crossed the read budget. A **bounded delta can carry it** until the 11/20 grade, which is the natural whole-refresh point.

### (f) Cross-agent observations
- DAEDALUS (owner of `scripts/`): second instance of the charter-row grading pattern seen at AEOLUS — `read_cap_check --agent HOMER` lists `AGENTS/HOMER/CLAUDE.md` 41,649 B as "128% of budget, over budget", although it is under the 50,000 B charter ceiling. If confirmed, this misreports every desk whose READS manifest declares its charter as a whole read.
- PROME: DOCKET L978 (HOM-03 resolution, due 11/30) is still PENDING at cutoff although HOMER graded HOM-03 HIT on 11/12 (`4ff19c7ac7`) — the row can be closed against the owner's ledger.
- BOND / HOMER: the 10Y-FRM spread is carried on two bases (HOMER 213bp survey-matched; BOND 201bp publication-date); HOMER recorded BOND's as a separate basis in `workbook/RATES.tsv` (`d9b75772fc`). Consumers must cite the basis with the figure.

---

## CRUISE (Market, map L3 / H, last scored 2026-10-21)

### (a) Commits in period
**30** touching `AGENTS/CRUISE/`, of which **19** are CRUISE's own (sessions 11/05, 11/06, 11/11, 11/14, 11/17). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | NCLH 10-Q graded (L714): actual 9/30 liquidity about $1.4B, funding leg does not re-open, breakeven −12.7%/yr (endpoint test); CRU-12 to CRU-14 registered; four combination themes; L874 charter fix; Sweep #5 memo to DAEDALUS | `31222e472d`, `37a111d056`, `3e6d561784`; `STATUS.md:45-60` |
| 11/06 | WQ-628 A: TRADE row 1 conviction 3 to 2 (WATCH / NO CARD); WQ-627 A and WQ-640 A: VX-CRU-05 cells live, RED(4) to ORANGE(3), convergence 10/20 to 9/20 | `0c495686d3`, `df86b56721`; `TRADE.md:9`; `STATUS.md:35-43` |
| 11/11 | Catch-up, no score moved; GREEN-cell reading asked of PROME | `bb54f0012c` |
| 11/14 | CRU-11 graded FAILED (+2.23pp vs ≤ −5pp); WQ-670 A encoded (GREEN cell); WQ-678 Changelist A and all six B trims applied | `94a34e0e36`, `4497c44206`; `STATUS.md:14-21` |
| 11/17 | L715 graded NOT SPRUNG, provisional (issuer 9/30 liquidity ~$1.4B vs $800M line; 10-K certifies; reversal only by an 8-K by 11/23, PROME checks EDGAR 11/24); 28 stale KB rows retired, 1 refreshed; closeout write-back after PROME consumption | `7259977733`, `6aa6ab63af`; `STATUS.md:3-12`, `:129` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Fuel-channel and operator-split theses killed on their letters; narrower NCLH ticket-price, deposit-quality and leverage read remains | STILL-TRUE | `STATUS.md:108-110` (exit rules 1 and 2 fired); BOTTOM LINE `:153` |
| G2 | Q3 10-Q read by owner November 5; no liquidity bear leg through 2027 | STILL-TRUE, reinforced by L715 NOT SPRUNG 11/17 (provisional) | `STATUS.md:9`, `:45-60` |
| G3 | Endpoint funding model and fixed covenant add-back caveats remain | STILL-TRUE ("Endpoint test, not a low-point schedule"; add-back fixed at $7,409.0M through 2028) | `TRADE.md:24`; `STATUS.md` 11/5 Covenants row |
| G4 | No independent filing or market grade here | STILL-TRUE as a caution | — |
| N1 | L4 reading-A / actual TERRY consumption remains unverified | RESOLVED on consumption, verified at TERRY's artifacts: TERRY built `TRY-COND-NCLHDEC14P` from CRUISE row 1 (2026-09-19, NOT PROPOSED, SHELVED 10/29, rotated 10/31) and its 11/16 decision row `TRY-NOTRADE-INBOX-NOV16` lists CRUISE among sources with NCLH, outcome NO TRADE. Which reading-A branch this satisfies is still open (see d) | `git show 208bd704ea:AGENTS/TERRY/SETUPS.tsv` (11/16 row; rotation comment line); `b4f50e108e`; CRUISE → TERRY packets `06e43b0b7f`, `8b611687f1` |
| N2 | CRU-11 and November 17 springing-test obligations stay owner-owned | RESOLVED — CRU-11 FAILED 11/14; L715 graded 11/17; remaining reversal check is PROME's EDGAR read 11/24 | `STATUS.md:18`, `:9`, `:129` |
| N3 | Do not repeat the obsolete unread-Q3-filing ask | History; drop | — |

### (c) Proposed replacement cells

- **Gaps:** `Fuel-channel and operator-split theses dead on their letters; the remaining NCLH read is ticket price per day, deposit quality and leverage (VX-CRU-05 ORANGE 3 under WQ-640 A; convergence 9/20). Liquidity leg closed through 2027: L715 NOT SPRUNG on November 17, provisional until the FY26 10-K; endpoint funding test and the fixed $7,409.0M covenant add-back remain caveats. CRU-11 FAILED November 14; CRU-12 to CRU-14 OPEN. TERRY consumed the trade row (setup built September 19 and shelved October 29; NO TRADE decision November 16 names CRUISE). STATUS at 27,572 B is in the rotate tier.`
- **Next_upgrade:** `L4 needs a DAEDALUS ruling on which reading-A branch a WATCH / NO CARD row that TERRY demonstrably consumes satisfies (feeds proposals, or a re-arm condition stated on the row); the consumption evidence is in place. Profile needs a whole refresh (first build September 5).`

### (d) Grade verdict — RETAIN L3 / H (L4 is reachable now; RAISE recommended once DAEDALUS confirms the reading-A branch)

| Leg | Verdict | Basis |
|---|---|---|
| L0 | PASS | `AGENTS/CRUISE/CLAUDE.md` present |
| L1 (reading B) | PASS | `STATUS.md:151-153` `## BOTTOM LINE`, current to the 11/17 L715 grade |
| L2 | PASS | `workbook/PREDICTIONS.tsv` (6 CONFIRMED, 5 FAILED, 3 OPEN), KB-CRU-225 to KB-CRU-263 added in period |
| L3 matrix + exit rules + predictions resolving + dated falsification | PASS | Convergence Matrix 5 rows with upgrade triggers and a conservation summary (`STATUS.md:92-104`); exit rules with fired dates (`:106-113`); CRU-11 resolved 11/14; dated tests (L715 11/17, reversal window to 11/23) |
| L4 trade leg (reading A) | NOT-ADJUDICATED, leans PASS | consumption verified (N1). Branch 1 ("feeds proposals"): TERRY built and evaluated setups from the row but none was proposed. Branch 2: row is WATCH / NO CARD, not declared flat or frozen, and no explicit re-arm or card condition found on the row (grep of `TRADE.md` for re-arm / condition wording finds none on row 1). Branch 3: CRUISE has a book row, so not no-book. Needs a ruling, not a mechanical pass |
| L5 | NOT-ADJUDICATED (L4 not yet granted) | closeouts recorded 11/06 x2, 11/14, 11/17 with consumption write-back (`6aa6ab63af`) |

### (e) Profile trigger
Profile is the 2026-09-05 FIRST BUILD (`profiles/CRUISE.md:9`) with deltas 10/21, 11/02, 11/07. **Event key (CCL Q3 print about 9/28-29): FIRED. Date-age (>21d, checkpoint 2026-09-26): FIRED.** Since the body: both founding theses killed, VX-CRU-05 re-specified, conviction cut to 2, CRU-11 failed, L715 graded. **A bounded delta cannot carry it**; whole refresh owed. The profile's own event key has no successor; the re-cut key should be the next NCLH or CCL print (CCL Q4 / FY27 guide, which also resolves CRU-12).

### (f) Cross-agent observations
- PROME: the L715 reversal check (NCLH 8-K by 11/23) is PROME's EDGAR read on 11/24, which wakes CRUISE only on a reversal (`STATUS.md:129`); this is reachable and correctly owned, so no CRUISE gap should be carried for it.
- TERRY: `SETUPS.tsv` 11/16 row `TRY-NOTRADE-INBOX-NOV16` carries glued numbers in neighbouring archived rows (e.g. "Completed9/2 buy1 at2.20 inRobinhood" in the 10/29 diff of `b4f50e108e`) — WQ-560 class residue on TERRY's surface, noticed in passing, not graded.

---

## Summary

| Desk | Map now | Verdict | Profile trigger | Bounded delta enough? |
|---|---|---|---|---|
| OTTO | L5 / M | RETAIN L5 / M (Conf H condition met on its letter; confirm-read owed) | FIRED (date-age) | No — whole refresh |
| CORAL | L4 / M | RETAIN L4 / M | FIRED (own 30-day clock) | No — whole refresh; stacked deltas now contradict the desk |
| MARCO | L4 / M | RETAIN L4 / M | FIRED (>45d) | No — whole refresh |
| AEOLUS | L4 / M | RETAIN L4 / M (L5 leans FAIL on currency) | FIRED (three content legs + date floor) | Yes — body is October 21 |
| HOMER | L4 / H | RETAIN L4 / H | Date leg NOT FIRED (11/20); content leg arguably FIRED | Yes, until the 11/20 grade |
| CRUISE | L3 / H | RETAIN L3 / H; RAISE to L4 recommended after a reading-A branch ruling | FIRED (event key and date-age) | No — whole refresh |

## Not read / limits

| Item | Limit |
|---|---|
| Brief provenance | Brief reconstructed by DAEDALUS (stated in the brief); its "Written 10:4x ET" stamp is later than this reader's own start (10:29 EST by `date`) — noted, not material |
| Full reads | STATUS read whole at cutoff for OTTO, CORAL, MARCO, CRUISE; AEOLUS and HOMER STATUS read in part (head, structure, predictions, owed, bottom line). No desk charter read whole; THESIS files read at header level only (OTTO, CORAL, MARCO, HOMER structure grep) |
| Convergence matrices | Structure checked for all six; per-row score against source colour not re-verified (OTTO 10 rows, AEOLUS 6, CRUISE 5); CORAL and MARCO matrix form not re-adjudicated |
| read_cap_check | Run at working tree `29a370742c`, not at the cutoff. No cohort file changed after the cutoff except a WALTER card into HOMER's inbox, so figures should match; the script itself may have changed post-cutoff (not checked) |
| forecast_report.py | Run at working tree for the CORAL N2 claim; output only, internals not read |
| The read_cap charter-row observation (AEOLUS, HOMER) | Two cases seen in output; not reproduced against a clean case; no code read. Treat as a lead, not a finding |
| Profiles | Only header, vintage and Staleness lines read; profile bodies not re-verified against the desks |
| Outside-audit claims | The 11/16 PROME audit packets to OTTO, MARCO, HOMER read for their item text only; claims not verified (except OTTO-06/09 ledger rows shown as excluded from calibration) |
| Inbound packets | Unprocessed-packet counts are from `git ls-tree` of each inbox root at cutoff; packet bodies read only for the WQ-701 (AEOLUS), WQ-700 (HOMER), audit and WQ-678 packets |
| Closeout cleanliness | Judged from commit subjects/bodies and LAST_COMPLETION / SCRATCH / NEXUS_BRIEF last-touch dates; closeout scripts (orphan, consumer, claim checks) not re-run for any desk |
| External sources | None fetched; no market, filing or court figure re-verified |

END OF REPORT
