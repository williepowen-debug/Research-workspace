# Agent Profile — VULCAN

**Built by:** DAEDALUS · **Body:** 2026-08-07, refreshed 2026-09-05, **WHOLE refresh 2026-10-08** (2026-10-08 16:52 EDT from `date`; pulled forward from the owner-dated 10/12 slot, L490) · **Method:** Mode-A, three fresh Opus readers over file clusters (V1 core docs + consumption leg · V2 ledgers, docket, registry, code, guards run both directions · V3 delta since 9/05, every 9/05 claim re-graded), DAEDALUS synthesis + spot-verification. Reader slices (PAT-100 companions): `VULCAN_REFRESH_2026-10-08_READER_V{1,2,3}.md`. Prior body: `_prior/VULCAN_2026-09-05.md` (26 claims: 7 still true · 16 changed · 2 false · 1 unverifiable).
**Staleness trigger:** refresh at the **10/28 EXIT_PROTOCOL §7 re-derivation** or **21 days (2026-10-29)**, whichever first; or at once if a kill-rail leg fires.

## 1. Identity
Market desk: the AI-capex / semiconductor / memory cycle as **systemic-risk transmission** through five channels S1–S5 (concentration · memory · power demand · Taiwan chokepoint · financing). Composite **14/25** (from 15 at the 10/01 MU FQ4 grade, S2 3→2), no channel fired, thesis-kill count **1 of 4** (the 4th leg, financing, was ADDED 9/29, so 1/3→1/4 is by addition, not evidence) (`STATUS.md:30,54,72`; `EXIT_PROTOCOL.md:21-26`).

## 2. File anatomy — where the richness lives
| File | Size / role |
|---|---|
| `THESIS.md` | 62.6 KB: stage tables + the NVDA guaranty mechanism. Richest analysis. ⚠️ `:64` contradicts `STATUS.md:75` on which S1 test is live |
| `CLAUDE.md` | 82 KB: its FILES table (`:229-273`) works as the engineering log. ⚠️ `:259` says the GPU ledger has 0 rows (it has 10 since 10/02) |
| `LESSONS.md` | L-01…L-42 (L-42 added 10/08: Nasdaq-100 membership had CRWV/ORCL backwards) |
| `STATUS.md` | 106 lines, the matrix (`:20-30`) and the exit triad |
| `EXIT_PROTOCOL.md` | the kill rail. ⚠️ header `:3` "Newest entry 10/01" while a 10/08 entry sits at `:140` (same defect VULCAN fixed 9/25) |
| `TRADE.md` | "No book … not yet" (`:3`); unchanged since 8/27 (42 days), still says every channel = 3 |
| `workbook/` | 10 data ledgers + SCHEMA. **No `Last real data refresh:` header and no `LEDGER_GLOB` anywhere.** `S2_SERIES.tsv` 45 days stale (8/24), unbannered, 0 of 8 scheduled readings taken |
| `tools/` | `mag7.py`, `semi_watch.py`, `edgar_watch.py`, `gpu_panel.py`; `boot.py` at root |

