# ACCEPTANCE — boot gate ACTION OWED class (WQ-467 A, Will 2026-10-21 10:05 ET)

**Written before the code** (WQ-229). This is process change 4 of session af287aee; the ceiling is now five (AUTONOMY change log 2026-10-21).

## Defect, in its own terms
Three gate checks whose rule in `PROME/BOOT.md` REQUIRES an act print as `[advisory]`: fire-time (step 5: "rc=1 always means act"), the exempt-desk BOARD gap (step 6: packet or doorbell the desk), and WILL_QUEUE (step 3b/5: act on DUE TODAY, reconcile PASSED). The gate's footer then says "advisories above are judgment calls". At the 10/21 boot PROME read that label as optional, did none of the three, and reported "Skipped controls: none". Nothing compared that claim with the flags.

## Acceptance conditions (properties)
- **AO1 — label matches the rule:** each of the three checks, when it flags, prints as `[ACTION OWED]`, never `[advisory]`. A passing run of the same check still prints ✅.
- **AO2 — still never blocks:** an ACTION OWED flag alone leaves rc 0 and the verdict PASS. `aggregate_rc` treats it exactly like an advisory. Boot is never stopped by it.
- **AO3 — the footer counts what is owed:** when one or more ACTION OWED lines flagged, the footer names how many need a disposition in this boot's report, and no longer says "judgment calls" about them. With none flagged, the footer is unchanged.
- **AO4 — the header counts the class separately:** the header line reports blocking / action-owed / advisory counts, so the new class is visible at a glance.
- **AO5 — the report must answer it (AMENDED after read 1, C3):** `PROME/BOOT.md` step 8 requires the boot report to list each ACTION OWED line with its disposition. Only **done** (cite the artifact) or **routed to <owner>** (cite the packet) keeps the headline clean. Deferred, partial or no disposition ⇒ SKIPPED + PARTIAL. The gate footer says the same thing (read 2, R2-1). The `/boot` runner (root and local copies, identical) carries the same line.
- **AO6 — no other check changes class:** every other check keeps its severity, and the set of check names printed is unchanged.

## Neighbours (WQ-229, consider)
- **Ordinary:** a clean boot prints the three as ✅ with the unchanged footer.
- **Overlap:** an ACTION OWED flag together with a BLOCKING failure: rc 1, the BLOCKED footer, and the action lines still print.
- **Wrong owner (AMENDED after read 1, C2):** desks do not run `prome_gate.py`. The ACTION class applies at boot and refresh only (`GATE_MODE`). At closeout, WILL_QUEUE stays advisory, because CLOSEOUT has no ACTION OWED rule. Fire-time and the BOARD gap are boot-only.
- **Missing information:** unchanged behaviour. A check script that crashes is recorded under its own class with the exception text, plus the DID NOT RUN marker when the script prints it (`run_script`, pre-existing). So a crashed ACTION OWED check prints as ACTION OWED carrying the failure detail, not as a clean ✅. A gate-level abort stays ERROR (rc 2).
- **Concurrent activity:** N/A. This is a pure labelling and printing change, with no file writes added.

## Tests
`PROME/tools/tests/test_gate_action_owed_WQ467.py`, plus the existing gate suites (`test_gate_isolation_L294_F7.py`, which counts printed check lines, is updated to count the new label).

## Reads
- **reads: 1.** Independent read 1, 2026-10-21 ~10:13 ET (general-purpose, Opus, own counterexamples, fixture runs of the working-tree gate): **HOLD, 4 ❌ · 6 ⚠️.**
  - **Author claims checked:** the 4 `test_gate_isolation_L294_F7` failures are VERIFIED pre-existing (the fixture runs `git archive HEAD`). PROME's claim that "test_gate_orch_summary needs pytest" was **REFUTED**: `.venv/bin/python -m pytest` gives 8 passed, 1 skipped.
  - **Fixed after the read:**
    - **C1:** a missing WILL_QUEUE.md now records under the action class.
    - **C2:** ACTION applies at boot/refresh only (`GATE_MODE`); at closeout WILL_QUEUE stays advisory, because CLOSEOUT has no ACTION OWED rule.
    - **C3:** step 8 now says only *done* (cite the artifact) or *routed to <owner>* (cite the packet) leaves the headline clean; deferred, missing or partial ⇒ SKIPPED and PARTIAL, aligned with `PROME/CLAUDE.md` § Skipped-control reporting.
    - **W1:** blocked and incomplete footers now also print the owed count.
    - **W2:** a passing action-class check prints `[action]`, and the header counts only flagged lines ("N action owed").
    - **W3/W4:** step 8 no longer names the three checks or claims rules "above"; the gate prints the class.
    - **W5:** the `exempt_gap.py` docstring is updated.
    - 3 tests added (11 total).
  - **State:** IMPLEMENTED · TESTED. The post-read fixes are unverified until read 2.

## Declared residue (WQ-178, 2026-10-21)
- **C4 (❌ in read 1 — CARRIED under § Review budget's disposition: closeout report + DOCKET row, not WQ-178 residue):** one disposition covers a whole ACTION OWED line. Fire-time keeps owner-routed flags on the list ("persist") and does not separate new flags from old, so "routed" can stay true at every boot while a NEW DATE flag sits among 47 old ones. A real fix diffs the fire-time log against the previous boot's run and requires a disposition per NEW flag. That is a fire-time tool change, its own episode, candidate for the 10/25 L600 review. **Mitigation now (restated after read 2, R2-5):** the wording only. C3 makes a whole-line "routed" untrue when any flag in it was not routed, but checking that needs the per-flag comparison C4 says does not exist. Applied honestly, it puts PARTIAL on most boots while the fire-time list carries 47+ persisting flags. A standing PARTIAL stops carrying information, the way "[advisory]" did. That is why the fire-time new-vs-persisting split (DOCKET row registered 2026-10-21) is the real fix.
- **W6:** the `[ACTION OWED]` label is 3 characters wider than the padded column; no positional parser was found. `hooks/forge_validate.py` keeps only BLOCK/ADVISE rows and today runs no ACTION check; if one is ever added there, it must be taught the class.
- **Additional pre-existing failure (not this change):** `test_review_mechanism_WQ240b` 1 failure / 1 error on closeout SKILL text.
- **Read 2 (2026-10-21 ~10:18 ET, Opus): HOLD, 1 ❌ · 5 ⚠️.** **R2-1 ❌ FIXED:** the gate's PASS footer still offered "deferred + reason"; it now carries step 8's wording, and a test asserts "deferred" appears only as a route to PARTIAL. Per the reader, this copies existing wording and changes no rule's meaning, so no third read. **R2-2 FIXED:** the isolation test now counts `[action  ]`. **R2-4 FIXED:** AO5 and the wrong-owner bullet amended in place. **R2-5:** the mitigation is restated above and a DOCKET row is registered. **R2-3 (residue):** the header counts only owed action rows, so its totals do not sum to the printed lines when an action-class check passes. **R2-6 (residue):** label-column width, as W6.
- **reads: 2 of 3. Episode closed.** Final state: IMPLEMENTED · TESTED. The R2-1 fix is post-read and is not independently verified.
