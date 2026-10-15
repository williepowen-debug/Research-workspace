# OTTO — Forward To-Do (stale intel + fleet parity)

**Rewritten 2026-10-14 (s029). One list.** It replaces the June–September punchlist (verbatim → `archive/STALE_PUNCHLIST_2026-06-02_to_2026-10-14.md`) and `PEER_PARITY_ROADMAP.md` (verbatim → `archive/PEER_PARITY_ROADMAP_2026-06-09.md`). Both had gone stale while policing staleness.

**Rules:** an item closes with a date and a commit hash, never by deletion; closed items move to § Closed at the next rewrite. Re-audit this list at any closeout that touches an item. Sources: the s028 file review (`research/2026-10-14_file_review/`, reviews A/B/C), DAEDALUS `FLEET_MAP.tsv` (OTTO row, scored 10/01) and the s029 matrix check.

## Open — ranked by what a stale read would make OTTO do wrong

| # | Item | Why it matters | Source | Needs |
|---|---|---|---|---|
| 2 | **THESIS v1.6** | The canonical thesis is ~7 weeks behind STATUS: First Brands "not yet entered", Tricolor deal counts, OTTO-34 figures, OBK reclassification, Manheim | Review A H1–H5, M1, M7–M9, M11–M14, L1–L14 | OTTO |
| 2a | — conflicts the s029 matrix exposed | V6: STATUS "LOW" vs THESIS "KILLED on first measurement"; SDT "one more REFUTE" (STATUS) vs "next two runs" (THESIS L11); V2 recovery magnitude has no case-level downgrade rung; OTTO-30 called "the one calibration win" (it scores 0.36 as-made) | s029 verifier | OTTO, in v1.6 |
| 2b | — fold the 9/30 failure-pattern rules from `PREDICTIONS_ARCHIVE.md` into THESIS § Predictions | Doc Ownership puts the rules in THESIS; they live only in ARCHIVE | Review A M13 | OTTO, in v1.6 |
| 4 | **OTTO-11 has no instrument, source, unit or perimeter**; 2.0–2.5% gap is a dead zone | Resolves 12/31 and cannot be graded as written | Review A M2 | OTTO, before 12/31 |
| 5 | **OTTO-12 10/01 attempt never logged** | DAEDALUS map row carries it; Ally Q3 10/20 is the next read | FLEET_MAP; review A M4 | OTTO, 10/20 |
| 6 | **True-at-creation check on the four early hits** (OTTO-01, -08, -09, -27, made 2/23, confirmed within weeks) | If any was already true, the 0.2400 as-made Brier flatters the book | s029 scoreboard | OTTO |
| 7 | **Dashboard refresh**: Fitch ANL and recovery rows are Mar-2026 data; the Bank Losses row has no dates or total; the lender watchlist was rotated to cold `[STALE]` and needs a rebuild or a retirement | Stale rows read as live | Review B M11, M12, L8 | OTTO |
| 8 | **Seasoning repair not independently verified**; CARL's BLAST ruling (a/b) pending | The 🔴 39-of-39 row stands on it | s028 GAPS | OTTO / CARL |
| 13 | `research/TIER2_FORENSIC_SCREEN_SPEC.md`: build "authorised" 7/25, no date | An owed build with no clock | Review C L9 | OTTO: schedule or drop |
| 14 | **Archive sweep — remainder** (27 Feb–Mar files moved s029, `c7361651a`; its commit message says 26): `research/WAL/` (5 files, 12.4 MB .docx; REGINALD holds a copy; hand over via PROME) · `workbook/STATUS_archive_2026{0325,0608,0725,0803,0814}.md` (links from STATUS_COLD would need re-pointing) · `LESSONS.md` (Will's call, parked since June) · `research/outputs/` Feb packages stay (the research index points into them) | Root retirement rule | Review B L13–L17; review C | OTTO; WAL needs REGINALD/PROME; LESSONS needs Will |
| 15 | `MEMORY.md` findings/references contradict each other (Verita "blocked" vs working; superseded entries) | A boot read that disagrees with itself | Review B M3–M5 | OTTO, at closeout |
| 17 | `TRADE.md` FROZEN since 7/4 | No action unless a position opens | — | dormant |

## Closed

| Item | Closed | Commit |
|---|---|---|
| §2 universal 5-pt handle + Independence (DAEDALUS card priority 2; L5 gate leg) | 2026-10-14 s029 | MAINTENANCE (c) |
| WINTERKORN spec + memory refresh; docket archive split (review C H3/M3/M4/M5/M6/M8) | 2026-10-14 s029 | `8aff72737` |
| PREDICTIONS_ARCHIVE as-made scoreboard + OTTO-04 / OTTO-30 post-mortems (review A M10) | 2026-10-14 s029 | this commit |
| As-made markers on 7 ledger rows, each from git first appearance (OTTO-05 and OTTO-30 written at 60%) | 2026-10-14 s029 | closeout commit |
| OTTO-33 re-examined on its own overdue trigger: 68% → 60% (instrument silent 76 days; ECF 162 read) | 2026-10-14 s029 | closeout commit |
| `EDGAR_8K_MONITOR.md`: frozen bank-watchlist half archived verbatim; FLG cc duty (self-assigned 8/27, never run) retired with reason; method half kept, live users refreshed | 2026-10-14 s029 | this commit |
| `RESEARCH_STATUS.md`: index re-synced (RP-OTT-1.7, 2.5, 3.3, 5.1), queue rebuilt (2 resolved, 1 done, 1 retired, 2 added), Feb vector tables archived | 2026-10-14 s029 | this commit |
| Dead stub scripts archived (`abs_issuance_tracker.py`, `extension_proxy.py`) and `VX_HISTORY.tsv` FROZEN-bannered (items 9–10; closed late — done at `765ee7534`, the list kept them open for three hours) | 2026-10-14 s029 | `765ee7534` |
| Boot shows days since the last WINTERKORN run (🟠 DUE at ≥7; fails closed on an unreadable LAST RUN; 5-case guard test) | 2026-10-14 s029 | this commit |
| Charter version-stamp drift (DAEDALUS F-2) | 2026-09-12 s022 | — |
| Dead `AGENTS/SIGNALS.md` append instruction | 2026-09-02 | — |
