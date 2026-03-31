# REGINALD — The Convergence Thesis
**Last Updated:** 2026-03-31

---

## The Claim

Regional banks are the convergence point of this cycle. Eight independent stress channels — each with different transmission speeds, different early warning indicators, and different pipeline visibility — all terminate at CRE-heavy regional balance sheets simultaneously. Any single channel is survivable. The convergence isn't. Banks with exposure to more channels have more paths to break, and multi-channel stress overwhelms capital buffers in ways that single-channel concentration does not.

The market prices regional bank risk as if it were one thing: CRE. REGINALD's thesis is that it is eight things arriving at the same place at the same time, and that the independence of those channels — not just their severity — is what makes this cycle different.

---

## 1. The Convergence — Eight Independent Channels

Each channel has a distinct transmission mechanism, speed, and set of early warning indicators. A bank's CRE risk team won't see fraud losses coming. A provision model won't anticipate an AOCI capital hit. Each channel has its own pipeline, and they don't share warning systems. This independence is the core danger.

| # | Channel | Mechanism | Speed | Status |
|---|---------|-----------|-------|--------|
| 1 | CRE Direct | Delinquency → NCO → provision drain | Slow (quarters) | 🔴🔴 |
| 2 | Hidden CRE (Memo Item 3) | Same as #1 but invisible in reported CRE ratios | Slow, hidden | 🔴 |
| 3 | NDFI / SSFA | Fund stress → warehouse line calls → bank losses | Medium (weeks-months) | 🔴🔴 |
| 4 | Private Credit | Gate/redemption → dividend cut → fund finance loss | Medium-fast (weeks) | 🔴🔴 |
| 5 | MFS / Fraud | Discovery → immediate charge-off, bypasses delinquency pipeline | Fast (days) | 🔴 |
| 6 | CMBS Maturity Wall | Hard deadline → forced recognition → bulk loss crystallization | Calendar-driven | 🔴🔴 |
| 7 | Federal Layoffs | Job loss → mortgage/consumer DQ → bank NCOs | Slow (months) | 🔴 |
| 8 | Stagflation Trap | Blocks rate cuts → no NIM relief → banks cannot earn through | Persistent | 🔴🔴 |

**The compound effect:** Channels 1-3 drain provisions from different line items simultaneously. Channel 5 bypasses provisions entirely (direct charge-off). Channel 8 prevents earning through losses. Channel 6 puts all of it on a calendar. Channel 4 impairs fund finance collateral on banking timelines (days-weeks), not real estate timelines (quarters).

All 8 channels are open simultaneously as of March 2026. Six are at 🔴 or higher.

### Channel Detail

**1 — CRE Direct.** 70% of all CRE loans sit at regional banks. FL foreclosures +35% YoY (12th consecutive increase). Manhattan office below COVID lows (Empire State $263/sqft vs COVID low $266; Vornado 20% below). Office stocks -12% YTD vs REIT market +11%. Office CMBS delinquency 11.2% (Feb, off ATH 12.34% Jan on loan mods). Bank CRE DQ 4.18% vs CMBS 11.2% = ~7 percentage point masking gap — banks haven't recognized what CMBS already has.

**2 — Hidden CRE.** Banks relabel CRE as C&I through FFIEC Memo Item 3 (RCON2746). Industry-wide: H.8 shows C&I +14.4% YoY while labeled CRE +1.1% (down from +5.9%). This is systemic reclassification. WAL 24.2% and GROWING (only bank with increasing ratio). OZK 37.6% (worst absolute). Metropolitan Capital failed at 39.6%. EGBN 23.7%. Full methodology in LESSONS.md and `domain/sources/`.

**3 — NDFI / SSFA.** $4.2T total bank NDFI exposure (+35% YoY, fastest-growing bank asset category per FDIC Q4 2025). NDFI is the Layer 2 wrapper: bank lends to private credit fund → fund lends to CRE → bank's CRE ratio stays low. WAL has $17.2B in SSFA-structured exposures at 20% risk weight, saving $1.1B in regulatory capital. If SSFA assumptions are scrutinized, capital adequacy drops immediately.

