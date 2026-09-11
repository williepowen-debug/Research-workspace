# PROME recent-work audit — September 11, 2026

**Assessment:** useful coordination work, but the new audit and decision-history tools have four reproducible defects. Repair these before treating their green checks as assurance. The sampled owner-to-coordinator research updates agreed; this review did not independently establish the external market facts.

**Scope:** committed work after `6f342d55ba9cfec4f93cb8c158078d7df50cb028`, through `9c7ebc145127a0b61a537798c7b8925f3166b3fd` (September 11, 17:59:25 ET). The first PROME-prefixed commit in this range is September 10, 11:20:10 ET: approximately 31 hours. Inventoried 150 PROME-prefixed commits touching 226 distinct paths, with additional inspection of PROME-owned FORGE work. Inventory is not a claim that every changed assertion received a full audit. Deep review concentrated on the Decision Deck, WQ ledger, exempt-desk BOARD check, ARGUS, spawn-driver changes, Git-wrapper repair, and selected decision-state updates.

The checkout was active and contained other agents' changes. Review used a fixed commit boundary; experiments used temporary repositories and fixtures. No operational files were changed, no pulls or commits were made, and no agent messages were sent. The four affected implementation files were unchanged between the audit boundary and the later checkout check at `12b33b136`.

## Findings

### 1. P1 — ARGUS cannot inspect the pending closeout changes its verdict is supposed to approve

**VERIFIED — code and isolated Git reproduction.** Introduced in `c888dfa45`.

Locations: `PROME/tools/argus_scope.py:45`, `PROME/CLOSEOUT.md:134`, `.claude/agents/argus.md:11`.

The closeout manual runs ARGUS **after all writes in Chunks 1–3, before the closeout commit**. However, `scope()` takes paths only from already-committed `watermark..HEAD` changes, and ARGUS is told to inspect `git diff <watermark>..HEAD`. Pending tracked changes and new files are absent from both. Even a pending modification to an already-included path is absent from that instructed diff. ARGUS nevertheless returns a “safe to commit as-is?” verdict, and the trial is graded on defects caught before commit.

Reproduction: create a prior PROME closeout, commit one PROME tool change, then modify `PROME/HANDOFF.md` and create `PROME/BRIEF.md` without committing. The scope contains only the tool and returns **SKIP**, despite both closeout documents awaiting review. Once the closeout is committed, it becomes the next watermark, so these omissions need not be recovered at the next run.

Two additional weaknesses affect completeness:

- Attribution uses only subjects beginning `PROME`. Actual PROME-owned commit `4c3cd92fc` begins `FORGE:` and documents PROME's reconciliation and correction. Such a commit does not contribute its paths, although another included commit could incidentally touch them.
- `find_watermark()` excludes a closeout only if it is literally HEAD. A domain commit arriving immediately after a closeout makes the just-finished closeout the watermark. The fixture then returned an empty scope rather than the session just closed. This affects the advertised post-closeout behavior.

**Fix:** freeze an explicit last-audited baseline and candidate revision/diff. Include the intended pending closeout changes and newly created files, scoped to PROME's ownership rather than the entire shared dirty tree. Use durable attribution for shared-file work. Advance the audit watermark only after a successful audit of that candidate. Test pending files, shared-file commits, and intervening domain commits.

### 2. P2 — Corrections to decision records can be ignored while the Deck displays the obsolete version

**VERIFIED — pinned-code fixture reproduction.** Introduced in `a71ecefd5`.

Locations: `PROME/tools/wq_ledger.py:222`, `PROME/tools/decision_deck.py:206`, `PROME/tools/decision_deck.py:243`.

`diff_state()` compares status and only three other fields: `needed_by`, `verdict`, and `will_verbatim`. It ignores `record`, `title`, `rec`, `type`, `since`, `source`, and the source event date. A correction that leaves those four compared fields unchanged creates no UPDATED event. Because the Deck takes terminal ledger rows before the current queue, the obsolete ledger record wins over the corrected primary record.

Reproduction using the shipped fixture: backfill it, correct WQ-903's record timestamp from `09:00 ET` to `10:00 ET`, then sync and render Decided. Observed:

```text
sync: 0 events (ledger matches the queue)
Primary record contains 10:00: True
Deck still contains 09:00: True
ledger check: PASS
```

A corrected source path or substantive record text can be lost by the same mechanism. No existing ignored-field divergence was found in the live rows at the audit check; this is a reproduced failure mode, not evidence of a current wrongly displayed ruling.

**Fix:** define the semantic payload represented by an event and compare all of it, excluding generated write metadata. Preserve a canonical reference or hash for text that is intentionally abbreviated. Add a test that corrects a terminal record and verifies the rendered Deck, not just the ledger count.

### 3. P2 — Two legitimate updates on the same day make the ledger reject its own output

**VERIFIED — pinned-code fixture reproduction.** Introduced in `a71ecefd5`.

Location: `PROME/tools/wq_ledger.py:279`; related closeout requirement at `PROME/CLOSEOUT.md:54`.

The duplicate key is `(wq, event, at, status_after)`. Sync normally supplies `at` at day precision. Two deadline changes on one day can therefore both legitimately produce `(901, UPDATED, 2026-09-11, OPEN)`. Both appends succeed and the tool seals the resulting file; its own `check` then fails.

