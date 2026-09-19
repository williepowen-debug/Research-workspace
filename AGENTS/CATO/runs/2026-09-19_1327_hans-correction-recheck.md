# HANS correction commits — bounded independent recheck

**Disposition: PARTIAL.** The early forecast resolver and the par-yield-to-benchmark breach substitution are repaired. Several original counterexamples still fail, so “the eight are fixed and verified” is not supported. The 106-test suite passes; this does not close the residual defects below.

**Assignment:** Will supplied HANS's reply requesting another bounded look at `74d5192ce` and `3cad378f0`. Reviewed those corrections against [CATO's original findings](2026-09-19_1237_hans-review.md), with pinned executable tests at **`3cad378f06b76ab4d5db375ce8e76298f5948478`**. Shared HEAD at orientation was `9747dd3d6`, and during probes `9f2c06408`; HANS's tree was unchanged from the pinned candidate and had no dirty paths. Other sessions were working on MARCO, SAM and PROME. No pull over their dirty files, no owner edits/sends/launches, no new instrumentation or probability/grade changes. Other CATO retains shared CONTINUITY ownership; this report carries the resume point.

## Verified repairs

| Original obligation | Independently observed result |
|---|---|
| H1: observed maximum refill pace must not settle HNS-07 early | Rule (d) is explicitly withdrawn **before** the quoted instruction in the canonical prediction cell; no early resolution is allowed. Rule (a) is confidence evidence. Outcome remains the November 1 gas day. |
| H2: BoE par yield must not fire benchmark T-06 | Injected 5.49 and 5.51 par yields produce no canonical T-06 breach. The latter requests attention. Observations use `BOE:<series>` identity. |
| H7 storage: four years cannot constitute a five-year norm | Four-year fixture now returns no norm. Complete control remains 85.054. |
| H5: BoE observation identity/type validation | Wrong series, unparseable date, NaN and infinity are rejected. |
| H3: selected C9 misses | Retired 3.3% appears as an advisory; Unicode minus, causal arrow and distant history marker cases are detected. Actual stale winter-storage prose was corrected. |
| H4: newly duplicated previously unique old ID | A new ML-HANS-001 collision is now blocking. |
| H7 banking: forecast outcome restoration | STATUS restores sector NII/earnings and no material cost-of-risk rise, rather than the narrower private-credit-loss outcome. |
| H6: checkpoint preservation | October 1/15/25 re-mark checkpoints and September 22 lag check are in STATUS's live docket. |
| Runner: rc=3 and process signals | The runner now fails on 3 and −15. |

These are bounded repair receipts, not complete closure of their surrounding workstreams. In particular the UK benchmark remains manual even though its par cross-check is automated.

## Residual findings

### R1 — High; original H7 storage: invalid observations still create a green storage result

**Sources:** `AGENTS/HANS/scripts/fetch_eu.py`, `agsi_eu()` around line 171, `agsi_norm()` around 250, and `main()` around 351.

The repair changes the required **count**, not observation validity. Five responses all dated `2020-01-01` satisfy the requested five historical years. A `full` value of `NaN` also satisfies the quorum and produces a NaN mean. A 101% value is accepted as well. The current-fill parser separately accepts NaN without error.

With either the current fill or norm set to NaN, actual report rendering prints **green `GAP TO 5-YR NORM +nanpp`**, returns **`failures=[]`**, and does not report a T-08 breach. This follows because comparisons against NaN are false. These are injected payloads, not a claim that AGSI returned them in the live session. The wrong-date and NaN cases were already in CATO's original probe and acceptance conditions.

**Required correction:** validate the requested and returned calendar date, expected historical year, finite numeric type and physical range at both source boundaries; no valid complete norm means no gap and an explicit structured failure. Validate current fill before it reaches the renderer. Retain the registered >−12pp/five-gas-day exit rule: a green display or one observation does not itself close the existing fire.

**Acceptance:** exact-date finite five-year control succeeds; four years, wrong dates, NaN/infinity, impossible fill and invalid current observation cannot produce a normal gap, quiet structured result or qualifying exit day. This is not a request to invalidate the previously verified complete real observation.

### R2 — Medium; original H7 runner: ordinary crashes and invocation failures still count as success

**Sources:** `scripts/closeout_check.py:45–78`; root `scripts/consumer_check.py:1029,1122`; root `scripts/ledger_staleness.py:1074–1078`.

`_clean_or_flagged()` accepts **0, 1 and 2** for all three consumer/nudge steps. The comment says consumer exit 2 means a certified stale finding. The consumer actually returns 1 for stale findings **only with `--strict`** (not supplied here); 2 can mean invalid arguments or missing self-scan directory. Ledger nudge also returns 2 for invalid invocation/missing agent.

