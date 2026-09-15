# Independent review of the September 15 WALTER repairs

Reviewed: `2701229d4` and `ba3756c48`. Reviewer: independent Codex review worker, 2026-09-15. Scope: changed diagnostic behavior, executable instructions, read declaration, and shortened RULE 10. No live owner state, inbox consumption, external messaging, commits, or network-data collection performed by this worker.

## Verdict

One reproduced display regression and two remaining dashboard failure modes should be repaired before calling the dashboard hardening complete. The core state/routing corrections and the shortened RULE 10 preserve the examined gates. Boot declarations still need reconciliation with other executable instructions. No threshold changes are recommended by this review.

## Findings

### R1 — MED: quiet output can omit an indicator whose final zone is red

Location: `FORGE/tools/market-data/dashboard.py`, `main`, the new `display_results` assignment before `detect_transitions`.

`detect_transitions` mutates result zones when hysteresis retains the previous classification. Filtering first means the displayed set reflects preliminary classification instead of final classification. Reproduced with real transition logic: HY OAS current 279/yellow, prior 281/red, registered buffer 5. `--json --quiet --no-save` yields `results: []`, `summary.red: 1`, `data_completeness.status: COMPLETE`, exit 0. The corresponding old-red/current-red indicator is absent from a breaches-only display. Conversely a preliminary red retained as yellow can remain in that display.

Fix: construct the quiet display list after transition processing. Add a fixture using real `detect_transitions`; current new dashboard tests mock it and therefore cannot find this regression.

### R2 — MED: a non-finite value is certified COMPLETE and can generate a red classification

Location: `dashboard.py` `fetch_all` classification and the new completeness calculation in `main`.

Reproduced by patching `fred_fetch` to return `[{"value": "NaN", "date": "2026-09-15"}]` for the actual HY OAS series definition, then running the actual `fetch_all`. Its row is value NaN, zone red, formatted `nanbps`. Main reports COMPLETE, available 1, and exits 0. JSON includes the non-standard numeric token `NaN`. Positive/negative infinity also pass the new non-None completeness condition.

The provider/classification permissiveness predates this repair; the new COMPLETE assertion now blesses it. Validate finite numeric values before classification, normalize unavailable results to an explicit unknown/error row, and cover NaN/infinities through the fetch-to-main path. Do not reject zero.

### R3 — MED: an incomplete run still overwrites the last valid alert baseline

Location: `dashboard.py` `main`, save/transition operations occur before the new incomplete exit.

Reproduced with prior HY OAS zone red/value300 and a current unknown/None row. Main exits 3 but calls `save_state` with HY OAS unknown/None, replacing the valid baseline. Recovery to the unchanged red300 produces `unknown → red`, which cron logic considers a new red. It also records `red → unknown` as a zone transition during the failed fetch. This behavior predates the patch but remains a material gap in the attempted missing-data repair.

Fix: unavailable measurements should remain visible in output/log completeness, but should not become market-zone transitions or erase the last valid per-series baseline. Add a three-run valid → unavailable → unchanged-valid fixture. Also test agent/tier runs, which fetch the full set separately for persistence; a valid selected slice does not establish the other saved series are valid.

### R4 — MED: executable filter boot requirements remain outside the declared boot perimeter

Location: `design/FILTER_SPEC.md:9`–20, charter boot checklist, and WALTER rows of `PROME/registry/READS.tsv`.

The filter spec explicitly says “At session start, load” `FORGE/STATUS.md`, `AGENTS/RED/CALENDAR.md`, and recent `filtered/` and `routed/` contents. These are not written as dispatch-only conditions. They are absent from the charter boot sequence and the declared perimeter. The repair enumeration reviewed the charter sequence but does not resolve this second boot contract. Calling the entire effective boot manifest complete is consequently too strong.

Fix at the owning filter source first: specify whether these reads remain session-start requirements or are conditional filtering inputs, choose the actual scoped operations for recent ledger rows and position/catalyst evidence, then propagate into the execution path and manifest. Do not simply add whole-directory reads. Position mirror vintage and off-repo position authority must survive the wording.

Related declaration ambiguity: the repair `read-enumeration.md` says BOARD index discovery is followed by whole new signal bodies. READS contains the scoped index row, but no WALTER BOARD signal-body class. Charter step7 only says drill into clusters. Either name and declare the conditional body read or narrow the receipt to the actual index-only requirement. An undeclared dynamic-read disclaimer should not substitute for a known static class.

### R5 — LOW: two repaired tool contracts remain contradicted by the executable boot text

The parent independently identified these; verified here:

- Charter step7e(c) still says lane stale `>2d`; intake and doctor now use more than two missed weekday runs. Friday→Monday is a direct divergent case.
- Step7f's `ls … | grep …` counts Zone.Identifier sidecars and non-scaffold directories. Doctor now counts only regular files and excludes Zone.Identifier, while the manifest claims that latter operation. Use one shared enumeration contract or the same exact predicate in both paths.

These do not negate the code repairs, but an agent executing the prose can reproduce the old errors.

### R6 — LOW: delivery lifecycle prose is still inconsistent within the revised spec

`BOARD_CONSUMPTION_SPEC.md` revised `written_state` table allows WALTER's origin-proven post-push promotion. The next “Critical (requirement B)” paragraph still says WALTER records written/committed state only and delivered state is derived read-only by doctor. Clarify that WALTER reconciles the stored claim using git evidence, while doctor independently derives/verifies delivery and PROME never edits the log. This is an instruction consistency fix, not new authority.

## Verified behavior and coverage limits

- Ran `AGENTS/WALTER/tools/test_boot_repairs.py`: all 8 tests passed.
- Ran `AGENTS/WALTER/tools/test_false_assurance_regressions.py`: all 67 behavioral assertions passed. This includes origin-history proof and ownership-sensitive consumption checks.
- Verified all 18 hash entries in the repair basis snapshot against the exact `2701229d4` blobs: no mismatch.
- Reviewed weekday cadence and malformed/future timestamp handling. Weekend behavior is consistent across the two consumers; holidays are deliberately counted and scheduling within a day is not modeled.
- The version guard now scans the registered inline CANONICAL form and table forms, checks companion headers, and fails visibly on unreadable sources. It is deliberately not a semantic contradiction detector. A single remaining recognized reference does not prove every reference in all prose was examined.
- `reads_check.attestation_stale` uses git calendar dates. Same-day changes and dirty edits to previously tracked basis files do not invalidate that date comparison; the stored hashes are not enforced there. This is a pre-existing, material coverage limit. A WALTER-local hash check can close it without silently changing every fleet reader's contract.
- The new runtime section correctly preserves UNKNOWN for absent fleet visibility rather than inferring DARK. Thread-local agent visibility is explicitly insufficient.
- Shortened RULE 10 preserves create-only handoffs, recipient-only consumption, actionability escalation, CARL/RED ACTION overrides, PROME fail-safe treatment, TERRY's resolved ID-diff choice and precise reopen conditions, and the no-new-NOTE-telemetry rule. The archived original wording remains available. I found no lost routing gate in that rewrite.
- The maintained MED for legacy NOTE rows is appropriate pending content-level review. Shape classification is not actionability proof.
- No independent current-market grading, image interpretation, recipient integration verification, or source-level war-state validation was performed by this review worker. Passing fixtures do not establish an operationally complete boot.

## Reproduction recipe

Use the repository `.venv/bin/python` and insert `FORGE/tools/market-data` into `sys.path` before importing `dashboard`. All reproductions are fixture-only:

```python
from unittest.mock import patch
import sys
sys.path.insert(0, 'FORGE/tools/market-data')
import dashboard as d

# R1: real hysteresis mutates yellow to red after quiet selection.
rows = [{'name': 'HY OAS', 'value': 279, 'zone': 'yellow', 'emoji': '', 'tier': 1}]
with patch.object(sys, 'argv', ['dashboard.py', '--json', '--quiet', '--no-save']), \
     patch.object(d, 'fetch_all', return_value=rows), \
     patch.object(d, 'load_last_state', return_value={'HY OAS': {'zone': 'red', 'value': 281}}):
    try:
        d.main()
    except SystemExit as result:
        print('exit', result.code)

# R2: actual fetch/classification path accepts non-finite FRED value.
series = next(s for s in d.SERIES if s['name'] == 'HY OAS')
with patch.object(d, 'fred_fetch', return_value=[{'value': 'NaN', 'date': '2026-09-15'}]):
    print(d.fetch_all([series]))

# R3: patch save_state/append_log to mocks (never write real cache), feed
# unknown/None with a prior red300 baseline, invoke main without --no-save.
# Inspect save_state.call_args.args[0], then feed that dictionary to
# detect_transitions([{'name':'HY OAS','value':300,'zone':'red'}], saved).
```