Reproduction: move the fixture's WQ-901 deadline from September 30 to October 1, sync, then to October 2 and sync again. Both runs append one event. Check reports exactly:

```text
duplicate event ('901', 'UPDATED', '2026-09-11', 'OPEN')
```

The required closeout check now blocks on valid tool-generated history. The closeout manual incorrectly equates rc=1 with a broken seal and recommends restoring from Git; that is not the cause here and can discard legitimate intermediate events.

**Fix:** give each event a unique identity or sequence; distinguish repeated payloads from distinct changes on the same date. Keep idempotence based on semantic state. Validate proposed additions before writing and distinguish schema/event errors from seal failures in the recovery instructions.

### 4. P2 — Rapid taps can overwrite a decision's approval history

**VERIFIED — executed the pinned Deck JavaScript with DOM/store stubs.** Introduced in the Decision Deck build, `049308576`.

Locations: `PROME/tools/decision_deck.py:622–624`; intended contract in `PROME/proposals/2026-09-10_wq202-decision-deck-RULED.md:16`.

The approved design promises one document per tap. The implementation builds the ID from the WQ number plus a timestamp truncated to seconds and calls `doc(id).set(...)`. Only the clicked button is disabled; a different verdict button remains available.

Reproduction: invoke APPROVE at `18:00:00.100Z` and DECLINE at `18:00:00.900Z` for WQ-901. Both writes target `901-20260911180000`. With normal document-set overwrite semantics the store retains one document, containing DECLINE. Reordered asynchronous writes can also undermine the intended latest-tap ordering because only one document survives.

This test verifies the generated client code and its storage keys. It did not access the hosted artifact or establish that any real tap has been lost.

**Fix:** use a unique ID per tap, retaining the full timestamp as data. Preserve every tap and explicitly determine the effective latest ruling during pickup. Test rapid conflicting taps and out-of-order write completion. Disable the card's controls during an in-flight submission if desired, but do not use that as the sole uniqueness guarantee.

## Existing limitations that should stay visible

- **BOARD row presence is not proof of disposition.** `exempt_gap.logged_ids()` clears an ID even when the disposition is blank. PROME explicitly declared this as R4 in `b9071b818` and subsequently escalated the issue in `1f3030be9`; this audit does not count it as a newly discovered defect. The instrument is useful for finding missing rows, but its green result must remain limited to row presence until it checks valid disposition content.
- **The promised unconsumed-tap boot advisory is absent from `prome_gate.py`.** The WQ-202 ruling record promises a script advisory; BOOT step 3b instead provides a manual Artifact-store pickup. The gate contains no corresponding check. This is a documented-deliverable gap, not proof that a tap was missed. Either implement a verifiable pickup receipt/freshness check or amend the description so a green boot gate does not imply the store was checked.
- The ledger's CRC limitation and abbreviated fields were already disclosed. They are not newly reported here; findings 2 and 3 concern behavior beyond those acknowledged limits.

## What held up in the sampled coordination work

**VERIFIED at repository artifacts, not independently at external sources:**

- WATT's `P1 5→3`, composite `16→14/20`, was carried consistently from the owner's STATUS and delivery memo into DOCKET L319. PROME recorded the full-day tape caveat rather than smoothing it out.
- REGINALD's September 10 exit-log row records `79.28`, nonqualifying, run zero. PROME's ROLL70-EXIT state matches the proposed owner cells and retains the next observation as owed; it does not confuse an intraday move with the close-based rule.
- XLE's surviving contract closure agrees across TERRY's receipt, WQ-210, DOCKET L253, and FORGE's management row. The unknown first contract's date/price remains explicitly open under D-49. The audit did not independently authenticate the broker capture.
- The Git-wrapper rename repair has discriminating tests for both rename paths, unstaged deletion, and preservation of another agent's staging. Moving consumer regression tests onto frozen fixtures also removes dependence on unrelated live-book changes.

## Verification and feedback

**Existing checks:** 58 tests passed across `test_commit_pipeline`, `test_exempt_gap`, `test_prome_gate_gates`, `test_desk_attention`, and `test_heartbeat_projection`. The WQ-ledger selftest passed; the then-current ledger passed its schema/seal check. Spawn-list selftest passed 11/11 and queue-parser selftest passed 23/23. The complete operational boot/closeout gate was not run because it contains stateful actions. Hosted Artifact database behavior and actual operator tap history were not inspected.

**Additional checks:** the four findings above were reproduced separately from those passing tests using source frozen at the audit SHA. Local harnesses and evidence are under `/tmp/prome-audit-20260911/`: `reproduce.py`, `reproduction-output.txt`, and `taps.js` (with the extracted `deck.js`). The report preserves the triggers and outputs because `/tmp` is not durable repository evidence.

**INFERRED process assessment:** PROME is improving ownership and follow-through, but its new controls repeatedly measure a narrower object than their descriptions promise: committed paths instead of the pending submission; selected state fields instead of corrected decision history; ID presence instead of completed disposition. More checks alone will not resolve that mismatch.

**Recommended order:** repair ARGUS's candidate scope; repair ledger update detection and event identity; repair tap uniqueness; then tighten the existing BOARD and pickup checks. For each repair, require one adversarial end-to-end test that changes the underlying obligation while leaving the old proxy looking healthy. Keep the ARGUS trial, but grade only audited candidates and separate detection of already-committed defects from prevention before commit. No implementation changes were made as part of this audit.
