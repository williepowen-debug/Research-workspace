# Boot maintenance — authorized steps 1 and 2

Scope: Will's explicit October 4 instruction; CATO findings B8–B10 in `AGENTS/CATO/runs/2026-09-21_1619_prome-boot-proposal-review.md` (5fcadc777). New maintenance episode; diagnostic reviews of the September proposal are provenance, not acceptance of this implementation. No step 3, changed historical-read scope, fleet manifest recertification, capability workaround or extra acceptance boot. Authority and budgets do not change.

## Acceptance conditions (written before implementation)

1. Factor only consecutive repetitions of the exact known gap reason under the exact producer header. Full agent labels (spaces, roles, Unicode and delimiter-like text), complete date/touch/key identities, order and multiplicity survive. Other failures and malformed rows remain verbatim, including separators/singletons. Producer output is a test fixture, not a live-log assumption.
2. Paging preserves the complete representation, bounded serialized UTF-8 text and continuation integrity. Source, view or renderer revision changes refuse old offsets. Original logs are untouched; fallback and unreadability behavior stays conservative.
3. Explicit charter mode adds root and local charters to assessed whole reads once each, preserving manifest defects and unknowns. Missing/unreadable charter evidence cannot yield green. Injection mode is caller-declared, not inferred; unspecified standalone coverage discloses its exclusion assumption. PROME gate and runner default explicit, forward the mode, and save it in receipts. Retry returns original coverage without re-running; refresh separately records its mode. Other desks' default grade and existing output counts remain compatible.
4. CLAUDE, BOOT and SCRATCH cleanup preserves operative rules, named current obligations and unresolved conditions; exact originals live in linked archives with measure.py CRC receipts. Rotated files finish below the existing 70% stop. Charter's under-20,000-B target measures the consolidation pass and licenses nothing; this bounded rotation reaches the existing rotation stop but does not meet that separate target. Generated SCRATCH blocks stay unchanged except later authorized generation. Boot still requires all historical orchestration output; no new historical-summary contract. Native Artifact and fleet capability limitations remain disclosed.
5. Preserve foreign dirty files and commit only this task's paths. Standard checks and scoped Git delivery; no extra live boot. Practical benefit stays UNVERIFIED pending next ordinary cold boot.

## Neighbours

- Ordinary: exact producer rows; explicit and confirmed-injected runtimes; ordinary whole reads.
- Overlap: a charter already in the manifest counts once; repeated identical keys stay repeated; gap and unfamiliar failure interleave without swallowing a boundary.
- Wrong owner: identity is preserved, never reattributed; shared checker defaults for other desks unchanged. No owner files edited.
- Missing information: empty/malformed labels, unknown formats, absent/unreadable charters, unattested manifest, old receipts without a mode → no invented evidence.
- Concurrent activity: source/digest changes refuse continuation; document source hashes checked before apply; protected foreign dirty files hashed, never staged or replaced. No live boot / cursor advancement for acceptance.

## Proposed implementation and evidence

Plan candidate: `/tmp/prome-maintenance-20261004/draft/{CLAUDE,BOOT,SCRATCH}.md`, originals in adjacent `before/`. Apply only after plan disposition. Archives will be `PROME/archive/BOOT_MAINTENANCE_2026-10-04/` with exact original filenames; pointers retain original headings. Measure via `PROME/tools/measure.py`. Historical snapshot evidence is on-demand; no live obligation is satisfied by archival.

Tool changes: broaden only GAP_ROW's label slot to a nonempty single-line label anchored by the final touch/key/reason suffix; version compact continuation digest. Add `--charter-mode explicit|injected|unspecified` to existing read-cap agent check (default unspecified, no fleet inference); explicit mode checks root/local charters, no default fleet changes. PROME runner/gate accept explicit|injected (default explicit); response and saved receipt disclose mode. Existing seven-read manifest remains attested as declared; runtime overlay is reported separately, no implied re-attestation.

## Review ledger

reads: 3
- 2026-10-05 plan review: maintenance_plan_review, one blocker in acceptance wording (under-20,000-B target mislabeled aspirational), corrected before implementation. No authority/preservation blocker in drafts. Advisories: header emphasis typo (one-word/format correction), October4 snapshot date precedes October5 apply, little SCRATCH headroom (remeasure after generation).
- 2026-10-05 result read2: maintenance_result_review; two independently reproduced blockers (charter alias double-count and COVERED wake suppression), fixed for bounded read3; three advisory residues. Blind anchor recovery, payload CRCs, matcher counterexamples and disposable CLI execution passed. Full record: `PROME/reports/2026-10-05_boot-maintenance/result-review.md`.

## Delivery states

IMPLEMENTED: matcher, runtime coverage and document rotation applied. TESTED: focused tests and offline replay below. INDEPENDENTLY VERIFIED: read2 passed preservation/replay/anchors; final corrected-candidate verdict is recorded in `PROME/state/argus_review.json`, not inferred from author tests. STILL UNRESOLVED: runtime coordination/publication access; practical cold-boot benefit; historical closeout gaps. Prior unrelated debt remains at its existing owners/rows.

