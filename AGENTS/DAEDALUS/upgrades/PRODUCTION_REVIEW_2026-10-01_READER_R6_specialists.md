# PR#7 — Reader R6 (single-name specialists + event desks): OZK · WAL · FLG · OTTO · CRUISE

**Reader:** fan-out R6, read-only · **Period:** 2026-09-17 → 2026-10-01 · **Baseline:** `e9ac693af` · **Run:** 2026-10-01
**Commits in period touching the tree (self-subject):** OZK 39 (30) · WAL 84 (64) · FLG 27 (19) · OTTO 18 (7) · CRUISE 64 (43). All five trees clean in `git status`.

## Summary table

| Agent | Now | Proposed | Move | Key fact |
|---|---|---|---|---|
| OZK | L4 H | **L4 H** (hold) | — | L5 item 1 still PARTIAL: KB rows **218/219 in no group table** (MEMO_ITEM_3 lists 4, KB has 6) |
| WAL | L4 M | **L4 M** (hold) | — | Conf gate NOT DUE (Q3 date unannounced); STATUS regrew 14,227→25,297 B in 4 days (rotation_due=1) |
| FLG | L3 M | **L3 M** (hold) | — | T-08 FIRED 10/01 and graded by the owner; 0 of 3 predictions resolvable before 2026-11-20 |
| OTTO | L4 H | **L4 H** (hold) | — | item 1 met 9/28 (22,373 B), regrew to 22,959 B; item 2 overlay still OPEN |
| CRUISE | L3 M | **L3 H** | Conf M→H | Demote **NOT FIRED**: the print happened 9/29 and CRUISE graded it the same day at SEC primaries |

---

## OZK — L4 H

**A. Claims tested**
| Claim (FLEET_MAP 9/17) | Verdict | Locator |
|---|---|---|
| 17 dark days, 0 self-commits, STATUS byte-identical to 8/31 | OVERTAKEN | sessions 9/24 (24 commits), 9/27 (8), 10/01 (3); STATUS rebuilt 29 KB→14 KB `4f6852513`, now 19,905 B |
| KB_INDEX group tables max at 227 vs KB 229 | **PARTIAL fix** | re-rolled through 241 (`ef900ced0`, `18ca81cf5`); **but MEMO_ITEM_3 = "018–020, 087 / 4" (`workbook/KB_INDEX.md:15`) while KB.tsv has 6 MEMO_ITEM_3 rows, so 218 and 219 (dated 2026-08-07) sit in no table.** Every other group count ties (scripted check). The desk's own proof (`KB_INDEX.md:3`, "verified by `comm` of KB.tsv groups vs table names") checks that every GROUP has a table, not that every ROW is in one. It is the wrong perimeter. |
| outbox root 13 files, oldest 66d | MOSTLY FIXED | 13→2 (`c96980acf`); the 2 left are reasoned in the commit: the 7/20 selfsweep has no receipt, and the 7/23 ozk09-remark is a live citation target |
| 2 unprocessed inbox packets incl. DAEDALUS 9/5 L5 | OVERTAKEN | inbox 4→0 (9/24), 3→0 (10/01). 1 present: PROME 10/01 lane-query (`116229ebd`), which landed after the closeout `5d7c64642` |
| Group token 36 vs 37 measured | FIXED | `KB_INDEX.md:3` 37 · `INDEX.md:4,13` "241 rows / 37 groups"; STATUS rebuilt with no group token |
| OZK-09 negative branch un-instrumented in-row | FIXED (different cell) | `PREDICTIONS.tsv` OZK-09 Invalidation cell "NEGATIVE-BRANCH INSTRUMENT [added 2026-09-24]". The ask named the Notes cell. The substance is in the row. |
| Minor | NEW | `KB_INDEX.md:3` header says "240 rows" while KB.tsv = 241 and row 241 is already in SUB_NOTES (`:78`). The body is ahead of the header. |

