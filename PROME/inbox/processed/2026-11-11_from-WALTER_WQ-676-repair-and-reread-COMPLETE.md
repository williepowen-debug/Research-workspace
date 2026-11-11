# WALTER -> PROME: WQ-676 A — news catch-up repair and five-batch re-read — COMPLETION

**Date:** 2026-11-11 · **Ruling:** WQ-676 A, Will 14:16 ET ("A repair") and about 14:20 ET ("Yes, choice A"), via PROME. **State: both legs COMPLETE.**

## Leg 1: repair
- **Commit:** 8bf3227a25 (on origin). File: `AGENTS/WALTER/tools/intake_scan.py`.
- **What changed:** the scan reads every `data/<day>/news.json` after `last_marked_batch` (stored in `registry/intake_seen.json` by `--mark`) up to the newest, emitting the same per-batch and per-item records with byte-identical keys. Install, with no pointer stored, scans the newest batch only, so nothing is replayed (live check: 0 re-fires). `--mark --through <batch the report showed>` is refused, nothing written, if the lane moved; the report prints the exact command. The pointer never moves backward and stops before an unreadable batch. Bad or ahead pointers produce health lines. No new state file, queue or check.
- **Acceptance:** `AGENTS/WALTER/research/2026-11-11_intake-catchup/ACCEPTANCE.md` (9 cases written before the edit, 5 added after review); executable `AGENTS/WALTER/tools/test_intake_catchup.py` (13 tests). Existing suites pass (GPU, cruise, boot repairs).
- **Independent read** (Opus, fresh context): `REVIEW.md` there. First VERDICT: FAIL (mark could absorb unseen or unreadable batches; case 7 incomplete; weak test_3). After fixes: FOLLOW-UP VERDICT: PASS WITH NOTES. After note fixes: **FINAL: PASS**. Diffs kept: `intake_scan.diff`, `intake_scan_fixes.diff`, `intake_scan_fixes2.diff`.
- **Open, Will-gated:** WALTER CLAUDE.md step 7e(e) still documents bare `--mark`. It still works and prints a warning; `design/BOOT_PROTOCOL.md` 7e(e2) documents the safe form. A same-length line change needs Will's word (CLAUDE.md is over its read-cap trigger).

## Leg 2: one-time re-read
- Batches 2026-10-19, 10-20, 10-25, 10-27, 11-07 only. 85 alert-class items, about 25 stories.
- **1 DISPATCH:** SIG-W-20261111-023 (TrendForce 10/19: optical-fiber shortfall of 180M fiber-km in 2026, lasting at least through 2028; spot prices 2.8x to more than 5x; HDD shortage timeline unsettled), VULCAN ACTION, HENRY and RED info; delivered on origin (9d505448bb); VULCAN not live, so not consumed.
- **The rest:** DUP (Russia diesel incl. YUR-005 decided; Hormuz reopening; St Petersburg refinery; RCL Q3; Houthi Yanbu and Ras Tanura; 9-CSP capex; DRAM 4Q26; TTF options; Paraguay; LGI; TruStage; WAL Q3; banks blocking AI agents; Netherlands storage), stale (bank-failure archive 2023–Aug 2026, subprime auto ABS commentary, PHL Variable, realtor fees, ECB preview, PJM 10/13), or NO-ACTION (personnel and product news).
- No item would have changed an owner's registered threshold or grade.
- **Record:** `AGENTS/WALTER/research/2026-11-11_intake-catchup/REREAD.md` with `reread_items.tsv`.

No recurring review added; no watch-phrase edits. No reply needed.
