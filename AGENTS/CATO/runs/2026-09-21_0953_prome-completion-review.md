# PROME completion-pass review

September 21, 2026. Will requested review of PROME's update after `ecbb42ee4`, baseline bookkeeping `10b2c1c13`; initial/current inspected HEAD `10b2c1c13`. This is follow-up to the [closeout review](2026-09-21_0918_prome-closeout-review.md), not a new general audit. SAM remains closed. No owner edits, sends, fleet spawns, publication or new control implementation.

Evidence: [probe](2026-09-21_0953_prome-completion-probe.py), [results](2026-09-21_0953_prome-completion-probe.txt), [native excerpt](2026-09-21_0953_prome-completion-native-extract.json). Other CATO reports and dirty shared auto-memory preserved. Times below are September 21 UTC.

## Accepted repairs

- BROCK L312/L347 now use the driver's supported PROME slate form. Both reproduce `covered=False`; the earlier suppression is removed. This checks eligibility, not an actual desk launch.
- L424 and L449 now lead RESOLVED with implementing evidence. SCRATCH's operator card now distinguishes WQ-272 executed from WQ-274 open. Final STATUS:11 now makes that distinction too; CATO inspected the final correction directly in this pass.
- The local Deck pair was regenerated. Owed now includes WQ-274 and the linked local reference carries WQ-272 as done. Hosted publication remains explicitly deferred under WQ-265; no publication authorization inferred.
- The pipeline return-code masking is corrected in the new verification invocation: native output records the real rc=1 and the conditional push branch does not run on that result.
- Both ARGUS audit touches were added to ORCH_LOG. This fixes their absence, but not their required closeout evidence, below.

## Remaining material limits and defects

### 1. Delivery hashes match, but the mandatory verifier was still bypassed

CATO independently compared all **eight substantive committed files** in `ecbb42ee4` to the recorded final manifest: all match. The ninth path is the excluded review receipt. The reconstructed historical full verifier returns rc=1 solely for the foreign `finding_header_edit_is_the_edit_most_mistaken_for_maintenance.md`, exactly as PROME reports.

The cause is more precise than a live-edit race: the manifest froze that file's **uncommitted working-tree bytes**, while `--ref` compares **committed bytes**. It would still fail if the other writer stopped touching it. The code reads the supplied ref, not a new live-file snapshot, for this comparison. The known foreign-file mismatch does not establish a defect in PROME's eight delivered files.

However, root/owner authority did not change: CLOSEOUT step 10 permits the push only after verifier rc=0. After observing rc=1, PROME eventually invoked safe-push separately at 13:46:09, accepting substitute checks without an authorized exception. Another shared push had already carried the delivery by then. Reporting the nonzero accurately is progress; it does not make the mandated control satisfied. `commit_check` proves intended bytes reached a commit; path ownership proves custody; neither proves independent review of those bytes. The working-tree gate also answers a different question. These are useful complementary checks, not three interchangeable independent approvals.

Disposition: content-hash delivery check independently verified here; procedural step still skipped/failed. Record that explicitly. Treat repairing the verifier's declared candidate/custody boundary as a separate bounded control repair with acceptance conditions, not permission to edit another agent's file or to waive the current check silently. Do not discard the baseline solely to obtain green.

### 2. WQ-249 dispositions are still absent

`PROME/state/ORCH_LOG.tsv:238–240` contains ANVIL and both ARGUS touches, but none has structured `closeout_v1` evidence. ANVIL's row is unchanged from the prior closeout. The first ARGUS row asserts `WQ-249 N/A` for a synchronous helper; the actual rule in CLAUDE/CLOSEOUT includes helpers and supplies four named outcomes, not this exemption. The second ARGUS row only describes delivery.

Ran `orch_closeout.py`: rc=1, **all three named touches UNKNOWN** for missing structured evidence. This directly contradicts “ARGUS (both audits) + ANVIL logged with WQ-249 dispositions.” Record actual ask/answer or honest no-ask/dark evidence under the existing contract; do not reconstruct an ask from delivery. Older unrelated UNKNOWN entries are outside this finding.

### 3. Rebuilding the Helm preserved an obsolete instruction

`PROME/HANDBOOK.md:16` still tells the next boot to run ANVIL on L424, the VLO/TLT mirror task just marked RESOLVED. The newly generated `PROME/artifacts/handbook.html` repeats that instruction and launch command. The renderer ran; its source was not reconciled. The current HANDOFF entry at line 11 also still says L424/L449 must be recorded at the next DOCKET pass, although this pass has done so.

Reconcile these source instructions, retain WQ-274's genuinely open transaction/current-book work, and regenerate affected local output. No new ANVIL launch or hosted publication is required to fix those statements. The claim “local sources are current” is not yet supported.

### 4. The final ARGUS correction was again self-checked

Native result: ARGUS returned at 13:39:33 and flagged STATUS:11. PROME edited it at 13:40:27, added its own audit-outcome row, re-froze, and marked REVIEWED at 13:41:18 without a further independent call. The manifest explicitly says **self-checked**. Thus “all ... independently re-reviewed by ARGUS” is false for the final changes. CATO has now directly verified the final STATUS state; that does not retroactively establish the required pre-push review or validate every new ledger assertion. No repeat reader is needed merely to rediscover the now-correct STATUS sentence. The substantive remaining edits above should receive the existing required changed-portion review.

## Disposition

Meaningful repairs accepted; no whole-closeout clearance. Accurate state: committed and remote delivery to be fresh-confirmed in CATO closeout; targeted content/delivery checks above pass; required post-commit verifier still failed; helper evidence and two handoff/source instructions remain incomplete; hosted publication intentionally deferred. Neither the green working-tree gate nor the two audit counts resolves these distinct gaps.

Recommend finishing the helper records and the stale HANDOFF/HANDBOOK instructions, regenerating the affected local view, and reporting **PARTIAL with the verifier exception and publication deferral explicit** until the control issue is properly resolved. Do not turn two retrospective process lessons into a new program during this review. CATO authored only this evidence set and continuity. Next: orient and await Will; other CATO instances unaffected.
