# LIQUID DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Treasury Markets, Repo/Funding, SOFR, RRP, FHLB,
#          Global Liquidity, Cross-Currency Basis
# Agent:   LIQUID (Treasury/Funding Markets Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-25
# Author:  SAM Network Enhancement
#
# Usage:
#   - Load this file at the start of any LIQUID session
#   - Provides entity types, relationship vocabulary, core architecture
#   - Thresholds define tripwires for escalation
#
# Methodology Compliance: Aligned with CARL Methodology Skeleton v0.2

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This System

A **session** is one continuous LLM interaction window. Sessions are numbered sequentially (LIQUID-I, LIQUID-II, etc.). At session end, handoff documents transfer context to the next session.

**Two Documents:**
- **Domain skeleton** (this document): Defines *what* LIQUID monitors — entities, vectors, glossary, thresholds
- **Methodology skeleton** (separate): Governs *how* to operate — principles, protocols, templates

Load both at session start.

### Current Thesis

**PRIMARY THESIS: Funding Market Fragility — VALIDATED BY RESEARCH**

US Treasury/repo funding markets are structurally vulnerable:
1. **RRP DEPLETED** — Liquidity buffer exhausted (~$2.5B). Fed started RMP ($40B/mo).
2. **SRF CEILING POROUS** — Dec 31 2025: SOFR breached SRF by +12bps. GSIB constraints binding.
3. **FTD ELEVATED** — Settlement stress at $42.4B due to scarcity + clearing transition.
4. **DEALER CAPACITY CLOGGED** — Net long ~$200B. SLR prevents intermediation.
5. **MMF→HF TRANSMISSION ARMED** — $1.85T basis trade funded by MMF repo.

**Key Transmission Risks:**
- Japan institutional repatriation ($60-100B) hitting markets with zero RRP buffer
- Basis trade unwind: MMF stress → repo pullback → forced Treasury selling
- TGA rebuilds (April 2026) draining reserves without RRP cushion

**Confidence:** Pattern 90% | Timing 70% | Magnitude 85% (upgraded from 85/70/80)
**Status:** MONITORING — System transitioned to Fed-dependent regime

### Coordinating Agents

| Agent | Domain | State Vector Exchange |
|-------|--------|----------------------|
| **SAM** | Japan Sovereign, BOJ, JGB, Yen | VX-LIQUID ↔ Japan repatriation flows |
| **REGINALD** | Regional Banks, Credit, CLOs | VX-LIQUID ↔ Bank funding stress |
| **MASTER** | Cross-Domain Synthesis | Receives LIQUID stress indicators |

### Session Type Routing

| Session Type | Load Sections | Purpose |
|--------------|---------------|---------|
| Update | 0, 4 (thresholds) | Ingest new data, update logs |
| Analysis | 0, 3, 4 | Deep dive on specific mechanism |
| Crisis | 0, 4, 6 | Active funding stress monitoring |
| Reconciliation | 0, 4 | Cross-reference audit, cleanup |
| Handoff | Full skeleton | Explicit knowledge transfer |

---

## 1. ENTITY TYPES

*The vocabulary of the domain. Every node belongs to exactly one entity type.*

### Federal Reserve / Policy Entities

**Federal Reserve**
- Key properties:
  - `iorb_rate`: Interest on Reserve Balances (current: 4.40%)
  - `rrp_balance`: Reverse Repo facility balance (~$2.5B — depleted)
  - `qt_pace`: Quantitative Tightening rate
  - `fed_funds_target`: 4.25-4.50%
- Key actors:
  - **Powell Jerome** (Chair)
  - **Williams John** (NY Fed President — repo operations)

**Treasury Department**
- `auction_calendar`: Issuance schedule
- `tbill_supply`: Short-term supply pressure
- `cash_balance`: TGA (Treasury General Account)

### Market Infrastructure

**Repo Market**
- `sofr_rate`: Secured Overnight Financing Rate (3.67%)
- `sofr_iorb_spread`: SOFR minus IORB (key stress indicator)
- `repo_volume`: Daily transaction volume
- `tri_party_volume`: Tri-party repo activity

