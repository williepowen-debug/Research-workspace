# LV-03: Conversion Velocity — Time from Trigger to Default

**Research Thread:** Latent Vulnerability
**Priority:** HIGH
**Created:** 2026-01-24
**Session:** CARL 008
**Expected Output:** `research/outputs/LV-03_RESULTS.md`

---

## Context

Traditional credit risk models assume 6-12 months from financial stress to visible delinquency. However, recent data shows 37% of Americans can't cover a $400 emergency and 62% live paycheck-to-paycheck. For this population, the lag between trigger event and missed payment may be much shorter — potentially 0-3 months.

Understanding "conversion velocity" is critical for predicting when latent vulnerability converts to visible stress in credit metrics.

---

## Prompt

I'm researching how quickly financial trigger events convert to visible delinquency (missed payments, collections, default), particularly for households with limited financial buffers.

## PART A: JOB LOSS TO DELINQUENCY

1. **Time to first missed payment after job loss:**
   - What's the median time from job loss to first missed bill payment?
   - How does this vary by savings level? Specifically:
     - Households with <$1,000 liquid savings
     - Households with $1,000-$5,000
     - Households with >$10,000
   - How does this vary by income level?

2. **Historical compression:**
   - Has the job-loss-to-delinquency lag shortened over time?
   - Compare 2008-2010 recession vs. 2020 pandemic vs. current (2024-2025)
   - What factors explain any compression (lower savings rates, higher fixed costs, gig work prevalence)?

3. **Unemployment duration thresholds:**
   - At what duration of unemployment do delinquency rates spike?
   - Is there a "cliff" (e.g., after 4 weeks, 8 weeks, 12 weeks)?

## PART B: MEDICAL EVENT TO DELINQUENCY

1. **Time from medical event to first missed payment:**
   - For uninsured patients with a major medical event (hospitalization, surgery, serious diagnosis), how quickly do they miss payments on other bills?
   - For underinsured patients (high deductible plans), what's the lag?
   - For adequately insured patients, what's the lag?

2. **Medical debt timeline:**
   - How long from medical service to first bill?
   - How long from first bill to collections referral?
   - How long from collections to credit report impact?
   - What's the total timeline from "got sick" to "credit damaged"?

3. **Spillover effects:**
   - When medical debt accumulates, how quickly do people start missing payments on OTHER bills (rent, utilities, credit cards)?
   - Is there a prioritization pattern (which bills get skipped first)?

## PART C: GENERAL CONVERSION DYNAMICS

1. **Buffer duration research:**
   - Studies on how long households can maintain expenses after income loss
   - JPMorgan Chase Institute "cash buffer days" — what are the current figures by income quintile?
   - Has buffer duration decreased over the past decade?

2. **The "cascade timeline":**
   - Once first payment is missed, how quickly do subsequent delinquencies occur?
   - Is there a typical sequence (utilities first, then credit cards, then rent/mortgage)?
   - How long from first 30-day late to 90-day late to charge-off?

3. **Velocity by trigger type:**
   - Rank these triggers by speed of conversion to delinquency:
     - Job loss
     - Medical event
     - Auto accident (with liability)
     - Divorce/separation
     - Natural disaster
   - Which triggers have the shortest lag? Which have the longest?

## PART D: IMPLICATIONS FOR FORECASTING

1. **Model assumptions:**
   - What lag assumptions do standard credit risk models use?
   - Are these assumptions still valid given current savings rates?
   - Have any institutions (Fed, banks, credit bureaus) updated their lag assumptions?

2. **Leading indicators:**
   - What behavioral signals appear BEFORE the first missed payment?
   - How much advance warning do these signals provide?
   - Are there studies on "early warning" indicators that predict delinquency 30-60-90 days out?

---

Please cite sources for all statistics. Academic studies, Federal Reserve research, JPMorgan Chase Institute, credit bureau studies, and bank research preferred. Most recent data (2022-2026) preferred, but historical comparisons valuable for trend analysis.
