# CREED Domain Skeleton

**Agent:** CREED (Commercial Real Estate Exposure & Distress)
**Parent:** REGINALD
**Domain:** CRE Market-Level Monitoring
**Version:** 1.0
**Created:** 2026-01-27

---

## QUICK START

CREED monitors the commercial real estate market at the property and instrument level — delinquencies, valuations, modifications, maturities, fund flows, and regional concentration. REGINALD consumes CREED's output to assess bank-level CRE exposure. CREED does NOT track individual bank metrics; it tracks the market those banks are exposed to.

**Primary Question:** When does extend-and-pretend break, forcing recognition of CRE losses?

**Core Method:**
1. Track delinquency by property type and reporting channel (bank vs CMBS)
2. Monitor modification wave exhaustion (re-default rates, 2nd/3rd mod frequency)
3. Map maturity walls against refinancing capacity
4. Track open-end fund NAV drift and redemption pressure
5. Assess regional concentration and HOA/insurance amplifiers

---

## ENTITY TYPES

### Vectors (VX)
Quantifiable CRE market metrics tracked over time.

**Naming Convention:** VX-CREED-[Domain].[Number]
- Domain 1: DQ (Delinquency)
- Domain 2: MOD (Modifications)
- Domain 3: VAL (Valuations)
- Domain 4: MAT (Maturities)
- Domain 5: FND (Fund Flows)
- Domain 6: REG (Regional / HOA)

### Property Types
| Code | Type | Current Risk |
|------|------|-------------|
| OFF | Office | CRITICAL — 11.31% DQ, 20.5% vacancy |
| MF | Multifamily | ELEVATED — Sunbelt overbuilt, rent deceleration |
| RET | Retail | MEDIUM — Secondary markets weak, grocery-anchored stable |
| IND | Industrial | LOW — Logistics demand supports; 0.80% DQ |
| HTL | Hotel/Hospitality | ELEVATED — Leisure normalizing, business travel lagging |
| DC | Data Center | LOW — AI demand structural; supply constraints |

---

## RELATIONSHIP TYPES

### feeds
CREED market data feeds bank-level assessments.
```
[CREED Vector] feeds [REGINALD Vector]: [Mechanism]
Example: VX-CREED-1.01 feeds VX-REG-3.01: CMBS DQ leads bank DQ by 2-4 quarters
```

### masks
One metric conceals true stress in another.
```
[Metric A] masks [Metric B]: [Mechanism]
Example: Modifications mask true DQ: $7.7B modified to avoid NPL recognition
```

### forces
Structural deadline compels action.
```
[Maturity/Deadline] forces [Action]: [Timeline]
Example: 2026 maturity wall forces refinancing at repriced values: Q2-Q3 2026
```

---

## VECTOR REGISTRY

### Domain 1: DQ — Delinquency

**VX-CREED-1.01: Office CMBS Delinquency Rate**
- Description: 90+ day delinquency rate on CMBS office loans
- Source: Trepp
- Current: **11.31%**
- Status: **RED**
- History: Pre-COVID ~2%; peaked 10.7% in GFC
- Context: Exceeds GFC peak. Structural vacancy (remote work) not cyclical
- Thresholds: Y >5%, O >8%, R >10%
- Update: Monthly

**VX-CREED-1.02: Bank CRE 90+ Day Delinquency**
- Description: All CRE loans 90+ days past due at FDIC-insured banks
- Source: FRED (DRCRELEXFACBS)
- Current: **1.56%**
- Status: **GREEN** (but masked by modifications)
- Context: Large banks 1.86%, small banks 1.14%. Gap suggests different forbearance regimes
- Thresholds: Y >3%, O >5%, R >7%
- Update: Quarterly

**VX-CREED-1.03: Multifamily CMBS Delinquency**
- Description: 90+ day DQ on CMBS multifamily loans
- Source: Trepp
- Current: **~3.5%**
- Status: **YELLOW**
- Context: Sunbelt overbuilding driving stress; gateway cities stable
- Thresholds: Y >3%, O >5%, R >8%
- Update: Monthly

