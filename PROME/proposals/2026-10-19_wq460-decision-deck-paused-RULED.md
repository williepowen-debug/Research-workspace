# WQ-460 — Decision Deck paused

**Status:** RULED PAUSE by Will, 2026-10-19; recorded 12:30 ET in PROME's Codex session `01a154f2-6950-7162-acc6-136aa6f3223f`.

Will's instruction, verbatim:

> Id like to pause the decision deck for now.  My reasoning being = its becoming a bit cumbersome and I think we would benefit by spinning it off of Prome's plate.  Thoughts?

Effective immediately, pause PROME's Decision Deck-specific upkeep: hosted ruling-store pickup, card/explainer maintenance for the Deck, HTML generation, publication and hosted verification. This temporary direct instruction takes precedence over those Deck duties in the existing boot/closeout instructions and WQ-446's publication trigger. Report them as PAUSED BY WILL (WQ-460), not completed. Resume only on Will's word.

Decisions continue in the PROME conversation and WILL_QUEUE, with the existing approval records and append-only WQ ledger. Domain obligations, approved actions and other surfaces retain their existing scope. Shared queue parsers and record-integrity checks remain usable; this pause does not delete tools or history.

The hosted page has not been disabled or updated. Its private ruling store is unavailable in this runtime; unobserved earlier taps remain UNKNOWN, not consumed or discarded. Any eventual return needs reconciliation before treating that page as current.

Spinning off Deck operations is a direction for discussion, not an approved owner assignment or build. PROME recommends that a future operator own presentation and publication, while PROME retains prioritization, recommendations and decision follow-through. No replacement desk or implementation is commissioned by this receipt.

## Procedure encoding — directed follow-through

Will's follow-up, verbatim:

> Okay is this completed?  Can you  check both boot up and close out procedures to make sure we edit its references there as well?

The first receipt recorded the pause but did not edit the manuals. This follow-through updates BOOT.md, BOOT_MODULES.md, CLOSEOUT.md, both root/local boot and closeout skill copies, and the two Deck-specific closeout gate checks. No full boot or closeout is requested by this instruction.

### Draft instructions and invariants (before implementation)

- Boot step 3b becomes **Decision intake; Decision Deck PAUSED BY WILL (WQ-460)**: no hosted-store read/write, tap consumption or Deck regeneration. Unseen taps remain UNKNOWN. Keep WALTER LAST_COMPLETION §WILL_NEEDS intake into WILL_QUEUE and affected queue/ledger checks. BOOT_MODULES' unit-tap procedure becomes dormant until explicit resume and reconciliation. The runtime-disclosure line no longer requires discovery of a paused Deck store; other capability checks continue.
- Both manuals and all four skill copies point to this ruling. BOOT execution order treats paused duties as PAUSED BY WILL rather than an unperformed mandatory control; step 3b's non-Deck intake still runs.
- Closeout Pre-closeout 5 and symmetry row: **Deck-specific prerequisites, explainers, Owed and Reference rendering/publication are PAUSED BY WILL (WQ-460)**. Helm scope remains WQ-382(b); check its publication prerequisites only when publishing it. No stale Deck page is described as current.
- Closeout step 7 retains **ALL generation** before review for active outputs, including the existing Helm generator; omit decision_deck.py and Deck-only explainer upkeep. Keep table_check, done_rows_check, WQ-ledger and orchestration-log checks. Corrections regenerate affected active outputs only. Shared parsers remain installed.
- Closeout step 11 keeps **Publish the verified artifacts** for active authorized surfaces, with Helm's existing scope and supporting-file handling. Deck Owed/Reference publication, hosted reads and hosted-receipt writes are suspended. Existing artifacts/stores/receipts remain intact. Old Deck publication rules are retained in git history and their ruling records; resuming requires Will's word, store reconciliation and synchronized procedures/gate, not merely a timer or spine audit.
- Delivery reports **Deck: PAUSED BY WILL (WQ-460)**, never PUBLISHED or a current NO-OP. The pause alone does not make a session PARTIAL. Other owed delivery failures, skipped active controls and all commit/review/push protections retain their consequences.
- The two integration pointers in COMPLETION_SPEC §How Prome Uses This step 4 and ORCHESTRATION_PLAYBOOK step 5 are narrowed to active Helm sources/renders under CLOSEOUT, with Deck work suspended under WQ-460. Owner-record integration remains mandatory.
- Gate: explicit module constant `DECISION_DECK_PAUSED = True` citing WQ-460; `check_publication_prereqs` and `check_deck_republish` return an advisory **PAUSED BY WILL (WQ-460)** result before reading any Deck input. Their original active branches remain for a separately authorized resume; no other check or gate severity changes.