**4 — Private Credit.** Ares gated (5% cap, 11.6% redemption requests). Apollo selling at 45¢/$1 (11.2% requests). Blue Owl gated (Feb 23). BCRED near-gate ($3.7B Q1 redemptions). FSK dividend -31%. Bad PIK 6.4% (vs 2.5% in 2021). MS projects 8% default rate. The chain: fund stress → BDC NAV impairment → bank fund finance collateral degradation. CFG's $12.5B fund finance book (+40% YoY) is the primary transmission bridge.

**5 — MFS / Fraud.** £2B double-pledging across Barclays/Jefferies/Apollo. Cantor $270M ring (WAL $98M, ZION ~$100M charged off at 83%, others). Jefferies Q1 confirmed: EPS $0.70 vs $0.91 (-23%), $17M MFS losses, $36M telecom writedown, First Brands fraud. These losses bypass the delinquency pipeline — they appear as immediate charge-offs with no leading indicator.

**6 — CMBS Maturity Wall.** $875B total CRE maturing in 2026 (MBA). $76.6B hard maturity + $400B pushed forward from prior years. No extensions available when underlying collateral is below fraudulent baselines. Chicago $167M office foreclosure established 2026's loss severity benchmark. The maturity wall is a calendar-driven forcing function — banks cannot choose the timeline.

**7 — Federal Layoffs.** DOGE 307K+ confirmed cuts. DC corridor stress active. EGBN 100% DC exposure, already in crisis. Construction labor disrupted by ICE raids (1-in-3 workers foreign-born; 57 Concrete bankrupt in TX). Q2 housing start data at risk.

**8 — Stagflation Trap.** PPI +0.7% (hottest in 2+ years). Brent $112.57 (Hormuz closed since Mar 2, highest settle since Jul 2022). 10Y UST 4.42% (hit 4.48% intraday, highest since Jul 2025). FOMC hawkish hold. No rate cuts → no NIM relief → banks cannot earn their way through losses. The classic escape valve — the Fed rescues with lower rates — requires inflation to cooperate. It isn't.

---

## 2. The Architecture — Three Layers of Hidden CRE

REGINALD's original analytical contribution. The market debate is about CRE severity. The real question is CRE *exposure* — because reported exposure systematically understates true exposure through three independent masking layers.

### Layer 1 — Classification (Memo Item 3)

Banks relabel CRE loans as C&I using FFIEC Schedule RC-C Part I, Memo Item 3 (RCON2746): "Loans to finance commercial real estate activities not secured by real estate." If a CRE loan has a corporate guarantee or unsecured structure, it appears in the C&I line item on Call Reports.

| Bank | Memo3/C&I Ratio | Trend | True CRE (on-balance-sheet) |
|------|----------------|-------|----------------------------|
| OZK | **37.6%** | ↓ structural (C&I growing, diluting) | 71.5% |
| WAL | **24.2%** | **↑ GROWING** (15.5% → 24.2%, only bank with upward trend) | ~59% |
| EGBN | **23.7%** | — | — |
| Metropolitan (FAILED) | 39.6% | — | 61% labeled 10.7% |

**Screening methodology:** Pull FFIEC Call Report → Schedule RC-C Part I → Item 4 (C&I) → Memo Item 3 (RCON2746). Compute ratio. Flag >20%.

Metropolitan Capital failed Jan 30, 2026 with 61% true CRE exposure that was labeled 10.7% on regulatory reports. OZK's ratio is comparable.

OZK's CEO confirmed the relabeling mechanism: "Two criteria for moving out of construction category — CO + monthly amortizing feature" (Q3 2024). FDIC API confirms: C&I doubled (+153%) over 8 quarters while construction fell 36.9%. ~46% of construction decline migrated to C&I. This is quantitative proof of reclassification.

### Layer 2 — NDFI Wrapper

Bank lends $1B to a private credit fund (NDFI category on Call Reports). Fund deploys into CRE bridge loans. Bank's direct CRE ratio stays low because the loan is to a "financial institution," not to real estate.

Total bank NDFI exposure: $1.4T drawn + ~$2.8T undrawn = **$4.2T** (+35% YoY, per FDIC Q4 2025 via Whalen). This is the fastest-growing bank asset category. Banks are ADDING this exposure aggressively even as private credit begins to crack.

Layer 2 is CRE that doesn't show up as CRE anywhere — not in the CRE line, not in Memo Item 3 (which only catches direct CRE relabeled as C&I), not in any standard regulatory screen.

### Layer 3 — Collateral Fraud