**FHLB (Federal Home Loan Banks)**
- `advance_rate`: Utilization of lending capacity
- `member_borrowing`: Bank draw on FHLB
- Key threshold: >85% advance rate = stress signal

**Clearing/Settlement**
- `ftd_total`: Fails-to-Deliver in Treasuries ($42.4B current)
- `ficc_volume`: FICC clearing activity
- `delivery_status`: Normal / Delayed / Failed

### Institutional Participants

| Type | Key Entities | Role | Stress Signal |
|------|-------------|------|---------------|
| Money Market Funds | Fidelity, Vanguard, BlackRock | RRP users, T-bill buyers | RRP outflows |
| Primary Dealers | JPM, GS, Citi, etc. | Auction intermediaries | BTC decline |
| Foreign Officials | Japan lifers, GPIF, China | UST holders | FX-driven selling |
| Hedge Funds | Basis traders | Relative value | Leverage stress |

---

## 2. RELATIONSHIP TYPES

*How entities connect. Every edge has exactly one relationship type.*

### Funding Relationships
- `borrows`: Entity obtains funding (Bank borrows from FHLB)
- `lends`: Entity provides funding (MMF lends in repo)
- `deposits`: Entity places reserves (Bank deposits at Fed)
- `draws`: Entity utilizes facility (Bank draws FHLB advance)

### Flow Relationships
- `sells`: Entity sells securities (Japan lifers sell UST)
- `buys`: Entity purchases securities (MMF buys T-bills)
- `settles`: Transaction clears (Trade settles via FICC)
- `fails`: Settlement does not complete (FTD recorded)

### Stress Relationships
- `transmits`: Stress propagates (SOFR spike transmits to FHLB)
- `amplifies`: Factor worsens stress (RRP depletion amplifies SOFR volatility)
- `hedges`: Risk mitigation (FX hedge covers Japan exposure)

---

## 3. TRANSMISSION PATHS (Named Cascade Routes)

*Documented pathways for funding stress propagation.*

### FLOW-LIQUID-1.01 — RRP Depletion Cascade

```
Speed: HOURS to DAYS
Status: CRITICAL — RRP at $2.5B (depleted)
Layer: 1 (Domestic Funding)

Pathway:
  RRP Balance Exhausted
    → Money Market Funds Must Deploy Cash Elsewhere
    → Increased T-bill Demand (yield compression)
    → OR Increased Repo Lending (SOFR pressure)
    → [IF SHOCK: SOFR Spikes Above IORB]
    → Banks Face Funding Stress
    → FHLB Advance Demand Surges
    → Credit Tightens

Trigger: RRP <$5B AND any flow shock
Current Position: ARMED — at $2.5B
Key Insight: Zero buffer for any significant flow event
```

### FLOW-LIQUID-1.02 — Japan Repatriation Transmission

```
Speed: DAYS
Status: ARMED — Awaiting trigger
Layer: 2 (Cross-Border)

Pathway:
  Japan Institutional Selling (GPIF, Lifers)
    → $60-100B UST Selling Pressure
    → Primary Dealers Must Absorb
    → Dealer Balance Sheets Stressed
    → SOFR Pressure (dealers need funding)
    → [RRP Depleted: No Buffer]
    → Credit Spread Widening

Trigger: USD/JPY >160 OR BOJ emergency action
Current Position: LATENT — 158.55 current
Key Insight: RRP depletion removes shock absorber
```

### FLOW-LIQUID-2.01 — FHLB Stress Cascade

```
Speed: DAYS to WEEKS
Status: LATENT
Layer: 1 (Domestic)

Pathway:
  Bank Deposit Outflows
    → Banks Draw FHLB Advances
    → FHLB Advance Rate Rises (>85%)
    → FHLB Issues More Debt
    → Crowding Out in Funding Markets
    → Broader Funding Stress

Trigger: Advance rate >85%, delivery status issues
Current Position: NORMAL
Key Insight: Hidden second-order stress path. REGINALD monitors.
```

### FLOW-LIQUID-2.02 — Basis Trade Unwind Cascade (NEW)

