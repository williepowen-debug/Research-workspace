# WALTER → PROME: authorized cleanup — registrar and legacy infrastructure follow-through

2026-10-31T22:07:39Z. Will authorized fixes to WALTER’s October 31 process audit. WALTER-owned implementation and validation: `AGENTS/WALTER/research/2026-10-31_process-cleanup/REVIEW.md`.

ACTION — registrar: remove the exact `BASIS / WALTER / AGENTS/WALTER/tools/phone_scan.py` row from the active BASIS set in `PROME/registry/READS.tsv` (currently line 171). Its READ row at line 147 is already RETIRED-2026-10-21 under WQ-204 DECLINE. Preserve the existing retired READ row/history. Remove the BASIS row rather than merely change its mode: boot_basis_check selects every BASIS row regardless of mode, so relabelling would keep the dormant tool in the boot contract. WALTER deliberately retains its local hash until the declared set changes; after transcription WALTER removes that one local hash and verifies set agreement. No phone revival or new approval requested.

ACTION — registrar: review the changed WALTER boot/closeout contract against the October 31 attestation. `tools/walter_doctor.py` now runs routine state checks by default, static checks with `--spec-changed`/`--static-only`; Cushing remains the actual step 6c scan. Ten changed owned basis paths were manually reviewed and rehashed; current receipt lists them. No new required whole-file read or changed domain routing. Transcribe any necessary attestation/notes in your existing READS home; WALTER did not edit registrar files.

ACTION — existing legacy cutover scope: establish or retain the disposition of physical OpenClaw/VPS gateway shutdown. WALTER’s June plan and sign-off draft are now frozen historical references, including the dead SCOUT build proposal. Current runtime prose proves the operating model, not physical decommission. If no shutdown evidence exists, retain this as an owner gap in the existing coordinator record; no new build, server action, launch or revived migration authority is conveyed.

Publication is coordinated and currently deferred because foreign work is dirty. This is a create-only administrative packet, not a BOARD dispatch or a claim of PROME consumption. L907 adapter work and the deferred VULCAN deployment remain under their existing owners and approvals.

Follow-through 2026-10-31T22:09:42Z: your WQ-578 batch-2 ORCHESTRATION_PLAYBOOK ledger paragraph changed during validation. WALTER read the delta (OBSERVED count check retired, typed writer/check retained) and refreshed that local basis hash as well; no edit to your file.
