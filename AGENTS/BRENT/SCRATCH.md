# BRENT SCRATCH — November 20 CHECKPOINT (PROME prome-77 due-row wake, booted 11:59 EST; checkpoint 12:14 EST on the operator's word "lets checkpoint here"; times from `date`)

⚠️ **This is a mid-session checkpoint, not a closeout.** The BRT-33 window, the PROME delivery packet and COT #15 are still owed (NEXT SESSION 1–3). Closeout steps 12–14 have not run.

## CHANGES SINCE LAST SESSION
- **December crack collapse:** HOZ26 × 42 − CLZ26 about $82.10 at 11:50 ET 11/20 (vendor daily row, intraday, not a settle), from $95.09 on 10/21; below $90.16 since 11/16. January $79.57. **CLZ26 last trade is today 11/20.**
- **Russia:** refinery processing ~700k → ~400k t/d, −43% on the stated tonnes (Reuters via Kyiv Independent, OSPREY); Crimea fuel purchase limits; Kaleykino (Druzhba feeder) hit, no flow effect. Shenzhen declaration's refined-products clause is not an export decision (YURI).
- **Gulf:** FALCON relays Kpler via AP: all-route Middle East shipments about 64% of pre-war (97% October), Hormuz crude 8.5 mb/d preliminary. **NOT found at a source.** Iran export "restart" = intent plus one STS transfer (OilPrice 11/20). Russian missiles landed in Poland (no energy asset).
- **Tape at boot:** BZF27 91.22, BZH27 86.82 (11:44–11:50 ET bars, M1−M3 about +4.40) [vendor, delayed ~10 min]. `fetch.py` boot quotes served February Brent (88.78) and January WTI (82.02): D:L1179 roll caveat applies, quote named contracts.

