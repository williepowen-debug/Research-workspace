# ACCEPTANCE CONDITIONS — `spawn_list.py --open` structured export (JSON v1 / TSV)
**Written 2026-10-29 11:5x ET BEFORE the edit** (WQ-229 repair-completion discipline). Requested by CATO for the Agent Launcher's due-work badge (packet `PROME/inbox/2026-10-29_from-CATO_launcher-approved-export-and-review.md`, commit 143e84d72; Will's approval in the CATO window, verbatim *"Okay I approve and you can go ahead and implement now if your ready"*). Owner PROME; one bounded process change (WQ-299 ceiling, 1 of 5 this session).

## The defect, in its own terms
`--open` prints a human table and ignores `--tsv`; it folds "due today" and "overdue" into one flag, drops the owner cell to 26 characters and the catalyst to 64, omits the state cell, the coverage annotation and the notes, and distinguishes nothing between "the docket could not be read" and "no open rows". A consumer that wants the owed-work question answered has to parse prose. The property wanted: **one machine-readable export of the shared "still open" reading, with every field the reader needs and an unmistakable UNKNOWN.**

## Acceptance conditions — the repair must hold ALL of these
1. **One interpretation.** The export is a projection of the SAME `state_kind`/date reading `list_open()` uses today; `list_open()`'s tuple shape and results are unchanged (its existing tests stay green).
2. **Full text, never truncated:** `date_cell`, `owner_cell`, `state_cell`, `catalyst`, `notes` are the raw cells.
3. **Operative date** = the LAST `YYYY-MM-DD` in the date cell (a range's END; `~` approximate flagged `approx: true`); an undated row has `due: ""` and `status: "undated"` and is still listed.
4. **Status partition** vs `--as-of`: `overdue` (due < as_of) · `today` (due == as_of) · `future` · `undated` — four cells, no overlap.
5. **Coverage visible, not applied:** `covered` (raw `COVERED` present in state or notes), `coverage` (the annotation text), and `spawn_suppressed` (the driver's own `covered()` reading) are fields; no row is filtered by them. Will-owned and PROME-owned rows are included and flagged.
6. **UNKNOWN is loud:** an unreadable docket ⇒ rc 2 and (JSON) an object with `error` and `rows` absent — never rc 0 with an empty list. A genuine empty result ⇒ rc 0, `rows: []`, `count: 0`.
7. **Versioned, self-describing:** JSON carries `schema`, `version`, `as_of`, `source`, `source_sha256`, `scope` ("DOCKET only — GATES rows are not in this export"), `count`. TSV carries a header row with the same column names, booleans as `true`/`false`.
8. **The human table still prints** when neither flag is given.

## Neighbours CONSIDERED (five categories)
- **ordinary** — a plain dated PENDING row exports with every field. Tested.
- **overlap** — a row that is PENDING *and* carries a COVERED promise (the L368 class) is listed with `covered: true`; a range date is due on its END; a `~` date is both dated and approximate. Tested.
- **wrong owner** — Will-owned and PROME-owned rows are present and flagged, never dropped; an owner cell with a slash inside a parenthetical keeps one owner name set via the canonical `owner_names`. Tested.
- **missing information** — undated row listed as `undated`; unreadable docket ⇒ rc 2 + error object, never a quiet empty success. Tested.
- **concurrent activity** — N/A: read-only, one file read per call, no state written; the consumer passes `--as-of` so two callers on different clocks disagree only on `status`, by design.

## Completion states (WQ-229 — distinct, never merged)
IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED — filled in below after the edit.

## Completion note — 2026-10-29 12:0x ET (PROME prome-5c)
- **IMPLEMENTED:** `open_records()` (the full-record reading), `list_open()` re-expressed as its projection, `export_open()` with `json` / `tsv` / `human`, `--json` flag; `owner_names` imported from `scripts/docket_view.py` (canonical, never copied).
- **TESTED:** `PROME/tools/tests/test_spawn_list_open_export.py` — `grep -c 'def test_'` = 14, all pass; existing `test_docket_open_query_L368.py` (9) pass unchanged; `test_spawn_list_fail_closed.py` 15/15; `--selftest` 11/11; `--cadence-selftest` PASS. Live docket at as-of 2026-10-29: 204 open = 126 future + 46 undated + 26 overdue + 6 today; the human header's "32 due or overdue" = 26 + 6, unchanged.
- **INDEPENDENTLY VERIFIED:** not yet — a small self-contained tool change (no gate, no shared contract on PROME's side until CATO integrates); CATO's approved Opus review of the launcher is the natural reader of the consumer side. The contract is frozen at v1; a field change is v2.
- **STILL UNRESOLVED:** none known. Residue: `--open` ignores `--horizon`, `--gates`, `--roster` by design (scope line says DOCKET only).