## 3. Per-dimension local representation
- **Convergence:** 5-channel 0–5 matrix in STATUS, composite /25.
- **Predictions:** 17 registered · 12 resolved · **5 OPEN** (08, 10, 13, 15, 17). MU FQ4 graded 10/01: 02 HIT · **11 FALSIFIED** · 12 HIT (composition disagreement recorded) · 14 HIT; the sheet was written before the print and untouched above its grades afterwards (V3, git-verified). The four graded rows are still in the live file (archive owed, self-listed).
- **Falsification (§3b inventory, V2):** 26 surfaces: 18 CURRENT · 5 stale by own stamp · 1 unstamped · 2 spent/frozen. **S2 kill leg part 2 is unmeasurable** while `S2_SERIES` is stale.
- **Trade:** no book; per-channel "Trigger to propose" cells exist but are 42 days stale.
- **Signals / consumers:** WATT (55/32 GW wording current), NEXUS (14/25, 34.54% / −5.07pp current), TERRY (card L590; took the 10/08 correction). **ZHAO and VIOLET no longer credit VULCAN** (the 9/05 profile's two other proofs are gone; VIOLET now says "HENRY owns" equity concentration). **VIOLET's last absorbed VULCAN read is 9/02's "32.87% falling, breadth +5.17pp" (`board_log.tsv:96`); VULCAN now reads 34.54% and rising, breadth −5.07pp; VULCAN's 10/01 packet is unread in VIOLET's inbox** (verified).

## 4. Deviations from standard (+why)
No two-clock ledger headers or LEDGER_GLOB (predates the convention; never adopted) · rail header kept by hand · the GPU instrument's contract tier has no public quote, so the spread it was designed for cannot be graded (built 9/06, panel frozen 9/13, first rows 10/02).

## 5. DO NOT TOUCH
The pre-committed Friday `mag7.py` cadence slots (5 of 8 on 10/09) · the GPU-panel freeze (9/13) · the MU FQ4 grading sheet above its grades section · the Will-approval language anywhere a trade path is named.

## 6. Maturity snapshot (input to PR#8, 10/15; not a re-grade)
| Leg | Evidence | Read |
|---|---|---|
| L3 | matrix + exit triad + predictions resolving (12 of 17) + dated rewrite trigger (EXIT §7 ~10/28) | MET |
| L4 (ruling A) | "No book … not yet": passes only on "signals reach a consumer" (WATT, NEXUS, TERRY verified); TRADE.md's stale "every channel = 3" is the cell a ruling-A check reads | **AT RISK at 10/15**: holds on the consumer leg, fails if TRADE is read as the surface |
| L5 | S2 series 45 days stale; TRADE stale; an outside desk (TERRY) caught an error before VULCAN did (10/08) | NOT MET |
| Conf | gate "one reader-side consumption confirmed at the reader's artifact": still met (3 readers) | **H holds** |

## 7. Findings and open questions (route to VULCAN unless marked)
1. `tools/edgar_watch.py` assumes MU FY ended 8/27; it was a **53-week year ending 9/03**, so the 10-K window is computed 10/02–10/22 instead of 10/09–10/29, and from 10/23 to 10/29 an unfiled 10-K reads "not open" rather than overdue (V2 recalculated; the test suite has no 53-week case). Tomorrow's MU 10-K re-check row depends on this window.
2. **6 named corrections unreceipted** for VULCAN (two from September); `boot.py` doesn't run the corrections check.
3. Silent-pass guards (V2 broken-input tests, 6 of 26): impossible date passes the schema validator; the catalyst neighbour scan prints ✓ after failing to read HAWK's file, and misses a `Date`-cased header; `gpu_panel.py` accepts a 26-day-old hand price as new.
4. Stale state in boot-read files: `CLAUDE.md:259` and `GPU_INSTRUMENT_SPEC.md:4` (0 rows vs 10); `EXIT_PROTOCOL.md:3` header; `NEXUS_BRIEF.md:64,70` standing table (VIOLET Mag-7 33.55% as of 9/1; HAWK's August TSMC figure).
5. `semi_watch.py:200` stamps UTC, not the ET trade date; no saved row is wrong yet (all runs before 8 p.m. ET).
6. **DAEDALUS's own:** the 10/01 PR#7 re-score was never sent to VULCAN (`STATUS.md:5` still cites 9/17); the tripwire candidate (old profile F-1) went unruled at 9/12 and PR#7.
7. **For L628 (PROME's row):** the live register now carries 3 rows on 10/09, not 4; see `builds/summons_fix_2026-10-08/README.md` apply-time note.
Open: does VIOLET's live concentration view depend on the 9/02 read (VIOLET's to answer)? Will ZHAO re-cite VULCAN or has ownership moved?
