# Standard Prompt: BLS Productivity and Costs

Use this prompt template when the BLS Productivity and Costs release is published (quarterly, typically ~5 weeks after quarter end). Update the quarter and date.

---

From the BLS Productivity and Costs release for [QUARTER YEAR] (published [DATE]), provide:

**Nonfarm Business Sector (Table 2):**
1. Labor productivity (output per hour) — annualized quarterly % change for [Q] and prior 3 quarters
2. Unit labor costs — annualized quarterly % change for same quarters
3. Output — annualized quarterly % change for same quarters
4. Hours worked — annualized quarterly % change for same quarters
5. Compensation per hour — annualized quarterly % change for same quarters (real compensation if available)

**Annual and Cycle Context (Table C1):**
6. Full-year productivity growth (annual average and Q4/Q4)
7. Current business cycle productivity rate vs prior cycle and long-term (1947-present) average

**Manufacturing Sector:**
8. Manufacturing labor productivity — quarterly % change
9. Manufacturing unit labor costs — quarterly % change
10. Durable goods manufacturing productivity — quarterly % change
11. Nondurable goods manufacturing productivity — quarterly % change
12. Any BLS commentary contrasting manufacturing with aggregate trends

**Revision Status:**
13. Are current quarter figures preliminary or revised?
14. Were prior quarter figures revised? If so, what drove the revision (hours, output, compensation)?
15. Date of next scheduled revision

Source all figures to specific BLS table numbers from the Productivity and Costs release.

---

## Why each item matters (for LABOR agent context):
- Items 1-5: Core productivity-cost dynamics. When productivity > compensation growth, unit labor costs fall and firms can absorb wage increases without margin pressure. When reversed, margins compress → layoffs accelerate.
- Items 6-7: Cycle context tells us if current productivity is structural (AI/tech adoption) or cyclical (layoff-driven denominator shrinkage).
- Items 8-12: Manufacturing divergence from aggregate is a key thesis input. Manufacturing weakness + rising ULC = stress on industrial borrowers (REGINALD), regional employment (WARN/geographic), and durables demand (auto sector).
- Items 13-15: Preliminary figures are frequently revised. Track revision direction for signal vs noise.

## Verification Protocol:
Run through 2 LLMs minimum. First LLM answer for Q4 2025 had Q1 productivity at -1.5% (actual -0.9%) and Q2 at +3.3% (actual +4.2%). Cross-verify before logging to KB.