```
Speed: HOURS
Status: ARMED
Layer: 1 (Domestic/Leverage)

Pathway:
  Market Shock / Volatility Spike
    → MMF redemptions OR liquidity hoarding (WAM shortens)
    → MMFs stop rolling FICC Sponsored Repo
    → Hedge funds ($1.85T exposure) lose funding
    → Forced unwind of basis trade (short futures, long cash)
    → Massive cash Treasury selling
    → Dealers SLR-constrained, cannot absorb
    → Treasury prices crash, yields spike
    → VaR shock ripples through system

Trigger: SOFR spike + MMF WAM shortening + redemption pressure
Current Position: ARMED — $1.85T exposure, no RRP buffer
Key Insight: March 2020 "Dash for Cash" repeat but without buffer.
```

### FLOW-LIQUID-3.01 — SRF Ceiling Breach (NEW)

```
Speed: HOURS
Status: CONFIRMED
Layer: 1 (Domestic Funding)

Pathway:
  GSIB quarter-end/year-end constraints
    → Dealers shed repo exposure to manage Method 2 scores
    → Private repo liquidity evaporates
    → Non-dealers (hedge funds) cannot access SRF directly
    → SOFR trades ABOVE SRF rate (ceiling breached)
    → Segmentation: SRF-eligible vs non-eligible
    → Non-eligible borrowers pay penalty rates

Trigger: GSIB constraints + high collateral demand
Current Position: CONFIRMED — Breached Dec 31 2025 (+12bps above SRF)
Key Insight: SRF is porous ceiling, not hard cap. Expect at every quarter/year-end.
```

### FLOW-LIQUID-3.02 — Auction Failure Cascade (NEW)

```
Speed: HOURS
Status: LATENT
Layer: 2 (Treasury Market)

Pathway:
  Weak auction (BTC <2.10x, Tail >3bps)
    → Dealers forced to absorb large takedown (>30%)
    → Dealer balance sheets clogged
    → Secondary market bid-ask widens
    → Price discovery fails
    → Yield spike across curve
    → VaR shocks trigger risk-off
    → Credit spread widening

Trigger: BTC <2.0x AND Tail >3bps (Feb 2021 template)
Current Position: LATENT — Jan 2026 auctions healthy
Key Insight: 7Y tenor historically most fragile. Watch Jan 29 auction.
```

### FLOW-LIQUID-4.01 — TGA Drain Cascade (NEW)

