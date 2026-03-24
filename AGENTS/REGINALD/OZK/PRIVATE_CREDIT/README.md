# OZK — PRIVATE CREDIT EXPOSURE

OZK's vulnerability to the private credit cascade. This is the transmission channel between BROCK's domain (private credit deterioration) and OZK's balance sheet.

OZK doesn't just lend to real estate developers — it lends to the lenders. $2.74 billion in loans to non-depository financial institutions (NDFI), and the CEO admitted on an earnings call that "a chunk" of those are CRE debt fund loans managed by RESG. This is debt-on-debt: if the private credit ecosystem cracks, OZK takes losses from both sides — directly on construction loans AND indirectly through its lending to funds that are themselves exposed.

---

## File Instructions

### NDFI_EXPOSURE.md
The $2.74B NDFI book — what it is, who the counterparties are, and how much is actually CRE in disguise:
- Breakdown by FFIEC category (business credit intermediaries, PE funds, other)
- Named counterparties and their stress levels
- Gleason's own admission that NDFI contains RESG loans
- Shadow CRE estimate (how much of NDFI is CRE-correlated)

**Core data exists in:** `../research/NDFI_SHADOW_CRE_ANALYSIS.md` (migrate key findings here)

### COUNTERPARTY_WATCH.md
Living tracker of OZK's NDFI counterparties and their health:
- Named entity, relationship type, estimated exposure
- Current stress indicators (gating, redemption queues, NAV markdowns, covenant breaches)
- Cross-reference to BROCK's private credit cascade tracker

**23 counterparties identified so far.** 19 CRE-linked, 4 non-CRE. 6 of 19 CRE partners already under stress:
- Affinius Capital — $2.7B bond maturity Oct 2026, 7+ OZK deals
- Square Mile Capital — stress signals
- Starwood — dividend cut 2023
- Blue Owl — redemption gates (OBDC, OBDCII)
- JVP Management — stress signals
- Others TBD

Update when BROCK flags new private credit events. Any fund gating, redemption freeze, or NAV markdown that touches an OZK counterparty gets logged here.

### TRANSMISSION.md
How private credit stress reaches OZK's P&L — the mechanics of the transmission chain:
- **Direct:** OZK construction loan borrower defaults → charge-off (this is the main thesis)
- **Indirect (NDFI):** PC fund gates/defaults → can't repay OZK warehouse/bridge line → OZK loss on NDFI book
- **Reflexive:** PC fund stress → fund stops providing mezz/takeout for OZK construction borrowers → borrower can't refinance at maturity → construction loan defaults
- **Collateral cascade:** JPM marking down collateral pledged by PC funds → margin calls → forced selling → further markdowns

The reflexive channel is the one nobody's modeling. OZK's construction borrowers often rely on PC funds for takeout financing. If those funds are gated or frozen, the exit for OZK's construction loans disappears even if the underlying property is performing.

---

## Connection to BROCK

BROCK tracks the private credit cascade at the sector level. This folder tracks how it specifically reaches OZK. Key BROCK signals to watch:
- Fund gating events (9 funds in ~7 weeks as of Mar 24)
- APO/ARES/ARCC/OWL — any that are OZK NDFI counterparties
- JPM collateral markdowns on PC-pledged assets
- Partners Group defaults doubling to 5%+
- Software maturity wall ($70B in 2028) hitting BDC portfolios

When BROCK escalates, check COUNTERPARTY_WATCH.md for OZK-specific exposure.

---

## Key Numbers (Baseline Q4 2025)

| Category | Amount | % of NDFI | CRE Correlation |
|----------|--------|-----------|-----------------|
| Business credit intermediaries | $1.20B | 43.8% | HIGH — CEO confirmed CRE debt funds |
| Private equity funds | $772M | 28.2% | MODERATE — subscription lines, but LP stress = risk |
| Other NDFIs | $722M | 26.3% | UNKNOWN — likely BDCs, mortgage REITs, specialty |
| Consumer credit intermediaries | $48M | 1.8% | LOW |
| **Total NDFI** | **$2.74B** | **100%** | **Estimated 50-75% CRE-correlated** |

Shadow CRE via NDFI adds est. $1.25-1.75B to true CRE exposure, pushing adjusted CRE/Tier 1 from 358% to ~411-420%.

---

*BROCK status → `../../BROCK/STATUS.md` | NDFI research → `../research/NDFI_SHADOW_CRE_ANALYSIS.md` | KB → `../workbook/KB.tsv` (KB-OZK-021 through 027)*
