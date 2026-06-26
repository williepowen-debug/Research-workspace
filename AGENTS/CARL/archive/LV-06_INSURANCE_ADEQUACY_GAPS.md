# LV-06: Insurance Adequacy Gaps — Quantifying the Protection Deficit

**Research Thread:** Latent Vulnerability
**Priority:** MEDIUM
**Created:** 2026-01-24
**Session:** CARL 008
**Expected Output:** `research/outputs/LV-06_RESULTS.md`

---

## Context

We know 23% of Americans are "underinsured" (Commonwealth Fund definition: OOP costs ≥10% of income or deductible ≥5% of income). But this binary classification doesn't tell us the SIZE of the gap between coverage and exposure.

If the average underinsured person has a $3,000 deductible and $2,500 in savings, the gap is $500 (manageable). If they have an $8,000 deductible and $400 in savings, the gap is $7,600 (catastrophic).

Additionally, employer-provided insurance has been degrading (rising deductibles, higher cost-sharing). Understanding the trajectory helps predict how fast the underinsured population is growing.

---

## Prompt

I'm researching the actual dollar gap between insurance coverage and financial exposure for American households, plus the trajectory of employer insurance degradation over time.

## PART A: THE COVERAGE-TO-EXPOSURE GAP (Health Insurance)

1. **Deductible levels:**
   - What's the current average/median deductible for:
     - Employer-sponsored plans
     - ACA marketplace plans (by metal tier: Bronze, Silver, Gold)
     - High-deductible health plans (HDHPs)
   - Distribution: What percentage of insured have deductibles of $1K, $2K, $3K, $5K, $8K+?

2. **Out-of-pocket maximums:**
   - Current average/median OOP max by plan type
   - What percentage of people hit their OOP max annually?
   - When they hit it, what's the average total OOP spending?

3. **Liquid savings by insurance status:**
   - For people with different deductible levels, what are their average liquid savings?
   - Cross-tabulate: Deductible level × Savings level → What percentage have savings < deductible?
   - This is the "gap population" — insured but unable to meet deductible

4. **The actual gap calculation:**
   - For the underinsured population:
     - Average deductible: $___
     - Average liquid savings: $___
     - Average gap: $___
   - What's the distribution? (Some gaps small, some catastrophic)
   - Total aggregate gap across all underinsured Americans: $___B

5. **Coinsurance exposure:**
   - After deductible, what's typical coinsurance (20%? 30%?)
   - For a $100K medical event with 20% coinsurance and $8K OOP max:
     - Insured pays: $8K
     - If savings = $400, gap = $7.6K
   - What percentage of underinsured would face this scenario?

## PART B: AUTO INSURANCE ADEQUACY

1. **Liability limit adequacy:**
   - What are common state minimum liability limits?
   - What's the average cost of a serious injury accident?
   - What percentage of drivers carry only state minimums?
   - What percentage of accidents result in damages exceeding policy limits?

2. **The underinsured motorist problem:**
   - Different from uninsured (15.4%) — what percentage are underinsured?
   - What's the average gap between liability limit and potential exposure?
   - Geographic variation (which states have lowest limits + highest accident costs)?

3. **Comprehensive/collision gaps:**
   - What percentage of drivers have comprehensive/collision coverage?
   - For those without, what's the average vehicle value at risk?
   - Correlation with income/savings levels

## PART C: HOMEOWNER/RENTER INSURANCE GAPS

1. **Replacement cost underinsurance:**
   - What percentage of homeowners are underinsured relative to replacement cost?
   - By how much on average? (The "60% underinsured by 20-25%" stat needs validation)
   - Has this gap widened with construction cost inflation?

2. **Renter insurance gaps:**
   - What percentage of renters have renter's insurance?
   - For those without, what's the average value of possessions at risk?
   - What's the typical renter's insurance deductible vs. renter savings?

3. **Disaster-specific coverage gaps:**
   - Flood insurance: 30% take-up in flood zones — what's the dollar exposure for the 70%?
   - Earthquake insurance: ~10% in CA — dollar exposure for the 90%?
   - Wildfire: What's the gap between FAIR Plan coverage limits and actual property values?

## PART D: EMPLOYER INSURANCE DEGRADATION TRAJECTORY

1. **Deductible trend:**
   - Average employer plan deductible: 2010 vs. 2015 vs. 2020 vs. 2024
   - Annual rate of increase
   - Is the rate accelerating?

2. **Cost-sharing shift:**
   - Employee premium contribution: trend over time
   - Employer vs. employee share of total premium: trend
   - Coinsurance and copay trends

3. **Plan design changes:**
   - Shift from PPO to HDHP: trend over time
   - What percentage of employer plans are now HDHPs?
   - Prevalence of HSA-eligible plans (and actual HSA funding levels)

4. **Coverage erosion:**
   - Are more services being excluded from coverage?
   - Prior authorization requirements: trend
   - Network narrowing: trend
   - Any quantification of "coverage that looks good on paper but doesn't pay"?

5. **Projection:**
   - If current trends continue, what will average deductible be in 2028? 2030?
   - At what point does employer insurance become functionally "underinsurance" for median worker?

## PART E: THE AGGREGATE PROTECTION DEFICIT

1. **Total exposure calculation:**
   - Sum across all categories:
     - Health insurance gap: $___B
     - Auto insurance gap: $___B
     - Property insurance gap: $___B
   - Total protection deficit for American households: $___B (or $___T)

2. **Comparison to buffers:**
   - Total liquid savings of underinsured/underinsured population: $___B
   - Ratio: Exposure / Savings = ___x
   - This ratio indicates how many "incidents" worth of exposure exists relative to ability to pay

---

Please cite sources. KFF Employer Health Benefits Survey, Commonwealth Fund, Insurance Information Institute, NAIC, Federal Reserve SCF, and academic studies are all valuable. Looking for both current snapshot and historical trends.