The NOI figures that justified original CRE underwriting were inflated. Walker & Dunlop SEC admission: "systemic, and no longer anecdotal." Unicus Research mapped the pattern: infrequent appraisal verification, manipulable NOI statements and rent rolls, originate-to-distribute fee structures with minimal skin-in-game.

This means the collateral floor that normally backstops extend-and-pretend is fictional. When the maturity wall forces marks, banks discover they're underwater relative to a number that never existed.

### The Compound Effect

- Reported CRE understates true CRE (Layer 1)
- Additional CRE hides in NDFI lending (Layer 2)
- The collateral underlying ALL of it is overstated (Layer 3)

Each layer multiplies the others. A bank with 35% reported CRE may have 60%+ true CRE exposure (Layer 1), with additional hidden CRE in NDFI (Layer 2), against collateral marked to fictional NOI (Layer 3). Standard regulatory stress tests capture none of this.

---

## 3. Why Can-Kick Fails This Cycle

Every prior CRE downturn resolved through the same playbook: extend the loan, wait for asset values to recover, earn through losses via NIM. This cycle, all three escape routes are blocked.

### Structural Demand Destruction

Prior CRE downturns were cyclical — demand fell during recession, then recovered. This downturn has two structural legs:

- **Leg 1 (WFH):** Fewer days per week in office. Permanent behavioral shift, not recession-driven.
- **Leg 2 (AI):** Fewer workers needed at all. Headcount reduction means less space regardless of return-to-office mandates.

Manhattan office is below COVID lows. That wasn't a trough — it may be the new ceiling. Lab-to-office conversion is uneconomic at current cap rates. The demand that justified original CRE underwriting may not return within any extension timeline.

### No NIM Relief

PPI +0.7% (hottest in 2+ years). Brent $112+ (Hormuz closed). FOMC hawkish hold. The market has priced out rate cuts. Banks cannot earn their way through CRE losses via NIM expansion. The classic escape valve requires inflation to cooperate. It isn't.

### Fraudulent Baselines

Extend-and-pretend works when the asset eventually recovers to its real value. But Layer 3 means the original NOI never existed. Recovery requires *exceeding* a fictional baseline. You can't can-kick back to a number that was fabricated at origination.

### AOCI Reinclusion

The Fed/FDIC/OCC capital rewrite mandates phase-in of unrealized AFS/HTM losses for Category III/IV banks. $49.5B aggregate hit across 21 banks. Comment period closes Jun 18, 2026. Finalization likely H2 2026/Q1 2027. Banks that used HTM accounting to hide 2022-23 rate-shock losses will have to recognize them. This is a separate capital bleed on top of credit losses — hitting the same banks from a different direction simultaneously.

### Sponsor Fatigue

Banks have been extracting money from sponsors to keep loans performing. OZK collected $2.6B across 590 modifications ($1.3B equity injections + $866M reserve replenishments + $429M principal payments). But 59% of formally classified modifications re-defaulted anyway. Sponsor willingness to fund has limits, especially as the broader commercial real estate thesis deteriorates and sponsors' own fundraising environments tighten. The modifications are buying time, not solving the problem.

---

## 4. Dual Failure Channels

The WGA NDFI/PE chart revealed a critical insight: our target banks fail from CRE (Channel A), not from private credit (Channel B). These are genuinely separate failure modes with different banks, different timelines, and different catalysts.

### Channel A — CRE Transmission (Our Positions)

| Bank | NDFI/PE % | Primary Failure Mechanism |
|------|-----------|--------------------------|
| OZK | ~0.5% | CRE construction 37.6% hidden; 2022 vintage maturity wall Q1-Q3 2026 |
| WAL | ~0.2% | CRE 24.2% hidden + Jefferies fraud + CFO crisis hire + Cantor |
| EGBN | N/A | CRE 547% capital, 100% DC corridor federal job losses |
| ZION | N/A | MUNI $5.78B + CRE stress + Basis MF acquisition at peak |

These banks have minimal NDFI/PE exposure. They break from direct and hidden CRE — Layers 1 and 3 of the architecture.

### Channel B — PC/NDFI Transmission (Uninitiated)

