# Gemini Deep Research — Private Credit Contagion Mechanics
**Source:** Gemini Deep Research, received Mar 25 2026
**Prompt:** Private credit contagion mechanics — "How does this actually break?"

## KEY FINDINGS

### 1. Four Transmission Channels (Mechanical)

**Channel 1 — Feeder Fund Liquidity Spirals**
- Liquid wrappers for illiquid assets create instant duration mismatch when master fund gates
- Fund-of-funds forced to sell LIQUID assets to meet redemptions → overweight in gated illiquid → "denominator effect in reverse"
- Blackstone injected ~$400M of own capital into BCRED feeder fund to avoid formal gate
- Creates "liquidity call" on remaining healthy funds in portfolio

**Channel 2 — Allocator Prisoner's Dilemma**
- When Fund A gates, allocators preemptively pull from Fund B (still open) to exit at current NAV
- Rational behavior: first mover gets capital at reported NAV, latecomers get gated
- Stress in retail vehicle (BDC) transmits to institutional drawdown fund because SAME allocators hold both
- 2022 UK LDI precedent: inability to redeem illiquid → forced sale of liquid public assets

**Channel 3 — Counterparty Haircuts / Margin Resets**
- Banks provide leverage via margin loans and repo secured by loan portfolios
- Gating signals questionable collateral valuation → synchronized margin requirement tightening
- Blue Owl forced sale at 99.7¢ created new "market mark" → banks reset LTVs industry-wide
- Funds must post more cash (which they don't have) or sell into thin market → further price depression

**Channel 4 — CLO Structural Triggers**
- Same loans sit in BDCs AND CLOs
- BDC downgrade (FSK Ba1) → rating agencies review same loans in CLOs
- If loans downgraded to CCC, count against CLO's 7.5% concentration limit
- Excess CCC valued at market (not par) for OC test → OC failure → cash flow diverted from equity/junior to senior
- CLO equity often held by the SAME BDCs already gating → feedback loop

### 2. The 2007 Analog — Month-by-Month Timeline

| Month | 2007 | 2026 |
|-------|------|------|
| 1 (Jun 07 / Jan 26) | Bear Stearns funds gate after 20% subprime losses | Multiple BDCs gate; Apollo, Ares restrict |
| 2 (Jul 07 / Feb 26) | Bear liquidates funds; mass MBS downgrades | BDC secondary discounts widen to 15%; BlackRock writes loan to zero ("first honest mark") |
| 3 (Aug 07 / Mar 26) | BNP suspends 3 funds; money markets freeze | **9 funds gated; Blue Owl margin call moment** ← WE ARE HERE |
| 4-6 (Q3-Q4 07 / Apr-Jun 26) | Citi, BofA reveal $10B+ writedowns from "liquidity puts" on CDOs | **PROJECTED:** Major banks report writedowns on NAV facilities; facility sizes reduced |
| 10 (Mar 08 / Oct 26) | Bear Stearns terminal run → sold to JPM | **PROJECTED:** First major PC manager insolvency or forced merger |
| 16 (Sep 08 / Apr 27) | Lehman collapse; Reserve Primary "breaks the buck" | **PROJECTED:** System-wide credit crunch; private + bank lending both freeze |

**Key analog mechanism:** 2007's "liquidity puts" connecting subprime to banks = 2026's NAV facilities and subscription lines connecting private credit to banks. Same structural flaw, different wrapper.

**Lag: 5 months from first gate to bank balance sheet impairment (2007).** Applied to 2026: major gating Mar → bank writedowns in Q2-Q3 earnings.

### 3. The Marks Problem

Three forces compel honest marks:
1. **Liquidation/fire sales** — Blue Owl's 99.7¢ sale establishes observable input. Auditors ask why identical loans elsewhere still at 100.
2. **Regulatory intervention** — SEC "target examinations" + CFCE statute (personal criminal liability for executives who manipulate collateral)
3. **Perceived arbitrage** — non-traded BDC reports 0.5% NAV loss while public peers trade at 20% discount. Investors stampede to exit at "par."

**2007 lag:** Private equity NAVs peak-to-trough 28%, but fully realized by Q1 2009 — 18-month lag from initial cracks. **Current cycle expected compressed** because semi-liquid BDC structures require more frequent reporting.

### 4. Bank Balance Sheet Exposure — Quantified

- Total bank + non-bank lending to US private credit: **$410-540 billion**
- Y-14 banks committed: $123B, with $30B specifically for BDCs
- Utilization: $74B (~60% of committed)
- Banks have **$2.8T in undrawn commitments** to non-deposit-taking financial institutions (NDFIs)
- Comparison: 2007 real estate was 53% of bank lending; BDC/PC is ~12.5% today
- MUFG: banks can absorb ~30% of BOJ JGB holdings before hitting risk limits (separate but related constraint)

**Breakdown points:**
1. LTV breach → margin call
2. Advance rate reduction (70% → 50%) → immediate partial repayment demanded
3. Non-renewal of subscription/warehouse lines at maturity
4. DB already exposed $30B in PC risk; stock dropped 6.1%

### 5. Six-Month Cascade Projection (Mar-Aug 2026)

| Month | Event | Indicator | Signal |
|-------|-------|-----------|--------|
| Mar (NOW) | 9 funds gated. Blue Owl margin call moment. | BDC discounts 20-25% | Haircuts reset industry-wide |
| Apr | Rating agencies downgrade cohort (FSK + Ares BDCs) | LSTA index <88 | CLO OC tests fail → dividend suspension for BDC-held equity |
| May | Pension Q1 marks revealed; true allocations way over target | Secondary LP interests >30% discount | Dry powder freeze — all new commitments halted |
| Jun | Gated funds draw down 100% of undrawn bank commitments | Bank CDS spike; NDFI utilization 50%→90% | Banks tighten all corporate lending to preserve capital |
| Jul | Mid-sized manager (Monroe/Cliffwater) fails margin call | HY OAS >800bps | Forced liquidation establishes market clearing price → 15-20% NAV markdown |
| Aug | Credit crunch reaches real economy | Middle-market M&A/IPO near-zero; software defaults spike | Fed forced to open PC liquidity facility or emergency cut |

### 6. CLO Structural Triggers — Specific Thresholds

| Trigger | Limit | What Happens on Failure |
|---------|-------|------------------------|
| CCC concentration | 7.5% of portfolio | Excess valued at market (not par) for OC test |
| Overcollateralization (OC) test | 105-120% depending on tranche | Interest/principal diverted from junior → senior |
| Interest Coverage (IC) test | Interest income > interest expense | All excess cash to senior principal |
| Event of Default (EOD) | Adjusted par < 102.5% of AAA par | **Forced liquidation of entire portfolio** |

~30% of middle-market BDC loans also financed via private/mid-market CLOs → valuation crisis in BDCs inevitably de-leverages CLOs.

## SOURCES
60 citations including Moody's, S&P, Oaktree, PGIM, Guggenheim, Invesco, AllianceBernstein, FCA, FASB, OFR, JPM Private Bank, State Street, BU research, IMF, Federal Reserve History, NAIC, multiple law firms (Simpson Thacher, White & Case, Macfarlanes, K&L Gates, Cleary Gottlieb)