**VX-CREED-1.04: Office Vacancy Rate**
- Description: National office vacancy rate
- Source: CBRE, JLL, Cushman & Wakefield
- Current: **20.5%**
- Status: **RED**
- Context: Pre-COVID ~12%. Structural shift from remote/hybrid work. SF 36%, NYC 22%
- Thresholds: Y >15%, O >18%, R >20%
- Update: Quarterly

### Domain 2: MOD — Modifications

**VX-CREED-2.01: CRE Modification Volume**
- Description: Total CRE loans modified to avoid NPL recognition
- Source: Bank 10-Q/10-K footnotes (aggregated)
- Current: **$7.7B+ documented** (WFC $770M alone)
- Status: **ORANGE**
- Context: Banks modify distressed CRE to report as "current." Masks true DQ rates. Pattern: modify → report current → avoid provision → charge-off later
- Thresholds: Y >$5B, O >$7B, R >$10B
- Update: Quarterly

**VX-CREED-2.02: Modification Re-Default Rate**
- Description: % of modified CRE loans that re-default within 12 months
- Source: Bank disclosures, Trepp
- Current: **>50% on 2nd modifications**
- Status: **ORANGE**
- Context: WFC 10% annualized charge-off on CURRENT modified loans proves mods failing. FLG reduced allowances 142bps during stress = reverse indicator
- Thresholds: Y >30%, O >40%, R >50%
- Update: Quarterly

**VX-CREED-2.03: Modification Backlog**
- Description: Total CRE loans in modification pipeline or approaching exhaustion
- Source: Bank disclosures, MBA
- Current: **$24.5B backlog**
- Status: **ORANGE**
- Context: First mods expire → 2nd mods → exhaustion. Pipeline indicates future forced recognition
- Thresholds: Y >$15B, O >$20B, R >$30B
- Update: Quarterly

### Domain 3: VAL — Valuations

**VX-CREED-3.01: Office Price Index (Green Street CPPI)**
- Description: Commercial property price index — office sector
- Source: Green Street CPPI
- Current: **-30 to -40% from 2022 peak**
- Status: **RED**
- Context: Price discovery limited; few transactions. Appraisals lag reality by 6-12 months
- Thresholds: Y >-15%, O >-25%, R >-35%
- Update: Monthly

**VX-CREED-3.02: Cap Rate Bid-Ask Spread**
- Description: Gap between buyer and seller cap rate expectations
- Source: Real Capital Analytics, CBRE
- Current: **~150-200bps** (office)
- Status: **ORANGE**
- Context: Normal spread ~50bps. Wide spread = no price clearing. Transactions down ~60% from peak
- Thresholds: Y >75bps, O >125bps, R >175bps
- Update: Quarterly

**VX-CREED-3.03: CRE Transaction Volume**
- Description: Dollar volume of CRE transactions (all types)
- Source: Real Capital Analytics, MSCI
- Current: **~$350B annualized** (down ~55% from 2022 peak of ~$800B)
- Status: **ORANGE**
- Context: Low volume = broken price discovery. When forced sales resume, price gaps revealed
- Thresholds: Y <$500B, O <$400B, R <$300B
- Update: Quarterly

### Domain 4: MAT — Maturities

**VX-CREED-4.01: CRE Loan Maturity Wall**
- Description: Quarterly volume of CRE loans reaching maturity
- Source: Trepp, MBA
- Current: **$300-500B quarterly through 2026-2027**
- Status: **ORANGE**
- Context: Loans originated 2019-2022 at low rates now face refinancing at repriced values + higher rates. If >20% fail to refinance → systemic recognition
- Thresholds: Y >$250B/Q, O >$350B/Q, R >$500B/Q
- Update: Quarterly

**VX-CREED-4.02: CMBS Maturity Default Rate**
- Description: % of maturing CMBS loans failing to pay off at maturity
- Source: Trepp
- Current: **~25% office** (estimated)
- Status: **ORANGE**
- Context: Office worst; industrial/multifamily manageable. Maturity defaults force recognition that modifications delay
- Thresholds: Y >15%, O >20%, R >30%
- Update: Monthly

