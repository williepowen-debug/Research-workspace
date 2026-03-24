# C3: Capital Absorption & Position Sizing Analysis
**Created:** 2026-03-24

---

## The Bull Argument
OZK has CET1 of 11.70% — 520bps above the 6.50% well-capitalized minimum. That's ~$2.3B in loss absorption before regulatory action. The thesis is about stock repricing, not bank failure. With 14-15% short interest and only 10% EV edge ($38.75 vs $43), the risk/reward is thin for a crowded short.

## Capital Absorption Math

### How Much Can OZK Lose Before Capital Triggers?

| Metric | Current | Well-Capitalized Min | Buffer | $ Buffer |
|--------|---------|---------------------|--------|----------|
| CET1 | 11.70% | 6.50% | 5.20% | ~$2,310M |
| Tier 1 | 12.50% | 8.00% | 4.50% | ~$2,000M |
| Total RBC | 14.80% | 10.00% | 4.80% | ~$2,130M |
| Tier 1 Leverage | 13.60% | 5.00% | 8.60% | ~$3,500M |

**Binding constraint: Tier 1 at 8.00% = ~$2,000M buffer.**

But that's the *regulatory* floor. The *market* reacts much earlier:

| CET1 Level | What Happens | Implied Loss to Get There |
|------------|-------------|--------------------------|
| 11.70% | Current — stock at ~$43 | — |
| 10.00% | KBRA downgrade territory. Analyst concern. Stock reprices. | ~$755M |
| 9.00% | Possible MOU discussions. Dividend at risk. Serious repricing. | ~$1,200M |
| 8.00% | Supervisory attention certain. Capital raise likely. | ~$1,645M |
| 6.50% | Well-capitalized floor breached. FDIC intervention. | ~$2,310M |

**The stock doesn't wait for 6.50%. It reprices at 10.00% or below.** The market threshold for OZK (a CRE-concentrated bank under KBRA Negative outlook) is probably ~9.5-10.0% CET1.

### What Drives CET1 Erosion?

CET1 erodes through: (a) charge-offs in excess of provision, and (b) provision expense reducing earnings below dividend payouts.

**Current run rate:**
- Quarterly gross charge-offs: $98.3M (Q4, from mgmt)
- Quarterly provision: $50.6M (Q4)
- Gap: **$47.7M per quarter consumed from capital** (net of provision)
- Annual earnings: ~$680M ($6.18 EPS × 110.4M shares)
- Annual dividend: ~$172M ($1.56/share × 110.4M shares)
- Retained earnings (pre-provision): ~$508M

So even at Q4 run rates, OZK earns enough to offset the provision gap. That's the bull case for capital — the bank is profitable enough to self-fund credit losses *at current rates*.

### When Does It Break?

It breaks when charge-offs overwhelm earnings:

| Scenario | Annual NCOs | Annual Provision | Earnings After Prov | After Dividend | CET1 Impact |
|----------|------------|-----------------|-------------------|---------------|-------------|
| **Current Q4 run rate** | $393M (Q4×4) | $200M | $487M | +$315M | CET1 RISES |
| **Bear: NCOs double** | $600M | $400M | $280M | +$108M | CET1 flat |
| **Severe: NCOs triple** | $900M | $700M | -$20M | -$192M | CET1 falls ~45bps/yr |
| **Crisis: IQHQ + wave** | $1,200M | $1,000M | -$320M | -$492M | CET1 falls ~110bps/yr |

**At current run rates, OZK's capital GROWS.** This is the uncomfortable truth for the bear case.

To get CET1 to fall meaningfully, you need charge-offs to roughly triple from current levels. That requires the maturity wall to deliver a step-change in losses, not a continuation of the current trajectory.

### The Reframe: This Is NOT a Bank Failure Trade

The thesis is about **earnings compression → multiple compression → stock repricing**. Not about capital depletion.

Here's the actual transmission:
1. Noncurrent keeps rising (maturity wall, interest reserve depletion)
2. Management forced to increase provisions to match (can't keep cutting ACL)
3. Provision surge compresses EPS: $6.18 → $4.00-5.00 (bear) or $2.00-3.00 (severe)
4. Market re-rates from "growth bank" (10-12x P/E) to "stressed CRE bank" (6-8x P/E)
5. Stock reprices to $24-40 depending on severity

**Capital is fine. Earnings are the vulnerability.**

| EPS Scenario | P/E Multiple | Stock Price | Downside from $43 |
|-------------|-------------|-------------|-------------------|
| $6.18 (current) | 7x (current) | $43 | — |
| $5.00 (provision up) | 7x | $35 | -19% |
| $5.00 (provision up) | 6x (stressed) | $30 | -30% |
| $4.00 (bear) | 6x | $24 | -44% |
| $3.00 (severe) | 5x | $15 | -65% |

The stock currently trades at ~7x earnings. If EPS compresses to $5.00 and the multiple holds, that's $35. If the multiple also compresses (which it will — stressed CRE banks don't hold 7x), you get to $30.

---

## Position Sizing: Put-Specific Risk/Reward

### Aug $45 Put

| Scenario | Prob | Stock Price | Intrinsic | Weighted |
|----------|------|-------------|-----------|----------|
| Bear ($33.50) | 50% | $33.50 | $11.50 | $5.75 |
| Base ($41.00) | 30% | $41.00 | $4.00 | $1.20 |
| Bull ($57.50) | 15% | $57.50 | $0.00 | $0.00 |
| Tail ($21.50) | 5% | $21.50 | $23.50 | $1.18 |
| **EV** | | | | **$8.13** |

If the put costs ~$3-4, the expected return is **~2-2.7x** on a probability-weighted basis. That's a positive EV trade even accounting for the 15% bull/squeeze scenario where it goes to zero.

**Max pain scenario:** Stock squeezes to $55 in May/June on a positive headline (strong Q1 earnings, IQHQ tenant announcement). Put temporarily marks to near-zero. If you can hold through the squeeze, the maturity wall still arrives Q2-Q3.

### May $42.5 Put

| Scenario | Prob | Stock at May Exp | Intrinsic | Weighted |
|----------|------|-----------------|-----------|----------|
| Bear (partial) | 35% | $38 | $4.50 | $1.58 |
| Base | 35% | $42 | $0.50 | $0.18 |
| Bull | 20% | $48 | $0.00 | $0.00 |
| Tail | 10% | $35 | $7.50 | $0.75 |
| **EV** | | | | **$2.50** |

Narrower window = narrower EV. This is a **catalyst bet** on April 16 earnings. If Q1 shows noncurrent rising + provision surge, it prints. If management kitchen-sinks and the stock rallies on "worst is over," it expires worthless.

---

## Key Takeaway for Position Management

1. **This is an earnings compression trade, not a capital depletion trade.** Frame it that way.
2. **Aug $45 is the right structure** — 2-2.7x EV, captures the maturity wall window, survives a squeeze if you hold.
3. **May $42.5 is marginal** — positive EV but narrow. Only works if April 16 catalyzes.
4. **The 10% EV edge on stock ($38.75 vs $43) IS thin for a stock short.** But we're not shorting stock — we're buying puts. The asymmetry changes the math. A $3-4 put that pays $8-12 in the bear case is a 2-3x return with a defined max loss.
5. **Squeeze risk is real but survivable.** 14-15% SI with 12-18 days to cover means any positive catalyst spikes the stock. Size to survive $50-55 without panic selling.

---

*Sources: FDIC API capital ratios, SCENARIOS.md probability weights, OZK management comments (EPS, dividend).*