### Acceptance and review record

reads: 2

1. 2026-10-19 — `deck_pause_plan`, read-only PLAN review: one blocking omission, Repeat boot's fresh-private-rulings requirement and missing-tool PARTIAL wording. Accepted: make both subject to WQ-460. Reader also called out Pre-closeout item 4's Standard+ sentence, included in the draft implementation. Hosted-page availability/unseen taps are declared residue, not a shutdown commission.
2. 2026-10-19 — `deck_pause_result`, independent RESULT review plus read-only procedure walkthrough: RELEASE, no blocking findings. Fresh/repeat boot, Standard/Heavy closeout, correction loops and spine-audit paths honor the pause; WALTER intake and active Helm delivery survive. Reader's own fixture counterexample used actual closeout dispatch/functions: paused Deck plus FIRED-UNEXECUTED gate and missing required review returns rc1 at Standard/Heavy; missing GATES input returns rc2. No Deck inputs/receipts created. New pause tests 4/4, skill parity and scoped whitespace checks pass. No live boot/closeout or repository mutation by reader. This is scoped verification, not the session's final ARGUS review.

- Ordinary: manuals/runners agree and both Deck checks report the named pause; Owed and Reference are covered.
- Overlap: WALTER decision intake, queue/ledger parsing and integrity checks, Helm work and commit/review/push controls survive despite shared Deck code and procedure paragraphs.
- Wrong owner: no files in working desks or hosted artifacts change; root skill copies are within Will's requested procedure-reference scope.
- Missing information: missing/stale Deck store, explainers or hosted receipt cause no Deck obligation during pause; no assertion of empty or consumed taps. The preserved active gate branches still report UNKNOWN on missing input when tested under an explicit fixture override.
- Concurrent activity: fixture-only gate tests do not touch the shared live tree; exact-path edits/commit preserve other agents' work and shared index. No concurrent hosted activity can be claimed observed.
- Verification: inspect the procedure diff, compare skill copies, exercise the paused gate entry points with missing inputs and forbidden reads, run focused existing gate/closeout tests plus a procedure walkthrough. Do not run a live advancing boot or full closeout just to test this change.

**Implementation:** IMPLEMENTED in the named manuals, mirrored skills, integration pointers and gate. **Tests:** TESTED — `test_deck_pause_WQ460.py` (4), `test_deck_owed_digest_L738.py` (16), `test_closeout_simplification_WQ240.py` (23) and `test_review_mechanism_WQ240b.py` (28), all passing under `-W error::ResourceWarning`. Both skill pairs match. Gate entry points print PAUSED without reading Deck inputs; queue/ledger integrity checks remain enabled. No live boot/closeout was run for verification. **Independent verification:** INDEPENDENTLY VERIFIED for this scoped procedure/gate change, read 2 RELEASE. **Still unresolved:** none within the requested workflow pause. **Declared residue:** hosted page is still accessible and its unseen taps remain UNKNOWN; Helm's renderer still links that page. No hosted shutdown or link removal was requested or performed. Existing done-row advisories remain outside this change; terminal-event and queue-view checks pass.
