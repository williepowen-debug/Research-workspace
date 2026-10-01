# SHADE — ARI attribution match: AAIA 4/24/2026 loans vs ARI's own loan tables · 2026-10-01

**Task:** PROME touch 2 (`prome-0c`, Will "go for the six" 12:49 ET). **Rails:** no trade proposal, no threshold move.

## 0. MATCH RULE — PRE-REGISTERED (written and committed BEFORE any ARI table was fetched or read)

**Population (A):** every AAIA Q2-2026 statutory Schedule B Part 2 row with Date Acquired = **04/24/2026** in the commercial (0499999) or mezzanine (0699999) subsections, i.e. the 62 rows totalling **$7,405,267,470** (actual cost at acquisition). Fields available: loan number (Athene's own), city, state/country, rate, actual cost, value of land and buildings. **No borrower name, no property type, no maturity** in Part 2.

**Reference (R):** ARI's own loan-level disclosure from its latest periodic filings before the sale closed (10-K FY2025, 10-Q Q1-2026 if it lists loans) and the sale proxy/8-K, from SEC EDGAR, each with accession number and date.

**A loan a ∈ A MATCHES an ARI loan r ∈ R iff ALL of:**
1. **LOCATION:** same city (or the borough/metro ARI names, e.g. "Manhattan" ↔ NEW YORK) AND same US state or same country.
2. **SIZE:** a's actual cost is within **±15%** of r's carrying value / amortized cost / principal at the most recent ARI report date, **or** within ±15% of r's funded balance where ARI reports commitment and unfunded separately. (Partial-funding and FX moves since the report date are the reason for the band.)
3. **RATE (only where both sides report one):** a's rate within **±75bp** of r's coupon or all-in rate. Where one side lacks a rate, condition 3 is skipped and the match is labelled SIZE+LOCATION only.

**Assignment:** one-to-one. If several ARI loans satisfy 1–2 for one AAIA row (or vice versa), assign by smallest absolute size gap; ties stay AMBIGUOUS.
**Labels:** **MATCH** (1+2+3, or 1+2 where 3 unavailable) · **LOCATION-ONLY** (1 met, 2 failed) · **UNMATCHED**.
**Verdict rule (fixed now):**
- **CONFIRMS** "these are the ARI loans" if **≥75% of A's dollars** are MATCH **and** no AAIA 4/24 row ≥ $100M is UNMATCHED without an explanation from the ARI side (e.g. a loan ARI says was excluded).
- **REFUTES** if **<25% of A's dollars** are MATCH (location+size coincidence would be expected to give few matches if the loans came from elsewhere).
- **UNDETERMINED** otherwise, or if ARI's tables do not disclose loans at a granularity that permits rule 1 for most of the book.

**Known limits stated in advance:** location+size cannot prove identity (a coincidental same-city, same-size loan from another seller would MATCH); conversely, ARI loans restructured, paid down or split between report date and 4/24 can fail rule 2 while being the same loan. Neither side reports borrower names in this pairing.
