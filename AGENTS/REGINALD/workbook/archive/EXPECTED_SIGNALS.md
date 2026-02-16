# REGINALD Expected Signals

**Purpose:** Pre-document expected signal types so they are recognized when they occur.

**Updated:** 2026-01-25

---

## Bank Sector Stress Signals

### KRE Decline

**What it looks like:**
- KRE down -10% (Yellow), -15% (Orange), -20% (Red) from recent peak
- May occur gradually (CRE concerns) or rapidly (individual bank crisis)

**Causes:**
- CRE loan loss recognition
- CLO mark-to-market losses
- Deposit flight concerns
- Individual bank failure contagion

**Response:**
- Alert SAM and LIQUID
- Monitor individual bank stocks for concentration
- Check for corresponding CLO spread widening

---

### Individual Bank Stock Crash

**What it looks like:**
- Single regional bank stock -20%+ in a day
- Often triggered by earnings miss, fraud disclosure, or deposit news

**Causes:**
- CRE loss recognition
- Deposit outflow disclosure
- Regulatory action
- Short seller report

**Response:**
- Alert LIQUID immediately (deposit run risk)
- Monitor other regional banks for contagion
- Check FHLB advance data if available

---

### VLY (Valley National) Crisis — #1 Watchlist Bank

**What it looks like:**
- VLY stock down -10% (Yellow), -15% (Orange), -20% (Red) from $12.18 high
- Q4 earnings miss with provision catch-up >$25M
- Auto NCO ratio disclosed above 6.65% (already breached)
- Analyst downgrades cascade (1-5 expected)

**Why VLY matters:**
- 475% CRE concentration (extreme)
- 6.65% auto NCO rate (BREACHED threshold)
- Dual exposure creates non-linear risk
- Q4 2025 earnings Jan 31, 2026 (5 DAYS AWAY)
- Old agent flagged as 9.5 vulnerability score (RED CRITICAL)

**Causes:**
- Provision catch-up forcing recognition of hidden losses
- Auto portfolio deterioration accelerating
- CRE losses compound with auto losses
- Market recognition of dual exposure risk

**Response:**
- Update VX-REG-6.02 status immediately
- Watch for deposit flight signals (FHLB advance spike)
- Alert LIQUID if CDS >325bps
- Monitor analyst commentary for "control failure" language
- Track peer regional banks for contagion

---

### FHLB Contagion Cascade — Systemic Amplifier

**What it looks like:**
- FHLB system advances spike above $700B (Yellow), $750B (Orange)
- FHLB announces collateral haircut increases (+5%, +10%, +15%)
- Multiple banks simultaneously increase FHLB dependency
- Regional bank forced asset sales at discounts

**Why FHLB matters:**
- Joint & several liability: all 11 FHLBs back each other
- 77.2% real estate collateral (49.4% SFR, 19.9% CRE, 10% MF)
- Peak advances $675B during 2023 crisis
- This is the "plumbing" that turns isolated failures systemic

**Transmission pathway:**
Bank stress → FHLB haircuts tighten → Forced asset sales →
CRE prices fall → Other bank collateral impaired →
Further haircuts → Cascade accelerates

**Response:**
- Update VX-REG-7.01 and VX-REG-7.02 status
- Map which banks have highest FHLB dependency
- Alert SAM on systemic implications
- Alert LIQUID on funding market stress
- Monitor for capital calls across FHLB member banks

---

### HOA/Condo Special Assessment Crisis — Regional Catalyst

**What it looks like:**
- Special assessments >$10K/door in FL or NV
- Owner delinquency rates >10%
- Super-lien foreclosure filings spike +50% YoY
- Insurance premium increases >50% YoY

**Why it matters:**
- Florida SB 4-D mandates structural reserves
- Super-lien priority means HOA lien ranks AHEAD of mortgage
- Bank LGD increases substantially on foreclosures
- Regional bank CRE collateral values impaired

**Response:**
- Update VX-REG-8.01 status
- Track county lien filing data
- Monitor insurance carrier exits in FL/NV
- Alert if bank portfolios have FL/NV condo exposure

