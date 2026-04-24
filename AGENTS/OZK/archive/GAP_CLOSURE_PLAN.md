# OZK Gap Closure Plan — Before April 16 Earnings
**Created:** 2026-03-23 | **Source:** AUDIT_REPORT.md
**Goal:** B+ → A folder. 7 fixes, 24 days.

---

## FIX 1: Pull Q4 2025 Primary Data ✅ COMPLETE
**Gap:** All Q4 2025 numbers sourced secondhand from Temple 8.
**Result:** Pulled from Q4 Mgmt Comments + 8-K Financial Supplement. Key corrections: ACL ratio 1.26% not 1.16%, coverage 1.6x not <1.0x, CRE/TCE 387% not 455%. NPLs doubled Q3→Q4. THESIS.md + EVIDENCE.md updated. → `sources/10K_Q4_2025_EXTRACT.md`
**Attack:**
- Pull OZK Q4 2025 earnings release from IR page (ozk.com)
- Pull 10-Q from EDGAR (should be filed by now — search CIK 0001609065)
- Extract: ACL balance, charge-offs, NCO rate, RESG %, noncurrent loans, unfunded commitments
- Build ACL bridge: $619M (Dec 2024) → peak $680M (Sep 2025) → $632M (Dec 2025)
- **Who:** Spawn into OZK folder with extraction task
- **Time:** 1 session, ~30 min

## FIX 2: Source IQHQ RaDD Independently ✅ COMPLETE
**Gap:** Thesis climax loan ($915M) has zero primary sourcing — funded amount, valuation, tenants, maturity all from Temple 8.
**Result:** Core numbers confirmed via Bisnow, Commercial Observer, Seeking Alpha. CRITICAL FINDING: two-year loan extension (Bisnow Oct 2024) → maturity likely ~Aug 2028, not 2026. IQHQ injected $87M equity. Occupancy 3% (1 tenant). Cole values at ~$500M vs $555M funded. SD vacancy 25-29%. THESIS.md + EVIDENCE.md updated. → `sources/IQHQ_RADD_RESEARCH.md`
**Attack:**
- Search EDGAR for OZK 10-Q/10-K IQHQ disclosures (likely in "significant loans" or "concentration" footnotes)
- CoStar/CBRE San Diego RaDD campus — leasing activity, vacancy, asking rents
- Google: "IQHQ RaDD San Diego tenant" + "IQHQ RaDD lease" for news
- Look for Rebel Cole's analysis (Temple 8 cites him — find the original)
- Check if IQHQ has SEC filings or press releases
- **Who:** Can be done in parallel — Will can Google IQHQ news while agent pulls EDGAR
- **Time:** 1-2 sessions

## FIX 3: Reconcile CRE Concentration Denominators ✅ COMPLETE (bundled with Fix 1)
**Gap:** 455% / 415% / 358% / 900% used interchangeably with different denominators.
**Result:** Full reconciliation table in extract. CRE/Tier1=358%, CRE/TCE=387%, TotalRE/TCE=425%, CRE/TotalRBC=302%. 455% unreproducible. 900% unreproducible (best: 682%). THESIS.md + EVIDENCE.md updated.
**Attack:**
- From 10-K: calculate CRE / Tier 1 Capital (should give ~415%)
- From 10-K: calculate CRE / Tangible Equity (should give ~455%)
- From KBRA citation: note their scope (probably on-balance-sheet only, different CRE definition)
- Moody's "nearly twice" = on-B/S + unfunded (~900%)
- Write one reconciliation table in EVIDENCE.md with date, source, denominator, result
- **Who:** Agent with 10-K + calculator
- **Time:** 15 min, can bundle with Fix 1

## FIX 4: Fill RC-C Data 🟢 PARTIAL COMPLETE
**Gap:** Empty placeholder in EARNINGS_PREP.md. Need state-level noncurrent rates for OZK specifically.
**Result (Phase 1 — FDIC API, Mar 23):** Pulled 8 quarters of loan composition, noncurrent, ACL, charge-off data via FDIC API (CERT 110). Key findings: C&I +153% while construction -36.9% (reclassification proof). Noncurrent spiked to $341M (1.07%). ACL cut $56.6M into deterioration. Coverage collapsed to 1.39x. Data saved to `sources/FDIC_API_CALL_REPORT_DATA.md`, integrated into EVIDENCE.md + THESIS.md.

**Phase 2 COMPLETE (FFIEC CDR, Mar 23):** Will pulled full Call Report from cdr.ffiec.gov (RSSD 107244, Q4 2025). Key extractions:
- **RCON2746 = $1.289B** → Memo Item 3 / C&I = 37.6% ✅ confirmed
- **RC-N noncurrent**: 75.2% concentrated in other nonfarm nonres ($256.7M) — office/life sci
- **Interest reserves**: $7.0B of $7.8B construction book (89.7%) — massive artificiality
- **NDFI exposure**: $2.74B in loans to non-depository financial institutions
- Full data → `sources/FDIC_API_CALL_REPORT_DATA.md`

**Still missing:**
- State-level breakdowns (not in standard call report format)
- Construction ACL category breakdown (may need RC-R detail)

