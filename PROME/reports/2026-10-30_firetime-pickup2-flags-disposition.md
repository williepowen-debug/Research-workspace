# October30 Friday second pick-up fire-time dispositions

Owner: PROME (session prome-c5, Claude Code, Fable 5.1, desktop; "pick up PROME" refresh of run directory `/tmp/prome-boot-20261030-1024`, refresh `refresh-mjp9czmf`, 16:3x ET Fri 2026-10-30). Gate line: 59 flags, 2 NEW, 57 persisting (earlier receipts named on the gate line), 11 dispositioned flags no longer reported (pruned). Each NEW flag was read at its artifact in full context before disposition (WQ-467 C4). Recorded 2026-10-30 16:4x ET.

**Why two UNREADABLE flags surfaced:** DOCKET rows L885 and L886 (registered 14:2x and 15:2x ET today) cited the WALTER BOARD cards by a shell glob (`BOARD/SIG-W-20261030-002-*.md`, `BOARD/SIG-W-20261030-011-*.md`). `firetime_check.py` opens cited paths literally, so a glob is an unreadable artifact. PROME's own rows; a pointer-form defect, not a changed fact.

| Source and flag | Disposition and evidence |
|---|---|
| DOCKET L885 source cell — NEW UNREADABLE `BOARD/SIG-W-20261030-002-*.md` | DONE: cell re-cut to the literal file `BOARD/SIG-W-20261030-002-tech-selloff-ndx-minus-3-qqq-under-690-gamma-trough-spx-7550-below-7700-put-wall-vix-22-intc-minus-31-HENRY.md` (exists; `ls BOARD/`). Row meaning unchanged. |
| DOCKET L886 source cell — NEW UNREADABLE `BOARD/SIG-W-20261030-011-*.md` | DONE: cell re-cut to the literal file `BOARD/SIG-W-20261030-011-iran-two-hull-attacks-oct29-louise-1-explosive-devices-above-waterline-ukmto-187-26-riti-25-crew-evacuated-musandam-jask-us-strike-unconfirmed-ras-tanura-shut-not-established-FALCON.md` (exists). Row meaning unchanged. |

Lesson (PROME, not yet a memory row): a DOCKET source cell is read by an instrument — write literal paths, never globs; the WALTER lane card under `AGENTS/<DESK>/inbox/WALTER/SIG-W-….md` is the short literal form when the BOARD filename is long.

Accept: `python3 PROME/tools/firetime_delta.py --log /tmp/prome-boot-20261030-1024/refresh-mjp9czmf/checks/04-firetime-owner-routed-flags-persist-.txt --prune` then `--accept --pointer PROME/reports/2026-10-30_firetime-pickup2-flags-disposition.md`; `PROME/state/firetime_dispositioned.tsv` committed with this record.
