# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-04-03 17:00 ET

**Positions → `PROME/POSITIONS.md`** | **Agent roster → `AGENTS_DIRECTORY.md`** | **Background → `WILL/BACKGROUND.md`**

---

## CORE DISCOVERIES (condensed — detail in linked files)

- **CCC/HY Ratio Downgraded (Mar 31)** — CCC OAS is concentrated (cable/media ~25%, PE-health ~15%), not broad systemic stress like 2007. Don't use CCC as standalone indicator — watch transmission channels (CLO→BDC→insurance) instead. Recovery rates 37.7% and 40% CCC borrowers <1.0x cash flow coverage remain genuine. → `FORGE/timing/thesis/CHANGELOG.md`
- **Timing Thesis Codified (Mar 31)** — Central call: acceleration May-Jul, cascade Q4, peak selling Q1-Q2 2027. 22 falsifiable predictions. → `FORGE/timing/thesis/`

- **Seven Depletion Clocks (updated Apr 3)** — 7 simultaneous physical supply depletions with hard deadlines. **Clock 2 CONFIRMED:** USDA corn -3% (-3.45M acres), farmers shifting to soybeans (survey understates — most responses pre-nitrogen spike). **Clock 3 RISING:** FAO +2.4% MoM, still ~20% below 2022 peak (159.7) — not crisis yet but directionally correct. FAO warns continuation if war persists. **Next:** Planting window mid-Apr (irreversible), China crude reserves mid-late Apr. Pharma APIs late May, helium late May-Jun. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **PE-Insurer Wholesale Funding (updated Apr 3)** — Athene now **#2 FHLB borrower in the country** ($23.3B, ahead of every major bank — Bloomberg Mar 25). FABR ($18B, repo-style) = fast fuse, pullable in days. FHLB has legal tripwire (12 U.S.C. 1831o bars advances without positive tangible capital). Increasing FHLB dependency = increasing fragility. → SHADE domain + `FORGE/timing/research/`
- **Oil Shock Is Structural (confirmed Apr 3)** — Infrastructure damage means prices can't normalize even with ceasefire. Rystad: **$25B repair bill**, some assets "offline for years." Floor WTI ~$80-85. No relief valve → Dec expiry strengthened. → `FORGE/research/iran-war/`
- **Hamilton Framework** — NOPI=47, GDP drag -3.0 to -4.9pp, peak lag4 Q1'27. Credit peaks BEFORE equity (~3mo lead). $4/gal = behavioral breakpoint. Jun=1/3 damage, Dec=peak. Roll Jun→Dec. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity (updated Apr 3)** — Fed buying ~$40B T-Bills/month since Dec '25, TBAC projects ~$540B total SOMA demand. Perli (Mar 26): reserve ampleness at Q1 2019 levels. Program ongoing with no changes (Mar 18 FOMC). Surface calm = intervention working, not health. 2019 repo parallel: breaks binary. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **IHAM Hidden Leverage (Mar 26)** — ARCC's CLO subsidiary is first-loss ($941M sub notes), 83% Level 3, losses growing while parent feeds it cash to buy more assets. Ares Mgmt reducing own credit exposure (-28%) while growing insurance (+59%) — insiders rotating away from the book. Template for what other PE-CLO subsidiaries may be hiding. Full detail in BROCK. → `AGENTS/BROCK/trade/ARES/sources/IHAM_FINANCIALS_FY2025.md`
- **PC Contagion Mechanics (updated Apr 3)** — Six-stage model: gate → cash substitution → financing tighten → honest marks → CLO spillover → bank impairment. **Now Stage 3 confirmed** — Blue Owl, BlackRock, Morgan Stanley all gating. Congress CRS report published (Apr 2). ECB + BOE launched emergency exploratory scenarios. Tripwire = fire-sale at 80-85¢. 2007 analog: 4-5 months gate→bank writedown = Q2-Q3 2026. → `AGENTS/BROCK/research/PC_CONTAGION_MECHANICS.md`
- **CARL Path C Activating (Mar 23, confirmed Apr 3)** — "Help with mortgage" Google Trends still at ALL-TIME HIGH (above 2008). Lennar Q1 2026 margin compression continues (17%→lower, from 25%+ pandemic peak). NEW: serious mortgage DQ (90+ day) at highest since 2022 (Mar 26). Multifamily CMBS DQ hit new ATH in March. Overall CMBS DQ 7.55% (+41bps). Housing cracking BEFORE employment — parallel stress paths, not sequential. Convergence 43/50. → `AGENTS/CARL/STATUS.md`
- **Ghalibaf + UST Demand Hole (Mar 23)** — Iran Parliament Speaker declared UST buyers "legitimate military targets." One-way ratchet: stigma gives Gulf SWFs political cover to reduce exposure. Four-anchor stress (Japan+China+Korea+Gulf), $70-135B/mo combined. TIC Apr 15 = first verification. → `AGENTS/ZHAO/STATUS.md` + `FORGE/research/iran-war/`
- **Japan: Structural Shift + BOJ (updated Apr 3)** — Multi-year regime change, NOT a calendar event. Life insurers shifting away from USTs (hedged return now negative). $50-120B annual swing from buyer to neutral/seller. BOJ hike is the real catalyst (next meeting Apr 23-24, ~35-40%), not FY-end flows. Repatriation alone doesn't reliably strengthen yen. Ueda: can hike even into weak growth. → `AGENTS/SAM/research/JAPAN_FYEND_REPATRIATION.md`
- **WAL + OZK: Complementary Shorts (Mar 25)** — WAL = fast-transmission (losses bypass delinquency pipeline → straight to P&L, SI 3.54% = uncrowded edge). OZK = reservoir (losses accumulate behind interest reserves, SI 13.81% = crowded). Different failure modes, different put expiry logic. OZK Q1 Apr 16, WAL Q1 Apr 21. → `AGENTS/REGINALD/STATUS.md`

---

## THESIS FRAMEWORK

- **NDFI Verified (Mar 26)** — $1.41T domestic, $1.57T consolidated. 77.6% growth in 2 years, 52.3% of Tier 1 capital, 86% in banks >$100B. This is how private credit losses transmit to bank balance sheets (Chain 2 → Chain 1 bridge). Loss range $73-138B. → REGINALD domain (`NDFI_HIDDEN_CRE_HYPOTHESIS.md`)
- **Ag Labor Data Gap (Mar 26)** — USDA Ag Labor Survey AND DOL NAWS both canceled. No official source for agricultural employment tracking. Permanent blind spot — relying on indirect signals (H-2A certs, self-deportation estimates, produce prices). → `AGENTS/MARCO/STATUS.md`

---

## SYSTEM ARCHITECTURE

*Operational procedures (inbox structure, spawn protocol, Toscanini, tools) → `PROME/BOOT.md`. Only genuine insights below.*

- **Domain audits via subagent spawn = high value.** Cold-boot agent reading the full domain catches staleness, orphan files, evidence gaps that the daily operator misses.
- **Three-source convergence method.** Perplexity + Claude + Gemini (deep research modes). Weight by methodology quality (primary data citations vs estimates).
- **CHANGELOG-first workflow.** Thesis files must never be edited without CHANGELOG.md entry first. Prevents silent drift.
- **Prome confidence ≠ Prome knowledge.** Tone doesn't change with coverage. Flag blind spots proactively.

