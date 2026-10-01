# SHADE → PROME · 2026-10-01 (touch 2, Will "go for the six" 12:49 ET) · ARI attribution match + L241 DLIC annual

**No trade proposal, no threshold move, no score move.** Detail: `AGENTS/SHADE/research/ARI_ATTRIBUTION_MATCH_2026-10-01.md` · `AGENTS/SHADE/research/DLIC_FY2025_ANNUAL_CHARTER_RATIOS_2026-10-01.md`.

## 1. ARI match — **UNDETERMINED** by the rule I stated before running it
**Rule** (committed `0b2eeb897` at 12:50 ET, before any ARI table was fetched): an AAIA 4/24/2026 row matches an ARI loan if it is in the same city and state/country AND its cost is within ±15% of ARI's balance (AND within ±75bp of the rate where both report one); one-to-one. CONFIRMS at ≥75% of dollars, REFUTES below 25%, otherwise UNDETERMINED.
**Reference:** ARI 10-Q Q1-2026 portfolio table as of 3/31/2026 (**acc 0001193125-26-187094, filed 2026-04-28**; 54 loans, $8,918M amortized); 10-K FY2025 (**acc 0001193125-26-044725, 2026-02-10**; Schedule IV has rates for the top 3 loans); closing 8-K (**acc 0001193125-26-177686, 2026-04-24**: about $8.6B cash at 99.7% of commitment; **no loan list**).
**Result:** **16 of 62 rows, $2,328,729,691 = 31.4%** match against 3/31 (39.1% against 12/31). **What does not match:** ARI lists **16 loans / $3,101M only as "Various"** (no city, so they cannot match by construction); about half the same-city pairs sit at ~80% of ARI's balance, outside the ±15% band; large AAIA rows with no ARI city counterpart ("Delaware" DEU $261.5M, Green Oaks IL $191.7M, El Paso TX $180.0M, …).
**Post-hoc (not the test, labelled):** two **exact-rate** matches on ARI's largest disclosed loans (London office 6.6%, $668.3M · NYC office 3.0%, $269.1M); ARI's Manhattan **three-tranche same-property** loan reproduced at AAIA (three rows on one $1.13B collateral, all at 0.001%: $167.2M vs ARI $163M); and a **bimodal size ratio**: in the 12 cities where the pairing is unambiguous, five at ~1.00 and six at **0.79–0.81**.

**In plain words:** most of ARI's book very likely now sits, legally, at Athene's Iowa insurer, but my pre-registered test cannot certify that, and I am not upgrading it after the fact. 🔑 **New:** the §2.8 "all or any portion" designation appears to have been used as a **pro-rata ~80/20 split** on about half the loans. **The ~20% holder is unidentified**: not AANY (zero Q2 mortgage acquisitions) and not visibly ALRe (mortgage loans +$149M over all of H1). Non-accruing ARI loans (**$265.6M**) were bought at **102–103% of ARI's mark net of its specific CECL** (no discount to ARI's impaired value). **Legal ownership ≠ economics:** AAIA cedes onward to AARe/ACRA by modco/quota share; **leg (b) stands** (AARe's note discloses no allocation).

## 2. L241 — Delaware Life FY2025 annual (DONE in part)
- **Affiliated Reinsurance Ratio 1.62%** ($62,230,134 affiliate reserve credit ÷ C&S $3,838,481,434; FY24 4.15%). **GREEN: the affiliate risk is on the asset side, not in reinsurance.**
- **Illiquidity 9.75% FLOOR** (mortgages + Sch BA $4,475,891,908 ÷ GA $45,903,192,677) **→ ≈37.2% if the $12,619M affiliate-contingent bonds count as "illiquid ABS"**. ⚠️ **That is a definition range. The 30% red flag is NOT recorded as breached; the charter never defined the ABS leg.**
- NAIC SVO override count: **still owed** (not zero).

## COMPLETION — SHADE — 2026-10-01 (touch 2)
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/SHADE/research/{ARI_ATTRIBUTION_MATCH,DLIC_FY2025_ANNUAL_CHARTER_RATIOS}_2026-10-01.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md; PROME/inbox memo
RESULT: ARI match UNDETERMINED by the pre-registered rule: 16/62 rows, $2,328,729,691 = 31.4% vs ARI 3/31 (acc 0001193125-26-187094). Post-hoc: exact-rate and three-tranche matches plus a bimodal ~1.0/~0.8 ratio ⇒ INFERRED ~80/20 §2.8 split on about half the loans; the ~20% holder is unidentified (not AANY, not visibly ALRe). L241: Affiliated Reinsurance 1.62% (green); Illiquidity 9.75% floor / ≈37.2% conditional.
GAPS: ~20% holder not found (ACRA/managed accounts publish nothing loan-level); ARI DEFM14A not read; "illiquid ABS" definition unregistered; SVO count not attempted.
WILL_NEEDS: None now. If PROME wants the Illiquidity Ratio graded against 30%, someone must define the ABS leg; that is a threshold-adjacent ruling for Will.
FOLLOW-UP: Read ARI DEFM14A for a loan annex; AAIA Q3 statutory (~mid-Nov) Schedule B Pt 3 shows any disposals/repayments of the 4/24 loans.
