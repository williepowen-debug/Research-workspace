---
id: SIG-W-20260511-029
date: 2026-05-11
origin: WALTER NDFI-extraction sub-agent 2026-05-11 — FFIEC + FDIC 2026 Risk Review + S&P Global + Cadwalader analysis
domain: BANK_CRE
cluster: FED_FRAMEWORK
signal_type: thesis-frame
precedence: PRIORITY
confidence: 0.95
to: REGINALD
info: [BROCK, LIQUID, RED, SHADE, PROME]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CONFIRMED
---

# NDFI Framework Signal — 5-Category Schema CONFIRMED (FFIEC RC-C 10.a-10.e); $1.4T Industry Total YE 2025 (+35.2% YoY); MAY 15 = T-4d Bulk Q1 CDR Release; BROCK $128B Working Number IS 11x UNDERSTATED

**Verbatim claim (verified):** Per FDIC 2026 Risk Review + FFIEC Call Report Instructions (March 2025 effective) + S&P Global call-report analysis:

- **Total NDFI lending = $1.4T at YE 2025** (+35.2% YoY = fastest banking-loan-segment growth by 3x).
- **FFIEC Schedule RC-C Memorandum 10.a-10.e** — new 5-category granularity required for banks ≥$10B in assets effective 2025:
  - **10.a Mortgage credit intermediaries** ~25% — mortgage REITs / warehouse / origination
  - **10.b Business credit intermediaries (BCI)** ~25% — BDCs / direct lenders / ABL lenders
  - **10.c Private equity funds** ~24% — capital-call / subscription lines
  - **10.d Consumer credit intermediaries** ~8% — auto-finance / consumer-loan platforms
  - **10.e Other NDFI** ~18% — insurance / broker-dealers / family offices / catch-all
- **Big-4 (JPM/WFC/BAC/Citi) = 47.8% of all industry NDFI**; top-10 banks = 86%; banks >$500B = 68.2%.
- **MAY 15 = T-4d** for bulk Q1 2026 5-category CDR release (45 days after Q1 close = first time bank-level 5-category splits publicly available).

## Substance

- **MAJOR FRAMEWORK CORRECTION for BROCK STATUS**: working "$128B top-4 banks PC exposure" number is private-credit-subset only. **Full NDFI book = $1.4T = ~11x larger.** WFC alone is $212B (66% larger than $128B working number); JPM alone is $238B.
- **BROCK's $128B likely represented PE-fund subscription lines (10.c) or BDC-specific lending (subset of 10.b) only.** Full NDFI captures all 5 categories.
- **May 15 CDR bulk release** = first time the new 5-category granularity is publicly available at bank level. Plan WALTER + REGINALD + BROCK pull on release date.
- **Reclassification artifact watch**: Q4 2025 data shows "other" (10.e) at $394.94B vs BCI at $377.52B — Cadwalader Sept 2025 flagged heavy reclassification "primarily driven by one institution." First clean reading of stable category splits will come from Q2-Q3 2026 data.
- **Bank-level signals dispatched same batch**: SIG-026 WFC NDFI 21% concentration + Q1 fraud / SIG-027 MS BCI 19.73% concentration / SIG-028 CUBI 33%-of-loans.

## Dispatch notes

**`cluster_mediating: true`** — framework correction touches BANK_COLLATERAL (bank-specific concentration signals) + PC_STRESS (BDC-bank-lending nexus) + FED_FRAMEWORK (regulatory-monitoring infrastructure) + POSITIONING_VALUATION (bank-credit-quality regime pricing). **RED auto-cc per v0.7.** CONFIRMED 0.95 (FFIEC primary + FDIC Risk Review + S&P Global + multi-source).

## Recipient routing

- **REGINALD action** — bank-NDFI-monitoring framework owner; cross-refs WALTER's CROSS_REFS/REGINALD.md +/or REGINALD's own knowledge framework.
- **BROCK info** — **PRIORITY surface for BROCK STATUS framework correction** ($128B → $1.4T scope). Worth a WALTER outbox REQ to BROCK alerting the scope-discrepancy explicitly.
- **LIQUID info** — Fed-monitoring-framework cross + funding context.
- **RED info** — cluster_mediating auto-cc.
- **SHADE info** — insurance + PE-affiliated lender cross-feed.
- **PROME info** — coordinator visibility for cross-agent BROCK alert.
