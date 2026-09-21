# CRUISE — September 20 evidence and registration review

**Reviewer:** CATO, dedicated CRUISE-only session. **Date:** 2026-09-20, approximately 10:56–11:05 EDT. **Disposition:** review delivered; corrections proposed, none implemented.

**Assignment boundary:** Will requested CRUISE only, a uniquely named report under CATO `runs/`, no CONTINUITY or owner-file edits, and no Git mutations. Other CATO sessions' assignments and approvals are separate. The coordinating CATO integrates this report. No owner messages, registrations, grade changes, trade actions or policy changes were performed or authorized here.

**Snapshot:** initial HEAD `787f1df16f89bedeee4f7ee699064bc07b116224`; principal research commit `815bc120f`; CRU-09 registration/definition commit `6639cbfa8`. Shared HEAD moved during review. Twelve inspected CRUISE surfaces were byte-compared with the initial snapshot and still matched at the evidence check; manifest below. Other sessions' pending CATO files were preserved. This is a context-aware review of owner implementation, not a blind cold read or certification of other sessions' approvals.

## Assessment

Useful new evidence exists: the NCL promotion is real, most capacity arithmetic reproduces, and separating company disclosure from causal evidence remains the right design. However, the latest research repeatedly converts an aggregate outcome or an observed financing choice into a claim about its cause. The three most consequential defects are the new CRU-10 causal interpretation, the denial example in CRU-09's frozen definition, and the claim that Truist's Carnival target increase disproves the Norwegian transmission story. Those should be reconciled before these records guide the September 29 assessment.

Eight findings follow. Severity refers to reliability of the research/decision record, not an instruction to trade. Source checks support the stated narrower corrections; they do not establish that Norwegian contagion either exists or does not exist.

## F1 — HIGH: CRU-10 reinstates the aggregate-yield causal test that CRU-09 explicitly retired

**Locations:** `AGENTS/CRUISE/workbook/PREDICTIONS.tsv:11` (entire CRU-10 row); STATUS opening item 7; TRADE opening CRU-10 bullet; `domain/sources/2026-09-20_the-discounting-event-found-at-primary.md:81`; KB-CRU-092/104; `CADENCE.md` trigger 8.

CRU-10 predicts a Q3 constant-currency net-yield result at/above the company's approximate 1.2% guide, then equates that result with Norwegian's sale not denting Carnival's realized yields. Its Notes simultaneously say it grades the contagion limb and that it measures only the level, without attributing cause. The last sentence assigns attribution to CRU-09, even though CRU-09 deliberately permits competitors other than Norwegian. The contradiction is operative in both live summaries.

