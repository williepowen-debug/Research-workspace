# OZK Gap Closure Plan — Before April 16 Earnings
**Created:** 2026-03-23 | **Source:** AUDIT_REPORT.md
**Goal:** B+ → A folder. 7 fixes, 24 days.

---

## FIX 1: Pull Q4 2025 Primary Data 🔴 CRITICAL
**Gap:** All Q4 2025 numbers sourced secondhand from Temple 8.
**Attack:**
- Pull OZK Q4 2025 earnings release from IR page (ozk.com)
- Pull 10-Q from EDGAR (should be filed by now — search CIK 0001609065)
- Extract: ACL balance, charge-offs, NCO rate, RESG %, noncurrent loans, unfunded commitments
- Build ACL bridge: $619M (Dec 2024) → peak $680M (Sep 2025) → $632M (Dec 2025)
- **Who:** Spawn into OZK folder with extraction task
- **Time:** 1 session, ~30 min

## FIX 2: Source IQHQ RaDD Independently 🔴 CRITICAL
**Gap:** Thesis climax loan ($915M) has zero primary sourcing — funded amount, valuation, tenants, maturity all from Temple 8.
**Attack:**
- Search EDGAR for OZK 10-Q/10-K IQHQ disclosures (likely in "significant loans" or "concentration" footnotes)
- CoStar/CBRE San Diego RaDD campus — leasing activity, vacancy, asking rents
- Google: "IQHQ RaDD San Diego tenant" + "IQHQ RaDD lease" for news
- Look for Rebel Cole's analysis (Temple 8 cites him — find the original)
- Check if IQHQ has SEC filings or press releases
- **Who:** Can be done in parallel — Will can Google IQHQ news while agent pulls EDGAR
- **Time:** 1-2 sessions

## FIX 3: Reconcile CRE Concentration Denominators 🟠 HIGH
**Gap:** 455% / 415% / 358% / 900% used interchangeably with different denominators.
**Attack:**
- From 10-K: calculate CRE / Tier 1 Capital (should give ~415%)
- From 10-K: calculate CRE / Tangible Equity (should give ~455%)
- From KBRA citation: note their scope (probably on-balance-sheet only, different CRE definition)
- Moody's "nearly twice" = on-B/S + unfunded (~900%)
- Write one reconciliation table in EVIDENCE.md with date, source, denominator, result
- **Who:** Agent with 10-K + calculator
- **Time:** 15 min, can bundle with Fix 1

## FIX 4: Fill RC-C Data 🟠 HIGH
**Gap:** Empty placeholder in EARNINGS_PREP.md. Need state-level noncurrent rates for OZK specifically.
**Attack:**
- FFIEC CDR (cdr.ffiec.gov) → search Bank OZK → Schedule RC-C Part I
- Pull: nonfarm nonresidential by state (FL, NY, CA, IL, GA)
- Compare institution-level vs FDIC district benchmarks already in EVIDENCE.md
- If CDR doesn't break by state, check Schedule RC-N (past due by loan type)
- **Who:** Agent or Will can pull from FFIEC CDR website
- **Time:** 1 session, ~30 min

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

## FIX 6: Resolve Life Sciences $3.2B vs $1.85B 🟡 MEDIUM
**Gap:** Temple 8 says $3.2B, 10-K shows $1.85B funded.
**Attack:**
- Check if $3.2B includes unfunded commitments (10-K should have unfunded by property type)
- Check if it includes adjacent categories (medical office, lab-industrial hybrids)
- If the gap is unfunded: note it explicitly. If it's a different definition: note that.
- If can't resolve: flag in THESIS.md as "reported $3.2B (Temple 8) vs $1.85B funded (10-K)" and use the conservative number
- **Who:** Bundle with Fix 1 (10-Q pull)
- **Time:** 15 min

## FIX 7: Resolve Construction ACL Discrepancy 🟡 MEDIUM
**Gap:** $85M and $139M both appear for construction ACL in 2024.
**Attack:**
- Re-read 10-K ACL movement table carefully
- Likely: $139M = total construction ACL, $85M = specific reserve (with $54M general). Or vice versa.
- Verify and annotate in EVIDENCE.md
- **Who:** Bundle with Fix 1
- **Time:** 10 min

---

## EXECUTION PLAN

### Phase 1: Primary Data (This week, before Mar 28)
- **Fixes 1 + 3 + 6 + 7** — One spawn session pulls 10-Q from EDGAR, extracts Q4 2025 data, reconciles CRE denominators, resolves life sciences and construction ACL discrepancies. ~1 hour.
- **Fix 2 (IQHQ)** — Parallel: Will Googles IQHQ news/leasing, agent searches EDGAR for OZK IQHQ disclosures. ~30 min each.

### Phase 2: Institutional Data (Next week, before Apr 7)
- **Fix 4 (RC-C)** — Pull from FFIEC CDR. Compare institution vs district. ~30 min.
- **Fix 5 (Scenarios)** — Requires Fix 1 data. Build bull/base/bear with stock targets. ~1 session.

### Phase 3: Final Review (Apr 7-14)
- Update EVIDENCE.md with all new data
- Re-run audit agent to verify fixes
- Final EARNINGS_PREP.md update with RC-C data and scenario framework
- Confirm all research agenda items checked off

**Target:** A folder by Apr 14, two days before earnings.

---

*After each fix, mark complete here and update the relevant file.*
