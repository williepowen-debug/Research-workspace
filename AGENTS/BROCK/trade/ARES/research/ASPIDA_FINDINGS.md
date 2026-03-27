# ASPIDA Deep Dive — Phase 1 Findings
**Date:** 2026-03-26 | **Agent:** BROCK | **Status:** PARTIAL (statutory data obtained; NAIC cocode unconfirmed)

---

## 1. Legal Entity Map

All entities found via EDGAR company search:

| Entity | Type | Domicile | SEC CIK |
|--------|------|----------|---------|
| **Aspida Life Insurance Company (ALIC)** | US Life Insurer | **Michigan** (redomesticated Apr 2022) | 0001934234 |
| **Aspida Life Re Ltd.** | Reinsurer | Bermuda (Class E per ARES 10-K) | 0001934206 |
| **Aspida Re Cayman Ltd. ("AReC")** | Reinsurer | **Cayman Islands** (Class B(iii)) | — |
| **Aspida Holdings Ltd.** | Parent Holdco | **Cayman Islands** (redomesticated from Bermuda Jan 1, 2025) | — |
| Aspida Holdings LLC | US Holdco | — | — |
| Aspida Re (Bermuda) Ltd. | Reinsurer | Bermuda | — |
| Aspida Re Services Ltd. | Services | — | — |
| Aspida Financial Services, LLC | Admin/Services | Delaware | — |
| Aspida Financial Distributors, LLC | Broker-Dealer | Delaware | — |
| Aspida 360, Inc. | — | — | — |
| Aspida Risk Advisors, LLC | — | — | — |

**Key structure note:** Aspida Holdings Ltd. redomesticated from Bermuda → Cayman Islands effective January 1, 2025. The ARES 2025 10-K still refers to "Aspida Re, a Bermuda Class E insurance company" — likely referring to Aspida Life Re Ltd., a separate entity from AReC.

**History:** Aspida Life Insurance Company was formerly **UBS Life Insurance Company USA**, acquired by Aspida Holdings Ltd. in November 2021. Name legally changed December 1, 2021. Originally incorporated in California in 1956; redomesticated to Michigan April 2022.

---

## 2. Domiciliary State & NAIC Number

