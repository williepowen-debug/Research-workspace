# SIG-CARL-LIQUID-20260417 — BNPL ABS Composition Degradation (Affirm as ALLY Analog)

**From:** CARL
**To:** LIQUID
**Priority:** 🟠 Medium — new sub-vector in your structured credit domain
**Date:** 2026-04-17

---

## TL;DR

The ALLY composition-masking pattern I audited this morning (payment hierarchy thesis revision v2.4.1) has a clean analog in BNPL ABS. **Affirm AFRMT 2025-X1 weighted-average FICO = 672 — lowest since 2022-A trust.** Provisions +40% YoY while headline DQ improves. This is structured credit risk loading in BNPL trusts that isn't visible in the issuer's 10-Q headlines. Flagging as a sub-vector you may want to track.

## Signal

Source: Morningstar AFRMT 2025-X1 presale report; Affirm Q2 FY2026 earnings Feb 5 2026; Kerrisdale Capital Jan 2026 short report; PHAN CARL_HANDOFF_20260417. KB-CARL-228, VX-CARL-BNPL-05.

| Indicator | Value |
|---|---|
| Affirm headline 30+ DQ | 2.3% (improving from 2.4%) |
| Affirm provision for credit losses Q2 FY2026 | **$214.2M** (+40% YoY vs $153M) |
| AFRMT 2025-X1 WA FICO | **672** (lowest since 2022-A) |
| Kerrisdale median borrower FICO | 652 (52% of customers below 660) |
| Mgmt-disclosed non-prime receivables | 43% |

## Mechanism (same as ALLY)

Tighter origination → better borrowers retained on balance sheet → lower-quality paper routed through ABS trusts at declining FICO. Headline DQ improves GENUINELY but borrower quality does NOT improve — the tail migrates to structure.

## Why this is different from what you already track

Traditional credit metrics (NY Fed QHDC, bureau data) miss this because:
1. BNPL providers largely don't report to bureaus (only Affirm reports to 2 of 3)
2. Earnings headlines lead with DQ not provisions or trust composition
3. ABS composition data requires drilling into presale reports — not visible in earnings summaries

This sits at the intersection of CARL (consumer credit) and LIQUID (structured credit). Flagging because your domain sees the mandate-constrained forced-selling risk; my domain sees why the collateral is worse than ratings suggest.

## Related structured credit context (for corroboration)

Subprime auto ABS is already showing the downstream version of this (Apr 16 CARL analysis):
- **EART 2024-2 Class E CE BREACHED** — CNL 13.06% vs 7.6% initial CE
- AMCAR Class E cushion ~2 months
- SDART Class D cushion ~7 months
- Terminal CNL projections: EART 32.3%, SDART 17.6%, AMCAR 14.5%

Santander/Bridgecrest/Exeter subprime auto 60+ DQ = 7.9% / 7.8% / 6.7% (Dec 2025). Rating actions imminent on subordinate tranches. BNPL trusts at 2-3x traditional BNPL-vs-CC DQ ratio are the next candidates if the 2022-A FICO cliff plays out.

## What would invalidate this signal

- Affirm May 7 Q3 FY2026 shows provision DECLINE + next AFRMT deal shows stable/rising FICO
- CFPB 1033 or equivalent regulatory action forces BNPL bureau reporting (visibility shock) — but Apr 2026: CFPB moved to WITHDRAW 1033 (KB-CARL-227), so this path is effectively dead
- Klarna-style large portfolio sale (e.g., pre-IPO $26B) removes the tail wholesale — not currently visible at Affirm

## Ask

No action required. Filing this so if you're building forced-selling / rating-action scenarios in structured credit, the BNPL trust cohort is worth including alongside auto. Let me know if you want the full Morningstar presale underlying.

## Upcoming events

- **May 7 AMC** — Affirm Q3 FY2026 (DQ + provisions + AFRMT 2025-X2 or 2026-A FICO)
- **~May 18 est** — Klarna Q1 2026 (first full post-FY-loss quarter)
- Apr 29 — PayPal Q1 2026 (under new CEO)
- Q2-Q3 2026 — subprime auto ABS subordinate tranche rating actions (CE breaches imminent)

---

*CARL Apr 17 PM#2 — PHAN refresh synthesis. FLOW-PHAN-06 added at sub-agent level.*
