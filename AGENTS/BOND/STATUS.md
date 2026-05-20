# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure
**State:** 🟡→🟠 WATCH (long-end leg) — 10Y broke 4.5, 30Y sustained above 5; credit cash still calm
**Last Updated:** 2026-05-19 by BOND (live data pull)

---

## Regime Read

Two-track divergence widened over the past week. **Long-end yields broke higher decisively** (10Y 4.46→4.59, 30Y 5.03→5.12 since 5/13) while **public credit stayed calm** (HY OAS 283, IG OAS tightened to 75, VIX ~18). TLT lost another buck-eighty to **$83.01**. No coupon auctions May 14-19 — bill auctions came in clean (BTC 2.66-3.20), so the move is term-premium / duration, not auction-mechanism failure. May 12-13 refunding tails (3Y +0.6 / 10Y +0.4 / 30Y +0.5) plus the post-refunding follow-through are starting to look less like transient supply concession and more like durable repricing.

The "all clear" read on credit is still defensible — CCC at 942 is elevated but not breaking, HYG only off 60 cents, and SOFR-IORB at -12bps shows no funding stress. But the duration thesis is firming up: BND-07 prediction (10Y >4.5 or 30Y >5 for 5 sessions) is **now in motion** — Day 1 for the 10Y trigger and ~3 sessions deep on the 30Y >5 read. **May 20 20Y auction is tomorrow** and becomes the next decisive read on whether long-end demand is mechanically broken or just expensive.

**Decomposition (5/19):** today's 10Y break is **predominantly real-yield-driven**, not reflation. DFII10 has moved +21bp over 4wk (1.92→2.13) while 10Y breakevens have moved only +11bp (2.38→2.49) — real yields are the heavier contributor to the +24bp move in 10Y nominal. That sharpens the term-premium/supply read going into tomorrow's 20Y auction: this is a duration-risk-repricing story, not a Fed-expectations story. **The catch:** 5Y5Y forward inflation has risen +16bp over the same window (2.16→2.32), drifting above the 2.25 anchor band. Near-term breakevens (T5YIE +6bp) are subdued — so it's not transitory oil/JPY pass-through carrying the long-term move. **Long-term inflation expectations are slowly drifting while real yields break higher** — the worse combination, because it means tomorrow's auction is reading into a tape with both real-rate stress AND incipient unanchoring, not just one.

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| HY OAS | **283bps** | 🟢 | FRED `BAMLH0A0HYM2`, May 18 | Below 300; short-HY thesis not active. |
| CCC OAS | **942bps** | 🟡 | FRED `BAMLH0A3HYC`, May 18 | Lower-quality stress still elevated, not broad contagion. |
| IG OAS | **75bps** | 🟢 | FRED `BAMLC0A0CM`, May 18 | IG actually tightened; market functional. |
| 10Y yield | **4.59%** | 🔴 | FRED `DGS10`, May 15 | **Broke 4.5 (+13bp/wk).** BND-07 trigger Day 1. |
| 2Y yield | **4.09%** | 🟡 | FRED `DGS2`, May 15 | +19bp/wk; front-end firmer but not curve-stressed. |
| 2s10s | **+50bps** | 🟡 | FRED derived, May 15 | Modest bear-steepener; not acute. |
| 30Y yield | **5.12%** | 🔴 | FRED `DGS30`, May 15 | **Sustained above 5** (5.03/5.03/5.02/5.12 last 4 sessions). Term-premium repricing. |
| SOFR-IORB | **-12bps** | 🟢 | Dashboard, May 19 | More negative; no funding confirmation of duration stress. |
| HYG | **$79.36** | 🟢 | yfinance, May 19 | -0.62 from 5/13; credit ETF not breaking. |
| TLT | **$83.01** | 🔴 | yfinance, May 19 | New leg lower (-1.79 from 5/13); duration weak. |
| VIX | **17.99** | 🟢 | Dashboard, May 19 | Equity vol still complacent vs duration move. |
| Corp issuance YTD | **$1,013.9B through Apr, +28.2% YoY** | 🟢 | SIFMA May 2026 | Primary market not frozen. |
| **10Y TIPS yield (DFII10)** | **2.13%** | 🔴 | FRED `DFII10`, May 18 | **Real yield +21bp/4wk (1.92→2.13).** Single largest driver of 10Y nominal break — term-premium/supply story dominant over reflation. |
| **10Y breakeven (T10YIE)** | **2.49%** | 🟡 | FRED `T10YIE`, May 19 | +11bp/4wk (2.38→2.49). Inflation expectations drifting up but not the leading leg. |
| **5Y breakeven (T5YIE)** | **2.66%** | 🟡 | FRED `T5YIE`, May 19 | +6bp/4wk (2.60→2.66); choppy. Near-term inflation expectations mixed — JPY/Brent pass-through showing but not dominant. |
| **5Y5Y forward inflation (T5YIFR)** | **2.32%** | 🟠 | FRED `T5YIFR`, May 19 | **+16bp/4wk (2.16→2.32).** Long-term expectations drifting; approaching unanchoring watch zone. Combined with DFII10 break = "real yields + slowly-drifting LT expectations," worse mix than pure real-yield story. |

