# Is the CCC tier's October widening a few telecom restructurings? Optimum, Altice, and the rated-CCC basket
**Date:** 2026-10-23 (research 15:55–16:09 ET) | **Mode:** Thesis | **Request:** Will-approved follow-on to REQ-DEWEY-20261023-003 (slate #1, "approved go ahead" 15:54 ET); no WALTER REQ | **Confidence:** High on Optimum's balance sheet and the rated-CCC basket composition (SEC 10-Q; fund's own holdings page). Medium on concentration: plausible, not proven. No public October price change is available for the rated-CCC basket.

## Key Finding
**Concentrated in cable, telecom and media, with no AI.** BondBloxx XCCC tracks Bloomberg's CCC index (2% issuer cap). As of 10/22 it holds:
- **0% AI builders.** CoreWeave is not CCC-rated.
- **~5.9% software** (7.2% on a broad definition).
- **~16.5% cable, telecom and media.** The largest names are Optimum/CSC Holdings 2.2% (capped), Altice France 2.0%, Uniti 1.8%, iHeart 1.6%, Brightspeed 1.6%, Altice International 1.5%, Gray 1.3% and Viasat 1.3%.

**Optimum is a live restructuring.** Its 10-Q carries a going-concern warning; $4.12B matures in April 2027; lenders sued on 9/28; press reports Chapter 11 preparation (10/22). On 10/22, CCC's +33bp day coincided with that report.

**Two of the biggest losers in the high-yield sleeve, JetBlue and FMC, are not in the rated-CCC basket at all.** The sleeve result in the REQ-003 report therefore overstates "everything else" for the *rated* tier and understates telecom.

**Whether a handful of names explain *most* of +161bp: UNKNOWN.** The arithmetic allows it; the price data to prove it is not public.

## Evidence

### (1) The rated-CCC basket (actual CCC, not a yield proxy)
BondBloxx CCC-Rated USD HY Corporate Bond ETF (XCCC), holdings "As of 10/22/2026"; index "Bloomberg US High Yield 300MM CCC 2% Issuer Capped Index" (ticker I40741US, index market cap $110.133B). XCCC fund statistics: YTW 17.07%, OAS 1,218bp; NAV MTD −3.32% to 10/22. [PRIMARY: fund page, https://bondbloxxetf.com/bondbloxx-ccc-rated-usd-high-yield-corporate-bond-etf/, fetched 2026-10-23 16:0x ET; 178 lines summing to 99.25%]

| Bucket (DEWEY name classification) | Weight | Names |
|---|---|---|
| (i) AI builders | **0.0%** | none: CoreWeave, SoftBank and the compute SPVs are absent |
| (ii) software / AI-disruption, core | **5.9%** | athenahealth 2.07, McAfee 1.63, CoreLogic 0.79, Rocket Software 0.62, Dye & Durham 0.35, Newfold Digital 0.30, GoTo 0.12 |
| (ii) broad add-on | +1.3% | Virtusa, Xerox, AHEAD |
| (iii-a) cable / telecom / media | **16.5%** | CSC Holdings 2.20, Altice France (3 issuers) 1.96, Uniti 1.80, iHeart 1.63, Connect Holding II (Brightspeed) 1.62, Altice Financing 1.49, Gray Media 1.34, Viasat 1.28, LCPR 0.95, EW Scripps 0.88, Sinclair 0.53, CMG Media 0.44, Allen Media 0.20, Cable One 0.19 |
| (iii-b) everything else | ~76% | led by CHS/Community Health 2.01, Ardonagh 1.79, 1261229 BC 1.48, Chobani 1.44, Mauser 1.37 and others; diversified |

**Caveats:**
- **The 2% issuer cap understates concentration.** Optimum/CSC's uncapped index weight is UNKNOWN and likely higher.
- **These are weights, not moves.** No 9/30 XCCC holdings file exists to compute October contributions. That is the next pull: `etf_holdings.py` does not yet cover XCCC.
- This is the Bloomberg index, not the ICE index behind FRED's BAMLH0A3HYC.
- **Not in XCCC:** JetBlue, FMC and Virgin Media O2. Their exclusion means they are rated above CCC, issued under $300M, or ineligible. The reason was not checked.

### (2) Optimum Communications (formerly Altice USA; CSC Holdings is the borrower)
**The rename is confirmed:** EDGAR CIK 0001702780 is "Optimum Communications, Inc." (OPTU) [PRIMARY].

**Balance sheet, Q2 2026 10-Q** (accession 0001702780-26-000048, filed 2026-08-06; DEWEY spot-checked the maturity figures and the going-concern sentence in the extracted text) [PRIMARY]:

| Item | Amount |
|---|---|
| Total principal including leases, 6/30/26 | $26.74B |
| CSC Restricted Group (carrying value) | $21.99B |
| Cash | $1.30B |
| Revolver availability | **$75M undrawn of $2.475B** |
| Due 4/15/2027 | Term Loan B-5 $2.8125B + 5.50% notes $1.31B = **$4.1225B** |
| Due 7/13/2027 | revolver drawn $2.225B |
| Going concern | "substantial doubt exists about our ability to continue as a going concern within one year" |

A separate maturity table in the 10-Q shows 2027 total = $6.3325B; not reconciled.

**Events:**
- **9/16 (8-K 9/21):** Item 4.02 non-reliance. FY2025 and three 10-Qs will be restated for deferred-tax items, and a material weakness is expected. Cash and EBITDA are unaffected [PRIMARY].
- **8/14:** NYSE below-$1 notice; cure deadline 2/13/2027 [PRIMARY].
- **9/28:** lenders sued in New York State court, alleging fraudulent transfer and related claims, against Drahi and executives [NEWS: Broadband Breakfast 2026-09-29, https://broadbandbreakfast.com/creditors-sue-optimum-allege-fraudulent-schemes-to-address-billions-in-debt/]. **Docket/index number: UNKNOWN.** Plaintiffs reported as including Apollo and Oaktree [NEWS, weak].
- **~10/14:** Drahi sought to keep about $3B of equity; creditors offered about $500M [NEWS citing Bloomberg, via billionaires.africa 10/16].
- **10/21:** close to a deal handing control to lenders (Apollo, Oaktree, JPMorgan) and settling the litigation [NEWS citing WSJ: Broadband Breakfast 10/21, https://broadbandbreakfast.com/debt-plagued-isp-optimum-close-to-handing-the-keys-to-lenders-resolving-litigation/].
- **10/22:** reports of Chapter 11 preparation, possibly before year-end. The stock fell 18.4% to about $0.58 [NEWS, weak: Tickeron 10/22; original outlet not named].
- **Not found:** an October 8-K, a signed restructuring support agreement, rating actions, and bond quotes.

### (3) Altice France and Altice International
- **Altice France** restructured in 2025: €8.6B of debt cut; ISDA credit event 6/9/2025 [NEWS, secondary]. On 6/6/2026 it agreed to sell SFR to Bouygues, Iliad and Orange at €20.35B enterprise value, with completion as late as H2 2027 [INSTITUTIONAL: Mayer Brown]. **An October 2026 catalyst was not found.** French sovereign stress around 10/19 (OATs ~5.0%) is DEWEY's inference, not a sourced cause.
- **Altice Financing SA** is Altice International (Portugal and Dominican Republic), not Altice France. It pulled assets from the collateral pool in November 2025 and converted €2.5B of MEO debt to equity in May 2026 [NEWS: ECO 2026-05-13]. No October catalyst found.

### (4) The high-yield-sleeve names that are NOT rated CCC
- **FMC (company shock).** The 10/15 8-K cut Q3 revenue to "$65 million to $125 million", with adjusted EBITDA "negative $565 million to negative $510 million". FMC will seek "further modifications to its covenants over the next year" [PRIMARY: 8-K exhibit 99.1, accession 0000037785-26-000149; quotes DEWEY-verified]. Q3 earnings 10/29.
- **JetBlue (company stress).** Loyalty-backed 9.875% 2031s were at 72 on 10/10, down from about 84 in July [NEWS: View from the Wing 10/10]. Record lows on 10/22 per a Bloomberg headline [UNVERIFIED: about 40c from a search summary only]. Q3 earnings next week.
- **Virgin Media O2.** UK regulatory overhang (Nexfibre/Netomnia) "rippled across high yield"; No. 7 in Bloomberg's Pan-European HY index at >1.2% [NEWS: briefs.co 10/12].

### (5) Concentration arithmetic (DEWEY-derived, illustrative)
| If the stressed names are this share of the CCC index | each must widen by about | to produce +161bp alone |
|---|---|---|
| 10% | ~1,600bp | |
| 16.5% (XCCC cable/telecom/media weight, capped) | ~975bp | |
| 20% | ~800bp | |

Bonds falling 20–40 points widen by four figures, so a cable/telecom block of about 16.5% *could* account for most of +161bp. The tier split points the other way, toward a broader move:
- From 9/30 to 10/22, CCC moved +161bp, against B +30 and BB +16 (FRED).
- Since 4/30, CCC has moved +431bp, against B +35.

If CCC normally moves about 2.5× B (an unsourced assumption), about 75bp of October is broad beta and about 86bp is excess. On that reading, roughly half the move is idiosyncratic.

## Counter-Evidence
- **For "a few names":** BNP Paribas AM's Daniel Morris: "A large part of the index spread widening has been concentrated in a few names in the lower-ranked parts of the index (CCC)" [INSTITUTIONAL: ioandc.com 2026-10-22, https://ioandc.com/bnp-paribas-am-says-the-jump-in-high-yield-spreads-is-volatility-not-a-warning/]. His window was 9/8–10/1. Janus (10/15) names cable/satellite and wirelines.
- **Against "only telecom":** CCC has diverged from B for six months, not just October. The rated-CCC basket is about 76% non-telecom and diversified. XCCC's NAV fell 3.32% month-to-date, a basket-wide move. Penn Mutual (10/15): "stress is building at the lowest end of the quality spectrum" generally.
- **Rejected as unverifiable:** a "median CCC constituent widened ~66bp" claim attributed to "Deer Point Macro" (no such source found) and a "CCC 807bp on 9/30" figure that contradicts FRED.

## Source Quality Assessment
- **Primary and strong:** XCCC holdings, Optimum's 10-Q and 8-Ks, FMC's 8-K.
- **Weak:** the Optimum lawsuit, the Drahi equity talks and the Chapter 11 report, all press with paywalled originals.
- **Missing:** the decisive fact, name-level October price changes in the rated-CCC basket, is not public for free.

## References
(accessed 2026-10-23) URLs inline. FRED: BAMLH0A3HYC, BAMLH0A2HYB, BAMLH0A1HYBB, BAMLH0A0HYM2. EDGAR: Optimum CIK 0001702780 (10-Q 0001702780-26-000048); FMC 8-Ks 0000037785-26-000149 (10/15) and 0001193125-26-427896 (10/21).

**Reproduce the XCCC table:** fetch the fund page and strip the HTML. Parse the "All Holdings" table with the regex `(.+?) ([0-9A-Z]{9}) \$([\d,\.]+) ([\d\.]+) %`, between "Name CUSIP Market Value % of Net Assets" and "NET OTHER ASSETS". Bucket by issuer-name prefix as in §1.

## Process Report
**Searches run:**
- One Opus leg: 59 tool calls, ~17 searches.
- DEWEY found and parsed the XCCC holdings (the leg had pointed to XCCC as the route) and spot-checked Optimum's 10-Q and FMC's 8-K.

**Data gaps:**
- Uncapped CCC weights.
- October price changes in the rated-CCC basket.
- The lawsuit docket number.
- Rating actions.
- An Altice October catalyst.
- Why JetBlue, FMC and VMO2 are excluded from XCCC.

**Source frustrations:** Bloomberg, Fierce, Axios, CNBC and others returned 403. NYSCEF requires a manual search.

**Confidence in findings:** High on composition; Medium on the concentration verdict.

**If I had more time/tools:**
- A 9/30 XCCC holdings snapshot (Wayback?) for weight-implied moves.
- The NYSCEF docket.

**Suggestions:**
- Add XCCC to `etf_holdings.py` (holdings are embedded in the page) and save daily alongside HYG/JNK. This gives the fleet a free rated-CCC composition series.
- Watch Optimum for an 8-K: a signed restructuring support agreement or a Chapter 11 filing is a dated CCC event that LIQUID/REGINALD would see inside REG-T-04's window.