## WHAT I DID THIS SESSION (to 12:14 EST)
- **Commission D:L783 delivered as a file:** `research/2026-11-20_diesel-commission/REPORT.md` (catalyst table, crack path, PROJECTION about 20% January back above $90.16 before CLF27's 12/21 last trade, unscored). Question 3 answered: the line was reached 11/2; no live Valero line reads the crack (D-78).
- **Inbox drained:** 16 consumed = 16 board_log rows = 16 `git mv` (4 top-level incl. PROME outside-audit and TERRY ask; 12 WALTER). Corrections COR-20261119-14 APPLIED, COR-20261120-12 NO-OP; check rc 0.
- **TERRY packet committed** (`AGENTS/TERRY/inbox/2026-11-20_from-BRENT_postmortem-thesis-grades-and-crack-handoff.md`): USOARM MIXED, XLE65C WRONG on the equity leg, REFINER MIXED, FIRE-006 UNRESOLVED; WQ-696 crack handoff, no new idea.
- **CATALYSTS:** China GAC October graded PARTIAL (5.18 Mt customs total, secondary); NEHHOR graded (300,000 bbl awarded 11/4, completion NOT CONFIRMED); combo rows yanbu-bypass, diesel-buffer, gulf-access-cost reviewed and re-dated 11/25; gulf-flow-basis logged. Calendar re-rendered.
- **REGISTRY:** KILL-LEG2-JWC-LISTING last_verified 2026-11-20 (JWLA-035 still newest, curl default string). ⚠️ First read used a browser-like string (12:05:30), disclosed in UA_REVIEW.md, not relied on.
- **UA_REVIEW.md (draft for PROME, no code changed):** `instrument_check.py` and `thresholds.py` still send a Chrome identity plus browser headers; the 11:59 boot sent it. Proposed fix and measured table in the file.
- **STATUS:** 11/16 and 11/14 blocks plus receipts rotated verbatim → `archive/STATUS_dated_2026-11-20_rotation.md` (5 sets, crc in header); 11/20 summary for Will written. **No November 20 dated block yet** (written after the window).
- **Commits (local, not pushed):** d135ad7354 (main), TERRY packet commit, this checkpoint commit.

## NEXT SESSION (dated, future-verifiable)
1. **TODAY Fri 11/20, BRT-33 eighth window [14:28,14:30) ET.** A background pull (`research/2026-11-20_brt33/pull.py c1`) was scheduled for 14:44 EST into `run_c1.txt`; if this session ended, it died with it: **re-run `pull.py c1` by about 22:00 ET today** (vendor one-minute reach ~8 days, but read today). Valid = both BZF27 and BZH27 with a positive-volume bar. If valid and not under +3.5000 → **8 of 8, NO is reached at the first read after 11/27** unless a later session crosses. Write `research/2026-11-20_brt33/NOTE.md`, CATALYSTS row 28 note, TRACKER stamp, fill REPORT § Window (Dec HO−CL from the same capture).
2. **TODAY after 15:30 ET: COT #15 (as-of 11/17), G:GATE-BRENT-COT-35B review.** `cot_grade.py --expect 2026-11-17` (plain client string) + Socrata 72hh-3qpy cross-check; COT_VINTAGES row; NOT-SPENT floor 118,326 (#14 was 122,378).
3. **Then deliver:** STATUS November 20 dated block; NEXUS_BRIEF rewrite (figures changed: crack, BRT-33, COT; new SENDING row TERRY handoff); PROME packet at `PROME/inbox/2026-11-20_from-BRENT_...md` (commission, window, COT, outside-audit answers below, UA_REVIEW draft, charter line: step 12 already matches WQ-719 A since 11/18, no change needed), commit, SendMessage to prome-77; HOLD until PROME asks to close.
   - **Outside-audit answers (for the packet):** 1 BRT-23 and 2 BRT-22/BRT-28 — auditor right on the letter: `AGENTS/DAEDALUS/scripts/scorecard.py` maps "RESOLVED — MECHANISM-CONFIRMED" to HIT and FAILED to MISS. Proposed: BRT-23 letter met (Glencore FM by May) → hit with mechanism falsified noted; BRT-22 threshold untested → NO-VERDICT (needs Will: his Jun 1 split ruling); BRT-28 grade on its own else-branch (Brent held $90–100 to 7/1?) after a price read. Not applied. 3 BRT-26 confirmed: scored at 85% (9/6 mark), last before the 9/25 outcome. 4 answered 11/17.
4. **Wed 11/25: WPSR week 11/20** (no holiday shift per EIA schedule read 11/19): BRT-31 MET only at or under 8,263.66 kb/d; BRT-34 third print; combo reviews (now five rows dated 11/25).
5. **Thanksgiving 11/26–11/27 hours UNREAD** (cmegroup.com IP-blocked; Will can read the CME PDF). Only matters for BRT-33 if today is invalid.
6. **Before 11/29 (OPEC+ January):** IEA spare still missing; read CONTESTED.
7. **Next ordinary session:** UA_REVIEW fix if PROME agrees (C2 for LESSONS L25); TSA from 11/13; PortWatch token question to FALCON/WALTER.
8. **Housekeeping (carried):** USO observations freeze or refresh; 10 INCIDENTS ACTIVE rows past 60 days; DXY basis break; TANKER-LIVENESS.

## OPEN THREADS / WATCHES
- 🟠 Diesel crack unwind vs a thinner world buffer (combo:diesel-buffer, review 11/25).
- 🟠 Kpler all-route figure unverified; watch for a Kpler or Vortexa primary.
- 🟠 Hormuz and Gulf states: laden crude loss / stated Gulf-ally loss / M1−M3 above about +6.3 with flat price rising.
- 🟠 BRT-31 hinges on 11/25.

## POSITION DECISIONS PENDING
- None from BRENT. D-104 (three Fidelity lines gone) is Will's and PROME's: CHECKED-AT-ARTIFACT-AND-STILL-OPEN (FORGE/STATUS.md, 11/20 boot). No expiry reminders (USER.md).

## MAIL STATE
- Inbox: clear (top-level and WALTER/), as of 12:05 EST.
- Outbox: TERRY packet delivered and committed. PROME delivery packet NOT yet written (item 3).