---

## Latest Auction Read

| Date | Tenor | Size | BTC | High Yield | Indirect | Direct | Dealer | Read |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Apr 22 | 20Y reopening | $13B | 2.68 | 4.883% | 59.6% | 20.2% | 8.6% | Healthy BTC; long-end yield high. |
| Apr 23 | 5Y TIPS | $26B | 2.57 | 1.367% | 57.0% | 23.7% | 7.5% | Improved from March stress. |
| Apr 27 | 2Y | $69B | 2.65 | 3.812% | 49.7% | 27.8% | 10.4% | Acceptable. |
| Apr 27 | 5Y | $70B | 2.33 | 3.955% | 64.1% | 13.3% | 11.2% | Soft but not failed. |
| Apr 28 | 7Y | $44B | 2.51 | 4.175% | 51.7% | 26.6% | 10.3% | Acceptable. |
| May 11 | 3Y | $58B | 2.54 | 3.965% | 63.0% | 20.1% | 16.9% | Weak: +0.6bp tail, BTC below 6mo avg, dealer take elevated. |
| May 12 | 10Y | $42B | 2.40 | 4.468% | 64.0% | 24.1% | 12.0% | Weak: +0.4bp tail, 4th consecutive 10Y tail; foreign demand soft vs recent avg. |
| May 13 | 30Y | $25B | 2.30 | 5.046% | 66.6% | 21.7% | 11.7% | Below avg: +0.5bp tail and lower BTC; demand mix not failed. |

**May refunding read:** all three coupon auctions tailed modestly and bid/covers were below recent averages. This is **yellow duration fatigue**, not red auction dysfunction: tails were small (<1bp), indirect demand stayed around/above 63%, dealer take did not spike catastrophically, and SOFR-IORB remains calm.

**May 14-19 follow-through:** No coupon auctions; bill auctions clean (4W 2.66, 8W 2.72, 13W 3.17, 17W 3.20, 26W 3.07, 6W 3.01). Bills are absorbing fine. Long-end repricing is happening **without** a fresh failed auction — pure term-premium move. **May 20 20Y is the next live read.**

---

## Convergence Matrix

