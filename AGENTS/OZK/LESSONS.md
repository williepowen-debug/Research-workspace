# LESSONS.md — OZK Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. This file is for verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data source learnings, see `MEMORY.md` (Feedback + Findings sections). Seeded from REGINALD/LESSONS.md during OZK spinout 2026-04-24: 6 rules copied verbatim, 1 rewritten for OZK (NDFI), 1 skipped (hub-agent-only).*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK — actual was 8.6% per SEC filing. Consumer finance names (SYF, BFH, ALLY) were assumed stressed but SEC filings showed improvement.
**Rule:** Before any metric informs a trade, verify against the 10-K/10-Q. Agent research is a starting point, not ground truth.

### [Data] — OZK CIB/NDFI Is Not Monolithic
**Mistake pattern:** Treating OZK's CIB segment or NDFI exposure as a single risk bucket misses that the sub-segments behave very differently. Fund Finance (capital call subscriptions to PE funds), Lender Finance Group (lending to non-bank lenders), Indirect Lending, and other CIB lines have different collateral, credit, and competitive dynamics.
**Evidence:** Q1 2026 — Jake Munn (CIB President) disclosed OZK is *pulling back* from Fund Finance due to non-bank lender + insurance-company price/structure competition; Lender Finance Group also showing compression. Two of four CIB sub-segments in managed retreat. Meanwhile written Mgmt Comments show Fund Finance growing $210M → $1.275B YoY — no commentary on margin erosion.
**Rule 1:** Decompose OZK CIB/NDFI by sub-segment before assessing risk. Don't treat it as monolithic.
**Rule 2:** Verbal-only disclosures (earnings call transcript) that don't appear in written Mgmt Comments PDFs are the leading signal. Watch for disclosures that vanish between spoken and written form — they're telling you what management doesn't want formalized.

### [Analysis] — Hidden CRE Methodology
**How to screen:** Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = "Loans to finance CRE not secured by RE." Ratio = Memo3/Item4. Flag if >20%.
**Key finding:** OZK worst in screen at 37.6%. WAL ratio is GROWING (15.5% → 24.2%), only bank with upward trend.

### [Analysis] — Distinguish Classification Levels
Three levels of CRE masking:
1. Extend-and-pretend (don't force refinancing)
2. Mark-to-model (don't write down)
3. Classification (call CRE "C&I" if unsecured) ← Memo Item 3
All three can coexist at the same bank. OZK's 37.6% MI3 baseline means classification masking is the primary vector; watch for extend-and-pretend + mark-to-model signals (e.g., foreclosed asset transfers at prior-appraisal values, substandard accrual without specific reserve).

### [Process] — Date Your Data
**Rule:** Every metric must have a date. "Office DQ is 12.34%" means nothing without "as of Jan 2026." Stale data in STATUS.md causes wrong analysis.

### [Process] — STATUS.md Is Not a Research Report
**Rule:** STATUS.md is a dashboard — current state, thresholds, positions. Research detail belongs in archive/, workbook/, or source files. If STATUS.md exceeds 10KB, it needs pruning.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** STATUS.md stated Brent $118-125 and built an entire FL energy shock cascade on that figure. Actual was $81.40. The error propagated through multiple sections before being caught.
**Rule:** Always confirm price levels from a live source before modeling downstream effects. A 45% error on an input produces garbage on all outputs.

---

*Last reviewed: 2026-04-24 (seeded from REGINALD/LESSONS.md during spinout)*
