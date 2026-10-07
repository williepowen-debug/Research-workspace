# BOND — October 7 catch-up continuation

Written 2026-10-07T18:13:02.516363-04:00. Completes the two primary auction grades, September-meeting minutes synthesis and bounded VX-20/intake review left in the preserved 16:27 checkpoint. Independent dated FedWatch/OIS comparison remains unavailable. This is a research delivery, not session closeout.

## Decision relevance
The 10-year auction clears strongly while the long end still sells off. October 7 Treasury 30Y 5.67% rose 3bp on the day; 2Y 4.77% fell 2bp. The 3Y auction's weak indirect share is a rarity marker, with no OLD-conjunctive or cover failure. The Fed minutes preserve a conditional further-hike bias and distinguish stable funding from higher duration costs. No new mechanism confirmation or capital authorization follows.

WQ-357 LATER/path C to October 14 and WQ-280 NO-ADD stand. October 7 broker capture: TLT Oct-16 82P ×1, TBT 10 shares; exact capture time and Activity absent. The prior operational exit recommendation remains MET under WQ-291. Net inventory is not proof of warehousing; its funding window remains UNGRADED. Existing WQ-339 drafting only and WQ-360 fill unapproved remain separate. No new proposal or order.

## Auctions — primary, frozen two-decimal manual verdicts

TreasuryDirect fetched 2026-10-07T18:13:02.516363-04:00; raw responses, instrument fields, exact competitive-accepted denominators, cleaned benchmark pools and machine-readable calculations: `analysis/2026-10-07_catchup/raw/auction_grades.json` and `ta_ws_auctioned.json`. Shares below are percent of competitive accepted, not total issue including SOMA/noncompetitive.

| Test | October 6 3Y new, 91282CRQ6, $58B | October 7 10Y reopening, 91282CRF0, $39B |
|---|---:|---:|
| Competitive accepted | $56.9955375B | $38.665438B |
| High yield; BTC | 4.932%; 2.62 | 5.300%; 2.77 |
| Indirect / direct / dealer | 57.594842 / 31.664953 / 10.740205% | 80.338513 / 17.116578 / 2.544908% |
| Governing frozen I-prime | 58.90%; **FIRED**, margin −1.305158pp | 65.05%; NOT MET, +15.288513pp |
| Reopening-only alternate | N/A | 66.32%; NOT MET, +14.018513pp |
| OLD indirect <min AND dealer >max | 56.50 / 19.50; neither leg, margins +1.094842 / −8.759795pp | 63.95 / 13.38; neither leg, +16.388513 / −10.835092pp |
| Cover below frozen minimum | 2.54; NOT MET, +0.08 | 2.39; NOT MET, +0.38 |
| Downgrade test: indirect ≥median AND dealer ≤median | Medians 62.959175 / 11.338725; indirect fails | Medians 69.941473 / 9.278966; both pass |

Downgrade counter: prior 0 → 0 after 3Y → **1 after 10Y**. Three consecutive qualifying nominal coupons are required; no downgrade today. Composite remains **17/35 = 5+4+2+3+1+1+1**. Row 2 remains 4: the new 3Y marker has no confirmed non-auction mechanism leg, so it does not satisfy the second-paired-failure upgrade. 10Y cover exceeds its prior-12 maximum 2.71; that is a defined-window comparison, not an all-time record. Auction indirect includes custodial bidding and is not a direct foreign-official holdings measure.

Governing bars are the October 1 frozen snapshot in AUCTION_HEALTH.md, strict comparisons, equality never fires. Recomputed P15 audit: 3Y 58.898473, 10Y 65.050319; both agree with frozen-bar verdicts outside the tie band. System Python lacked numpy and printed a misleading final CLEAN after an explicit missing-I-prime warning; that line was rejected. The saved venv research calculation includes numpy and separately applies the frozen 2dp bars. The standing grader tie-band defect remains unrepaired. No tails measured or graded.

## Rates and credit — separate publication frontiers

