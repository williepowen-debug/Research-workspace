# PROME → REGINALD: Q1 Call Report Triage + ZION Ownership

**Date:** 2026-05-10 17:27 ET
**From:** PROME / Chief of Staff
**To:** REGINALD
**Priority:** 🔴 Monday decision support
**Owner:** REGINALD domain — banks / regional credit / Call Reports

## Ask
Own the **Q1 Call Report triage** for the live regional-bank book and fill the ZION scaffold enough to support Monday execution decisions.

Prome will synthesize your output into Will's Monday bank decision prompt. Prome should not duplicate your domain work unless blocked.

## Banks
Primary:
- WAL
- OZK
- ZION
- CFG
- VLY
- EGBN
- FITB

Secondary / as needed:
- SSB
- HBAN
- RF

## Extract / Score
For each bank where Q1 Call Report / 10-Q data is available, extract:

1. **MI3 / RCON2746 hidden-CRE screen**
   - Especially owner-occupied CRE, construction, investor CRE, multifamily, office.
2. **NDFI / warehouse / lender-finance exposure**
   - Any nonbank finance / private-credit / specialty-lender linkage.
3. **Credit quality trend**
   - ACL, NCOs, criticized/classified, nonaccruals, 30-89d, modified loans.
4. **Funding / liquidity fragility**
   - FHLB, brokered deposits, uninsured deposit coverage, wholesale funding dependence.
5. **Maturity wall / recognition pressure**
   - Multifamily and CRE maturities, interest reserves, loan mods/extensions.
6. **Position read**
   - Does the evidence support: add / hold runway / roll selectively / cleanup / kill?

## ZION Specific
Treat ZION as **under-researched, not exonerated**.

Current trade posture from Prome:
- `ZION $57.5P Jul 17 2026` = **kill / no-roll if usable bid** unless Call Report MI3/RCON2746 or related evidence changes the picture.
- Do not confuse current trade timing weakness with clean fundamentals.

Start with:
- `AGENTS/REGINALD/ZION/INDEX.md`
- `AGENTS/REGINALD/ZION/TODO.md`
- `AGENTS/REGINALD/ZION/research/ZION_DEEP_DIVE_FRAMEWORK.md`

Target output if possible:
- `AGENTS/REGINALD/ZION/research/MI3_HIDDEN_CRE_SCREEN.md`

Then, if time:
- `CRE_MULTIFAMILY_MATURITY.md`
- `MUNI_CONDUIT_RISK.md`
- `AOCI_CAPITAL_RULE.md`
- `FRAUD_ACCOUNTING_COMPARISON.md`
- `INSIDER_GOVERNANCE_SCAN.md`

## Output Format Wanted
Write a concise domain memo with:

```markdown
# REGIONAL BANK Q1 TRIAGE — May 2026

## Executive Read
- Base case:
- Bear case:
- Strong Bear triggers:
- Monday action implication:

## Bank Table
| Bank | MI3/hidden CRE | NDFI/warehouse | Credit trend | Funding | Position implication | Confidence |

## ZION Update
- Hidden CRE:
- Multifamily:
- Muni/conduit:
- Funding/AOCI:
- Trade posture change? yes/no

## Decision Inputs for Prome
- May scraps cleanup:
- June roll/salvage candidates:
- Sep/Dec runway holds:
- Kill/no-roll names:
- What would change your mind:
```

## Due
Before Monday open if possible. If blocked, leave a clear blocker note with exactly what data is missing.

## Constraints
- No trade execution.
- Do not ask Will for broad context; use local files and public filings first.
- Prome is acting as chief of staff; REGINALD owns bank-domain judgment.
