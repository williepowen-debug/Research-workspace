# D5: Dividend Sustainability Analysis

**Created:** 2026-03-24
**Sources:** OZK Q4 2025 Management Comments, FDIC API, C3 Capital Absorption Analysis
**Status:** COMPLETE

---

## Current Dividend Profile

| Metric | Value | Source |
|--------|------:|--------|
| Annual dividend | **$1.56/share** | IR page |
| Quarterly dividend | $0.39/share | |
| FY 2025 EPS | $6.18 | Mgmt Comments |
| **Payout ratio** | **25.2%** | $1.56 / $6.18 |
| Consecutive quarterly increases | **62 quarters** (~15.5 years) | Management highlights this constantly |
| Shares outstanding | ~113M | |
| Annual dividend cost | **~$176M** | |
| Dividend streak narrative | Core to OZK investor identity | Bulls cite this as "management commitment" |

At 25% payout, the dividend looks impregnable. That's the bull case. But payout ratios are backward-looking — they reflect last year's earnings, not next year's provisions.

---

## EPS Compression Scenarios → Payout Ratio Impact

| Scenario | EPS | Payout Ratio | Sustainable? | Notes |
|----------|:---:|:------------:|:------------:|-------|
| **FY 2025 actual** | $6.18 | 25% | ✅ | Status quo |
| Base: moderate provision surge | $5.00 | 31% | ✅ | Manageable — no cut needed |
| Bear: NCO doubles + provision catch-up | $4.00 | 39% | ✅ | Still comfortable but boards get nervous |
| Severe bear: sustained 2% NCO | $3.00 | 52% | 🟡 | Payout >50% = dividend growth stops |
| Tail: 2.5% NCO + provision surge | $2.00 | 78% | 🔴 | Board must choose: cut div or erode capital |
| Extreme: 3% NCO (breakeven) | $0-1.00 | 156-∞% | 🔴 | **Dividend cut forced** |

---

## When Does the Board Face a Decision?

### The 50% Payout Threshold
Bank regulators don't mandate dividend cuts, but they scrutinize payout ratios above 50% — especially at banks under enhanced CRE supervision (which OZK almost certainly is, given 358%+ CRE/Tier 1). The informal guidance:
- **<30%:** No issues
- **30-50%:** Acceptable if capital trends positive
- **>50%:** Expect regulatory questions
- **>75%:** Expect regulatory pressure to cut or suspend
- **>100%:** Paying out more than you earn — capital erosion

### The Capital Buffer Math
OZK has ~$2.3B in capital above regulatory minimums. Annual dividend costs $176M. In isolation, OZK could pay the dividend for **13 years** before hitting capital minimums — even with zero earnings.

But dividends don't exist in isolation. They compete with:
- **Provisions** — if NCOs spike, provisions must rise to rebuild ACL
- **Loan growth** — new loans require risk-weighted capital
- **Regulatory expectations** — maintaining CET1 above peer averages during stress

### The Decision Framework

The board won't cut proactively. They'll cut when **one of three things happens:**

| Trigger | EPS Threshold | Probability by Q4 2026 |
|---------|:------------:|:----------------------:|
| **Payout ratio crosses 50%** | EPS < $3.12 | 20% |
| **Regulatory MRA citing capital preservation** | Any EPS + rising NCOs | 10% |
| **ACL depleted below 1.0x noncurrent** | Coverage < 100% | 15% |

**Combined probability of dividend cut within 12 months: ~20-25%**

---

## Why Dividend Cuts Are Catalysts for Regional Banks

### The Mechanical Selloff
OZK's 62-quarter dividend streak is central to its investor narrative. A significant percentage of OZK holders are:
- **Dividend-focused retail investors** — bought for yield and "management quality"
- **Dividend ETFs** — mechanical rebalancing on cut announcement
- **Income funds** — mandate requires minimum yield; cut = forced sell

A dividend cut doesn't just reduce the cash flow — it **destroys the narrative**. The stock reprices on two axes simultaneously:
1. Lower earnings → lower multiple
2. Lost dividend premium → multiple compression

### Historical Precedents

| Bank | Div Cut Date | Stock Impact | Context |
|------|:-----------:|:------------:|---------|
| **NYCB/FLG** | Jan 2024 | **-38% in 1 day** | Surprise 70% cut + provision surge |
| **Zions (ZION)** | 2020 | -25% in week | COVID precautionary |
| **KeyCorp** | 2020 | -15% on announcement | Even partial cuts punished |
| **SVB** | N/A (failed) | — | Never cut — went from paying div to FDIC receivership |

The NYCB template is the most relevant: surprise provision surge → dividend cut → algorithmic selloff → depositor concern → spiral. OZK's setup is similar (CRE concentrated, provisions lagging losses).

---

## The Dividend Cut Scenario for OZK

### Path to Cut (12-18 months)
1. **Q1 2026 earnings (Apr 16):** NCOs spike as construction loans mature into frozen refi market
2. **Q2 2026:** Provision surge to rebuild ACL. EPS drops to $4.00-4.50
3. **Q3 2026:** Second consecutive EPS miss. Payout ratio approaches 40%
4. **Q4 2026:** Board faces choice — maintain streak or preserve capital. If NCO rate hits 2%+, the math forces the cut.

### What a Cut Would Look Like
- **50% cut** ($1.56 → $0.78): Saves $88M/year. Signals stress but not desperation.
- **Full suspension**: Saves $176M/year. Nuclear option — signals serious trouble.

### Stock Impact of a 50% Cut
Current: ~$43, ~$6.18 EPS, ~7x P/E
Post-cut scenario: ~$4.00 EPS, 5-6x P/E (stress multiple) = **$20-24**

That's the tail case, not the base case. But a dividend cut is the mechanism that takes a $38-40 stock (base case) down to $20-25 (tail).

---

## Position Sizing Implication

The dividend is **not the thesis** — it's the **amplifier**. The thesis is earnings compression via provision surge. The dividend cut is what converts a 10-15% decline (earnings miss) into a 30-50% decline (narrative destruction + forced selling).

**Aug $45 put captures both scenarios:**
- Base (no cut, EPS compression): stock to $38-40, put worth $5-7
- Bear (cut): stock to $25-30, put worth $15-20

The dividend streak is the grenade pin. We don't need it to pull for the trade to work — but if it does, the payoff multiplies.

---

## Cross-References
- C3 Capital Absorption: `research/C3_CAPITAL_ABSORPTION_ANALYSIS.md` (EPS sensitivity table)
- D4 Problem Bank: `research/D4_PROBLEM_BANK_COMPARISON.md` (NCO breakeven analysis)
- SCENARIOS.md: Bear/tail case probability weights
- EARNINGS_PREP.md: Apr 16 catalyst setup
