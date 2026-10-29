# WQ-515 batch 1: source versus recipient information fidelity, ten prospective transfers

*Saved verbatim by PROME (prome-92) from the independent Sonnet reader's returned text, 2026-10-28 20:4x ET. The reader's Write tool refused the report file ("Subagents should return findings as text"); it wrote SOURCE_INVENTORY.md and provenance.tsv in this directory before that refusal. PROME changed no number or word below.*

**Method:** `AGENTS/DEWEY/output/2026-10-25_wq515-information-fidelity-method.md`, applied unchanged. **Sample:** `AGENTS/WALTER/research/2026-10-26_WQ515/transfers.tsv`. **Clock reads:** 2026-10-28 20:40:59 to 20:44:37 EDT, all from `date`.

**Summary**
1. Assessable transfers: 6 / 10. BROCK (positions 1 and 2), HANS (position 8) and SAM (position 9) have no record.
2. Caveats assessed: 8 / 17.
3. Weighted retention: 92.5% (18.5 / 20 weight assessed, out of 42 total).
4. Severity-3 losses: 0. Three severity-3 caveats were assessable, and all three were retained.
5. Slope: computable, -8.33 percentage points per additional handoff. That is 6 transfers, 12 observations, hops 1 to 2. It rests entirely on one judgment call (position 6, FALCON) and should not be read as a trend.

## 1. Sample and provenance

All 30 source, BOARD and handoff hashes match `transfers.tsv`. Six handoff packets (positions 3, 4, 5, 6, 7 and 10) have since moved to `inbox/WALTER/processed/`; the bytes at the new paths match. Eight transfers share one whole-file source hash (`e63e3002...`) for the morning SOURCE-CHECKS.md. Each transfer's frozen source is its section of that file, which holds one qualifying quote plus a locator.

| Pos | Signal | Dispatched UTC | ACTION owner | Co-owners | Class |
|---|---|---|---|---|---|
| 1 | SIG-W-20261026-001 | 10-26 16:40:23 | BROCK | LIQUID | contingent/current |
| 2 | -002 | 10-26 16:40:23 | BROCK | none | contingent/current |
| 3 | -003 | 10-26 16:40:23 | VULCAN | none | contingent/current |
| 4 | -005 | 10-26 16:40:23 | LABOR | none | contingent/current |
| 5 | -006 | 10-26 16:40:23 | BRENT | none | contingent/current |
| 6 | -007 | 10-26 16:40:23 | FALCON | none | contingent/current |
| 7 | -009 | 10-26 16:43:36 | ISHM | CARL | inference/measurement |
| 8 | -010 | 10-26 16:43:36 | HANS | none | inference/measurement |
| 9 | -012 | 10-26 17:49:26 | SAM | LIQUID, HENRY | inference/measurement |
| 10 | SIG-W-20261027-001 | 10-27 00:38:30 | CARL | none | inference/measurement |

The chain for each transfer is source -> WALTER BOARD card (hop 1) -> ACTION owner's own record (hop 2). The owner's inbox copy of the handoff is not a destination record.

**Destination records.** All reads were 2026-10-28, 20:42 to 20:43 EDT, which is after every 24-hour hold. Every record used is committed and the tree was clean.

| Pos | Owner | Record used | Commit |
|---|---|---|---|
| 1, 2 | BROCK | none found | n/a |
| 3 | VULCAN | `AGENTS/VULCAN/workbook/KB.tsv` KB-VULCAN-292 and 297; `board_log.tsv` | 03ed29ec0 and 594ff5c39 |
| 4 | LABOR | `AGENTS/LABOR/workbook/KB.tsv` KB-LAB-224 | 634928ebf |
| 5 | BRENT | `AGENTS/BRENT/research/2026-10-26_energy-review/REPORT.md` section 4 (sha 0df6c120...) | 113332181 |
| 6 | FALCON | `AGENTS/FALCON/reports/2026-10-26_saudi-claims-and-L807.md` (sha c2710acb...) | 35bd7d149 |
| 7 | ISHM | `AGENTS/ISHM/workbook/KB.tsv` KB-ISH-007, `AGENTS/ISHM/workbook/PRINTS.tsv` DALLAS row, `STATUS.md` | 0dbba244d (PRINTS b606ab70e) |
| 8 | HANS | none found | n/a |
| 9 | SAM | none found | n/a |
| 10 | CARL | `AGENTS/CARL/research/2026-10-26_L786/RECEIPT_RECONCILIATION.md` row 20261027-001 (sha 4fd59eec...) | 5b18d5a88 |

