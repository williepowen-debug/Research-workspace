# PROME boot: concrete corrections and bounded repair suggestions

**Assignment:** Will asked for suggestions or fixes to the quoted prome-92 boot. This is a bounded review and repair proposal, not authorization to take over active PROME/TERRY files. Main snapshot: `ca3e519e04e72e237781898cdbd1d4ab0d96dbef`, September 19, 2026. PROME and desks are active; findings are snapshot-limited. No owner edits, sends, launches, trade actions or publication performed. No new standing review gate proposed.

## Recommended corrections, in order

### 1. Repair the presence reader's shared contract and distinguish failure from uncertainty

**Medium / VERIFIED.** `PROME/tools/spawn_list.py:collect` returns eight fields, inserting cadence before catalyst. `PROME/tools/session_presence.py:report` still unpacks seven. Feeding the actual producer's one-row output to the actual reader raises `ValueError: too many values to unpack (expected 7)` before the completion marker. An empty valid fixture completes at rc 0; an empty stale fixture completes at rc 1. Testing only empty inventories would miss this regression.

**Fix:** update the reader to the current eight-field contract; do not use a permissive slice that silently shifts catalyst into cadence. Pass the roster input if this reader is meant to use cadence. Add one producer-to-consumer regression with a due row, plus empty and invalid-input cases. A named record is a possible later simplification, not required for this repair. Audit direct consumers of `collect` within the existing L446 review.

`PROME/tools/prome_gate.py:272` treats every child non-success as the caller-selected severity; this reader is invoked as ADVISE at the boot call site. The traceback remains in the saved log and its last line is shown. Therefore it is **not hidden**, but a crash and an ordinary evidence gap occupy the same advisory category; the parent check label always says presence UNKNOWN.

**Acceptance:** one or multiple producer rows render fully; empty rows work; stale/malformed snapshots retain UNKNOWN and never authorize spawning; a reader crash yields an explicit incomplete/failed-check result with the full log. Preserve the distinction between a failed instrument and an instrument that successfully establishes insufficient evidence. Define that child's outcomes before adapting the wrapper; do not globally reinterpret rc 1 across unrelated tools or silently promote all advisories to blocking. L446 already carries independent review, and PROME's WQ-229 discipline applies.

### 2. Make the proposed position-mirror repair complete at its consumers

**Medium / VERIFIED source and current parser; historical build claims remain owner-reported.** The September 19 ANVIL packet under `PROME/inbox/2026-09-19_from-ANVIL_L424-vlo-fill-and-tlt85p-mirrored-plus-a-9-16-capture-that-contradicts-six-cells.md` reports two additional defects beyond Fleet-Ops bindings: TERRY's parser omits the new `Account UNATTRIBUTED` section, and the proposed mirror exceeds the read cap. Current `AGENTS/TERRY/scripts/positions_from_forge.py:57` admits only Fidelity/Robinhood headings; an unknown level-two heading exits the position region. Rebinding Fleet-Ops alone does not establish that the new position reaches TERRY. The earlier over-cap candidate is absent, so its exact size and seven-error dashboard result were not independently reproduced here.

**Fix proposal:** cover L424/L449's mirror edit and dashboard binding, TERRY's handling of an unattributed account, and necessary size reduction in the same bounded completion scope. Keep account and fill time UNKNOWN until supplied; preserve historical evidence and broker disagreements. Before any authorized archive split, apply the existing owner review rules. L448's broker capture/Activity reconciliation remains separate and cannot be closed by copying a screenshot interpretation.

**Acceptance:** the approved receipted fill appears exactly once at both relevant consumers with unknown account preserved; prior rows retain their intended classification; dashboard assertions pass against the final mirror; applicable read-cap checks pass; differences of vintage and unresolved broker facts remain visible. This review does not grant WQ-271 or a trade approval.

**Correction to the boot:** ANVIL's packet is dated September 19, not yesterday. Its TLT 85P finding says the sale was already correctly mirrored; the proposed change adds the late card-closeout cross-reference. Do not describe this as adding a missing TLT position. The later capture contradicts an assertion that the older quantities are *current*, not necessarily their truth on the older snapshot date.

### 3. Preserve proposed changes while approval is pending

**Medium / mechanism correction VERIFIED; disappearance cause UNKNOWN.** Uncommitted files normally survive a session boundary. The quoted checks establish the absence of the expected working-tree edit at that boot; they do not establish what removed it. No forensic recovery was commissioned here.

