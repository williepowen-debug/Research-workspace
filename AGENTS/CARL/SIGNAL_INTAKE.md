# CARL — Signal Intake Spec

**Owner:** CARL | **Consumer:** WALTER (routing) | **Last Updated:** 2026-04-19
**Domain:** US consumer stress — credit DQ, housing, spending, K-shape bifurcation, multi-vector cost squeeze

*Living document. CARL updates when thesis evolves, thresholds change, or new vectors emerge. WALTER reads at routing time.*

---

## PRIORITY LEVELS

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 | Thesis-level, time-sensitive. Could breach a convergence vector or invalidation threshold. | Immediately |
| 🟠 | Important context. Informs analysis but not urgent. | Same day |
| 🟡 | Background. Useful but low urgency. | Batch weekly |

---

## 🔴 IMMEDIATE

### Credit DQ / Charge-offs
- **CC 90+ DQ**: any Fed Board / NY Fed QHDC release, card issuer monthly master trust filings (NCO, 30+, 90+)
- **Subprime auto 60+ DQ**: Fitch ATR updates, Santander/Exeter/Bridgecrest/Westlake/American Credit master trust data
- **Student loan 90+ DQ**: FICO score reports, NY Fed QHDC, Dept of Ed payment data, TransUnion / Experian student reports
- **Mortgage 90+ DQ / FC starts**: MBA Weekly Applications, ICE / Black Knight mortgage monitor, Fannie + Freddie monthly summaries
- **Issuer earnings with DQ commentary**: SYF, COF, ALLY, AXP, DFS, BFH (Bread), C (card segment), JPM (card segment)

### Housing Distress
- **ATTOM**: monthly + quarterly foreclosure reports
- **Fannie MF DQ**: monthly release (CRL-03 watch 0.80%)
- **Freddie MF DQ + K-series** deep dives
- **Trepp CMBS**: MF, office, retail DQ monthly
- **FHA / Ginnie** DQ / servicing transfers
- **HOMER-relevant builders**: DHI, PHM, LEN, KBH Q earnings / guide cuts
- **Mortgage servicer earnings**: Rithm / NewRez, PennyMac, Mr. Cooper, Ocwen

### Cost Squeeze (consumer-facing)
- **Gas pump national avg** breaching: **$4.25**, **$4.50**, **$4.75**, **$5.00** (CRL-08 watch at $4.50)
- **Food CPI** YoY prints: above 3.5% monthly, any upward revision (CRL-10 watch at 4.0%)
- **UI exhaustion cascade**: FL DEO weekly, state extensions, federal program reinstatement news
- **SNAP / TANF** changes, work requirements, benefit reductions
- **Utility shutoff moratoria** expiring, rate hike approvals (FL, TX priority)

### Structured Credit (consumer ABS)
- **EART**, **SDART**, **AMCAR**, **HAROT**, **ALLY** 10-D monthly collection reports
- **AFRMT** (Affirm), **KLAR** (Klarna), **SOFI** BNPL ABS performance
- Credit enhancement breaches, downgrades, trigger events
- Loss severity spikes (GFC 55-65% benchmark)

### Earnings Events (quadruple/triple priority days)
- **Apr 21** — SYF Q1, COF Q1, UNH Q1, DHI Q2
- **Apr 22** — ELV Q1, CB Q1
- **Apr 23** — AXP Q1, PHM Q1
- **May 6** — Uber Q1, DoorDash Q1
- **May 7** — Dave Q1, Lyft Q1, Affirm Q3 FY2026

---

## 🟠 SAME DAY

### Macro Data (consumer-relevant)
- CPI / PPI monthly releases
- PCE, retail sales, personal income/savings
- UMich sentiment (preliminary + final)
- Conference Board consumer confidence
- NFIB Small Business Optimism (Uncertainty index especially)
- Real estate: Case-Shiller, FHFA, NAR existing home sales, NAHB builder sentiment

