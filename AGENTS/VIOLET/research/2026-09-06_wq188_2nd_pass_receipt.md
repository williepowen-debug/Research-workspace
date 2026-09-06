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
2. **No false-success exit** — **case 2 (HTML) exits 2**, because that IS a failed fetch. ⚠️ **CORRECTED (Codex 3rd pass): an earlier draft of this line said "cases 2 and 3 exit 2" — case 3 exits 0, as this file's own transcript below shows.** That is correct and not a false success: a valid CSV that simply lacks the target date is **not a failed fetch**, so the run legitimately succeeds having *preserved an existing verified value* rather than written a fallback. Cases 3, 5, 6 and 7 exit 0 with nothing unverified written under an authoritative label. ⚠️ **My summary contradicted the transcript printed directly beneath it** — the transcript was right.
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

---

# ADDENDUM — 3rd pass (Codex, same day): the provisional safeguard failed on the SECOND run

**Codex re-ran my own missing-date fixture twice and the guard did not survive it.**

| Run | SKEW | Basis | Exit |
|---|---|---|---|
| 1st: blank filled from Yahoo | 149.00 | *(blank / provisional)* | 0 |
| 2nd: **identical** source responses | 149.00 | **SETTLE** | 0 |

**Reproduced here before changing anything** — `run 1: skew='149.0' basis='' rc=0` → `run 2: skew='149.0' basis='SETTLE' rc=0`.

## Why it failed, and the rule worth keeping

The 2nd-pass safeguard gated on `d_str in provisional_rows` — **a set built during the current run.** On run 2 the provisional value is already on disk, the destination gate correctly **preserves** it, so *no new provisional write is recorded*, the set is empty, and the stamp condition then only asked whether CBOE had `vix`.

🔑 **A GUARD WHOSE MEMORY IS SHORTER THAN THE STATE IT GUARDS FAILS ON THE SECOND RUN.** The state — a provisional cell — is **persistent**; my evidence for it was **per-run**. The fix is not to persist the bookkeeping but to stop needing it: **read the invariant off the row itself**, which is where the state actually lives.

