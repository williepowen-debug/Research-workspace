---
signal_id: SIG-W-20260426-005
precedence: PRIORITY
timestamp: 2026-04-26T14:15:00Z
source: WALTER
origin: "Will Telegram image 2026-04-26 13:52 UTC (msg 1083) — @FirstSquawk verified-aggregator post ~Apr 25 2026 evening, 17K views: 'US FARM BANKRUPTCIES UP 46% YoY — 70% IN THE MIDWEST.' No primary citation in tweet. VERIFY-RESEARCH (general-purpose Sonnet ~$0.05) traced primary: American Farm Bureau Federation Market Intel analysis of US Courts Chapter 12 data, published February 2026. Investigate Midwest secondary article."

to: CARL (ACTION — CONSUMER_CREDIT / LABOR / ag-credit-stress primary)
info: REGINALD, BROCK, RED, HENRY, NEXUS, PROME
group: —
dispatched: 2026-04-26T14:15:00Z
dispatch_note: "VERIFY-RESEARCH VERDICT: CORRECTED-FRAMING 0.75. The 46% YoY figure is CONFIRMED — Chapter 12 farm bankruptcies rose from 216 (2024) to 315 (2025) per AFBF analysis of US Courts data, +46%, published Feb 2026. The MATERIAL FRAMING ERROR is the '70% Midwest' claim. The Midwest accounted for 121 of 315 total filings = ~38% of national filings, NOT 70%. The 70% figure is the YoY GROWTH RATE of Midwest filings specifically (i.e., Midwest filings grew ~70% YoY), conflated by FirstSquawk with share-of-total. Primary AFBF source confirms both numbers but their framings are distinct. This is Chapter 12 (family-farmer reorganization) only, not Ch11 or all chapters. CARL primary because ag-credit stress = consumer-credit-adjacent signal (farm households) AND LABOR-adjacent (rural employment). REGINALD secondary because regional bank ag-loan exposure (esp. Midwest community banks not in KRE but mechanics inform regional credit health). BROCK secondary on AgFinance-paper credit pricing. HENRY secondary — Ag-heavy regional banks fund via Farm Credit System + FHLB; spread movement matters. RED adversarial: bull rebuttal is mean-reverting (cyclical low ag prices, inflated input costs in 2024-25 reverse), bear is structural (commodity-price-trough-extending into 2026 + interest-rate-sensitivity-on-leveraged-farms). 2026 data through Q1 not yet visible."

signal_type: threshold-crossed
confidence: 0.75
confidence_language: assesses
resources: 1
safety_net: clear

word_count: 460

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: CONSUMER_STAGFLATION
---

## Signal

US Chapter 12 farm bankruptcies (family-farmer reorganization) rose from **216 in 2024 to 315 in 2025 = +46% YoY** per American Farm Bureau Federation Market Intel analysis of US Courts data, published February 2026. Midwest filings grew ~70% YoY (the strongest regional growth rate); Midwest's share of total 2025 filings was 121 of 315 ≈ **38% of national filings**, not 70%.

@FirstSquawk re-surfaced this on Apr 25 2026 in a multi-headline screenshot, with the framing "US FARM BANKRUPTCIES UP 46% YoY — 70% IN THE MIDWEST" — a conflation of regional growth rate with national share.

## Relevance

- **CARL (ACTION — CONSUMER_CREDIT / LABOR — ag-credit and rural-household primary):** Ag-credit stress is leading-edge consumer-credit-adjacent. Rural farm households are early in cycle for: (a) commodity-price-driven income compression, (b) input-cost squeeze (fertilizer / fuel / equipment financing), (c) interest-rate sensitivity on operating credit lines. The 46% YoY surge in Ch12 filings = primary-grade credit stress signal. CARL pickup work: cross-reference with USDA ERS farm income forecast, Federal Reserve Senior Loan Officer Survey ag-credit conditions, Farm Credit System impairment trends.

- **REGINALD (info — regional bank ag exposure):** Most Ch12 filings hit community banks more than KRE mid-tier regionals, but the mechanics of ag-credit stress inform regional credit health. Watch: (a) Farmer Mac (AGM) impairment trends, (b) ag-heavy regionals (Glacier GBCI, S&T STBA, Heartland HTLF). Cluster-side relevance for KRE/WAL/OZK only modest because their ag exposure is small, but transmission via correspondent-banking to community banks is real.

- **BROCK (info — AgFinance paper):** AgFinance ABS pricing, Farm Credit System debt pricing, AgriBank/CoBank wholesale debt are all relevant. Pricing reaction muted historically because Farm Credit benefits from GSE-like status, but stress-cycle transmission is real.

- **HENRY (info — funding):** Ag-heavy regionals fund via Farm Credit System + FHLB. Watch FHLB advance-rate spreads to community-bank classes.

- **RED (info — adversarial):** Bull rebuttal: 315 filings remains far below 2018-2020 cycle peak (~600+ Ch12 filings annually); cyclical-low-commodity-prices + inflated-input-costs are mean-reverting; 2026 USDA forecast assumes commodity-price recovery. Counter-counter: 46% YoY growth is the highest-acceleration print since 2019; structural farm-leverage build-up (avg farm debt at record nominal levels per USDA ERS); 2026 commodity-price assumptions optimistic.

- **NEXUS (info — cluster):** Connect to consumer-credit-stress meta-cluster building (CC delinq -007, FL LABOR -001, ag bankruptcies, pending Q1 2026 HHDC mid-May). Pattern: leading-edge stress in marginal sub-populations (rural / state-specific / sub-V business) before national average breaks.

- **PROME (info):** Coordinator awareness; ag-LABOR-cluster classification candidate.

## Caveats

- **Chapter 12 only, not all chapters.** Ch11 farm filings + Ch7 + non-bankruptcy distress (forced-sale, FSA workout) not included.
- **2024 baseline of 216 is below recent historical** — base-effect amplifies the YoY %. 2018-2020 peak was ~600+/yr; 315 in 2025 is recovery from 2024 trough, not new high.
- **Midwest 70% framing error must be flagged in dispatch_note** — this is the dominant CORRECTED-FRAMING pattern. Specifics imprecise, direction confirmed.
- **2026 data through Q1 not yet visible** — AFBF cycle is ~quarterly with Feb/Aug release cadence.
- **First Squawk aggregator** original post — primary-grade source verified via subagent.

## Source

- Will Telegram image 2026-04-26 13:52 UTC (msg 1083)
- @FirstSquawk verified, multi-headline screenshot
- Verify-research subagent (general-purpose, Sonnet, ~$0.05) — verdict CORRECTED-FRAMING 0.75
- Primary: AFBF Market Intel Feb 2026 — https://www.fb.org/market-intel/farm-bankruptcies-continued-to-climb-in-2025
- Secondary: Investigate Midwest Feb 25 2026 — https://investigatemidwest.org/2026/02/25/farm-bankruptcies-jumped-46-in-2025-as-debt-loads-and-costs-rise/
