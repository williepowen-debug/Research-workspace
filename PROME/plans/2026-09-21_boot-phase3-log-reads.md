# Phase 3 — bounded orchestration-log reading

**Authorization:** Will, “Okay go on ahead and proceed with phase 3,” after CATO's Phase 2 acceptance and the B4/B5 maintenance corrections. Implements a bounded part of recommendation 4: shorter default check output with complete evidence retained. Incremental boot, capability frameworks, ledger repairs and manifest re-attestation are outside scope.

## Measured scope and proposed implementation

The existing saved boot `/tmp/prome-boot-codex-20260921-1608` is historical evidence, not a fresh boot. `measure.py` measured its orchestration closeout log at 33,180 bytes, the largest individual check log in that run. Its dominant repetition is `UNKNOWN: <date desk touch full-key>: missing or duplicate structured closeout evidence`. Phase 3 factors only this identical reason, retaining each full record identity in original order. It makes no assertion that a gap is unchanged since another boot, historical-only, resolved, nonactionable or safe to omit.

Extend the existing `PROME/tools/boot_read.py` with `--view orch-compact-v1`. Recognize the exact `orch_closeout.py` header and consecutive runs of at least two exact missing/duplicate-evidence rows. Print the shared UNKNOWN reason once per run, followed by every date, desk, touch and full key. All other text stays verbatim, including receipts, pending asks, dark-before-ask evidence, inventory gaps, other UNKNOWN reasons, malformed rows, and any new exception. No severity, time, owner, state or exit-code inference. No output limit beyond the existing bounded pages, which must still be read to EOF.

The complete original log stays on disk. Rendering occurs on read; no cached summary, baseline or new report registry. Unrecognized header/shape produces full text and `full-fallback` metadata. Missing/unreadable data never produces a clean/empty result. Continuation digests bind both the original bytes and selected view so source changes or accidental mode switches cannot reuse offsets. Full mode retains its interface and raw-source SHA.

Exact candidate: `/tmp/prome-phase3/boot_read.py`. Scope is the reader, its tests, BOOT's explicit exception, both boot skill indices, this record and concise continuity updates. The gate, producer, one-shot runner, BOARD cursor and check severities/exit codes are unchanged. READS remains unrenewed: its schema does not admit `/tmp` log paths; do not invent a repository path or broaden the registry framework to conceal that known completeness limitation.

## Acceptance conditions — written before implementation

1. Every identity and every distinct reason/caveat in the input is present in the read representation. The sole transformation is factoring the one repeated exact UNKNOWN reason; no line disappears based on age, rc, severity, owner or apparent completion.
2. An old pending ask, a current missing receipt and a novel failure remain visible alongside grouped gaps. Different reasons, malformed/unrecognized rows and inventory-coverage gaps remain verbatim. No receipt or native-presence claim is inferred.
3. Full logs stay byte-identical. A missing/unreadable input returns UNKNOWN/error, never EOF success. Unsupported formats fall back to full text. Other logs and `gate.txt` still require full reads; previews never suffice.
4. Every page stays within the existing serialized-text budget; complete pagination reconstructs the exact compact representation. Changed sources, mode changes, invalid offsets and missing continuation digests refuse rather than skip evidence.
5. BOOT and both skill indices agree on the exception and fallback. The full-log contract remains binding elsewhere; no new boot run directory or raw gate call bypasses the one-shot rule. Full mode is the immediate rollback.
6. Verify with disposable fixtures under strict ResourceWarning; do not run a live boot. Replay the saved report read-only for measured byte reduction, not runtime/token savings or renewed operational state.
7. One independent plan read before production edits and one independent result read with a reviewer-designed counterexample. Fix blockers; declare advisories under the existing read budget. Report implementation, tests, independent verification and remaining limits separately.

Neighbour cases: ordinary repeated gaps; overlap old pending work/current gaps/novel findings; wrong-owner entries and keys preserved without reclassification; missing header/log/digest and malformed rows fall back/refuse; concurrent source edits and representation switches invalidate continuation. None is N/A.

## Exact instruction amendments for plan review

