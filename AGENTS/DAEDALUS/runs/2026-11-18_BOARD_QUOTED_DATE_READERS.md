# BOARD quoted-date fixture through every desk BOARD reader — 2026-11-18

**Asked by:** PROME packet 2026-11-16 (`inbox/processed/2026-11-16_from-PROME_BOARD-quoted-date-reader-blind-spot-from-TERRY.md`), assigned for today by Will's "go" relayed by PROME 15:30 ET. **Run:** 2026-11-18 ~15:40 ET, `.venv/bin/python3 runs/2026-11-18_BOARD_QUOTED_DATE_FIXTURE.py <scratch> <READER>`.

**Fixture:** a temporary root holding one `SIG-W-20261110-9nn-fixture-<desk>.md` per reader, with front matter in WALTER's live quoted form (`signal_id: "…"`, `date: "2026-11-10"`, `timestamp:`/`dispatched:` quoted, `action: ["<DESK>"]`), and an empty ledger, so a working reader must report it as unlogged. Each reader's own function was run against it with its module paths re-pointed at the fixture root.

**Control (the fixture can catch a blind reader):** TERRY's boot.py as it stood before the fix (`d82da9ba4d^`) returned `([], 0, 0, [])`, so it dropped the fixture silently. TERRY's current boot.py returned the signal unlogged, 8 days old.

| Reader | How it dates or selects a signal | Fixture result | Verdict |
|---|---|---|---|
| TERRY `scripts/boot.py` `board_gap` (pre-fix, control) | front-matter `date:` unquoted only | dropped | blind (fixed 11/16 in d82da9ba4d) |
| TERRY `scripts/boot.py` `board_gap` (current) | front matter, quotes accepted | caught, unlogged 8d | OK |
| RED `scripts/boot.py` `section_board_gap` | date from FILENAME; `action:` quotes stripped | ALERT 1 unlogged, 8d | OK |
| PROME `tools/exempt_gap.py` `scan` (RED, TERRY, CARL) | date from FILENAME; `parse_front` strips quotes in lists | each desk's fixture unlogged; 0 skipped | OK |
| PROME `tools/board_scan.py` `inspect_signal` | routing per line; quoted `dispatched:` accepted | action {PROME}, no problem codes | OK |
| HENRY `scripts/boot.py` `walter_lane_backlog` | filename only (inbox/WALTER lane) | 🟠 1 unlogged, 8d | OK |
| REGINALD `scripts/boot.py` `check_inbox` | id by regex over the file body (a quoted id still matches) | NEW, rc 1 | OK |
| CARL `scripts/board_gap.py` `index_rows` | reads `BOARD/INDEX.md` table, not front matter | all 265 November quoted-date files on the live BOARD appear in the INDEX rows it parses | OK |

**Other scripts that matched `BOARD`/`SIG-W` on the census grep** (CYPHER, FLG, HANS, HAWK, LIQUID boot or tools; FALCON baghdad_watch; WAL maintenance check; VULCAN crwv_library; OTTO backfill; TERRY snapshot; RED board_log_append; PROME decision_deck, inbox_census, reads_check, spawn_list; root consumer_check, corrections_boot_check, read_cap_check) cite a signal id in a comment or string, or read a ledger or filename. None selects BOARD signals by front-matter date, so none can drop a quoted-date file this way. Read at the grep line, not run.

**Disposition:** no other desk reader is blind to quoted dates. Nothing to repair; nothing for WALTER (its quoted form is read correctly by every live reader). Limit: function-level runs on a fixture, not whole boots; a reader added after today is not covered.