⚠️ **And the comment directly above that code already stated the correct invariant** — *"ONLY when every column in the row was confirmed by CBOE this run"* — **while the code checked only `vix`. That is the second time in one day that a comment in this file certified what the code did not do** (the first was `fetch_cboe_history`'s "parse failure" docstring). A stated invariant is not an implemented one, and writing it down is what stops the next reader checking.

## The fix (Codex's "smallest robust" option, adopted)

Stamp `SETTLE` only when, for **every** one of the six spot columns, either CBOE confirmed the value for that date **or the cell is blank** (a blank is the absence of a claim, not a mirror value). Stateless, no bookkeeping, and **recovery comes free**: once CBOE publishes the missing series its pass overwrites the provisional value, every column becomes confirmed, and the row settles legitimately.

**The now-dead `provisional_rows` plumbing was removed rather than left in place** — a strictly weaker second guard only manufactures the impression of depth, which is the same criticism I levelled at the AM test suite.

## Also fixed this pass

- **`--falsify` was broken by the very commit that shipped it.** The baseline loader read `HEAD:…backfill.py`; HEAD became the *fixed* file the moment I committed, so Codex's run compared fixed code against fixed code (6 passed / 3 failed). **A baseline that moves is not a baseline.** Now pinned to `1e8ae5d00^`. *(Codex independently confirmed that revision reproduces the intended result — 2/3/5 fail, 1/4 pass — so the original experiment stands; only its committed reproduction mechanism was broken.)*
- **Two live summaries reconciled** — the FT-10 row's *"published 9/10"* (a T+1 assumption my own **KB-VIO-137 retracted**; `^SKEW` publishes same-day ~17:00 ET, and no date is asserted now), and this file's own acceptance line, which contradicted the transcript printed beneath it.
- **Wording:** three readers *reduce the risk of* reader error; they do not categorically rule it out.

## 3rd-pass run output

### 7 cases, fixed code
```
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

[6] TWO RUNS, identical responses — the stamp must NOT appear on run 2
  ✅ FIXED: provisional 149.00 never acquires SETTLE across two runs
       run1=('149.0', '', 0) run2=('149.0', '', 0)

[7] RECOVERY CONTROL — when CBOE supplies SKEW, it replaces the provisional value and the row MAY settle
  ✅ FIXED: CBOE's 151.58 replaces the provisional value and the row settles
       skew='151.58' basis='SETTLE' rc=0 (replaced=True settled=True)

======================================================================
  7 passed · 0 FAILED
======================================================================
```

### `--falsify` against the PINNED pre-fix revision `1e8ae5d00^`

```
  FALSIFICATION — the same cases against PRE-FIX backfill.py (1e8ae5d00^)
  A guard whose failure path has never been RUN is an assumption.
======================================================================

[1] CBOE returns HTTP 503 for SKEW — transport failure
  ✅ PRE-FIX: verified 151.58 preserved, run exits 2
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=2 (want 2) · no-Yahoo-under-SETTLE=True

[2] CBOE returns HTTP 200 whose body is HTML — parse failure
  ❌ PRE-FIX: verified 151.58 preserved, run exits 2
       skew='149.0' (want 151.58*) · basis='SETTLE' · rc=0 (want 2) · no-Yahoo-under-SETTLE=False

[3] CBOE returns a VALID CSV that lacks 2026-09-04 — destination gate
  ❌ PRE-FIX: verified 151.58 preserved (no fallback overwrite)
       skew='149.0' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=False

[4] CONTROL — CBOE valid and complete; the pass must be inert
  ✅ PRE-FIX: 151.58 unchanged, run exits 0
       skew='151.58' (want 151.58*) · basis='SETTLE' · rc=0 (want 0) · no-Yahoo-under-SETTLE=True

[5] Provisional FILL into a blank cell must BLOCK the SETTLE stamp
  ❌ PRE-FIX: blank filled provisionally, row NOT stamped SETTLE
       skew='149.0' basis='SETTLE' rc=0 (filled=True not_settle=False)

[6] TWO RUNS, identical responses — the stamp must NOT appear on run 2
  ❌ PRE-FIX: provisional 149.00 never acquires SETTLE across two runs
       run1=('149.0', 'SETTLE', 0) run2=('149.0', 'SETTLE', 0)

[7] RECOVERY CONTROL — when CBOE supplies SKEW, it replaces the provisional value and the row MAY settle
  ✅ PRE-FIX: CBOE's 151.58 replaces the provisional value and the row settles
       skew='151.58' basis='SETTLE' rc=0 (replaced=True settled=True)
  ✅ FALSIFIED: case [2] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: case [3] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: case [5] FAILS against pre-fix code
       the test can distinguish fixed from unfixed
  ✅ FALSIFIED: case [6] (two-run stamp) FAILS against pre-fix code
       the 3rd-pass defect is reproduced by the pinned baseline
  ✅ FALSIFIED: cases [1] and [4] still pass pre-fix (WQ-188 ① held)
       the new suite does not simply fail everything

======================================================================
  12 passed · 0 FAILED
======================================================================
```

### Live control, re-run after the 3rd-pass change
```
yfinance (provisional): 0 written, 492 deferred to CBOE, 0/0/0 withheld
CBOE: 2496 cell(s) agreed, 0 filled, 0 CORRECTED, 0 stamped SETTLE, 0 NOT stamped
rc=0 · md5 before == after == 8b8b779820bd58d584d3d35948c66c32
```

**Case [7] is the negative control that matters:** a guard that never let anything settle would pass case [6] and be useless. Recovery still settles, and it passes pre-fix too — the pre-fix code was over-permissive, not under-permissive.