**VX-CREED-4.03: Office Lease Expiration Schedule**
- Description: Square footage of office leases expiring 2025-2028
- Source: CoStar, CBRE
- Current: **~15-20% of total stock expiring by 2028**
- Status: **YELLOW**
- Context: Tenants downsizing on renewal (avg -20-30% SF). Each expiration = potential vacancy increase + rent decline. Concentrated in gateway cities
- Thresholds: Y >12% expiring, O >18% expiring, R >25% expiring
- Update: Quarterly

### Domain 5: FND — Fund Flows

**VX-CREED-5.01: Open-End Fund Hidden Losses**
- Description: Estimated gap between reported NAV and market-clearing value in open-end CRE funds
- Source: ODCE, NCREIF, fund reports
- Current: **$130-217B**
- Status: **ORANGE**
- Context: BREIT gated for 1+ year (2%/mo cap). Bravern sale at -56% discount to appraisal validates shadow NAV. Pension funds (CalPERS, NYSTRS, Texas TRS, FL SBA) heavily exposed
- Thresholds: Y >$75B, O >$125B, R >$200B
- Update: Quarterly

**VX-CREED-5.02: Fund Redemption Queue**
- Description: Redemption requests as % of NAV across open-end CRE funds
- Source: ODCE quarterly reports
- Current: **12-13%** (down from 19.3% peak)
- Status: **YELLOW** (improving but still 3x historical)
- Context: Historical norm ~4%. Queues declining but still elevated. Any new stress reverses trend
- Thresholds: Y >8%, O >12%, R >15%
- Update: Quarterly

**VX-CREED-5.03: CRE CLO Issuance**
- Description: New CRE CLO issuance volume
- Source: Bloomberg, Trepp
- Current: **~$15B YTD** (down from ~$45B peak)
- Status: **YELLOW**
- Context: Declining issuance = tighter CRE credit. Existing CRE CLOs face collateral quality deterioration. Refinancing gap widens
- Thresholds: Context-dependent (declining = tighter credit)
- Update: Quarterly

### Domain 6: REG — Regional / HOA

**VX-CREED-6.01: HOA/Condo Special Assessments**
- Description: Special assessment severity in FL and NV condominium markets
- Source: County records, FL DBPR
- Current: **>$10K/door documented** in FL
- Status: **ORANGE**
- Context: Florida SB 4-D mandates structural reserves. Super-lien priority means HOA lien ranks AHEAD of mortgage. Bank LGD increases substantially. Insurance premiums +50% YoY amplify
- Thresholds: Y >$5K/door, O >$10K/door, R >$15K/door
- Update: Ad-hoc (event-driven)

**VX-CREED-6.02: Office-to-Residential Conversion Pipeline**
- Description: Square footage / units in active office-to-residential conversion
- Source: CBRE, local planning departments
- Current: **~70M SF announced** (~45K units); <15% completion rate
- Status: **GREEN** (aspirational, not material)
- Context: Conversion economics rarely work (cost $400-600/SF vs new build $300-500/SF). Only viable for specific building types. Will NOT solve vacancy at scale
- Thresholds: Context-dependent
- Update: Semi-annual

**VX-CREED-6.03: Construction Starts (CRE)**
- Description: New CRE construction starts by property type
- Source: Census Bureau, Dodge Data
- Current: **Office -65% from peak; MF -40% from peak**
- Status: **GREEN** (supply correction happening)
- Context: Reduced construction is positive for future supply-demand balance but takes 2-3 years to impact vacancy. Industrial and data center remain active
- Thresholds: Context-dependent (declining = future positive)
- Update: Monthly

---

## TRANSMISSION PATHS

