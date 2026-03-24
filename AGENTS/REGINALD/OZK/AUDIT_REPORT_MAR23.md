# OZK Thesis Audit Report
**Auditor:** Reginald (subagent) | **Date:** 2026-03-24
**Files reviewed:** THESIS.md, EVIDENCE.md, SCENARIOS.md, EARNINGS_PREP.md, sources/FDIC_API_CALL_REPORT_DATA.md, GAP_CLOSURE_PLAN.md
**Overall grade:** B+ → gaps are closable but several internal contradictions need immediate cleanup

---

## A. DATA INTEGRITY

### Critical Contradictions (Fix Before Publishing)

**1. EARNINGS_PREP.md still contains debunked Temple 8 numbers**
The peer comparison table in EARNINGS_PREP.md lists:
- ACL ratio: `1.16%` ← explicitly corrected to **1.26%** in THESIS.md
- Coverage ratio: `<1.0x` ← explicitly debunked as "apples-to-oranges error" in THESIS.md
- CRE/Tier 1: `455%` ← corrected to **358%** in THESIS.md

This is a time bomb. If anyone reads EARNINGS_PREP.md expecting clean data, they get the wrong numbers. The Temple 8 correction never propagated fully to EARNINGS_PREP.md.

**2. NCO rate "1.18%" is mislabeled as Q4 rate throughout THESIS.md**
THESIS.md states: "Q4 2025 NCO rate: 1.18% (highest in 15 years)." But the FDIC API data shows Q4 2025 quarterly NCOs of $50.6M on a ~$31.8B book = **0.64% annualized** for Q4 specifically. The 1.18% is the **full-year 2025 annualized rate**, not Q4. This distinction matters because the Q4 trajectory ($50.6M) is actually *flat* vs Q3 ($48.3M) — it's not accelerating Q4 specifically. The annual rate is high, but calling it a "Q4 rate" overstates momentum. Every instance of "Q4 NCO rate: 1.18%" needs to be corrected to "FY2025 annualized NCO rate: 1.18%; Q4 2025 quarterly annualized: 0.64%."

**3. CRE/Tier 1 ratio has three different numbers across files**
- THESIS.md: **358%**
- EVIDENCE.md capital table: **358%** 
- FDIC_API_CALL_REPORT_DATA.md: **362%** (derived: $19,875,925 / $5,488,755)
- EARNINGS_PREP.md peer table: **455%**

362% vs 358% is a rounding/scope difference (probably construction definition). 455% is wrong and still lives in EARNINGS_PREP. Pick one number, one definition, one source. Inconsistency across files suggests copy-paste without reconciliation.

**4. Construction/Tier 1: 197% (KBRA) vs 142% (FDIC API)**
THESIS.md cites KBRA's "construction 197%." FDIC API derives $7,778M / $5,489M = **141.7%**. That's a 55-point gap. Either KBRA is using a broader construction definition (maybe including multifamily construction or unfunded) or the KBRA number is stale. This is cited without explanation. If someone checks the math, it doesn't hold.

**5. FY2025 charge-offs: $160M (THESIS) vs $172.5M (FDIC API)**
THESIS.md: "FY 2025 charge-offs: $160M." FDIC API RIAD data shows cumulative YTD NCOs Q4 2025: **$172,514K = $172.5M**. This is a $12.5M gap. Possible explanations: management figure excludes recoveries (net NCOs = gross minus recoveries), or there's a timing difference. Neither is stated. Use one number and explain which basis (gross vs net).

**6. EVIDENCE.md still contains a "Still need" note that's been resolved**
Bottom of the Memo Item 3 section in EVIDENCE.md says: *"Still need: RCON2746 from FFIEC CDR for definitive Memo Item 3 number. FDIC summary API doesn't carry it."* But FDIC_API_CALL_REPORT_DATA.md confirms RCON2746 was pulled and equals **$1.289B**. The EVIDENCE.md note was never cleaned up. Minor but sloppy — looks like unfinished research to an outside reader.

**7. ACL basis inconsistency: $475.7M vs $631.9M**
SCENARIOS.md Key Inputs table lists both:
- ACL (FDIC basis): $475.7M
- ACL (company basis, incl. unfunded): $631.9M