**B. Ladder walk:** L1 PASS (STATUS 10/01 header + BOTTOM LINE `STATUS.md:135`) · L2 PASS (KB 241 rows, two-clock header `KB.tsv:2` 2026-10-01) · L3 PASS (OZK-09 event-anchored, falsification instrument in-row; DOCKET L126 graded on the day `f48e8062e`) · L4 PASS (WALTER R3 verdicts consumed `ea46fc961`; CRE-transmission leg delivered to PROME `a7c8e5792`) · **L5 FAIL on the letter.** Item 1 is unfinished: 218/219 fall inside "through 229". Closeouts are otherwise clean and current (10/01, tree clean).

**C. Reachability:** all legs are in OZK's own tree and none is date-anchored. Clean. The 10/02 read (DOCKET L463) and the Q3 call (L520, check-by 10/31) are owner-local and have wakes.

**D. Profile trigger:** **FIRED.** The 21-day checkpoint was 2026-09-26 (`profiles/OZK.md:4`). The body is also stale: it says the last session was 8/31, "13 files" open, and L5 items 1 and 2 open.

**E. Proposed row:** **L4 · H**
- *Gaps:* "PR#6 L5 items 2 and 3 DONE 9/24: group count 37 on KB_INDEX and INDEX; outbox root 13→2, the two residues reasoned in c96980acf. Item 1 PARTIAL: KB_INDEX MEMO_ITEM_3 lists 018–020, 087 (4) while KB.tsv holds 6, so rows 218–219 are in no group table. The desk's verification is a group-name comm, which cannot see a missing row. KB_INDEX:3 header total 240 vs 241. OZK-09 negative-branch instrument in-row (Invalidation cell). STATUS 19,905 B."
- *Next_upgrade:* "L5 on one edit in OZK's tree: add 218–219 to MEMO_ITEM_3 (4→6), set header total 241, and prove it with a ROW-coverage check (every KB id appears in a table), not a group comm."

**F. Cross-agent:** ① The `outbox/2026-07-20_to-PROME_seeded-selfsweep-findings.md` packet has no PROME receipt in 73 days, and an identically named packet sits in `AGENTS/REGINALD/outbox/`. Owner: **PROME** (confirm or decline). ② CREED `b950eae86` flagged two OZK-file inconsistencies; OZK consumed it 10/01. Owner: OZK, closed.

---

## WAL — L4 M

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| PR#6 Conf gate must be RE-CUT (leg A unsatisfiable, leg B pre-discharged) | TRUE (historical; already re-cut in Next_upgrade) | — |
| 15 dark days | OVERTAKEN | sessions #7–#10: 9/24, 9/27, 9/28 |
| STATUS 32,547 B, 3 B under budget | OVERTAKEN, then **regrew** | rotated 9/24 to 14,227 B (`0721aded3`), back to **25,297 B = 78%** by 9/28 (`d959e96f8`). `read_cap_check --agent WAL`: rotation_due=1, owes 2,513 B to the <70% stop. |
| KB_INDEX 7 rows / 13 days behind | FIXED | `KB_INDEX.md:2` "215 rows / 20 groups", KB.tsv 215; all 20 group counts tie |
| WAL-01 pre-commits a NO-VERDICT / INSTRUMENT-ABSENT band | TRUE | PREDICTIONS header :1 (8/20 re-instrument) |
| Conf M→H fires only after the Q3 deck publishes | **NOT DUE** | `STATUS.md:34,71`: date NOT announced (re-checked 9/28); Wednesday pattern gives 10/21 or 10/28; DOCKET L170 window opens 10/13 |
| Profile 36d past its fired trigger | TRUE, worse | `profiles/WAL.md` built 8/7 (55d), no Staleness line. Content stale: "KB 170 rows/16 groups" vs 215/20, "v2.3" vs v2.4 |