---

### CRE Modification Exhaustion — Extend-and-Pretend Breaking

**What it looks like:**
- Bank reduces loss allowances during CRE stress (reverse of normal)
- Second modification rates exceed 40-50%
- Re-default rates on modified loans spike
- Charge-offs on "current" modified loans (WFC: 10% annualized)

**Why it matters:**
- $7.7B+ CRE loans modified to avoid NPL recognition
- >50% re-default rate on second modifications
- 24.5B modification backlog
- FLG reduced allowances 142bps = canary signal
- When modification runway exhausts, forced recognition cascade

**Mechanism:**
Modify loan → Report as current → Avoid provision →
12-month window expires → Re-default →
Second modification → Exhaustion →
Forced recognition → Charge-off cascade

**Response:**
- Update VX-REG-9.01 and VX-REG-9.02
- Monitor bank 10-Q footnotes for modification disclosures
- Track "modifications to borrowers experiencing financial difficulty"
- Alert if allowance reductions during stress (FLG pattern)

---

### Open-End CRE Fund NAV Cascade — Hidden Losses Revealed

**What it looks like:**
- Redemption queues exceed 15% of NAV (currently 12-13%, down from 19.3%)
- Fund imposes gates (BREIT 2%/mo cap for 1+ year)
- Forced asset sales at 40-60% discount to appraisal
- Shadow NAV calculations diverge from reported NAV

**Why it matters:**
- $130-217B hidden losses in open-end CRE funds
- Pension funds (CalPERS, NYSTRS, Texas TRS, FL SBA) have significant exposure
- Bravern sale at -56% discount validates shadow NAV risk
- When gates lift, forced sales cascade begins

**Transmission:**
Redemption surge → Fund gates → Forced sales at discount →
Shadow NAV revealed → Peer funds markdown →
Pension actuarial losses → More redemptions → Feedback loop

**Response:**
- Update VX-REG-9.03
- Track ODCE/BREIT quarterly redemption queue reports
- Monitor for forced asset sales (Callan, Trepp data)
- Alert if pension fund announcements on CRE allocation changes

---

### BDC PIK Earnings Inflation — Cash Divergence Signal

**What it looks like:**
- PIK interest exceeds 15-20% of total investment income
- Dividend appears "covered" but cash NII declining
- Dividend cut despite reported NII coverage
- Portfolio company defaults spike after high PIK period

**Why it matters:**
- Golub Capital PIK spike 173% YoY (confirmed in Q3 2025 10-Q)
- PIK = portfolio company pays with IOU, not cash
- BDC books as income despite receiving NO CASH
- Dividend cuts reveal "covered" as accounting fiction
- PUBLIC NARRATIVE DIVERGENCE: Blackstone blames cuts on Fed rate cuts (benign)
  SEC filings show reality: portfolio stress (severe)

**Response:**
- Update VX-REG-9.04
- Calculate PIK % for major BDCs (BCRED, BXSL, ARCC, TCPC)
- Track cash NII vs reported NII divergence
- Alert if PIK >15% across multiple BDCs = sector-wide issue

---

### Deposit Composition Stress — SVB Pattern

**What it looks like:**
- Uninsured deposit share exceeds 50%
- Brokered CD growth >30% YoY (hot money)
- Deposit beta exceeds loan beta (funding cost squeeze)
- Weekly outflows >2% of total deposits

**Why SVB pattern matters:**
- Confidence shock → Uninsured flee first
- Speed: days, not weeks
- Banks with high uninsured + CRE concentration = double exposure
- VLY, FLG, WAL are key watches

**Response:**
- Update VX-REG-10.01
- Monitor Q4 earnings for deposit composition disclosures
- Track Call Reports (mid-Feb) for deposit mix changes
- Alert LIQUID immediately if weekly outflows >2%

---

### RF (Regions Financial) Stress — CLO Bellwether

**What it looks like:**
- RF stock down -10% (Yellow), -15% (Orange), -20% (Red) from recent peak
- May precede or coincide with CLO spread widening