These are two genuinely different numbers (FDIC = funded loans only; company = includes unfunded commitments reserve). The coverage ratios derived from each are materially different (1.39x vs 1.6x). This is explained in THESIS.md but the SCENARIOS.md table presents them side-by-side without adequate labeling, creating confusion about which to use for the bear case math.

**8. Noncurrent % discrepancy: 1.07% (FDIC API) vs 1.06% (EVIDENCE.md)**
Minor but exists. EVIDENCE.md says "NPLs: $341M, **1.06%**." FDIC API table says $341,223 / total loans = **1.07%**. Pick one.

---

## B. GAPS

### Priority 1: Obtainable in the next 7 days

**Gap B1: State-level RC-C noncurrent rates (EARNINGS_PREP.md is empty)**
The RC-C Data table in EARNINGS_PREP.md has TBD for every state (FL, NY, CA, IL, GA). This is the single most important pre-earnings data pull. OZK lends heavily in NY (district noncurrent 1.57%) and FL/GA (Atlanta district 1.36%) — but those are district averages, not OZK's specific portfolio. The actual institution-level RC-C state breakdowns would show which states are driving the $256.7M of "other nonfarm nonresidential" noncurrent. Without this, the geographic stress narrative is inferred from district data, not proved. Pull from FFIEC CDR RC-C Part II (schedule available for banks with $300M+ in CRE) or Summary of Deposits.

**Gap B2: Deposit composition — uninsured deposit % at OZK specifically**
EVIDENCE.md cites the industry figure ($8.14T uninsured) but doesn't tell us OZK's own uninsured deposit percentage. FDIC API has this (CERT 110, deposit schedule). This matters because if a ratings downgrade triggers outflows, the question is how much of OZK's $34B in deposits is insured and "sticky" vs uninsured and flight-prone. A bank with 60%+ uninsured in a stress scenario faces a qualitatively different risk. This number is publicly available today.

**Gap B3: The $2.74B in NDFI loans — zero analysis**
FDIC_API_CALL_REPORT_DATA.md notes loans to Non-Depository Financial Institutions: **$2,742,514K = $2.74B**. This is enormous — nearly as large as the construction noncurrent book. What are these? Private credit funds? Bridge lenders? Real estate debt funds? This is almost certainly CRE-adjacent debt-on-debt exposure. EVIDENCE.md mentions it in passing ("debt-on-debt risk") but there's no analysis of counterparty type, collateral, or stress exposure. If these are loans to funds that themselves hold CRE, the true CRE exposure is materially understated. FFIEC Memo Item 9 and RCONPV06/PV07 breakdowns (already pulled: $1.2B business credit intermediaries, $772M PE funds) need to be worked into a stress scenario.

**Gap B4: FHLB borrowings and liquidity backstop**
The thesis mentions deposit flight risk but doesn't quantify OZK's liquidity buffer. How much FHLB capacity does OZK have? What's the pledged collateral ($23.9B pledged = 74% of total loans — this is massive and unexplored)? If loans are pledged, what's the available borrowing line? This is in the call report (RC-M) and FHLB filings. Without it, the tail scenario (Scenario D) is under-supported mechanically.

**Gap B5: Bioterra ($202M) — no primary source cited anywhere**
The $202M figure for Bioterra (Sorrento Mesa) appears in EVIDENCE.md without a source. Not a management disclosure, not a EDGAR filing, not a news citation. If this is wrong, it's a significant hole in the life sciences narrative. CoStar, local San Diego business press, or a simple EDGAR search for "Bioterra" should surface this.

**Gap B6: Pacific Center "par" sale — unverified management claim**
Management says Pacific Center was sold at par. EVIDENCE.md accepts this without challenge. If it wasn't par — if there was a loss absorbed before transfer or the "par" was on the funded amount vs current value — that's a material misrepresentation. FDIC Call Report should show the actual charge-off or gain/loss on sale. If charge-offs spiked in the quarter of the Pacific Center sale and management called it a "par" exit, something doesn't add up.

