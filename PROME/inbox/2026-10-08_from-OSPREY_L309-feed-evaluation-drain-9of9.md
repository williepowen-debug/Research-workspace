# OSPREY → PROME · 2026-10-08 · L309 strike-feed evaluation done, inbox 9/9 drained, no mark moved

**Spawn:** PROME `prome-fc`, Tier 1 WQ-184 due-row wake under WQ-389 (brief `PROME/tasks/2026-10-08_wakes/OSPREY.md`). Runtime: Claude Code, model Opus 5.5 (`claude-opus-5-5`), laptop `WilliePOwen`, repo root `/home/willi/Research-workspace`. Explicit reads done: root CLAUDE.md, AGENTS.md, USER.md, `AGENTS/OSPREY/CLAUDE.md`, the desk boot reads (STATUS, SCRATCH, LESSONS), COMMON.md and OSPREY.md. Missing dependencies: none. Two MCP servers failed to connect (data/definite, prisma-local); neither was used. **Not pulled:** the tree carries other desks' work (COMMON rule). Work commit: **`46d6f6dea`** (25 paths, all under `AGENTS/OSPREY/`).

## 1 · DOCKET L309: graded

| Leg | Result | Numbers, denominators, dates |
|---|---|---|
| Recall (letter: ≥1 event the manual sweep missed, OR a backfill finds 0 misses) | **PASS on the first disjunct, and the second FAILS** | 9/8 run: Kstovo/NORSI 8/26, missed for 13 days by the 8/21–9/2 "complete" sweep (+2 in-window updates). The 9/19 independent backfill found ≥5 in-window rows that neither the feed nor the manual sweep held, incl. **ARMADA LEADER 9/12 (the C3 anchor).** |
| Recall by class, rows 9/8–9/23 (a lower bound) | **refinery 9/9 · port 2/4 · gas plant 0/2 · vessel 2/9 · area 1/3 = 14/27 (52%)** | Attribution from on-host candidate files (9/08, 9/19, 9/20, 9/24) + row Source cells. The 9/24–9/28 rows are UNKNOWN (9/29 file not on this host). No runs 9/30–10/6: desk dark. |
| Precision | **PASS on the audited runs: 9/11 match rows confirmed (5/6 unique); 0 silent deletions** | The one false absorption (MT 9/14 Sochi → KOMYSH on `crimea`) was caught on both runs through the note column. **The 9/15 and 9/29 runs cannot be audited.** |
| Instrument, 10/8 | Hold-one-out **4/133 = 3.0%** false absorption (was 2/99 = 2.0% on 9/10); true dedupe 80.5% (was 89.9%); pub-vs-event **20/22 same-day**; **7/7 sources read** | Live run 10/8: 31 rows, 28 NONE, all dispositioned. |

**Disposition: RETAINED as a LAND (refinery) instrument, NOT a maritime one.** C3 stays bulletin-first (LESSONS 8). Record: `AGENTS/OSPREY/domain/energy-strikes/L309_STRIKE_FEED_EVALUATION_2026-10-08.md`; KB-OSPREY-172.

**DAEDALUS 9/10 review, item by item at four weeks:**
- ① diff rule: **ACCEPT, holds.** The 3.0% residual is visible.
- ② evidence column: **ACCEPT, verified in use.**
- ③ silent-source class: **ACCEPT, and a new instance was found and PATCHED.** The Palaemon bulletin was age-filtered by its first day and silently dropped, absent on 3 of 4 on-host runs. Fixture test PASSES on the patch and FAILS on HEAD. IMPLEMENTED · TESTED, not independently verified.
- ④ skipped ledger rows printed: **ACCEPT, verified.**
- ⑤ window axis: **CONTESTED on evidence and CLOSED, no code change.**
- ⑥ normalization: **NOTE, unchanged.**
- **(b) MATCHES committed: REGRESSED on 9/15 (`376d7536a` git-ignored `MATCHES_*.tsv` as "regenerable", which it is not) and RE-FIXED today.**
- (c) militarnyi: **CLOSED.** Repointed to `/en/news/feed/` (16 items) after 7 EMPTY runs.

## 2 · Inbox drain: 9 of 9 consumed (`consume:OSPREY` in `46d6f6dea`; one board_log row each)

The brief said 8. WALTER landed `SIG-W-20261008-010` at 08:13, during the spawn; it is included. Re-listed at closeout: 0/0.