### FLOW-CREED-01: CRE Doom Loop
```
Speed: QUARTERS (slow burn, then sudden)
Status: ACTIVE

Office Vacancy Structural Shift (20.5%)
  → Property Values Decline (-30-40%)
  → Loan-to-Value Ratios Deteriorate
  → Modifications Attempted ($7.7B+)
  → Re-defaults (>50%)
  → Forced Recognition
  → Bank Provisions Spike
  → [→ REGINALD: Bank earnings collapse]

Trigger: Modification exhaustion (>60% re-default)
Inherited from: FLOW-REG-2.01
```

### FLOW-CREED-02: Maturity Wall Cascade
```
Speed: QUARTERS (2026-2027 concentrated)
Status: ARMED

$300-500B Quarterly Maturities
  → Refinancing at Higher Rates + Lower Values
  → LTV Breach → Equity Call or Default
  → If >20% Fail → Systemic Recognition
  → Appraisals Forced Lower
  → Open-End Fund NAV Marks Down
  → [→ REGINALD: Bank balance sheet impairment]
  → [→ LIQUID: Refinancing demand on funding markets]

Trigger: >25% maturity default rate
Key Date: Q2-Q3 2026 peak maturities
```

### FLOW-CREED-03: Open-End Fund NAV Cascade
```
Speed: MONTHS
Status: ACTIVE

Redemption Pressure (12-13% queue)
  → Fund Gates (BREIT 2%/mo)
  → Forced Asset Sales at Discount
  → Transaction Prices Reveal True Values
  → Peer Fund Marks Down
  → More Redemptions (feedback loop)
  → Pension Fund Actuarial Losses
  → [→ REITS: Public vs private NAV gap]

Trigger: Queue >15% NAV or major forced sale
Inherited from: FLOW-REG-8.01
```

### FLOW-CREED-04: HOA Super-Lien Cascade
```
Speed: MONTHS
Status: ACTIVE (FL/NV)

SB 4-D Mandatory Reserves
  → Special Assessments >$10K/door
  → Owner Delinquency >10%
  → Super-Lien Foreclosure Filings (priority over mortgage)
  → Bank Recovery Impairment (LGD increases)
  → [→ REGINALD: Reserve builds required]
  → [→ MARCO: Regional housing stress]

Trigger: Foreclosure filings +50% YoY
Inherited from: FLOW-REG-6.01
```

### FLOW-CREED-05: Extend-and-Pretend Collapse
```
Speed: QUARTERS → DAYS (when it breaks)
Status: ACTIVE (slow)

First Modification → 12-Month Window
  → Re-Default (>50% rate)
  → Second Modification (backlog $24.5B)
  → Exhaustion (no more extensions possible)
  → Forced Recognition → Charge-Off Cascade
  → [→ REGINALD: Provision spike, earnings miss]

Trigger: Mod exhaustion >60%; FLG-type allowance cuts as canary
Key Signal: FLG reduced allowances 142bps during stress = reverse indicator
Inherited from: FLOW-REG-7.01
```

### FLOW-CREED-06: Lease Expiration Vacancy Ratchet
```
Speed: QUARTERS (structural, multi-year)
Status: MONITORING

Leases Expire 2025-2028 (~15-20% of stock)
  → Tenants Downsize -20-30% on Renewal
  → Effective Vacancy Ratchets Higher
  → Rent Decline on Renewals
  → NOI Decline → Debt Service Coverage Breach
  → Feeds into Maturity Wall (FLOW-CREED-02)

Trigger: Vacancy >25% national; any major metro >35%
Key Risk: SF already 36%; NYC 22% and rising
```

---

## THRESHOLDS SUMMARY

### Delinquency (DQ)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-1.01 | Office CMBS DQ | <3% | 3-5% | 5-8% | >10% | **11.31%** | **RED** |
| VX-CREED-1.02 | Bank CRE DQ | <2% | 2-3% | 3-5% | >7% | 1.56% | GREEN |
| VX-CREED-1.03 | MF CMBS DQ | <2% | 2-3% | 3-5% | >8% | ~3.5% | YELLOW |
| VX-CREED-1.04 | Office Vacancy | <13% | 13-15% | 15-18% | >20% | **20.5%** | **RED** |

