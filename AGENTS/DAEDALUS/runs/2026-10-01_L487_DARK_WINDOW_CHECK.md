# L487 — dark-days-in-window check: BUILT as a descriptive instrument (2026-10-01 evening, for the 10/02 row; Will "okay can you do these now")

**Row:** `PROME/DOCKET.tsv` L487 half (b): "DAEDALUS has a registered check or a declined-with-reason." Half (a) (WATT's WATCH_FOR list) was encoded by PROME on 9/25. **Skeleton of record:** my 9/25 packet `PROME/inbox/processed/2026-09-25_from-DAEDALUS_cadence-and-watch-terms.md` §4, B1–B5, with N left to Will.

## 1. Decision: BUILD, not decline, but with no threshold
A decline would leave the WATT shape (an event inside a live test window while the owner was dark for weeks) with no reader at all. Half (a) fixes only PJM headlines; the class is any desk. **Build** it, but as a **measuring** instrument: it ranks every desk that holds a live test by its dark run and prints the figures. **It alerts only when a caller passes `--threshold N`, and N is Will's to set** (the same rule as the scorecard's L290 floor). Wiring it into PROME's boot report is PROME's call; I register it and hand it over.

## 2. Definitions (one source each, imported where one exists)
- **Live test** at a desk = an OPEN row in a prediction ledger registered in `AGENTS/DAEDALUS/scorecards/LEDGERS.tsv` (status `LIVE` rows of the registry only), **or** a `PROME/GATES.tsv` row whose state starts `LIVE` and whose owner cell names the desk. "Open" = `scorecard.bucket(status) is None`: the scorecard's terminal-token map, imported, never re-derived.
- **Dark run** = calendar days since the desk's last **own-authored** commit (subject starts with the desk name, e.g. `WATT:` or `WATT -> X`). PROME drains and WALTER deliveries into the desk's tree never count (B3); a spawned session committing under the desk's name does.
- **Replay** (`--as-of` before today): commits up to that date; a ledger row counts as open if it was made on or before that date and either is still non-terminal or its resolution date (the registry's date column, or the first ISO date of the outcome cell) is after that date. This is approximate and labelled as such.

## 3. Acceptance conditions (each a selftest fixture or a watched real run)
| # | Must |
|---|---|
| B1 ordinary | a desk with ≥1 open row and its last own commit D days ago prints one line with D, the open-row count and up to three row IDs |
| B2 overlap | many open rows at one desk ⇒ ONE line for the desk, never one per row |
| B3 wrong owner | a commit `PROME -> WATT: …` or `WALTER: deliver … WATT` does not reset WATT's dark run; `WATT: …` and `WATT -> PROME: …` do |
| B4 missing | a registered ledger absent, header lacking the status or made column, or an unparseable made date ⇒ a `CANNOT-EVALUATE` line naming the ledger and reason, never silence; zero ledgers evaluated ⇒ rc 2 |
| B5 concurrent | a desk named in `--live` prints `LIVE-UNCOMMITTED` instead of a dark figure; without `--live` the header says liveness was NOT CHECKED (a script cannot call ListAgents) |
| B6 threshold | no `--threshold` ⇒ rc 0, nothing flagged, the header says N is unset and is Will's; `--threshold N` ⇒ desks with a dark run ≥ N flagged ⏰, rc 1 |
| B7 terminal | a terminal row (`MISS`, `HIT`, `RETIRED` …) never makes a desk "in test" in live mode |
| FIRE (real) — **CORRECTED** | ~~`--as-of 2026-09-25` … last own commit 2026-09-06 … with WATT-11 open~~ — **wrong as written** (result read X1/X2): WATT booted 09:42 on 9/25, so that replay reads 0d; 9/06 is WATT-11's MADE date, not a commit; the last own commit before the gap was **2026-09-11**; WATT-11 now lives in an unregistered archive and cannot appear. **Corrected FIRE: `--as-of 2026-09-24` ⇒ WATT 13d dark since 9/11 with open tests (WATT-08/09/10).** |
| CLEAN (real) — **CORRECTED** | ~~WATT's last own commit was 10/01~~ (the 10/01 commits in WATT's tree were a VULCAN packet and a WALTER delivery, correctly not counted; result read X3). **Corrected CLEAN: live 10/01 ⇒ WATT 6d since 9/25**, matching `git log`. |

