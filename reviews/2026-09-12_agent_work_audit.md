# September 12 agent work audit

The desks delivered substantive work, but the session report overstates completed coordination. PROME committed invalid decision-ledger events and left completed desk work pending in its tracking. DAEDALUS's new read-cap consumer also has reproducible false-green paths despite its passing selftest.

Scope: changes after `381ea6efb` through `408e87e20`. Inventoried the changed paths and commits; deeper inspection covered the six desk deliveries, corresponding PROME records, READS consumer, spawn-driver repair, pipeline guard, RED's board-gap and threshold arithmetic repairs, and selected shared-script fixes. This is not an assertion that every changed sentence was audited. Relevant inspected live files still matched the pinned revision at verification. The checkout contained unrelated dirty files; no operational state was edited, no pull/push was performed, and no agents were messaged. Only this review and its evidence files were added.

## Findings

### 1. High — PROME's four new decision-history events are invalid

**VERIFIED by the existing validator on before/after committed snapshots.**

`PROME/registry/WQ_LEDGER.tsv:214–217` contains the new WQ-234, WQ-235, WQ-219 update, and WQ-236 records. The three new registrations use `OPENED`, which is not an allowed event. All four have date-only `written_at` values and empty verdicts that the validator rejects. The committed CRC sidecar was not updated with these additions.

Before this session, the committed ledger and sidecar pass. At the audit boundary they produce **12 problems and rc=1**. This is an actual regression in operational records, not a hypothetical fixture. The ledger engine refuses synchronization on a broken seal. The bad additions were committed in `14e6f6bb1`, `67e84de4a`, and `c9f4a4fbe`.

PROME's statement that it registered the decisions with ledger rows is literally true, but those rows do not satisfy the ledger's contract. Their shape is inconsistent with the engine's normal generated rows; the artifact proves invalid additions, not the exact command used to write them.

Repair: preserve all four events and their provenance, reconcile them against the queue through a reviewed recovery, and validate the resulting ledger and seal. Do not blindly follow the validator's generic checkout instruction: the invalid ledger is already committed, so restoring current HEAD would not repair it.

Evidence: [before](evidence-2026-09-12/ledger-before.txt), [after](evidence-2026-09-12/ledger-after.txt). Reproduce with `python3 PROME/tools/wq_ledger.py check`; historical comparisons used `git show REV:PROME/registry/WQ_LEDGER.tsv` and the matching `.crc` in temporary files.

### 2. High — the new read-cap consumer can replace malformed evidence with a passing heuristic

**VERIFIED with pinned-code temporary fixtures.**

`scripts/read_cap_check.py:259` detects a malformed header, but `declared_reads()` returns the same absence-shaped result used for an undeclared desk. `check_agent():443` then falls back to the charter heuristic unless strict mode is explicitly requested. With a malformed manifest and a small STATUS, both `--agent TEST` and `--fleet` return **rc=0**. The output says the desk has no declaration rather than exposing the parse failure.

This directly violates acceptance condition C10 in `AGENTS/DAEDALUS/runs/2026-09-12_R7_STAGE2_READS_CONSUMER.md`: an unparseable/half-written manifest must return rc=2. Preserving heuristic compatibility for genuinely undeclared desks does not justify doing so after a failed parse.

A second schema weakness: `declared_reads():302` treats any self-signed ATTESTATION row as complete without checking its mode. A fixture with mode `NOT-COMPLETE` still prints ATTESTED and passes.

Repair: distinguish absent desk declarations from unavailable/malformed manifest evidence, validate attestation fields, and exercise the public agent/fleet paths in tests, not just the parser helper.

### 3. High — fleet mode discards errors the per-agent checker already detects

**VERIFIED with two independent fixture triggers.**

In `scripts/read_cap_check.py:761`, fleet mode obtains each desk's `rc` but determines failure from over-budget counts alone. A missing declared file yields **rc=1** under `--agent TEST`, yet **green, zero reads, rc=0** under `--fleet`. A misspelled read mode on an oversized file produces the same inconsistency. `--require-manifest` is also parsed but not passed into fleet-mode `check_agent()` calls.

Repair: aggregate every desk's result, retain manifest defects in fleet output, and honor the strict flag in fleet mode. A missing required input cannot disappear into a zero-read green row.

Findings 2–3 evidence: [reproduction script](evidence-2026-09-12/reproduce.py), [observed output](evidence-2026-09-12/reproduction.txt). The script loads the audited code from Git and creates disposable fixtures; it does not edit production declarations.

### 4. Medium — delivered work is still pending in PROME's authoritative tracking

**VERIFIED at the pinned artifacts.**

- BROCK's L260 grade and OTTO's L311 grade are delivered; RED's delivery discharges L320. Yet `PROME/DOCKET.tsv:260`, `:311`, and `:320` remain PENDING.
- All six September 12 rows in `PROME/state/ORCH_LOG.tsv` remain IN-FLIGHT, with drain/outcome cells unfilled, despite the report declaring the desks terminal.
- `PROME/SCRATCH.md:6` still says the COT grade has not landed and is the first act of the next boot. Its generated overdue list still carries the three completed desk rows.
- L294 is marked RESOLVED but still says PROME's consumer read is owed, despite the session report and consumption commit claiming that read.

