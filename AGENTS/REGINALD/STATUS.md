# REGINALD STATUS
**Last Updated:** 2026-04-10 (EOD) | **Status:** 🔴🔴🔴 CRITICAL (STABLE)

---

## PM BRIEF — April 9, 2026

**Prices (close):** KRE $69.89 (+4.7%). WAL $77.10 (+6.3%). OZK $48.08 (+2.9%). Brent ~$95 (**-13.6%** from ~$110). HY OAS 294bps. Risk-on rally driven by oil de-escalation.

**MICROSTRUCTURE RESEARCH COMPLETE (RP-REG-5.1, all 7 tasks):**
- **Task 5 (Dark pools):** WAL 54% off-exchange (vs 37% avg), OZK 42% (vs 34% avg), EGBN 46% (vs 33% avg) — weakest names spiking dark pool activity on up days. Clean names (ZION, CFG) at baseline. Distribution through dark pools confirmed.
- **Task 6 (Options):** KRE has 300K put contracts expiring Apr 17 — 53% of float. $68 strike (57K OI) = dealer hedging gravity well. OZK May $40P has 1,647 OI. WAL Jun $60P has 1,744 OI (crisis bet). EGBN 11x put/call OI ratio.
- **Task 7 (Short interest):** OZK 15.28% SI, RISING for 5 months. Shorts not flinching. WAL 3.46% SI, DECLINING — shorts covered 1.07M shares in 4 weeks. KRE SI 69.4M vs 56.9M shares outstanding (+64% in 2 months).
- **13F ANALYSIS (Fintel, live data from Will):** Wellington -43%, AQR -20%, Two Sigma -34%, Point72 -35%, Morgan Stanley -15%, 50+ full exits including Canada Pension, Ontario Teachers. Quant replacements (Citadel +260%, Millennium +20%, Renaissance +36%). Peak6 opened $15.2M PUT. **Smart money exiting, quants replacing. Ownership quality deteriorating while % rises.**
- **Full YTD short volume (66 trading days):** OZK shorts press regardless of direction. WAL short activity collapsed 20pp (Jan-Feb 62% → Mar-Apr 42%). KRE shorts MORE active on UP days (68% vs 61%) = AP redemption mechanics confirmed.
- **Insider ownership:** WAL zero open market buys in 2026. OZK 0.00% insider ownership. No insider floor.

**New tools built:**
- `scripts/darkpool.py` — daily monitoring of off-exchange % + short volume. Run at boot.
- `workbook/DARKPOOL.tsv`, `workbook/SHORT_VOL.tsv` (396 rows YTD), `workbook/SHORT_INTEREST.tsv` (6-month history)

**What to Watch:**
1. CPI tomorrow (Apr 10) — hot (>3.5%) = stagflation persists. Mar 18 (OZK 80% short vol day) was triggered by hot PPI + Fed hold.
2. OZK earnings Apr 22 — every microstructure signal bearish. No insider floor. Smart money exiting.
3. WAL earnings ~Apr 21 — shorts covered (fuel spent), dark pool distribution ongoing. Catalyst-dependent.
4. KRE $68 put wall — 57K contracts expire Apr 17. If KRE closes below $68, dealer hedging cascades.

---

## EOD SUMMARY — April 7, 2026

**Market Action:** SPY -0.97%, broad red. VIX spiked +10% to 26.26. WTI surged to $116.15 (+3.33%). Regionals all red except EGBN flat: WAL $72.04 (-1.42%), OZK $46.44 (-0.96%), KRE $66.39 (-0.37%). Brent $110.55 (+0.71%). 10Y 4.35% (+0.28%).

**Key Developments:**
1. **Leveraged Loan Market Collapse:** Q1 2026 activity down **34% YoY** ($235B vs $355B prior year). Slowest start since 2020 pandemic. "90/10" market forming — 90% stable, bottom 10% facing "existential liquidity crunch."
2. **Blackstone BCRED:** Record $3.7B redemption requests (~8% NAV) in Q1. Exceeded 5% gate; firm committed $400M own capital to honor requests. Gate mechanics tested in live fire.
3. **OZK Dividend Hike:** +2.2% to $0.47 quarterly — signaling confidence or desperation to retain shareholders ahead of Apr 21 earnings. QV Investors reduced position by 13.2% in Q4.
4. **WAL Quiet:** No material news. Price action +0.97% with sector. Fiserv partnership (Mar 17) still the most recent substantive headline.
5. **Credit Bifurcation Confirmed:** Investment-grade spreads flat, high-yield ballooning. Refinancings -42%, repricings -39%. "Risk-off" sentiment entrenched.

