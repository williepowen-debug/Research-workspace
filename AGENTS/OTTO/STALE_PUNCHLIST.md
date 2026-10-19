# OTTO — Forward To-Do (stale intel + fleet parity)

**Updated 2026-10-19 (s032); rewritten 2026-10-14 (s029). One list.** It replaces the June–September punchlist (verbatim → `archive/STALE_PUNCHLIST_2026-06-02_to_2026-10-14.md`) and `PEER_PARITY_ROADMAP.md` (verbatim → `archive/PEER_PARITY_ROADMAP_2026-06-09.md`). Both had gone stale while policing staleness.

**Rules:** an item closes with a date and a commit hash, never by deletion; closed items move to § Closed at the next rewrite. Re-audit this list at any closeout that touches an item. Sources: the s028 file review (`research/2026-10-14_file_review/`, reviews A/B/C), DAEDALUS `FLEET_MAP.tsv` (OTTO row, scored 10/01) and the s029 matrix check.

## Open — ranked by what a stale read would make OTTO do wrong

| # | Item | Why it matters | Source | Needs |
|---|---|---|---|---|
| 2 | **Target 10/30** (CATALYSTS). **THESIS v1.6** | The canonical thesis is ~7 weeks behind STATUS: First Brands "not yet entered", Tricolor deal counts, OTTO-34 figures, OBK reclassification, Manheim | Review A H1–H5, M1, M7–M9, M11–M14, L1–L14 | OTTO |
| 2a | — conflicts the s029 matrix exposed | V6: STATUS "LOW" vs THESIS "KILLED on first measurement"; SDT "one more REFUTE" (STATUS) vs "next two runs" (THESIS L11); V2 recovery magnitude has no case-level downgrade rung; OTTO-30 called "the one calibration win" (it scores 0.36 as-made) | s029 verifier | OTTO, in v1.6 |
| 2b | — fold the 9/30 failure-pattern rules from `PREDICTIONS_ARCHIVE.md` into THESIS § Predictions | Doc Ownership puts the rules in THESIS; they live only in ARCHIVE | Review A M13 | OTTO, in v1.6 |
| 4 | **By 11/30** (CATALYSTS). **OTTO-11 has no instrument, source, unit or perimeter**; 2.0–2.5% gap is a dead zone | Resolves 12/31 and cannot be graded as written | Review A M2 | OTTO, before 12/31 |
| 5 | **Ledger repair + refresh DONE10/19** (`cebaa8c61` evidence; s032 state). October1 attempt explicitly recorded as MISSED; actual attemptOctober19, not backdated | No exit found in scope; VRM post9/30UNKNOWN. Ally actual read + VRM recheck remain10/20 dated work | FLEET_MAP; review A M4; readiness/WAREHOUSE_READ | OTTO,10/20 follow-up |
| 6 | **By 11/30** (CATALYSTS). **True-at-creation check on the four early hits** (OTTO-01, -08, -09, -27, made 2/23, confirmed within weeks) | If any was already true, the 0.2400 as-made Brier flatters the book | s029 scoreboard | OTTO |
| 7 | **Remaining dashboard debt:** Bank Losses row needs dated/basis-specific sourcing; lender-watchlist disposition remains. March Fitch rows retired to cold in s031; the deal recovery instrument is explicitly separate | Stale rows read as live | Review B M11, M12, L8 | OTTO |
| 13 | `research/TIER2_FORENSIC_SCREEN_SPEC.md`: build "authorised" 7/25, no date | An owed build with no clock | Review C L9 | OTTO: schedule or drop |
| 14 | **Archive sweep — remainder** (27 Feb–Mar files moved s029, `c7361651a`; its commit message says 26): `research/WAL/` (5 files, 12.4 MB .docx; REGINALD holds a copy; hand over via PROME) · `workbook/STATUS_archive_2026{0325,0608,0725,0803,0814}.md` (links from STATUS_COLD would need re-pointing) · `research/outputs/` Feb packages stay (the research index points into them) | Root retirement rule | Review B L13–L17; review C | OTTO; WAL needs REGINALD/PROME |
| 19 | **DONE10/19** bounded historical release-date check (`cebaa8c61`): CVNA48/21/0 calendar days, olderCACC18 | Four observations, dependent/retrospective; no dependable cadence. October21/28 watches still future, not discharged | readiness/SHORT_REPORT_TIMING.md; LESSONS | Complete; move to Closed next rewrite |
| 17 | `TRADE.md` FROZEN since 7/4 | No action unless a position opens | — | dormant |

## Dated work (lives in `docket/CATALYSTS.tsv`; boot step 5 shows it)

**L708 DONE + CONSUMED10/19** (`a95429b7c`, PROME receipt and NEXUS acknowledgment verified): formal NO_INSTRUMENT unchanged, no further attribution study. **September SDART/BLAST + M&T reads DONE10/19 (`3a68e48c1`)**; panel has no turn and September covers5/9 deals. BlackRock10/16 confer outcome remains pending10/21. CRMT seventh-bridge STD10/22 (BROCK). Next: Ally/D&O10/20 · OTTO-07/T-7/suppression/§72110/21 · Carvana/CRMTbackstop510/28 · EART September~10/29 · THESISv1.610/30 · M&T narrow-custody10-Q check~11/05 · year-end readiness11/30. Full canonical set: `docket/CATALYSTS.tsv`.



## Waiting on others, or on Will

| Item | Who | Since | Where |
|---|---|---|---|
| L5 ruling on OTTO (both stated legs landed; placement is a block above the dashboard, not columns on it) | DAEDALUS | 2026-10-14 | packet `054aaf5b8` in `AGENTS/DAEDALUS/inbox/`; FLEET_MAP OTTO row |
| `research/WAL/` disposition (5 files, 12.4 MB; REGINALD holds a copy) | REGINALD / PROME | 2026-07-07 (DAEDALUS card) | item #14 |
| Veto, or not, the retirement of the FLG 8-K forwarding duty | Will (optional) | 2026-10-14 | `EDGAR_8K_MONITOR.md` footer |

## Closed

| Item | Closed | Commit |
|---|---|---|
| Ally comparison sheet: primaryQ2/Q3-2025 baseline and definitions, Q3 outcomes unfilled | 2026-10-19 s032 | `cebaa8c61` |
| #15: stale memory/history pruned; duplicate lessons consolidated; old boot memory preserved | 2026-10-19 s031 | `3a68e48c1` (archive/lessons), `80aab5846` (memory state) |
| #18: LESSONS rebuilt and boot3a installed, CLAUDEv3.0 | 2026-10-19 s031 | `3a68e48c1` |
| September10-D and M&T10/16 reads; settled calendar residue retired; STATUS headroom restored | 2026-10-19 s031 | `3a68e48c1` evidence; `80aab5846` state |
| #8: CARL independently checked 16/16 EART cells and SDART pair; BLAST ruling (a) computed-basis schema applied. Legacy parser branches remain outside this verification | 2026-10-19 s030 | `a95429b7c` |
| L708 commission #3: bounded attribution returned NO_INSTRUMENT; conditional equities MIXED | 2026-10-19 s030 | `a95429b7c` |
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