How the "none found" rows were established (SEARCH-NOT-FOUND, checked in the owner-declared paths: `board_log`, `STATUS`, KB, `SCRATCH`, `NEXUS_BRIEF`, `research`, `reports`):
- **BROCK:** its last own commit and last `board_log` and KB change are 2026-10-25 (84e7a03c1). Signals 001 and 002 are still unprocessed in `inbox/WALTER/`.
- **HANS:** its last own commit is 2026-10-22. Signal 010 is unprocessed in its inbox.
- **SAM:** its last own commit is 2026-10-20. The only Brazil hit is a CYPHER inbox file.

## 2. Frozen source inventory

The inventory is in `SOURCE_INVENTORY.md`. It lists 17 caveats: 6 at severity 3 (weight 4), 7 at severity 2 (weight 2), 4 at severity 1 (weight 1) and none at 0. Total weight is 42.

Because the frozen sources are single quotes, most transfers carry only one or two inventoried caveats. I did not re-fetch the issuer pages, so any caveat a fuller source would carry is not inventoried.

| Pos | Caveats (severity) |
|---|---|
| 1 | C1 no agreement for the broader program (3) |
| 2 | C1 lease subject to closing conditions (3) |
| 3 | C1 amount raised uncertain (2) |
| 4 | C1 voluntary, time-limited program (3) |
| 5 | C1 regulatory approvals pending (3) |
| 6 | C1 meeting date unspecified (2); C2 earlier report, later AP updates status (1) |
| 7 | C1 diffusion index is net breadth, not magnitude (2) |
| 8 | C1 weak hard data vs stronger surveys (2); C2 full analysis subscriber-only (1) |
| 9 | C1 cannot identify or rule out specific yen-funded losses (3); C2 ETF prices are not OAS or financing proof (2); C3 EMB contains Brazil (2); C4 no BRL/JPY funding return or carry probability graded (2); C5 SAM view dated Oct 20 (1) |
| 10 | C1 completed historical deal, not evidence of current access (3); C2 only the date correction is resolved (1) |

## 3. Six-field comparisons

Field grades are 1 (preserved), 0.5 (partly) and 0 (lost). UNKNOWN means the evidence is unavailable.

**Pos 3, VULCAN. Adopted with qualification.**
- **Finding (1):** card "Anthropic publicly files for its IPO"; KB-292 "Public filing status only".
- **Evidence (1):** VULCAN retrieved the primary S-1 itself ("retrieved directly: IPO not effective/priced", KB-297). This is an upgrade with a stated basis, not a loss.
- **C1 (1):** source "amount ... ultimately raises remains uncertain"; card "Offering price, proceeds and valuation are not final"; KB-297 "Price, share count, proceeds and IPO date unset".
- **Confidence (1):** card "reports" at 0.8; KB-292 PROVISIONAL, KB-297 EMPIRICAL.
- **Conditions (1):** IPO not effective or priced.
- **Implication (1):** "No IPO proceeds, final valuation, cash runway ... established".

**Pos 4, LABOR. Adopted.**
- All six fields are 1.
- **C1:** source "time-limited, voluntary program"; card "time-limited voluntary exit offer"; KB-LAB-224 "offers and eligibility are not exits".
- **Evidence:** "~60,000 ELIGIBLE per secondary coverage, unverified, NOT a departure count".
- **Implication:** "Moves no score ... v5 stays 4".

**Pos 5, BRENT. Adopted with qualification.**
- All six fields are 1.
- **C1:** source "subject to the receipt of required regulatory approvals"; card "conditional on shareholder/regulatory approvals"; report "conditional on required regulatory approvals/clearances ... Announced is not closed."
- BRENT read the EQT page and the Range PDF directly, and added the sub-$2 breakeven and NGL-equivalence limits.
- **Evidence:** "COMBINED enterprise value, not the price paid solely for Range".

**Pos 6, FALCON. Adopted with qualification. This is the only imperfect transfer.**
- **Finding (1):** "Tehran regional delegations ... are separate evidence".
- **Evidence (0.5):** "The handoff AP locator is malformed; independent Reuters material and Oman primary checks supply limited cross-checks". The AFP/TBS origin is not named.
- **C1 (0.5):** the card says "earlier AFP wording had no meeting date, so that earlier wording is not proof the meeting had occurred". FALCON states the delegations as present without that qualifier.
- **C2 (0.5):** the card relays that the later AP report supplies the in-person update. FALCON mentions the AP locator but not the earlier-report staleness.
- **Confidence (1):** "limited cross-checks, not a repaired AP attribution".
- **Conditions (0.5):** timing is not carried.
- **Implication (1):** "Mediation is not an executed settlement, a permanent corridor agreement, demining, restored cover or restored shipping".
- **Judgment call:** I graded C1 at 0.5 because decision-relevant protection survives. The C1 qualifier concerned an earlier report that the later AP update, which the source's own C2 names, overtook. Section 6 gives the sensitivity.