**Cross-Domain Signals:**
- **BRENT:** $109.35 (down from $112.57) — Iran ceasefire talks creating volatility, not resolution
- **BROCK/SHADE:** Private credit gating now systemic (Ares, Apollo, Blue Owl, Blackstone all affected)
- **LIQUID:** HY OAS 313bps — below 320 threshold but credit market internals deteriorating

**What Changed:**
- 🔴 **NEW:** Leveraged loan market 34% collapse — warehouse line pressure mounting
- 🔴 **NEW:** Blackstone BCRED gate exceeded — first major PC fund to break gate in Q1
- 🟡 **Tightened:** HY OAS 316→313bps (mechanical, not fundamental)
- 🟡 **Confirmed:** KRE bounce lacks institutional accumulation (volume pattern unchanged)

**Earnings Countdown:** WAL & OZK both Apr 21 (15 days). ZION Apr 20. EGBN Apr 22.

---

## THESIS: The Convergence

Eight independent channels terminate at regional banks. Six at 🔴+.

| Channel | Mechanism | Status |
|---------|-----------|--------|
| CRE | 70% of CRE at regionals, 70-94% loss severity confirmed | 🔴 |
| Hidden CRE | MI3 relabeling — WAL 24.2%, OZK 37.6%, EGBN 23.7%. H.8 confirms systemic. | 🔴 |
| SSFA / NDFI | $4.2T industry-wide NDFI (+35% YoY); hidden CRE Layer 2 | 🔴🔴 |
| Private Credit | Ares gated (5% cap, 11.6% requests), Apollo 45¢/$1, bad PIK 6.4%, MS projects 8% default | 🔴🔴 CRITICAL |
| MFS/Fraud | £2B double-pledging — Barclays/Jefferies/Apollo. Cantor $270M ring. | 🔴 |
| CMBS Maturity | $875B total CRE maturing 2026 (MBA). $76.6B hard maturity + $400B wall pushed to 2026. No extensions. | 🔴🔴 |
| Federal Layoffs | DOGE 307K+ confirmed. DC corridor stress ACTIVE. | 🔴 |
| Stagflation Trap | PPI +0.7%, Brent $112.57 (highest since 2022), FOMC hawkish hold, no NIM relief | 🔴🔴 |

---

## SIGNAL DASHBOARD