**Fix:** preserve the proposed diff as an exact-path committed patch in PROME's own proposal/report area, with base revision, affected paths, review limits and the approval needed. The live mirror can remain at its last approved state. Verify that the patch applies to its declared base and recheck conflicts against current owner work before application. A WQ row preserves the decision, not the bytes. ANVIL's narrative can support reconstruction but is not proof of byte-exact recovery. Investigate the actual loss only if needed; do not make a broad deletion-cause claim from an empty diff/stash.

### 4. Correct the ownership claim before using it to restructure work

**Medium / VERIFIED at the inspected snapshot.** The canonical pending-state reader finds 154 live rows, 103 mentioning PROME, and 48 with PROME as first parsed owner. Nineteen rows end September 19, of which eighteen have PROME first. These are later counts than the boot's 140/95/18, not proof that its earlier counts were wrong. First-owner parsing is itself a routing convention, not proof of sole substantive ownership. The distinction is enough to reject using “names PROME” as the count of work only PROME can perform.

**Fix:** label involvement and lead routing separately. For the bounded current-day triage, distinguish owner delivery awaiting consumption, actual PROME implementation, independent verification, and a decision only Will can make. Read the existing receipts before commissioning more work. “PROME-OWNED — do it, never spawn” belongs to this due-row desk-spawn classifier; it does not by itself revoke PROME's separately governed instrument/delegation authority.

**Acceptance:** resolve only against evidence and done-conditions; re-date with a reason and preserved obligation; retire only with a superseding disposition or applicable authority. Queue shrinkage is not the measure of completion. Do not reopen an already approved decision simply because it moved dates.

### 5. Reduce generated repetition without using queue clearance as a prerequisite

**Low / VERIFIED code behavior; design suggestion.** `scripts/docket_view.py:render` truncates catalyst prose but inserts the entire owners cell into every forward calendar entry. Long role explanations therefore recur in boot text. Reducing live obligations is not the only possible remedy for calendar size.

**Fix proposal:** keep full ownership semantics in the canonical docket/detail view; render a compact owner identity and row reference in the boot calendar, preserving overdue visibility, dates, counts, coverage caveats and access to every full obligation. Evaluate a compact rendering against the current snapshot before broader archival work. Do not truncate canonical owner fields or silently omit inconvenient rows. Use existing rendering machinery rather than a second queue.

### 6. Apply the existing skipped-control rule to the boot headline

**Medium / VERIFIED rule versus supplied quotation.** `PROME/CLAUDE.md` §Session Process Controls says a skipped required control makes the report headline PARTIAL. The quotation discloses the skipped DATE-DRIFT reread but opens “Booted” and later claims all built controls work and nothing is a correctness failure. The crash and skipped control contradict that generalization. Blocking gate PASS can still be reported as its limited result; it does not certify the complete boot procedure.

**Fix:** say “Boot PARTIAL: blocking checks passed; presence reader failed; required artifact reread outstanding,” followed by the actual limitations. Replace the saturation diagnosis with a hypothesis supported by workload evidence, not an explanation that excludes correctness defects.

The read-only firetime scan returned rc 1 and 11 flags at this later snapshot, including the cited Dec-18 flag. During review, TERRY moved the cited packet to `inbox/processed/`; its complete text was read there. Dec-18 is an option-expiry illustration, not automatically a docket catalyst date. That makes contextual disposition necessary, not a date replacement. The packet also says “2026-09-22 onward” for eligibility, so a full logic reread must assess bounded tenor eligibility and current applicability, not only explain the flagged string. This pass did not adjudicate the trade, its current gates, all dependencies or all eleven flags. PROME must verify current owner disposition before duplicating a reread; no expired allowlist or stale packet path should be treated as current clearance.

## Evidence, limits and closeout

[Read-only probe](2026-09-19_1725_prome-boot-fixes-probe.py) and [results](2026-09-19_1725_prome-boot-fixes-probe.txt) preserve revision and source hashes, the actual producer/reader counterexample, valid/stale empty cases and the queue census. The firetime scan and direct source reads support the other findings; no full PROME boot or financial-source verification was run. The TLT deadline, prices, broker facts, inbox census, hosted Deck and comparative claims about a month ago are outside this bounded verification.

**Implemented:** CATO evidence/report and resume pointer only. **Tested:** isolated current-code counterexample and canonical queue census; existing firetime instrument run read-only. **Independently established here:** the contract failure, parser heading limit, count distinction, renderer behavior and instruction/quoted-headline mismatch. **Unresolved:** owner repairs, proposed candidate rebuild, disappearance cause, financial facts and approval decisions. Prior CATO-authored components remain author follow-up, not independently certified by this session.

No owner repair or peer send is assigned. Next: await Will; if owner fixes are submitted for review, begin with these bounded acceptance conditions and current revisions. Do not automatically re-audit the whole operation. Closeout checks and exact-path commit/push receipt are delivered in-session.