### Modifications (MOD)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-2.01 | Mod Volume | <$3B | $3-5B | $5-7B | >$10B | **$7.7B+** | ORANGE |
| VX-CREED-2.02 | Re-Default Rate | <20% | 20-30% | 30-40% | >50% | **>50%** | **RED** |
| VX-CREED-2.03 | Mod Backlog | <$10B | $10-15B | $15-20B | >$30B | **$24.5B** | ORANGE |

### Valuations (VAL)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-3.01 | Office Price Index | >-10% | -10-15% | -15-25% | >-35% | **-30-40%** | **RED** |
| VX-CREED-3.02 | Cap Rate Bid-Ask | <50bps | 50-75bps | 75-125bps | >175bps | **150-200bps** | ORANGE |
| VX-CREED-3.03 | Transaction Volume | >$600B | $500-600B | $400-500B | <$300B | **~$350B** | ORANGE |

### Maturities (MAT)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-4.01 | Maturity Wall | <$200B/Q | $200-250B | $250-350B | >$500B | **$300-500B** | ORANGE |
| VX-CREED-4.02 | CMBS Mat Default | <10% | 10-15% | 15-20% | >30% | **~25% off** | ORANGE |
| VX-CREED-4.03 | Lease Expirations | <10% | 10-12% | 12-18% | >25% | **15-20%** | YELLOW |

### Fund Flows (FND)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-5.01 | Hidden Losses | <$50B | $50-75B | $75-125B | >$200B | **$130-217B** | ORANGE |
| VX-CREED-5.02 | Redemption Queue | <6% | 6-8% | 8-12% | >15% | **12-13%** | YELLOW |
| VX-CREED-5.03 | CRE CLO Issuance | Context | Context | Declining | Frozen | **Declining** | YELLOW |

### Regional (REG)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED | Current | Status |
|--------|--------|-------|--------|--------|-----|---------|--------|
| VX-CREED-6.01 | HOA Assessments | <$3K | $3-5K | $5-10K | >$15K | **>$10K (FL)** | ORANGE |
| VX-CREED-6.02 | Conversion Pipeline | Context | Context | Context | Context | 70M SF / <15% done | GREEN |
| VX-CREED-6.03 | Construction Starts | Context | Context | Context | Context | Off -40-65% | GREEN |

---

## STATUS SUMMARY

**RED (4):** Office CMBS DQ, Office Vacancy, Office Prices, Mod Re-Default Rate
**ORANGE (7):** Mod Volume, Mod Backlog, Cap Rate Spread, Transaction Volume, Maturity Wall, CMBS Mat Default, HOA Assessments, Hidden Losses
**YELLOW (4):** MF CMBS DQ, Lease Expirations, Redemption Queue, CRE CLO Issuance
**GREEN (3):** Bank CRE DQ (masked), Conversion, Construction

**Assessment:** Office is in outright crisis. The rest of CRE is in slow-burn extend-and-pretend that will break when maturity walls force refinancing at repriced values (Q2-Q3 2026). Bank-reported DQ (GREEN) vs CMBS-reported DQ (RED) is the single largest masking signal in the network.

---

## GLOSSARY

**CMBS:** Commercial Mortgage-Backed Securities
**Cap Rate:** Net Operating Income / Property Value (higher = cheaper)
**CPPI:** Commercial Property Price Index
**DQ:** Delinquency (90+ days past due)
**HOA:** Homeowners Association
**LGD:** Loss Given Default
**LTV:** Loan-to-Value ratio
**Maturity Wall:** Concentration of loan maturities requiring refinancing
**NOI:** Net Operating Income
**NPL:** Non-Performing Loan
**ODCE:** Open-End Diversified Core Equity (fund index)
**PIK:** Payment In Kind (non-cash interest)
**Re-Default:** Default after modification
**SB 4-D:** Florida Senate Bill 4-D (structural reserve mandate)
**Super-Lien:** HOA lien with priority over mortgage lien

---

*CREED Domain Skeleton v1.0*
*Created: 2026-01-27*
