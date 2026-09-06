# VIOLET — WQ-188 2nd pass: acceptance receipt

**Date:** 2026-09-06 PM2 · **Trigger:** Codex 2nd pass on `backfill.py`, routed by PROME (`AGENTS/VIOLET/inbox/2026-09-06_from-PROME_Codex-backfill-closure-still-too-broad-...md`), under Will's WQ-188 ruling (10:58 ET).
**Fixture:** `scripts/test_backfill_endtoend.py` · **Findings:** KB-VIO-264 / 265 / 266 · **Ledger:** `workbook/VX_DAILY.tsv` unchanged (md5 `8b8b779820bd58d584d3d35948c66c32` before and after the live control run).

## What was wrong (both verified by reproduction, not accepted on report)

| # | CBOE response for SKEW | Pre-fix result | Branch |
|---|---|---|---|
| 1 | HTTP 503 | 151.58 preserved, rc=2 | already closed by WQ-188 ① |
| 2 | HTTP 200 carrying **HTML** | **149.00 written, `SETTLE` retained, rc=0** | **parser** (`fetch_cboe_history`) |
| 3 | Valid CSV **missing the target date** | **149.00 written, `SETTLE` retained, rc=0** | **write gate** (destination) |
| 4 | Valid CSV with the date | inert | control |
| 5 | Valid CSV missing date, **blank cell on a non-SETTLE row** | **149.00 filled, row then NEWLY STAMPED `SETTLE`** | **basis stamp** — *not in Codex's table; found here* |

## The three fixes, by branch

- **Parser (case 2)** — after HTTP 200, validate CSV **structure**: a DATE column plus `CLOSE` (OHLC indices) or a column named for the index (VVIX/SKEW), verified live against all six endpoints. Anything else is a parse failure and fails **closed** (`ok=False` → column enters `failed` → `main()` exits 2). A valid header with zero data rows remains a legitimate empty answer `({}, True)`.
- **Write gate (case 3)** — a **destination** gate: yfinance may fill a blank, may **never overwrite**, and may **never touch a row stamped `SETTLE`**. Nothing the provisional pass writes can sit under an authoritative label by construction — no demotion, no new token.
- **Basis stamp (case 5)** — a row that took a provisional cell **this run** cannot be stamped `SETTLE`. The pre-existing whole-run `not failed` guard cannot see this case because *nothing failed*. **Ablation-proven load-bearing:** disabling this one clause reproduces `skew=149.00` under `basis=SETTLE`.

## Acceptance criteria (Codex's, verbatim) — met

1. **No Yahoo overwrite carrying `SETTLE`** — asserted on the file after every case, all five.
2. **No false-success exit** — cases 2 and 3 now exit **2**; case 5 exits 0 having written nothing under an authoritative label.
3. **Actual program path, not source-string assertions** — `backfill.main(["--spot-only"])` is executed; only `requests.get` and the `yfinance` module are stubbed and `DAILY_LOG` is redirected to a temp file.

## Run output

### `test_backfill_endtoend.py` (fixed code)
```
======================================================================
  END-TO-END — the ACTUAL program path, only the network stubbed
======================================================================

[1] CBOE returns HTTP 503 for SKEW — transport failure
  ✅ FIXED: verified 151.58 preserved, run exits 2
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=2 (want 2) · no-Yahoo-under-SETTLE=True

[2] CBOE returns HTTP 200 whose body is HTML — parse failure
  ✅ FIXED: verified 151.58 preserved, run exits 2
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=2 (want 2) · no-Yahoo-under-SETTLE=True

[3] CBOE returns a VALID CSV that lacks 2026-09-04 — destination gate
  ✅ FIXED: verified 151.58 preserved (no fallback overwrite)
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=True

[4] CONTROL — CBOE valid and complete; the pass must be inert
  ✅ FIXED: 151.58 unchanged, run exits 0
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=True

[5] Provisional FILL into a blank cell must BLOCK the SETTLE stamp
  ✅ FIXED: blank filled provisionally, row NOT stamped SETTLE
       skew='149.0' basis='' rc=0 (filled=True not_settle=True)

======================================================================
  5 passed · 0 FAILED
======================================================================
```

