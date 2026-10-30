# REGINALD whole-profile refresh — 2026-10-30

Status: whole-profile comprehension COMPLETE (seventh of the accepted nine: AEOLUS 10/21, HAWK 10/22, HOMER 10/28, WAL 10/30, BROCK 10/30, CREED 10/30, REGINALD 10/30); two remain (FALCON, MIDAS; RESOLVE_BY 2026-11-07). Queue clock in `sweeps/REGISTRY.tsv` advances only after the whole scope.

## Runtime, authority and preservation

Claude Code, Opus 5.5, DAEDALUS desk session 3 (Will-launched; booted 16:31 ET). Commissioned by Will in-session ("yes go ahead", 16:40 ET, on the boot report's REGINALD recommendation). Four read-only Opus readers launched ~16:41 at HEAD `9f0975860`: R1 architecture/spine, R2 ledgers/guards, R3 flows/consumers/ladder, R4 per-bank tree/reports/research. Reports and index: `runs/2026-10-30_REGINALD_REFRESH_READERS/` (`REGINALD_REFRESH_READER_REPORTS.md`; `R1_ARCHITECTURE.md` 33,322 B §I · `R2_LEDGERS_GUARDS.md` 30,177 B §I · `R3_FLOWS_REVIEW.md` 33,485 B §11 · `R4_BANK_TREE.md` 27,484 B §H). REGINALD not live (last REGINALD commit `9ebedf3e2` 10/30 09:15); every reader recorded `git status -- AGENTS/REGINALD/` empty at start and end; mutations ran on scratch copies under `/tmp/claude-1000/reginald-r*/`. Prior profile preserved at `profiles/_prior/REGINALD_2026-10-30_before_refresh.md` (crc32 1434954275).

## Result

`profiles/REGINALD.md` replaced whole (prior body vintage 8/07, two banners to 10/21). FLEET_MAP REGINALD row re-cut: **L4 / H retained**, Last_scored 2026-10-30. The 10/22 row was stale: four of its named gaps were closed by REGINALD 66 minutes after it was written (`233ba18f7` 11:31 → `f8405c6f2` 12:37), and its Next_upgrade condition was met. **L3 dated-falsification leg adjudicated PASS** (it was AT RISK). L5 per-leg (profile §6): clean closeouts PASS with debt, current PARTIAL; **L5 NOT AWARDED**. Before-image in FLEET_MAP_HISTORY; directory regenerated. `upgrades/REGINALD_CARD.md` was already CLOSED AS A QUEUE (8/17); no change.

Of the prior profile's big items: the MI3/OZK repair is DONE (basis re-derived; 37.6% kill-on-sight in the charter) with two residual carriers; the per-bank "F1 layer" is CLOSED by retirement; THESIS v1.4 is retired to a stub with STATUS thesis-canonical; the 15-packet backlog is gone (inbox drained at each of the last 5 closes).

## Verified by DAEDALUS at the artifact before shipping

| Finding | Reader | Check | Verdict |
|---|---|---|---|
| Kill rail re-derived and dated; CBRE defined and retired | R1, R2, R3 | `STATUS.md:87`, `:93` | HOLDS |
| REG-T-07 live reading | R1, R2 | `STATUS.md:109` 12.16% Sept (secondary) | HOLDS |
| Charter 24,977 B = 77% | R1 | `wc -c`; `read_cap_check --agent REGINALD` | HOLDS |
| read_cap rc 1 from one BOARD class member | R1 | same run: rc=1, 1 over budget 39,509 B (121%), companion `WALTER/reading/SIG-W-20260619-008.md` 67% does not shadow | HOLDS |
| READS attestation stale; channel reads undeclared | R1 | `PROME/tools/reads_check.py --agent REGINALD` → STALE ATTESTATION; `grep REGINALD_CHANNEL READS.tsv` = WAL's own row only (:559) | HOLDS |
| thresholds.py cannot fail | R2 | code: only `sys.exit(1)` at `:18` (import); `main()` returns nothing; `boot.py:47` category ALERTS | HOLDS (by code; fixture is R2's E10) |
| VX row rot contradicting STATUS | R2 | `VX.tsv:47` (15.01 GREEN 0bp), `:64` (15.02 ORANGE 4.67%) vs `STATUS.md:113` 4.99%, `:115` +5bp; header lines 1–6 disclose "other rows retain own vintages" | HOLDS (disclosed at header, wrong at cell) |
| KRE 68P absent from trade surfaces | R3 | `FORGE/STATUS.md:71` (owner UNKNOWN, D-74); grep TRADE/POSITIONS → no 68P | HOLDS |
| 37.6% unflagged in report + KB | R4 | `reports/2026-07-30_bank-side-HY-attribution.md:122`; KB rows -075/-098/-115/-129/-133 carry 37.6; charter `:127` kill-on-sight; DECK_EVIDENCE:25, STATUS_MATRIX:35, LESSONS:31 are flagged | HOLDS |
| DOCKET L621/L711 delivered but PENDING | R3 | `c6bb09ab0` 10/23 (CUBI Q3 grade); `registry/NOTES.md:183` (10/16 non-session reading); DOCKET lines 621, 711 PENDING | HOLDS |
| WAL seam exception | R1 | `STATUS.md:94` restates WAL NCO 30bp vs `:30` pointer-only rule | HOLDS — routed as an owner question, not a defect |

## Where the readers were wrong or over-reached, or where I narrowed

- R1 listed the WAL-seam exception as a defect; it is the 10/22 re-keying DAEDALUS asked for, written with a dated source. Routed as "confirm intended", not as a fix.
- R4 counted 46 retirement-eligible research files on the mechanical letter; its own judgment is ~20 genuine. The packet uses ~20 and points at R4 §C.
- R3's "graded 10/23" for L621 was checked against the desk commit, not against PROME's consumption record.

## Routing

- REGINALD owner packet: `AGENTS/REGINALD/inbox/2026-10-30_from-DAEDALUS_profile-refresh.md` — 14 items (1–4 decide L5) + an amendment to my same-day falsification-#5 ask (the `V1V3-ACCELERATE` rename is conditional on WALTER per `registry/NOTES.md:341-346`; R2 rank 3). PAT-102 reconciliation: R1 H ranks 1→6, 3→5, 5→PROME 8, 6→7, 7→14, 8→12, 9→amendment, 10–16→13; R2 H ranks 1→1, 2→2, 3→amendment, 4→10, 5→8, 6→9, 7–8→11, 9–11→13 (partial; TRADE.md :7 vintage and KB header carried in R2 report), 12→PROME 8, 13→DAEDALUS, 14→13; R3 §10 ranks 1→map, 2→4 + PROME 1, 3→7, 4→PROME 4, 5→13 (cold-surface drift-grep scope; carried in R3 report), 6→PROME 7, 7→PROME 6, 8→7, 9→REGINALD's own next boot (no ask), 10→profile §7 (FLG refresh); R4 G ranks 1–2→3, 3–5, 7–8→13, 6→none before 11/07, 9→DO-NOT-TOUCH.
- PROME: `PROME/inbox/2026-10-30_from-DAEDALUS_reginald-profile-refresh.md` — COMPLETION; KRE 68P owner; READS rows; read-cap class-row remedy (choice of PROME manifest change or DAEDALUS tool change); DOCKET L621/L711 + GATE last_checked; charter-trim row; topology edges; GIBBS wake; JWT (informed).
- DAEDALUS-side → STATUS, Production Review 11/04: `ledger_staleness.py` reads header clocks only (row-level `Last_Updated` ungraded; perimeter line should say so) and keys `--trade` freshness on STATUS, not the FORGE reconcile vintage; `falsification_scan.py --help` runs a full scan; `read_cap_check` companion-shadowing if PROME picks that remedy.
- Design lessons: PAT-110 extended (desk-local form: the orchestrator decided the check's rc does not matter); PAT-138 extended (my own map row overtaken in 66 minutes).
