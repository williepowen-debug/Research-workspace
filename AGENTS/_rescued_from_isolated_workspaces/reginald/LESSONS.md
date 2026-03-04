# LESSONS.md — REGINALD Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever.*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK — actual was 8.6% per SEC filing. Consumer finance names (SYF, BFH, ALLY) were assumed stressed but SEC filings showed improvement.
**Rule:** Before any metric informs a trade, verify against the 10-K/10-Q. Agent research is a starting point, not ground truth.

### [Data] — NDFI Is Not What It Looks Like
**Mistake:** WAL's NDFI ($6.5B) was initially flagged as major risk. Reality: 68% is mortgage warehouse (0.08% reserves, near-zero losses), NO auto warehouse. Ex-mortgage only $4.3B in secured SPV structures.
**Rule:** Decompose NDFI by type before assessing risk. Mortgage warehouse ≠ auto subprime ≠ BDC lending.

### [Analysis] — Hidden CRE Methodology
**How to screen:** Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = "Loans to finance CRE not secured by RE." Ratio = Memo3/Item4. Flag if >20%.
**Key finding:** WAL ratio is GROWING (15.5% → 24.2%), only bank with upward trend. OZK worst at 37.6%.

### [Analysis] — Distinguish Classification Levels
Three levels of CRE masking:
1. Extend-and-pretend (don't force refinancing)
2. Mark-to-model (don't write down)
3. Classification (call CRE "C&I" if unsecured) ← Memo Item 3
All three can coexist at the same bank. WAL uses all three.

### [Process] — Date Your Data
**Rule:** Every metric must have a date. "Office DQ is 12.34%" means nothing without "as of Jan 2026." Stale data in STATUS.md causes wrong analysis.

### [Process] — STATUS.md Is Not a Research Report
**Rule:** STATUS.md is a dashboard — current state, thresholds, positions. Research detail belongs in archive/, workbook/, or source files. If STATUS.md exceeds 10KB, it needs pruning.

---

*Last reviewed: 2026-02-27*
