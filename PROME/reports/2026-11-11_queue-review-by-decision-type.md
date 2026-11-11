# WILL_QUEUE review: research and trade decisions vs system decisions, and which approvals were avoidable repeats

Source: `PROME/WILL_QUEUE.md` as of 2026-11-11 (master; latest queue commit 99ca0fd79a era), read in full, both sections. Charter grants checked against `PROME/CLAUDE.md` § Ask First. Read-only review; no repository change.

## A. Coverage

- **Rows classified: 209.** That is 208 RECENTLY DONE rows plus 1 OPEN row (WQ-31, the credential-renewal sitting that needs Will's hands).
- **Done-date range: 2026-10-04 to 2026-11-11.** Earliest: WQ-369, 377, 379, 380, 383 and 384, all Done 2026-10-04. Latest: WQ-669 to 672, Done 2026-11-11. RECENTLY DONE is not a strict 7-day window, so older rows are still in the file.
- **Rows I could not classify: 0.** But the recommendation could not be read for 35 rows: receipts, hands rows, one lapsed row, and rows whose text does not record PROME's recommendation (WQ-663, 527, 503, 505, 441, 492, 518). Those are marked "no rec shown" in C.
- **Not covered:** the roughly 300 earlier rows already moved to `PROME/archive/WILL_QUEUE_ROWS_*` files. I did not read them. When I say "already approved before", the evidence comes from this window plus the grants in the charter.

## B. Counts: DOMAIN by KIND

| DOMAIN | CHOICE | REQUESTED | REPEAT | OTHER | Total |
|---|---|---|---|---|---|
| RESEARCH/TRADE | 81 | 3 | 16 | 11 | 111 |
| SYSTEM | 46 | 8 | 36 | 8 | 98 |
| **Total** | **127** | **11** | **52** | **19** | **209** |

- **Trade, spend and position items: 35.** All of them are counted as CHOICE in the research/trade row, as instructed.
- **REQUESTED rows (Will's own request):**
  - Research/trade: WQ-622, 544, 523.
  - System: WQ-619, 540, 448, 538, 525, 460, 447, 446.
- **OTHER rows (19):**
  - Receipts for acts done under C9 or recorded under C2.
  - Hands rows marked done, and rows closed because they were overtaken.
  - WQ-558, a test question asked only to try out the Decisions app.
  - WQ-554, a record of Will's word that asked nothing.
  - The OPEN row WQ-31.

## C. Did Will take the recommendation?

Counted over rows where a recommendation was shown.

| DOMAIN | Taken unchanged | Changed | Declined against the rec | No rec shown, or a receipt |
|---|---|---|---|---|
| RESEARCH/TRADE | 80 | 10 | 0 | 21 |
| SYSTEM | 65 | 14 | 5 | 14 |
| **Total** | **145** | **24** | **5** | **35** |

- **Research/trade changes (10):** WQ-668, 656, 650, 649, 632, 589, 550, 622, 493, 494. Three times he declined a hands task, and each time on PROME's own recommendation to drop it (WQ-547; and 477 and 548 had no recommendation). Those count as taken unchanged, or as no rec shown, not as declines.
- **System declines (5):** WQ-599, 623, 576, 529, 380.
- **System changes (14):** WQ-662, 667, 658, 657, 655, 653, 652, 648, 597, 570, 566, 488, 482, 449.
- **Acceptance rate:** about 89% on research/trade (80 of 90) against about 77% on system (65 of 84). System proposals are where he most often edits, adds conditions or says no.

## D. Avoidable repeat approvals, grouped into classes and ranked by count (52 rows)

1. **Confirming a research reading or grade that changed no gate level (10 rows).**
   - Rows: WQ-629, 512, 644, 522, 603 (already covered by a grant); WQ-605, 604, 643, 671, 516 (could be covered).
   - In plain words: a desk's written rule already decided the answer, or the ruling expressly moved no level, operator, instrument or consequence.
   - Example: WQ-629, *"629 A"*. FERT's note placed in the gate's condition cell; level and operator unchanged, not fired.
   - Existing grant:
     - C1 (owner's wording clarification) already covered WQ-629 and 512.
     - C3 (a no-change answer that the desk and PROME both recommend) already covered WQ-644 and 522.
     - WQ-603 is close to C1.
     - The rest are not covered: grading a forecast by its written rule (605), a desk's own score step (604), re-pointing an unchanged test to its next print (643), a descriptive status line with no gate (516), and ownership of a figure (671). Will's 9/29 word already gave prediction-market odds to ORACLE, but ownership is still a reserved class in the charter.
   - Standing permission that would remove the class: "a desk may grade, score or roll forward its own forecast under its written rule, and PROME records it and reports it the same day."
2. **Waking desks past the per-boot limit, or on a due row (9 rows).**
   - Rows: WQ-626, 618, 588, 481, 479, 465, 391, 390, 389.
   - Example: WQ-588, *"588 Yes you may wake desks approved"*.
   - Existing grant: C6 and the WQ-184 due-row rule covered waking up to eight desks. Every row here was either over that limit, or a desk-usage question raised by an earlier remark from Will.
   - Standing permission: already given. WQ-667 B and WQ-661 A (2026-11-10) removed the count limit, so this class should now stop recurring. Check it at the next review.
3. **Text-only edits to manuals and charters that changed no rule (9 rows).**
   - PROME's own manuals and the root rulebook: WQ-371, 552, 549, 630, 602.
   - Desk charters and instructions: WQ-519, 660, 543, 457.
   - Example: WQ-552, BOOT.md rotation, *"okay go ahead with 552 A"*. The record says "No rule's meaning moves."
   - Existing grant:
     - C4 covers a desk editing its own charter where no authority, route or threshold moves. That arguably covers WQ-519 and 660 (660 also extended WQ-622, which Will had already approved).
     - Nothing covers PROME's own charter (C4 excludes it) or the root rulebook.
   - Standing permission: "a wording, rotation or consolidation edit that a blind reader confirms changes no rule's meaning may land without asking, and is reported the same day."
4. **Next steps inside work already approved (6 rows).**
   - Rows: WQ-641, 607, 510, 517, 458, 393.
   - Example: WQ-458. Will said, verbatim, *"Walter is handling this and progressing through. Does not need a WQ for me to approve."*
   - Existing grant: Tier 1 ("follow-ups inside an approved workstream") arguably covered all six. WQ-393 re-ruled a docket item he had already ruled.
   - Standing permission: "a step that stays inside a ruled scope does not come back to Will unless it moves money, authority or a gate." This is Tier 1 applied to system builds as well as research.
5. **Retiring, trimming or re-filing process items with nothing changed in substance (6 rows).**
   - Rows: WQ-654, 645, 594, 595, 379, 530.
   - Example: WQ-594 reclassified two gate rows' check type with "No grade, threshold, operator, consequence or owner changes." Will's word on WQ-594 to 597: *"no repeat approval is needed."*
   - Existing grant: none by name. Will's 10/31 standing preference for fewer checkers and rules points the same way.
   - Standing permission: "retiring or trimming a process check, schedule or backlog item may be done without asking when no gate, authority or Will ruling is touched, and is reported the same day."
6. **Research commissions that did not fit C9 (5 rows).**
   - Rows: WQ-537 and 511 (before C9 existed); WQ-545 (three desks); WQ-646 (four weekend reads); WQ-524 (one more case in an approved review).
   - Example: WQ-537, *"A approved"*. In the same breath Will asked that this class be fired without asking, which became WQ-538.
   - Existing grant: C9 since 10/29, but it covers only one desk and two commissions per boot.
   - Standing permission: "C9 may cover one coordinated read by several desks on the same finding, counted as one commission."
7. **Exceptions to PROME's own process limits, and extra review reads (5 rows).**
   - Rows: WQ-467 and 445 (the process-change ceiling); WQ-468, 384 and 534 (an extra reader round, or which review counts).
   - Example: WQ-384, *"CATO review does count."*
   - Existing grant:
     - The ceiling has been suspended since WQ-566 (10/31).
     - The review budget still requires Will's named word for any read past three.
   - Standing permission: "an independent review already done by another desk counts toward the budget." A spent budget defaults to "shelve and report" (as in WQ-534) rather than a question to Will.
8. **Changes inside a lane already granted to PROME (2 rows).**
   - Rows: WQ-598 (free news queries) and WQ-450 (adding a HEARTBEAT section).
   - Example: WQ-598, *"approved with your recs"*, covering two free `when:7d` search queries.
   - Existing grant: C7 (free feeds) and the 8/23 grant making HEARTBEAT PROME's to edit. Both already covered these.
   - Standing permission: none needed. Apply the grants as written.

Other signs of repeat asking:
- **Double asks.** WQ-570 was ruled in CATO's window and then asked again by PROME. WQ-565 was okayed in the NEXUS session and asked again. WQ-553 asked for the principle and then the exact text the same day.
- **Will handing the call back.**
  - WQ-513 to 516: *"lets have you approve with your recs"*.
  - WQ-483: *"approve(as long as you recommend this)"*.
  - WQ-601: *"Can I approve with your suggested recs"*.
  - WQ-617 to 614: *"approve with your recs all four"*.

## E. Five choices that were worth his time

- **WQ-615.** The HYG junk-bond hedge (put spread ×5 at no more than $0.60, maximum loss $306.50). It is his money, and the order is his hand.
- **WQ-656.** He closed CARL's CRL-15 forecast as ungradeable against PROME's recommendation A, and set how the failure is reported. This is his standard for judging forecasts.
- **WQ-550.** On the Binance hack he rejected the recommendation to exclude it (*"it certainly matters and we should definitely clock it"*). This changed how a research band is graded.
- **WQ-599.** He said no to shrinking the fleet and no to the RSP trade in one word. Roster, cost and a trade are all his.
- **WQ-667.** He picked "no number" over PROME's eight-desk wake limit. This is his cost appetite, and it reversed a long-standing brake.

## F. Where Will declined or changed a SYSTEM proposal (where a standing grant would be unsafe)

- **Declined (5):**
  - WQ-599: fleet shrink.
  - WQ-529: retiring the YURI desk.
  - WQ-576: a cadence-wake rule.
  - WQ-380: the `.env` read fence.
  - WQ-623: launches deferred to the next session.
- **Changed (14):**
  - WQ-662 and 667: picked B over PROME's A.
  - WQ-655: approved the direction but not the migration, and added "No trial, measurement program, new checker or expanded audit".
  - WQ-658 and 657: added conditions.
  - WQ-653: his own wording.
  - WQ-652: a review condition.
  - WQ-648: clarifications.
  - WQ-597: accepted the four repairs, with one bounded correction only and "not another general maintenance sweep".
  - WQ-570: chose the improvements over PROME's revised recommendation C.
  - WQ-566: removed the ceiling, going beyond option A.
  - WQ-488: the cap question needed correction first.
  - WQ-482: asked for written forum guidelines.
  - WQ-449: moved the calendar view out of the NOW page.
- **His own unprompted retirements:** WQ-460 paused the Decision Deck (*"its becoming a bit cumbersome"*). WQ-461 retired routine Helm work (*"I have not been using it"*).
- **Where a grant would be unsafe:**
  - New process programs, trials, checkers and measurement studies (WQ-655, 597, 599).
  - Numbers that set PROME's own limits (WQ-667, 566).
  - Design of the decision surfaces (WQ-570, 662, 449, 482).
  - Roster and seats (WQ-529, 599).
  - Security and privacy (WQ-380, 600, 565).
- **Pattern:** his changes mostly cut steps (WQ-566, 667, 576, 458). The exception is WQ-570, where he wanted more built.

## G. Confidence and the main ways this could be wrong

- **Confidence: moderate.**
  - The DOMAIN split is firm: about 5 rows mix both domains (WQ-601, 590, 533, 494, 377), and each was assigned by its main element.
  - The CHOICE / REPEAT line is the soft part.
- **The biggest swing: 37 non-trade research rulings.** These rulings set gate levels, band cells, forecast letters or end windows. Will approved PROME's recommendation unchanged, with no money involved, and I counted them as CHOICE because they changed what a gate does and real alternatives were shown.
  - Rows: WQ-670, 669, 666, 665, 664, 659, 647, 640, 637, 636, 635, 634, 627, 624, 620, 611, 609, 608, 563, 562, 559, 553, 551, 541, 542, 536, 535, 533, 532, 528, 521, 459, 453, 444, 395, 392, 368.
  - If Will treats an answer that the desk and PROME agreed on as delegable, REPEAT would rise from 52 to about 89, and research would become the larger repeat area.
- **Who started the ask is unclear for some rows.**
  - WQ-594 to 597 are labelled "user-provided implementation plan", but their proposals were PROME's. I counted them as PROME-originated.
  - The origins of WQ-523, 525 and 526 are not stated in the rows.
  - WQ-560 followed Will's challenge on glued words but was PROME's proposal.
  - I marked REQUESTED only where the row or its record quotes Will starting it.
- **"Already approved before" is judged from this window only.** First instances such as WQ-537, 371 and 389 may have antecedents in the rows already moved to the archive files.
- **Unknown recommendations.** For 7 ruled rows the recommendation is not recorded, so C undercounts both changes and acceptances.
- **Borderline single calls:**
  - WQ-671: ownership is a reserved class, but Will's 9/29 word arguably settled it.
  - WQ-652: the condition only restated the existing review rule.
  - WQ-391: "spawn at Opus" repeated an existing preference.
  - WQ-661: counted as CHOICE, not as a wake repeat.