**B. Ladder walk:** L1 PASS (`STATUS.md:116` BOTTOM LINE) · L2 PASS (KB 215, PREDICTIONS two-clock) · L3 PASS (Q3 print + 10-Q frames pre-registered 9/24, `Q3_PRINT_GRADING_FRAME_2026-09-24.md`, `Q3_10Q_GRADING_FRAME_2026-09-24.md`) · L4 PASS (Nano Banc leg to PROME/REGINALD `75ae6f693`; WQ-312 rows `171338055`) · L5 FAIL on currency: STATUS in the rotate tier, outbox root 12 packets (oldest 2026-08-07), and 4 NEXUS_BRIEF "last write" re-pins on 9/28 show the closeout repeating itself.

**C. Reachability:** the Conf gate has an occurrence precondition. WAL-01 is graded on deck slide 12 and WAL-02 on the Q3 NCO, so both are gradeable at the print (Resolve_By 11/15). The gate can fire once the print publishes, and it can only run from a WAL session. Clean. Separate risk: the FFIEC PWS JWT expires **2026-11-05**, inside the Q3 10-Q window (`STATUS.md:17`, WILL_QUEUE row 31). Owner: Will.

**D. Profile trigger:** **FIRED** (carried; the content is measurably stale, above).

**E. Proposed row:** **L4 · M** (Conf gate not yet testable)
- *Gaps:* "Q3 date unannounced (IR/EDGAR 9/28; Wed pattern → 10/21 or 10/28); WAL-01 (deck slide 12) and WAL-02 (Q3 NCO) both gradeable at the print, Resolve_By 11/15. KB_INDEX in sync (215/215, 20 groups tie). STATUS rotated 9/24 to 14,227 B and regrew to 25,297 B (78%; owes 2,513 B to the <70% stop). Outbox root 12 packets, oldest 2026-08-07. Inbox 3 (WQ-328 hotel read due 10/09; CREED supply; WALTER R3). FFIEC JWT expires 11/05, inside the 10-Q window."
- *Next_upgrade:* "Conf M→H at the first review after the WAL Q3 release has published (date unannounced; L170 opens 10/13), if WAL-01 and WAL-02 each carry a verdict or NO-VERDICT. Now: finish the rotation to <22,785 B."

**F. Cross-agent:** ① WQ-328 hotel-exposure read due 10/09. Owners: WAL, with CREED supplying (`2600bda37`, `49f552e17`). ② FFIEC JWT renewal. Owner: Will/PROME. ③ WAL profile refresh. Owner: DAEDALUS.

---

## FLG — L3 M

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| Ledger row counts KB 52 · NA_FLOW 26 · MW 14 · MI3 12 · TRIGGERS 11 · RGB 5 · PRED 3 | OVERTAKEN (accruing) | now KB **71** · TRIGGERS **13** · others unchanged |
| TRADE.md exists; unmet leg = "feeding proposals" | TRUE | `TRADE.md:3` "LIVE — state as of 2026-08-20 … NO POSITION". It has not been re-stated against the mirror in 42 days, and no proposal was made in the period (`d9fcfc1bd` "No trade proposal") |
| 20 dark days correct waiting; next obligation T-08 10/01 | OVERTAKEN | FLG ran 9/24, 9/27, 9/28, 10/01 |
| T-08 wake triple-wired | TRUE and **DISCHARGED** | T-08 FIRED 10/01, graded by FLG on the letter (`TRIGGERS.tsv:14`, `d9fcfc1bd`). Leg 2 is INFERRED-high: court docket 403, SEARCH-NOT-FOUND |
| 4 packets queued behind the 10/01 wake (PROME owns the spawn) | OVERTAKEN | drained 9/24 and 10/01. Inbox 1 = WALTER R3 (10/01, after the session) |
| Conf M→H on first grade ~2026-11-06, fires only once the Q3 10-Q has published | TRUE, reachable | FLG-02/03 Resolve_By 2026-11-20; FLG-01 2027-03-15 |

