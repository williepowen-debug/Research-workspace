# WAL Fraud Exposure — Status Overview
**Last Updated:** 2026-03-25 | **Status:** THREE ACTIVE VECTORS

---

## Summary

WAL has three independent fraud exposures from three unrelated fraud rings. This is not bad luck — it's a pattern.

| Vector | Fraud Ring | WAL Exposure | Reserved | Unreserved | Status |
|--------|-----------|-------------|----------|------------|--------|
| **1. First Brands / Point Bonita** | DOJ-indicted (Jan 29 2026) | [DATA NEEDED — via Jefferies fund] | [DATA NEEDED] | [DATA NEEDED] | Active — Jefferies confirmed $17M Q1 loss |
| **2. Tricolor** | $800M confirmed fraud | [DATA NEEDED — WAL specific] | [DATA NEEDED] | [DATA NEEDED] | Active litigation (JPM, Barclays, Fifth Third) |
| **3. Stupin / Cantor Group CRE** | Collateral subordination | **$98.6M** | **$30M (30%)** | **$38–68M** | Under-provisioned vs ZION 83% benchmark |

**Stupin is the only vector with quantified WAL-specific exposure.** First Brands and Tricolor WAL exposures are confirmed but not yet dollar-quantified in public filings.

---

## Total Estimated Exposure

| Scenario | Stupin | First Brands | Tricolor | Total |
|----------|--------|-------------|----------|-------|
| **Known/Reserved** | $30M | ~$0 disclosed | ~$0 disclosed | ~$30M |
| **Probable Additional** | $38–68M | [DATA NEEDED] | [DATA NEEDED] | $38–68M + unknowns |

**Conservative floor:** $68M unreserved (Stupin alone at ZION-matching 83% loss rate)
**With all three vectors:** Likely $100M+ total exposure, potentially significantly higher

---

## Key Dates

| Date | Event | Vector |
|------|-------|--------|
| Aug 2025 | WAL sued Cantor Group V | Stupin |
| Oct 2025 | Bloomberg: "Western Alliance faces First Brands risk" | First Brands |
| Oct 15 2025 | ZION disclosed Stupin fraud, charged off $50M | Stupin |
| Oct 16 2025 | WAL 8-K disclosure, $30M reserve | Stupin |
| Jan 29 2026 | DOJ indicts First Brands | First Brands |
| Feb 25 2026 | Jefferies sued (First Brands) | First Brands |
| Feb 27 2026 | WAL -10.64% Convergence Day (zero WAL-specific news) | All |
| Mar 2 2026 | WAL -10.82% on CRE litigation disclosure | Stupin/CRE |
| Mar 25 2026 | Jefferies Q1: $17M loss confirmed (First Brands + MFS) | First Brands |
| **Apr 21 2026** | **WAL Q1 earnings — must address all three** | **All** |

---

## Transmission Map

```
FIRST BRANDS ($9.3B debt)          TRICOLOR ($800M fraud)          STUPIN/CANTOR ($270M+)
     │                                   │                              │
     ▼                                   ▼                              ▼
DOJ indictment                   Bank creditor litigation         Collateral subordination
Jan 29 2026                      JPM/Barclays/Fifth Third         Title forgery, armed seizure
     │                                   │                              │
     ▼                                   ▼                              ▼
Jefferies leveraged fund ──►     Grant Thornton auditor ──►      WAL direct lender
Jefferies $17M Q1 loss           (same as CVNA/DriveTime)        $98.6M / $30M reserved
     │                                   │                              │
     ▼                                   ▼                              ▼
  WAL EXPOSURE                     WAL EXPOSURE                   WAL EXPOSURE
  (via intermediary)               (via auto/BDC chain)           (direct, quantified)
```

**Common thread:** All three involve collateral fraud — double-pledging, subordination, or falsification. WAL's underwriting failed to catch the same category of fraud from three independent sources.

---

## Files

| File | Content |
|------|---------|
| `FIRST_BRANDS.md` | Vector 1 deep dive |
| `TRICOLOR.md` | Vector 2 deep dive |
| `STUPIN_CRE.md` | Vector 3 deep dive |
| `CONVERGENCE.md` | Pattern analysis — why three frauds at one bank matters |
| `sources/README.md` | Source document index |

**Canonical research:** `../research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md` (Stupin deep comparison)
