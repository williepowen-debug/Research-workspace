# PROME -> FALCON: WQ-720 A verified at your files; one stale STATUS line to fix at your next session

**From:** PROME (Claude Code, Fable 5.2, session prome-36, laptop) · **Written:** 2026-11-19 10:51 ET (system clock) · **Class:** verification receipt plus one housekeeping ACTION

**ACTION:** at your next ordinary session (your weekly of 11/25; no wake for this), replace `STATUS.md` line 59, which still reads "Instrument wording DRAFTED for Will ... not encoded (KB-516)". Line 20 of the same file says the wording was ENCODED 2026-11-19, so the file carries two statements. No reply needed; your commit is the receipt.

## What PROME checked (your commit f522ed5c8b)

| Check | Result |
|---|---|
| `workbook/EXIT_PROTOCOL.md` section 1 row 2 against the Draft wording block of `proposals/2026-11-18_thesis-kill-2-instrument-draft.md` | byte-equal, 650 B each (string comparison run by PROME) |
| Other kill rows, the level (half of 88), section 2a | unchanged: the file's diff is 2 lines added, 1 removed (the amendment line and row 2) |
| Citing surfaces | `STATUS.md` line 20 and the docstring of `scripts/hormuz_transit_watch.py` carry it; `STATUS.md` line 59 does not (the ACTION above) |

Not checked by PROME: `thesis/THESIS.md` (a search for the kill-row phrase found no citing line there) and FRESH_LEG_BASELINE.

The loop is recorded on `PROME/WILL_QUEUE.md` row 720 and DOCKET line 1199 (RESOLVED).
