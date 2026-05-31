# CARL — Signal Intake Spec

**Owner:** CARL | **Consumer:** WALTER (routing)
**Last meaningful update:** 2026-04-19 (full version)
**Last hygiene pass:** 2026-05-31 — trimmed stale tables; durable routing parts retained

*Domain:* US consumer stress — credit DQ, housing, spending, K-shape bifurcation, multi-vector cost squeeze.

---

## ⚠️ How to read this file

Routing rules are durable; **dated state is not in this file.** When you need a current number, threshold, or catalyst, go to the live source:

| Need | Live source |
|------|-------------|
| Current dashboard values (gas pump, CC 90+ DQ, Fannie MF DQ, etc.) | `STATUS.md` |
| Forward catalysts (earnings, releases, key dates) | `docket/CATALYSTS.tsv` (run `scripts/docket_countdown.py`) |
| Live routing calibration with WALTER | `handoff_WALTER/LIAISON.md` |
| Active predictions + invalidation lines | `thesis/PREDICTIONS.tsv` |
| Per-vector thresholds | `thesis/THESIS.md` + `workbook/VX.tsv` |

Per auto-memory [[project_messaging_overhaul]], the inbox/outbox/HERMES surface is being replaced — don't extend or patch routing infra here. New routing logic should be negotiated turn-by-turn in `handoff_WALTER/LIAISON.md`, not added to this file.

What stays in this file: **what to flag and what to suppress** (durable scope rules).

---

## PRIORITY LEVELS

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 | Thesis-level, time-sensitive. Could breach a convergence vector or invalidation threshold. | Immediately |
| 🟠 | Important context. Informs analysis but not urgent. | Same day |
| 🟡 | Background. Useful but low urgency. | Batch weekly |

---

## 🔴 IMMEDIATE — what to flag

### Credit DQ / Charge-offs
- **CC 90+ DQ**: Fed Board / NY Fed QHDC releases, card issuer monthly master trust filings (NCO, 30+, 90+)
- **Subprime auto 60+ DQ**: Fitch ATR updates, Santander/Exeter/Bridgecrest/Westlake/American Credit master trust data
- **Student loan 90+ DQ**: FICO score reports, NY Fed QHDC, Dept of Ed payment data, TransUnion / Experian student reports
- **Mortgage 90+ DQ / FC starts**: MBA Weekly Applications, ICE / Black Knight mortgage monitor, Fannie + Freddie monthly summaries
- **Issuer earnings with DQ commentary**: SYF, COF, ALLY, AXP, DFS, BFH (Bread), C (card segment), JPM (card segment)

### Housing Distress
- **ATTOM**: monthly + quarterly foreclosure reports
- **Fannie / Freddie MF DQ**: monthly releases (CRL-03 watch — current threshold in STATUS/PREDICTIONS)
- **Trepp CMBS**: MF, office, retail DQ monthly
- **FHA / Ginnie** DQ / servicing transfers
- **HOMER-relevant builders**: DHI, PHM, LEN, KBH Q earnings / guide cuts
- **Mortgage servicer earnings**: Rithm / NewRez, PennyMac, Mr. Cooper, Ocwen

### Cost Squeeze (consumer-facing)
- **Gas pump national avg**: any sustained move ≥2wk through CRL-08 threshold (live in STATUS/PREDICTIONS)
- **Food CPI** YoY prints above current CRL-10 threshold or any upward revision
- **UI exhaustion cascade**: FL DEO weekly, state extensions, federal program reinstatement news
- **SNAP / TANF** changes, work requirements, benefit reductions
- **Utility shutoff moratoria** expiring, rate hike approvals (FL, TX priority)

### Structured Credit (consumer ABS)
- **EART**, **SDART**, **AMCAR**, **HAROT**, **ALLY** 10-D monthly collection reports
- **AFRMT** (Affirm), **KLAR** (Klarna), **SOFI** BNPL ABS performance
- Credit enhancement breaches, downgrades, trigger events
- Loss severity spikes (GFC 55-65% benchmark)
- Custodial / trustee disruptions (Wilmington-Trust-style exits)

### Insurance — consumer-cost transmission (POLLY scope, CARL-relevant)
- UNH / ELV MLR / MA membership prints
- ALL / PGR / TRV combined ratio shifts
- CA FAIR Plan / FL Citizens policy counts + rate filings
- Auto / tenants CPI prints (BLS monthly)

---

## 🟠 SAME DAY

### Macro Data (consumer-relevant)
- CPI / PPI monthly releases
- PCE, retail sales, personal income/savings
- UMich sentiment (preliminary + final)
- Conference Board consumer confidence
- NFIB Small Business Optimism (Uncertainty index especially)
- Real estate: Case-Shiller, FHFA, NAR existing home sales, NAHB builder sentiment
- GDP releases (advance / 2nd est / 3rd est) — composition matters more than headline for V12