**Pos 7, ISHM. Adopted.**
- All six fields are 1.
- **Finding:** identical figures in PRINTS and KB-ISH-007.
- **C1:** source "subtracting the percentage ... reporting a decrease from the percentage reporting an increase"; card "diffusion indexes, not percent output changes or national measured production"; PRINTS "Positive indexes indicate slower expansion, not falling measured output"; STATUS "No synthetic national output average".
- **Evidence:** 64 of 114 respondents is preserved.

**Pos 10, CARL. Adopted.**
- All six fields are 1.
- **Finding:** "EART 2026-4 closed August 31; August 28 is filing history."
- **C1:** "No uninterrupted current funding claim." The `board_log` also says "historical issuance does not certify current financing access".
- **C2:** "Selected pricing and Ally source questions ... remain outside this correction."
- CARL's earlier "deferred" `board_log` rows were superseded by "acted" at 2026-10-27T02:37:39Z.

**Pos 1, 2, 8, 9: hop 1 only.** Hop 2 is UNKNOWN because there is no owner record.

| Pos | Card evidence | Caveat grades at the card |
|---|---|---|
| 1 | "no agreement ... not $95B cash raised" | C1 = 1 |
| 2 | "Entry remains conditional ... not proof of cash drawn" | C1 = 1 |
| 8 | Capital Economics "cautions that weak hard data do not match stronger surveys"; "full analysis is subscriber-only" | C1 = 1, C2 = 1 |
| 9 | "does not establish a broad yen-funding unwind ... Unsupported is not disproved" | C1 = 1, C2 = 0.5, C3 = 0, C4 = 0.5, C5 = 0 |

For position 9, the card's evidence is Brazil Journal plus WALTER's own vendor snapshot, not the LIQUID paragraph the TSV names as source. I graded hop 1 against the LIQUID paragraph, as the method requires. Hop-1 weighted retention is 6/11, about 54.5%, and is descriptive only.

## 4. Dispositions

| Pos | Owner | Disposition |
|---|---|---|
| 1, 2 | BROCK | no record found |
| 3 | VULCAN | adopted with qualification |
| 4 | LABOR | adopted |
| 5 | BRENT | adopted with qualification |
| 6 | FALCON | adopted with qualification (one partial caveat) |
| 7 | ISHM | adopted |
| 8 | HANS | no record found |
| 9 | SAM | no record found |
| 10 | CARL | adopted |

Nothing was declined with a reason, and nothing was deferred among the assessable six.

## 5. Weights and retention (assessable caveats, last record)

| Pos | Caveat | Severity | w | Hop 1 r | Last r | w x r |
|---|---|---|---|---|---|---|
| 3 | C1 | 2 | 2 | 1 | 1 | 2 |
| 4 | C1 | 3 | 4 | 1 | 1 | 4 |
| 5 | C1 | 3 | 4 | 1 | 1 | 4 |
| 6 | C1 | 2 | 2 | 1 | 0.5 | 1 |
| 6 | C2 | 1 | 1 | 1 | 0.5 | 0.5 |
| 7 | C1 | 2 | 2 | 1 | 1 | 2 |
| 10 | C1 | 3 | 4 | 1 | 1 | 4 |
| 10 | C2 | 1 | 1 | 1 | 1 | 1 |
| | Total | | 20 | | | 18.5 |

## 6. Calculations

**Primary weighted end-to-end retention** = 100 × 18.5 / 20 = **92.5%**.
- Included: 6 transfers, 8 caveats, weight 20.
- Excluded: 4 transfers, 9 caveats, weight 22. By position that is 4 (pos 1), 4 (pos 2), 3 (pos 8) and 11 (pos 9).
- Assessed share of total weight is 20 / 42 = 47.6%.
- Missing records are counted neither as 100% retention nor as loss.

**Unweighted counts over 8 caveats:** fully retained 6, partly retained 2, lost 0.
- **Material (severity 2) losses:** none at 0. One partial: position 6 C1 at 0.5.
- **Reversal (severity 3) losses:** 0 of the 3 assessable severity-3 caveats (positions 4, 5 and 10). The other 3 severity-3 caveats (positions 1, 2 and 9) sit on unassessable transfers.

**Per-handoff slope.** Hop 1 (card) and hop 2 (owner record) are both observed with the same caveats for the six assessable transfers, so n_i = 2 for each. The four unassessable transfers have one observed hop and are excluded.