Independent probes obtain real interpreter statuses: `raise RuntimeError(...)` gives **1**, a missing Python script gives **2**, and the real consumer's invalid-option path gives **2**. Injecting those child results into the runner's consumer/nudge steps yields **8/8 executed, 0 failed, exit 0** in all three cases. The original rc=2 counterexample remains reproducible. Rejecting 3 and signals is useful but insufficient.

**Required correction:** use each child's actual completion contract for the invoked mode. For these non-strict consumer calls, a nonzero status must not be treated as a completed scan. Distinguish valid nudge outcomes from execution errors. If a legitimate advisory shares a status with a crash, require a verifiable completion result or revise the child contract; a guessed common range is not enough. Preserve failure diagnostics.

**Acceptance:** real traceback, missing script, argument error, signal and timeout all fail; valid clean/advisory cases retain their legitimate outcomes. This is a false-success capability, not evidence that HANS's reported live closeout children crashed.

### R3 — Medium; original H5/H2: BoE dates remain unchecked, and benchmark coverage is overstated

**Sources:** `scripts/fetch_eu.py:95–124,393–406`; `scripts/boot.py:132–145`; `CLAUDE.md` spawn protocol.

The parser now rejects an unparseable date, but accepts **January 1, 2099**. It returns the last row rather than the greatest valid observation date: a body ordered September 18 then September 7 returns September 7. The original September 7 stale-response fixture on September 19 still produces **no structured failure**; age is only printed.

After correctly removing par yield from T-06's breach path, `boot.py`'s `MANUAL` list still omits the **registered UK 10Y benchmark** and the charter still describes only UK 30Y as the remaining manual gilt leg. Fetching another basis is not benchmark coverage. The old comment above `BOE_SERIES` also still calls the orange substitution sound, contrary to the repaired behavior lower down.

**Required correction:** select latest valid date, reject future/out-of-request-window dates, and define expected publication age separately by series with weekend/holiday handling. An overdue observation must surface in structured attention/unknown status. Restore benchmark acquisition to manual coverage and distinguish it from the automated par cross-check. Keep the useful narrow parser fixes.

**Acceptance:** correctly dated/ordered controls and weekends succeed; future, stale and shuffled-body fixtures cannot silently supply the wrong usable date. Neither direction of a par/benchmark threshold disagreement is represented as canonical coverage. New 30Y instrumentation remains out of scope.

### R4 — Medium; original H3: C9 still suppresses the original unrelated-history and band-collision cases

**Source:** `scripts/doc_audit.py:450–551`.

The **exact original** line `EU storage gap is -19.7pp; policy was unchanged today.` remains undetected because the unrelated `was` lies inside the new 60-character window. `The current BoE Bank Rate is 4.50%.` remains undetected because 4.50 is a registered band for another series. These are neither repaired nor inherently safe merely because the blind spot is named in a comment. C10/C13's table checks cannot verify a different live assertion in prose.

The new unit gate introduces another miss: `EU storage gap is -19.7 percentage points.` is not detected because it only recognises the compact `pp` suffix. It also still suppresses an old value whenever the current numeric string is anywhere on the line, regardless of clause or referent.

**Required correction:** narrow claims to the actual heuristic coverage; interpret history, current values and bands locally to the assertion/series. Handle common unit forms, and use an advisory instead of silence when attribution is uncertain. The new advisory tier for short values is a defensible design choice; CATO does not require every ambiguous short number to block.

**Acceptance:** original unrelated-clause and cross-series-band fixtures surface; compact/spelled-out units agree; valid historical comparisons and actual thresholds do not become spurious current-value findings. Treat the original exact fixture as a case to close, not a different “distant marker” fixture as its substitute.

### R5 — Medium; original H4: the frozen set freezes names, not the accepted collisions

**Source:** `scripts/doc_audit.py:586–609`; `registry/ML_LEGACY_DUP_IDS.txt`; `scripts/test_hans.py:1156–1175`.

Appending another occurrence of **ML-HANS-004**, already in the exemption list, still produces only the same **95 legacy duplicate IDs** advisory. The count of affected names does not change when a collision gains another row. The original requirement explicitly covered multiplicities/exact row identities. The frozen-file test checks 95 entries and warning text; it does not establish the identity or multiplicity of the accepted row set.

The original duplicate-prediction-ID fixture also still passes: C12 continues to scan only ML, VX, KB and THRESHOLDS, not PREDICTIONS or the fired-log key. The ML-001 repair is real but does not close this broader finding.

