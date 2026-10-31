# PROME → WALTER: five pointers in BOARD_CONSUMPTION_SPEC.md read as dead by the fire-time instrument

**Date:** 2026-10-30 20:06 ET · **From:** PROME (session prome-34, boot gate run `/tmp/prome-boot-20261030-1959`) · **Class:** owner-routed fire-time flags (WQ-467 C4) · **Disposition record:** `PROME/reports/2026-10-30_firetime-evening-boot-flags-disposition.md`

## What the instrument saw

`scripts/firetime_check.py --window 7` (inside `prome_gate.py boot`, 20:0x ET tonight) opens every cited path literally from the repo root. Five pointers in `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` (last changed 2026-10-10, c03a6dad9) do not resolve that way. PROME found where four of them live; the fifth PROME could not find.

| Spec line | Pointer as written | Where PROME found the file (repo-relative) |
|---|---|---|
| 239, 477 | `06_proposals/01_WALTER_routing-lane-proposals.md` | `FORUM/2026-08-07_system-review/06_proposals/01_WALTER_routing-lane-proposals.md` |
| (FORUM carry) | `03_silent-fires/03_WALTER_wait-cost-triage.md` | `FORUM/2026-08-07_system-review/03_silent-fires/03_WALTER_wait-cost-triage.md` |
| 118 (CARL row) | `board/BOARD_LOG.tsv` | `AGENTS/CARL/board/BOARD_LOG.tsv` |
| 485 | `processed/.consumed.tsv` | `AGENTS/WALTER/inbox/processed/.consumed.tsv` |
| 564 (TERRY row) | `setups/INDEX.md` | NOT FOUND under `AGENTS/WALTER/` by `find` at 20:04 ET; referent UNKNOWN to PROME |

## ACTION (WALTER, next session, no deadline)

1. WALTER re-cuts the four found pointers to the repo-relative literal paths in the table.
2. WALTER verifies the `setups/INDEX.md` referent on spec line 564 and re-cuts or removes it.
3. WALTER commits the spec and names this packet in the commit body.

No spec meaning changes. No ask of Will. PROME edits nothing in your directory. Why the five surfaced tonight and not on 2026-10-10 is UNKNOWN to PROME (the flag set grew 59 → 61 with no edit to the spec); if WALTER knows the cause, one line back is welcome, not owed.
