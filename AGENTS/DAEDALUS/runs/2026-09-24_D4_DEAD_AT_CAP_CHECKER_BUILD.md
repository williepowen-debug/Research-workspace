# D4(a) checker build — a passed `date_cap` never clears a NAMED target's block

**Date:** 2026-09-24 ~20:52Z · **Author:** DAEDALUS build subagent (spawned by DAEDALUS lead) · **Surface:** `scripts/corrections_boot_check.py` (repo-root, DAEDALUS `scripts/` grant)
**Ruling:** Will 2026-09-24 14:59 ET, WQ-254 D4(a) "A3 semantics". Record: `PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md` row 254. Spec: `runs/2026-09-17_P4_SITTING_RULING_PACKAGE.md` §4 D4.
**State:** ⚠️ **UNCOMMITTED working-tree edit** (the subagent brief forbade mutating git). md5 before `6410121a5c27c5fa7aab33b435346ce0` → after `251141fc2033551a0f4f440bac30a18a`. 135 insertions, 15 deletions.
**Gate:** WQ-229 — **NOT yet "fixed"**. It needs an independent reader with its own counterexample (see Residue).

## 1. Design decisions

| # | Case | Before | After | Why |
|---|---|---|---|---|
| 1 | `RETIRED` row, any target | skip | skip (unchanged) | RETIRED = verified closure on WALTER's ladder. The owner declared it closed. |
| 2 | NAMED row, status `DEAD-AT-CAP`, no receipt from this desk | skipped before anything ran (L139): no INFO line, rc 0 | **BLOCK rc 1**, labelled `DEAD-AT-CAP (row status …; cap … passed/not passed — …WQ-254 D4(a))` | D4(a): a row's status never discharges the target |
| 3 | NAMED row, status `LIVE`/`RECEIPTED`, cap passed, no receipt from this desk | INFO line, then skipped (L149): rc 0 | **BLOCK rc 1**, same label (row status shown as-is) | D4(a): a passed cap never discharges the target |
| 4 | NAMED row, cap passed or `DEAD-AT-CAP`, **receipted by this desk (any action)** | skip | skip | "until a receipt of ANY action exists." CONTESTED and DEFERRED count too. |
| 5 | `ALL`-row, cap passed or `DEAD-AT-CAP`, unreceipted | INFO line (cap-passed only), no warn, no block. A `DEAD-AT-CAP` ALL-row was skipped silently. | INFO line (counted as ALL-row), no warn, no block | Broadcast expiry is unchanged. **Small visible change:** a `DEAD-AT-CAP` ALL-row now appears on the INFO line instead of vanishing. rc is unchanged. |
| 6 | `ALL`-row, cap not passed, unreceipted | WARN, rc 0 | WARN, rc 0 (unchanged) | Warn-never-block |
| 7 | NAMED `LIVE` row, cap in the future, unreceipted | BLOCK | BLOCK (unchanged), labelled `[LIVE]` | — |