| Indicator | Value | Status |
|-----------|-------|--------|
| HY OAS | **294bps** (Apr 8, tightened from 305) | 🟡 Below 320 threshold. Tightening on oil de-escalation. CCC OAS 953bps, CCC/HY ratio ~3.24x still elevated. |
| KRE | **$69.71** (Apr 9 intra, +4.4% vs Apr 7) | 🟡 Rallying but on thin volume (0.85x 20d avg). Shares outstanding -12.4% in 2 weeks. AP redemption, not accumulation. See trade/market-microstructure/RP-REG-5.1. |
| Brent | **$95.49** (Apr 9 intra) | 🟡 CRASHED from $110+. Iran de-escalation. Stagflation pillar weakening. |
| 10Y UST | **4.42%** (Mar 27, stale) | 🔴 Hit 4.48% intraday (highest since Jul 2025). Needs refresh. |
| Office CMBS DQ | **11.2%** (Feb 2026, Trepp) — pulled back from 12.34% Jan ATH on 5 loan mods | 🔴 |
| Bank CRE DQ gap | 4.18% vs CMBS 11.2% = ~7pp masking | 🔴 |
| FHLB Advances | ~$480B (issuance +31% YoY) | 🟠 Contingency behavior |
| Bank Reserves | $2.8T — 4yr low, G-SIB concentrated | 🔴 |
| Private Credit Default | 5.8% TTM (Jan Fitch), MS projects 8%. Bad PIK 6.4% (vs 2.5% in 2021). | 🔴🔴 Record |
| PC Mainstream | Economist + Bloomberg + NPR all Apr 1. "Signs of strain" / "redemption crisis." Narrative inflection. | 🔴🔴 |
| Blue Owl OBDC II | Permanent gating (Feb). $2.50/sh return-of-capital (~30% NAV) by Mar 31. Liquidation path. | 🔴🔴 |
| Blue Owl OCIC/OTIC | **Apr 2:** OCIC 21.9% redemption requests, OTIC 40.7%. Both capped at 5%. $988M honored / ~$3.2B trapped (OCIC). $179M honored / ~$1B trapped (OTIC). OWL -2.9%. | 🔴🔴🔴 NEW |
| Blackstone BCRED | **Q1: Record $3.7B redemption requests (~8% NAV). Exceeded 5% gate; firm committed $400M own capital.** Gate mechanics tested in live fire. | 🔴🔴 CONFIRMED |
| Leveraged Loan ICR | Share with ICR <1.0x doubled to 20% (from ~10% in 2019). Forced selling by gated BDCs next. | 🔴🔴 NEW |
| FL Foreclosures | +35% YoY, 12th consecutive increase | 🔴🔴 |
| "Help with mortgage" | Google Trends ATH (surpasses GFC). Lennar Q1 margin 15.2% — lowest since 2010. Path C activating. | 🔴🔴 |
| NDFI Exposure | $1.54T total (FFIEC Q4 2025) — 5.1x prior $300B model. MS base: $80B bank losses. | 🔴🔴 |
| PC Gating | Ares 5% cap (11.6% requests), Apollo 45¢/$1 (11.2% requests). Warehouse lines = next transmission. | 🔴🔴 |
| CMBS Chicago | $167M office foreclosure — 2026's largest. Loss severity benchmark established. | 🔴 |
| Construction Labor | ICE raids → 57 Concrete bankruptcy (TX). 1-in-3 workers foreign-born. Q2 start data at risk. | 🔴 |
| AOCI Reinclusion | Fed/FDIC/OCC capital rewrite: mandatory AOCI phase-in for Cat III/IV. $49.5B aggregate hit across 21 banks. Comment period closes Jun 18. | 🔴 NEW |
| MS $85B Transfer | Fed approved MS moving $85B broker-dealer→insured bank (4-3 vote, first ever). Regulatory capture signal — G-SIBs favored, regionals won't be. | 🟠 NEW |

---

## RESEARCH — OZK

