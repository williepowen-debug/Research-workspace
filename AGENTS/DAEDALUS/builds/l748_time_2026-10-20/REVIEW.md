# Independent review — /root/time_review — October20

Proposal counterexample: append a November invalidation for an October touch, rotate October, then November. A hot-only reader loses target and debt. Remedy adopted: pin both sides against rotation. Other proposal findings adopted: exclude correction from TOUCH metrics (CLOSE summary), pin provenance/byte equality and disclaim append-time proof, validate target under append lock.

First code read counterexample: malformed correction carrying valid trailing closeout_v1 could retain ALREADY_CLOSED and disappear in historical filtering. Other findings: empty/no-header audit could return green; rotation only checked syntax/target length rather than complete correction contract. All three fixed, runtime changes delta-reviewed.

Final reader text (verbatim):

> Counterexample rechecked: malformed mixed-marker correction cannot close or hide itself, malformed correction blocks unrelated rotation, and audit explicitly rejects a zero-row structured population.
>
> **Disposition: APPLIED 3 · RESIDUE 0 for implementation findings.** Independently reran **13 tests; all passed**.
>
> Reviewed the updated `orch_time.py` and `orch_closeout.py` changes against the earlier writer/consumer scope. Approval remains bounded to this repair and standalone audit; it does not establish production installation, timestamp authenticity, or recipient consumption.
>
> The committed-empty test strengthening remains test-only POST-REVIEW work; its current fixture reaches the missing-Git branch. I did not rerun the four frozen production examples. No repository edits or commits.

Author disposition of caveat: after that reviewed test snapshot, strengthened test commits a seed and each empty/bad/header-only ledger; all13 rerun pass. This is POST-REVIEW test-only, not silently folded into reviewed tests. Four real examples are author-verified only. Runtime code unchanged after the final read. Hashes independently supplied by reader:
- orch_time.py 891ac86886a83d2785b0f195bf7976db3b2ee25dc4e8ddf32ed1b4d1cfb727ce
- orch_log.py 16efc7f002f619b96a9619fd84dfd6e1979e5d0663bacb55b066f5dfef7f35dd
- orch_closeout.py c005cdbee0ab693ae024ca87f241c6a83ff0ef1fa231d7188ade273c6e1f9cd0

Scope limits: read-only helper, Codex/OpenAI, exact model UNKNOWN; no PROME identity or live fleet coverage. Root/local instructions verified by reader. count_reads.py/L470 extraction was not reviewed. No production apply, all-fleet completeness or maintenance completion clearance.

Final test-only delta and closeout response (verbatim):

> Test-only delta reviewed and independently passed: seed commit plus all three committed empty/bad/header-only states now exercise the intended refusal paths.
> Review complete; no work remains running. No repository edits or commits. Runtime-code disposition remains APPLIED 3 · RESIDUE 0 at the recorded hashes.

Thus the test-only caveat above is resolved by a separate final read; no runtime-code change followed review.