### `test_backfill_endtoend.py --falsify` (same cases against pre-fix `backfill.py` from git HEAD)

A regression test that has never been observed to FAIL is an assumption. Cases 2/3/5 MUST fail pre-fix; 1/4 must still pass, so the suite cannot "succeed" by failing everything.

```
  FALSIFICATION — the same cases against PRE-FIX backfill.py (git HEAD)
  A guard whose failure path has never been RUN is an assumption.
======================================================================

[1] CBOE returns HTTP 503 for SKEW — transport failure
  ✅ HEAD: verified 151.58 preserved, run exits 2
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=2 (want 2) · no-Yahoo-under-SETTLE=True

[2] CBOE returns HTTP 200 whose body is HTML — parse failure
  ❌ HEAD: verified 151.58 preserved, run exits 2
       skew='149.0' (want 151.58*) · basis='SETTLE' · rc=0 (want 2) · no-Yahoo-under-SETTLE=False

[3] CBOE returns a VALID CSV that lacks 2026-09-04 — destination gate
  ❌ HEAD: verified 151.58 preserved (no fallback overwrite)
       skew='149.0' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=False

[4] CONTROL — CBOE valid and complete; the pass must be inert
  ✅ HEAD: 151.58 unchanged, run exits 0
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=True

[5] Provisional FILL into a blank cell must BLOCK the SETTLE stamp
  ❌ HEAD: blank filled provisionally, row NOT stamped SETTLE
       skew='149.0' basis='SETTLE' rc=0 (filled=True not_settle=False)
  ✅ FALSIFIED: case [2] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: case [3] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: case [5] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: cases [1] and [4] still pass at HEAD (WQ-188 ① held)
       the new suite does not simply fail everything

======================================================================
  9 passed · 0 FAILED
======================================================================
```

### Live control run against the real 416-row ledger
```
[1b] yfinance provisional: 0 cell(s) written, 492 deferred to CBOE, 0 WITHHELD (failed),
     0 WITHHELD (row already basis=SETTLE), 0 WITHHELD (cell already holds a value)
[1c] CBOE: 2496 cell(s) agreed, 0 blank(s) filled, 0 CORRECTED, 0 row(s) stamped SETTLE,
     0 row(s) NOT stamped (hold a provisional yfinance cell from this run)
rc=0 · md5 before == md5 after == 8b8b779820bd58d584d3d35948c66c32 · diff: IDENTICAL
```
⚠️ **Note the 0s in the withhold counters: the healthy path never exercises the new gates**, because CBOE served every cell. That is exactly why the stubbed cases above — not the control run — are the acceptance evidence.

## The finding against my own instrument (KB-VIO-266)

The AM suite's **12 green contracts, cited to PROME and on STATUS as assurance the fix held, could not have caught either hole.** `run_yf_pass()` is a hand transcription of the write gate, so the shipped code is never executed; a transcription agrees with its original by construction. One assertion — `"settle_stamped" not in str(rows)` — compares a counter's *name* against the repr of ledger row dicts, where it can never appear: **a check that cannot fail.** And its stated rationale, *"pre-existing SETTLE is left alone,"* described as safe the precise end state Codex flagged as dangerous.

**Root cause: I wrote the contracts from the fix I had just made instead of from the failure mode.** Both self-defects are repaired in place and the file keeps an explicit scope banner; it is retained for its AST/print-literal and structural checks, which remain useful.

## Scope limit, stated

This covers `backfill.py` only. **`thresholds.py` still writes the leading-edge `VX_DAILY` row from yfinance at every boot** — the six columns are authoritative in *history* and provisional at the *leading edge* (KB-VIO-255/257), which is precisely the window an FT-10 bar is graded in. Deliberately **not** bundled here: re-pointing it is a design question about what a pre-settle row means, not a bug fix.
