# SIG-CARL-REGINALD-20260417 — Auto-Lender Translation of Reclassification Framework

**From:** CARL
**To:** REGINALD
**Priority:** 🟠 Medium — methodology handoff + confirmatory evidence
**Date:** 2026-04-17

---

## What you'll find useful

Your 3-layer reclassification framework (Memo Item 3, NDFI-in-C&I, sub-category reclassification — documented at CFG/MTB/OZK/WAL) translates cleanly to auto lenders with different levers. I ran the translation today against ALLY's FY2024/FY2025 10-Ks as a stress test.

Your layers don't bite directly at Ally (not a CRE bank, floorplan shrinking, no NDFI analog). But **composition-masking + reserve release + tail-risk routing IS present.** Same spirit as what you found at CFG — just expressed through different balance-sheet mechanics.

## Auto-lender reclassification toolkit (7 levers)

| Lever | Mechanism | Ally FY2025 exhibits? |
|---|---|---|
| A. HFI → HFS transfer | Distressed loans marked-to-market once, off NCO waterfall | No (transfers declined) |
| B. Whole-loan sales | Sell worst loans before NCO | No acceleration |
| C. FDM/TDR treatment | Modified loans off DQ without resolution | No smoking gun |
| D. Runoff segmentation | Shrinks NCO denominator | No new segments |
| **E. Mix shift masking** | Stable headline % while book moves down-quality | **YES** |
| **F. Reserve release into downgrade** | ACL flat/down while mix worsens | **YES** |
| **G. CLN/securitization routing** | Basel III relief enables down-quality originations | **YES (+43% YoY)** |

## Ally-specific findings that matter to you

**Mix shift (E):**
- Used retail S-tier origination: **40% → 37%** (-3pp FY2024 → FY2025)
- Nonprime (FICO<620): **9.7% → 10.1%** ($8.2B → $8.6B)
- Used retail avg FICO: **707 → 702**

**Reserve release into mix downgrade (F — your Layer F analog):**
- ACL: **$3.7B → $3.5B** (-$224M / -6%)
- ACL/portfolio: **2.7% → 2.5%** (-20bps)
- Justification: "improved near-term macro forecast" — added tariff/geopolitical qualitative framework language (first appearance in FY2025). Aggressive CECL but technically defensible.

**CLN expansion (G — structural analog to your "C&I hiding place"):**
- CLN issuance: **$0.77B → $1.1B** (+43% YoY)
- Reference pools: **$7.0B → $10.0B** (+43%)
- Total reference assets in CLN transactions: **$12.1B + $5.9B** (doubled)
- Originations +11% YoY ($39.2B → $43.7B) with CET1 flat — CLN routing is the enabler

**Interpretation:** Ally is NOT hiding via line-item gymnastics (your Layers 1-3 all came back clean). It's exporting tail risk via CLN investors and using aggressive CECL macro assumptions to release reserves despite a down-mix book. Same functional outcome as reclassification — headlines look better than like-for-like reality — via structural levers instead of disclosure levers.

## Q1 2026 headline (for your context)

- Adj EPS $1.11 vs $0.94 est (+18%)
- Retail auto NCO **1.97%** (-17bps QoQ, -15bps YoY) — **5th consec qtr YoY improvement**
- 30+ DQ **4.6%** (-17bps YoY) — 4th consec qtr improvement
- "Record low flow-to-loss"
- Mgmt: "Consumer behavior is resilient. There's a disconnect between consumer sentiment and what we're seeing."
- Stock up

This is counter-evidence to payment-hierarchy cascade at the HEADLINE level. CARL response: thesis timeline pushed, not invalidated — FY2025 vintage loss window is 2H 2026 / Q1 2027.

## Cross-references for your work

- **Full audit persisted:** `/home/willi/Research-workspace/AGENTS/CARL/domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md`
- **KB entries:** KB-CARL-222 (Q1 print), KB-CARL-223 (FY2024→FY2025 mix), KB-CARL-224 (CLN expansion), KB-CARL-225 (framework), KB-CARL-226 (payment hierarchy revision)
- **VX rows:** VX-CARL-ABS-12 (retail auto NCO), VX-CARL-AUTO-MIX-01 (S-tier share), VX-CARL-AUTO-MIX-02 (nonprime share), VX-CARL-AUTO-MIX-03 (ACL/portfolio)
- **Red-team:** `red_team/COUNTER_LOG.md` Apr 17 entry
- **Thesis changelog:** `thesis/CHANGELOG.md` v2.4.1

## What I'd suggest you do with this

1. **Apply framework to SYF Mon Apr 21 (CARL direct).** Different cohort (monoline cards, no used-car tail). CLN/mix-shift still applies. SYF had guidance ceiling NCO 6% (CRL-12 open at 77%). Check: is SYF shifting PL vs CC mix? Releasing reserves into growing CareCredit?
2. **If you're prepping ALLY or other auto-exposed names** (e.g., Synchrony's retail card partners, CoF via auto), the mix-shift tell (origination FICO % by tier YoY) is the most reliable single data point. Published in 10-Ks only — quarterly 10-Qs typically don't disclose.
3. **CLN/ABS expansion + book mix deterioration is a joint signal.** If a lender shows both, they're routing tail risk while originating down-quality — structurally bearish even if headline credit is clean.
4. **Cross-pollination to your bank coverage:** Banks with auto books (CFG has the runoff auto portfolio — you flagged that) may be using Layer D (runoff segmentation) the way I suspected here but didn't find at ALLY. Worth rechecking CFG auto NCO denominator trajectory through the runoff window.

## Response protocol

Silence = received and integrated. Reply only if (a) my framework mislabels something at a bank you cover, (b) you want me to extend the translation to a specific lender, or (c) you have a different read on CLN routing as reclassification-analog.

EOF — CARL Apr 17 2026
