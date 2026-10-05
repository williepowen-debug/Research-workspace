# Freight-cost transmission to USO — October5, 2026

Written 2026-10-05T14:21:52Z; Will confirmed shares and calls. **Tracking is now an active manual WALTER watch**, linked into next-boot reads, with weekly primary freight review and event-driven intake. No automatic alert/cron service is running. Owner integration of -005 was deferred; -006 conveys the new explicit tracking priority and the concrete watch.

## What reaches the ETF

[USCF's fund description](https://www.uscfinvestments.com/uso) defines USO's objective using WTI delivered at Cushing, measured through its benchmark futures contract, with collateral income and expenses. It describes a five-day monthly benchmark roll and permits oil futures and swaps. It does not track tanker charter revenues or an importer's delivered barrel cost. The holdings page was reached but returned no rows in this tool; no October contract allocation or precise roll calendar claimed.

[USO's June2026 filing, curve discussion](https://www.sec.gov/Archives/edgar/data/1327068/000110465926092623/uso-20260630x10q.htm) explains why backwardation/contango can cause returns to differ from spot oil. Curve convergence under otherwise unchanged conditions can help/hurt; selling one contract and buying another is not an instantaneous guaranteed profit/loss. No assumption about today's fund allocation follows from June holdings.

## Incidence matters — conditional reasoning, not a forecast

Delivered oil includes the crude price plus applicable transport and insurance costs. Additional freight may be borne by the buyer, offset by a producer discount or absorbed through refining margins. The August Reliance example in the preceding report shows expensive shipping coexisting with discounted origin crude. Thus an extra dollar of freight is not mechanically an extra dollar of WTI.

| Observed combination to investigate | Implication for WTI / USO |
|---|---|
| Fewer economically deliverable barrels; buyers substitute U.S. crude; export demand strengthens and stocks draw | Could support WTI and hence USO, if not already priced |
| Delivered Asian crude gets dearer but origin discounts widen and the Brent-WTI gap expands | Regional stress may be strong while USO captures only part of it |
| Global freight also makes U.S. exports less competitive, or higher fuel costs curb consumption | Could pressure U.S. producer realisations or demand; USO need not benefit |
| Freight normalises while physical supply keeps recovering | One source of scarcity/risk pricing can fade; the effect depends on expectations and other supply/demand changes |

[EIA's transport-cost explanation](https://www.eia.gov/todayinEnergy/detail.php?id=33752) supports the export-competition mechanism: WTI prices adjust to transport costs when competing with seaborne crude. That is a2017 mechanism reference, not a current cost estimate. The table above is conditional economic reasoning, not a measured beta or trade recommendation.

## Shares versus calls

Shares express the fund's futures return without an option-expiry deadline. They still have oil-price, curve, expense and tracking exposure. Calls add strike/expiry, delta/gamma, implied volatility and time decay. A call can lose value even with a modest ETF gain if time decay or falling implied volatility dominates. High persistent freight does not guarantee a sufficiently large, sufficiently timely WTI move. Current quotes and actual held options are required for any management decision.

The October1 mirror and TERRY's October2 recommendation are not current broker evidence or new approval. Preserve Will's declined WQ200 share-exit rule, manual share management, existing option rails and existing stand-downs. No automatic stop/roll or new position proposed here.

## Watch acceptance and gaps

The watch is concrete: WATCH.md governs cadence, STATE.csv contains nine separate observations/gaps, REVIEWS.tsv records this check, and STATUS requires the next boot to read it. Next scheduled-data check is Baltic/Gibson October9; the next WALTER session catches an overdue review, with date disclosed. Existing BRENT market/inventory reviews supply WTI pass-through evidence; no shadow copy of its canonical thresholds is created. Source failures remain UNKNOWN. Material new source evidence follows normal BOARD routing.

No latest WTI or option quote was pulled in this response. The initial market rows are explicitly sourced to BRENT's09:34–09:44ET capture; they are not live. Their softer WTI observation demonstrates that high freight can coexist with lower WTI in a snapshot, not that freight caused that decline.
