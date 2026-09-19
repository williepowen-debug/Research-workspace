# ZHAO — bounded correction verification

**Disposition: PARTIAL.** Will relayed ZHAO's completed correction pass while CATO was testing HANS. Reviewed the committed correction set through **`7edb949a3008b58e2aa6359bd0413228ec735e62`**, against the [five findings](2026-09-19_1359_zhao-closeout-review.md). Fresh fetch confirms this revision on origin/master. Owner files were clean at inspection; shared FORGE/dashboard files were not. No owner edits, new instruments, allocation ruling or agent sends were made.

## What is independently verified

- KB-177 distinguishes the BIS last stay day from reimposition; FLOW-14, STATUS's main calendar and the catalyst row now use the effective date. PROME has a committed instruction to re-date its own row. This is delivery to PROME's inbox, not evidence that PROME acted on it.
- KB-178 and the new decision include qualifying LFP cathode material, both performance conditions, expanded equipment groups and materials/technology exposure. The original omission is acknowledged; the new matrix has problems below.
- KB-179 and FLOW-15 restore the specified Annex parts and the **by-value** threshold to the foreign-content route. The new correction acknowledges the separate technology route and blocks classification until the Annex is mapped. Preserve the alternative routes: the summary sentence beginning “where … ≥0.1%” describes I(1), not a universal prerequisite for I(2) or I(3).
- KB-180 is recorded as ASSUMPTION and retracts the administrative-capacity/cost inference. Parent KB-156/166/174/175/176 carry correction markers at the start of Notes; prior text is preserved.
- Brief lines **19, 69 and 98** now explicitly supersede the old source/scope assertion, correct the LIQUID ask, and mark SOFR/vector-8 work resolved. These exact requested repairs pass.
- The final brief commit `0c86259a8` follows STATUS commit `644afa396`. The prediction ledger is unchanged. The PROME packet was moved to processed. The brief now retracts the stale inbox claim. These are artifact receipts, not independent proof of the claimed historical read times.

## Remaining issue A — High/medium: the revised battery matrix confuses two instruments

**Source:** `PROME/inbox/2026-09-19_from-ZHAO_CORRECTED-battery-decision.md`, matrix and following annex caveat; KB-178; FLOW-15.

Rows 3–4 defer battery-material details to an unretrieved **Annex 1**. That is Announcement **61**'s attachment. Announcement **58** enumerates its battery/cathode/graphite items in the **body**: those two rows do not depend on retrieving 61's Annex. The matrix also omits **3E901.a**, technology for producing controlled 3A001 cells, while including only 3E901.b technology. [Announcement 58, I(3), II and III](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_79646f0161564975a938fe00fee158d5.html).

**Consequence:** the claimed complete eight-row inventory is incomplete and carries the wrong research blocker. “Seven of eight rows reach stationary storage” promotes a table's “likely” into a categorical count; these are grouped regulatory categories, not measured exposure shares. A qualifying LFP material can fall within scope without every grid-storage product or supplier being exposed. The recital alone does not establish commercial use or realized disruption.

**Required:** finish the 58 matrix from its body, include the missing technology limb and the actual item parameters, and reserve the Annex blocker for 61. Label potential applicability separately from demonstrated grid exposure. Keep the qualifying LFP correction. PROME should decide from the corrected perimeter, not the seven-of-eight slogan. This review neither assigns WATT nor disputes that some material/equipment pathways can matter to it.

## Remaining issue B — High/medium: active readers still repeat the withdrawn conclusions

The correction was applied at selected anchors, not across the live handoff:

- **NEXUS_BRIEF line 17** still says no licensing practice/compliance base/administrative precedent and that lapse is cheap for Beijing. **STATUS lines 17 and 178** repeat that same live inference, despite the header and KB-180 withdrawing it.
- **Brief line 18** still lists four cell-machine classes, omits the cathode branch, tells NEXUS to carry the chemistry-selector story, and retains the weakened intent inference. **STATUS line 168** still describes the pending recommendation as “equipment+anode only,” with a do-not-re-litigate instruction.
- **Brief line 92** still dates the BIS event **Mon Nov 9** and attaches automatic coverage consequences. It remains precisely the last-day/effective-day conflation the correction was intended to remove; line 93 directly below now says effective November 10. The old one-day framing also survives inside the newly edited As-of line.
- **KB-173 remains wholly unchanged and ACTIVE**, still carrying the incomplete battery enumeration. The five corrected parent rows ZHAO actually names do not include this original scope row.
- The memory file gained a scoping paragraph, but **brief line 16** still asserts independence and universally absent secondary coverage. That consumer did not receive the narrowed claim.

**Required:** correct these named current assertions at their own text, with historical preservation in existing archives or clear local supersession. Do not solve this by adding another new header or KB row. This is incomplete propagation of the original findings, not a new research assignment.

## Delivery remains pending; “replaced” needs a narrower description

The corrected battery decision **is committed in PROME's inbox**. It explicitly supersedes the old decision and HOLD. That is useful and verifiable. PROME's allocation remains unmade in the reviewed evidence.

The corrected VULCAN/HAWK/HENRY packet exists in **ZHAO's outbox** as `2026-09-19b_to-VULCAN-HAWK-HENRY_CORRECTION-2-dates-and-scope.md`, marked **Proposed route: PROME**. The new decision's GAPS also says it needs routing. No copy of this correction was found in the three recipient trees at the pinned revision; those still contain the older September 18 clock packets. Thus **prepared/committed, awaiting routing** is supported; replacement at recipient entry points is not. ZHAO's quoted assertion that the morning correction was already in all three inboxes was not reproduced from the tree either. Do not infer delivery from sender-side outbox presence.

The **old PROME closeout memo itself is unchanged**, still describes the old battery packet as live, and has no in-place retraction. The new decision and brief do retract the inbox claim. The reported “on the memo” repair therefore exceeds the artifact evidence. Preserve the memo historically, but add a clear pointer if its live decision instruction can still be consumed. Its literal “inbox empty” sentence was boot-labelled even before the repair; this review does not independently allege a falsified boot check.

PROME being dark is a normal routing dependency, not permission for CATO to send or for ZHAO to bypass its routing rules. The durable corrected packet can wait if that dependency is explicitly carried. No downstream integration is certified.

## Evidence and next step

[Read-only probe](2026-09-19_1424_zhao-correction-probe.py) · [pinned output](2026-09-19_1424_zhao-correction-probe.txt) · [shared review checks](2026-09-19_1424_review-checks.txt). Record-property checks passed: TSV widths, new rows and parent pointers, three exact brief repairs, unchanged predictions and commit ordering. My first probe had a stale text anchor (“FOR NEXUS” had been removed); I changed it to the actual surviving historical clause after inspection, then reran. That was a probe error, not an owner failure.

**Suggested stopping condition:** correct the named live contradictions and the 58/61 matrix mix-up, then carry routing and Annex 61 classification as unresolved dependencies. No new report on unrelated desk work is needed. This is not a request for another broad sweep or a requirement that CATO review every future commit. Next session: orient and await Will. Shared CATO continuity remains preserved; this report carries this task's disposition. Exact-path commit/push receipt is delivered in-session.