```
Speed: DAYS
Status: LATENT
Layer: 1 (Reserve Management)

Pathway:
  Tax season (April) or large auction settlement
    → Cash flows from banking system to TGA
    → Without RRP buffer, drains reserves 1:1
    → Reserves could drop below $3T (LCLoR threshold)
    → Banks hoard reserves (LCR constraints)
    → SOFR spikes, SRF usage surges
    → Fed forced to accelerate RMP or emergency repo

Trigger: Tax season + RRP depleted + large TGA rebuild
Current Position: LATENT — April 2026 is key risk window
Key Insight: TGA sensitivity has returned now that RRP buffer is gone.
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

*All escalation thresholds. Updated 2026-01-25 based on exhaustive research.*

**Color Coding:** GREEN = Normal | YELLOW = Watch | ORANGE = Alert | RED = Critical

### CORE FUNDING INDICATORS

| Vector | Metric | Current | Yellow | Orange | Red | Status | Research Notes |
|--------|--------|---------|--------|--------|-----|--------|----------------|
| VX-LIQUID-1.01 | SOFR-IORB Spread | -1bp | +5bps | +15bps | +25bps | GREEN | VERIFIED 2026-01-25: SOFR 3.64%, IORB 3.65%. Post year-end normalization. Dec 31 breach was +12bps. |
| VX-LIQUID-1.02 | RRP Balance | $1.96B | <$50B | <$10B | <$5B | RED | VERIFIED 2026-01-25: H.4.1 "Others" (domestic) at $1.96B. Buffer = ZERO. Fed RMP ongoing. |
| VX-LIQUID-1.03 | Treasury FTD | $42.4B | $40B | $50B | $60B | YELLOW | Elevated due to clearing transition + scarcity. Monitor aged fails. |
| VX-LIQUID-1.04 | SRF Usage | $74.6B peak | >$25B sustained | >$50B sustained | >$75B sustained | ORANGE | **NEW** Record Dec 31 2025. Usage outside quarter-end = broken interbank. |
| VX-LIQUID-1.05 | Dealer Net Position | ~$200B | >$150B | >$200B | >$250B | ORANGE | **NEW** FR 2004 data. When stuffed = zero elasticity. Undervalued indicator. |
| VX-LIQUID-1.06 | Sponsored Repo Vol | ~$2.48T | Plateau | -$100B/week | Sharp decline | GREEN | **NEW** MMF→HF transmission. Contraction = deleveraging. |

### TREASURY AUCTION HEALTH

| Vector | Metric | Current | Yellow | Orange | Red | Status | Research Notes |
|--------|--------|---------|--------|--------|-----|--------|----------------|
| VX-LIQUID-2.01 | Treasury Auction BTC | 2.554x | <2.30x | <2.10x | <2.00x | GREEN | VERIFIED: Jan 13 10Y at 2.554x (vs 6-mo avg 2.51x). Strong. |
| VX-LIQUID-2.02 | Indirect Bid % | 69.5% | <60% | <55% | <40% | GREEN | VERIFIED: Jan 13 10Y at 69.5% (2nd highest ever). Yield 4.173%. |
| VX-LIQUID-2.03 | Auction Tail | Stopped through | >1.5bps | >3.0bps | >5.0bps | GREEN | VERIFIED: Jan 13 10Y stopped through. Watch Jan 29 7Y closely. |

### CROSS-BORDER FUNDING

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-LIQUID-4.01 | CCY Basis (USD/JPY) | -45bps | -60bps | -75bps | -100bps | GREEN |

### BANK FUNDING

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-LIQUID-3.01 | FHLB Advance Rate | Normal | >75% | >85% | Delivery | GREEN |

### LIQUIDITY & LEVERAGE (NEW CATEGORY)

| Vector | Metric | Current | Yellow | Orange | Red | Status | Research Notes |
|--------|--------|---------|--------|--------|-----|--------|----------------|
| VX-LIQUID-5.01 | MMF WAM | ~40 days | <30 days | <20 days | <15 days | GREEN | **NEW** Shortening = hoarding liquidity. |
| VX-LIQUID-5.02 | Basis Trade Exposure | $1.85T | >$1.5T | >$2.0T | >$2.5T | YELLOW | **NEW** Lagged SEC Form PF. MMF-funded leverage. |

---

## 5. VECTOR REGISTRY

*Full tracking in VX sheet. Updated 2026-01-25 based on research.*

### Layer 1: Domestic Funding

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-LIQUID-1.01** | SOFR Stress | GREEN | 90% | -1bp spread (verified Jan 25, post year-end normalization) |
| **VX-LIQUID-1.02** | RRP Depletion | RED | 95% | $1.96B remaining (DEPLETED, verified Jan 25) |
| **VX-LIQUID-1.03** | Settlement Stress | YELLOW | 80% | $42.4B FTD |
| **VX-LIQUID-1.04** | SRF Usage | ORANGE | 90% | $74.6B peak (record Dec 31) |
| **VX-LIQUID-1.05** | Dealer Capacity | ORANGE | 75% | ~$200B net long (stuffed) |
| **VX-LIQUID-1.06** | Sponsored Repo | GREEN | 80% | ~$2.48T (MMF→HF channel) |

### Layer 2: Treasury Market

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-LIQUID-2.01** | Auction Demand | GREEN | 90% | BTC 2.554x (Jan 13 10Y, verified) |
| **VX-LIQUID-2.02** | Foreign Demand | GREEN | 90% | 69.5% indirect (Jan 13 10Y, verified) |
| **VX-LIQUID-2.03** | Auction Tail | GREEN | 90% | Stopped through (Jan 13 10Y) |

### Layer 3: Bank Funding

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-LIQUID-3.01** | FHLB Stress | GREEN | 70% | Normal advance (REGINALD monitors) |

### Layer 4: Cross-Border

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-LIQUID-4.01** | CCY Basis Stress | GREEN | 75% | -45bps (SAM monitors Japan) |

### Layer 5: Liquidity & Leverage (NEW)

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-LIQUID-5.01** | MMF Liquidity Stance | GREEN | 75% | WAM ~40 days |
| **VX-LIQUID-5.02** | Basis Trade Exposure | YELLOW | 70% | $1.85T (lagged, funded by MMF repo) |

---

## 6. CURRENT WATCHLIST

*Updated 2026-01-25 based on research. System has transitioned to Fed-dependent regime.*

### RED STATUS (Immediate Action)

| Entity | Value | Note |
|--------|-------|------|
| RRP Balance | $1.96B | VERIFIED Jan 25: H.4.1 domestic "Others" category. Buffer = ZERO. |

### ORANGE STATUS (Enhanced Daily Monitor)

| Entity | Value | Threshold | Note |
|--------|-------|-----------|------|
| SRF Usage | $74.6B peak | >$50B sustained | Record Dec 31. Usage outside quarter-end = distress. |
| Dealer Net Position | ~$200B | >$200B | Dealers "stuffed" — zero elasticity for shocks. |

### YELLOW STATUS (Daily Monitor)

| Entity | Value | Threshold | Distance |
|--------|-------|-----------|----------|
| FTD | $42.4B | $50B Orange | $7.6B (85%) |
| Basis Trade | $1.85T | $2.0T Orange | $150B |
| CCY Basis | -45bps | -60bps Yellow | 15bps |

### GREEN STATUS (Weekly Monitor)

| Entity | Value | Note |
|--------|-------|------|
| SOFR-IORB | -1bp | VERIFIED Jan 25: Post year-end normalization |
| FHLB Advance | Normal | No stress (REGINALD monitors) |
| Auction BTC | 2.55x | Healthy (Jan 10Y) |
| Auction Indirect | 69.5% | Strong foreign demand (2nd highest ever) |
| Auction Tail | 0bps | Stopped through — excellent |
| Sponsored Repo | ~$2.48T | Peak levels — MMF→HF channel healthy |
| MMF WAM | ~40 days | Normal — not hoarding |

### HIGH PRIORITY UPCOMING DATES

| Date | Event | Risk Level |
|------|-------|------------|
| **Jan 29** | 7Y Note Auction ($44B) | **HIGH** — This tenor failed Feb 2021 |
| Feb 4 | QRA Announcement | HIGH — Q2 supply outlook |
| Feb 12 | 30Y Bond | MEDIUM — Duration test |
| April 2026 | Tax Season | **HIGH** — TGA drain without RRP buffer |

---

## 7. DATA SOURCES

*Updated 2026-01-25 with new critical sources from research.*

### Primary (OSINT - Daily/Weekly)

| Metric | Source | URL | Cadence | Priority |
|--------|--------|-----|---------|----------|
| SOFR Rate | NY Fed | newyorkfed.org/markets/reference-rates/sofr | Daily | HIGH |
| RRP Balance | NY Fed | newyorkfed.org/markets/desk-operations | Daily | HIGH |
| SRF Usage | Fed H.4.1 | federalreserve.gov/releases/h41 | Weekly (Thurs) | **CRITICAL** |
| Treasury Auctions | TreasuryDirect | treasurydirect.gov/instit/annceresult | Per auction | HIGH |
| FTD (Gross Fails) | DTCC/FICC | dtcc.com | Daily (T+1) | HIGH |
| FTD (CUSIP-level) | SEC | sec.gov/data/foiadocsfailsdatahtm | Bi-weekly | MEDIUM |
| Dealer Net Position | FR 2004 | newyorkfed.org/markets/gsds | Weekly (Thurs) | **CRITICAL** |
| MMF Assets/Holdings | ICI | ici.org/research/stats/mmf | Weekly | HIGH |
| Sponsored Repo Volume | OFR | financialresearch.gov/short-term-funding-monitor | Daily | HIGH |
| Treasury Cash Balance | Daily Treasury Statement | fiscal.treasury.gov/reports-statements | Daily | MEDIUM |

### Secondary (OSINT - Monthly/Quarterly)

| Metric | Source | Cadence | Notes |
|--------|--------|---------|-------|
| MMF Portfolio Holdings | SEC Form N-MFP | Monthly | WAM, asset allocation |
| Hedge Fund UST Exposure | SEC Form PF | Quarterly (lagged) | Basis trade proxy |
| QRA Supply Outlook | Treasury | Quarterly | Issuance projections |
| TIC Foreign Holdings | Treasury | Monthly (lagged) | Foreign demand confirmation |

### Proxy (OSINT - For Terminal Data)

| Terminal Data | OSINT Proxy | Source | Quality |
|---------------|-------------|--------|---------|
| CCY Basis (USD/JPY) | FX forward points | Investing.com | MEDIUM |
| Bank Funding Stress | FHLB debt issuance | Bloomberg News | LOW-MEDIUM |
| Real-time HF leverage | Futures open interest | CME | LOW (proxy only) |
| Repo specials | GC-special spread commentary | Market news | LOW |

---

## 8. GLOSSARY

### Acronyms

| Acronym | Definition |
|---------|------------|
| BTC | Bid-to-Cover (auction metric) |
| CCY | Currency |
| FHLB | Federal Home Loan Banks |
| FICC | Fixed Income Clearing Corporation |
| FTD | Fails-to-Deliver |
| GC | General Collateral (repo rate) |
| GSIB | Global Systemically Important Bank |
| IORB | Interest on Reserve Balances |
| LCLoR | Lowest Comfortable Level of Reserves |
| MMF | Money Market Fund |
| RMP | Reserve Management Purchases (Fed "not-QE") |
| RRP | Reverse Repo (Fed facility) |
| SLR | Supplementary Leverage Ratio |
| SOFR | Secured Overnight Financing Rate |
| SRF | Standing Repo Facility (Fed backstop) |
| TGA | Treasury General Account |
| UST | US Treasury |
| WAM | Weighted Average Maturity |

### Key Concepts

**RRP Depletion:** When the Fed's Reverse Repo facility drains to zero, money market funds must deploy cash elsewhere, removing a critical buffer for funding shocks. As of Jan 2026, RRP is effectively at zero ($2.5B). Fed responded with RMP.

**SOFR-IORB Spread:** The difference between SOFR (market rate) and IORB (Fed administered rate). Normally slightly negative; positive spread signals friction. Dec 31, 2025 saw +12bps above SRF rate—the SRF ceiling is POROUS.

**Standing Repo Facility (SRF):** Fed backstop that should cap repo rates. However, GSIB constraints prevent dealers from arbitraging, and non-dealers cannot access it. The ceiling is therefore porous during constrained periods.

**Basis Trade:** Leveraged arbitrage between cash Treasuries and futures. Current exposure ~$1.85T, funded by MMF repo via FICC Sponsored Repo. Unwind risk = Treasury selling cascade.

**Fails-to-Deliver:** When a party fails to deliver securities on settlement date. Current $42.4B level reflects: (1) high rate scarcity (4.3% failing cost), (2) central clearing transition friction, (3) SLR dealer constraints.

**Central Bank Balance Sheet Trilemma:** The Fed can only achieve 2 of 3: (1) Small balance sheet, (2) Low rate volatility, (3) Limited market intervention. By starting RMP, Fed chose #2 and #3, abandoning #1.

**GSIB Constraints:** Global Systemically Important Banks face Method 2 scoring that creates "cliff effects" at year-end. This causes aggressive repo withdrawal, explaining Dec 31 SRF breach.

**Sponsored Repo:** FICC program allowing MMFs to lend to clearinghouse, enabling netting that bypasses SLR. Critical transmission channel: MMF→FICC→Dealers→Hedge Funds.

**Auction Tail:** Difference between When-Issued yield and auction High Yield. Positive tail = weak demand. Feb 2021 7Y failure had +4.2bps tail. Most immediate signal of auction stress.

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-25 | Initial skeleton created |
| 2.0 | 2026-01-25 | Major update: 6 new vectors added (SRF, Dealer Position, Sponsored Repo, Auction Tail, MMF WAM, Basis Trade). Thresholds validated by research. New flows added. Thesis confidence upgraded (Pattern 90%, Magnitude 85%). |
| 2.1 | 2026-01-25 | Pre-auction verification: SOFR-IORB confirmed -1bp (normalized), RRP $1.96B (H.4.1), Jan 13 10Y auction strong (BTC 2.554x, Indirect 69.5%, stopped through). Jan 29 7Y flagged CRITICAL. |

---

*End of LIQUID Domain Skeleton v2.0*
