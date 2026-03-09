# PROMPTS.md — Research Prompts for Will

Prompts for Will to run through external LLMs (multi-model cross-verification protocol).
Prome adds prompts here; Will picks them up and runs them.

---

## Queued

### ✅ DHS Shutdown Status Verification — COMPLETED
**Result:** CONFIRMED ONGOING as of Mar 9. Day 23+. Senate blocked House bill 51-45. 234K essential without pay, 26K furloughed. All claims prints since Feb 14 suppressed.
**Verified by:** Perplexity + Gemini (Mar 9)

### Google Trends — Labor Search Terms
**Priority:** 🟡 LABOR KB staleness
**⚠️ WILL MUST DO MANUALLY** — LLMs cannot access real-time Google Trends data. Go to trends.google.com directly.
**Prompt (for your own reference):**
```
Using Google Trends data for the United States, provide the current relative search interest (past 90 days trend) for each of the following terms:

1. "unemployment benefits"
2. "file for unemployment"
3. "laid off"
4. "severance package"
5. "hiring freeze"
6. "food stamps" / "SNAP benefits"
7. "job openings near me"

For each term, state: current week's index value (0-100), 4-week average, whether the 90-day trend is rising/flat/declining, and any notable spikes in the past 30 days. Compare current levels to the same period in 2025 and 2024 if possible.

Note if any terms show breakout or unusual patterns. These are used as real-time sentiment proxies for labor market stress.
```

---

### Taiwan Taipower LNG Buffer Status
**Priority:** 🔴 CRITICAL — Mar 10 potential exhaustion
**Run Monday morning before open**
```
What is the current status of Taiwan's LNG reserves and Taipower's natural gas supply as of March 9-10, 2026? Specifically:

1. How many days of LNG reserves does Taiwan currently hold?
2. Has Taipower issued any rationing notices, emergency procurement, or public statements about supply concerns related to the Hormuz Strait closure?
3. What percentage of Taiwan's LNG imports transit the Strait of Hormuz or originate from Qatar/UAE?
4. Are there reports of any industrial power curtailment or semiconductor fab impact (TSMC, UMC)?
5. Has Taiwan activated any emergency energy protocols or sought alternative supply (US, Australia)?

Cite sources with dates. This is time-sensitive — Taiwan's buffer was estimated at 7-11 days as of Mar 1.
```

### Oil $100 Breach — Downstream Impact Scan
**Priority:** 🔴 — Brent just broke $100 tonight (Mar 9)
```
WTI crude oil has surged past $100/barrel as of March 9, 2026 (Hormuz closure, Iraq 70% shut-in). Provide a current assessment of:

1. US national average gasoline price (AAA or GasBuddy, most recent)
2. Diesel/ULSD rack price trend over the past 7 days
3. Jet fuel spot price (Gulf Coast or NY Harbor) — current vs 30 days ago
4. Any airline announcements about fuel surcharges, route cuts, or capacity reductions since Mar 1
5. Any trucking/freight company announcements about surcharges or service changes
6. Fertilizer price changes (urea, DAP, potash) since Hormuz closure
7. US SPR status — any announced or rumored releases?

Focus on data from the past 7 days. Cite sources with dates.
```

### Kennedy-Wilson Bondholder Revolt
**Priority:** 🟠 — CRE can-kick failure signal (NEXUS C-17)
```
What is the current status of Kennedy-Wilson Holdings' (KW) debt exchange offer as of early March 2026? Specifically:

1. What are bondholders demanding vs what KW offered?
2. Has any bondholder group publicly rejected the exchange?
3. What are the key deadlines or court dates?
4. What is KW's current credit rating and any recent rating actions?
5. Are there comparable CRE companies facing similar bondholder resistance to debt exchanges?

This relates to the broader thesis that "extend and pretend" in CRE is breaking down. Cite sources.
```

### Gulf Fertilizer Supply Chain (NEXUS C-18)
**Priority:** 🟠 — Spring planting window NOW, not on consensus radar
```
Assess the impact of the Hormuz Strait closure (since March 1, 2026) on global fertilizer supply:

1. What percentage of global urea, DAP, and potash exports transit Hormuz?
2. India's dependency on Gulf-origin nitrogen fertilizers — what percentage and from which countries?
3. Current urea and DAP spot prices vs pre-closure levels
4. Have any major fertilizer importers (India, Brazil, SE Asia) announced emergency procurement or rationing?
5. What is the timeline pressure — when must fertilizer be procured for Northern Hemisphere spring planting to avoid yield impact?
6. 280 dry bulk carriers reportedly trapped — any confirmation of this number and impact on ag commodity shipping?

Cite sources with dates. This is a second-order effect of the Hormuz closure that is largely absent from mainstream financial coverage.
```

### BlackRock HLEND Gate — Contagion Tracking
**Priority:** 🟠 — First hard gate triggered Mar 6
```
BlackRock's HLEND ($26B private credit fund) formally gated redemptions on March 6, 2026, paying $620M of $1.2B requested. Provide an update:

1. Has BlackRock issued any public statement since the gate announcement?
2. Have any OTHER private credit funds (beyond BCRED and HLEND) announced redemption limits, gates, or liquidity restrictions since Mar 6?
3. What is the current status of Blackstone BCRED — are they still honoring 100% via employee capital injection?
4. Blue Owl OCSL II — status of the permanent liquidity freeze?
5. Any new BDC dividend cuts or NAV markdowns announced in the past week?
6. Regulatory response — has SEC or any regulator commented on the HLEND gate?

Cite sources with dates. Focus on events since March 5, 2026.
```

### ABS Baseline — Subprime Auto (14 CARL VX rows PENDING)
**Priority:** 🟡 — Overdue since Feb 15
```
Provide current auto loan ABS performance data as of the most recent available reporting (likely January or February 2026 remittance reports):

1. Subprime auto 60+ day delinquency rate (Fitch composite or S&P index)
2. Prime auto 60+ day delinquency rate
3. Net loss rate (annualized) for subprime auto ABS
4. Recovery rates on repossessed vehicles — current vs 12 months ago
5. Any new subprime auto ABS deals priced in Feb-Mar 2026? What were the subordination levels vs 2024 vintage?
6. Carvana (CVNA) / DriveTime ABS performance specifically — any trustee reports or rating actions?

This is for tracking the subprime auto ALL-TIME RECORD (7.1% 60+ DQ per Fitch Feb 2026). We need the trend, not just the level.
```

---

## Completed

### Indeed Job Postings (Mar 9)
4 LLMs: Gemini, DeepSeek, Perplexity, ChatGPT → KB-LAB-018 updated

### Cass Freight Index (Mar 9)
4 LLMs: Gemini, DeepSeek, Perplexity, ChatGPT → KB-LAB-043 updated

### Continuing Claims + JOLTS (Mar 9)
3 LLMs: Gemini, Perplexity, ChatGPT (DeepSeek skipped) → KB updated

### PSEC PIK Verification (Mar 9)
4 LLMs: Gemini, Perplexity, ChatGPT, Kimi 2.5 → **35% CONFIRMED POISONED.** Actual 8.6%. KB-LAB-060, KB-LAB-071, VX-LAB-8.04, TRADE.md, RP-LAB-014 all corrected.