- **Domiciliary state:** Michigan
- **Regulator:** Michigan Department of Insurance and Financial Services (MiDIFS)
- **NAIC number:** **UNCONFIRMED** — NAIC CIS database blocked programmatic search. The company formerly traded as UBS Life Insurance Company USA (California domicile). Will need manual lookup via [NAIC CIS](https://content.naic.org/cis/searchBasic.do) or Michigan DIFS portal.
- **Licensed in:** District of Columbia and all states **except New York**

**SEC filings:** CIK 0001934234. Files N-4/N-4A (variable annuity registrations). Statutory financial statements embedded in prospectus filings — these are the primary public source of statutory data.

Source: ARES 2025 10-K (ares-20251231.htm); N-4/A filed 2025-08-29, exhibit tm2518749d1_n4a.htm

---

## 3. Offshore/Bermuda Structure

### Primary offshore entity: **Aspida Re Cayman Ltd. ("AReC")**
- Class B(iii) insurer, domiciled **Cayman Islands**
- Effective December 1, 2023: ALIC entered funds withheld coinsurance agreement with AReC
- April 1, 2024: Agreement amended to cover 2023 and 2024 business issued on/before June 30, 2024
- July 1, 2024: New agreement expanded to cover all newly written MYGA and FIA premiums on or after July 1, 2024
- **2024 totals ceded to AReC:** Ceded premiums = $2.86B; Ceded reserves = $3.54B

### Third-party offshore cession
- Effective May 1, 2024: Separate cession to **non-affiliated Class B(iii) insurer, Cayman Islands**
- 2024 ceded premiums: $511M; Ceded reserves: $490M

### Assumed reinsurance
- Effective June 1, 2024: ALIC **assumed** a quota share from a **non-affiliated insurer domiciled in Delaware**
- 2024 assumed premiums: $346M; Assumed reserves: $358M

### Holdings structure shift
- **Aspida Holdings Ltd.** (the ARES-linked parent) redomesticated Bermuda → Cayman Islands, January 1, 2025
- Effective April 1, 2025: ALIC amended its cession treaty to adjust quota shares going forward

**The structure:** ALIC writes annuities in the US → cedes most liabilities to AReC in Cayman on a **funds withheld coinsurance** basis (ALIC keeps the assets, AReC bears the risk and earns investment spread). This is the Athene/Bermuda template adapted to Cayman.

---

## 4. Statutory Financial Statements

**Source:** ALIC N-4/A (filed 2025-08-29), statutory financial statements for years ended December 31, 2024 and 2023. *(Audited)*

### Balance Sheet — Key Items ($thousands)

| Item | Dec 31, 2024 | Dec 31, 2023 | YoY Change |
|------|-------------|-------------|------------|
| **Total admitted assets** | **$7,711,458** | **$3,080,855** | **+150%** |
| Bonds (total) | 6,377,111 | 2,623,116 | +143% |
| — U.S. government bonds | 24,720 | — | — |
| — Industrial & misc (corporate) | 3,051,010 | — | — |
| — ABS | 1,447,258 | — | — |
| — CMBS | 722,068 | — | — |
| — RMBS | 889,588 | — | — |
| Mortgage loans | 276,836 | 1,615 | +17,000%+ |
| Derivatives | 199,407 | 67,430 | +196% |
| Other invested assets | 151,158 | 20,789 | +627% |
| Preferred stocks | 10,500 | — | — |
| Cash + equivalents | 581,646 | 298,283 | +95% |
| **Total cash & invested assets** | 7,603,906 | 3,017,144 | +152% |
| Reinsurance receivables | 2,633 | 12,115 | -78% |
| Separate account assets | 1,528 | 1,774 | — |

| **LIABILITIES** | Dec 31, 2024 | Dec 31, 2023 | YoY |
|----------------|-------------|-------------|-----|
| Aggregate reserve for life contracts | 2,927,845 | 2,068,747 | +41% |
| Liability for deposit-type contracts | 8,041 | 22 | — |
| **Asset Valuation Reserve (AVR)** | **39,105** | **10,625** | **+268%** |
| **Funds held under reinsurance (unauthorized reinsurers)** | **3,867,938** | **555,366** | **+597%** |
| Due to reinsurers | 230,212 | — | — |
| Derivative collateral liability | 130,422 | — | — |
| Interest maintenance reserve (IMR) | 679 | 182 | — |
| Payable to affiliates | 14,869 | 9,548 | — |
| **Total liabilities** | 7,278,408 | 2,728,829 | +167% |

| **CAPITAL & SURPLUS** | Dec 31, 2024 | Dec 31, 2023 |
|----------------------|-------------|-------------|
| Common stock (25,000 shares @ $100 par) | 2,500 | 2,500 |
| Paid-in & contributed surplus | 566,666 | 416,666 |
| **Unassigned deficit** | **(136,116)** | **(67,140)** |
| **Total capital & surplus** | **433,050** | **352,026** |
| Total liabilities + surplus | $7,711,458 | $3,080,855 |

### Income Statement — Key Items ($thousands)

| Item | 2024 | 2023 | 2022 |
|------|------|------|------|
| Premium & annuity considerations | 783,928 | 1,447,149 | 627,051 |
| Investment income (net) | 306,834 | 109,253 | 6,212 |
| Commissions from reinsurance ceded | 203,491 | 2,507 | — |
| Amortization of deferred reinsurance gain | 43,526 | — | — |
| Modified coinsurance assumed adjustment | 24,472 | 22,119 | 21,451 |
| **Total revenues** | **1,363,718** | **1,581,500** | **654,745** |
| Annuity benefits | 28,649 | 23,714 | 5,059 |
| Surrender benefits | 61,671 | 21,661 | 15,591 |
| Commissions & brokerage expense | 307,307 | 134,361 | 18,950 |
| Increase in aggregate reserves | 859,098 | 1,413,077 | 655,670 |
| Reinsurance investment credit | 137,309 | 3,339 | — |
| General insurance expenses | 42,665 | 28,876 | 13,458 |
| **Total deductions** | **1,441,574** | **1,626,347** | **709,291** |
| **Loss from operations (pre-tax)** | **(~77,856)** | **(~44,847)** | **(~54,546)** |

---

## 5. Key Risk Metrics vs. Athene Benchmarks

| Metric | Aspida (Dec 2024) | Athene (benchmark) | Notes |
|--------|-------------------|--------------------|-------|
| **Total admitted assets** | $7.7B | $310B+ | Aspida = tiny vs Athene |
| **Total capital & surplus** | $433M | — | |
| **Reinsurance ceded / surplus** | 3,867,938 / 433,050 = **8.9x** | ~55x (Athene) | Still significant; offshore cession structure |
| **Unassigned surplus** | **NEGATIVE** (-$136M) | Positive | 🚨 Cannot pay dividends without regulator approval |
| **AVR** | $39.1M | — | Growing fast (+268% YoY) |
| **Affiliated LP investments** | $142M (1.8% of assets) | — | 9 affiliated LPs = Ares funds |
| **Affiliated ABS** | $69M (0.9% of assets) | — | 10 affiliated ABS securities |
| **Total affiliated paper** | ~$211M (~2.7% of assets) | High at Athene | **Low % BUT** all investments managed by Ares Insurance Solutions (affiliated) |
| **Unfunded commitments** | $267M | — | Future Ares deal pipeline |

---

## 6. Affiliated Investment Exposure (The Smoking Gun Check)

From Note 9 (Related Party Transactions):
- **9 affiliated limited partnership investments** as of Dec 31, 2024 — NAV = **$142.4M** (vs $20.8M in 2023 = +6.8x)
- **10 affiliated ABS** as of Dec 31, 2024 — carrying value = **$68.9M** (vs $13.9M in 2023 = +5.0x)
- **All investments managed by Ares Insurance Solutions LLC** (affiliated entity, fee-bearing)
- Ares Insurance Solutions charged $11.6M in fees for 2024 (up from $9.0M in 2023, $0.6M in 2022)

**Key note:** The ABS portfolio is $1.447B total — unknown how much is ARCC paper or other Ares-originated assets. Only $68.9M explicitly labeled as "affiliated ABS." This is the area for deeper investigation (ARCC paper, Ares CLO equity, etc.).

---

## 7. Capital Structure Red Flags

1. **Negative unassigned surplus**: $(136M) as of Dec 31, 2024 — **zero dividends payable** without MiDIFS Commissioner approval (per Michigan law, max dividend = 10% of prior surplus or net income; both thresholds = $0)

2. **Funded by capital injections**: Holdings LLC injected $150M (2024), $247M (2023), $75M (Jan-May 2025). Company is not self-sustaining.

3. **Offshore cession ratio exploding**: Funds held under reinsurance treaties with unauthorized reinsurers grew **+597% in one year** ($555M → $3.87B). This is the economic cession to Cayman-domiciled AReC — assets stay onshore but economic risk/reward goes offshore.

4. **Operating losses every year**: Loss from operations 2022, 2023, 2024 — a growth-phase annuity insurer, being built out rapidly.

5. **AUM vs. balance sheet mismatch**: ARES 10-K says AIS manages $25.9B AUM "for Aspida" — but ALIC's admitted assets are only $7.7B. The gap (~$18B) is likely in the Bermuda/Cayman entities (Aspida Life Re Ltd. and AReC) where offshore reserves are parked.

---

## 8. The Offshore AUM Gap

**Critical discrepancy:**
- AIS manages $25.9B for "Aspida" (ARES 2025 10-K, as of Dec 31, 2025)
- ALIC admitted assets: $7.7B (Dec 31, 2024) — likely ~$9-10B by Dec 31, 2025

**Inferred offshore AUM**: ~$16-18B in AReC (Cayman) + Aspida Life Re Ltd. (Bermuda) + Aspida Re (Bermuda) entities — these are the "unauthorized reinsurers" receiving ceded reserves via funds withheld treaties.

This means the REAL statutory risk pool is spread across multiple Cayman/Bermuda entities with limited US regulatory visibility. Michigan MiDIFS only directly supervises ALIC's $7.7B balance sheet.

---

## 9. Statutory Filings — Sources Found

| Document | Type | Period | URL |
|----------|------|--------|-----|
| N-4/A (with statutory financials) | SEC filing | Dec 31, 2024 audited + Jun 2025 unaudited | https://www.sec.gov/Archives/edgar/data/1934234/000110465925085511/tm2518749d1_n4a.htm |
| ARES 2025 10-K | Annual report | FY2025 | https://www.sec.gov/Archives/edgar/data/1176948/000162828026011413/ares-20251231.htm |
| ARES SEC filings | All | Various | CIK 1176948 |
| Aspida Life Insurance Co SEC filings | N-4/40-APP | Various | CIK 1934234 |

**Not found (publicly):** ALIC's NAIC Annual Statement (filed with Michigan MiDIFS). This would show the full Schedule D (investments), Schedule F (reinsurance), and RBC ratio. This is behind a paywall (S&P Global Market Intelligence, AM Best, or SNL Financial).

---

## 10. What's Still Missing / Needs Will's Help

### Immediate gaps:
1. **NAIC Cocode** — blocked by NAIC CIS programmatic search. Will can look up at [https://content.naic.org/cis/searchBasic.do](https://content.naic.org/cis/searchBasic.do) (search "Aspida Life Insurance Co" or state "Michigan") — takes 30 seconds
2. **Full NAIC Annual Statement** — available via SNL Financial / S&P Global Market Intelligence (Bloomberg has partial). Would show:
   - Full Schedule D (all bonds — can confirm ARCC paper, Ares CLO positions)
   - Schedule F (reinsurance — full treaty details)
   - RBC ratio (vs 300% Authorized Control Level = danger zone)
3. **Aspida Life Re Ltd. financials** — Bermuda. BMA publishes limited data. AM Best rating may exist.
4. **Aspida Re Cayman Ltd. financials** — Cayman Islands regulatory filing. Very limited public access.
5. **ARES owns what % of Aspida?** — the 10-K says "AIS acts as dedicated investment manager" but doesn't specify ownership %. Earlier filings or press releases may clarify.

### Paywall sources:
- **SNL Financial / S&P Global Market Intelligence** — NAIC Annual Statements (full statutory data)
- **AM Best** — ratings report, RBC ratio (if ALIC has an AM Best rating)
- **Bloomberg BLP** — ALIC bloomberg issuer search

---

## 11. Thesis Implications

### Key findings for the ARES thesis:

**CONFIRMED:** The Athene/Apollo template is being replicated:
- Offshore cession structure (Cayman, not Bermuda like Athene)
- Funds withheld coinsurance = assets onshore, risk offshore
- All investments managed by affiliated Ares entity (fee-generating for ARES)
- Affiliated fund investments growing fast (LPs + ABS = Ares deal pipeline)

**IMPORTANT NUANCE:** Aspida is SMALL relative to what ARES reports:
- AIS manages $25.9B for "Aspida" total (Dec 31, 2025)
- ALIC admitted assets only $7.7B (Dec 31, 2024)
- ~$16-18B is offshore in Cayman/Bermuda entities with no US public filings

**RED FLAGS for the bear thesis:**
1. **Negative unassigned surplus** — company is loss-making, funded by parent injections
2. **Offshore cession explosion** (+597% YoY) — rapid hollowing of onshore balance sheet
3. **Reinsurance with "unauthorized" reinsurers** — AReC is not authorized in Michigan → ALIC holds the assets as "funds withheld" but the credit risk of getting back those reserves if AReC fails is real
4. **$267M unfunded commitments** to Ares LPs and ABS — future captive deal pipeline
5. **No dividends possible** to parent — this is a capital-consuming machine, not a capital-returning one

**For the bull counterargument:**
- ALIC has only $7.7B in admitted assets — systemic risk from Aspida alone is contained
- The reinsurance offset: ALIC holds the assets (funds withheld), so if AReC failed, ALIC would have the bonds
- Growth is massive but from a small base

**The ARES-specific risk:** ARES reduced its own credit investments (-28%) while growing Aspida. This suggests a deliberate shift — using Aspida/AIS to originate and hold yield assets that ARES itself used to hold. The affiliated LP/ABS investments in ALIC are growing 5-7x per year. This is the mechanism worth tracking.

---

## 12. Next Steps

1. **Will:** Look up NAIC cocode at naic.org (5 minutes) — enables direct MiDIFS filing access
2. **Will:** Request ALIC NAIC Annual Statement via SNL/Bloomberg — full Schedule D is the key piece
3. **Phase 2 research:** Pull the Bermuda Class E filing for Aspida Life Re Ltd. (BMA public register)
4. **Phase 2 research:** Find ARES ownership % in Aspida via ARES proxy or 10-K subsidiary schedule
5. **Cross-agent:** Flag to REGINALD — Aspida is writing MYGA/FIA products; rising policyholder lapses in rate environment would pressure the cession treaties

---

*Sources: ARES 2025 10-K (SEC CIK 1176948); Aspida Life Insurance Co N-4/A (SEC CIK 1934234, filed 2025-08-29); EDGAR company search*
