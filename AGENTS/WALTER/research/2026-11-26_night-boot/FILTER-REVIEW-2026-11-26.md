# Filter review, 2026-11-26 (report only; changes nothing without Will)

**Asked:** Will 2026-11-23 17:18 ET ("filter review ... sample recent cards against desk use; changes nothing without Will"), run on his word 2026-11-26 23:09 ET. Prior empirical review: `design/FILTER_V3_REVIEW.md` (2026-07-04). Window: cards SIG-W-20261112 to 20261126 (228 route rows), kills since 2026-11-12 (37). Method: route_log, kill_log, delivery_log, BOARD front matter, git grep of each recipient desk's own files. Limits are stated per section.

## Headline

The filter is still structurally sound: no false-positive kill found and routing lands on the right owners. The weak points are downstream of the filter: **one card in seven is a correction**, **a third of ACTION cards leave no trace in the owner's work beyond being filed**, and two record fields (confidence wording, the doorbell ledger) have drifted from their specs.

## 1. Kills (37 since 11/12): no false positive found

| Gate | Count | What they were |
|---|---|---|
| Novelty, date trap | 31 | Old articles the Research-Intake collector re-served as new: Yanbu and Petroline from September and October (12), the US diesel-export-ban story from September to October (9, still recurring tonight), Russia's diesel ban extension (3) |
| Credibility | 2 | A mock 'Fed approves Nvidia bank holding company' headline; an X list stringing outages into a pattern |
| Relevance | 2 | A calendar base rate with no decision content; a car matched by a GPU search |
| Novelty, owner holds it | 2 | Russia's diesel ban to January 2027: YURI graded the decree at the primary on 10/31 (YUR-005) |

Spot check of the one kill that looked like a miss (Russia diesel to 2027 with a 'Trump carve-out', Kyiv Post 11/01): correct, the owner holds it. **Change since July:** the dominant kill class moved from 'owner already has it' (about 55% in July) to 'old article re-served by the collector' (84% now). The collector's onset logic flags a headline's first appearance, not the event's age.

## 2. Volume and precedence

228 cards in 13 sitting days (4 to 44 a day; 44 on 11/25). Precedence: PRIORITY 129, ROUTINE 60, IMMEDIATE 35, FLASH 4. Top ACTION recipients: VULCAN 44, FALCON 30, HENRY 21, CYPHER 21, TERRY 19 (BOARD-only), BROCK 19, BRENT 19, LIQUID 18, CORAL 15.

## 3. Desk use (cards 11/12 to 11/24, two-day grace)

| Role | Deliveries | Cited in the owner's own work (KB, STATUS, research) | Filed only (consumption ledger, no other trace) | No trace |
|---|---|---|---|---|
| ACTION | 210 | 134 (64%) | 69 (33%) | 7 (3%) |
| INFO | 862 | 292 (34%) | 534 (62%) | 36 (4%) |

Filed (moved to processed) across all recipients: 1,332 of 1,463 handoffs, 91%. ACTION cards with no citation at all: OSPREY 2, YURI 2, PROME 2, OTTO 1. Desks that file ACTION cards without citing them: SAM 5 of 5, SHADE 3 of 3, BRENT 8 of 13, VULCAN 11 of 29, HENRY 6 of 13.
**Limit:** citation by ID is a proxy. A desk can use a card's content without writing its ID, so 'filed only' is an upper bound on non-use, not proof of it.

## 4. Card quality