## FIX 5: Scenario Analysis + Target Prices 🟠 HIGH
**Gap:** No quantified bull/base/bear, no stock targets, no max drawdown tolerance.
**Attack:**
- **Bear case:** ACL depleted by Q3 2026. IQHQ writedown $200-300M. TBV erodes to ~$37-38. Stock trades to 0.9x TBV = $33-34. (May 2025 low was $35.71.)
- **Base case:** Charge-offs continue at $80-100M/quarter. ACL flat (they provision just enough). No IQHQ resolution. Stock drifts to $40-42 (1.0x TBV).
- **Bull case:** IQHQ gets a major tenant. Life sciences vacancy improves. ACL rebuilt to $700M+. Stock recovers to $55-60 (1.3x TBV). **This is the loss scenario for our puts.**
- **Squeeze scenario:** SI 14-15%, days-to-cover 12-18. Green day + positive headline = spike to $55-58. Temporary but painful. Max drawdown tolerance?
- Add to THESIS.md or create separate SCENARIOS.md
- **Who:** Agent with the data already in folder + 10-Q once pulled
- **Time:** 1 session after Fix 1

## FIX 6: Resolve Life Sciences $3.2B vs $1.85B ✅ PARTIAL (bundled with Fix 1)
**Gap:** Temple 8 says $3.2B, 10-K shows $1.85B funded.
**Result:** $3.1B total commitment confirmed (Figure 14, 10.7% of RESG). Funded/unfunded split NOT disclosed in Mgmt Comments. "$1.85B funded" remains unverified — may need Call Report. EVIDENCE.md updated with $3.1B total.
**Attack:**
- Check if $3.2B includes unfunded commitments (10-K should have unfunded by property type)
- Check if it includes adjacent categories (medical office, lab-industrial hybrids)
- If the gap is unfunded: note it explicitly. If it's a different definition: note that.
- If can't resolve: flag in THESIS.md as "reported $3.2B (Temple 8) vs $1.85B funded (10-K)" and use the conservative number
- **Who:** Bundle with Fix 1 (10-Q pull)
- **Time:** 15 min

## FIX 7: Resolve Construction ACL Discrepancy 🟡 DEFERRED
**Gap:** $85M and $139M both appear for construction ACL in 2024.
**Result:** Category-level ACL is NOT disclosed in Mgmt Comments or 8-K Financial Supplement. Only specific reserves on named substandard credits ($36.1M total). Need FFIEC Call Report (RC-R / RI-C) — bundle with Fix 4 (RC-C pull).
**Attack:**
- Re-read 10-K ACL movement table carefully
- Likely: $139M = total construction ACL, $85M = specific reserve (with $54M general). Or vice versa.
- Verify and annotate in EVIDENCE.md
- **Who:** Bundle with Fix 1
- **Time:** 10 min

---

## EXECUTION STATUS (Updated Mar 23, 10:20 PM ET)

| Fix | Status | Notes |
|-----|--------|-------|
| 1 | ✅ COMPLETE | Primary data extracted from Mgmt Comments |
| 2 | ⬜ OPEN | IQHQ — not disclosed in OZK filings, external sources only |
| 3 | ✅ COMPLETE | CRE denominators reconciled |
| 4 | ✅ COMPLETE | FDIC API + FFIEC CDR pulled |
| 5 | ✅ COMPLETE | SCENARIOS.md created, EV $38.75 |
| 6 | ✅ PARTIAL | $3.1B total confirmed, funded split unverified |
| 7 | 🟡 DEFERRED | Construction ACL — may not need separate pull |

### AUDIT GAPS (from AUDIT_REPORT_MAR23.md)
| Gap | Status | Notes |
|-----|--------|-------|
| A (Data integrity) | ✅ COMPLETE | All 8 contradictions fixed |
| B1 (State-level RC-C) | ❌ OPEN | Not in standard call report format |
| B2 (Uninsured deposits) | ✅ COMPLETE | $11.9B / 35.8% |
| B3 (NDFI $2.74B) | ✅ COMPLETE | 23 named counterparties via 4 deep research models |
| B4 (FHLB/liquidity) | ❌ OPEN | $23.9B pledged, borrowing capacity unknown |
| B5 (Bioterra source) | ✅ COMPLETE | Square Mile Capital co-originator, $203M Dec 2022 |
| B6 (Pacific Center "par") | 🟡 PARTIAL | Consistent with mgmt comments, not independently verified |
| B7 (Insider Form 4s) | ✅ COMPLETE | Prior data in INSIDER_SCAN_OZK.md. No new transactions per GuruFocus. CRO discretionary sale Feb 24 remains strongest signal. |
| B8 (IQHQ in OZK filings) | ✅ CONFIRMED ABSENT | Zero mention in any OZK filing |
| C (Weaknesses) | ✅ COMPLETE | C1-C3 rebuttals done. C4 Gleason framing corrected. C5 IQHQ timeline noted. |
| D (Opportunities) | ✅ COMPLETE | D1 LTV extrap, D2 pledged/liquidity, D3 shadow CRE lever, D4 problem bank, D5 dividend sustainability |
| E (Publication readiness) | ❌ OPEN | Temple 8 refs, PDNA geography inversion |

### Publishing Prep (Mar 24)
- Core findings are publication-ready
- Need to clean Temple 8 references
- Need to write standalone publishable piece (separate from internal files)

**Target:** A+ folder by Apr 14, two days before earnings.

---

*After each fix, mark complete here and update the relevant file.*
