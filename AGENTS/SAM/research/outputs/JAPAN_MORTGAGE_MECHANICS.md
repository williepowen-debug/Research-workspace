# Japan Floating Rate Mortgage Mechanics — Research Package

**Date:** 2026-04-07
**Author:** SAM
**Classification:** Research — BOJ Political Constraint / EWJ Trade Foundation
**Confidence:** HIGH (mechanics verified from BOJ, FSA, NRI, multiple sources)

---

## EXECUTIVE SUMMARY

75-80% of Japanese mortgages are floating rate (¥180T of ¥227T outstanding), linked to the short-term prime rate (currently 2.125%). Rate hikes transmit with a 3-7 month lag due to semi-annual review dates. The 5-year rule and 125% rule mask payment shock — borrowers don't feel rate increases for up to 5 years, but silently accumulate negative amortization. This creates a delayed-fuse problem invisible in current delinquency data.

**Punchline:** Takaichi's 0.75% ceiling is driven by FEAR of future household stress, not visible current stress. The damage from hikes already done won't show up in data until 2027-2028.

---

## 1. MECHANICAL TRANSMISSION

### Rate Linkage
- Floating mortgages linked to **short-term prime rate** (tanki prime rate), NOT directly to BOJ policy rate
- Current short-term prime rate: **2.125%** (Feb 2026, up from 1.625% pre-hike cycle)
- Banks set mortgage rate = prime rate minus discount (~1.0-1.2%), so actual rates ~**0.85-1.00%+**
- As of **April 1, 2026**, several major banks lifted posted floating rates above 1.00% for first time

### Transmission Timing
- Rate reviews: **semi-annual** on April 1 and October 1
- New rate applies to payments ~3 months later
- BOJ's December 2025 hike (to 0.75%) → Apr 1 review → **July 2026 payment cycle**
- **Total lag: ~3-7 months from BOJ decision to borrower payment change**

### The 5-Year Rule (5-nen rule)
- Monthly payment amount **stays fixed for 5 years** regardless of rate changes
- When rates rise, payment composition shifts: more to interest, less to principal
- Borrower sees **no change** in monthly outlay
- Risk: if rates rise enough, payment may not cover interest → **negative amortization** (principal grows)

### The 125% Rule
- At 5-year reset, new payment **capped at 125% of prior payment**
- Maximum payment shock = 25% every 5 years
- Any unpaid interest deferred → added to principal balance

### The Hidden Trap
These rules **defer pain, not eliminate it.** A borrower whose rate doubled may:
- Not notice for 5 years (5-year rule)
- Face only 25% increase at reset (125% rule)
- But owe significantly MORE principal than originally expected
- Balloon payment risk at maturity or on sale

---

## 2. PAYMENT IMPACT MODELING

### Published Estimates

| Source | Finding |
|--------|---------|
| Nikkei Asia | BOJ's two hikes add ~¥8,000/month ($51) to average mortgage |
| BOJ/Japan Times | Per 25bp hike: deposit income +¥13K, mortgage cost +¥28K = net -¥15K/year for avg household |
| BOJ/Japan Times | For households in 20s-30s: net impact **-¥47,000/year per 25bp hike** |
| Mizuho Research | Total household mortgage cost increase from 0.50% hike: **¥0.4T/year** across all households |
| Meyka (Apr 2026) | ¥35M mortgage, 1.00%→1.25%: +¥4,100/month (~¥49,000/year) |

### Payment Table (35-year term, standard amortization, WITHOUT 5-year rule)

| Rate Scenario | ¥30M mortgage | ¥35M mortgage | ¥40M mortgage |
|---------------|--------------|--------------|--------------|
| Pre-hike (0.35%) | ¥75,903/mo | ¥88,554/mo | ¥101,204/mo |
| Current (~1.00%) | ¥84,686/mo | ¥98,800/mo | ¥112,914/mo |
| BOJ at 1.00% (mort ~1.25%) | ¥88,226/mo | ¥102,930/mo | ¥117,635/mo |
| BOJ at 1.50% (mort ~1.75%) | ¥95,573/mo | ¥111,502/mo | ¥127,431/mo |

### Total Interest Over Life of ¥30M Loan
- At 0.35%: ¥1.88M
- At 1.00%: ¥5.57M (3x more)
- At 1.75%: ¥10.14M (5.4x more)

---

## 3. DELINQUENCY DATA — WHAT EXISTS (AND DOESN'T)

### Available
| Metric | Value | Date |
|--------|-------|------|
| Bank NPL ratio (all loans) | ~1.0% | Sep 2025 |
| Total problem loans (FRA) | ¥9.6T | Mar 2024 |
| Historical peak NPL | 8.4% | 2002 |
| Real estate loan NPL trend | "Low level, declining" | FSA |

### NOT Available (Critical Gap)
- **No mortgage-specific delinquency rate** published (no equivalent to US MBA National Delinquency Survey)
- **No published household debt service ratio** (no equivalent to US Fed DSR ~10%)
- **No breakdown of how many households have DSR >30% or 40%**
- **No published estimate of household defaults under 1.0% or 1.25% policy rate scenarios**