Disposition: parent owns fixes and final regression reruns. This report records the reviewed pre-fix implementation and must not be interpreted as a claim that later changes remain defective.

## Independent post-fix verification — R1–R3

Reviewed the parent's working-tree changes to `dashboard.py` and `test_boot_repairs.py` after the report above. **R1, R2 and R3 are resolved within the tested perimeter.** No implementation edits were made by the reviewer.

- **R1:** quiet selection now happens after real transition/hysteresis processing. New fixtures cover both preliminary-yellow retained-red and preliminary-red retained-yellow, checking displayed count against final red summary.
- **R2:** current and comparison non-finite values are normalized before classification and serialization; current unavailable values produce rc3. New fixtures exercise NaN and both infinities through actual FRED fetch normalization into main, then require strict JSON serialization. Additional independent fixtures confirmed non-finite prior values preserve a valid current300 observation while clearing `prev` and `change`.
- **R3:** unavailable rows generate no market transition and do not replace the previous valid baseline or its timestamp. The new three-run fixture proves unchanged-red recovery is not a new alert. Agent/tier runs now fetch only the selected scope once and preserve other baselines, avoiding the second unobserved full-market fetch. Additional independent fixtures exercised both cron and notify: an unchanged existing red returns1, unavailable returns3, neither emits a notification, and the failed run preserves the complete prior dictionary. Recovery from a legacy unknown baseline also creates no synthetic transition.

Validation: **all 12 repair tests passed**, plus **8 independent fixture checks** (four cron/notify combinations, three invalid-prior variants, one legacy-unknown recovery). Save, append-log and notification functions were mocked in main-entry fixtures; no live cache, owner state or external messages were written.

Limits: this acceptance covers R1–R3 and the examined scoped-save behavior, not every possible malformed provider payload or broader threshold/hysteresis design. R4–R6 documentation/perimeter work remains with the parent and was not re-reviewed in this follow-up. No network-data validation was needed or performed.

## Independent guard verification — basis freshness and archive pairs

Added reusable `tools/test_resolution_guards.py`; **all 14 tests pass** against the current implementations. These exercise production functions with isolated filesystem and Git fixtures.

- **Basis guard:** matching bytes; changed bytes with the original nanosecond mtime preserved (therefore independent of same-day/dirty-edit clocks); missing source; added/removed declared basis; foreign-reader exclusion; absent manifest; absent hash record; malformed JSON and malformed hash-record schema. The first review found `[]`/`null` caused an uncaught AttributeError; the parent added explicit object/SHA256 validation, and the rerun covers that fix plus invalid values.
- **Archive guard:** exact staged move passes; unpaired deletion and edited move require review; foreign deletions remain explicitly outside the perimeter; foreign additions cannot satisfy a WALTER deletion; a single identical addition cannot cover two deletions; unstaged deletions are outside the staged-only perimeter. Fixtures use real Git index/blob behavior with rename heuristics disabled, not mocked name-status output.

No live Git index, cache or owner state was changed. The only added implementation-adjacent file is the reusable test module. This acceptance concerns declared byte identity and staged byte conservation: it does not certify complete read declarations, actual reading, semantic preservation in edited/split archives, all filesystem metadata, foreign-file safety, or unstaged deletions. A deliberate edited/split move must still supply separate conservation evidence and receive the named review rather than being silently auto-cleared.

## Independent later-consumption verification and production recheck