## Author validation before result review

Evidence: `PROME/reports/2026-10-05_boot-maintenance/`.

- `python3 -B -W error::ResourceWarning -m unittest discover -s PROME/tools/tests -p 'test_boot*.py'`: 46 tests pass.
- `... discover -s PROME/tools/tests -p 'test_repeat_boot.py'`: 33 tests pass.
- `... discover -s PROME/tests -p 'test_boot_hardening.py'`: 11 tests pass. One old expectation still said “Source changed”; updated it to the existing “Source or view changed” error while retaining the changed-source refusal assertion.
- `python3 scripts/read_cap_check.py --selftest`: 112/112 legs pass. `measure.py --selftest` passes. No extra boot was launched.
- CATO's frozen `orchestration-original.txt`: all 478 known gaps match; compact pages 14 (prior CATO result) → 12. Expansion reconstructs the original exactly, including order/multiplicity and every unfamiliar line. New representation 66,013 B versus original 93,391 B (measure.py receipts in replay.json); this is saved-case evidence, not a live cold-boot timing claim.
- Explicit read-cap mode assesses nine reads including both charters; injected mode assesses the seven declared reads. Both rc0 with zero over-budget, rotation-due or manifest-defect counts. Static READS attestation remains unchanged; this does not recertify the fleet.
- Full original payloads in archive markers round-trip byte-identically and match their CRC headers. Regenerated SCRATCH blocks are generator output. Final sizes must be remeasured after generation; charter under20k target remains unmet.
- User-authorized shared read-cap edit now has an exact SHARED row in AUDIT_PERIMETER, so delivery verification covers it; no broad scripts ownership grant. Root charter unchanged. Foreign baseline and WALTER file hashes preserved.

## Normal closeout and unresolved conditions

GATES/WILL_QUEUE/ACTIVE_DECISIONS/STATUS/HEARTBEAT: no task-driven decision, gate, regime or owner-grade change. Consumer numeric/threshold scan, ledger nudge and auto-memory index mutation are not triggered. Root orphan/weekday checks ran; orphan's filename-based “not yours” labels for this authored daily note and the explicitly authorized shared script are resolved by authorship/authorization, not swept. WQ ledger sync records the earlier committed WQ-369 ruling; it grants no C8/unattended execution. HANDOFF and daily memory point here.

The October5 closeout check exposed four due, undispositioned rows (L527/L557/L589/L590). Routing notes retain their named owners, PROME follow-up, PENDING state and original deadline, explicitly disclaiming delivery, grade or liveness. No desk was launched or messaged. Native fleet preflight/messaging and private Artifact ruling/store/publication controls remain UNAVAILABLE. Historical orchestration inventory stays UNKNOWN; no receipts manufactured for old gaps. Local dashboard/Helm/Deck renders run; hosted reads/listing/publication SKIPPED for absent native Artifact tools, so overall closeout remains PARTIAL. Local Deck links are local only; publication needs paired native URLs and the existing prerequisites.

Preexisting dirty `PROME/state/argus_baseline.json` is preserved: post-commit baseline replacement is SKIPPED to avoid overwriting concurrent work. Practical benefit/ordinary procedure execution remains UNVERIFIED until the next ordinary cold boot (no special acceptance boot). Charter under20k consolidation target and other owners' debt remain outstanding; no standing rule was relaxed.

Declared residue (2026-10-05): low headroom on rotated documents may require future normal rotation; no larger reading-contract redesign undertaken. Historic context-injection cost remains unmeasured by the read cap. Result review and final delivery receipt follow.

## Result-read disposition and delivery boundary

Both read2 blockers repaired: explicit overlay merges lexical charter aliases; regression covers whole/scoped `./` and `../` overlaps. DOCKET L527/L557/L589/L590 use the existing `COVERED: PROME SLATED` exception and return false from spawn_list.covered(); they stay due/PENDING and eligible, never completed or claimed awake. The result reader's historical-banner advisory was treated as consequential stale instruction: it otherwise directs a repeat rotation under a new stamp. Date-qualified the prior closeout and pointed its size assertion to this maintenance record, preserving all unresolved carries and archived original text. No new authority or rule.

Read3 is reserved for these changed portions and the required post-fix disposable procedure execution; no further broad audit. All final source receipts/ARGUS run-log must be included before that review. Its final verdict is in the normal review receipt. Existing firetime owner-pointer/date and multipath flags remain at SCRATCH owner-lane carries/L593; no fire-time artifact logic changed in this maintenance.

- 2026-10-05 read3: bounded changed-portion and post-fix disposable procedure execution requested from the result reader; this is the final allocated read. Final verdict/closeout receipt is owned by `PROME/state/argus_review.json`. No fourth read or extra live boot authorized.
