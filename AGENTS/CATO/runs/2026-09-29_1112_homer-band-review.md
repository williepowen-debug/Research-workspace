# HOMER band proposals — CATO review, September 29, 2026

## Current assessment

Recommend Apartment List option A at existing >20/>40/>55% levels, and foreclosure STARTS >100K/>130K/>175K, with the bounded installation conditions below. These are descriptive breadth/severity instruments; predictive performance for losses, bank stress or trades has not been demonstrated. No ruling, installation or owner-file repair by CATO. No additional research commission is needed to choose between these options.

Rent independently reproduces: 46 of 100 cities negative YoY in September 2026, versus 60 in April and 52 in August, on the September vintage. This is widespread but narrowing rent decline. Reactivation at Orange restores measurement; it does not establish fresh deterioration. Lower rents can pressure property income while relieving tenants; breadth alone does not establish household or bank losses.

The foreclosure ladder fixes the old Red threshold flagging every 2017–19 quarter. It cannot carry early warning alone: Q2-2026 derived starts of 81,935 remain below Yellow while rising about 15.1% YoY on HOMER's comparator. Keep existing monthly conversion/inventory observations and same-quarter growth beside the level. No duplicate alert framework proposed. No rung crossed must never mean no housing stress.

Favor 175K as the earlier of the two proposed severity markers. **175K versus 185K changes zero classifications in all 58 supplied quarters.** History does not select between them. The 2013 average is 186,932; 185K is a rounded alternative. Describe 175K as judgment informed by the workout period, not an estimated crisis boundary.

## Scope and authority

Will requested help with HOMER and supplied its retune/completion summary. Scope: the two choices, decision usefulness and reproducibility. Snapshot: master, HEAD `db23c2fa4156fea41fb8aff046ffdf03affa7d03`; HOMER packet `1eea348d6`, reports `db23c2fa4`. Other work present: CRUISE staged renames plus CRUISE/PROME/shared-memory edits. No pull or owner-file edits. CATO charter/root rules/HOMER CLAUDE read; no HOMER AGENTS.md at checked path.

Read packet, A3/A4 reports, scripts and stored series; targeted A4 period evidence; relevant STATUS/NEXUS/docket rows and thesis rail for context. Did not audit the full thesis rail, charter authorization, complete PROME list, CARL convergence proposal or running shells. Combined reads initially truncated; needed A4 opening, evidence and code were separately retrieved. Historical-source coverage remains limited below.

Targeted search of current `PROME/WILL_QUEUE.md` found no A3/A4 retune registration. The existing packet asks PROME to register one; packet delivery is not registration. PROME owns that next formal step. CATO did not edit its active queue or send messages. Advice here activates nothing.

## Verification

