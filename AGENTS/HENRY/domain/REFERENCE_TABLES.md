# HENRY — Static Reference Tables
*Moved from STATUS.md Mar 5 to save space. These rarely change.*

## CASCADE ORDER

> ⚠️ **AUM column = UNSOURCED mechanism illustrations, not tested facts** (Will-ruled 7/31, implemented 2026-08-06 — PROME rulings packet §1; DEWEY confirmed the quanta are not publicly sourceable, per NEXUS_BRIEF). Trigger CONDITIONS stay; never cite the $ figures as measurements. The SPX levels in the Trigger column are Mar-2026 relics — pull live via `gamma_flip.py`, never from here.

| Order | Strategy | AUM *(UNSOURCED)* | Trigger | Speed |
|-------|----------|-----|---------|-------|
| 1 | Fast Vol-Control | Multi-$T | 10-day realized vol | Immediate |
| 2 | Short-Term CTAs | ~$100B | 50-DMA breach (6,883 — Mar relic) | Days |
| 3 | Medium-Term CTAs | ~$200B | 6,707 (Mar relic) close below → $80B | 1-4 weeks |
| 4 | Longer-Duration CTAs | ~$200B+ | ~6,494 (Mar relic) sustained below | Weeks |
| 5 | Risk Parity | ~$1T | Cross-asset correlation | Monthly |

## LEADING INDICATOR SEQUENCE

```
MOVE rises (VIX flat)       → 2-5 days before
VIX inverts (spot > futures) → 1-3 days before
GEX thins (<$2B)            → 1 day before
DIX drops (<40%)            → 1-2 days before
PUT WALL BREAKS             → T-0: Cascade begins
CTAs flip at 6,494          → T+1 to T+5
Risk parity deleverages     → T+5 to T+30
```

## CREDIT-EQUITY TRANSMISSION

| HY OAS 5-Day Change | Equity Impact | Lead Time |
|---------------------|---------------|-----------|
| +25-50 bps | -2% to -5% | 2-3 sessions |
| +50-100 bps | -5% to -10% | 0-1 session |
| +100+ bps | -10%+ | Same day |

## GAMMA-CUSHION VALIDITY RULE (GCVR)
*Codified 7/6 from the mid-July-node adversarial pass. The discriminator for when "+GEX cushions equity" is TRUE vs falsely reassuring. Reusable — classify the shock BEFORE citing a gamma cushion.*

> **Core rule:** Positive dealer gamma (+GEX, SPX above the flip) dampens moves that travel **ALONG the SPX price axis**. It gives **zero offset to shocks that originate OFF that axis** — rates/duration, cross-asset correlation, credit. Mis-applying "equity is cushioned" to an off-axis shock is falsely reassuring. **And a fast off-axis gap that clears the flip converts +GEX → −GEX — the cushion doesn't just vanish, it inverts to an amplifier.**

**Why +GEX only cushions the SPX axis:** long-gamma dealers hedge by buying SPX dips / selling rips → mechanically dampens *intraday SPX oscillation*. That provides NO offset to (a) multiple compression from a higher discount rate (real yields/term premium up — the shock enters via the denominator, not the index price); (b) a cross-asset correlation spike (stocks AND bonds down together → risk-parity/vol-target forced de-lever = **cascade step 5** — a selling FLOW dealer gamma can't see); (c) credit-led selling (HY OAS gaps; credit leads equity 2–3 sess — gamma bounds velocity, not the trend).

| Shock class | Originates on | +GEX cushion | Leading vol tell | Correct read |
|-------------|--------------|--------------|------------------|--------------|
| Equity-index level drift / mean-reverting dip | SPX price axis (positioning, equity news) | **VALID** — genuinely cushioned | VIX-led | "cushioned" is fair |
| Rate / duration shock (30Y tail → 10Y gaps; real-yield/term-prem up) | rates | **INVALID — can invert** | **MOVE-led** | NOT cushioned; watch −GEX flip |
| Cross-asset correlation spike / risk-parity de-lever | cross-asset | **INVALID** | correlation + MOVE | forced-selling flow, gamma blind |
| Credit-led (HY OAS gaps) | credit | **INVALID / partial** | HY OAS + MOVE | gamma bounds velocity, not trend |

**Three fast tells — which regime am I in?**
1. **Where's the vol?** MOVE (rate vol) rising with VIX flat = off-axis shock → cushion INVALID (cf. LEADING INDICATOR SEQUENCE: MOVE leads VIX by 2–5 days). VIX-led = on-axis, cushion holds.
2. **Stock-bond correlation sign.** Stocks AND bonds DOWN together = correlation spike → cushion INVALID. Stocks down / bonds bid (flight-to-quality) = on-axis.
3. **KRE direction** (the existing margin-vs-credit test): KRE down *with* equity = credit story → cushion INVALID.

**Worst case:** an off-axis shock LARGE enough to gap SPX under the flip = no cushion + then −GEX amplification.

**Worked application (7/6 node):** the 7/9-30Y-reopen → CPI-7/14 path is an **off-axis rate/duration shock** (a soft 30Y gaps 10Y through 4.50 with no dovish-growth offset). So "equity cushioned now (+~1% over the flip, +GEX dampening)" is VALID *only* vs an equity-level move — it is **falsely reassuring for the live risk path**. A hot-CPI rate-led gap >~1% both (a) is the shock class +GEX doesn't cushion AND (b) flips SPX under the flip into −GEX amplification. Read "equity cushioned" as "cushioned against a garden-variety level dip, NOT against the rate-led gap that is the actual node risk."

## TRANSMISSION PATHS

- **LABOR → HENRY:** Claims >300K = fundamental trigger → gamma test of Put Wall
- **HENRY → CARL:** SPX -10%+ → Reverse Wealth Effect → spending pullback. SBC amplifies to $19-26T wealth destruction.
- **SAM → HENRY:** Yen appreciation = carry unwind = Aug 2024 playbook

## SENTIMENT REVERSAL FRAMEWORK (3-pillar)
*Reusable structure from KB ML-HEN-021 (Jan'26); read the pillars, pull live readings — don't cite the archived Jan levels.*

| Pillar | What to read | Reversal-risk signature |
|--------|--------------|-------------------------|
| 1. Positioning | AAII / NAAIM allocation | Fully-invested both = exhausted upside |
| 2. Structural leverage | FINRA margin debt + retail options share | Record margin + high 0DTE/retail = fragile |
| 3. Smart-money distribution | Insider sell/buy ratio | >3σ from ~2-3:1 norm = distribution phase |

## SENTIMENT / FLOW DATA SOURCES (release cadence)
*From KB ML-HEN-025 (Jan'26). Where to pull each input.*

| Source | Cadence | Source | Cadence |
|--------|---------|--------|---------|
| AAII | Thu | ICI fund flows | Wed |
| Investors Intelligence | Wed | OCC options | Daily |
| CNN Fear & Greed | Real-time | Fintel insiders | Daily |
| NAAIM | Thu | NASDAQ short interest | Bi-monthly |
| FINRA margin | Monthly | | |
