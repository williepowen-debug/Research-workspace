# CATO — ZHAO committed closeout review

Will requested review of ZHAO's closed session through **`c0092ebad059e69ee54dccf9058ecead65e6b2aa`**. Reviewed the owner changes from `a7e284a4b` through that closeout, including primary/result letters, KB-172–176, KB-166, FLOW-15, STATUS, the final brief, archives, catalyst edit, memory and PROME decision packets. Other agents' concurrent work and later commits are outside this verdict. This is independent review of ZHAO's implementation, with author follow-up on earlier CATO objections where they recur below.

**Disposition: the primary date pull delivered useful, verified corrections; the research handoff is not clean. Five substantive findings remain.** No owner files, allocation decisions, prediction grades or recipient inboxes were changed by this review.

## What independently checks out

- Announcement 70 explicitly names **2026-11-10**, both ministries, and the six suspended announcements. The date no longer needs to rest on secondary reporting. Its enumerated scope excludes Announcement 18; this confirms the narrow F6 test, not an exhaustive search for every subsequent policy change. [MOFCOM 70](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_b1ec77dd3f0d4762952904df7cdaadec.html).
- The five elements in F4 match Announcement 57. Its commencement and Announcement 58's commencement were scheduled after the suspension; Announcement 61's foreign-content and technology limbs also had later commencement. The limited **suspended-before-commencement** finding is sound. [MOFCOM 57](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_59ec4f6bec0b459aa4a30c4bbd0a41c1.html), [58](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_79646f0161564975a938fe00fee158d5.html), [61](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_7fc9bff0fb4546ecb02f66ee77d0e5f6.html).
- The military-AI qualifier was incorrectly attached to the semiconductor limb; the new disjunction reading fixes that. Finding 3 concerns the outer scope that still must surround it.
- The prediction ledger is byte-for-byte unchanged across the reviewed session. ZHA-16 remains OPEN, Resolve_By 2026-09-30; ZHA-18 remains open, Resolve_By 2026-10-23. The expected October 16 publication and the October 23 resolution deadline are distinct; retain those labels in future summaries.
- KB-166 is CORRECTED, with its original Fact unchanged and its original Notes preserved verbatim after a prominent correction. The three sampled archive moves also preserve their removed lines verbatim with live pointers. This is appropriate preservation of historical evidence.
- The final brief commit `068e753c7` descends from STATUS commit `a89c6cce6`, and its timestamp is not earlier. The ordering repair is real. STATUS measures 25,609 bytes, 78.7% of its 32,550-byte budget; the brief measures 100 lines / 42,499 bytes. The brief's size is a measurement, **not a claimed hard-cap violation**: NEXUS's schema treats line-cap enforcement and read truncation separately.
- Changed TSVs have consistent widths, and catalyst date_class values match the reader's enum. The memory file was committed in `f30359f85`. These mechanical passes do not validate the meaning of the prose.

## 1. High — the battery allocation omits the cathode branch

**Where:** `PROME/inbox/2026-09-19_from-ZHAO_DECISION-battery-leg-allocation.md:20–44`; KB-173/176; FLOW-15; brief line 18.

The decision describes three legs—cells, cell equipment, graphite anodes—and recommends WATT receive equipment/anode only. **Announcement 58 separately controls qualifying LFP cathode material:** compaction density ≥2.5 g/cm³ **and** specific capacity ≥156 mAh/g. It also includes other cathode materials/precursors and cathode-manufacturing equipment. The decision never mentions cathodes. Its cell-equipment list names four categories where the text has six. [Primary, sections I–III](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_79646f0161564975a938fe00fee158d5.html).

**Consequence:** the proposed scope excludes a potentially relevant grid-storage input. A sub-300 Wh/kg finished cell does not establish that its cathode material is outside the separate control. Nor is ≥300 a chemistry classification: ZHAO's own NMC range begins below that threshold.

**Suggested fix:** replace the three-leg abstraction with a complete item/parameter matrix; distinguish finished cells, materials, equipment and technology. Reissue the allocation packet with the omitted exposure and retain intent as inference. PROME still owns allocation; this review does not select WATT or open a channel. Do this before deciding from the current packet.

## 2. High — the BIS effective date remains wrong in the freshly issued handoff

**Where:** RESULT line 66; outbox correction lines 12/45; STATUS lines 12/133; brief lines 6/19/92–93; existing FLOW-14. The PROME-to-ZHAO packet committed at `5a2cf6d3f` already distinguished the two dates and barred quoting a one-day separation pending resolution.

