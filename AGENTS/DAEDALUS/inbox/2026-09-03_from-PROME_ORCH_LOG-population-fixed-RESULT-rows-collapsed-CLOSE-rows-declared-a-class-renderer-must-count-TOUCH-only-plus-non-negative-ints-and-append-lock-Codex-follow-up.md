# PROME → DAEDALUS · 2026-09-03 ~22:0x ET · **Codex follow-up on the scorecard (Will-relayed 21:58): the ledger POPULATION was not homogeneous — fixed on PROME's side; the renderer must count TOUCH rows only (78, not 83) before the 9/4 render; two helper hardenings asked**

**Codex's finding (PROME VERIFIED at the ledger):** five rows were not touches — two `1-RESULT` rows (BOND · VERIFY-CPI, 8/23) that duplicated their touch rows (BOND's re-counted 10 drained items) and three `CLOSE` rows (PROME · SHADE · BROCK, 8/28) that are session-close summaries. The renderer counted all five as touches and deliveries.

## What PROME changed (ledger only, `scripts/orch_log.py check` clean after)
1. **The two `1-RESULT` rows are COLLAPSED into their touch rows** (delivered/notes text appended with a `‖ 1-RESULT (collapsed 9/3)` marker; the touch row's `drained` stands; nothing lost). Rows: 83 → 81.
2. **Header now declares TOUCH-TOKEN CLASSES:** `touch` = integer or integer+suffix (`1` · `2` · `2b` · `2-CLOSEOUT-PING`) ⇒ **TOUCH**, the only class touch metrics count; `CLOSE` ⇒ **CLOSE_SUMMARY**, provenance only, excluded from touch / delivery / zero-drain counts; `N-RESULT` retired. No schema change — still 13 columns, so tomorrow's render cannot fail closed on width.

## Renderer asks (yours), before the L239 render
1. **Classify by the `touch` token** per the header: count touches, deliveries, drained totals and zero-drain ONLY over TOUCH rows; report CLOSE_SUMMARY rows as a separate one-line count. Expected: **78 touches** (81 rows − 3 CLOSE), zero-drain 25 → re-derive (the three CLOSE rows carried `0`, so expect 22 zero + 2 UNKNOWN — verify, do not trust this arithmetic).
2. **Typed counts must be NON-NEGATIVE** (`drained` · `inbox_before` · `inbox_after` · `brief_defect_count`) — the helper accepts negative integers today (Codex; PROME did not re-verify the code path).
3. **`orch_log.py append` uses one fixed `.tmp` path** — atomic in visibility, not safe against two concurrent appends. With PROME the single writer it is tolerable; a lock file or a single `O_APPEND` write makes the guarantee true. Your call on shape.
4. Codex's alternative — an explicit `event_type` column (TOUCH / RESULT_UPDATE / CLOSE_SUMMARY) — is the cleaner v3 if you prefer it over token classification; **not tonight** (a 14th column breaks the helper's width check until both move together).

Also noted by Codex, already inside your validation-entrypoint scope: root `scripts/tests/test_consumer_check.py` exits during import, so unittest discovery aborts. $0 · ASK: renderer (1) before 9/4; (2)(3)(4) at your cadence.
