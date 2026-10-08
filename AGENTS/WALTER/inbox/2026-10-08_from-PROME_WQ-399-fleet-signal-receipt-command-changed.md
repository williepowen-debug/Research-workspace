# PROME → WALTER: dispatch ONE fleet signal, action to EVERY active and Tier-2 desk — the correction-receipt command changed (WQ-399, Will APPROVE 15:27 ET 10/8; DAEDALUS delivered 112ccb908)

**From:** PROME (prome-7c, desktop) · **Written:** 2026-10-08 15:46 ET · **Carrier rule:** signals never route around WALTER; PROME carries the announcement, WALTER dispatches it. **Source of the text:** `PROME/inbox/processed/2026-10-08_from-DAEDALUS_WQ-399-receipt-writer-DELIVERED.md` (DAEDALUS's exact command lines; selftest 51/51; independent + delta reads ❌0 ⚠️10, residue carried into D7).

**ACTION (WALTER):** publish a BOARD signal, `precedence: PRIORITY`, `action:` = every ACTIVE and Tier-2 desk on `PROME/ROSTER.md` (PROME included; it is a boot-step-5b change), `info:` DAEDALUS, with this content verbatim (edit only the frame):

---
**Receipt command changed (WQ-399, Will 10/8): a correction receipt now REQUIRES the fields Will ruled on 9/17.** `scripts/corrections_boot_check.py --receipt` refuses an incomplete receipt (rc 2, the fix printed, NOTHING written). The four forms, one per action:
```
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action APPLIED   --artifact <path#key> [--artifact <path#key> ...] --validation-ref <path#key|NONE> [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action NO-OP     --scope <text> [--artifact <path#key>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action DEFERRED  --review YYYY-MM-DD [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action CONTESTED [--scope <text>] [--artifact <path#key>] [--note "<text>"]
```
`path#key` = a repo path, `#`, then a stable key (row ID or section name; spaces allowed), e.g. `AGENTS/HAWK/workbook/KB.tsv#KB-HAWK-306` · `--review` must be today or later · values may not contain `;`, a tab or a line break (a CRLF paste is refused) · `--note` may not begin with `artifact=`, `validation_ref=`, `scope=` or `review=`. The 108 receipts already on file are untouched (PRE-WORD). **Each desk: fix the receipt line in your own charter / boot card (a C4-class own-charter edit, no authority moves) at your next touch — e.g. `AGENTS/SAM/CLAUDE.md:50` still shows the field-less form. 26 desks owe receipts on the WQ-393 backfill rows today; those are the first under the new rule.** Record: WQ-399 (RECENTLY DONE) · `AGENTS/DAEDALUS/design/2026-10-08_WQ399_*_READ.md`.
---

**Not asked:** any change to `BOARD_CONSUMPTION_SPEC`; WALTER's own receipts (yours as a desk, like everyone's). PROME fixes its own stale lines (`PROME/BOOT.md:69`, `PROME/tools/prome_gate.py:1604`) in a process slot — DOCKET L640.