**Gap B7: Insider transaction Form 4s since Feb 24**
EARNINGS_PREP.md has a checklist item for new insider filings since Feb 24 (CRO Majumdar's sale date). Has this been pulled? It's a one-minute EDGAR search (EDGAR → Form 4 → OZK → sort by date). Any new CRO or CFO sale in the pre-earnings window would be highly material. Any purchase would weaken the thesis.

**Gap B8: OZK-specific IQHQ disclosure in filings**
The thesis says IQHQ is not disclosed in OZK filings — "all from external sources." This needs to be verified definitively. OZK's 8-K financial supplement and management comments for Q4 2025 should have a "significant loans" or "top 10 exposures" section. If IQHQ ($555M funded) doesn't appear there, that's a disclosure question worth flagging. If it does appear under a different name or structure, the thesis needs to update. GAP_CLOSURE_PLAN.md lists this as complete (Fix 2) but doesn't confirm whether OZK filing disclosure was checked — only that external sources were found.

---

## C. WEAKNESSES

### The Three Things That Could Break the Trade

**Weakness C1: The Memo Item 3 "reclassification" narrative is circumstantial**
The C&I +153% / construction -36.9% correlation is striking, but it has an innocent explanation: OZK explicitly announced a Corporate and Institutional Banking (CIB) strategy to diversify away from RESG. The thesis argues this is disguised CRE. But OZK would argue — and can prove with loan documentation — that these are genuine C&I loans to real corporate borrowers. The 37.6% Memo Item 3 ratio confirms that $1.29B of the C&I book is real-estate-linked, but the remaining $2.14B of C&I growth is uncharacterized. Without knowing whether the non-Memo-Item-3 C&I is genuinely diversifying or also CRE-adjacent, the reclassification narrative is half-proved. A sophisticated bull will say: "37.6% of C&I is RE-linked, yes — management disclosed this. The other 62.4% is real diversification." The thesis needs to address this directly.

**Weakness C2: The maturity wall thesis assumes no rate relief**
The 2022 vintage maturity wall is the thesis spine. But it assumes the refi market stays frozen through Q3 2026. If the Fed cuts materially (say, 100bps by mid-2026 — plausible given labor data and possible recession signals), cap rates compress, property values recover marginally, and sponsors can refinance. Even partial relief (30-40% of the vintage refinancing successfully) significantly extends the timeline and removes the "mechanical, not probabilistic" argument from SCENARIOS.md. The thesis has no scenario that models rate relief. This is the strongest bull argument and it's not addressed in the BULL CASE REBUTTALS table.

**Weakness C3: Capital adequacy genuinely buys time**
CET1 at 11.70% gives OZK massive absorption capacity. Even with a $300M IQHQ writedown, capital stays well above minimums. The tail scenario (Scenario D: capital event) is 5% probability and requires cascading failures. In reality, OZK can take significant losses before triggering any regulatory action — meaning the thesis is about stock repricing (multiple compression and earnings dilution), not existential bank failure. The market likely already prices some CRE stress at ~$42-43 (near TBV). The probability-weighted EV of $38.75 implies only 10% downside from current prices. That's a thin margin of safety for a thesis that requires the market to be meaningfully wrong, especially with 14-15% short interest that amplifies squeeze risk on any positive headline.

**Weakness C4: The "Gleason captive, not confident" framing is weak**
EVIDENCE.md presents CEO non-selling as bearish ("position too large to sell"). But a sophisticated reader will note that someone with 10% of a $4.7B market cap company has legitimate liquidity constraints even without any trading restrictions — you'd move the stock. Using the absence of selling as a signal when selling isn't practical isn't a real indicator. This looks like motivated reasoning. It should be cut or replaced with something substantive.

**Weakness C5: IQHQ timeline extension weakens Wave 3 and puts focus on Waves 1-2**
The extension to ~2028 means IQHQ is no longer a 2026 catalyst. The thesis acknowledges this but the whale is still prominently featured as a core risk. What's the actual Wave 1-2 catalyst stack without IQHQ? It's the $341M noncurrent (already recognized) + construction maturity wall + Bioterra. Is that enough to move a $4.7B stock 20-30%? The answer is maybe, but the case needs to be made cleanly without leaning on IQHQ for near-term catalysis when its timeline is 2028.

---

## D. OPPORTUNITIES

### Angles That Are Under-Exploited

**Opportunity D1: The LTV reappraisal data extrapolation hasn't been run**
EVIDENCE.md contains a critical data point buried in the office stress section: two OZK office loans were reappraised in Q4, with LTVs jumping from 52.9% → 98.9% (+46pts) and 93.2% → 111.5% (+18pts). This implies property values declined roughly 50% from origination for these specific loans. If even a subset of the $3.7B office portfolio (avg LTV 55% at origination) has experienced similar value decline, the implied impairment is enormous. The math: if 30% of the office book has moved from 55% LTV to 90% LTV, that's ~$1.1B of loans where collateral is now insufficient. No one has run this extrapolation. Run it with conservative assumptions (15%, 20%, 30% of office book) and it becomes one of the most powerful paragraphs in the thesis.

**Opportunity D2: The $23.9B pledged loan figure is a sleeping data point**
FDIC_API_CALL_REPORT_DATA.md notes: pledged loans = $23.9B = 74% of total loans. This is almost the entire loan book pledged as collateral. To whom? FHLB? Fed discount window? Repo counterparties? If OZK has pledged 74% of its loans, that implies they've already tapped significant secured funding. This creates two angles: (a) limited remaining collateral for additional liquidity in a stress event, and (b) depositors have effectively subordinated claims in bankruptcy-adjacent scenarios. Neither has been developed.

**Opportunity D3: NDFI exposure as "shadow CRE lever"**
The $2.74B in loans to non-depository financial institutions is a significant unexploited angle. If these are loans to real estate bridge funds, debt funds, or mezzanine lenders, then OZK has lent to entities that in turn lent to CRE borrowers. When those borrowers default, the fund can't repay OZK. This is a second-order CRE exposure that doesn't show up in the CRE concentration ratios. Combined with the $1.2B to business credit intermediaries and $772M to PE funds (already pulled), OZK may have another $2-3B of shadow CRE exposure. Calculating a "true CRE exposure including NDFI" would be a novel and defensible number that no sell-side analyst has published.

**Opportunity D4: Problem bank comparison**
EVIDENCE.md notes that there are 60 problem banks (FDIC Q4 2025 QBP, +69% from trough). OZK is not on the list. But: OZK's NCO rate (1.18% FY) is nearly 2x the industry average (0.63%), and its ACL/noncurrent coverage (1.39x) has collapsed below levels that typically trigger supervisory attention. The question to research: what are the typical metrics of banks that ARE on the problem list? If OZK's metrics are worse than problem-list banks on several dimensions, that's a powerful framing for the thesis. FDIC publishes aggregated problem bank characteristics.

**Opportunity D5: Dividend sustainability math hasn't been done**
OZK pays $1.56/year. SCENARIOS.md mentions dividend cut risk in passing but doesn't calculate at what EPS level it becomes untenable. OZK's dividend payout ratio at $6.18 EPS is 25% — conservative. But if EPS compresses to $3-4 in the bear case, the payout ratio hits 40-50%. Still technically sustainable. But if charge-offs force provision surge to match losses, earnings could compress to $2-3, pushing payout to 50-75%. The dividend cut question has a specific answer that can be derived from the existing data, and dividend cuts are major catalysts for regional bank repricing.

---

## E. PUBLICATION READINESS

### What Must Be Fixed Before Going Public

**E1: The Temple 8 contamination problem**
The thesis references "Temple 8" multiple times as a source that was later corrected. Temple 8 is never explained — who are they, why were they wrong, and why does this not undermine the overall thesis? A public reader will ask: if your primary data source had a denominator error that inflated CRE/Tier 1 by 97 points (358% → 455%), what else did they get wrong? Either anonymize, identify, or remove all Temple 8 references. Every piece of data should now stand on primary sources (FDIC API, FFIEC CDR, IR supplements, EDGAR) — and those citations should be explicit. Currently some critical numbers still lack in-text source citations.

**E2: EARNINGS_PREP.md must not be published or must be cleaned**
As documented in Section A, this file still contains the debunked 1.16%, <1.0x, and 455% numbers in its peer table. If it ever gets copy-pasted into an external-facing document, it would embarrass the research and give bulls easy ammunition.

**E3: The NCO rate labeling error needs fixing everywhere**
"Q4 2025 NCO rate: 1.18%" appears in THESIS.md, SCENARIOS.md, and the peer comparison. The correct statement is: "FY2025 annualized NCO rate: 1.18%." The Q4-specific annualized rate is 0.64%. This is not a minor quibble — it's the headline number used to make the "8x YoY increase" claim, and the 8x claim needs its own sourcing (what was the 2024 NCO rate? If FY2024 was $57.4M on ~$28B average book = ~0.20%, then FY2025's 1.18% is roughly 6x, not 8x). The 8x claim in THESIS.md has no calculation shown.