### K-Shape Signals
- **Top-40% pullback**: Dollar Tree HHI >$100K share, luxury retailer traffic, RV market, boat sales, second-home listings, private-jet hours, retail-investor flow data
- **Bottom-60% distress**: Wendy's / McD's same-store traffic, Dollar General / Dollar Tree traffic, BNPL installment count, payday lending volumes, check-cashing data, plasma donations
- Walmart Q earnings segment commentary (grocery mix, trade-down)
- Restaurant comps (Black Box, Cinemark, etc.) — sector bifurcation prints
- Big Lots, Joann, Party City, Express — bankruptcy filings or going-concern doubt

### Consumer Finance Companies
- Dave, MoneyLion, LendingClub, Upstart, SoFi, OneMain Q earnings
- BNPL-specific: Affirm, Klarna, Sezzle, Afterpay / Cash App
- Payroll advance / EWA: Earnin, Brigit, DailyPay data

### Cross-Agent Signals (from others, CARL receives)
- **LABOR**: initial claims breach, JOLTS openings/ratio (current threshold in PREDICTIONS), NFP revisions, LFPR collapse
- **HAWK / BRENT**: oil supply shock, Hormuz status, OPEC+ action. *Pump-pass-through lag: ~2-3wk normal, accelerated to ~3-4d in Iran cluster (May 2026); 17-18d both-directions confirmed reverting 5/22-5/29.*
- **REGINALD**: bank-level confirmation of consumer stress (credit card issuer reserve builds, auto lender commentary)
- **LIQUID**: ABS stress, structured credit dysfunction, funding strain affecting consumer lenders
- **RED**: counter-evidence to thesis (consumer-strength arguments, K-shape-closing data, masking-framework counterexamples)
- **MARCO**: FL/TX/Sun Belt outflow + remittances when consumer-budget transmission applies

### Political / Policy (consumer-credit-specific)
- **SAVE → RAP transition** developments — MOHELA, AFT, CFPB
- **IEEPA / Sec 122 tariff** developments (cliff dates in docket)
- OBBBA redetermination implementation
- Student loan forgiveness news (any forgiveness restoration or new executive action)
- CFPB enforcement / rule changes affecting consumer lending
- Mortgage forbearance programs, foreclosure moratoria

---

## 🟡 WEEKLY BATCH

- Regional Fed surveys (Empire, Philly, KC, Dallas) — Non-Mfg variants especially (services-side stagflation)
- CCAR / stress test results
- Insurance / P&C underwriting data (state rate filings) — POLLY scope
- Small business data (NFIB detail, Sub-V bankruptcy filings, business formation BFS)
- Medical debt, healthcare affordability data — DOC scope
- Gig economy metrics (Uber/Lyft/DoorDash driver counts, tips data)
- Shadow inventory: condo HOA special assessments, property tax delinquency, tax-lien filings
- State-level consumer stress (FL, TX, MD priority diffusion)

---

## KEYWORD PATTERNS

WALTER can pattern-match on these terms to flag potential CARL signals:

**High confidence (almost always relevant):**
CC 90+, DQ, delinquency, charge-off, NCO, subprime auto, foreclosure, ATTOM, Fannie MF, Freddie MF, Trepp, CMBS, FICO, student loan, SAVE, MOHELA, RAP, BNPL, Affirm, Klarna, Dave, gas pump, $4 gas, SNAP, food stamps, UI exhaustion, claims, K-shape, Dollar Tree, Dollar General, Walmart (consumer), SYF, COF, ALLY, AXP, DFS, DHI, PHM, Rithm, PennyMac, EART, SDART, AMCAR, AFRMT, Wilmington Trust (ABS custody), Tricolor, masking framework, condo K-shape

**Medium confidence (relevant in context):**
UMich, consumer sentiment, NFIB, Sub-V, bankruptcy, NCO, loss severity, credit enhancement, payday, EWA, Earnin, payroll advance, restaurant closure, FL condo, FL insurance, CA FAIR Plan, redlining, ACA cliff, Medicaid redetermination, tariff + small business, Uber driver, DoorDash driver, gig worker, savings rate, Real DPI, plasma donations, Real-wage K-shape

**Low confidence (only if consumer angle):**
inflation, oil, tariff, regional bank, private credit, CMBS (commercial non-MF), Fed rate cut, mortgage rate, stagflation (V12 transmission)

---

## WHAT NOT TO SEND

- Japan-specific macro → SAM
- China trade / export controls → ZHAO
- Bank capital / deposit / loan-level health → REGINALD (unless consumer-DQ-relevant); OZK specifically → OZK
- Oil / crude / refining supply → BRENT / HAWK (CARL only cares about gas-pump transmission)
- Equity positioning, VIX structure, short squeeze → HENRY
- Private credit / BDC-specific → BROCK / LIQUID
- Insurance UW catastrophe / supply-side → MARCO (CARL overlap ONLY on consumer-budget transmission, not supply-side)
- Pure employment data (claims, NFP establishment survey beats) → LABOR (CARL receives LABOR output, not raw)
- Counter-thesis red-team work → RED (CARL stages in `handoff_RED/`, does not maintain)

---

*Active thresholds + dated catalysts removed 2026-05-31 — they belong to STATUS / PREDICTIONS / docket which are kept live. This file is now scope-of-attention only.*
