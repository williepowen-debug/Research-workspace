---
id: SIG-W-20260511-027
date: 2026-05-11
origin: WALTER NDFI-extraction sub-agent 2026-05-11 — Morgan Stanley Bank NA call-report data per S&P Global
domain: BANK_CRE
cluster: FED_FRAMEWORK
signal_type: pattern-match
precedence: PRIORITY
confidence: 0.85
to: REGINALD
info: [BROCK, LIQUID, RED]
signal_role: routine
event_window: closed
verify_research_verdict: CONFIRMED
---

# Morgan Stanley Bank NA — BCI (Business Credit Intermediaries) at 19.73% of Total Loans; +316bps QoQ Growth = Highest BCI Concentration Ratio in Big-Bank Tier

**Verbatim claim (verified):** Morgan Stanley Bank NA Q4 2025 / Q1 2026 — **BCI (Business Credit Intermediaries, FFIEC Schedule RC-C Memorandum 10.b) = 19.73% of total loans and leases** + **+316bps QoQ growth**. Highest BCI-as-%-of-total-loans among the big-bank tier; growth pace +316bps QoQ is the largest single-quarter BCI ratio expansion in named-bank tier.

## Substance

- **BCI (10.b) is the FFIEC sub-category for BDC + middle-market direct-lender + asset-based-lender lending.** Morgan Stanley's 19.73% concentration in this specific NDFI subcategory = direct exposure to the BDC + direct-lending universe BROCK tracks for PC cycle.
- **316bps QoQ ratio expansion** = MS's BCI book is growing faster than total balance sheet by a wide margin. Either MS is adding BCI loans rapidly OR retiring non-BCI loans faster than BCI. Either way, concentration risk rising.
- **Highest concentration ratio in big-bank tier**: JPM $237.85B is absolute leader; WFC has BCI = 33% of NDFI (high but vs total-loans = lower); MS BCI = 19.73% of TOTAL loans (different denominator, highest ratio).
- **FFIEC 5-category schema** per primary: 10.a Mortgage-credit (~25%) / 10.b BCI (~25%) / 10.c PE-funds (~24%) / 10.d Consumer-credit (~8%) / 10.e Other (~18%). Industry BCI total $377.52B Q4 2025.
- **Investment-banking lender concentration matters because**: MS is non-deposit-bank-dominant (vs WFC + JPM full-service banks). BCI exposure means MS is funding the BDC universe directly — first-loss position if BDC NAV-marks deteriorate.

## Dispatch notes

CONFIRMED 0.85. signal_type pattern-match (concentration trajectory). Not cluster_mediating-tagged (single-name concentration story; doesn't cross multiple clusters fundamentally). May 15 CDR bulk Q1 2026 release will update — watch for MS BCI ratio Q1 figure to confirm trajectory.

## Recipient routing

- **REGINALD action** — Big-Bank-NDFI-subcategory primary.
- **BROCK info** — direct BCI-to-BDC-cycle exposure.
- **LIQUID info** — funding-spread context.
- **RED info** — adversarial overlay on "MS-is-conservative" prior framing.
