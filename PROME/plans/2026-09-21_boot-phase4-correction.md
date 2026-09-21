# Phase 4 — changed-policy recovery and spawn wording

Authorization: Will, “Okay go ahead,” after CATO's review at `2fef9aa05` and PROME's recommendation to correct both advisories, then observe ordinary use. No new boot framework or live boot in this maintenance batch.

## Proposed change and acceptance — before editing

Extend the existing receipt schema to retain per-file policy hashes and a pending-policy-read list. On policy change in the same repository/context, accumulate changed paths in the pending list, discard prior page/acknowledgement receipts, and report the remaining paths in every stateful read/ack response. A date change resets page receipts but must not erase pending policy reads. A second policy change accumulates unresolved paths, including a change back to prior content. Reuse of either USER or BOOT is denied until the pending set is empty, even if USER itself was reread and acknowledged.

Use the existing bounded full-read, contiguous EOF and explicit --ack-read protocol to clear each pending path. Policy-basis paths may record full reads and acknowledgements for this purpose; only USER/BOOT may ever return REUSED_IN_CONTEXT. All other files/views always emit full text, even after recovery. No new commands or lock mechanism. Missing policy inputs, contention, failed saves and source/policy races cannot authorize reuse on that call. **Final storage-failure boundary:** only successfully checkpointed debt is durable; a failed recovery checkpoint requires abandoning reuse for that retained context and plain full reads, caller-enforced across process restarts. This supersedes the original unqualified cross-call persistence acceptance; see closeout audit below. Old v1 or corrupt same-context receipts have no reliable per-file basis: require full policy-basis recovery, never silently promote them. A genuine new context/repository starts fresh; context identity and initial instruction loading remain caller responsibilities, not authentication. Deleting/changing state is not a supported recovery procedure.

Acceptance neighbours:
- Ordinary: unchanged acknowledged USER/BOOT reuse still works; changed CLAUDE is named, delivered by bounded reads and acknowledged before either can reuse.
- Overlap: USER re-ack cannot clear CLAUDE; two changes accumulate; date advance cannot drop pending; a changed-back path is still pending; other basis files never become reusable.
- Wrong owner: repository/context mismatch cannot carry old acknowledgements; outside/symlinked paths cannot clear a pending instruction.
- Missing information: legacy/corrupt receipts conservatively require basis recovery; missing basis/source cannot clear pending; partial or skipped pages and absent/wrong digest cannot acknowledge.
- Concurrent activity: existing lock/save/race rules remain; policy mutation during recovery or failed acknowledgement write leaves recovery unsatisfied.

## Exact BOOT replacement

Replace the Repeat boot paragraph with:

> **Repeat boot:** only `USER.md` and this manual may reuse acknowledged full reads in retained context. Add `--read-state /tmp/prome-reads-ID.json --context-id ID` to `boot_read.py` reads/continuations; after contiguous EOF use `--ack-read --sha256 <sha256>`, later `--reuse`. New session, compaction, handoff or uncertain retention requires a new ID and full reads. Policy changes report `pending_policy_reads`: fully read and acknowledge each listed path with the same state/context before reuse; USER acknowledgement alone cannot clear other paths. Never reset state/ID to bypass recovery. Other mismatches and files require full reads. Reuse never covers live state, checks, private rulings or capability/preflight. Repeat via `boot_session.py --run-dir <original-run-dir> --refresh`: a completed original permits fresh checks without BOARD advancement; an incomplete original stays UNKNOWN, never bypassed with a new directory. Refresh grants no additional per-boot spawn allowance. Repeat all manual steps; missing tools remain PARTIAL.

Stamp the BOOT amendment with this record; keep existing skill indices (already point to the amended paragraph). Update terse HANDOFF/SCRATCH continuity and append disposition to the original Phase 4 record. Keep startup budgets, generated blocks, owner state, old READS attestation and ARGUS baseline unchanged. Measure BOOT with the approved instrument; avoid a new rotation finding by tightening the existing repeat/header wording if necessary without dropping controls.

## Validation and completion

Run the original 98-test selection plus regression cases under strict ResourceWarning; only disposable fixtures. One independent plan review before implementation and one result review with an independent counterexample, per PROME/CLAUDE. Fix blockers only, declare new advisories. No production boot, refresh, raw gate, market or private-ruling checks.