- **Receipt-first ordering.** `if cid in receipts: continue` now runs before any cap or status logic. A desk's own receipt is the only thing that clears a NAMED row.
- **INFO line restored and split.** `INFO N dead-at-cap with no receipt from this desk: <ids> — k NAMED (still BLOCKING…) · m ALL-row (broadcast expired…)`. The leading phrase is kept verbatim for anyone who greps it.
- **BLOCK header** now reads `… unreceipted for X (k of them DEAD-AT-CAP):`.
- **PASS line perimeter.** It counts only ALL-rows past their cap as "broadcast expired, not an obligation". It names both inputs (the register and this desk's receipts file). It says what a PASS does not prove: that the receipt's action was correct, or that the correction was applied (CHECK_STANDARD §2).
- **rc contract unchanged**, quoted from the docstring: `0 no unreceipted NAMED rows for this desk` · `1 >=1 unreceipted NAMED row` · `2 CANNOT-EVALUATE — register absent … required header column missing, unparseable date … unparseable receipts file, or an UNKNOWN AGENT NAME`. The rc-1 docstring line was re-worded to state D4(a). It also names the §3(e) production acceptance set (SAM defective / HAWK clean, time-bound).
- **§9 consumer survey (before the edit).** Every rc consumer keys on rc alone: `AGENTS/DAEDALUS/scripts/daedalus_gate.py:148` (`{0: CLEAN, 1: BLOCKING, 2: UNKNOWN}`), `PROME/tools/prome_gate.py:1320` (ADVISE, rc-keyed) and `scripts/validate_all.py` A1 (runs `--selftest`, rc-keyed). No consumer parses `dead-at-cap` or the BLOCK text, so the wording changes break no consumer. `validate_all.py --only A1` after the edit printed `✅ VALIDATE-ALL 0 CLEAN: 1 PASS`, rc 0.

## 2. Live outputs (live register, 26 rows; `--today` default = 2026-09-24)

**SAM BEFORE** (rc 0):
```
CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for SAM (register 26 row(s), 0 ALL-warn, 0 dead-at-cap; receipts on file: 2) — PASS covers the register at /home/willi/Research-workspace/AGENTS/WALTER/registry/CORRECTIONS.tsv, nothing else
```
**SAM AFTER** (rc 1):
```
  INFO 1 dead-at-cap with no receipt from this desk: COR-20260826-02 — 1 NAMED (still BLOCKING until receipted, WQ-254 D4(a)) · 0 ALL-row (broadcast expired: no warn, no block)
CORRECTIONS-CHECK 1 BLOCK: 1 NAMED correction(s) unreceipted for SAM (1 of them DEAD-AT-CAP):
       COR-20260826-02 [DEAD-AT-CAP (row status DEAD-AT-CAP; cap 2026-08-28 passed — a passed cap never discharges a named target, WQ-254 D4(a))] 2026-08-26 -> read BOARD/SIG-W-20260819-024-the-carry-trade-is-said-to-be-rotating-from-yen-to-swiss-franc-the-cftc-primary-says-the-franc-absorbed-3-6-percent-of-it.md, then receipt: corrections_boot_check.py SAM --receipt COR-20260826-02 --action <APPLIED|NO-OP|DEFERRED|CONTESTED>
```
**HAWK BEFORE** (rc 0):
```
CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for HAWK (register 26 row(s), 0 ALL-warn, 0 dead-at-cap; receipts on file: 2) — PASS covers the register at /home/willi/Research-workspace/AGENTS/WALTER/registry/CORRECTIONS.tsv, nothing else
```
**HAWK AFTER** (rc 0; its receipt is `2026-09-08T21:30Z COR-20260828-01 NO-OP`):
```
CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for HAWK (register 26 row(s), 0 ALL-warn, 0 ALL-row(s) past cap unreceipted = broadcast expired, not an obligation; receipts on file: 2) — PASS covers the register at /home/willi/Research-workspace/AGENTS/WALTER/registry/CORRECTIONS.tsv and this desk's receipts file, nothing else (it does not prove a receipt's action was correct or that the correction was applied)
```
Other paths watched after the edit:

| Run | Result |
|---|---|
| `ZZZNOTANAGENT` | rc 2 `unknown agent` |
| `--register /nonexistent.tsv` | rc 2 `register not found` |
| `DAEDALUS` (not a target on any row) | rc 0 |
| `SAM --today 2026-10-02` | rc 1, still only `-0826-02`. SAM receipted `-0924-19` APPLIED at 2026-09-24T20:44Z, so that row's 10/01 cap passing adds nothing. |

## 3. Selftest totals

| Run | Result |
|---|---|
| **BEFORE** | `SELFTEST 0 PASS: 5/5 cases`, rc 0. These are the header-validation cases only. |
| **AFTER** | `SELFTEST 0 PASS: 18/18 cases`, rc 0. That is the 5 existing cases plus 13 D4 cases. Each D4 case asserts the rc **and** required/forbidden output substrings. Text is asserted because the 9/24 regression showed only in text (`INFO 1` became `0 dead-at-cap`) while rc stayed 0. |
| **First AFTER run** | **16/18, rc 1.** Two of my assertions were too loose: forbidding `"BLOCK"` matched the INFO line's word "BLOCKING", and forbidding `"DEAD-AT-CAP"` matched the header's "(0 of them DEAD-AT-CAP)". I tightened them to the exact markers `CORRECTIONS-CHECK 1 BLOCK` and `[DEAD-AT-CAP`. The checker was not at fault, and the FAIL path was watched printing. |
| **Mutation check** | New selftest run against the **old** `cmd_check` (the BEFORE copy was monkeypatched in): **11/18, rc 1.** All 4 D4 capable cases FAIL with rc 0 (DEAD-AT-CAP named · cap-passed LIVE named · DEAD-AT-CAP with no cap · multi-target other-desk unreceipted), plus the mixed case. The 2 wording-only cases fail on text. The new cases therefore separate the old code from the new. |

D4 cases, in order:

1. DEAD-AT-CAP named, unreceipted → 1
2. The same row, receipted NO-OP → 0
3. The same row, receipted CONTESTED → 0
4. Cap-passed LIVE named, unreceipted → 1
5. DEAD-AT-CAP with no cap → 1
6. ALL-row past its cap → 0, no WARN
7. ALL-row with its cap not yet passed → 0 with a WARN
8. HAWK multi-target, receipted → 0
9. The same row for BRENT, unreceipted → 1
10. DEAD-AT-CAP naming another desk → 0
11. RETIRED named → 0
12. LIVE named with a future cap → 1, labelled `[LIVE]`
13. Mixed → 1, counts split

## 4. Desks whose boot verdict changes

All 25 desks named on any register row were run before and after. **The rc changes for exactly one desk: SAM, 0 → 1** (`COR-20260826-02`).

| Group | Desks | What changed |
|---|---|---|
| BLOCK before and after | BRENT · FALCON · HANS · HENRY (7 rows) · LIQUID · RED · REGINALD · WATT | Output is identical except for the new header suffix `(0 of them DEAD-AT-CAP)`. None of their blocking rows is cap-passed. |
| rc 0 before and after | BOND BROCK CARL DEWEY HAWK HOMER LABOR MIDAS NEXUS PROME SHADE TERRY VIOLET VULCAN WAL ZHAO | PASS-line wording only. |

**Why HENRY and ZHAO do not change:**
- HENRY's 7 blocking rows have no cap, so they were already blocking.
- ZHAO is named only on `-0908-01`, which has no cap.
- Neither desk is named on any cap-passed row.

**Cross-check on a different perimeter.** A direct read of all receipts files against every cap-passed or DEAD-AT-CAP row (10 rows) did not use the checker. It found exactly one unreceipted target: SAM on `-0826-02`. That agrees with the checker's delta, and with WALTER's prune (1 DEAD-AT-CAP, the other 9 cap-passed rows all RECEIPTED).

**For PROME's briefs.** Only SAM needs a brief: *"your next boot will BLOCK once on COR-20260826-02 (LIQUID → SAM, the CFTC yen→franc carry correction, cap 8/28). Read the pointer and receipt it with any action."* SAM was live at 20:44Z today (receipt for `-0924-19`).

## 5. Residue — what an independent reader should try to break

**Not tested:**
1. A `targets` cell that mixes `ALL` with names (for example `ALL,SAM`). `is_all` is false, so it is treated as NAMED for SAM and ignored for everyone else. That behaviour is pre-existing and was not re-examined under D4.
2. Case variants of the status token (`dead-at-cap` or padded). They are handled by `.strip().upper()`, but no selftest case covers them.
3. A blank status on a cap-passed named row. By code reading it blocks; this was not run.
4. The `cap == today` boundary. `cap < today` means a cap equal to today has **not** passed. This is unchanged and untested here.
5. A receipt whose `correction_id` has stray whitespace. It is stripped on both sides, but not fixture-tested.
6. Receipts for ids that are not in the register are harmless to `cmd_check`. Only `--receipt` refuses them.

**Attack surfaces:**
- **(a)** Does any `RECEIPTED`-status row carry a named target with no receipt? The checker ignores the status and blocks, which is correct, but WALTER's prune would then be wrong. None exists today (§4 cross-check).
- **(b)** The label builder: it reads `r['date_cap']` raw while `cap` is the parsed value.
- **(c)** Whether the §3(e) acceptance set in the docstring should be pinned to a frozen fixture copy rather than the live register. It will go stale the moment SAM receipts.

**Owed, outside this subagent's perimeter:**
- A `CHECKS.tsv` row update for this check (DAEDALUS lead).
- WALTER's register banner ("DAEDALUS's checker edit, pending"; "L139 skip … HIDES SAM's obligation"). It becomes stale on commit and is WALTER's file; send a packet, do not edit it.
- The commit itself, with the fleet before/after diff (§4) in the body per §3(d).

## §Addendum — independent read verdict + two residues fixed (DAEDALUS lead, 2026-09-24 evening)
**Independent read (`runs/2026-09-24_D4_CHECKER_INDEPENDENT_READ.md`): PASS-WITH-RESIDUE → D4(a) is FIXED.** 16 own counterexamples; checker-free re-derivation agrees on 25 of 25 desks; fleet delta SAM only; selftest 18/18.
**R4 FIXED (lead):** `main()` normalises the agent token once (`a.agent.strip().upper()`) before validation and path derivation. Fire: `corrections_boot_check.py hawk` was rc 1 with a false BLOCK on two receipted rows and a printed remedy that would have written `AGENTS/hawk/registry/`; now rc 0, identical to `HAWK` (clean case, unchanged output).
**R1 FIXED (lead):** in `cmd_check` a receipt row whose `action` is not in `ACTIONS` is `CORRECTIONS-CHECK 2 CANNOT-EVALUATE` (A2 law: unparseable is rc 2, never a discharge) — under D4(a) the receipt is the sole discharge, so a blank/non-enum action must not clear a named target. Fire: a scratch receipts file with `action=''` on COR-20260826-02 → rc 2 with the row named; clean: the same row with `NO-OP` → the check runs and SAM blocks only on its LIVE -0924-19 row (rc 1, expected). Selftest 18/18 unchanged (no new legs added for R1/R4 — declared; the two live runs above are the §3 proof).
**R2 (RETIRED discharges a named target with no receipt) → Will/WALTER by packet; not changed.** R3 (mixed `ALL,SAM` targets cell silently mis-scoped, no MALFORMED line), R5–R7: declared, pre-existing, not changed.
