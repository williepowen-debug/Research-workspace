# HENRY equity cohort — delivered October19,2026

HENRY selection/window/matching task is complete; financing causality is untested. Fixed eight names are SNDK, COHR, STX, WDC, MGM, MOS, DELL and SMCI. This outcome-selected retrospective sample describes weak stocks; it cannot estimate a predictive debt-risk premium or explain the whole market. LIQUID owns the dated financing comparison.

## Fixed outcome and matches

Primary window: September18 close–October16 close,20 sessions. Adjusted-price returns below, including distributions; raw-price declines fixed selection. Secondary5/60-session windows startOctober9/July23, endOctober16. No endpoint moves.

|Weak name|Formation size proxy $bn|20-session adjusted return|Control|Weak−control pp|
|---|---:|---:|---|---:|
|SNDK|261.606|-27.49%|UNMATCHED|—|
|COHR|62.124|-26.61%|LITE|-15.142814809423568|
|STX|194.945|-25.53%|WDC|-0.7542148695770621|
|WDC|159.331|-24.78%|STX|0.7542148695770621|
|MGM|9.512|-24.36%|WYNN|-16.91495214213193|
|MOS|7.782|-23.12%|UNMATCHED|—|
|DELL|363.558|-20.48%|UNMATCHED|—|
|SMCI|25.678|-19.08%|HPQ|-6.322536099548483|

Five matched rows are only four unique industry comparisons: STX↔WDC is reciprocal, not two independent observations. SNDK/MOS/DELL remain unmatched; no caliper widening. Candidate audit and all5/20/60 raw/adjusted returns are machine-readable. COHR/LITE and MGM/WYNN differences are large; HDD relative difference is small. SMCI/HPQ qualifies only at broad hardware depth: AI servers vs PC/printing is a material product-mix confounder. These are candidate contrasts, not clean causal controls.

## Size and source rules

Size is September18 raw close × last period-end outstanding economic common shares publicly available before formation, with all equal economic common classes included. It is an estimate with a share-count lag, not certified exact September18 market cap. Do not use EPS weighted-average/diluted shares, issued shares including treasury, current market caps, enterprise value or later filings. `shares.json` records count, period, pre-window availability, exact source and class adjustment for all15 names. Original prices and counts retain float/rounding limitations.

LITE includes2.9M1:1convertible preferred with equal dividend/liquidation economics plus88.6Mcommon=91.5M; common-only size remains inside2x. DELL includes all640M A/B/C economic common shares. COHR SeriesB had converted by December2025. SMCI/HPE other preferred claims remain separate and must enter LIQUID's capital/funding reconciliation; common proxy is not fully diluted equity or EV.

Candidate choices were fixed by industry before financing comparison, then smallest absolute log-size gap subject to max/min≤2. Controls can themselves be weak. Single issuer industry pools are limited; an unmatched row means no eligible match in the fixed pool, not no possible company elsewhere.

|Weak|Candidate|Size ratio|Disposition|
|---|---|---:|---|
|SNDK|MU|4.384|outside2x|
|COHR|LITE|1.371|eligible|
|STX|WDC|1.224|eligible|
|WDC|STX|1.224|eligible|
|MGM|WYNN|1.126|eligible|
|MGM|LVS|2.723|outside2x|
|MOS|CF|2.488|outside2x|
|DELL|SMCI|14.159|outside2x|
|DELL|HPE|4.505|outside2x|
|DELL|HPQ|11.704|outside2x|
|SMCI|DELL|14.159|outside2x|
|SMCI|HPE|3.143|outside2x|
|SMCI|HPQ|1.210|eligible|

## Selection/exclusions and provenance

Universe503 issuer-SPY holdings security lines as ofOctober16, retrieved by WALTER October19; issuer-sector ETF mapping excludes financial/REIT sectors. ExactSeptember18/October16 raw closes rank losses, ticker breaks exact ties. SKYD's−32.32% vendor history is retained in `screen.json` but excluded: issuerOctober6 announcement says WBD acquisition completed and SKYD trading started then, so historical ticker/entity continuity and pre-window accounting require reconciliation. Initial PLAN August timing was wrong and explicitly corrected; exclusion rule/selected eight unchanged. ARE is excluded as REIT. Entire503-line audit retained.

Current holdings create survivor/membership bias. Outcomes were known at selection; no claim of historical investability or pre-registration before the price moves. Source is one Yahoo chart vendor, not exchange-certified prices. `constituent-snapshot.json` and sector CSV copied from WALTER's frozen read-only sources; own15 adjusted-chart pulls retained with receipts. WALTER universe source:https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx . SKYD primary:https://ir.paramount.com/news-releases/news-release-details/paramount-completes-acquisition-warner-bros-discovery-creating . Reproduction:`.venv/bin/python AGENTS/HENRY/research/2026-10-19_catchup/reconcile.py`; checks exact endpoints, fixed selected identities, complete candidate audit and approved fuel bar convention.

## LIQUID handoff and interpretation boundary

Use pre-September18 financing exposure, dated in-window refinancing/access/covenant changes and issuer outcomes. Retain zero/low-debt weak names and accessible refinancing as falsifiers; do not replace names on finding inconvenient funding facts. Exclude post-outcome debt data from the initial exposure label. Separate common-price loss from enterprise funding loss, earnings/product-cycle/AI-demand repricing and acquisition effects. No high-risk-minus-low-risk return estimate until LIQUID independently classifies financing and checks event clocks. Analysis-only artifact; no recommendation, standing monitor or capital action.

Cruise study stays a separate illustrative pair: CRUISE's fresh owner packet gives June30 liquidity/gross principal incl leases RCL29.37% vs NCLH~9.81%, return+12.97% vs+6.59% in this20-session window (both rose), and strong operating/transaction confounders. This is not CRU-11's October2–November14 test. Owner source:`AGENTS/CRUISE/research/2026-10-19_cushion/RESULT.md`; not independently rebuilt here.

## Late LIQUID first-pass receipt and source correction

Read `AGENTS/LIQUID/research/2026-10-19_equity-financing/COHORT-FUNDING.md` and its incoming packet. Financing evidence is heterogeneous: SNDK's nil July debt and September bank renewal counter a universal refinancing-loss explanation; STX retirement changes opening cash/debt, WDC conversion cash calls differ from contractual maturity, SMCI drawn lines/working-capital absorption suggest sensitivity without proving denied access. Controls have their own conditional/entity-specific funding. No completed exposure ranking or causal coefficient. These are LIQUID's dated primary-source findings, not an independent second financing study. Its final committed-version consumption remains pending this HENRY commit.

LIQUID correctly flagged my draft caveat implying outstanding WDC preferred. Direct re-read of WDCJuly3 10-K balance sheet/Note13 confirms NIL convertible preferred versus prior229M, converted duringFY2026. Corrected COHORT/PLAN/shares basis;361Mcommon count,formationcap and matches unchanged. SMCI/HPE preferred remain distinct claims. Source:https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm .
