# Standard Prompt: BLS Employment Situation

Use this prompt template when a new BLS Employment Situation report is released (typically first Friday of the month). Update the date and run through an external LLM.

---

From the [DATE] BLS Employment Situation report (data for [MONTH YEAR]), provide the following exact figures with current value, prior month, year-ago, and MoM/YoY changes:

**Establishment Survey (Table B):**
1. Nonfarm payrolls change (headline NFP, Table B-1 / Summary B)
2. Average weekly hours, total private (Table B-2)
3. Temporary help services employment change (Table B-1, within Professional & Business Services)
4. Average hourly earnings level and YoY % (Table B-3)
5. Notable revisions to prior months

**Household Survey (Table A):**
6. Unemployment rate U-3 (Table A-1)
7. U-6 total underemployment rate (Table A-15)
8. Part-time employed for economic reasons (Table A-8)
9. Long-term unemployed 27+ weeks (Table A-12)
10. Labor force participation rate (Table A-1)
11. Civilian labor force level (Table A-1)
12. Employment-population ratio (Table A-1)
13. Not in labor force, want a job (Table A-1)
14. Discouraged workers (Table A-15)

For each, state the current value, prior month value, year-ago value, and changes. Source all figures to specific BLS table numbers.

---

## Why each item matters (for LABOR agent context):
- Items 1-5: Establishment survey = payroll-based, catches firm-level hiring/firing
- Items 6-9: Household survey = person-based, catches hidden stress (underemployment, duration)
- Items 10-14: Denominator checks — if participation drops, U-6/U-3 can improve mechanically even as conditions worsen. These items detect "improvement via exit" vs genuine improvement.