## 4. Evidence
- **Selftest 15/15**, rebuilt after the independent read: B3 now exercises the REAL filter (`own_dates`, which `own_commit_dates` calls); B7 asserts the exact open count (5), not whether an ID is printed. Fixtures were added for the threshold boundary (exactly N ⇒ flagged), git failure ⇒ rc 2, a RESOLVED gate absent from the output, WAL vs WALTER, ARCHIVE-status ledgers, made-after-as-of, sort order, graded-vs-event date, and unmapped tokens.
- **Mutation run (my own, on scratch copies):** 17 mutants. Every live guard fails at least one check: `(?!-)` · tag prefix · `\b` · both anchors · `≥` boundary · git-failure swallow · LIVE gate filter · owner substring · ARCHIVE include · made-after · sort · terminal-as-open · UNMAPPED-as-terminal · graded-date ignored · silent wrong-width. Two survivors are equivalent mutants: `^` alone or `match→search` alone, since each anchor guards the other.
- **Real fire (corrected):** `--as-of 2026-09-24` ⇒ **CREED 22d** (8 open; 5 before the graded-date fix) · **MIDAS 13d** · **WATT 13d** · VULCAN 11d. The reader verified each figure against `git log`, and `--threshold 7` at 9/24 flags exactly those four.
- **Real clean (corrected):** live 10/01 ⇒ 31 desks in test; longest MARCO 7d, then WATT 6d since 9/25.
- **Independent read** (Opus, scratch copies, own probes): X1–X7 ❌ and W1–W8 ⚠️, all dispositioned below. **The fixes were not re-read.** They are covered by the selftest and the mutation run, and that difference is stated here.

| finding | disposition |
|---|---|
| X1/X3 FIRE and CLEAN wrong as written | corrected in §3, original kept struck |
| X2 WATT-11 invisible (unregistered archive; its cell's first date is the made date) | **DECLARED R1**; the replay header now says LOWER BOUND |
| X4 event date read as resolution date | FIXED: `grade_date` prefers a date labelled `(graded)` |
| X5/X6 selftest checks that could not fail | FIXED: real filter exercised; exact counts asserted |
| X7 `[tag] SAM:` subjects missed | FIXED: one leading `[tag]` allowed |
| W1 permanent CANNOT noise from terminal rows | FIXED: only open-or-unmapped rows are reported (HENRY's 8 remaining are its own `RESOLVED-*` words, labelled as possibly terminal) |
| W2 unknown token counted terminal (`NEEDS_VERIFY`) | FIXED: unmapped counts OPEN (over-include, never hide) |
| W3 wrong-width rows silent | FIXED: counted and printed |
| W5 gate credited to role-note desks | ACCEPTED: errs toward inclusion, never hides a desk |
| W6 10 of 17 mutants survived | FIXED (above) |
| W7 UTC dates | FIXED: `--date=short-local` |
| W8 made-date from a hardcoded column list | DECLARED R3 (spot-checked: `Date` = creation date on 5 rows) |

## 5. Declared residue
- **R1** Replay reads today's files, so rows since moved to an unregistered archive are invisible (WATT-11 is the case). Replay is a lower bound and says so.
- **R2** "Own-authored" is a subject convention. `MIDAS-08 …`-style subjects (a row ID first) and unprefixed prose subjects do not count. 30-day measure: SAM 5 (now fixed by the tag rule) · MIDAS 8 on one day that had other matched commits (no figure changed).
- **R3** The made date comes from a column-name list, not the registry.
- **R4** Scheduled routines (BRENT) count as "lit", although no session reads.
- **R5** Liveness is the caller's: a script cannot call ListAgents, so `--live` is passed in.
- **R6** No alert level. **N is Will's**, as a WQ row, and the check flags nothing until it is set.

## 6. L487 half (b) disposition
**A registered check exists:** `AGENTS/DAEDALUS/scripts/dark_window_check.py` (agent-local, my directory). Not wired anywhere: wiring it to PROME's boot report, and the value of N, are PROME's and Will's.