**Why RF matters:**
- $4.17B CLO holdings (13.5% of securities portfolio)
- 25-30% of Tier 1 capital at risk from CLO marks
- Single largest regional bank CLO concentration
- Early warning for CLO → regional bank transmission

**Causes:**
- CLO mark-to-market losses
- Credit cycle deterioration affecting leveraged loan prices
- Market anticipating CLO writedowns
- Earnings miss on CLO-related losses

**Response:**
- Update VX-REG-6.01 status
- Cross-check with CLO spreads (VX-REG-2.02) — are they widening?
- Alert SAM if CLO transmission confirmed
- Alert LIQUID if -20% (deposit run risk for RF specifically)
- Monitor KRE for sector contagion

---

### CLO Spread Widening (From SAM)

**What it looks like:**
- SAM signals CLO AAA >150bps
- CLOZ ETF confirms spread movement

**Causes:**
- Norinchukin selling
- Broad risk-off event
- Credit cycle turning

**Response:**
- Elevate VX-REG-2.02 to YELLOW/ORANGE
- Assess regional bank mark-to-market exposure
- Prepare for potential KRE impact

---

## Credit Quality Signals

### CRE Delinquency Spike

**What it looks like:**
- FRED data shows 90+ DQ >3% (Yellow), >5% (Orange), >7% (Red)
- Concentrated in office or specific geography

**Causes:**
- Office vacancy normalization
- Interest rate refinancing stress
- Borrower distress

**Response:**
- Update VX-REG-3.01
- Identify most exposed regional banks
- Watch for loan loss reserve announcements

---

### BDC NAV Discount Widening

**What it looks like:**
- BDC sector trading at >10% (Yellow), >15% (Orange), >20% (Red) discount to NAV
- Signals market skepticism about credit marks

**Causes:**
- Credit deterioration in BDC portfolios
- Anticipation of defaults
- Liquidity concerns

**Response:**
- Update VX-REG-2.03
- Monitor for credit line draws (affects regional banks)
- Coordinate with LIQUID on funding implications

---

## Funding/Deposit Signals

### Deposit Flight

**What it looks like:**
- Call Report shows deposits down >2% QoQ (Yellow), >4% (Orange), >6% (Red)
- May be system-wide or concentrated at specific banks

**Causes:**
- Safety concerns (SVB echo)
- Rate seeking (yield competition)
- Specific bank stress

**Response:**
- Alert LIQUID immediately if acute
- Monitor FHLB advance data
- Watch for Fed emergency actions

---

### FHLB Stress (From LIQUID)

**What it looks like:**
- LIQUID signals advance rate >85%
- FHLB debt issuance surge

**Causes:**
- System-wide deposit stress
- Multiple banks tapping emergency funding

**Response:**
- Coordinate crisis protocols
- Assess which banks are most dependent
- Monitor for Fed intervention signals

---

## Transmission Signals (From Coordinating Agents)

### From SAM

| Signal | Meaning | REGINALD Response |
|--------|---------|-------------------|
| CLO AAA >150bps | Mark-to-market risk begins | Elevate monitoring, assess bank exposure |
| Norinchukin selling | CLO supply hitting market | Prepare for price impact |
| JGB crisis acute | Japan stress may transmit | Watch for CLO contagion |

### From LIQUID

| Signal | Meaning | REGINALD Response |
|--------|---------|-------------------|
| SOFR spike | Funding costs rising | Monitor bank NIM compression |
| FHLB stress | System funding strain | Identify dependent banks |
| RRP depletion + shock | No buffer for flows | Heighten all monitoring |

---

## Counter-Signals (Stabilization)

| Signal | Meaning | Implication |
|--------|---------|-------------|
| KRE stabilizing/rising | Sector stress abating | Reduce monitoring intensity |
| CLO spreads tightening | Credit risk perception improving | Lower transmission risk |
| Deposit inflows | Bank funding stabilizing | Reduce FHLB stress concern |
| CRE loan modifications | Extend-and-pretend working | Slow-burn continues |
| Fed BTFP extension | Backstop available | Reduces acute run risk |

---

*REGINALD Expected Signals v1.0*
