# falsification_scan.py — read kill rails embedded in STATUS.md (acceptance conditions first, WQ-229)

**Written:** 2026-10-30 (DAEDALUS, Will "yes" 12:49 ET to the scanner fix). **Defect:** found by the WAL profile refresh (reader R2 O2, `runs/2026-10-30_WAL_REFRESH_READERS/R2_LEDGERS_GUARDS.md`): a desk whose kill rail lives inside `STATUS.md` carries the blueprint §4 labelled stamp `Kill rail re-derived: YYYY-MM-DD`, but STATUS.md is the scan's reference clock, never a surface, so the rail has no mechanical reader. WAL reads CURRENT off its CHANGELOG whatever its STATUS rail stamp does; REGINALD (thesis file dead-bannered, live rail in STATUS) is graded only on CHANGELOG + a FROZEN validation file. **Base rate (grep of every `AGENTS/*/STATUS.md` and `PROME/STATUS.md`, 10/30):** 3 desks carry the labelled form in STATUS: WAL :90 (10/22), REGINALD :87 (10/22), FERT :86 (8/17, a pointer to `workbook/EXIT_PROTOCOL.md`, which is already scanned).

**Fix:** recognise the labelled stamp ANYWHERE in STATUS.md (rails sit far below the 18-line header) — the labelled form only, never prose — and emit one row per occurrence, `STATUS.md:<line>`, class `kill rail (in-STATUS)`, graded against the STATUS clock with the existing threshold.

## Acceptance conditions

- **AC1 (capable, live):** WAL gets a row `STATUS.md:90`, stamp 2026-10-22, verdict CURRENT; REGINALD gets `STATUS.md:87`, stamp 2026-10-22, CURRENT.
- **AC2 (alert watched):** a fixture STATUS whose rail stamp is >21 days older than its own Last Updated prints STALE-FLAGGED.
- **AC3 (no prose recognition):** a fixture STATUS that only mentions "kill rail" in prose yields no in-STATUS row.
- **AC4 (deep line):** a rail stamp below line 18 is found (WAL's is at :90).
- **AC5 (no collateral):** fleet `--tsv` before/after diff = only the added in-STATUS rows (expected 3: WAL, REGINALD, FERT); no existing row changes.
- **AC6 (dormant):** a DORMANT desk's in-STATUS rail reads DORMANT-SKIP, like any other surface.

**Not proven by a PASS:** that the rail's content is right, or that a desk without the labelled form has no rail in STATUS (prose rails stay invisible by design — the NO-RAIL bucket still names them).
