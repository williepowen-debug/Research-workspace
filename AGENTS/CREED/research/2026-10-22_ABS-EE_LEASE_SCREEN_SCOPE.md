# Scope — an office "largest lease expires before the loan matures" screen from SEC ABS-EE data

**Written:** 2026-10-22 (Thu) 13:48 ET · **Asked by:** Will, 2026-10-22: *"Scope it first"* (on the ABS-EE build question). **This page is the scope, not the build. Nothing is built until Will says so.**
**Origin:** refi-screen direction 2 (`research/2026-09-30_REFI_SCREENS_FOLLOWUP.md`); no publisher prints a national office version (only Trepp's Los Angeles one, 8/21).

---

## 1. The question it would answer

How much performing office CMBS debt has its **largest tenant's lease ending before the loan matures**, and how much of that sits on loans that are already thin (DSCR < 1.25x or occupancy < 80%)? That is the refinancing risk that has not yet shown up in delinquency: the loan pays today, but the lender at maturity underwrites a building that may lose its anchor.

**Why it matters to the thesis:** office DQ is one print from firing `CREED-T-01a`. Trepp's own September read is that the maturity book is **converting** into delinquency, not clearing (`KB-CREED-057`). This screen would size the **next** wave of conversions by maturity year, instead of waiting for them to print.

## 2. Data — verified at source 2026-10-22

SEC Regulation AB II requires **registered** CMBS trusts to file a monthly asset-level exhibit (Form ABS-EE, EX-102). CREED opened one: Benchmark 2024-V7, filing `0001888524-26-013329`, July 2026, **27 loans, 300 KB of XML**. Every field the method needs is present:

| Need | ABS-EE field (confirmed present) |
|---|---|
| Property type | `propertyTypeCode` |
| Largest tenant, its size, its lease end | `largestTenant`, `squareFeetLargestTenantNumber`, `leaseExpirationLargestTenantDate` (2nd and 3rd tenants too) |
| Building size | `netRentableSquareFeetNumber` |
| Loan maturity | `maturityDate`, `postModificationMaturityDate` |
| Cash-flow cover and occupancy | `mostRecentDebtServiceCoverageNetCashFlowpercentage`, `mostRecentPhysicalOccupancyPercentage` |
| Balance (to weight by dollars) | `reportPeriodEndActualBalanceAmount` |
| How fresh the tenant data is | `mostRecentAnnualLeaseRolloverReviewDate` |

**Cost:** free (SEC EDGAR, declared User-Agent, rate-limited to ~10 requests/second).

## 3. What it would and would not cover

| Covered | NOT covered |
|---|---|
| Registered (public) conduit CMBS, roughly 2017+ vintages | **144A deals: most SASB and all CRE CLOs** (off EDGAR) |
| Office, and the same method works for any property type | **Pre-2017 conduits** (no asset-level filing) |
| Monthly refresh as trusts file | **Bank balance sheets** (the bigger office lender) |
| | **Extension options:** the schema has no extension field (checked: no tag containing "extens"), so "hard vs extendable" maturity is not derivable |

⇒ It measures **one slice** (public conduit office) well. It must never be presented as "the office market" or summed with Trepp's all-CMBS figures without naming that perimeter (trap #5).

## 4. Method (if built)

1. List every ABS-EE filing in the latest month (EDGAR full-index, form type `ABS-EE`), fetch each EX-102.
2. Keep office loans; **de-duplicate pari-passu pieces** of the same loan held across several trusts (match on property name + address + origination, else balances double-count; Trepp uses its own ID for this).
3. Flag `leaseExpirationLargestTenantDate < maturityDate`; bucket by the largest tenant's share of rentable area (>30%, >50%) and by maturity year (2026–2029).
4. Cross with DSCR < 1.25x and occupancy < 80%; weight everything by current balance.
5. Report only when the tenant review date is within ~15 months; count and disclose the rest as stale.
6. **Positive control before trusting any total (trap #25):** reproduce Trepp's Los Angeles figures (8/21) from the same data within tolerance, or say why not.

## 5. Effort and what Will would get

- **Build:** one script in `AGENTS/CREED/scripts/` plus fixture tests, roughly **3–5 hours** of session time (most of it on de-duplication and the positive control). **Monthly run:** minutes. The trust count is not yet measured (an earlier agent estimated "a few hundred"); the first run would count it.
- **Output:** a dated table by maturity year: balance and count with the anchor lease ending first, split by anchor share and by DSCR/occupancy stress, plus coverage disclosures. One KB row per run; a VX vector only if Will approves one (a new instrument is a definition, so it is proposed, not added).
- **Risks:** pari-passu double counting (the main error source); stale tenant fields; a false sense of coverage (point 3 above).

## 6. Decision for Will

Build it (≈3–5 h, free data, public-conduit perimeter only), or park it until after the October Trepp print. **CREED's lean: build it after the October print**, so the first run can be read against the fresh `T-01a` outcome, and only if Will wants a forward-looking office instrument rather than waiting on the monthly prints.
