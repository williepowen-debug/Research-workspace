# USO — findings and analysis from October 20, 2026

Consolidates the investigation and subsequent discussion with Will. This records research already performed; it is not a new market-data refresh. Exact figures, observation dates and source coverage live in [observations.tsv](observations.tsv). The original [investigation](research-2026-10-20-short-interest/REPORT.md) and all its receipts are stored alongside this note.

## Established evidence

The directly retrieved FINRA records establish a substantial September 30 short position and a net reduction since September 15. September's path included an increase followed by a partial net reduction; the September 30 count was above August 31 and below late May. The source rows and full-file hashes are preserved in the investigation folder. [CONF: FINRA settlement dates in observations.tsv; retrieved October 20.]

September 30 was the latest public short-interest snapshot verified during the investigation. FINRA's calendar scheduled the October 15 settlement report for October 26 publication. There is no authenticated October position count in this research. October 20's actual balance could be higher or lower; the October 15 release will still predate October 20. [CONF: FINRA publication calendar, source in initial report.]

The issuer supplied a dated October 19 shares-outstanding, net-redemption and NAV-discount record. We did not authenticate a matching September 30 float denominator. Vendor short-percentage claims disagree, so no current or matching-date short-float percentage is certified. [CONF: saved issuer record and primary FINRA count; vendor comparisons in initial report.]

The one-broker lending proxy replenished after the open, then declined; the recorded post-open fee stayed unchanged. October 19's vendor-reported short-sale percentage was below its stated trailing average. Both are dated secondary observations, with their exact values and coverage in the observations table. The attempted primary daily short-volume downloads returned HTTP403, and the vendor average was not independently reproduced. [REPORTED_SECONDARY: ChartExchange borrowing and short-volume pages reviewed October 20.]

## Corrections clarified with Will

- A net reduction across historical settlement dates does not establish that the remaining shorts have now covered. Gross covering and gross opening can coexist within an interval.
- We have no evidence that the remaining positions are newly opened. “Newly minted” was unsupported framing and is not an adopted finding.
- Short-interest snapshots do not identify the age, entry price, owner, purpose or profit of individual positions. A large share-short total is not necessarily an equally large unhedged bearish oil bet.
- Daily short-marked transaction volume is not the outstanding short balance. It cannot be accumulated into one, and it does not reveal net covering.

## Assessment and conditional inferences

The available broker snapshots do not show continuously worsening borrow scarcity during their recorded interval. They do not establish market-wide conditions or prove covering: availability changes can reflect loan returns, new supply, inventory transfers, borrowing or withdrawn supply. A fee observation alone does not establish squeeze risk. No exceptional new shorting wave, coordinated headline trade, manipulation or imminent forced covering is established.

USO's documented creation/redemption mechanism can ease share scarcity while operating, but current restrictions still need verification. A persistent premium to fair value alongside verified creation constraints and tightening lending conditions would be more informative about share scarcity than a short-percentage headline alone. The initial report retains the filing source and historical creation-constraint example.

An oil reversal following failed negotiations could prompt short covering, but we cannot quantify that buying or attribute a reversal to it. Negotiation credibility and physical oil flows remain separate evidence questions from USO's share structure.

The strongest next positioning evidence would be a consistent daily series of shares on loan, new loans, loan returns, lendable supply, utilization and fees. Declining balances with increased returns would support an unwind interpretation; rising balances with tightening supply and rising fees would support borrowing pressure. Neither alone identifies intent. See [TRACKER.md](TRACKER.md) for remaining dependencies and the technical/options work that has not yet been performed.

Manual USO research tracking is authorized by Will's folder request. No automated schedule, trading trigger or capital decision was created. Position and approval references remain in [TRADE.md](../TRADE.md).