| Vector | Score | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|
| Treasury auction health | 3 | 🟡 | Coupon refunding tailed modestly; bills clean. No coupons May 14-19. | Upgrade on May 20 20Y BTC <2.3, tail >2bps, or dealer spike. |
| HY market function | 1 | 🟢 | HY OAS 283; issuance strong through Apr. | HY OAS >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | 🟢 | IG OAS 75 (tightening); no broad IG freeze evidence. | IG OAS +20bps/week or clustered pulled IG deals. |
| Dealer absorption | 3 | 🟡 | May refunding take contained (10Y 12.0%, 30Y 11.7%, 3Y 16.9%); prior ~$550B net. | Forced inventory decline during selloff or weak auctions + repo pressure. |
| Long-end/duration | **4** | 🔴 | **10Y broke 4.5 → 4.59; 30Y 5.12 (4th session above 5)**; TLT $83.01 fresh low. | 10Y >4.5 for 5 sessions and/or 20Y auction confirms demand hole = red 5. |
| CDX-cash basis | 2 | 🟡 | Direct CDX still not wired; March divergence not refreshed. | CDX widens while HY cash stays tight for 2+ weeks. |
| Credit-equity lead | 1 | 🟢 | HY OAS 283, VIX 18; credit hasn't led. | HY OAS +75-100bps from trough while VIX stays <20. |

**Composite:** **15/35 — watch with active long-end leg.** Public credit cascade thesis still inactive; **duration repricing thesis firming** (10Y >4.5 trigger now in motion). Cleanest near-term read is May 20 20Y auction: clean = term-premium-only repricing; failed = demand-hole confirmation and BOND escalates to orange.

---

## Trade Interface

- **HYG $75P Jun:** BOND still does not support adding/rolling. HY OAS 283 + IG OAS tightening + HYG holding $79 = no credit transmission to argue from. Position is salvage/lottery unless HY OAS reclaims 300 quickly.
- **TLT puts:** BOND posture upgrades from "watch/conditional hold" → **supports hold; supports add on May 20 20Y confirmation**. 10Y broke 4.5 (Day 1 of 5-session trigger); 30Y sustained above 5; TLT new low at $83.01. Aggressive add is justified if May 20 20Y delivers BTC <2.3 / tail >2bps / dealer spike; otherwise hold and let the 5-session 10Y trigger play out.
- **Credit-equity lead:** still inactive. HY OAS hasn't moved.

---

## Immediate Catalysts

| Date | Catalyst | What BOND watches | Signal Route |
|---|---|---|---|
| **May 20 (tomorrow)** | **20Y reopening (Leg 1)** | BTC vs 2.68 prior; tail size; dealer take vs 8.6% prior. See `WATCH_20Y_10Y_MAY20-21.md` §2 for verdict matrix and §4 for locked add specs (TLT $83P Aug 15 × 2 on orange print; aggressive-add pre-approved on failed/two-tail). | LIQUID/ZHAO if weak; PROME if failed |
| **May 21** | **10Y reopening 9Y8M (Leg 2 — escalation gate)** | **Two tails in 24h across both legs = BND-07 graduates "firming"→"FIRED", composite long-end 4→5, BOND 🟠→🔴.** See `WATCH_20Y_10Y_MAY20-21.md` §3. | LIQUID/ZHAO if weak; PROME if two-tail |
| Daily | 10Y closes >4.5 streak | BND-07 5-session trigger: Day 1 of 5 | HENRY (duration→risk-asset signal) |
| Daily | 30Y closes >5 streak | Day ~4 of sustained above 5 | LIQUID (term-premium funding consequences) |
| Weekly | HY/IG OAS + primary calendar | OAS >300 / pulled deals / issuance freeze | BROCK/REGINALD/HENRY |
| Weekly | Dealer positions (FR2004) | absorption capacity vs forced de-risking | LIQUID/ZHAO |
| As available | CDX.HY / CDX.IG | synthetic leading cash | HENRY/VIOLET/LIQUID |

---

## Bottom Line

The two-track regime is sharpening: **long-end is breaking, public credit is not.** 10Y broke 4.5 and 30Y is sustaining above 5 for the first time since 2007 — duration thesis has fresh evidence. But HY OAS 283, IG OAS *tightening* to 75, HYG holding, and VIX <20 mean credit cascade thesis still has no transmission. BOND's near-term decision pivot is **May 20 20Y auction**: clean = term-premium-only repricing (TLT puts work as carry-the-trend); failed = demand-hole confirmation and escalation to orange across long-end, dealer absorption, and FOI vectors. HYG June downside remains stale until HY OAS >300 with velocity.