### FSA Study (Oct 2025) — Internal Data Only
- "Analysis of Defaults in Housing Loans by Regional Banks" using granular loan data
- Found: **higher interest rate levels associated with higher default rates**
- Regional variation significant (higher DQ in Hokkaido/Tohoku)
- Summary statistics NOT published

---

## 4. HOUSEHOLD FINANCIAL POSITION

| Metric | Value |
|--------|-------|
| Household debt | ¥402T (record, Q4 2025) |
| Household financial assets | ¥2,286T (record, Sep 2025) |
| Assets/Debt ratio | **5.7x** — massive net creditor |
| Household debt/GDP | ~64.4% (moderate by intl standards) |
| Floating rate mortgage exposure | ~¥180T (80% of ¥227T) |
| New borrowers choosing variable | **79.0%** (Apr 2025, still growing) |

### The Aggregation Fallacy
- Assets concentrated among **elderly savers**
- Debt concentrated among **younger working-age households**
- BOJ acknowledges "considerable heterogeneity" but frames it optimistically
- OECD flagged Japan specifically for "high share of floating-rate housing loans" as vulnerability

---

## 5. POLITICAL CONTEXT

| Actor | Position |
|-------|----------|
| Takaichi (PM) | Vocal critic of higher rates. Drew explicit 0.75% line. |
| Honda (adviser) | Expects hike but "March/April too early" (Feb 2026) |
| Takaichi | Expressed reservations in private meeting with Ueda |
| Yoshimura (coalition) | "Buffer" defending BOJ independence — internal tension |
| BOJ | Held at 0.75% in Jan ahead of snap election — political timing |
| Ueda | Wants 1.0%+ for inflation credibility but constrained |

---

## 6. IMPLICATIONS FOR SAM THESIS

### FXY Position (near-term, 3-6 months)
- The 0.75% ceiling thesis is **STRONG** — Takaichi constraint is real
- But ceiling applies to hikes BEYOND 0.75%, not to the 0.75% hike itself
- Next hike (to 0.75%) has political cover — Takaichi's line allows it
- The hike to 1.00% is where political collision fires → D2 scenario

### EWJ Put Trade (longer-dated, 12-18 months)
- BOJ hike to 1.00% is the trigger (May 1 base case, if April doesn't deliver)
- But mortgage stress won't show in DATA for 5+ years (5-year rule)
- The trade needs to be based on **sentiment/fear** not actual delinquency data
- Trigger is: BOJ hikes → media coverage of mortgage impact → consumer confidence drops → consumption weakens → Nikkei falls
- This is a **narrative trade**, not a data trade

### Key Insight
The 5-year rule means Japan's mortgage stress is a **slow bomb, not a fast one**. The damage from current hikes is invisible now and will compound silently until 2027-2028 resets. Takaichi is fighting to prevent a problem that won't be visible for years — which makes her position politically strong (can claim prevention) but economically questionable (the damage is already being done beneath the surface).

---

## SOURCES

- [Nikkei Asia: BOJ rate hikes add $50 to average mortgage](https://asia.nikkei.com/economy/bank-of-japan/boj-rate-hikes-add-50-to-japan-s-average-monthly-mortgage-payment)
- [Japan Times: BOJ rate hike could be both good and bad for households](https://www.japantimes.co.jp/business/2025/12/20/economy/boj-rate-impact-households/)
- [Real Estate Japan: Beware the 5-Year Rule](https://resources.realestate.co.jp/buy/getting-a-variable-rate-home-loan-in-japan-beware-the-5-year-rule/)
- [Mizuho Research: Impact of BOJ additional rate hike](https://www.mizuhogroup.com/binaries/content/assets/pdf/information-and-research/insights/mhri/en-br250121.pdf)
- [Meyka: Japan mortgage rates top 1% on April 1](https://meyka.com/blog/japan-mortgage-rates-top-1-on-april-1-as-banks-lift-floating-loans-3103/)
- [BOJ Financial System Report (Oct 2025)](https://www.boj.or.jp/en/research/brp/fsr/fsr251023.htm)
- [FSA: Defaults in Housing Loans by Regional Banks (Oct 2025)](https://www.fsa.go.jp/en/about/fsaanalyticalnotes/20251010/01.pdf)
- [NRI: Rate hikes pose more risk to Japan mortgage borrowers than US](https://www.nri.com/en/knowledge/publication/fis/lakyara/lst/2023/08/01)
- [Japan Times: Takaichi expecting additional BOJ rate hike](https://www.japantimes.co.jp/business/2026/02/14/economy/takaichi-boj-rate-hike/)
- [JHF Survey: Most homebuyers still choosing variable rate](https://www.patiencerealty.com/post/survey-says-most-japanese-homebuyers-still-choosing-variable-rate-mortgages)

---

*Filed: AGENTS/SAM/research/outputs/JAPAN_MORTGAGE_MECHANICS.md*