**BOOT step 5 replacement for “Read `gate.txt` with the bounded reader, then the full check logs it names; previews are not complete evidence.”:**

> Read `gate.txt` with the bounded reader, then the check logs it names to EOF. Read every log in full except the “orchestrated touch closeout evidence (WQ-249)” log: for that log use `python3 PROME/tools/boot_read.py <log-path> --view orch-compact-v1`. This view factors only repeated identical UNKNOWN evidence-gap wording; every date, desk, touch and full key remains visible, all other text stays verbatim, and UNKNOWN never becomes a receipt. Retain the same `--view` on each continuation with the returned `--offset` and `--sha256`. The digest binds source and view; a refusal requires restarting at offset 0. `full-fallback` means read the returned full text to EOF. If the compact view is unavailable or errors, read the original log in full; a missing/unreadable original remains UNKNOWN. Full logs remain the drill-down source. Previews are not complete evidence.

**Both boot skill indices, step 2, replace the final sentence with:**

> BOOT.md step 5 owns the gate's meaning and log-read contract (including the bounded orchestration-log view and full-text fallback); step 6 owns the board-scan re-run rule.

Update BOOT's stamp with this dated record; no other rule changes. Continuity will state Phase 3's exact scope and keep incremental boot deferred. The historical Phase 2 record is not rewritten as if shorter reads were already approved then.

## Review and completion

- Plan review: `phase3_plan_review` found zero blockers/advisories before production edits. Its disposable counterchecks retained identities, Unicode findings and inventory caveats across pages, refused changed-source/mode continuation, and confirmed unfamiliar-header fallback. Read-only closeout acknowledged; no edits, commits or live/stateful checks.
- IMPLEMENTED: the reviewed reader and instruction amendments are applied; both boot skill indices match. HANDOFF/SCRATCH point to this bounded scope. Gate execution, producer, one-shot runner and check severity are unchanged.
- TESTED: `python3 -B -W error::ResourceWarning -m unittest PROME/tools/tests/test_boot_log_view.py PROME/tools/tests/test_orch_closeout.py` passed 29 tests. Covers fixture producer integration, every identity/order, old pending asks/current gaps/new findings, wrong-owner preservation, unfamiliar formats, missing inputs/UTF-8 failures, paging limits, source changes and mode switches. Saved-report replay preserves the original and matches complete paginated reconstruction. Protected-source hashes, generated blocks/cautions, skill parity, table checks and scoped whitespace passed. Declared read-cap rc=0; HEARTBEAT's separate rotation-tier finding remains outside scope. The orphan tool labels the root skill copy by location; that exact parity edit is self-authored within this authorized batch.
- INDEPENDENTLY VERIFIED: `phase3_result_review` found zero blockers/advisories and independently reproduced the 29-test pass. It recovered all 201 full keys in order from the saved report, including the old ARGUS pending ask, HAWK timing/shutdown caveats, dark-before-ask evidence, invalid timestamps and inventory UNKNOWN. Its own counterexample combined duplicate identities, wrong-owner labels, mixed CRLF/LF, a near-identical reason with an added required action, Unicode separators and an unterminated final row; multiplicity and exceptions survived. BOM/unfamiliar-header cases fell back; same-size source changes and view switches refused. Both reviewers explicitly acknowledged read-only closeout with no edits, commits or live/stateful checks; receipts are in ORCH_LOG. No result corrections or advisory residue were required.
- STILL UNRESOLVED: older READS completeness attestation, carried operational obligations and native/private capability limits. This change does not resolve any of them or establish faster boots. Only one repetitive log format is shortened; all other logs remain full reads.

## Frozen saved-report measurement — 2026-09-21

Measured through `PROME/tools/measure.py`: original orchestration log **33,180 bytes**, CRC32 **1765509790**; rendered text **22,536 bytes**, CRC32 **3861198606**. Reduction **32.1% for that log**, with two groups of repeated wording. Rendering output: `/tmp/prome-phase3/saved-orch-compact.txt`; exact source path above. JSON page envelopes are excluded from these text-byte measurements. This is neither a new boot receipt nor measured latency/token savings. The original log is unchanged; no finding is resolved by presentation.
