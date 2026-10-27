# FERT domain audit — 2026-10-26

**Requested by Will:** “Is your file domain built out fully/correctly? Are we not tracking anything that we SHOULD be as FERT?” **Boot clock:** 2026-10-26 23:07 Monday. **Evidence read:** 2026-10-27T03:15:28+00:00. Audit snapshot: `research/2026-10-26_domain-audit/audit_snapshot.json`.

## Judgment

**No: FERT is a functioning fertilizer watch desk with incomplete research coverage and several correctness defects.** The gate, calendar, inbox and benchmark safeguards are useful. They do not establish that CF fundamentals, physical supply, farm affordability or causal transmission are fully covered. More folders alone would not close these gaps.

The highest-value build is a CF operating record tied to named physical supply/demand evidence. Farm affordability and intermediate food-price measures should then test whether a fertilizer shock is being absorbed by farms, reducing demand, or moving downstream. Potash remains triage-only; trade construction remains TERRY. No new standing framework, paid feed, gate, score or company coverage is installed by this assessment.

## Inventory and controls checked

Snapshot before this audit's new artifacts: **99 files**, including **13 archive files**, **46 inbox files (mostly processed)**, **10 workbook files** and **18 source/research files**, the latter all belonging to the recent L758 verification. Only three current research/report Markdown files existed: October 21 self-sweep, October 26 startup, and the L758 report. A large evidence ledger is not equivalent to a reusable company or market history.

| Existing component | Finding | Assessment |
|---|---|---|
| Rules and identity | Nitrogen, phosphate, live China policy, food-CPI question, CF; potash triage only | Scope is clear and appropriate to preserve |
| STATUS / KB / VX / FLOW | Present; benchmarked price panel and separate channel states | Useful operating spine; specific defects below |
| Wake register | 13 rows: 11 dated live rows, T5 retired pending replacement, T6 consumed/retired | Working calendar; local source names are not fetch producers |
| Registered gates | G3 and G5 watch-only; G1/G2 held; G4 declined | Preserve approvals; this audit changes no letters |
| Prediction ledger | 12 resolved rows, 0 OPEN | History exists; no current forecast calibration loop |
| Startup / corrections / inbox | Boot quiet; 0 NAMED correction obligations; inbox only PROTOCOL/RECEIPT | Narrow checks pass, not a domain-completeness certificate |
| TSV shape | KB 89×13; VX 8×11; FLOW 7×8; predictions 12×11; triggers 13×7; no malformed widths or duplicate IDs | Syntax checks pass; semantics need repair |
| Reads declaration | No FERT row in PROME/registry/READS.tsv | Read-cap verdict uses charter heuristic, not an attested complete footprint |

## Correctness and maintenance findings

| ID | Finding and exact owned surface | Consequence | Disposition |
|---|---|---|---|
| C1 | STATUS vector 8 / VX-FERT-08 compare theoretical **ammonia** cost with **urea** selling price and conclude uneconomic production | Different products and conversion/basis costs; cannot grade profitability from that comparison | **FIXED:** withdraw that live comparison; profitability UNVERIFIED. Keep prior YELLOW/score as a labelled un-regraded legacy state, no new measured margin |
| C2 | VX-FERT-01 headline still presents “3.3 Mt quota unchanged”; notes say it may be an import tariff quota | A caveat buried below the current-value field permits reuse of an unverified export ceiling | **QUALIFIED:** promote UNVERIFIED basis to current-value field; preserve number as disputed registration history and leave bands/registered G3 untouched. MOFCOM check still owed November 5 |
| C3 | FLOW FL-FERT-06 remains Estimated, while its notes say restore on MAP >$975/ton; that condition was met October 14 (FERT-12 MISS). Old “second source still undischarged” text also predates later evidence | Old narrative needs a current owner assessment; “restore only on” is a necessary condition, not an automatic upgrade | **QUALIFIED:** annotate that eligibility was met, while attribution remains unproved. Estimated can legitimately remain; no mechanical contradiction or automatic promotion is asserted |
| C4 | GATE_GRADES contains October 21 grade but header says refresh October 15 and next grade October 21 | Metadata misdirects the next session despite a correct recorded grade | **FIXED:** last data refresh October 21, hygiene October 26, next grade October 28; no new print claimed |
| C5 | Charter still calls retired Advanced Turf the best free NOLA source; KB header says no fertilizer vocabulary exists | A cold boot can follow dead guidance; actual vocabulary includes FERTILIZER_N, PHOSPHATE and FOOD_CPI | **FIXED:** correct pointers/descriptions, not instrument scope. Legacy group mappings remain below |
| C6 | KB has **49 ACTIVE rows**, **16 past Stale_By**, **10 with no Stale_By**; neither boot.py nor ledger_staleness.py references Stale_By | Fresh file headers can mask overdue individual claims | **OPEN:** classify row-by-row at next maintenance; do not relabel immutable historical facts false or assign artificial far-future dates just to clear a scan. New row-deadline tooling is a proposal, not installed |
| C7 | KB groups absent from NETWORK_GROUPS: CHINA_POLICY (6), QATAR (1), POTASH (11), FERTILIZER_P (10), FERTILIZER_K (1) | Schema requires controlled groups; 29 rows use undeclared group labels | **OPEN:** map existing semantic equivalents where safe, or ask vocabulary owner to register missing groups. Preserve potash triage depth; no blanket recoding in this audit |
| C8 | Broad source-access claims are carried as if client-independent (e.g. SEC blocked); SEC CF release and 10-Q were reachable through this session's browser | Previously blocked access can become a stale reason not to read primaries | **PARTLY FIXED:** charter access guidance now says verify per client/session. No assertion that every SEC/IR endpoint is reachable |
| C9 | No READS declaration; STATUS 22.7 KB and KB 112.8 KB at audit start | A whole KB dump is not a viable default read, while heuristic cap checks cover only discovered reads | **OPEN:** declarative boot footprint via PROME; keep large KB scoped/programmatic. No need to split a file solely because it is large if it is never read whole |

