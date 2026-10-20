# USO shares sold short — October20 investigation

**Result:** FINRA directly reports10,437,989USOshares short at September30,2026, releasedOctober9. Latest public observation, not today's position. Down1,542,614/12.88% fromSeptember15; down46.91% fromMay29, but up9.10% fromAugust31. Large exposure relative to the fund's recent share count; no verified current squeeze, motive, trader identity or attribution of today's decline. One-off Will-requested investigation; no new monitoring/trade/threshold authority.

## Direct primary verification

Downloaded [September30 official file](https://cdn.finra.org/equity/otcmarket/biweekly/shrt20260930.csv) and exactUSO/ARCArow. Repeat independent HTTPrequest reproduces the full row and filehash; two retrievals of ONEmeasurementlineage, not two independent witnesses. Saved row/filehash receipts alongside this note. Other dates independently extracted from their own official files.

| Settlement date | Shares short | Prior report change | Average daily volume | Days to cover |
|---|---:|---:|---:|---:|
| May29,2026 |19,660,351|+930,324/+4.97%|8,600,937|2.29|
| August31,2026 |9,566,953|−400,294/−4.02%|3,960,537|2.42|
| September15,2026 |11,980,603|+2,413,650/+25.23%|6,382,228|1.88|
| September30,2026 |10,437,989|−1,542,614/−12.88%|6,442,785|1.62|

[CONF FINRA primary files, dates above; not estimates of currentpositions.] Exact arithmetic in calculations.json.1.62=10,437,989/6,442,785 rounded; a volume ratio, not a forecast that everyone can or must cover in1.62days. It contains no execution-capacity, borrow or buyer/seller constraint model.

**Interpretation:** September involved a build followed by partial net reduction; do not call it a steadily accelerating short attack or ignore the earlier build. Net balance changes do not identify gross newshorts versus covering, investor intent or returns.

[FINRA calendar](https://www.finra.org/filing-reporting/regulatory-filing-systems/short-interest) gives October15 settlement / October19 reportingdeadline / October26publication. September30 therefore remains the latest published snapshot onOctober20. October15's later publication still cannot describe positions opened during today's selloff. No new recurring monitor or promised release-day session created.

## The percentage problem

The FINRA file provides shortpositions and volume, NOT a float or shortpercentage. MarketBeat publishes92.21% forSeptember30; ChartExchange's indexedSeptember30result gives77.76%, while a direct page read returned the olderSeptember15vintage82.49%. These are not independent official percent-of-float measurements. MarketBeat also mixes a15.17Maveragevolume header with1.62days, which does not reproduce; use FINRA's6.442785Mmatching denominator for that report.

Recovered the actual [issuer page](https://www.uscfinvestments.com/uso)'s public dailyprice API after following its HTMLbase/path and JavaScript data contract. Issuer record explicitly identifiesUSO/CUSIP91232N207/NYSEArca: **12,323,603shares outstanding, displaydateOctober19**. The page's generic web-reader shell omitted values; it did not establish source absence. Endpoint record saved as issuer-dailyprice.json; provenance in sources.json. Public client token neither printed nor saved.

**10,437,989/12,323,603=84.70%, but dates do not match.** This is a scale comparison only; NOT today's percent short, NOT September30matched shortfloat. Same-date issuer outstanding/freefloat not authenticated. MarketBeat92.21% implies11.3198Mfloat; ChartExchange77.76% implies13.4233M. Do not select the more dramatic denominator. An ETF's changing issued sharecount makes this especially consequential.

Issuer October19record also shows net500,000shares redeemed and reported midpoint/NAVdiscount about0.15%. This shows that day's redemption/reporting activity and a small published discount, not proof of current unconstrained creations, universal borrowavailability, or absence of future squeeze risk. No live USOprice or positionmark adopted here.

## What short interest means for this fund

The [USO2025Form10K, filed2026](https://www.sec.gov/Archives/edgar/data/1327068/000110465926021501/uso-20251231x10k.htm) describes100,000share creation/redemption baskets available to authorizedparticipants and arbitrage intended to align marketprice withNAV. Share supply can therefore adjust when creations operate. The same filing documents creation constraints and historical premiums; NEVER assume unlimited creations or that USO cannot squeeze. Current creationcapacity was not independently surveyed.

**Assessment/inference:** a reported shortshare may be outright bearish oil exposure, a hedge against options/futures/anotherposition, or part of an arbitrage strategy. AggregateFINRAdata cannot allocate among these. Reportedshorts are grosspositions inUSOshares, not traders' netoil exposure; no names, nakedshort classification or profit/loss supplied.13Fholdings/puttables alone cannot solve that mapping.

A convincing current squeeze case would need current loanfees, lendableinventory/recalls, matchingdatedsharecount and premiums/creationconstraints alongside a pricecatalyst. Most remain missing; the dated brokerproxy below adds one limited observation, not a full market picture. This investigation does not establish forcedcovering. Conversely, the highhistorical exposure should not be dismissed merely because this is anETF.

## Dated lending snapshot recovered at the end of the pass

[ChartExchange IBKRfeed](https://chartexchange.com/symbol/nyse-uso/borrow-fee/) reports **3.07%annualfee/150,000available atOctober20 09:32:58EDT** [CONF content of secondarybrokerproxy, not independentprimaryloanfilevalidation]. Saved borrow-proxy.json. Its prior09:00row was3.00%/150,000. This is an earlier one-broker indication, notcurrentall-broker inventory, outstandingloanvolume, recalls/utilization or a borrowoffer guaranteed toWill. It supplies no evidence of acute fee escalation at that snapshot; no historicalpercentile/threshold is registered. Some earlier samepage zeros are not proof of no market-wide supply. Currentprimaryloanfile remainsunrecovered. This narrows the sourcegap without establishing no squeeze risk.

## Daily short-sale volume is different

[FINRA explanation](https://www.finra.org/investors/insights/short-interest) distinguishes openpositions from shortmarkedtransactions. A sale covered later the same day can enter dailyvolume without leaving an openshort; an oldposition can remain open without a new dailyprint. Summing dailyshortvolume does not reconstruct shortinterest. Venuecoverage and denominators matter; an offexchange percentage cannot be called the percentage of allUSOshares newlyshorted.

Fintel's current rendered page still carried October14dailyrows and no authenticated current borrowquote; undatedheaders/historicalSeptember9fee claims were rejected asOctober20evidence. No current consolidatedtoday shortflow established. Today's price decline alone does not demonstrate newshortpositions.

## Access and limits

FINRAprimaryCSV download works and covers exchange-listedUSO. OlderAPI metadata still describesOTConly; metadata language is not evidence thatUSOhas no shortpositions. Nasdaq's API explicitly says shortinterest unavailable because its endpoint supportsNasdaq-listed stocks;USOisARCA, so this is a coverage refusal, not a zeroshortreading. IssuerJS first resolved against the wrongroot returned500; corrected against the HTMLbase, then retrieved intendedpublicdata. Rawerrors preserved as diagnostic history. No credentialbypass/accountlogin/purchaseddataservice.

**Conclusion:** substantial reported shortposition, with netreduction in the latest report and a muchlower count thanMay29. The publiclag prevents attributing today's selling or negotiationheadlines to those positions. Exact current percentoffloat, market-wideborrowstress and motive remainunknown; datedonebrokerproxy retained above. No thesisversion/forecast/holdinggrade or newtrade; WAIT/WQ192unchanged. Data cannot establish manipulation or imminent squeeze.