Extended `test_resolution_guards.py` with five receipt tests, including the full `check_filed_vs_consumed` branch using controlled Git responses and real temporary ledger/evidence files. **All 19 guard tests and all 12 boot-repair tests pass** on the final recheck of this review pass.

Verified exact filename and owner matching (both `WALTER` and `consume:WALTER` forms); aliases and wrong owners fail. Missing ledgers, missing evidence, absolute/outside paths, future dates and dates preceding the move fail. A valid later evidence-backed receipt resolves the original production warning; a receipt naming another owner does not. The first run exposed a date-prefix bug: `2026-09-15NOT-A-DATE` passed because only the first ten characters were parsed. The parent changed this to a complete YYYY-MM-DD check and full date parse; the regression now passes.

**Required documentation alignment remains at this review point:** `BOARD_CONSUMPTION_SPEC.md` §5.1 lines459/463 still defines consumption solely by declaration in the moving commit. Add the later exact receipt path explicitly, including review-date semantics, exact owner/file, existing local evidence and the distinction between retrospective verification and historical consumption time. The tool may check the existence of the evidence pointer; it cannot establish that its content actually proves integration. That human review requirement must remain explicit. Do not describe a later review as independently measured historical read time, and do not weaken the recipient-only consumption boundary.

Rechecked the changed production diff for `walter_doctor.py` and `dashboard.py` and inspected the shared drop-zone enumerator. No additional blocking code defect was found in this bounded pass after the date fix. Drop-zone doctor and CLI now use the same predicate; dashboard retains the previously verified R1–R3 repairs. This is not an exhaustive audit of unmodified doctor checks or every provider payload. The spec/implementation mismatch above needs resolution before claiming this lifecycle change fully documented.


## Final dispatch and telemetry review — 2026-09-15

Independent read of SIG-W-20260915-001 through 008, their recipient copies and `dispatches.json`, followed by the separate 009 Fitch arrival. Three prepublication findings were sent to the parent and verified repaired:

- **MED — index taxonomy split:** quoted cluster/domain/precedence scalars were retained literally by the existing index generator. New signal scalars are now parser-compatible; the generated INDEX no longer has a separate quoted BANK_COLLATERAL group.
- **LOW — INFO exemption violation:** SIG-001 initially wrote a CARL INFO handoff despite RULE10. That copy and delivery row were withdrawn before publication; CARL remains a valid BOARD INFO reader. SIG-008 retains its distinct CARL ACTION handoff.
- **LOW — original correction placement:** SIG-027 had the new cycle correction appended below the old content. Its explicit partial-correction banner now appears immediately after frontmatter and points to SIG-002; the conference/BAC remainder survives.

SIG-002 IMMEDIATE body is 146 words, within the specification's 200-word **body** limit. Full handoff/header size is not that limit. Source qualifications remain explicit: gasoline is not natural gas; CMBS and Saudi cargo reports are secondary; Yasref event date and facility attribution remain unresolved; IATA jet/Dated-Brent basis is separated from ULSD; Shanghai arithmetic and contract basis remain unresolved; CARL trend completion is SEARCH-NOT-FOUND, not proven absence. Each ACTION names the required verification or changed-path/no-change receipt and owner; none claims recipient completion merely from routing.

SIG-009 separately distinguishes the secondary August 6.3% observation from the primary Fitch methodology, issuer counts from dollar losses, and default events from newly defaulting borrowers. BROCK must recover the original and verify the cohort before updating its May carry. No additional framing/routing blocker found within this bounded artifact review. Final observed publication set: **9 BOARD signals and 29 recipient handoff files** (the original eight now account for 24; Fitch adds five). This review did not independently retrieve external sources or certify their truth.

Added two reusable production fixtures in `tools/test_resolution_guards.py`: simultaneous consumed-but-unfiled and archive notices survive together, with three full-scan mtime rows distinguished from one aged warning; quoted correction targets accept JSON/single-quoted and legacy forms while rejecting empty EXTERNAL targets, invalid quoting and nonexistent SIG targets. **All 21 guard tests pass.** The retrospective reconciliation paragraph is now present in BOARD_CONSUMPTION_SPEC §5.1 and explicitly limits the checker to exact owner/name/date/existing evidence, not semantic certification or original read time.