| Pos | R hop 1 | R hop 2 | Change |
|---|---|---|---|
| 3, 4, 5, 7, 10 | 1.000 | 1.000 | 0 |
| 6 | 1.000 | (2×0.5 + 1×0.5) / 3 = 0.500 | -0.500 |

- The source-to-card edge is 0 for all six.
- The only adjacent-edge changes are position 6 C1 and C2, each falling from 1 to 0.5. No restoration was observed.
- Arithmetic: each transfer has a squared-deviation sum of 0.5 and weight 0.5, so the denominator is 6 × 0.25 = 1.5. The numerator, from position 6 only, is 0.5 × [(-0.5)(0.25) + (0.5)(-0.25)] = -0.125.
- beta = -0.0833, which is **-8.33 percentage points per additional handoff** (6 transfers, 12 observations, hop range 1 to 2).
- Five of six slopes are exactly zero. The whole negative value comes from one transfer and one judgment call. Hop 1 is WALTER's own card, written for the caveat classes being sampled, so a flat 1.0 there is expected.

**Sensitivity (original scores stand):**

| Variant | Retention | Slope |
|---|---|---|
| Position 6 C1 = 1 and C2 = 1 | 100% | 0 |
| Position 6 C1 = 0 and C2 = 0.5 | 17.5 / 20 = 87.5% | -13.9 pp per handoff (R2 = 0.167) |
| Add secondary-owner branches, outside the primary metric | 23 / 27 = 85.2% | not recomputed |

The branch row adds three records:
- **LIQUID on position 1 (C1 = 1, w 4):** "planned ATM capacity/forward commitments are not proceeds" (`NEXUS_BRIEF` at 89cc2db06, sha a565c88e...).
- **ISHM on position 8 (C1 = 0, C2 = 0.5, w 2 and 1):** KB-ISH-013 says "remain sender secondary numbers ... LOG only" with no hard-data-versus-survey qualifier. ISHM is an INFO recipient and HANS is the ACTION owner, so the narrower handling may be a deliberate scope choice rather than a loss.
- **CARL on position 7:** "diffusion-index and composition caveats retained" (r = 1, same as ISHM); it is already counted in the 20 / 20 above.

LIQUID and HENRY have no record on position 9.

## 7. Missing and ambiguous cases

1. **Positions 1 and 2 (BROCK):** no BROCK record. VULCAN's packet to BROCK (594ff5c39) and VULCAN's own `board_log` rows are another desk's record, not BROCK's. Sample positions are retained.
2. **Positions 8 and 9:** HANS and SAM have been dark since 10-22 and 10-20. The position 9 source mismatch is described in section 3.
3. **Read timing:** VULCAN, BRENT, FALCON and CARL wrote their records within about an hour or a few hours of dispatch. I read them more than 24 hours after dispatch, as required.
4. **Source inventory depth:** caveats a fuller source would carry (Meta program size and dates, SpaceX closing conditions) are not inventoried, so their retention is unmeasured.
5. **Position 6 grading** is a judgment call (section 6).
6. **Severity 2 versus 3 on positions 3 and 7:** raising either to 3 would only raise the percentage, since both are fully retained.

## 8. Contrary evidence

- **Primary re-reads:** VULCAN, BRENT, CARL and LABOR fetched primary text themselves. High retention may reflect the owner re-reading the issuer, not preserving what WALTER sent. The metric cannot separate the two.
- **Hop 1 is self-graded by design:** WALTER wrote the cards knowing the sampled caveat classes. Hop-1 retention of 1.0 on all six assessable transfers gives the slope almost no variance.
- **Position 6 may be a later-source correction:** the later AP report overtook the earlier timing caveat, and FALCON's "delegations" may simply be correct. Graded at 1, retention would be 100%.
- **Missing records may be delayed integration:** BROCK, HANS and SAM had not processed the packets. Nothing shows they would have dropped the caveats.
- **No reasoned rejections** occurred in the assessable set.
- **Only active desks are measured:** 4 of 10 owners had no record, so the 92.5% describes only the six active desks.

## 9. Limitations

- There is one reader and no inter-rater check.
- Severity and partial-credit grades are subjective.
- The set is 6 assessable transfers and 8 caveats, with effectively one imperfect transfer. That supports no rate, no fleet statement and no p-value.
- Topic, owner activity and WALTER authoring the cards confound the comparison.
- The rubric was applied unchanged. The one ambiguity is shown as a labeled sensitivity, with original scores retained.
- The only files written were in `PROME/reports/2026-10-28_wq515-batch1/`.