The published BIS rule distinguishes **November 9, 2026, the last suspension day**, from **November 10, 2026, reimposition effective**. The new correction packet nevertheless says the two instruments are 48 hours apart and now stand on primary text on both sides. [BIS final rule, section II.B](https://www.govinfo.gov/content/pkg/FR-2025-11-12/html/2025-19846.htm).

**Consequence:** readers can activate exposure changes on the wrong date; a known contested interpretation is presented as settled. “Within 48 hours” is not itself mathematically false for simultaneous events, but the explicit consecutive-day/one-day-gap narrative is wrong.

**Suggested fix:** label any November 9 reminder as the final stay day; date US reimposition November 10. Correct current summaries and send the requested disposition to PROME under the owner's routing authority. Keep the sovereign instruments separate. The Chinese text confirms its stated end date but does not justify asserting an exact shared intraday activation time.

## 3. High — fixing the semiconductor disjunction still leaves an overbroad jurisdiction claim

**Where:** new FLOW-15 Pathway; KB-174 Notes; outbox correction line 28; preregistration F5 and its unconditional PASS.

Announcement 61 I(1) concerns specified **Annex 1 Part 2** foreign-made items containing specified **Part 1** Chinese-origin items at ≥0.1% **by value**. I(2)'s technology route also names Annex-listed items. Clause IV supplies an end-use approval policy within that framework. It does not turn every rare-earth input to “any fab” into an automatically covered export. [MOFCOM 61](https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_7fc9bff0fb4546ecb02f66ee77d0e5f6.html).

**Consequence:** FLOW-15 drops both the specified-product perimeter and the value denominator; the correction packet's universal fab claim can inflate VULCAN's exposure map. F5 demonstrates that an extraterritorial threshold exists, but its test never challenges those missing restrictions. Six passes cannot certify the broader paraphrase.

**Suggested fix:** carry the item, jurisdiction, denominator and end-use conditions together. Keep the valid civilian/military distinction. Retrieve and map the annex before company/product exposure classification. This review accessed the announcement body but could not retrieve the linked WPS annex; it therefore does not offer a complete controlled-product inventory.

## 4. Medium — final refolding fixed order, but left conflicting live instructions

**Where:** final `NEXUS_BRIEF.md`, pinned to the reviewed commit. Reproductions are in the accompanying probe output.

- Line 19 still says the primary was not fetched, remains B2, and is owed before October 19; it also repeats the military-AI qualifier and “expansion returning.” The corrected findings sit immediately above it. This is an old dated bullet in the active cross-domain section without an in-place supersession notice, unlike KB-166's deliberate historical record.
- Line 69 still asks LIQUID about official selling/private buying and describes private demand absorbing official supply. The current header says July reversed that split. The outstanding ask lacks a June/historical qualification.
- Line 98 still calls the SOFR leg never verified and vector 8 scored 3; the current brief itself reports primary SOFR verification and vector 8 at 4.

**Consequence:** the next reader gets contradictory scope, source status, work obligations and market interpretation from a newly certified final brief. A fresh header does not reliably retire the lower instruction.

**Suggested fix:** update the active ask/carry fields and mark obsolete statements at their own text, preserving history in the existing archive. Verify the final brief against current ledger dispositions, beyond commit ordering. The skipped numeric consumer scan was disclosed; a semantic propagation check was still needed. No new broad scanner is required to repair these examples.

## 5. Medium — “first use” is promoted into unsupported administrative and cost conclusions

**Where:** KB-175 and FLOW-15 Notes; RESULT lines 54–58; STATUS line 177; brief line 17; outbox line 39.

The date comparison supports no prior operation **of those newly added clauses**. The records go further: no licensing practice, compliance base or administrative precedent; nobody including Beijing has operated the machinery; allowing expiry is cheap. That inference does not follow from commencement dates. ZHAO's own record acknowledges continuing April controls and that two portions had already operated.

**Consequence:** a useful temporal finding becomes an unsupported premise about implementation capacity and Beijing's incentive to extend. Pre-implementation preparation and the economic value of a concession are not measured by whether a particular clause had commenced.

**Suggested fix:** retain “no operating history under these newly added clauses”; mark throughput, preparation and political/economic cost unknown or separately evidenced. Keep the existing magnitude-unknown guard. Likewise scope the memory's source lesson to the sources actually inspected: correlated omissions are plausible, but neither “no secondary carried it” nor proven causal independence follows from three sources agreeing.

## Checks, limits and disposition

Evidence: [read-only probe](2026-09-19_1359_zhao-closeout-probe.py), [pinned results](2026-09-19_1359_zhao-closeout-probe.txt), and [closeout checks](2026-09-19_1359_zhao-closeout-checks.txt). The probe passed all record-property assertions; the root orphan advisory, six-file weekday check and working-tree whitespace check returned zero. The advisory exposed concurrent HANS/shared changes, all preserved. Primary sources were independently reopened during this review. F1–F4 and the narrow F6 exclusion check are supported; F5 requires the scope qualification above. I did not certify the entire six-announcement legal corpus, the exact historical order of pre-registration versus fetch, all original secondary articles, or downstream ingestion of the newly staged correction. Pre-registration and result first entering Git together do not independently timestamp their writing order.

The Sunday LPR date is not rejected merely for falling on a weekend: September 20 is a designated Chinese makeup workday in the [official 2026 holiday notice](https://big5.www.gov.cn/gate/big5/www.gov.cn/zhengce/zhengceku/202511/content_7047091.htm). I did not independently establish that specific forthcoming publication time. No trading recommendation or new instrument was created.

**Recommended next step:** a bounded owner correction of these five findings, beginning with the incomplete battery decision and the two rule-scope/date errors. Assess the corrected artifacts against the actual primary clauses; do not make another green aggregate check the acceptance condition. The disclosed missing Chinese-clock vector remains a separate, unassigned follow-up; this review does not authorize building it.

**Delivery/resume:** this report and its evidence are the assigned output. No owner response has yet been reviewed. Another CATO session was explicitly confirmed active and held CONTINUITY; this session preserves that file and records its resume point here. Next session should orient and await Will, not automatically launch repairs or re-review new HANS/MARCO commits. Exact-path commit and fresh-fetch push receipt are delivered in-session. No publication or agent message was sent.