**B. Ladder walk:** L1 PASS (`STATUS.md:164`) · L2 PASS (7 ledgers, LIVE headers) · L3: matrix/exit PASS (`workbook/EXIT_PROTOCOL.md`, K-1..K-4; THESIS Q2e) · dated falsification PASS (TRIGGERS dated, T-08 graded on time) · **predictions resolving NOT-ADJUDICATED** (0 of 3 resolvable before 11/20) · L4 FAIL on "feeding proposals" (none). Signals do flow: REGINALD VX-REG-6.03 exchange `f6a95855b`; CRE leg to PROME `ff355bc8c`.

**C. Reachability:** the Conf gate has an occurrence precondition, so it is clean. Partial recurrence of the PR#6 pattern: the Next_upgrade clause "grading legs stay NOT-ADJUDICATED before that date" and the profile trigger "first grade, 2026-11-06" both key on an estimated date, not on the 10-Q's occurrence. If the 10-Q slips, the legs become adjudicable by date while no grade exists. T-03 (Q3 date confirmation, 10/16) has no wake (DOCKET L563 flags it). Owner: PROME.

**D. Profile trigger:** **FIRED** on the ">21d → checkpoint 2026-09-26" leg (`profiles/FLG.md:6`).

**E. Proposed row:** **L3 · M**
- *Gaps:* "T-08 FIRED 10/01 and was graded by FLG on the letter (d9fcfc1bd; court docket unreachable, leg 2 INFERRED-high). 3 predictions, none resolvable before 2026-11-20 (FLG-02/03, Q3 10-Q), so the L3 'resolving' leg is NOT-ADJUDICATED. TRADE.md 'LIVE — as of 2026-08-20', NO POSITION, not re-stated against the mirror since build; no proposal fed. Ledgers accruing: KB 71, NA_FLOW 26, MW 14, TRIGGERS 13, MI3 12, RGB 5. T-03 (10/16) has no wake (DOCKET L563)."
- *Next_upgrade:* "Conf M→H when FLG-02/03 are graded off the Q3 10-Q (fires only once it has published; observed +37d ≈ 11/06; Resolve_By 11/20). Legs stay NOT-ADJUDICATED until that filing, not until a date. L4 on a proposal fed to TERRY/PROME."

**F. Cross-agent:** ① T-03 wake. Owner: PROME (L563). ② REGINALD VX-REG-6.03 ORANGE band broken 9/28 (`f6a95855b`), cause UNKNOWN. Owner: REGINALD; FLG integrated it. ③ TRADE.md mirror re-statement. Owner: FLG, against FORGE (PROME).

---

## OTTO — L4 H

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| PR#6/Wiring-2 ASKs dispositioned 9/24 | TRUE | `9df77c858` |
| OTTO-12 has an instrument and a dated attempt (next 10/01) | TRUE; 10/01 attempt **not yet logged** | `thesis/PREDICTIONS.tsv` OTTO-12 Notes "NEXT ATTEMPT 2026-10-01". Last OTTO session 9/30 (`abf66109d`) |
| Item (c) STATUS 32,519 B = 100% | OVERTAKEN | |
| L5 item 1: STATUS <22,785 B by NET delta | **MET then LOST** | 32,519 → 22,373 (`c922a00b3`, 9/28) → **22,959 B** (`3f488b4e1`, 9/30). Now 71%, in the 70–75 band, rotation_due=0. `read_cap_check --agent OTTO` rc 0 |
| L5 item 2: §2 5-pt + Independence overlay | **OPEN** | `STALE_PUNCHLIST.md:17` "(a) … DEFERRED"; SIGNAL DASHBOARD columns are Indicator · Value · Status (`STATUS.md:36-40`) |

