# Decisions WQ-579 import isolation repair

Candidate `bbf1347706ced19ec7b9542fb0bf60e8a570df80`; tree `97ca4ccd98f3e4c82db8b88067a960712cf91760`; prior reviewed candidate `1296e8bcb5ab3c8ea3e1c3750de05fa2f417b556`; cumulative base `3a9e489ba2acd3aa4e448f6c497caa14bca4ae82`. Frozen author repair, not installed or independently accepted. Live Decisions and acceptance are unchanged.

Will approved WQ-579 in PROME chat (October 31, 2026, 16:41 ET: “yes to both go ahead”) and directed CATO: “okay go ahead and do your repair”. Authority: `AGENTS/CATO/inbox/2026-10-31_from-PROME_WQ579-go-fix-round.md`. PROME owns ONE further focused recheck, then installation with matching acceptance on no blocker, without another ask. Chat confirmation remains required for every answer.

Verify artifact SHA-256s in manifest.json. Import candidate.bundle into an isolated clone containing the cumulative base; verify commit/tree. focused.patch is only the delta from 1296e8bcb; candidate.patch is cumulative. Both patches reconstruct the exact candidate tree in separate temporary indexes. Unlike the previous package, this package intentionally includes **scripts/githooks/pre-commit**. Do not replace the live checkout with the stale clone or install the hook separately from accepted app bytes and matching acceptance. No artifact applies itself.

## Repair and focused closure

- X-1: materialize exact pinned transport files; isolated Python imports and protected stdin-hook environment; refuse private replacement refs/tags and unexpected materialized scripts. All Repo Git reads disable replacement objects. Safe-push inherits the transient Git override `push.followTags=false`; the fleet script is unchanged. Existing remote tags are preserved.
- X-1 publication evidence: verify exact parent, one child commit, exactly the selected two paths and bytes from the shared repository after fetch. One captured ls-remote inventory per observation requires only master to move to that commit. Extra branch/tag/commit publication cannot receive an exact-success receipt.
- X-2: weekday advisory uses python3 -I; shared HEAD/index and publication base are captured before advisories. Movement refuses without undoing owner work. Real planted hashlib/argparse modules have positive controls and origin-only coverage in versioned test_import_isolation.py.
- Shared hook: both remaining Python calls use -I. The dormant row-cap block is removed under WQ-578 in this same candidate; line stability and account guards remain.
- W-R: receipt names previously committed riders. W-S remains: superseded half-published answers can still need manual clarification. Prior W-H–W-Q and other residue remain in release-review.json.

Author evidence: **135 Python tests PASS**, **38 native browser assertions PASS**, 22 build pins matched. Eleven new tests cover imports/environment, advisory HEAD/index races, replacement-object deception, tag following, extra branch/commit publication and shared post-fetch verification/rider wording. Original race/third-path witnesses were adapted for -I/sparse paths without weakening their assertions; initial failures and final results are in author-checks.txt. No real answer or receipt was written. Prior reviewer raw harness was not preserved; new author witnesses are versioned in this bundle.

## Return and limits

PROME should recheck X-1/X-2 and the approved hook change, retain the previously held properties, then reconcile W-L pending delivered answers and W-P old staged/committed exports before coordinated installation/acceptance. Never manually sweep reply exports. Full acceptance template and named residue are in candidate release-review.json. No second reviewer launched by CATO.

Concurrent legitimate remote updates can cause a reconciliation result even after the pair was delivered; no automatic ref rollback. Remote checks are bounded observations, not a transaction against subsequent writers or a sandbox against arbitrary same-user code/global Git configuration. Existing final check-to-push and owner-intake race limits survive. Actual cross-device restore and ordinary productivity remain unmeasured. This package is the author handoff; independent closure and live installation are PROME's remaining actions.
