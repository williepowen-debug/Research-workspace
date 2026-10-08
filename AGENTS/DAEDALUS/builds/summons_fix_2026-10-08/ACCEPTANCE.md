# ACCEPTANCE — L548: `prome_gate.check_desk_catalyst_summons` hides the rows it exists to show

**Written BEFORE any code (WQ-229), 2026-10-08 ~08:2x ET, DAEDALUS (fork of the 10/08 WQ-389 wake).** DOCKET row: `PROME/DOCKET.tsv` L548. Owner of the live tool: PROME (`PROME/tools/prome_gate.py`); this bundle is a PROPOSAL + isolated patch, never applied by DAEDALUS.

⛔ Not built by PROME 9/29 — the session's one process change was the registry line (R1).

## The defect, in its own terms
The check exists to SUMMON a desk session when a registered desk-catalyst row is due. It sorts every flag by date ASCENDING and prints `detail_bits[:4]` with no full-output log, so any ledger carrying more past-due rows than the slice pushes every in-window row (the rows it exists to surface) into `(+N more)`, invisible at boot and closeout. Reproduced 2026-09-29 (25 VULCAN rows; VULCAN 9/30 ×4 and LABOR 10/01 hidden). **Reproduces live again today 2026-10-08:** one VULCAN 10/05 past-due row + LABOR 10/08 ×2 + VULCAN 10/09 ×4 ⇒ three of the four VULCAN 10/09 rows sit inside `(+3 more)`.

## Acceptance conditions (properties, not the symptom)
- **AC-a — forward window first and in full.** Every row dated TODAY or within `SUMMONS_WINDOW_DAYS` appears in the recorded detail, ahead of every past-due item, with desk · date · [priority] · event · (TODAY | in Nd). No slice, count or past-due volume can remove a forward-window row from the detail.
- **AC-b — past-due summarized per desk.** Past-due rows are not listed one-by-one in the detail; each desk with any contributes exactly one bit `<DESK> N past-due (oldest <YYYY-MM-DD>) — owner prunes`.
- **AC-c — full list on disk, by the existing mechanism.** When anything flags, the complete untruncated list (every forward row, every past-due row in its old per-row form, every dead ledger) is written to a file in the run's `LOG_DIR` named the way `run_script` names its logs, and the detail ends with the same `\n       full output: <path>` suffix. One naming/LOG_DIR routine shared with `run_script` — not a second one. A log-write failure never loses the check: the detail says the log is UNAVAILABLE and why.
- **AC-d — dead ledgers still surface.** `MISSING` and `unreadable` ledgers appear in the detail (unchanged text) and make the check flag.
- **AC-e — consumer contract unchanged.** Severity `ADVISE`, check name `desk catalyst summons (BD-02)`, the WQ-184 owner/hint text, the `ok` rule (ok ⇔ nothing flagged) and gate rc are unchanged.
- **AC-f — quiet case unchanged.** No flags ⇒ detail is exactly `<n> desk ledger(s) quiet inside <N>d`, ok=True, no log suffix.
- **AC-g — testable clock.** `today` injectable (keyword, default `dt.date.today()`), so the tests never depend on the wall clock; both live call sites keep calling it with no arguments.

## Neighbours (WQ-229 five categories, considered)
| Category | Case | Test / N/A |
|---|---|---|
| Ordinary | 25 past-due + 4 in-window on one desk (the 9/29 VULCAN reproduction) | test: all 4 in-window rows in detail, before the single past-due summary |
| Ordinary | only in-window rows; only past-due rows; a TODAY row; a row exactly at the horizon (today+N) | tests: horizon row IS in window (unchanged `d > horizon` skip); today+N+1 is not |
| Overlap | a desk with BOTH in-window and past-due rows, and two desks interleaved by date | test: both desks' window rows in date order; one past-due bit per desk |
| Wrong owner | a row in desk X's ledger naming another desk | N/A by construction — the ledger is the desk's (unchanged from the 9/29 acceptance) |
| Missing information | missing ledger · unreadable ledger · a row with no parseable date | tests: MISSING/unreadable surface in detail; undated rows stay SKIPPED in the detail (unchanged behaviour) but are COUNTED in the full log when the check flags — **NOT MET in the quiet case** (no log is written, so an undated-only ledger stays silent; and an ISO-shaped invalid date aborts its ledger's remaining rows): see README § Residue and `INDEPENDENT_READ_2026-10-08.md` R2/R3 *(cell corrected 2026-10-08 after the independent read; pointer fix, no code change)* |
| Concurrent activity | two gate runs, or boot and closeout in one process | log path is index-prefixed by `len(results)` and opened exclusive-create, exactly as `run_script`; N/A beyond that — single-writer per run, and the check is read-only on ledgers |

## What passing establishes
IMPLEMENTED + TESTED against these conditions by the author. NOT INDEPENDENTLY VERIFIED: it changes a gate check's output contract, so it is a CONSEQUENTIAL repair (PROME/CLAUDE.md WQ-229) and owes an independent reader with its own counterexample before it is called fixed.