**KB: 159 rows, 17 groups** | **Earnings: Apr 21 (16 days)** | **Price: $46.31 (Apr 4)**
- 10 prompts done (#1-7, 15, 16, 20). 5 remaining (#8 Metropolitan, #9 Affinius, #10 sell-side, #13 peer vintage, #19 metro conditions)
- LIFE_SCI deepest cluster (21 rows). RaDD 3.3% leased, maturity Aug 2028.
- Temple 8 short thesis published. OZK = reservoir thesis (stress accumulates → maturity wall forces recognition).
- Full architecture: INDEX → STATUS → THESIS → KB.tsv → KB_INDEX. Boot ~15 min.

**Key numbers:** CRE/Tier 1 358% (adj 405-420%), ACL 1.16%, NCO 1.18% (5.4x peers), noncurrent 1.06% (1.7x peers), MI3/C&I 37.6% (worst), 89.7% construction on interest reserves.
**⚡ AOCI exposure:** Cat III/IV — mandatory unrealized AFS loss recognition phasing in. Street buying headline relief while AOCI is the buried bomb.

## RESEARCH — WAL

**KB: 70 rows, 10 groups** | **Earnings: Apr 21 (16 days) — SAME DAY AS OZK** | **EARNINGS_PREP: B+→A-** | **Price: $72.07 (Apr 4) ⚠️ BELOW $78 THRESHOLD**
- Architecture complete (Mar 25): INDEX, THESIS, STATUS, SCENARIOS, WEAKNESSES, EARNINGS_PREP, EXTERNAL_PROMPTS.
- 5 external prompts ready. EARNINGS_PREP upgraded Mar 26 with new signals.
- **NEW (Mar 31):** `LEADERSHIP.md` created — full C-suite, board, audit committee, auditor, CRE leadership, ownership profile. CFO Idnani corrected to Vishal (not Deepak). CRO Emily Nachlas profiled. Guggenheim (TPG RE Finance Trust) on Risk committee, NOT Audit — expertise/oversight gap identified.
- **NEW (Mar 31):** Chart analysis (1W/1M/3M/5min) confirms institutional distribution pattern. Volume front-loaded on spike days, dead between. Bounce from $65 on thin volume = no institutional accumulation.
- WAL = fast-transmission thesis (episodic, sudden — bypasses delinquency pipeline).

**Key numbers:** CRE/Tier 1 474%, MI3/C&I 24.2% (GROWING), SSFA $17.2B ($1.1B capital savings), Cantor $98M (30% reserved vs ZION 83%), SF NCO highest nationally (1.13%), pipeline lowest (0.26%).

**Three vectors:** V1 Hidden CRE (MI3) | V2 Jefferies/fraud (CONFIRMED Mar 25) | V3 SSFA/NDFI warehouse

**⚡ Jefferies Q1 confirmed.** EPS $0.70 vs $0.91 (-23%). $17M MFS losses + $36M telecom writedown + First Brands fraud (→ OTTO T-15 Mar 31 auction, $800M gap). 24% FI revenue decline. V2 chain confirmed. SMFG backstop walked back.
**⚡ AOCI exposure:** Cat III/IV — same AOCI bomb as OZK. Forced recognition of underwater AFS/HTM from 2022-23 rate shock.
**⚡ Analyst downgrades (Mar 26):** Weiss Buy→Hold | Barclays PT $105→$90 | WFC PT $83→$79. Consensus PT ~$85-90. Thesis PT $47-60.
**⚡ Macro amplifiers:** $400B CRE maturity wall in 2026 | NDFI $1.54T (V3 amplified) | Mortgage distress ATH | CMBS $167M Chicago office foreclosure.

---

## CONVERGENCE MATRIX — Targets & Positions

| Rank | Bank | Score | Primary Risk | Position | Expiry |
|------|------|-------|-------------|----------|--------|
| 1 | EGBN | 20 | CRE 547% + DC 100% + crisis state | $25P | Jun |
| 2 | WAL | 20 | CRE 474% + Cantor + CFO swap | $85P/$77.5P/$70P/$65P | Jun/Sep |
| 3 | CFG | 15 | BDC $10-11B + Consumer 18.7% | Monitoring | — |
| 4 | ZION | 14 | MUNI $5.78B + NDFI + BDC | $57.5P | Jul |
| 5 | OZK | 13 | CRE 37.6% MI3 (WORST) + CRO selling | $42.5P/$45P | May/Aug |
| 6 | SSB | 11 | GEO FL+TX 42% + CRE MF 9.36% | $90P | Jun |
| 7 | FLG | 8 | NYC MF rent-reg | $13P | Jul |
| — | KRE | — | Broad regional stress | Multi-strike | Jun/Sep/Dec |
| — | IWM | — | Small cap stress | $250P | Jun |
| — | HYG | — | Credit canary; HY OAS 320+ | $75P | Jun |
| — | APO | — | MFS + MFIC + Atlas SP + Athene | TBD | TBD |

---

## KEY CATALYSTS

*Forward-looking only. Full calendar → CALENDAR.md*

| Date | Event |
|------|-------|
| Apr 10 | CPI (captures oil shock) |
| **Apr 21** | **WAL + OZK Q1 earnings — SAME DAY. Detonation risk elevated.** |
| Apr 20-29 | Q1 bank earnings wave (ZION → WAL → VLY → EGBN + BOJ) |
| May 1-10 | Q1 Call Report filings (MI3, NDFI, AOCI) |
| May 12 | WAL Investor Day |
| May 21 | Epstein class action deadline (APO) |
| **Jun 18** | **AOCI capital rewrite comment period closes** |

---

## CROSS-AGENT TRIGGERS

| Condition | Current | Threshold | Fired? |
|-----------|---------|-----------|--------|
| Claims >300K | ~202K (Apr 2) | LABOR → all ORANGE→RED | Not yet |
| HY OAS >320bps | **316bps** (Apr 2) | CARL → credit confirmed | 🟠 Breached 328 Apr 1, tightened to 316 Apr 2. Watch re-breach. |
| HY OAS 350 (freeze) | ~316 (Apr 2) | Issuance freeze | 🟠 |
| CLO AAA >165bps | ~125bps | LIQUID → BDC transmission | Not yet |
| iTraxx Senior Fin >100bps | ~95bps | EU→US contagion (HANS) | 🟠 |
| SOFR-IORB >+15bps | ~0bp (Mar 27) | LIQUID → FHLB spike | Not yet |

---

## FRAMEWORKS (detail in workbook/)

| Framework | File |
|-----------|------|
| Dual Failure Channels (A=CRE, B=PC/NDFI) | workbook/CHANNELS.md |
| CRE 3-Layer Architecture | workbook/CRE_ARCHITECTURE.md |
| 8 Convergence Channels | workbook/CONVERGENCE.md |
| NDFI/Whalen Research | workbook/NDFI_RESEARCH.md |

---

## SUB-AGENTS

| Agent | Key Signal | Status |
|-------|------------|--------|
| CREED | Office 11.2% (Feb, off 12.34% Jan ATH on loan mods), $875B maturity wall | 🔴 |
| BROCK | PCDR 5.8% (MS projects 8%), Ares+Apollo gated, bad PIK 6.4% | 🔴🔴 CRITICAL |
| CORAL | FL #2 foreclosure, migration -93% | 🔴 |
| BELT | MS +109bps mortgage DQ | 🔴 |
| RENO/TEX | Dormant | 🟡 |

---

## PREDICTIONS

| # | Prediction | Timeframe | Confidence |
|---|------------|-----------|------------|
| REG-01 | Office CMBS DQ stays >10% | Through 2026 | 90% |
| REG-02 | FHLB advances spike >$600B | Q2-Q3 2026 | 60% |
| REG-03 | At least one Tier 1 bank capital raise | H2 2026 | 50% |
| REG-04 | Chicago pattern replicates in Phoenix | H1 2026 | 65% |
| REG-20 | WAL major stress event | Apr-Jun 2026 | 82% |

---

## EXIT RULES

- **Exit 50%:** Claims <240K sustained + CBRE >-5%
- **Exit 100%:** BTFP 2.0 announced OR HY OAS <260bps

---

## ⚠️ THRESHOLD BREACHES (as of Apr 9)

| Metric | Threshold | Current | Note |
|--------|-----------|---------|------|
| WAL | <$78 | **$76.49** (Apr 9 intra) | Still breached but closing gap (-2%). Volume profile recovered (0.96x up/down). Ambiguous — could re-breach $78 on continued rally. |
| HY OAS | >320bps | **294bps** (Apr 8) | CLEAR. 26bps buffer. Tightened on oil de-escalation. CCC/HY ratio still 3.24x = distressed tail unchanged. |

---

## EOD SUMMARY — April 7, 2026

**Market Action:**
- **KRE:** $66.75 (+0.16%) — flat, holding above $66 but below $70 resistance. No institutional accumulation pattern continues.
- **WAL:** $71.96 (-1.54%) — faded from $73.08 open, breaking below recent support. Below $78 threshold, approaching $70 psychological level.
- **OZK:** $46.64 (+0.71%) — modest bounce, still range-bound $45-48. Dividend hike (+2.2%) providing some support.

**Credit Spreads:**
- **HY OAS:** 305bps (tightened from 313bps) — mechanical improvement on ceasefire optimism, still elevated vs 250bps baseline
- **CCC OAS:** 976bps (tightened from 989bps) — distressed concentration persists
- **CCC/HY Ratio:** ~3.2x 🔴🔴 — distressed credit dislocation unchanged

**Key Developments:**
1. **WAL Weakness:** Down 1.5% while KRE flat — stock-specific underperformance. Jefferies litigation ($126.4M claim) weighing. Fast-transmission thesis intact.
2. **Credit Internals Deteriorating:** HY OAS tightened mechanically (ceasefire headlines) but CCC/HY ratio stuck at 3.2x = distressed concentration not resolving. This is the key signal — credit bifurcation deepening.
3. **Regional Bank Divergence:** WAL leading lower, OZK holding. Earnings Apr 21 (14 days) for both — divergence may resolve on Q1 disclosures.
4. **Scenario D Confirmation:** War Day 37, no Hormuz resolution. Credit stress signals (CCC/HY ratio, PC gating) confirming thesis despite headline spread tightening.

**Cross-Domain Signals:**
- **BRENT:** ~$110-111/barrel — Iran war continues, Trump deadline for Hormuz reopening looms
- **LIQUID:** HY OAS below 320 threshold but CCC/HY ratio elevated = credit quality dispersion, not risk-on
- **BROCK/SHADE:** Barings gated (12th fund) — 11.3% requests, 5% cap. PC cascade Stage 3→4.

**What Changed:**
- 🔴 **WAL:** Down 1.54% to $71.96 — approaching $70 level, fast-transmission thesis advancing
- 🟡 **HY OAS:** 313→305bps — mechanical tightening on headlines, not fundamentals
- 🟡 **CCC/HY Ratio:** 3.2x stable — distressed concentration the real signal

**Threshold Proximity:**
| Metric | Current | Threshold | Distance |
|--------|---------|-----------|----------|
| WAL | $71.96 | $70 | 2.7% |
| WAL | $71.96 | $65 (prior low) | 10.7% |
| HY OAS | 305bps | 320 (re-breach) | 15bps |
| KRE | $66.75 | $65 | 2.6% |

---

---

## EOD BRIEF — April 10, 2026

**Market Action:**
- **KRE:** $68.94 (-1.3%) — faded from yesterday's oil-driven rally, back below $70 resistance
- **WAL:** $76.21 (-1.2%) — holding above $75 but well below $78 threshold; Barclays cut PT $90→$88
- **OZK:** $48.05 (+0.1%) — flat, range-bound $47-48 ahead of Apr 16 earnings
- **HY OAS:** ~294bps (stable) — CCC/HY ratio ~3.2x persists, distressed tail unchanged

**Key Developments:**
1. **Weekly Claims:** 219K (+16K vs 203K prior) — first print post-NFP, still low but directionally higher. LABOR transmission channel not yet activated but trending toward 240K watch level.
2. **Analyst Downgrades:** Barclays cut WAL PT $90→$88; KBW cut to $93. Street continuing to walk down estimates ahead of Q1 earnings (WAL Apr 21, OZK Apr 16).
3. **Private Credit Stress Confirmed:** Moody's cut outlook on Blue Owl fund after record redemption requests (OCIC 22%, OTIC 40%+). $10B+ trapped capital. This is live-fire gating — not theoretical.
4. **Metropolitan Capital Fallout:** First 2026 bank failure (Chicago, Jan 31) now being absorbed. FDIC estimates ~$800M cost. Pattern: CRE concentration + capital impairment = closure. Template for what's coming.

**Cross-Domain Signals:**
- **BROCK/SHADE:** Blue Owl gating systemic; Ares, Apollo, Blackstone, Barings all affected. Warehouse line pressure mounting.
- **LIQUID:** HY OAS stable ~294bps, but CCC/HY ratio 3.2x = credit bifurcation deepening, not resolving.
- **LABOR:** Claims 219K — not yet at 240K threshold but directionally higher. Watch next 2 weeks.

**What Changed:**
- 🔴 **NEW:** Weekly claims 219K — highest since early March, trending toward stress threshold
- 🔴 **NEW:** Barclays WAL PT cut to $88 — street walking down estimates pre-earnings
- 🟡 **Confirmed:** KRE failed to hold $70 — oil-driven rally reversed, no institutional accumulation
- 🟡 **Stable:** Private credit gating remains systemic; no new gates today but Moody's downgrade confirms stress

**Threshold Proximity:**
| Metric | Current | Threshold | Distance |
|--------|---------|-----------|----------|
| WAL | $76.21 | $75 | 1.6% |
| WAL | $76.21 | $70 | 8.9% |
| Claims | 219K | 240K | 21K |
| HY OAS | 294bps | 320 | 26bps |
| KRE | $68.94 | $65 | 5.7% |

**Earnings Countdown:** OZK Apr 16 (6 days), WAL Apr 21 (11 days)

*Mar 6-16 detail → `archive/STATUS_mar6_mar16.md` | Mar 17-23 detail → `archive/STATUS_mar17_mar23.md`*