Official [Treasury nominal](https://home.treasury.gov/resource-center-data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026) and real curves now include October 7. 2Y/5Y/10Y/20Y/30Y = 4.77/5.03/5.28/5.71/5.67%; daily moves −2/0/+1/+3/+3bp. 2s10s = 51bp (+3), 2s30s = 90bp (+5): front-end rally with long-end selling. Real 10Y 2.92% (+1bp), real 30Y 3.36% (+1); same-date nominal minus real 10Y 2.36% (flat), 30Y 2.31% (+2bp). The long-end daily move is not exclusively real-rate-driven. 10Y real is 42bp above 2.50; sustain remains MET, no add authorized.

Treasury 2026 daily-observation scan: 30Y ≥5.00 on 82/193 dates, current run 66 (2026 scan); real10Y ≥2.50 run20. Separate FRED H.15 frontier October6: whole-series DGS30 run65, count81/192. Do not attach FRED ranks to the later Treasury cell. Boot output captured 17:47 ET is archived.

FRED ICE mirrors, October6 latest vintage: HY303/CCC1214/IG83/BBB102/BB185/B302bp. Daily changes −9/+3/−1/−2/−8/−12; CCC−BB gap1029bp. Broad HY relief coexists with worsening weakest-tier spreads. HY is 47bp below350 and 3bp above300; +40 from263, short of the +75–100 credit-equity lead leg. Index protection remains behind LIQUID/BROCK's separate capital gate. No comprehensive failed-deal census is available.

ACM10Y TP0.9462%[10/6], KW1.0847%[10/2]; models/windows differ. Fed-funds vendor strip captured17:47ET after halt, not settlement: November3.925, December4.070%, EFFR3.88[10/6]. Calendar-weighted YE=(31×4.070−9×3.925)/22=4.129318%, +24.93bp; October hold/+25 proxy18%. The prior10/2 own-vendor25.43bp vs WALTER24.7bp discrepancy is not resolved by today's print. CME page loaded but QuikStrike returned access/error; no dated FedWatch/OIS table obtained. WALTER032 remains PARTIAL and retained. This is around one further hike, not proof that a precise below-25bp claim is independently verified.

## Released September FOMC minutes — five implications

[Primary minutes](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm), September15–16 meeting, October7 publication; full policy/market/funding sections retrieved directly by approved curl after web-tool failure. Raw HTML/text saved. Publication is not a new policy decision.

1. Most participants considered a further increase likely appropriate by year-end, contingent on incoming evidence. This supports higher-for-longer risk without committing the October meeting.
2. The intermeeting approximately35bp rise in 2–10Y yields has a policy-path component; term-premium explanations include geopolitical risk, Treasury buyback uncertainty and AI borrowing. The minutes attribute the latter explanations to market commentary, not a quantitative causal identification.
3. Staff attributed much of longer-maturity yield increases to real rates; longer-horizon inflation expectations remained anchored. This is the September intermeeting window, not October7's daily decomposition.
4. Funding remained stable and reserves ample. Paused reserve-management purchases are flexible, not a preset withdrawal path. This does not grade the excluded September23 auction funding window.
5. The Desk explicitly says late-July yen intervention used Treasury funds as fiscal agent, with SOMA uninvolved. This narrows the funding-source uncertainty; it does not quantify the ESF split, establish FIMA use or identify UST liquidation. November13 quarterly FX report remains the detailed resolver.

## VX-20 and intake

Bounded primary review: NBIM September1 letter re-fetched, Ministry reports/letters index read via web (direct HTTP403), English/Norwegian adoption searches plus GPIF and second-holder benchmark searches. No adopted mandate or qualifying second mandated holder located. **Search-not-found, not proof of absence.** VX20 remains2, FL14 LATENT; agency-MBS taxonomy unchanged. January25 expert deadline is not an earliest-decision guarantee. Search also returned National Budget2027 chapter describing intended spring2027 assessment; its publication date was not established, so it is excluded from the October7 conclusion. Review serviced October7; recheck October14 and upon issuer announcement.

Whole current inbox read: WALTER032 retained PARTIAL; October7-002 integrated from primary, -006 logged as attributed August gold data with MIDAS owning verification/interpretation. Complete current BOARD wave001–017 read, including corrections012/017; dispositions in board_log.tsv. Other-domain items are logged without adopting their grades. October5 research and Paramount pricing correction were already delivered; no duplicate research commission or claim of independent source corroboration.

## Next 48 hours and remaining limits

October8: 30Y-R912810UW6 $22B13:00ET, frozen pooled I-prime63.89%, reopening alt61.20, OLD59.95/14.74, cover2.29; then20–30Y F2 buyback $6B cap13:40–14:00, results expected~14:15; FR2004 as-of9/30 and PMMS. No future result graded. VX19 undefined disorderly qualifier remains due October8; no new threshold authorized. October14 CPI and Will/TERRY sleeve review; October16 expiry. Register October28 curve prediction by October21; OPEN predictions0. True CDX, paid MBS OAS, comprehensive pulled-deal coverage and executable broker/Activity remain gaps.

## Runtime and delivery

Explicit root CLAUDE/AGENTS/USER, local CLAUDE/boot/state/PROTOCOL and runtime mechanics loaded. Repo /home/willi/Research-workspace; Codex/OpenAI gpt-6-astra verified in own turn_context dated21:09:37.905Z; session01a1181a-7aa4-7882-9d7d-df300b6b4665. Will opened this owner; no helper spawned. Native coordinator notification works; broader owner presence UNKNOWN. Pull skipped because foreign dirty/staged work exists. New coordinator01a1182c-1dad-75f2-8929-93d093e7478e; crash-recovery packet read. Correction check0 unreceipted; upcoming-auction coverage only throughOctober13, later span outside tool guarantee. Persistence/recipient acknowledgment reported separately after actual evidence. No closeout requested in this window.