C6 counts are **review debt**, not a claim that all 26 affected rows are invalid. Some blanks are permanent dated methodology/source-contamination records, and some overdue rows are historical print receipts. Their lifecycle and use must be classified before changing them.

## What should be tracked more completely?

| Priority | Lane / missing evidence | Why it can change the decision | Minimum useful build within the existing charter |
|---|---|---|---|
| **1** | **CF operating fundamentals**: no dedicated quarterly operating history or CF research dossier; issuer mentions are scattered in policy notes/frozen trade history | Fertilizer market direction does not tell us CF's realized margins, production, cash generation or investment burden | Product sales volume and realized price, ammonia output, gas expense including hedges, segment margins, cash flow, debt/cash, capex/JV flows, one-offs, outage/restart dates and management guidance; reconcile Q2 baseline before Q3 |
| **2** | **Physical supply and trade flows**, particularly realized China urea exports and US N/P imports; capacity outages/restarts are episodic prose | Announced allocations are not shipments; import replacement can offset a chokepoint or domestic curtailment | Monthly product-specific tonnage with publication lag and country basis; separate Chinese quota, supplier allocation, customs export and actual shipment. A dated affected-capacity/restart list, with issuer status and unknowns, not a fabricated global closure count |
| **3** | **Farm affordability and demand**: crop price/revenue versus fertilizer cost, crop mix/application behavior, credit/input purchasing constraints | High fertilizer prices can squeeze farm income or reduce use rather than reach grocery CPI. Planting on schedule does not measure application rates or profitability | A small corn/wheat/soy crop-input context using NASS prices paid/received and crop budgets/ERS expenses; specify geography, lag and crop year. Broad household effects remain CARL, macro CPI HENRY |
| **4** | **Intermediate food-cost evidence** between fertilizer and grocery CPI | CPI and ERS forecast revisions cannot isolate fertilizer causation by themselves | Farm-gate/food PPI and commodity-specific supply evidence alongside existing CPI/ERS; explicit competing explanations and lag. No revival of declined G4 machinery or claim that a forecast change proves input pass-through |
| **5** | **Ammonia / UAN economics and phosphate inputs** | CF is not a pure urea price; ammonia is also a phosphate input. Sulfur constraints may matter even with flat phosphate rock | At existing wakes, compare the same product/cost/delivery basis; pin heat rates, gas date and conversion costs before deriving a margin. Follow sulfur contract settlements and named issuer curtailment/restart evidence; BRENT retains gas ownership |
| **6** | **Relative nutrient tightness and seasonal demand** | Separate price cells show levels but do not provide a repeatable N-versus-P view, despite the charter calling this first-class | Use aligned observation periods and named series, preferably normalized within-series changes with original units retained; distinguish India/Brazil/US planting windows. No raw cross-benchmark subtraction or new automatic gate |

These are coverage recommendations, not six new daily desks. Priorities 1–2 carry the most immediate decision value. One bounded build can create a source map and an initial dated baseline, then maintenance should ride the existing weekly/monthly/earnings wakes. The actual cost and availability of candidate data must be established before committing to a new standing obligation.

## Public-source checks — what is actually available