### K-Shape Signals
- **Top-40% pullback**: Dollar Tree HHI >$100K share, luxury retailer traffic, RV market, boat sales, second-home listings, private-jet hours
- **Bottom-60% distress**: Wendy's / McD's same-store traffic, Dollar General / Dollar Tree traffic, BNPL installment count, payday lending volumes, check-cashing data
- Walmart Q earnings segment commentary (grocery mix, trade-down)
- Big Lots, Joann, Party City, Express — bankruptcy filings or going-concern doubt
- Restaurant closures (Chili's, Applebee's, TGI Friday's, etc.)

### Consumer Finance Companies
- Dave, MoneyLion, LendingClub, Upstart, SoFi, OneMain Q earnings
- BNPL-specific: Affirm, Klarna, Sezzle, Afterpay / Cash App
- Payroll advance / EWA: Earnin, Brigit, DailyPay data

### Cross-Agent Signals (from others)
- **LABOR**: initial claims breach (>275K 4-wk MA), JOLTS openings/ratio, NFP revisions, LFPR collapse
- **HAWK / BRENT**: oil supply shock, Hormuz status, OPEC+ action (2-3 week lag to gas pump)
- **REGINALD**: bank-level confirmation of consumer stress (credit card issuer reserve builds, auto lender commentary)
- **LIQUID**: ABS stress, structured credit dysfunction, funding strain affecting consumer lenders
- **RED**: counter-evidence to thesis (consumer-strength arguments, K-shape-closing data)

### Political / Policy (consumer-credit-specific)
- **SAVE → RAP transition** (Jul 1 2026) — MOHELA, AFT, CFPB developments
- **IEEPA / Sec 122 tariff** developments (Jul 24 cliff)
- OBBBA redetermination implementation
- Student loan forgiveness news (any Biden-era forgiveness restoration, new executive action)
- CFPB enforcement / rule changes affecting consumer lending
- Mortgage forbearance programs, foreclosure moratoria

---

## 🟡 WEEKLY BATCH

- Regional Fed surveys (Empire, Philly, KC, Dallas)
- CCAR / stress test results
- Insurance / P&C underwriting data (CA FAIR Plan, FL Citizens, state rate filings) — POLLY scope
- Small business data (NFIB detail, Sub-V bankruptcy filings, business formation BFS)
- Medical debt, healthcare affordability data — DOC scope
- Gig economy metrics (Uber/Lyft/DoorDash driver counts, tips data)
- Shadow inventory: condo HOA special assessments, property tax delinquency, tax-lien filings
- State-level consumer stress (FL, TX, MD priority diffusion)

---

## KEYWORD PATTERNS

WALTER can pattern-match on these terms to flag potential CARL signals:

**High confidence (almost always relevant):**
CC 90+, DQ, delinquency, charge-off, NCO, subprime auto, foreclosure, ATTOM, Fannie MF, Freddie MF, Trepp, CMBS, FICO, student loan, SAVE, MOHELA, RAP, BNPL, Affirm, Klarna, Dave, gas pump, $4 gas, SNAP, food stamps, UI exhaustion, claims, K-shape, Dollar Tree, Dollar General, Walmart (consumer), SYF, COF, ALLY, AXP, DFS, DHI, PHM, Rithm, PennyMac, EART, SDART, AMCAR, AFRMT

**Medium confidence (relevant in context):**
UMich, consumer sentiment, NFIB, Sub-V, bankruptcy, NCO, loss severity, credit enhancement, payday, EWA, Earnin, payroll advance, restaurant closure, FL condo, FL insurance, CA FAIR Plan, redlining, ACA cliff, Medicaid redetermination, tariff + small business, Uber driver, DoorDash driver, gig worker

**Low confidence (only if consumer angle):**
inflation, oil, tariff, regional bank, private credit, CMBS (commercial non-MF), Fed rate cut, mortgage rate

---

## WHAT NOT TO SEND

- Japan-specific macro → SAM
- China trade / export controls → ZHAO
- Bank capital / deposit / loan-level health → REGINALD (unless consumer-DQ-relevant)
- Oil / crude / refining supply → BRENT / HAWK (CARL only cares about gas-pump transmission)
- Equity positioning, VIX structure, short squeeze → HENRY
- Private credit / BDC-specific → BROCK / LIQUID
- Insurance UW / catastrophe → MARCO (CARL overlap ONLY on consumer-budget transmission, not supply-side)
- Pure employment data (claims, NFP establishment survey beats) → LABOR (CARL receives LABOR output, not raw)

---

## ACTIVE THRESHOLDS

*These are specific levels CARL is watching right now. Update as they change.*

| Metric | Level | Direction | Why It Matters |
|--------|-------|-----------|----------------|
| Gas National Avg | $4.06 | Current | CRL-08 watch $4.50+ |
| Gas National Avg | $4.50 | Above | Demand destruction phase |
| Fannie MF DQ | 0.74% | Current | GFC peak 0.80% (CRL-03) |
| Fannie MF DQ | 0.80% | Above | GFC BREACH — fire to REGINALD + PROME |
| CC 90+ DQ | 12.70% | Current | GFC peak 13.74% (CRL-05) |
| CC 90+ DQ | 13.74% | Above | GFC BREACH — fire to PROME |
| Student 90+ DQ | 9.8% | Current | CRL-04 watch 10%+ |
| Subprime Auto 60+ DQ | 6.9% | ATR | CRL-02 breached, watch acceleration |
| SYF FY2026 NCO | 5.8% Feb | Trending | CRL-12 watch 6.0% guidance ceiling |
| Foreclosure starts | 82,631 Q1 | Above | CRL-06 ≥70K/qtr threshold — already >70K |
| FL UI Wave 2 peak | Jul 26 | Date | CRL-07 exhaustion cascade |
| SAVE non-selection rate | TBD | Above 35% | CRL-13 window Oct 1 2026 |
| SBA 7(a) default rate | 3.7% | Trending | CRL-15 watch 6.5%+ by EOY |
| Brent | $80 | Below sustained | Full CRL-08 invalidation trigger |
| Claims 4-wk MA | 275K | Above | LABOR handoff threshold |

---

*Last reviewed: 2026-04-19 by CARL. Next review: when thesis version changes, CRL prediction resolves, or major threshold breach.*