These do not negate the desk work. They mean the claimed closure has not fully reached the surfaces that drive the next boot. Some write-backs may await formal closeout; the screenshots are a session report, not independently established proof that closeout ran. Even on that interpretation, these are unfinished closeout obligations, not completed tracking.

Repair: reconcile the delivered artifacts into the existing docket and orchestration rows, then regenerate dependent views. The existing two-correction restriction on ORCH_LOG is a known procedural constraint, not evidence that the rows are already closed.

### 5. Medium — LIQUID's timing claim changes meaning as PROME records it

**VERIFIED by comparing pre-session gate, owner delivery, and updated gate.**

The pre-session `GATE-LIQ-069.review_by` was **September 15**. LIQUID graded on **September 12**, explicitly preserved the September 15 date, and recommended October 15 to PROME. PROME accepted the successor, but its state cell now says **“GRADED AT review_by 2026-09-12.”** The screenshot repeats the claim that the grade happened at its review date.

The grade was early. Moving the successor was explicitly recorded as PROME's decision; that is separate from the incorrect historical timing statement. Keep observation date, previous review deadline, and successor deadline distinct. This finding does not establish an incorrect market grade.

## What the evidence supports

| Desk / claim | Audit result |
|---|---|
| BRENT graded COT vintage #5 | Owner STATUS and delivery agree with PROME's gate: shorts 107,229, OI 1,939,911, share 5.5275%; recomputed ratio agrees. A SPENT / B NOT-SPENT supports the recorded joint NO-VERDICT under the carried rules. Review deadline advances to September 18. This clears overdue review, not the standing instrument itself. |
| RED delivered three grades and repaired its board-gap check | Registry carries FT-10 at 1-of-4, FT-11 non-fire, and FT-06 not exited. Code replaces latest-date comparison with an ID difference including archived ledgers. Both new test scripts pass. Decimal scaling correctly stops published 9.30 from becoming a strict >930 fire. |
| BROCK and OTTO completed CRMT work | Both substantive grade artifacts exist. BROCK's source memo includes the corrected first extension of four days. OTTO records Letter 2 band 2A and the limitation that filing silence on September 18 is not a usable discriminator. PROME's new L343 carries that caveat. Docket closure remains incomplete as above. |
| LIQUID drained 35 items | Commit contains 35 inbox-to-processed renames and 35 added disposition rows; the five-gate table survives in STATUS. One later BROCK reply remains in its inbox, so the historical 35-item drain is supported, not a claim of a permanently empty inbox. |
| DAEDALUS shipped READS consumer and denominator correction | Implemented and tested, but findings 2–3 prevent treating it as robust completion. L247 F2/F5 delivery is a scoped specification review, not a claim that the whole KERNEL feature was implemented; the docket correctly preserves other open findings. |
| PROME repaired spawn classification on failed Git reads | Nonzero Git status now yields UNKNOWN rather than DARK; unparseable owner `?` is also refused as a candidate. The dedicated 15-check suite passes. Registration-date activity semantics remain unchanged. Acceptance condition 5 asks for failure coverage in `--selftest`, but those cases live only in the separate test file; the built-in selftest still reports 11/11. |
| DAEDALUS built the pipeline guard | Script and 19-case selftest exist; wiring is absent in the root and PROME settings inspected, as the report admits. Additional counterexamples show any occurrence of `pipefail` or `PIPESTATUS` suppresses diagnosis—even `set +o pipefail` or a trailing comment. It is a warning-only prototype, not demonstrated prevention of recurrence. Fix and test those cases before calling it effective. |

Additional state residue: BRENT's fresh COT section coexists with its standing COT ladder at `AGENTS/BRENT/STATUS.md:56`, still stamped vintage #4 and three consecutive NO-VERDICTs. The historical vintage is labeled, but the standing current-state carrier was not refreshed alongside the fresh block.

## Validation and limits

Passed: READ-CAP selftest 44/44; pipeline guard 19/19; claim-check 36/36; consumer-check 10/10; spawn-list built-in 11/11; separate spawn failure suite 15/15; RED board-gap suite 14/14; RED tie-atom suite. The independent fixtures above fail the advertised behavior despite those passing tests. RED's board test uses absolute live paths and expects exactly three ledgers, and its tie test reads the live registry; these are useful checks today but are not fully frozen regression fixtures.

Inspected the shared-script diffs for the session-banner status-code repair, DAEDALUS push verifier, fixture exclusions, weekday false-positive fix, and FIRMS key-presence addition. No production boot, dashboard build, synchronization, hook installation, or market fetch was run. Research verification here means repository evidence, arithmetic, and propagation agreement; external filings, market observations, and broker truth were not independently authenticated. No claim of independently verified P&L or trading outcomes follows.

Priority: repair the invalid ledger; reconcile completed desk work; close the READS false-green paths; then finish the already-carried maintenance. Preserve the useful desk work while repairing its completion and verification mechanisms.
