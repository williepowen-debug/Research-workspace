# RED SCRATCH — canonical session handoff
**S61 HANDOFF — written 2026-11-10 10:13 ET (from `date`). Booted 11/09 20:11 ET on the laptop, status-only on Will's task ("do not begin unassigned work"). Closed 11/10 on PROME prome-1e's relay of Will 10:11 ET: switch laptop → desktop. The S60 handoff and its addenda b to f are in git history (`git log -p -- AGENTS/RED/SCRATCH.md`).**

## CHANGES SINCE (S60-f closed 11/06 18:35 → S61 11/10 10:13)
- Official: VIXCLS 25.64 [11/06], 19.92 [11/09] · HY 342, CCC 1,317 [11/06]; the 11/09 HY cell was unpublished at 10:12 ET · SKEW 153.55 [11/06], 150.34 [11/09] Cboe · 5y5y 2.19 [11/09].
- Vendor, not closes: 11/09 SPY +2.37%, KRE +1.73%, Brent 92.33; 11/10 10:12 ET ^VIX 20.43, Brent 90.59, 10Y 4.99.
- Iran: FALCON graded 11/09, no mark moved. Qatar terms reported as accepted by Iran, unconfirmed by either government. The 11/8 Qeshm blasts are not established as US (FAL-09 0 of 5). WL-11 Brent <95 price leg met on vendor quotes, display only.
- SAM graded SoftBank overnight: leverage estimate CONFIRMED, 15.9% at 9/30 and 22.5% rolled (SAM commit cd0b8bc027, packet to PROME). Not yet read by RED.

## WHAT I DID (S61)
- Boot reads in full, boot.py, review_debt (clean), ledger staleness (clean), corrections (4 named, DEFERRED to 11/11 in the receipts file), basis (root CLAUDE.md WQ-651/652/653 and fetch.py L925 read, re-attested).
- **FT-06 exit 1 → 3 of 5** in canon, STATUS, CALENDAR and NEXUS. Scan view regenerated. No weight moved.
- board_log: PROME packet `deferred`, 13 Iran and AI info-cc cards `info-only` (titles read, bodies not). Rotated, 59.8%.
- STATUS headers S60-d and S60-c folded verbatim → `reports/2026-11-10_S61_status_headers_folded.md`. NEXUS vS60-e rotated → `reports/2026-11-10_NEXUS_BRIEF_vS60-e_rotated.md`.