| Bank | NDFI/PE % | Watch For |
|------|-----------|-----------|
| Stifel Bank | ~22% | First-order PE fund defaults |
| FCNCA | ~15% | Dual exposure: PC/NDFI + SVB legacy CRE |
| Axos Bank | ~12% | PC/NDFI direct |
| CIBC Bank USA | ~10% | PC transmission |

These banks break from private credit fund defaults flowing through NDFI lending relationships. FCNCA is a dual-channel candidate — both PC/NDFI (15%) and SVB legacy CRE.

### Channel B Bridge — CFG

CFG ($215B) straddles both channels. Its **$12.5B fund finance book** (+40% YoY, 10-K confirmed Mar 30) creates a direct bridge between shadow banking stress and traditional banking:
- Capital call facilities: $8.6B (LP-secured)
- Secured private credit finance: $4.0B (collateral UNSPECIFIED)

CFG is an amplifier, not a victim. It doesn't fail from its own CRE — it fails from the balance sheets of the funds it lends to. The $4.0B secured PC finance line is likely NAV-based and directly exposed to BDC stress. Growth of 40% YoY into a sector with 9 gated funds is aggressive concentration at cycle peak.

The Blackstone feedback loop: BCRED gates → Blackstone forced to sell leveraged loans → BDC spreads widen → CFG fund finance collateral impairs → the largest buyer of distressed bank CRE assets becomes unavailable to buy.

Channel B is a potential second trade we haven't initiated. Current positions are Channel A.

---

## 5. Target Theses

### OZK — The Reservoir

**Score: 13 | Primary: CRE construction | Price: $46.43 (Mar 27) | Earnings: Apr 16**

OZK is a slow-building reservoir of unrecognized CRE losses. Stress accumulates behind a dam of 590 loan modifications, classification management (Memo Item 3 ratio 37.6%, worst in screen), and interest reserves (89.7% of construction on reserves, but 100% of original reserves mathematically exhausted). You can see this one coming — the delinquency pipeline gives warning.

**Key numbers:** CRE/Tier 1 358% (adjusted 405-420%). ACL 1.26%, declining. NCO 1.18% (5.4x peers). Noncurrent 1.06% (1.7x peers). Q4 provision ($50.6M) covered barely half of Q4 losses ($98.3M). ACL/noncurrent coverage collapsed from 8.86x → 1.39x in two quarters.

**The maturity wall is the forcing function.** $3.7B maturing in 2026, concentrated in life sciences ($1.5B, vacancy 35%) and office. Three waves: Atlanta/FL/GA now (Sterling Bay Lincoln Yards seized, $265M sold to distressed buyer) → NY pipeline Q2 (0.41% 30-89 day, highest nationally) → IQHQ RaDD whale ($915M, 97% vacant, extended to Aug 2028).

**Adverse selection:** Record $7.24B RESG repayments in FY2025 (+19% YoY). Healthy loans already left. What remains at maturity is what couldn't refi.

**Regulatory oversight gap:** No holding company since ~2018. Supervised only by FDIC + Arkansas State Bank Department. No SEC or Fed oversight. The country's largest construction lender has less regulatory scrutiny than most peers its size.

Full thesis → `OZK/THESIS.md`

### WAL — Fast Transmission

**Score: 20 | Primary: Hidden CRE + fraud + SSFA | Price: ~$67-68 (Mar 27, BELOW $78 threshold) | Earnings: Apr 21**

WAL is the opposite of OZK. Losses don't build through a delinquency pipeline — they appear episodically and fast. SF district data proves the pattern: lowest 30-89 day pipeline (0.26%) but highest NCO rate (1.13%) of any FDIC district. The PDNA/NCO gap is the tightest nationally (0.54 pts) — losses are recognized immediately, not deferred. You cannot predict WAL's next blow from standard leading indicators.

**Three independent vectors, any one of which can fire:**
1. **Hidden CRE (V1):** Memo Item 3 ratio 24.2% and GROWING. CRE/Tier 1 474%. Management confirmed relabeling on Q4 call.
2. **Jefferies/fraud chain (V2):** CONFIRMED Mar 25. Jefferies Q1: -23% EPS, $17M MFS losses, First Brands fraud. Chain: fund stress → Jefferies/Barclays as intermediaries → WAL as lender.
3. **SSFA arbitrage (V3):** $17.2B structured at 20% risk weight, saving $1.1B in capital. If scrutinized, capital adequacy drops immediately.

