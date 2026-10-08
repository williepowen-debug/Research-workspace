# DAEDALUS → PROME — WQ-399 DELIVERED: receipt writer requires the 9/17 fields (command lines for your fleet packet)

**From:** DAEDALUS · **Written:** 2026-10-08 15:45 EDT (from `date`) · **Ruling:** WQ-399, Will 2026-10-08 15:27 ET, *"399 approve"* · **Code:** `scripts/corrections_boot_check.py` at `112ccb908` (on origin). You carry the fleet announcement; I have announced nothing.

## Exact command lines (one per action) — paste these into the fleet packet
```
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action APPLIED   --artifact <path#key> [--artifact <path#key> ...] --validation-ref <path#key|NONE> [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action NO-OP     --scope <text> [--artifact <path#key>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action DEFERRED  --review YYYY-MM-DD [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action CONTESTED [--scope <text>] [--artifact <path#key>] [--note "<text>"]
```
- `path#key` = repo path, `#`, then a stable key (row ID, section name; spaces allowed), e.g. `AGENTS/HAWK/workbook/KB.tsv#KB-HAWK-306`, `AGENTS/SAM/STATUS.md#BOTTOM LINE`.
- `--review` must be today or later. A missing, malformed or misplaced field is rc 2 with the fix printed, and **nothing is written**.
- Values may not contain `;`, a tab or any line break (a CRLF paste is refused). `--note` may not begin with `artifact=`, `validation_ref=`, `scope=` or `review=`.

## Evidence
- Selftest: `SELFTEST 0 PASS: 51/51 cases` (21 prior + 30 WQ-399 legs).
- Capable cases watched: the pre-change writer accepts APPLIED with no fields (rc 0, row written); the new writer refuses (rc 2, no file). The reviewer's CR defect was reproduced on `8bf9a3625` (write rc 0, then that desk's boot check rc 2) and is refused on `112ccb908`.
- Independent read ACCEPT-WITH-RESIDUE ❌1 ⚠️12 → fixed → delta read **ACCEPT-WITH-RESIDUE ❌0 ⚠️10 ✅27**: `AGENTS/DAEDALUS/design/2026-10-08_WQ399_{INDEPENDENT,DELTA}_READ.md`. Residue is declared in the acceptance doc, Amendment 3, and carried into the D7 build (no third pass on this file today).
- Regression: the boot check rc is identical on 45 names. The only output change is the BLOCK remedy line, which now names the fields.

## For your packet, beyond the commands
- **`PROME/tools/prome_gate.py:1604`** (yours) and `PROME/BOOT.md:69` / desk charters such as `AGENTS/SAM/CLAUDE.md:50` still show the field-less command. The writer refuses that form for 3 of 4 actions and prints the fix, so nothing breaks silently, but the docs are stale.
- Today SAM, HAWK, PROME and BRENT (and more: 26 desks at rc 1 fleet-wide) owe receipts on the WQ-393 backfill rows. Their next receipts will be the first under the new rule.
- The 108 existing receipts are untouched (ruling ③).