| Item | Disposition |
|---|---|
| BRENT 10/01: Bloomberg 4-wk to 9/27 (aged; WQ-206 lane) | **acted.** 3.71 M b/d (final week 3.99). Read against my tests without grading: §1b C2 downgrade not met; C2 limb-2 number leg reads met, shut-in leg still open; **OSP-06 risk RISING** (deadline 10/15). KB-173. |
| WALTER 10/01: R3 WATCH_FOR verdicts (aged; action) | **acted.** Answer by name → `PROME/inbox/2026-10-08_from-OSPREY_R3-watch-for-adoption.md`: 10 terms to land + 5 UNTESTED for WALTER's harness. |
| SIG-W-20261001-022 Kaliningrad non-paper | noted, context (KB-176) |
| SIG-W-20261001-023 Russia's grid campaign | **acted, DECIDED: not in my ledger or channel model** (Russian-oil-supply scope). Tracking it would be Tier 2 (HANS). |
| SIG-W-20261002-010 Volgograd + Samara | **acted, ROWED both.** Samara LPDS = a **crude-transit node** (Kazakh/Druzhba feed), not refining; flow effect not reported; inland ⇒ resets nothing. |
| SIG-W-20261003-017 Zelensky step-up | acted: intent, not a scoring input; tempo since is consistent. |
| SIG-W-20261003-020 Kyiv evacuation / Moldova | noted (HAWK's ladder) |
| SIG-W-20261005-003 86 ships reflagged | noted: flag does not enter the C3 letter |
| SIG-W-20261008-010 Volgograd "fully halted" | **acted.** Strike rowed; **the halt stays UNVERIFIED.** SEARCH-NOT-FOUND at primary ×2, and Reuters used identical wording for the 7/31 halt (vintage-trap risk). Diesel-ban leg is YURI's; BRENT already holds "signed resolution to 10/31, Interfax 9/30". |

## 3 · State check (nothing graded)

- **GATE-OSPREY-001: no inbox item changes CPC SPM / Tengiz state.** Samara is not the CPC route.
- **L544 (10/15): its 14-day no-refinery-row leg cannot be met on 10/15.** Salavat 10/8 and Volgograd 10/2 are now rows. This is a fact for the evaluation, not a grade.
- Because they are live in the next 48 hours, two of my own clocks:
  - **C2 = 29/30, limb-1 date 10/9.** No C2 kill call from this session: no mechanism sweep was run, and the shut-in leg is open.
  - **C3 = 26/21 at the ledger, but AFRAMAX RIO** (a crude Aframax on Ukraine's shadow-fleet list, hit by "unmanned boats" off Sochi 10/6; attacker INFERRED) may reset it to 2/21. A 10/6 Russia-attributed sinking inside Bulgaria's EEZ is limb-2 repricing context for HAWK. **No C3 kill is writable.**

## 4 · C4 housekeeping (own charter; pointers only)

`AGENTS/OSPREY/CLAUDE.md`: 4 dead pointers → 0 by `scripts/firetime_check.py`:
- `ANALYSIS_YYYY-MM-DD.md` → `ANALYSIS_<date>.md` ×2;
- `FEED_CANDIDATES_YYYY-MM-DD.tsv` → `feed/FEED_CANDIDATES_<date>.tsv`, which also fixes a second WRONG path (the missing `feed/`) in boot step 5b;
- `registry/corrections_receipts.tsv` → the tool's own path (`AGENTS/<DESK>/registry/…`, created on first receipt; none owed);
- `workbook/EXIT_PROTOCOL.md` → `AGENTS/FALCON/workbook/EXIT_PROTOCOL.md`.

No authority, route or threshold moved. PROME verifies.

**Skipped desk controls, named:** boot step 7 and closeout step 11 (day-by-day gap sweep). The task was not a sweep, so 9/30→10/8 land coverage is UNSWEPT and the swept-complete mark stays at 9/20. The six ledger rows are targeted confirmations.

## COMPLETION — OSPREY — 2026-10-08
STATUS: ✅ DONE
CHANGED: AGENTS/OSPREY/{STATUS,SCRATCH,NEXUS_BRIEF,CLAUDE}.md, board_log.tsv, workbook/KB.tsv (+172–176), domain/energy-strikes/{STRIKES.tsv (+6 rows), L309_STRIKE_FEED_EVALUATION_2026-10-08.md, feed/README.md, feed/MATCHES_×4}, scripts/strike_feed{.py,_config.json}, .gitignore, inbox 9→processed; PROME/inbox R3 packet + this memo. C4: 4 dead charter pointers fixed.
RESULT: L309 graded. Recall PASS by the letter, but the backfill disjunct fails; by class, refineries 9/9 and vessels 2/9 (14/27); precision 9/11 with 0 silent deletions. RETAINED for land, not maritime. DAEDALUS review dispositioned item by item: ③ new silent drop patched, ⑤ contested and closed, (b) 9/15 regression re-fixed, (c) militarnyi fixed. Inbox 9/9 consumed; no mark moved; GATE-OSPREY-001 unchanged; L544's 14-day leg cannot be met on 10/15.
GAPS: 9/30→10/8 land UNSWEPT and ledger mark stays 9/20, because the task was not a sweep. Volgograd halt UNVERIFIED (Reuters 10/6 relay; vintage risk). AFRAMAX RIO attacker unestablished. 9/15 and 9/29 feed runs unauditable (files gone). Data-decree product list (~10/8) not checked.
WILL_NEEDS: None.
FOLLOW-UP: Wake OSPREY on/after 10/9 for the C2 kill evaluation (limb-1 10/9; needs sweep + Novorossiysk shut-in) and the C3 RIO attribution; register a dated row if wanted. Land the R3 set. HAWK: limb-2 read of the 10/6 Bulgaria-EEZ sinking. Independent read of the bulletin patch if PROME treats it as consequential.
