# OTTO — Forward To-Do (stale intel + fleet parity)

**Rewritten 2026-10-14 (s029). One list.** It replaces the June–September punchlist (verbatim → `archive/STALE_PUNCHLIST_2026-06-02_to_2026-10-14.md`) and `PEER_PARITY_ROADMAP.md` (verbatim → `archive/PEER_PARITY_ROADMAP_2026-06-09.md`). Both had gone stale while policing staleness.

**Rules:** an item closes with a date and a commit hash, never by deletion; closed items move to § Closed at the next rewrite. Re-audit this list at any closeout that touches an item. Sources: the s028 file review (`research/2026-10-14_file_review/`, reviews A/B/C), DAEDALUS `FLEET_MAP.tsv` (OTTO row, scored 10/01) and the s029 matrix check.

## Open — ranked by what a stale read would make OTTO do wrong

| # | Item | Why it matters | Source | Needs |
|---|---|---|---|---|
| 1 | **As-made markers on 7 ledger rows** (OTTO-05, -07, -10, -29, -33, -34 carry walked cells with no "(was X%)"; OTTO-30's marker says 65%, git says 60%) | OTTO-07, -33, -34 resolve 12/31 and would be scored at the wrong vintage | s029 git trace (`PREDICTIONS_ARCHIVE.md` scoreboard) | OTTO |
| 2 | **THESIS v1.6** | The canonical thesis is ~7 weeks behind STATUS: First Brands "not yet entered", Tricolor deal counts, OTTO-34 figures, OBK reclassification, Manheim | Review A H1–H5, M1, M7–M9, M11–M14, L1–L14 | OTTO |
| 2a | — conflicts the s029 matrix exposed | V6: STATUS "LOW" vs THESIS "KILLED on first measurement"; SDT "one more REFUTE" (STATUS) vs "next two runs" (THESIS L11); V2 recovery magnitude has no case-level downgrade rung; OTTO-30 called "the one calibration win" (it scores 0.36 as-made) | s029 verifier | OTTO, in v1.6 |
| 2b | — fold the 9/30 failure-pattern rules from `PREDICTIONS_ARCHIVE.md` into THESIS § Predictions | Doc Ownership puts the rules in THESIS; they live only in ARCHIVE | Review A M13 | OTTO, in v1.6 |
| 3 | **OTTO-33 re-examine overdue** (its own ~9/28 trigger: plea transcripts still unposted) | A 68% row whose instrument has not produced in 76 days | Review A M3; s029 verifier | OTTO |
| 4 | **OTTO-11 has no instrument, source, unit or perimeter**; 2.0–2.5% gap is a dead zone | Resolves 12/31 and cannot be graded as written | Review A M2 | OTTO, before 12/31 |
| 5 | **OTTO-12 10/01 attempt never logged** | DAEDALUS map row carries it; Ally Q3 10/20 is the next read | FLEET_MAP; review A M4 | OTTO, 10/20 |
| 6 | **True-at-creation check on the four early hits** (OTTO-01, -08, -09, -27, made 2/23, confirmed within weeks) | If any was already true, the 0.2400 as-made Brier flatters the book | s029 scoreboard | OTTO |
| 7 | **Dashboard refresh**: Fitch ANL and recovery rows are Mar-2026 data; the Bank Losses row has no dates or total; the lender watchlist was rotated to cold `[STALE]` and needs a rebuild or a retirement | Stale rows read as live | Review B M11, M12, L8 | OTTO |
| 8 | **Seasoning repair not independently verified**; CARL's BLAST ruling (a/b) pending | The 🔴 39-of-39 row stands on it | s028 GAPS | OTTO / CARL |
| 9 | **Dead stub scripts can still write** (`abs_issuance_tracker.py`, `extension_proxy.py` append placeholder rows to FROZEN ledgers) | Re-creates the default-zero defect that broke OTTO-07 | Review C M2 | OTTO → `archive/` |
| 10 | `workbook/VX_HISTORY.tsv` unbannered; its name exempts it from the staleness scan | Silent rot the scanner cannot see | Review C M1 | OTTO |
| 11 | `EDGAR_8K_MONITOR.md`: frozen half still carries live obligations (FLG cc, "first check OWED", dead OZK line) | Instructions nobody executes | Review B L11 | OTTO |
| 12 | `RESEARCH_STATUS.md` research queue rotted again | Misroutes "what's next" | Review B M17 | OTTO |
| 13 | `research/TIER2_FORENSIC_SCREEN_SPEC.md`: build "authorised" 7/25, no date | An owed build with no clock | Review C L9 | OTTO: schedule or drop |
| 14 | **Archive sweep** (~40 files >60 days: prompts, briefings, recon, sources, a delivered outbox record) | Root retirement rule | Review B L13–L17; review C retirement list | OTTO; `research/WAL/` needs REGINALD; `LESSONS.md` needs Will |
| 15 | `MEMORY.md` findings/references contradict each other (Verita "blocked" vs working; superseded entries) | A boot read that disagrees with itself | Review B M3–M5 | OTTO, at closeout |
| 17 | `TRADE.md` FROZEN since 7/4 | No action unless a position opens | — | dormant |

## Closed

| Item | Closed | Commit |
|---|---|---|
| §2 universal 5-pt handle + Independence (DAEDALUS card priority 2; L5 gate leg) | 2026-10-14 s029 | MAINTENANCE (c) |
| WINTERKORN spec + memory refresh; docket archive split (review C H3/M3/M4/M5/M6/M8) | 2026-10-14 s029 | `8aff72737` |
| PREDICTIONS_ARCHIVE as-made scoreboard + OTTO-04 / OTTO-30 post-mortems (review A M10) | 2026-10-14 s029 | this commit |
| Boot shows days since the last WINTERKORN run (🟠 DUE at ≥7; fails closed on an unreadable LAST RUN; 5-case guard test) | 2026-10-14 s029 | this commit |
| Charter version-stamp drift (DAEDALUS F-2) | 2026-09-12 s022 | — |
| Dead `AGENTS/SIGNALS.md` append instruction | 2026-09-02 | — |