The 1.2% guide is real: [Carnival's June 23 Q2 release, guidance table, PDF page 4](https://www.carnivalcorp.com/wp-content/uploads/2026/03/2026-2Q-Earnings-Release-Final-Draft.pdf). A good benchmark does not make the causal claim identified.

**Reviewer counterexamples, illustrative rather than estimated effects:**

| Actual mechanism | Reported Q3 CC yield growth | CRU-10 numeric result | What it cannot establish |
|---|---:|---|---|
| Other improvements produce 1.8%; Norwegian subtracts 0.6 percentage points | 1.2% | Meets benchmark | Norwegian did not hurt CCL |
| No Norwegian effect; an unrelated deployment drag subtracts 0.6 points from 1.2% | 0.6% | Misses benchmark | Norwegian hurt CCL |

Likewise, RCL reporting higher realized pricing does not prove an adverse competitive effect was absent; pricing can improve while falling short of the counterfactual. It cannot date the channel's onset to July 1. A July **booking** promotion also does not establish the affected **sailing/revenue** cohort: the owner describes eligibility through 2027 and analyst concern about fall/winter sailings. Q3 exposure is possible, not proven to be the first or decisive observation.

The same defect appears in the newly operative port trigger: hitting approximately 9M passengers alongside a CCL yield-guide cut cannot confirm Norwegian discounting, and missing passenger budget alongside falling yields cannot separate discounting from demand destruction. More capacity and an unrelated geographic yield drag reproduce the first outcome; price cuts and weaker demand can coexist in the second. The source paper correctly names a missing capacity denominator, then its conclusion and cadence rule bypass it.

**Bounded correction:** preserve CRU-10's original registration/history and numerical forecast, but explicitly withdraw its causal interpretation through the owner's correction process. Do not silently rewrite its 60% or terms. Keep CRU-09 as a disclosure forecast and require Norwegian-specific evidence for the channel. Treat port counts as contextual volume evidence until cohort, capacity, itinerary and pricing comparisons exist. No replacement instrument or registration is authorized by this review.

## F2 — HIGH: CRU-09's frozen worked example confirms a denial of the forecasted effect

**Locations:** `domain/2026-09-19_DRAFT_FL-CRU-10_identifying_test.md:142` (§9a); §4a/4b/4c; `workbook/PREDICTIONS.tsv:10`. The live definition is byte-identical to the file at registration commit `6639cbfa8`.

Section 9a maps “Norwegian named and explicitly excluded as a cause” to **CRU-09 CONFIRMED**, explaining that a qualifying attribution was made. But the forecast requires management to attribute pricing/yield **pressure** to competitors' promotional behavior. A denial alone does not meet that predicate.

**Counterexample:** complete release, prepared remarks and Q&A; management states, “Norwegian's promotions did not affect our Q4 Caribbean pricing, and competitors' promotions caused no pressure elsewhere either”; there is no other qualifying statement. The registered positive predicate yields **FAILED**, while the example yields **CONFIRMED**. Norwegian-specific contrary evidence can affect the qualitative channel without confirming the disclosure forecast. If management separately attributes qualifying pressure to MSC, that separate affirmative statement can confirm CRU-09; the Norwegian denial itself cannot.

There are related incomplete repairs: §4c's alternative “or behaviour described that is uniquely Norwegian's” does not expressly carry affirmative causal attribution; §9d still says no CONTRADICTED channel state exists; the header says both REGISTERED and NOT REGISTERED. The principal denial row in §4c is improved relative to v3, but propagation into the disclosure examples is wrong.

**Bounded correction:** record the contradiction and an explicit authoritative clarification before grading, preserving the frozen record and using the owner's applicable registration-change rules. Do not silently edit the historic definition or treat CATO's earlier v3 support as certification of this subsequently added example. Test denial-only, denial-plus-other-competitor pressure, and an affirmative Norwegian attribution with improving aggregate prices separately. This session makes no approval or grade ruling.

## F3 — HIGH: the Truist target increase is assigned a causal meaning contradicted by the cited coverage

**Locations:** discounting paper §4 (`:52`); KB-CRU-103; STATUS opening item 2 and conclusion; TRADE opening assessment; FLOW FL-CRU-10; CRU-10 confidence rationale.

The desk argues that Truist could not have raised Carnival's target if it believed Norwegian was capping Carnival's yields, then treats this as its strongest contrary transmission evidence. But the cited [Investing.com coverage, updated July 23](https://m.investing.com/news/stock-market-news/truist-cuts-norwegian-cruise-line-to-hold-on-rising-promotional-activity-4809481?ampMode=1) attributes the target increase to **lower fuel and depreciation assumptions**. Cost offsets can lift valuation despite a yield drag. The article also describes wider mass-market yield pressure. Therefore the target move does not identify Truist's view of the Norwegian-to-Carnival effect. I checked the coverage, not Truist's proprietary note.

**Corroboration limit:** [Yahoo's copy](https://finance.yahoo.com/markets/stocks/articles/truist-cuts-norwegian-cruise-line-153936656.html) carries the same Sam Boughedda/Investing.com attribution; these are not two independent reporting sources. Truist is an additional analyst voice, but its earlier publication cannot prove that later banks used independent inputs.

**Bounded correction:** keep the dated target change, restore its reported rationale, and withdraw the asserted causal verdict and the claim that two outlet copies independently corroborate it. The channel remains unresolved on this evidence. Reassess the prose rationale supporting the forecast without retroactively tuning its probability. This finding neither strengthens nor weakens a trade recommendation by itself.

## F4 — MEDIUM: the promotion is verified, but its $280 example and baseline are misread

**Locations:** discounting paper §§1–2/5; KB-CRU-100/101; STATUS opening item 1 and conclusion; TRADE promotional-discount bullet; FLOW FL-CRU-10.

[NCL's July 8 release](https://www.ncl.com/fr/fr/newsroom/norwegian-cruise-line-launches-first-ever-semi-annual-sale-with-50-off-all-cruises-plus-free-pre-paid-gratuities-on-select-sailings/) confirms the promotion. Its $280 example is **added gratuity savings**; the footnote specifies the qualifying category and $20/person/day. Thus 2 × 7 × $20 = $280. It does not establish that total savings were only 10–15%, nor disprove the advertised fare discount. The report itself admits there is no measured fare denominator.

The assertion that the announcement is “self-baselining” is also unsupported. [NCL's June 23 release](https://es.ncl.com/newsroom/get-away-without-going-far-away-with-norwegian-cruise-line-and-new-unbeatable-summer-deals-for-close-to-home-voyages/) already advertised the same 50%-off headline, including Caribbean/Bahamas voyages. The July name and gratuity offer are evidence of a promotion, not a matched measurement of a new fare reduction or its regional concentration.

**Bounded correction:** keep “promotion confirmed; realized price change and incremental generosity unmeasured.” Remove the unsupported 10–15% replacement figure, second-guest speculation and proof-of-new-price-cut wording. The analyst's aggressiveness assessment remains attributed judgment. Do not upgrade Caribbean concentration from a worldwide campaign without additional evidence.

## F5 — MEDIUM: a December share issuance is treated as a new offset to a June forecast denominator

**Locations:** capacity paper §6(a), `:69–71`; KB-CRU-097; STATUS opening item 6/conclusion; TRADE share-count bullet and repurchase catalyst; CRU-08's existing fixed-denominator definition.

[Carnival's Q2 10-Q, PDF page 13](https://www.carnivalcorp.com/wp-content/uploads/2026/03/2026-2Q-10-Q.pdf) verifies the **December 2025** 69.1M-share issuance. The [June 23 Q3 guidance table](https://www.carnivalcorp.com/wp-content/uploads/2026/03/2026-2Q-Earnings-Release-Final-Draft.pdf) subsequently supplies the 1,377M adjusted diluted-share denominator used by CRU-08. An already completed issuance is part of that later starting share base, not a newly discovered adverse increment to add against future repurchases. The desk has supplied no evidence that the June guide omitted those shares.

The earlier 30M-repurchase calculation is a **scenario**, not evidence of 30M actual Jun–Aug retirements. End-period shares and quarter-weighted diluted shares also differ: timing matters, and a repurchase spread through the quarter does not receive a full quarter's weighting.

**Bounded correction:** distinguish the December historical stock-flow bridge from guide-to-actual Q3 weighted-share changes. Withdraw “2.3× bigger and opposite” as a demonstrated CRU-08 confound. Reconcile actual repurchase timing and other changes to the guide when available. Preserve CRU-08's frozen arithmetic; do not substitute an improvised denominator. Fuel-attributable arithmetic remains distinct from an EPS beat/miss.

## F6 — MEDIUM: capacity arithmetic reproduces, but the occupancy and causal headlines do not

**Locations:** capacity paper §§1–4, notably `:26/30`; KB-CRU-094/095/096/099; STATUS opening items 3–4 and conclusion; FLOW FL-CRU-10.

Using [NCLH's Q2 10-Q statistical table](https://www.sec.gov/Archives/edgar/data/1513761/000110465926089657/nclh-20260630x10q.htm), I reproduce capacity growth **8.8804%**, occupancy change **−1.5375pp**, and the derived Q1 YoY occupancy change **+2.2579pp**. But NCLH passenger cruise days rose **7.2693%**, and passengers carried rose **22.7520%**. The summary's “fewer people” is not an absolute-volume result.

[RCL's Q2 statistics](https://www.rclinvestor.com/content/uploads/2026/07/Royal-Caribbean-Group-Reports-Second-Quarter-Results-Above-Expectations-and-Raises-Full-Year-Guidance.pdf) show occupancy declining from 110.3% to 110.2% (about −0.079pp from unrounded passenger-day/capacity inputs). Therefore NCLH is not literally the **only** operator losing occupancy; it has the much larger decline. The desk's own table already shows this.

The 3.80pp number is a deterioration in the **YoY occupancy change**, not a 3.80-point sequential fall in occupancy. Rounded actual Q1→Q2 occupancy falls roughly 1.41 points. Growing capacity faster than passenger days is consistent with weaker utilization, but these company-wide figures do not identify why capacity expanded, why occupancy changed, a Caribbean-specific price response, or a single available management lever. Changing brand/itinerary mix can affect YoY deltas too; using deltas alone does not remove composition effects.

**Bounded correction:** retain the reproduced arithmetic, label the measures precisely, replace “only” with the relative magnitude, and call supply pressure a plausible explanation rather than a measured cause. Preserve the useful caution against treating all NCLH weakness as evidence of broad household stress.

## F7 — MEDIUM: the port-data search limit is promoted into a universal publication absence

**Locations:** port paper §1 (`:9/19`) and §4; CADENCE trigger 8; STATUS port-data gap.

The paper says no Florida port publishes monthly cruise passenger data, labels all three ports annual-only, and states further searching cannot produce an unpublished series. Its own evidence is a set of pages searched and an agenda-title inspection.

There is a concrete counterexample to the **annual-only** characterization: [Port Canaveral's April 24, 2025 announcement](https://www.portcanaveral.com/media-center/latest-news/blog/2025/04/24/port-canaveral-sets-new-single-month-record-for-cruise-guests) reports **925,994 passenger movements in March 2025**, with a March-on-March comparison. This proves publication of monthly observations; it does **not** prove that a complete, current FY2026 monthly series is readily downloadable. I did not establish that stronger result. Search also surfaced historical port financial-report attachments with monthly passenger counts, but a complete current attachment census was not performed.

**Bounded correction:** say a usable continuous current series was not found in the inspected sources; distinguish historical monthly observations from current coverage. Keep board financial-report contents as an unresolved route rather than declaring them absent from agenda headings. The annual catalyst can remain useful, but the categorical no-search instruction and the claim that annual data are necessarily the first physical observation are unsupported. Its causal grading defect is covered in F1, not closed by finding more data.

## F8 — MEDIUM: liquidity ratios and financing observations are overextended into access and credit-repricing verdicts

**Locations:** capital-access paper §§1–4 and “What this changes” (`:28/42/89`); KB-CRU-089/090/091; STATUS opening item 5/conclusion; TRADE credit-stress bullet.

Three inferences exceed the evidence the desk supplies:

1. **No observed NCLH bond issue in a window → no bond-market access / cannot borrow unsecured at all.** A financing choice or absence of issuance does not show that an issuer was refused funding or could not issue at a price. Its historical [2025 unsecured financing announcement filed with the SEC](https://www.sec.gov/Archives/edgar/data/1513761/000141057825002024/tm2525857d1_ex99-1.htm) also prevents treating inability as a timeless fact. This review does not certify September 2026 access or pricing.
2. **RCL August issuance → explanation of September equity weakness.** Successful funding is evidence about access at issuance, not proof that later equity weakness excludes credit risk. August 6 pricing is about six weeks before September 18, not the two weeks stated in the headline. The paper acknowledges the stale vintage elsewhere.
3. **A lower new-bond coupon/yield than old stated coupons → credit spreads improved.** Coupons on older issues are not their current yields or matched Treasury spreads. This comparison cannot establish a credit re-rating; the desk itself says current secondary spreads were not obtained.

The reported liquidity ratios reproduce **from the desk's displayed inputs**: 6,900/22,836 = 30.2154%; 6,700/25,570 = 26.2026%; 1,500/15,034.8 = 9.9769%. That does not standardize “gross debt”: KB-CRU-090 explicitly leaves the NCLH carrying/principal difference unreconciled, and as-of dates differ. Retain them as dated liquidity-to-stated-debt comparisons, not measures of marginal access or a demonstrated consumer K-shape. RCL has the weakest cited one-week equity return; the credit ranking alone cannot identify the cause of that return.

**Bounded correction:** retain dated transaction evidence and qualified ratios, replace access impossibility with the observed financing facts, and withdraw the coupon comparison's spread verdict. No live bond-pricing collection or replacement credit study is assigned here.

## Verified progress and remaining limits

- CRU-09 now exists at 25%, with a freeze deadline, grading cutoff and a recoverable registration revision. The owner records Will's approval; this session neither independently reconstructs that exchange nor borrows its authority. The positive disclosure predicate remains usefully separated from Norwegian-specific attribution. F2 identifies a defect in its frozen examples, not an absence of registration.
- The earlier live TRADE Caribbean catalyst now says a Q4 yield number does not settle the channel. That correction is present; CRU-10 introduces a new contradictory path, rather than the old sentence remaining wholly untouched.
- The promotion, dated share issuance, guide benchmark and sampled operating statistics were checked against issuer primaries. Truist was checked at the cited secondary coverage; the proprietary note was not obtained. The promotion's actual matched fares, regional realized price impact, full SEC filing census, market quotes and full credit-access ladder were not independently certified.
- The NCLH funding model's cash-flow timing, financing availability and minimum-reserve limitations remain unresolved from the earlier review. This pass did not re-model them. Current STATUS's header and KB-CRU-093 still call R7 discharged; TRADE still calls annual OCF the single number deciding the window and retains an already-spent funding-gap exit. Those are known carries, not independently closed by rechecking one settlement obligation.
- No confidence percentages, prediction grades, vector scores or trade convictions were changed. The numerical reproduction below is reviewer checking, not a software test suite or proof of causal identification. No implementation was undertaken; independent review of any eventual correction remains for its assigned reviewer.

## Reproduction and snapshot receipt

Read-only Python arithmetic, run September 20, used these disclosed or owner-displayed inputs:

```text
NCLH Q2 capacity: (6,589,740 / 6,052,273 - 1) * 100 = 8.880416%
NCLH Q2 passenger days: (6,745,954 / 6,288,800 - 1) * 100 = 7.269336%
NCLH Q2 occupancy delta: 100*(6,745,954/6,589,740 - 6,288,800/6,052,273) = -1.537505pp
NCLH Q1 derived numerator/denominator: subtract Q2 from H1 for each year
H1 passenger days: 13,380,480 / 12,076,043; H1 capacity: 12,982,709 / 11,752,836
Derived Q1 YoY occupancy delta = +2.257928pp
RCL Q2 capacity: (13,572,396 / 12,942,385 - 1) * 100 = 4.867812%
RCL Q2 occupancy delta: 100*(14,962,211/13,572,396 - 14,277,894/12,942,385) = -0.078866pp
CCL capacity growth from owner's rounded inputs: (24.7/24.2 - 1)*100 = 2.066116%
```

Snapshot path prefixes below are `AGENTS/CRUISE/`. SHA-256 prefixes identify the inspected bytes at `787f1df16`; all twelve matched the live files at the evidence check. Git history also established that the CRU-09 definition at `6639cbfa8` was identical to this snapshot.

| Path | SHA-256 prefix |
|---|---|
| STATUS.md | 002fd0d10f6134c6 |
| TRADE.md | 3b445d72e19dd098 |
| CADENCE.md | f567b99886d64543 |
| workbook/KB.tsv | ebf55e3a42cccf6a |
| workbook/PREDICTIONS.tsv | 99f2f77a1b8b54fc |
| workbook/FLOW.tsv | a9bd069bb37d5e40 |
| workbook/VX.tsv | fbae0ca090cfa18e |
| domain/2026-09-19_DRAFT_FL-CRU-10_identifying_test.md | 129a95e84332b5c8 |
| domain/sources/2026-09-20_capacity-vs-occupancy-the-mechanism-measured.md | 7534d61b46980b7d |
| domain/sources/2026-09-20_the-discounting-event-found-at-primary.md | a47d014594f915b3 |
| domain/sources/2026-09-20_capital-access-ladder-rcl-ccl-nclh.md | d960408c25ada965 |
| domain/sources/2026-09-20_florida-port-volumes-access-and-catalyst.md | f1db515ae634a6f7 |

**Delivery:** this report is the only file authored by this session. Left uncommitted for the coordinating CATO, as Will instructed. No Git mutation, CONTINUITY update or owner edit. Suggested integration order: F1/F2 grading semantics, F3 source-based correction, then the remaining evidence qualifications. Further work requires its own assignment; this report does not inherit another session's repair or communication approval.