- **CF primary is reachable:** [August 5 issuer release filed at SEC](https://www.sec.gov/Archives/edgar/data/1324404/000132440426000017/cf-08052026_ex991xearnings.htm) and [June 30 10-Q](https://www.sec.gov/Archives/edgar/data/1324404/000132440426000019/cf-20260630.htm) read through browser. Segment tables provide product and nutrient tonnage, realized selling prices, and margin information. Release footnote 4 says its **98% available-ammonia-capacity utilization excludes Yazoo City**; do not call it utilization of total nameplate. Highlights separately flag a **$170 million litigation settlement** in first-half results: reconcile the adjustment tables before interpreting recurring earnings. These examples show why one headline EBITDA growth rate is insufficient; no fresh valuation or trade is inferred.
- **Trade:** [Census monthly international trade API documentation](https://www.census.gov/data/developers/data-sets/international-trade.html) is the appropriate candidate for current HS-level US imports/exports. Urea, ammonia, DAP and MAP require product-specific codes; DAP/MAP are in **3105**, so “phosphates = HS3103” would omit key products. The [old ERS fertilizer trade product](https://www.ers.usda.gov/data-products/fertilizer-imports-exports) is **DISCONTINUED**, with underlying tables ending in 2012 despite a 2025 page stamp. Its [documentation](https://www.ers.usda.gov/data-products/fertilizer-imports-exports/documentation) is useful for historical definitions, not sufficient to certify current HTS codes. Census/USDA AMS feed extraction and current Chinese customs access remain untested in this audit; do not call them operational feeds yet.
- **Farm economics:** [ERS income/expense files](https://ers.usda.gov/data-products/farm-income-and-wealth-statistics/data-files-us-and-state-level-farm-income-and-wealth-statistics) identify the **September 3, 2026 data vintage** and **December 2 next forecast**. They offer production-expense and crop-receipt tables. This is slow context, not a weekly fertilizer demand gauge. In contrast, [ERS Fertilizer Use and Price](https://www.ers.usda.gov/data-products/fertilizer-use-and-price) has old underlying tables: price data through 2014, price indexes through 2018, and mixed application vintages. A recent page date is not fresh underlying evidence.
- **World Bank / DTN / tender sources:** existing named instruments remain useful; the free weekly NOLA level gap is a **known, approved limitation** (WQ-257), not a new discovery or permission to buy data. WQ-466 C explicitly accepts labelled inference for India award-price grading; preserve it unless changed by Will.

## Deliberate boundaries — not defects to fill automatically

Potash is FERT-owned **at triage depth only**. MOS/NTR may supply relevant producer evidence without becoming equity coverage. Clean-ammonia-as-fuel expansion, paid Argus/ICIS/Profercy subscriptions, a phosphate equity expression, new threshold letters and automatic monitoring are proposals requiring their existing approval route. CF's already-owned low-carbon project cash commitments belong in its financial analysis; that does not make clean-ammonia fuel demand a new owned sector.

There is no need for a live trade file or an OPEN prediction merely to populate a template. The frozen trade record is correctly marked historical. A new prediction should express a useful base-rated claim, not satisfy a quota.

## Concrete next build — reviewable, not installed

1. **CF baseline before the November 4–5 results wake:** extract comparable recent quarters from issuer filings, build product-price/volume/cost/cash reconciliation, preserve plant and utilization denominators, list the Q3 questions. Acceptance: source-located values, comparable units, explained one-offs and no unsupported EBITDA sensitivity.
2. **Physical-flow pilot at existing N/P wakes:** prove one accessible monthly US import series and a China actual-export source, identify lag/unit/revision policy, add a dated issuer outage/restart sheet only where evidence is available. Acceptance: distinguish allocation from shipment and product tons from nutrient tons; UNKNOWN stays UNKNOWN.
3. **Small affordability/transmission baseline:** crop receipts/prices versus input expenses and intermediate PPI evidence, coordinated with CARL/HENRY/ISHM. Acceptance: distinguish farm margins, fertilizer-demand destruction and grocery-price pass-through; no causal label from simple co-movement.
4. **Finish correctness debt first:** review FL-06's stale restoration rationale and explicitly distinguish eligibility from sufficient attribution, classify stale KB rows and undeclared group labels, and file a truthful read-footprint declaration. These are separate from adding more live metrics.

No new standing monitoring protocol, thresholds, paid data or outside equity coverage is activated here. No decision is required just to receive this audit. Recommended priority is the existing CF lane, then physical flows.

## Verification and persistence

After repairs: TSV widths/unique IDs pass; STATUS remains under 250 lines and below 70% of the read budget; read-cap has the stated heuristic perimeter. Weekday and scoped whitespace checks pass. Consumer scans for the withdrawn cross-product comparison and corrected next-grade metadata were run both across desks and within FERT; no peer action is indicated by the exact superseded phrases. No source market price or gate letter changed. Other owners have dirty paths, so pull/stash/push are deferred; only own artifacts and the self-authored PROME packet are committed.