- **Corrections:** 33 CORRECTION cards against 228 (14%). By cause, from the titles: wrong date or day label (about 10); a negative or a quote taken from search summaries that the issuer's own page contradicted (about 8; MUFG leak, Kremlin declaration, Florida EO, Apollo pricing); figure or basis errors (about 6; RSXFS ex-autos, Brent January vs February, CoreWeave bond); owner upgrades a claim (about 9). The first two classes are already in MEMORY findings 12 and 34 and keep recurring.
- **confidence_language off vocabulary:** FORMAT_SPEC lists `confirmed / reports / assessed / unconfirmed`. 169 of 228 cards (74%) start with something else: free prose 124, 'titles only' 6, 'confirms' 4 (two of them tonight's 003 and 004), 'reported' 3, 'owner grades' 3, others. The free prose usually says more than the enum would; the field has become a caveat line, and no reader grades it.
- **Doorbell ledger gaps:** DOORBELL_LOG has no rows for SIG-W-20261124-001 to -019 (rows resume at 020). Tonight's 8 cards had none until this review; 15 rows were added at 2026-11-27 (L1-UNKNOWN or IN-FLIGHT; no DARK verdict, no doorbell owed). The 11/24 rows are not backfilled here: liveness at that time cannot be reconstructed honestly.

## 5. Options for Will (nothing is changed by this report)

1. **Collector date traps:** ask PROME (who owns Research-Intake) for a lane flag when an article's publication date is more than 7 days before collection. It is not a kill rule; WALTER still reads the title. Cost: one script change in a repository WALTER may not write.
2. **confidence_language:** either relax the spec to 'enum token first, then free text' (`reports: ...`), which most recent cards could meet, or retire the field's enum. Recommendation: the first; dispatch_card.py could check the leading token.
3. **Corrections:** no new rule (Will 10/31: fewer checkers). The existing practice (read the issuer's page before a negative) is the fix; the count is the measure for the next review.
4. **Desk use:** a 'filed only' rate of a third on ACTION cards is worth one question to PROME at its next desk sweep for SAM, SHADE and BRENT: are those cards useful, or should they be INFO?
5. **Doorbell ledger:** keep writing rows at dispatch; dispatch_card.py could prompt for them. No backfill of 11/24.

Next review: after about 200 more cards or 30 days, whichever comes first.

## Addendum 2026-11-27 (written before 12:40 ET): outside check, and what changes in this report

An outside read-only check (file given by Will 2026-11-27 12:30 ET, `/mnt/c/Users/willi/Downloads/2026-11-27_walter-filter-review-check.md`, checked at 43e486b781) reproduced every count above and found five weaknesses. WALTER accepts all five:

1. **Misses were not tested.** The kill log's 37 rows are 37 of 96 KILL dispositions in BATCH_MANIFEST for 11/12 to 11/26 (others live as kills lines inside cards), and none of the 815 NO-ACTION title-skim items or 384 FOLDs were sampled. 'No false-positive kill' holds only for what was looked at; this review cannot say the filter drops nothing it should keep. The outside check sampled 7 kills, all correct.
2. **The use measure ignored the desks' own reading logs.** Every recipient keeps `board_log.tsv` with a disposition column (HENRY proposed exactly this measure on 11/17, `inbox/processed/2026-11-17_from-HENRY_routing-use-measure-outside-audit.md`). Combining it with ID citation, 36 of 210 ACTION deliveries (17%) show no sign of use, not 33%. SAM's log says acted 4 of 5, SHADE 2 of 3, BRENT 4 of 8 (one SAM case checked at its STATUS_REFERENCE line 53). The desks with most ACTION cards logged only 'noted' or 'info-only' are VULCAN 8, BRENT 4, FALCON 3, LIQUID 2. **Option 4 above is re-aimed at those, not at SAM and SHADE.**
3. **The correction rate has not improved** since the 11/17 to 11/18 outside baselines (cards later corrected: 9.3% Aug to Oct, 13.6% Nov 1 to 11, 18.6% Nov 12 to 17, 15.2% Nov 18 to 26 and may rise). Wrong weekdays went to 0 of 158 cards after the dispatch_card.py refusal of 11/17; search-summary negatives, handled only by a written practice, recurred 5 times (20261119-014, -015; 20261120-010; 20261123-012; 20261124-021).
4. **Option 1 would not have caught the old items that became corrections:** they came with fresh dates. It saves reading time; it should not be expected to move the correction rate.
5. **Not reported above:** DOORBELL_LOG has no rows dated 11/7 to 11/22 (last 11/6), not only the 11/24 gap; 6 INFO cards went to retired YEYOU and dormant BARON (all unread); the treasury_auctions feed has failed since at least 11/14 (the feed that raises weak-auction ACTION to BOND); SIG-W-20261116-005 item 1 (SoftBank $11B) was the September deal, flagged by SAM 11/25 and uncorrected.

**Done by WALTER on 11/27 (own lane):** correction SIG-W-20261127-001 (SoftBank), with R1 COR-20261127-01 and the banner on 20261116-005; dispatch_card.py now refuses YEYOU and BARON (existing NEVER_ROUTE list; tests pass, a negative control refused). **Not done:** a misses sample (the 815 titles live in the collector repository; a sample belongs in the 12/14 WQ-684 review if Will wants it); the 11/7 to 11/22 doorbell rows (liveness then cannot be reconstructed honestly).
**Option 2 recommendation withdrawn:** no live script reads `confidence_language`; edit the spec to match practice (token first as a writing habit, or free text), no check.