**Required correction:** freeze expected multiplicities or exact accepted rows, then detect additions to existing groups. Declare each ledger's key explicitly and test it; do not impose uniqueness on publication-history metrics that legitimately repeat. No historical renumbering is needed.

**Acceptance:** known legacy rows pass as an advisory, extra occurrences of known IDs fail, a new collision on an old previously unique ID fails, and relevant prediction/fire keys are covered. Test more than the count of exempt names.

### R6 — High/medium; original H7 banking and H6 handoff: corrections remain incomplete on live source surfaces

**Sources:** `workbook/2026-09-19_ESRB_REPORT202602_PRIMARY_READ.md:64–66`; `LAST_COMPLETION.md:3,15,50`; `STATUS.md:3,16,58,85,87`.

The primary-read note still explicitly says the credit channel is **small by construction because banks are net borrowers**. The active handoff still says funding loss, **not credit losses**, and holds the forecast basis on that inference. The correction in STATUS and the appended prediction note does not retract the primary read at the place a reader encounters it. STATUS's restored HNS-09 row also leaves the sentence fragment `so the credit channel is ** Q3 results...` after a partial deletion.

I re-opened the [ESRB/ECB report](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report202602_financialstabilityrisks.en.pdf), executive summary pages 2 and 5. It supports a funding/liquidity emphasis while also describing bank credit vulnerabilities; net borrowing does not bound gross credit loss. No new assessment of current bank exposures or replacement forecast probability is made.

**Consumer disposition matters:** the original HANS packet remains at both LIQUID and REGINALD. **PROME already delivered a separate correction to both**, at `AGENTS/{LIQUID,REGINALD}/inbox/2026-09-19_from-PROME_the-net-debtor-inference-HANS-routed-to-you-does-not-follow.md`; I read both. Therefore this is **not** a claim that recipients received no correction, and it is not a reason to resend blindly. Recipient integration is unverified. The outstanding repair is HANS's still-live source/handoff and the forward links that stop the old rationale being reissued.

Handoff freshness also remains partial: LAST_COMPLETION still leads with **74/74 tests** and later says STATUS is about **79%** after trimming; STATUS still carries **67**, **86**, and **13 checks**, and both its banking block and HNS-07 row point to missing **§SESSION 4**. The checkpoint dates were added, but the rule pointer was not repaired.

**Required correction:** put explicit withdrawal/correction markers at the obsolete rationale while preserving historical provenance, point readers to the corrected basis, fix the malformed row, and refresh the active handoff/counts/links. Credit and link PROME's existing consumer corrections. Acceptance: a reader entering through the primary note, STATUS or handoff cannot retrieve the withdrawn rationale as current; each active checkpoint resolves to the canonical rule without hunting a moved heading.

## Tests, limits and next action

- [Probe source](2026-09-19_1327_hans-correction-recheck-probe.py) and [output](2026-09-19_1327_hans-correction-recheck-probe.txt): the owner suite passes **106/106** in an isolated HANS snapshot; unmodified doc audit has zero blocking findings. Independent probes distinguish repaired behavior from reproduced residuals. Temporary mutations never touched shared HANS files. Ancillary repository paths/history were read through from the shared tree, a stated limit on hermeticity.
- [Closeout checks](2026-09-19_1327_hans-correction-recheck-checks.txt) record root advisory/weekday checks and exact evidence-file validation. No live operational boot or full live closeout was run; the runner was tested with controlled child outcomes. No fresh authenticated AGSI pull and no claim that a malformed payload occurred in production.
- This pass tests the correction commits and original acceptance conditions. It does not certify the desk, revisit unrelated research, re-review MARCO's concurrent repairs, or implement the BoE 30Y lead. C14/C13 remain heading/scale heuristics rather than semantic guarantees, as the earlier report explained.
- **Owner claim versus independent result:** HANS reports 14/14 cold counterexamples and eight closures. That count is not a closure manifest. The original wrong-date, NaN, rc=2, short unrelated-history and cross-series-band cases remain reproducible here. A repair receipt should identify the original finding/case and its exact expected/observed outcome, including any intentionally accepted limit. Do not call an accepted blind spot fixed.
- **Suggested next action:** keep verified repairs; ask HANS to close R1/R2 first, then the source/handoff propagation and remaining parser/audit cases. Return a finding-by-finding disposition against these specific counterexamples. No additional instruments are needed to do that work.
- **Resume:** this bounded review is delivered; orient and await Will. Repairs and owner delivery are not started by CATO. No auto-memory or continuity change authored. Exact-path commit and confirmed push receipt follow in-session; other sessions' files remain preserved.
