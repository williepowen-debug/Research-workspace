# OZK — PRIVATE CREDIT EXPOSURE

OZK's vulnerability to the private credit cascade. This is the transmission channel between BROCK's domain (private credit deterioration) and OZK's balance sheet.

OZK lends to real estate developers AND lends to the lenders. $2.74 billion in loans to non-depository financial institutions (NDFI), and the CEO admitted on the Q3 2025 earnings call that "a chunk" of those are CRE debt fund loans managed by RESG. This is debt-on-debt: if the private credit ecosystem cracks, OZK takes losses from both sides — directly on construction loans AND indirectly through its lending to funds that are themselves exposed.

**🆕 Q1 2026 refinement (Apr 22):** CIB President Jake Munn disclosed on the earnings call that OZK is **pulling back** from capital-call subscription facilities (Fund Finance) and facing pricing/structure compression in Lender Finance Group — both due to non-bank lenders + insurance companies entering those markets. The relationship is now bidirectional: OZK is simultaneously *exposed to* and *losing pricing ground to* the same private-credit/non-bank ecosystem. Structural exposure analysis unchanged; narrative layer refined. See `NDFI_EXPOSURE.md` §Q1 2026 Update.

---

## File Instructions

### NDFI_EXPOSURE.md
The $2.74B NDFI book — what it is, who the counterparties are, and how much is actually CRE in disguise:
- **🆕 Q1 2026 Update section** (Apr 23) — Jake Munn pullback, LFG compression, asymmetric disclosure
- Breakdown by FFIEC category (business credit intermediaries, PE funds, other)
- Named counterparties and their stress levels
- Gleason's own admission that NDFI contains RESG loans (Q3 2025)
- Shadow CRE estimate (how much of NDFI is CRE-correlated)

**Core data exists in:** `../research/NDFI_SHADOW_CRE_ANALYSIS.md` (migrate key findings here)

### COUNTERPARTY_WATCH.md
Living tracker of OZK's NDFI counterparties and their health:
- Named entity, relationship type, estimated exposure
- Current stress indicators (gating, redemption queues, NAV markdowns, covenant breaches)
- Cross-reference to BROCK's private credit cascade tracker

**23 counterparties identified so far.** 19 CRE-linked, 4 non-CRE. 6 of 19 CRE partners already under stress:
- Affinius Capital — $2.7B bond maturity Oct 2026, 7+ OZK deals (⚠️ NOT mentioned on Q1 26 call)
- Square Mile Capital — stress signals
- Starwood — dividend cut 2023
- Blue Owl — redemption gates (OBDC, OBDCII)
- JVP Management — stress signals
- Others TBD

Update when BROCK flags new private credit events. Any fund gating, redemption freeze, or NAV markdown that touches an OZK counterparty gets logged here.

### TRANSMISSION.md
How private credit stress reaches OZK's P&L — the mechanics of the transmission chain:
- **Direct:** OZK construction loan borrower defaults → charge-off (main thesis; Q1 26 past-due doubled, confirming live)
- **Indirect (NDFI):** PC fund gates/defaults → can't repay OZK warehouse/bridge line → OZK loss on NDFI book
- **Reflexive:** PC fund stress → fund stops providing mezz/takeout for OZK construction borrowers → borrower can't refinance at maturity → construction loan defaults. **🆕 Q1 2026 amplifier:** competitive displacement — same cohort displacing OZK on Fund Finance origination today is takeout ecosystem tomorrow. Stress hits both sides.
- **Collateral cascade:** JPM marking down collateral pledged by PC funds → margin calls → forced selling → further markdowns

The reflexive channel is the one nobody's modeling. OZK's construction borrowers often rely on PC funds for takeout financing. If those funds are gated or frozen, the exit for OZK's construction loans disappears even if the underlying property is performing — and with Q1 2026's competitive-displacement disclosure, the reflexive loop no longer requires outright fund failure to start constricting.

---

## Connection to BROCK

BROCK tracks the private credit cascade at the sector level. This folder tracks how it specifically reaches OZK. Key BROCK signals to watch:
- Fund gating events (9 funds in ~7 weeks as of Mar 24)
- APO/ARES/ARCC/OWL — any that are OZK NDFI counterparties
- JPM collateral markdowns on PC-pledged assets
- Partners Group defaults doubling to 5%+
- Software maturity wall ($70B in 2028) hitting BDC portfolios
- **🆕 Insurance-company entry into Fund Finance** — any named insurers moving into capital-call subscription facilities (Munn Q1 26 flagged as source of OZK's pullback)

When BROCK escalates, check COUNTERPARTY_WATCH.md for OZK-specific exposure.

---

## Key Numbers (Baseline Q4 2025, Q1 2026 updates noted)

| Category | Amount | % of NDFI | CRE Correlation | Q1 26 Signal |
|----------|--------|-----------|-----------------|--------------|
| Business credit intermediaries | $1.20B | 43.8% | HIGH — CEO confirmed CRE debt funds | 🆕 LFG pricing/structure compression (Munn) |
| Private equity funds | $772M | 28.2% | MODERATE — subscription lines, but LP stress = risk | 🆕 Capital-call subs pullback (Munn) |
| Other NDFIs | $722M | 26.3% | UNKNOWN — likely BDCs, mortgage REITs, specialty | No Q1 26 commentary |
| Consumer credit intermediaries | $48M | 1.8% | LOW | — |
| **Total NDFI** | **$2.74B** | **100%** | **Estimated 50-75% CRE-correlated** | — |

Shadow CRE via NDFI adds est. $1.25-1.75B to true CRE exposure, pushing adjusted CRE/Tier 1 from 358% to ~411-420%.

**Fund Finance component growth (Mgmt Comments Figure 17):** $210M Q1 2025 → $1,275M Q1 2026. Book grew ~6x YoY despite Q1 new-origination pullback — legacy roll-in dominates, pullback is at the forward edge.

---

*BROCK status → `../../BROCK/STATUS.md` | NDFI research → `../research/NDFI_SHADOW_CRE_ANALYSIS.md` | KB → `../workbook/KB.tsv` (KB-OZK-021 through 027; KB-OZK-186 through 188 post-Q1)*