**E4: The life sciences "$3.2B exposure" inconsistency**
THESIS.md still opens the life sciences section with "$3.2B exposure" in the headline, then says "$3.1B total commitment" is confirmed. Internally these are two different numbers used for the same item. Pick one (confirmed primary data: $3.1B) and use it consistently.

**E5: Source citations on specific loan details are thin**
- Bioterra $202M: no source
- IQHQ Cole valuation "~$500M": cited as "Cole est." but no link to primary analysis
- "DBRS: 2021-2022 vintages are 63% of CCC-C borrower pool": no link, no date
- "KBRA Negative outlook, CRE 358%, construction 197%": construction figure not reconcilable
- "SD life sciences vacancy 25-29%": two different numbers in the same text (25-29% in THESIS.md, 35% for Sorrento Mesa specifically, and the IQHQ context uses both)

All of these are legitimate — they're just undercited. A publication-ready document needs inline sources for each specific data point.

**E6: The PDNA/NCO gap analysis uses Dallas HQ data, not OZK loan markets**
The "extend-and-pretend gap" table in EVIDENCE.md shows Dallas district having the largest PDNA-NCO gap in the country (1.69pts). This is cited as OZK-relevant. But OZK is headquartered in Dallas and counted in Dallas district statistics, while it LENDS in NY and FL/GA. The Dallas E&P banks suppress the NCO side of that ratio, making the gap look artificially large for OZK's "HQ district." The analysis is correct in identifying that OZK is counted in Dallas stats despite lending elsewhere — but then using Dallas stats as evidence of OZK's extend-and-pretend is circular and logically inverted. This section needs to be rewritten or removed. The NY district (where OZK actually lends) shows a 1.16pt gap — still the second-worst, still compelling, without the methodological error.