IMPLEMENTED: schema v2 policy hashes, persistent pending reads, path-specific bounded recovery and explicit unchanged spawn allowance. TESTED: all 108 tests pass under strict ResourceWarning (original 98 plus ten recovery regressions, including the result reader’s error/reversion counterexamples); protected-file hashes, skill parity and SCRATCH caution/generated section preserved. Read-cap rc=0, with only the pre-existing HEARTBEAT rotation finding. INDEPENDENTLY VERIFIED: plan accepted; result reader reproduced the initial 31 repeat tests, accepted ordinary recovery/reuse boundaries and spawn wording, and found one error-path persistence blocker with two independent counterexamples. The single blocker correction is owner-tested below; no separate independent acceptance of that final correction is claimed. STILL UNRESOLVED: old manifest attestation, unavailable private/native tools, caller-asserted retention and unmeasured practical savings. Observe ordinary-use reading saved, elapsed time, recovery frequency and missed obligations before any expansion; no measurement framework added.

Plan authored at 2026-09-21T19:16:46-04:00 (observed clock).

## Plan review

`phase4_plan_review` found no blockers or advisories; read-only closeout acknowledged, no edits/commits/fixtures/live checks. Repeat/header wording was tightened before transplant to remain below BOOT’s rotation trigger without dropping recovery or spawn controls.

## Result review and blocker correction

`phase4_result_review` found one blocker, no additional advisories: newly detected pending changes were saved only after successful page/ACK work. Its independent counterexamples showed (1) rejected USER acknowledgement followed by CLAUDE reversion, and (2) an AGENTS change during CLAUDE acknowledgement followed by AGENTS reversion, could lose observed recovery debt. Both bypasses are now permanent regression cases.

The single correction pass persists newly detected policy debt before fallible page/ACK operations and preserves changes detected by the final race check, including when page production raises. Receipt history is cleared on those changes; a checkpoint write failure refuses the call. All 108 tests pass after that change. That pass changed no rule meaning. The later Will-requested closeout audit found a separate storage-failure boundary, dispositioned below. Both helpers explicitly acknowledged read-only closeout without repository edits/commits or live checks; receipts are in ORCH_LOG.

Table and whitespace checks pass; both unchanged skill indices point to the amended Repeat boot paragraph. The declared read-cap check passes without a new rotation finding; the separate manifest checker remains rc=2/UNKNOWN on its old attestation. Protected owner files, original boot/refresh machinery, BOARD cursor, ARGUS baseline and generated continuity sections remain unchanged. No live boot or full session closeout is claimed.

Context identity/retention and first-context instruction loading remain caller assertions. Recovery depends on the outside-repository state remaining available and writable; do not replace it or change IDs to bypass pending reads. No practical savings are yet established; ordinary use is the next evidence, not further expansion.

Completion recorded at 2026-09-21T19:24:59-04:00 (observed clock).

## Closeout audit — storage-failure boundary

The fresh-context closeout reader independently reproduced all 108 tests and found one further blocker in the unqualified persistence claim: if the FIRST recovery checkpoint fails, no durable debt was stored. After CLAUDE reverts, the old receipt can still mechanically reuse. The earlier write-failure test covered already-persisted debt, not this case. This remains a mechanism limitation; it is not claimed fixed by a second persistence system.

The checkpoint error now names all policy inputs and directs the caller to abandon reuse for that retained context, use plain full reads, and never retry old receipts/reset IDs. BOOT explicitly makes this a caller obligation across restarts. This supersedes any unqualified observed-change persistence guarantee above. Initial context loading, truthful context identity and surviving receipt storage remain assumptions. No performance improvement is established.

Exact final Repeat boot paragraph:

> **Repeat boot:** reuse only acknowledged full `USER.md`/`BOOT.md` reads in retained context. Add `--read-state /tmp/prome-reads-ID.json --context-id ID` to `boot_read.py` reads/continuations; after contiguous EOF use `--ack-read --sha256 <sha256>`, later `--reuse`. New sessions, compaction, handoff or uncertain retention require a new ID and full reads. Read and acknowledge every `pending_policy_reads` path using that state/context before reuse; USER acknowledgement clears no other path. Never reset state/ID to bypass recovery. A failed recovery checkpoint requires abandoning reuse for this context and plain full reads; this is caller-enforced across restarts. Other mismatches/files require full reads. Live state, checks, private rulings and capability/preflight stay fresh. Repeat via `boot_session.py --run-dir <original-run-dir> --refresh`: completed original required, no BOARD advancement; incomplete original stays UNKNOWN, never bypassed with a new directory. Refresh grants no additional per-boot spawn allowance. Repeat manual steps; missing tools remain PARTIAL.

Amendment recorded at 2026-09-21T19:32:19-04:00 (observed clock); changed rule/error wording requires closeout delta review.