- Downloaded the exact September Apartment List CSV; SHA-256 `aa05b458d52facddf5415071f2dc45db781c6b9ff9cba747bd938516a2d3a644`, matching HOMER's abbreviated hash. Selected City/overall, top 100 by current population, 100 unique FIPS. Independently compared decimal rent levels to the same month one year earlier, counted negatives and valid pairs. **All 105 months match** HOMER's n, negative count and percentage within float tolerance. Last 13 months cross Yellow/Orange 13 times each and Red seven times. No owner code used for this rent reproduction.
- Retained [verification receipt](2026-09-29_1112_homer-band-review_evidence/verification.json) and [exact selected source rows](2026-09-29_1112_homer-band-review_evidence/apartment_list_top100_2026_09.csv). Full 3,708-row file remains temporary; retained rows reproduce the examined series. Review evidence is not an installed owner refresh process.
- [Apollo January 2026 deck](https://www.apolloacademy.com/wp-content/uploads/2026/01/USHousingOutlookJan2026_v2.pdf), slide 91 text, confirms Apartment List source and 56% negative YoY among 100 largest cities. Screenshot retrieval failed; no visual reconstruction claim. Deck month need not equal data month. One near-match does not prove identical membership, method or vintage.
- [ATTOM Q1 release](https://www.attomdata.com/news/market-trends/foreclosures/q1-and-march-2026-foreclosure-market-report/) confirms 82,631 starts; [ATTOM midyear wire release](https://www.prnewswire.com/news-releases/foreclosure-activity-posts-annual-increase-in-first-half-of-2026-302827085.html) confirms H1 164,566. Subtraction gives **81,935**, DERIVED. This does not independently prove universal additivity of older reporting periods; deduplication/revisions remain reasons to keep derivation labels.
- Executed HOMER's read-only A4 script: 22/16/6 crossings among 51 non-moratorium quarters; 0/14 at each proposed rung recently. Independently compared >175K and >185K on its values: no different grades. Arithmetic verification of supplied history is not independent verification of every input.
- Archived 2013/2015 primary links were attempted but inaccessible in the web tool; those anchors remain owner-sourced. Zillow raw data was not reproduced. Inferred starts-definition continuity, revisions, seasonality, mixed derived/implied historical values and missing comparable quarterly GFC data remain material A4 limits.

## Findings and installation conditions

### HR1 — Medium: recovered source does not prove Apollo-method equivalence or threshold calibration

**Evidence:** A3 report §0/§6 and packet option A promote one matched point into “same statistic” and “levels travel”; §4 infers original calibration from historical fit. The same report correctly discloses single-point overlap and revisions. Apollo's source attribution does not establish the exact roster or threshold design.

**Consequence:** recovery could be mistaken for external validation. The levels can serve as descriptive cutoffs, but no loss-outcome calibration is supplied.

**Closure:** adopt explicitly as **HOMER-computed rent-decline breadth from Apartment List**, with levels retained by Will's judgment and the equivalence limit preserved. At installation retain input vintage and selected city IDs; fix membership for this adopted series or explicitly define future changes; carry valid n and missing-data handling. Recommend incomplete pairs produce an ungraded band plus observed count/n, not a silently changed denominator. Keep recalculated history distinguishable from contemporary readings. No new platform or lengthy Apollo replication study is needed.

### HR2 — Medium: historical foreclosure severity is not a validated early-warning threshold

**Evidence:** A4 §5b shows zero recent crossings; no test links proposed crossings to subsequent losses. Red 175K/185K gives identical historical classifications. Absolute counts do not hold the exposed housing/mortgage population constant.

**Consequence:** below-Yellow could obscure deterioration before a historically large level is reached.

**Closure:** install, if ruled, as a national starts **severity ladder**, retaining YoY and existing monthly conversion observations. No “normal/contained” inference from silence alone. No new normalized series or outcome backtest required for this limited use; stronger predictive claims would need separate evidence.

### HR3 — Low: boundary and provenance cleanup during installation

46% is nine percentage points below the 55% boundary, but **>55% requires 56/100: ten additional cities**. June's stored `55.00000000000001` falsely passes a naive float comparison; HOMER's summary script rounds first, so its reported seven Red months are correct and no live misgrade is demonstrated. Use exact count comparisons (`100 * negative > threshold * n`) or equivalent safe boundaries.

Packet A4 calls Q4-2015 131,585 printed; its report/evidence label it derived. A4 opening claims calibration on 2022–24; §6 correctly says the old levels' origin is unknown. Preserve the latter caveat. “Highest uncrossed” actually means nearest next rung in the sub-Yellow example. Finally, [Apartment List methodology](https://www.apartmentlist.com/research/rent-estimate-methodology) describes repeat transactions and rented-unit prices; narrow A3's broad “both asking rents” gloss. These corrections do not change the verified readings or justify extending research.

## Next step and stop condition

PROME registers the delivered packet with caveats; Will rules. If approved, HOMER makes the bounded installation pass, updates stale no-feed/successor descriptions in existing instructions/docket, and demonstrates refresh at the next Apartment List monthly release and ATTOM Q3 release. October 6 is a ruling reminder, not grounds to defer a ruling received sooner.

CATO's review is complete at advice and independent rent reproduction. HR1–HR3 remain owner implementation conditions, not CATO fixes or certifications. Stop here unless Will asks for implementation assistance or changed evidence arrives. No wider audit or successor study commissioned.

## Delivery checks

Root orphan advisory completed: only other-owner paths reported; authorship review found no self-authored external packets or shared files. Weekday claim check passed on PROME DOCKET/GATES/WILL_QUEUE. `git diff --check` passed; exact CATO changes inspected and CRUISE staging preserved. CATO read-cap tool returned rc=2 CANNOT-EVALUATE because it expects CLAUDE.md; direct byte check of the six required boot surfaces confirmed each below 32,550 bytes. This is a manual size check, not a checker pass. No product code, canonical owner figures, STATUS or shared memory changed by CATO; consumer, ledger-nudge and memory-mutation checks are inapplicable. Safe-push result will be delivered in-session. Shared publication can carry other agents' committed work; it does not approve either HOMER proposal.

Follow-up delivery correction: the selected CSV was initially committed with Python CSV writer CRLF endings, which the staged whitespace check flagged. Converted the evidence extract to LF without changing fields or values; retained the original commit and recorded the repair in a separate commit. The earlier clean diff check preceded staging the new CSV.