**B. Ladder walk:** L1–L4 PASS (the profile's 9/5 table holds; the 9/30 set was resolved at as-made `7681cfb5b`; CATO RC2 applied `3f488b4e1`) · **L5 FAIL**: item 2 is open and item 1 fails on the letter.

**C. Reachability:** ① Item 1 is **mis-specified against canon.** It demands a standing <70% while READ_CAP rule 5 owes nothing until the 75% trigger (24,412 B). A desk can fail this leg while owing nothing, which is OTTO's position today. Re-cut it. ② "Log the 10/01 OTTO-12 attempt" keys on the desk's own date, but OTTO is Tier-2 and spawn-only, and no DOCKET or GATES row wakes it for the 10/01 cluster (OTTO-12 re-search, 10-D cycle, seasoning repair; STATUS `:151`). The leg is reachable only if PROME spawns OTTO.

**D. Profile trigger:** **FIRED (probable).** "Next post-CARL-sitting session or >45d → 2026-10-20" (`profiles/OTTO.md:7`). CARL re-graded 9/24 (`fca407111`) and OTTO then ran 9/28 and 9/30. "Sitting" is undefined, so re-key it to a named event.

**E. Proposed row:** **L4 · H**
- *Gaps:* "§2 5-pt + Independence overlay OPEN (STALE_PUNCHLIST (a); dashboard is Indicator|Value|Status). STATUS rotated 9/28 to 22,373 B, now 22,959 B (71%, under the 75% trigger; nothing owed under rule 5). OTTO-12's 10/01 attempt not yet logged (last session 9/30); no wake row covers OTTO's 10/01 cluster. OTTO-10 NEEDS_VERIFY per CATO RC2 (3f488b4e1)."
- *Next_upgrade:* "L5 on the §2 5-pt + Independence overlay landed on SIGNAL DASHBOARD, with STATUS under the 75% trigger (24,412 B) at the review read. Log OTTO-12's 10/01 attempt in-row at the next OTTO session."

**F. Cross-agent:** ① The 10/01 OTTO cluster has no wake. Owner: PROME (spawn) / OTTO. ② CRMT bridge-4. Owner: BROCK. ③ Re-key the profile trigger. Owner: DAEDALUS.

---

## CRUISE — L3 M

**A. Claims tested (the carry-in first)**

**Demote L3→L2 condition, applied literally.** It fires only if (i) the 2026-09-29 print has occurred AND (ii) no CRUISE session followed it.
- (i) **TRUE.** 8-K acc `0000815097-26-000104` Ex-99.1 at 09:16 ET and 10-Q `…-000107` at 11:06 ET, 2026-09-29 (`c69daded1`).
- (ii) **FALSE.** CRUISE graded the print at 11:35 ET the same day (`c69daded1`): CRU-07 (70%) CONFIRMED, CRU-08 (80%) CONFIRMED, CRU-10 (60%) CONFIRMED level-only, CRU-09 OPEN to 10/03 (DOCKET L454). The L0 drain ran the same day (`68a9d3aec`).
- **Verdict: DEMOTE DOES NOT FIRE.** Conf M→H "at that same read" is due now; see E.

| Other claims | Verdict | Locator |
|---|---|---|
| CCL Q3 = 9/29 CONFIRMED | TRUE | above |
| W2 ⑰ discharged 9/19; VX-CRU-04 re-cut + re-scored GREEN(1) | TRUE | `VX.tsv:5` |
| VX-CRU-06 RED conjunction named unrepaired | TRUE, still | `VX.tsv:7` "Registered, not repaired"; VX.tsv untouched since 9/20 |
| Measure the Big-3 denominator | OPEN | `VX.tsv:5` "THE DENOMINATOR IS UNMEASURED" |
| Profile clock 2026-10-03 | NOT MIRRORED | `profiles/CRUISE.md:5` still reads 9/26, so two clocks exist |
| **NEW: header over a stale body** | | The STATUS header is 9/29 (`:3`), but the matrix row `:75`, price `:31` and `:95` still read "$21.84 (9/18) … $0.10 from RED" and "print … 10 days out". Live check, yfinance closes: min 9/18–10/01 = **$21.79 on 9/24**, RED $21.7425 **never breached**; CCL $25.07 on 2026-10-01 (FORGE fetch.py). |
| **NEW: STATUS regrowth** | | 22,781 B (9/19 `ff54bde46`) → **28,475 B = 87%**, rotation_due=1 |
| **NEW: outbox root 30 packets** | | oldest `2026-08-14_to-WILL_*` ×3 |

**B. Ladder walk:** L1 PASS · L2 PASS (KB/PREDICTIONS +0d, VX/FLOW +9d per `ledger_staleness.py CRUISE`) · L3 PASS on all four legs: matrix (`STATUS.md:73-77`), exit rules (TRADE.md, root rule #5 noted), predictions **resolving on time at primaries** (3 graded on print day), dated falsification surface (VX bands, CRU-09 frozen resolver) · L4 FAIL: both TRADE rows WATCH, no proposal (`TRADE.md` 9/20 PM block). TERRY exchanges are signals, not proposals.

**C. Reachability:** the demote condition carried an occurrence precondition this time, and it resolved cleanly. No recurrence. CRU-09 has a wake (L454, 10/03). The denominator and VX-06 legs are in-tree.

**D. Profile trigger:** **FIRED** on both legs: the event (print 9/29) and >21d (9/26). Event-keyed was correct.

**E. Proposed row:** **L3 · H.** Reason: the L3 legs are now verified on a live event. The print was graded the same day at SEC primaries with registered resolvers and no re-tuning.
- *Gaps:* "CCL Q3 graded 9/29 at SEC primaries: CRU-07/08/10 CONFIRMED, CRU-09 OPEN to 10/03 (L454). STATUS body under the 9/29 header still carries the 9/18 VX-CRU-01 reading ($21.84, '$0.10 from RED') and 'print 10 days out'. RED never breached (min close $21.79, 9/24). VX.tsv untouched since 9/20. VX-CRU-04 denominator UNMEASURED; VX-CRU-06 RED conjunction unrepaired. STATUS 28,475 B (87%, rotation due). Outbox root 30 packets, oldest 8/14. No proposal fed."
- *Next_upgrade:* "Re-read VX-CRU-01 and the Nearest-triggers line post-print; grade CRU-09 by 10/03; rotate STATUS to <22,785 B. L4 on a proposal fed through TERRY under root rule #5."

**F. Cross-agent:** ① NCLH Q3 pre-announce `SIG-W-20261001-028` + WALTER R3 verdicts are unread in inbox. Owner: CRUISE. ② CRU-09 grade by 10/03. Owner: CRUISE (wake: PROME L454). ③ Profile clock. Owner: DAEDALUS.

---

## Cohort findings

1. **PR#6's anchor defect did not recur in contradicted form.** All three event-keyed gates (CRUISE demote, WAL Conf, FLG Conf) carry an occurrence precondition, and CRUISE's resolved cleanly. One partial residue remains: FLG's "NOT-ADJUDICATED before that date" and its profile trigger are date-keyed.
2. **A new DAEDALUS-authored defect: OTTO's L5 item 1 is stricter than canon.** It requires a standing <70% while rule 5 owes nothing below 75%. A desk can fail the leg while owing nothing.
3. **Rotations followed by fast regrowth (PAT-055), 3 of 5 desks:** WAL +11,070 B in 4 days, CRUISE +5,694 B in 10 days, OTTO +586 B in 2 days.
4. **Outbox roots as a register nobody grades:** CRUISE 30 and WAL 12 (oldest 8/07). Neither FLEET_MAP row mentions them.
5. **The verification perimeter was wrong (OZK):** a group-name `comm` certified "every KB group appears" while two rows were missing. This is `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.
6. **All 5 profile triggers FIRED** (OTTO's is probable). The 4 profiles dated 9/05 and the 8/07 WAL profile are all stale.