## NEXT SESSION (dated, ordered; desktop pickup)
0. 🔴 **FT-06 / RED-29:** 11/10 and 11/11 VIXCLS. Both ≥18 → the 11/12 read after 10:30 ET executes Stag +2 / Managed −2 MECHANICAL, RED-29 TRUE, and no discretionary re-derivation 11/13. Any close <18 → reset to 0, RED-29 FALSE. 11/10 ^VIX 20.43 at 10:12 ET, about 2.4 over the line.
1. 🔴 **Oct CPI (printed 11/10 08:30), UNGRADED:** grade per `research/2026-11-10_OCT_CPI_DECISION_TREE.md`: FT-08 exit (only core ≤0.0), CHG-028 final verdict, RED-28. bls.gov 403s this box; use LABOR's or HENRY's saved release.
2. 🔴 **Household debt report 11/10 11:00 ET:** CHG-045 and CHG-049 re-review per `research/2026-11-10_HHDC_Q3_TREE.md`. The governing rule is the RE-SPEC (Will Option A 8/16, `PROME/reports/2026-11-09_CARL-HHDC-governing-rule.md`); the as-written row is the shadow only. CARL grades.
3. 🟠 **PROME packet, in `inbox/` (left there as the pickup):** fix CHG-RED-045's Key_Finding cell in `workbook/CHALLENGES.tsv` (canon; the STATUS line is GENERATED) so it no longer reads as "grade the kill rule as written". Then `status_mirrors.py --write`, then `git mv` the packet to `inbox/processed/`. PROME's date is 11/11 (D:L1064).
4. 🟠 **11/11 CHG-057 re-review (D:L1064):** SoftBank (SAM's grade, commit cd0b8bc027) and CoreWeave Q3 (11/10 17:00 ET) per `research/2026-11-10_AI_FUNDING_TEST_TREE.md`; VULCAN's read.
5. 🟠 **Then the post-CPI discretionary re-derivation** off the STATUS ledger, War included (FALCON 11/09 grade; price and flow read separately) — unless FT-06 executes 11/12.
6. 🟡 **Corrections:** COR-20261106-53, COR-20261107-02, COR-20261108-02, COR-20261109-09 are DEFERRED to 11/11: read each and re-receipt APPLIED or NO-OP (KB-RED-112 is the likely artifact).
7. 🟡 **OVERDUE since 11/09:** CHG-054 re-review: OZK 10-Q (FDIC filer), Chicago refi primary (SIG-W-20261027-041). Reasoning grade only; the book is Will's.
8. 🟡 **FT-02 and RED-27 daily:** HY 11/09 and 11/10 cells. **KB review cluster row (11/06) is OVERDUE on boot.py**: resolve it with an outcome. **11/13** combo theme credit-breadth-outside-ai. **11/19** ING auction. **11/20** three combo themes, Michigan final. **~11/25** FT-10 outcome grade.
9. 🟡 **CARL packet (11/06), still deferred:** press CRL-21 MISSED (see S60 handoff item 5 in git history; grade at `AGENTS/CARL/research/2026-11-06_L843/GRADE.md`).

## OPEN THREADS
- Live-event override: VIX over 20 intraday 11/10; the override applies at the next boot if a VIX close over 20 posts and an event is running.
- FT-10's ~11/25 CORRECT must not be read as war or credit foresight (tech and gamma trigger, ML-311).
- WL-11: price and flow still disagree; do not resolve by inference.

## PENDING WILL-DECISIONS
- None owned by RED.

## GIT STATE
See the closeout message. Shared tree held many other desks' dirty files at 10:12 ET (closeout traffic); RED committed by pathspec only.

---

## S62 ADDENDUM — 2026-11-10 11:50 ET (from `date`; desktop, PROME prome-07 on Will's word 11:38 ET; Will's task = items 0 to 9 above)
**Done:** 1 Oct CPI graded (FT-08 HOLD 3.66; CHG-028 CLOSED NO VERDICT, airfares +0.41% vs 2.35; no III move) · 2 household debt (re-spec NOT FIRED 23bp of 100bp; shadow MET, denominator only; CHG-049 RESOLVED-CONVERGED; CHG-045 open to 11/17 for Will only) · 3 PROME packet: CHG-045 Key_Finding canon cell rewritten, mirror regenerated · 4 CHG-057 SoftBank inputs staged (SVF2 loan inside ratio → Attack 6 reopens on the letter) · 6 corrections: 4 deferred + COR-20261109-11 receipted (2 APPLIED on KB-112, 3 NO-OP) · 7 CHG-054 on the OZK 10-Q (OZK leg MODERATE by rule; re-review 11/30) · 8 KB-065/066/096 dispositioned, cluster row resolved; FT-02 HY 334 [11/09] · 9 CARL CRL-21 presses answered by packet · inbox 3 → 0 · VX-002 October unreadable (no Oct 2025 CPI base, ML-329) · KB-RED-115 consumer combo opened.
**Not done:** 0 FT-06 needs 11/10 and 11/11 VIXCLS (read 11/12 after 10:30 ET) · 5 discretionary re-derivation NOT run and OWED (inside Will's items 0 to 9; the PROME packet first mislabelled it 'outside this task', corrected to PROME by message); run it after the 11/12 FT-06 read, not on 11/13 if FT-06 executes · CoreWeave 17:00 ET pending (VULCAN) · WALTER card SIG-W-20261110-001 (FT-08 ask, ACTION RED) arrived 11:4x ET after commit: log it, answer = HOLD, already graded.
**Next entry point:** 11/11 CHG-057 re-review from SAM and VULCAN reads (tree `research/2026-11-10_AI_FUNDING_TEST_TREE.md`); 11/12 FT-06 / RED-29 read; then the re-derivation only if FT-06 does not execute (otherwise not on 11/13).
**S62 addendum 2 (11:48 ET from `date`, after push ae1c321ff0):** WALTER card SIG-W-20261110-001 logged acted (FT-08 HOLD, same as the grade) and moved to `inbox/WALTER/processed/`; cards 002 info-only, 004 deferred to the 11/11 CHG-057 re-review (BROCK: a Microsoft cut is not a default on IREN's Mackenzie loan; body unread).
**S62 addendum 3 — 2026-11-10 17:47 ET (from `date`; PROME prome-07 17:40 ET on Will's 17:18 ET word):** SoftBank investigation, RED as challenger: nothing BROKEN, five lines WEAKENED (report `reports/2026-11-10_S62b_softbank_challenge_and_CHG057_grade.md`; math `reports/2026-11-10_S62b_sb_math.py`). CHG-057 graded EARLY: MODERATE unchanged; Attack 6 succeeds on capacity; re-review moved 11/11 → **11/19**. BROCK card 004 read (re-disposition acted). LIQUID packet on the S&P outlook conflict. Earlier 13:14 ET self-sweep (Will): STATUS hypothesis-table 'moves it next' column, Bottom Line, Top Priorities, bull-steelman check and trigger readings are stale; offered to Will, NOT done. **Next entry point unchanged:** 11/12 FT-06 / RED-29 read after 10:30 ET; then the item 5 re-derivation (not 11/13 if FT-06 executes), counting SoftBank once as AI-funding evidence.
**S62 addendum 4 — 2026-11-10 19:33 ET (from `date`; night closeout on PROME prome-07's relay of Will 19:32 ET, 'close up for the night'):** STATUS current-state reconciled (the stale sections from the 13:14 ET sweep: hypothesis-table cells, next re-derivation line, Top Priorities, Bottom Line; S58-and-older bottom-line entries folded verbatim → `reports/2026-11-10_S62c_status_bottomline_folded.md`). Still NOT done: bull-steelman re-check after CPI/HHDC/SoftBank (do it inside the re-derivation), trigger-table readings beyond the cells above, retirement pass (~8 files). **Next entry point, dated:** (1) **Thu 11/12 after 10:30 ET** FT-06 / RED-29 read on VIXCLS 11/10 and 11/11; (2) then the item 5 re-derivation, unless FT-06 executes (then not 11/13), counting CPI, household debt and SoftBank once each; (3) **11/13** KB-107 re-class plus KB rows due 11/11–11/13 and combo credit-breadth-outside-ai; (4) **11/17** CHG-045 (Will only); (5) **11/19** CHG-057 re-review (NVIDIA 10-Q, ING bids, SoftBank Tokyo/CDS/rating reads); (6) **by 11/20** Zweig thrust tree for 11/27; (7) ~11/25 FT-10 outcome.
