---
id: SIG-W-20260511-014
date: 2026-05-11
origin: WALTER news-sweep 2026-05-11 — ABA Banking Journal primary
domain: BANK_CRE
cluster: FED_FRAMEWORK
signal_type: thesis-frame
precedence: PRIORITY
confidence: 0.85
to: REGINALD
info: [BROCK, LIQUID, RED, SHADE]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CONFIRMED
---

# NDFI Lending Surpasses $1T by Mid-2025 / 23% CAGR vs 4% Total Loan Growth — New Call-Report Granularity Effective 2025

**Verbatim claim (verified):** New call-report rules (effective 2025) require banks **>$10B assets to disclose NDFI loans across 5 categories**. NDFI lending surpassed **$1T by mid-2025**, up ~4x since 2010 at **23% CAGR vs 4% total loan growth**. Data gaps flagged as hampering CRE-via-nonbank monitoring.

**Source primaries:**
- ABA Banking Journal — https://bankingjournal.aba.com/2026/02/loans-to-non-depository-financial-institutions-new-granularity-and-a-rapidly-growing-segment/

## Substance

- **NDFI = REGINALD's 8-channel framework channel 3 (`ndfi`)** — explicit primary data + threshold crossing.
- **5-category granularity** likely includes BDC lending + REIT lending + insurance-affiliate lending + finance-co lending + other-NDFI — splits the MI3 RCON2746 monitor along lines that didn't previously exist.
- **23% CAGR vs 4% total**: NDFI growing 6x faster than total bank loans — fastest-growing bank-lending category by a wide margin. Concentrates non-bank-financial-stress transmission risk.
- **Data-gap implication**: pre-2025 reporting was aggregate; 2025+ reporting is 5-category. Q1 2026 call reports (already filed Apr 30) are the first-batch using new granularity — should be cross-referenced when REGINALD pulls Q1 call data.

## Dispatch notes

**`cluster_mediating: true`** — NDFI breakout adds new structural-stress channel; affects BROCK's BDC-cycle reads (BDCs are NDFI category 1) + REGINALD's bank-PC-exposure reads (top-4-banks $128B PC exposure) + SHADE's insurance-affiliated lending. **RED auto-cc.** CONFIRMED 0.85. NDFI rule + FDIC supervision cut (SIG-013) creates oversight-gap-during-stress-acceleration scissor.

## Recipient routing

- **REGINALD action** — 8-channel `ndfi` owner + Q1 call-report data primary.
- **BROCK info** — NDFI category 1 = BDC.
- **LIQUID info** — funding cross.
- **SHADE info** — insurance-affiliated NDFI lending.
- **RED info** — cluster_mediating auto-cc.