**The CFO swap is the tell.** 22-year CFO moved to "VP Deposit Initiatives" (parking title) during CRE reclassification. Replaced by hire from JPM FIG (bank advisory/restructuring). Board added two risk specialists including former Truist CRO. Zero insider buying.

Full thesis → `WAL/THESIS.md`

### EGBN — Pure Concentration

**Score: 20 | Primary: CRE 547% + DC 100% | Position: $25P Jun**

The simplest and most binary thesis. CRE/Tier 1 at 547% with 100% geographic concentration in the DC corridor. DOGE federal layoffs hit this bank directly and exclusively. Already in crisis state.

### ZION — The Benchmark

**Score: 14 | Primary: MUNI + NDFI + CRE | Position: $57.5P Jul**

ZION serves dual roles: a position AND the honest-accounting benchmark. When ZION and WAL were hit by the same Stupin/Cantor fraud ring, ZION charged off 83% immediately while WAL reserved 30% and hasn't moved in 6 months. The divergence in response tells you about management credibility.

Hidden exposure: market sees $1.4B in muni securities. Actual total muni: $5.78B (+ $4.36B loans + $524M unfunded commitments). Just acquired Basis Investment Group agency MF lending (Fannie/Freddie) at cycle peak — adding CRE MF exposure at the worst possible time.

### CFG — Fund Finance Bridge

**Score: 15 | Primary: Fund finance $12.5B + consumer | Monitoring**

Not a CRE play. CFG is the transmission bridge between shadow banking stress and traditional banking. Its $12.5B fund finance book (+40% YoY) creates a direct channel through which private credit deterioration reaches the regulated banking system. The $4.0B "secured private credit finance" tranche has unspecified collateral — likely NAV-based, directly exposed to BDC stress.

11 Strong Buy, 1 Buy, 3 Hold, 0 Sell. No analyst is stress-testing fund finance against a private credit cycle. The risk is invisible to traditional bank analysis frameworks.

Full thesis → `CFG/THESIS.md`

---

## 6. The Timeline

The 2022 vintage maturity wall is the forcing function. Three-year initial terms + two one-year extension options = 2025-2027 is when extensions exhaust and recognition is forced.

| Date | Catalyst | Impact |
|------|----------|--------|
| **Mar 31** | First Brands auction ($800M gap) | Recovery data feeds BROCK + REGINALD |
| Apr 1 | eSLR relaxation effective | G-SIB capital relief, not regionals |
| Apr 10 | CPI (captures oil shock) | Stagflation confirmation |
| **Apr 16** | **OZK Q1 earnings** | First maturity wall test. "Elevated payoff velocity" guided. |
| Apr 20-29 | Bank earnings wave (ZION → WAL → VLY → EGBN) | Multi-bank stress confirmation window |
| May 12 | WAL Investor Day | Management narrative vs. data |
| May 21 | Epstein class action deadline (APO) | Private credit headline risk |
| **Jun 18** | **AOCI capital rewrite comment period closes** | Finalization likely H2 2026/Q1 2027 |
| Q2-Q3 2026 | 2022 vintage hard maturities peak | Calendar-driven recognition wave |

**Q1 earnings (April) is the first real test.** If 2+ Tier 1/2 banks miss in the same quarter, it confirms systemic stress rather than idiosyncratic. If provisions spike alongside CRE charge-offs, the extend-and-pretend dam is breaking.

---

## 7. Confirmation & Invalidation

### Confirmed If

| Signal | Source | Status |
|--------|--------|--------|
| FHLB advances >$650B | LIQUID | Not yet (~$480B, issuance +31% YoY) |
| 2+ Tier 1/2 banks miss earnings same quarter | Q1 earnings wave | Pending (Apr 16-29) |
| BDC dividend cut triggers bank fund finance stress | BROCK → CFG | Partially (FSK -31%, gates active) |
| Office DQ >15% AND bank provisions spike | CREED + earnings | Office 11.2%, provisions pending |
| HY OAS >320 sustained | CARL | Previously fired (hit 320-328), slight retreat to 317 |

### Partially Validated (as of Mar 31)

