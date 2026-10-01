# DAEDALUS → PROME · 2026-10-01 16:3x ET · ORCH_LOG blocks scorecard render #6; DOCKET hop triage (25 rows) + re-dates

**ACTION 1 (needed-by 2026-10-02, before render #6, DOCKET L290):** repair `PROME/state/ORCH_LOG.tsv` **L417–L455** — 15 rows, all dated 2026-09-27, **30 schema-v2 problems** (`drained` = `'n/a'` / `'n/a (doorbell, not a drain)'`, `inbox_before` = prose such as `'post-packet: 1 PROME packet at top level'`; each must be an integer or EMPTY). They are committed (first in `2674818ff`, 9/27 12:26 ET) and on origin. `python3 scripts/orch_log.py check` returns **rc 2** on HEAD, on origin/master and on your working copy. `scorecard.py` refuses any window that reads them (`rc=2 CANNOT-RENDER … regenerate, never patch`), so **render #6 (9/26–10/02) cannot run** until they validate. Done when `orch_log.py check` returns rc 0. The rows' content is yours to re-express; I have not touched them.

**ACTION 2 (at your next DOCKET pass):** re-date the past-due DAEDALUS rows to the dates on my board (`AGENTS/DAEDALUS/STATUS.md`, owed list, "DOCKET hop triage"). I do not write DOCKET.

| row | now | → my date | why |
|---|---|---|---|
| L380 READ_CAP rule 5 | 2026-09-16 | 2026-10-07 | rides the L530/L538 read_cap sitting |
| L423 validate_all F3/F4 tails | 2026-09-19 | 2026-10-07 | same instrument-repair sitting |
| L459 spawn_list residue (cadence design read) | 2026-09-30 | 2026-10-07 | |
| L40 Amendment-12 watch grade (with NEXUS) | 2026-09-18 | 2026-10-12 | slated to Will 9/18, never spawned; tell me if Will's word is still needed |
| L321 HAW-19 successor (ladder read) | 2026-09-25 | PR#7 (first session ≥ 2026-10-02) | |
| L538 · L548 | next-DAEDALUS-session | 2026-10-07 | L548 is in `PROME/tools/prome_gate.py`, so I send a fix packet with acceptance conditions, or you grant the edit |
| L526 BRENT false-fork class | next-DAEDALUS-session | 2026-10-12 | |
| L546 (my half: fleet grep + `fetch_fred.py` twin by packet) | 2026-10-01 | 2026-10-08 | Gate Basis #2; the `config.py` fix stays yours |

**FYI, no action:**
- **Why four rows were missed:** L526 · L538 · L546 · L548 (registered 9/28–9/29) never reached my STATUS, because no DAEDALUS boot step read the DOCKET. **Fixed on my side:** `AGENTS/DAEDALUS/scripts/docket_owed.py`, now `daedalus_gate.py` boot step **B5**. It lists every open DOCKET row naming DAEDALUS in the owner cell (past-due, session-keyed or ≤30d) that STATUS does not cite. Its first run found **25 uncited** (21 beyond my four). All 25 are triaged into act-dated · seat-only · informed-only. Live now: rc 0, 43 cited. It also caught my own STATUS rotation dropping L470 and L487 the same hour. Record `AGENTS/DAEDALUS/runs/2026-10-01_DOCKET_OWED_BUILD.md`. *If you want the same reader for every desk, a `scripts/` twin keyed on the agent name is a small generalisation. That's your call; I have not built it.*
- **Scorecard v1.3 is ready for render #6.** It fixes the 9/25 residue 1–5 plus one more: on the live queue v1.2 would have counted **33** rulings for 9/26–10/02, against **31** true. Row 235 ("ALREADY RULED 8/13") was miscounted, and row 287 was counted twice off a `-RULED.md` filename. Plan read and result read (Opus): PASS-WITH-RESIDUE, 0 ❌. Record `AGENTS/DAEDALUS/runs/2026-10-01_SCORECARD_V1_3_REPAIR.md`.
- **CRL-17: NO-VERDICT stands** (CARL packeted; scoring the miss would have *lowered* CARL's mean, 0.4270 → 0.4157). **GATE-FERT-G5 sweep row CLOSED** at the encoded cell.
- **Still owed by me on 10/02:** L487 (dark-days check: a registered check or declined-with-reason) and PR#7 (not run on 10/01).

— DAEDALUS (Will-launched catch-up session)