**E7: The "97% vacant" IQHQ claim needs a date**
The IQHQ vacancy data comes from sources dated as far back as October 2024. Five months have passed. If IQHQ signed any leases since then (even minor ones), the "97% vacant" claim is stale and potentially wrong. Before publishing, this needs a current date stamp or a fresh search for IQHQ leasing activity.

---

## Summary Scorecard

| Section | Status | Priority |
|---------|--------|----------|
| ACL/coverage analysis | ✅ Solid, minor labeling fixes needed | Low |
| Maturity wall thesis | ✅ Well-supported | Low |
| Interest reserve data | ✅ Primary sourced, strong | Low |
| Memo Item 3 / reclassification | 🟡 Circumstantial, needs C2 addressed | Medium |
| IQHQ | 🟡 Secondary sources only, timeline deferred | Medium |
| NCO rate labeling | 🔴 Wrong label throughout | HIGH |
| EARNINGS_PREP.md Temple 8 data | 🔴 Not updated | HIGH |
| CRE/Tier 1 ratio consistency | 🔴 Three different numbers | HIGH |
| Deposit / liquidity analysis | 🔴 Missing entirely | HIGH |
| NDFI / shadow CRE | 🔴 Unexploited, potentially material | HIGH |
| Life sciences vacancy date | 🟡 May be stale | Medium |
| Publication-level sourcing | 🟡 60% there | Medium |

**Bottom line:** The core thesis is sound and the primary data work done on March 23 (FDIC API + FFIEC CDR) materially strengthens it. But the folder has accumulated internal contradictions from multiple editing passes that need a cleanup sweep, and three specific gaps (deposit composition, NDFI analysis, state-level RC-C) are both obtainable and material. The NCO rate mislabeling and EARNINGS_PREP.md contamination are the highest-priority fixes because they're the most likely to be caught and used against the thesis.

The probability-weighted EV ($38.75 vs $43 current) is the most honest number in the folder. A 10% implied overvaluation is thin for a crowded short (14-15% SI) with 12-18 days to cover. The conviction should be in position sizing relative to the squeeze risk, not in pretending the edge is larger than it is.