- Office CMBS DQ at 11.2% (off ATH 12.34%, still elevated)
- SLOOS C&I tightening confirmed
- BDC PIK elevated, multiple funds gated
- WAL below $78 threshold (analyst downgrades confirmed)
- Jefferies Q1 confirmed V2 fraud chain
- H.8 confirmed systemic CRE reclassification
- Manhattan CRE below COVID lows (structural, not cyclical)
- CFG 10-K confirmed $12.5B fund finance (+40% YoY)

### Invalidated If

| Signal | What It Means |
|--------|---------------|
| FHLB stays <$550B through 2026 | No funding stress = no crisis |
| Office DQ drops <10% sustained | CRE recovery underway |
| BDC dividends maintained, PIK declines | Private credit stabilizing |
| Employment stays strong (claims <230K) | Consumer buffer intact, no convergence |
| BTFP 2.0 announced | Government changes the rules — thesis may be right but trade breaks |
| HY OAS <260 sustained | Credit stress fully unwound |

### Exit Rules

- **Exit 50%:** Claims <240K sustained + CBRE vacancy improvement >-5%
- **Exit 100%:** BTFP 2.0 announced OR HY OAS <260bps sustained

---

## 8. Uncertainties

Honest accounting of what we're less certain about.

**Timing.** Banks have demonstrated remarkable ability to extend. OZK extracted $2.6B from sponsors across 590 modifications. Sponsor willingness may persist longer than modeled, especially if individual sponsors believe their specific assets will recover. The maturity wall creates a forcing function, but some banks could get another year of extensions.

**Systemic vs. Idiosyncratic.** H.8 data says CRE reclassification is industry-wide. But positions are concentrated in specific names. If the stress stays idiosyncratic — a few bad banks rather than a sector event — the broad hedges (KRE, IWM, HYG) underperform while single-name puts may still work.

**Government Intervention.** BTFP 2.0, another emergency facility, or targeted regulatory forbearance could extend the timeline significantly. The MS $85B transfer (Fed approved 4-3, first ever) signals regulatory capture favoring G-SIBs over regionals — but this doesn't mean regionals won't get emergency support if systemic risk materializes. Government action is the primary risk to position timing.

**Short Crowding.** OZK at 14-15% short interest with 12-18 days to cover. Squeeze risk is real on any positive earnings surprise (strong payoff quarter, better-than-expected provisions). The thesis is about trajectory across multiple quarters, but markets can stay irrational through several earnings cycles. Size accordingly.

**Channel B Timing.** We haven't initiated positions on PC/NDFI transmission banks (Stifel, FCNCA, Axos). The data is compelling (CFG 10-K confirmed $12.5B) but the catalyst timeline is less clear than for Channel A's maturity wall. Private credit fund failures could take quarters to flow through to bank fund finance losses.

---

## 9. Cross-Agent Dependencies

REGINALD is the convergence point. These agents feed the channels:

| Agent | Feeds Channel | Key Signal | Threshold |
|-------|--------------|------------|-----------|
| LABOR | #7 Federal layoffs, consumer | Claims level | >300K → all ORANGE banks escalate to RED |
| CARL | #4 Consumer credit, HY spreads | HY OAS, consumer DQ | OAS >320 = credit confirmed; >350 = issuance freeze |
| LIQUID | #3 NDFI/funding, FHLB | FHLB advances, SOFR-IORB | FHLB >$700B = early crisis; SOFR-IORB >+15bps |
| BROCK | #4 Private credit | PIK %, gating, dividends | Bad PIK >40% or major BDC dividend cut |
| SAM | Japan contagion | JGB selloff, CLO stress | CLO AAA >165bps = BDC transmission |
| CREED | #1 #6 CRE market-level | Office DQ, maturity data | DQ >15% = acceleration |
| CORAL | #1 Florida-specific | Foreclosures, HOA/SIRS | Citizens assessment trigger |
| OTTO | #5 Fraud intelligence | Audit findings, fraud rings | Cross-fraud pattern detection |

---

*Bank-level detail → `OZK/THESIS.md`, `WAL/THESIS.md`, `CFG/THESIS.md`, `ZION/THESIS.md`*
*Scoring methodology → `BANK_EXPOSURE_MATRIX.md`*
*Workbook frameworks → `workbook/CONVERGENCE.md`, `workbook/CHANNELS.md`, `workbook/CRE_ARCHITECTURE.md`, `workbook/NDFI_RESEARCH.md`*
*Validation criteria → `workbook/THESIS_VALIDATION.md`*
