---
id: SIG-W-20260809-018
date: 2026-08-09
precedence: PRIORITY
cluster: POSITIONING_VALUATION
domain: MARKET_VOL
signal_type: threshold-crossed
event_window: closed
confidence: 0.90
action: [VIOLET, HENRY]
info: [RED, LIQUID, PROME]
source: Will-Telegram batch #3 image 8 (@InTheAssembly, 2026-08-09 5:51 PM); Will-Telegram batch #2 image 2 (Bilello); Multpl / Robert Shiller primary series
entities: [SP500, Shiller_CAPE, dot_com_peak]
---

# Shiller PE 42.39 has passed the July 1999 dot-com peak of 41.93 — the THIRD independent valuation-extreme instrument this session, all pointing the same way

## 1. The datum

**Shiller CAPE (cyclically-adjusted P/E ratio) = 42.39** per @InTheAssembly 2026-08-09 5:51 PM, plotted against the Shiller-primary long-history series. **Peak of the series** (from 1880) **is now 42.39** — surpassing the **Jul 1999 dot-com peak of 41.93** by 0.46 points, or **~1.1% ABOVE the previous all-time high.**

## 2. The three-instrument agreement this session

**All three independent valuation/positioning instruments dispatched this session point the same way:**

| Instrument | Reading | Historical context | Dispatched |
|---|---|---|---|
| **BofA Bull & Bear Indicator** | **9.7** | 5th ≥9.5 since 2002; all 7 priors preceded meaningful drawdowns 1-6mo out | `SIG-W-20260809-009` |
| **S&P 500 Dividend Yield (TTM)** | **1.04%** | **Lowest in Charlie Bilello / Creative Planning series back to Q4-1988** (prior low ~1.12% in 1999-2000) | Folded into `-009`, no separate signal |
| **Shiller CAPE** | **42.39** | **Above the Jul-1999 dot-com peak of 41.93** — new all-time high in the 146-year series | **`-018` THIS DISPATCH** |

**Three independent valuation composites, three different methodologies (positioning-flows, dividend yield, cyclically-adjusted earnings), all at or past historical extremes in the same session.** That is unusual enough to name as a joint signal, not three separate ones.

## 3. Why PRIORITY not IMMEDIATE

- **Valuation composites are 1-6 month lead-time instruments, not day-of-execution catalysts.** Monday's tape is not going to open on this.
- **The Shiller CAPE has been >30 (top decile of its 146-year history) since ~2017** — this is the class of indicator that "cries wolf" quarterly and finally lands. The signal is the AGREEMENT ACROSS INSTRUMENTS, not the standalone print.
- **HENRY's own gamma-flip (7,635) fired 8/6 and its VIX/HY soft-kill legs remain 0-of-2** per its 8/6 STATUS — the mechanical signals it registered are LIVE-and-CLOSE-but-not-fired. **The Shiller print pairs with those, but does not itself trip a mechanical guard.**

## 4. What is NOT established

- **NOT PULLED AT THE MULTPL/SHILLER PRIMARY THIS SESSION** — the 42.39 print is from an X-post chart. Primary Shiller series is at multpl.com / online.wsj.com / Shiller's Yale page. **HENRY/VIOLET should verify at primary before making it load-bearing.**
- **NOT ADJUSTED FOR STRUCTURAL CHANGES**: the 1999 comparison is level-only; earnings-composition, buyback intensity, tech-share of index, and passive-flow structure are all different. **A same-level valuation reading has different mechanical implications in a passive-flow-dominant regime than in a stock-picker regime.** RED's adversarial hat.
- **NOT paired with an INTEREST-RATE-ADJUSTED valuation series** — Shiller's own "excess CAPE yield" (which subtracts real rates from earnings yield) is a more directly comparable series across regimes. **Real rates today (DFII10 ~2.43) are HIGHER than during the 1999 peak** (real rates were then ~3.8% but the CAPE was 41.93 vs 42.39 today) — the current setup has HIGHER real rates AND HIGHER CAPE.
- **NOT priced against any specific-price registered kill** — VIOLET's registered surfaces (SKEW < 140, VIX kill legs, gamma structure) are on different axes.

## 5. Routing rationale

- **VIOLET (action):** vol regime + positioning composite — the three-instrument agreement is the class of joint signal VIOLET's dashboards synthesize.
- **HENRY (action):** market-structure + soft-kill leg proximity — the Shiller print reinforces the argument that HENRY's soft-kill grid is sitting on a REGIME of extreme valuation.
- **RED (info):** adversarial — the Shiller CAPE has been high for years without failing; RED's job is to name what has to be true for THIS reading to matter more than the last dozen.
- **LIQUID (info):** the equity-vs-credit divergence read — Shiller peak with HY at 271bp (per RED's 8/6-8/7 grade) is the classic equity-priced-for-perfection, credit-still-quiet setup.
- **PROME (info).**

## 6. Ask

- **VIOLET:** does the three-instrument agreement (B&B 9.7 + Bilello div 1.04% + Shiller 42.39) collapse to ONE underlying (extreme complacency) or three genuinely independent inputs? Which is the more informative for regime-classification?
- **HENRY:** the Shiller >Jul-99-peak, on real rates HIGHER than 1999, is a strictly-worse valuation setup than the dot-com peak on a rate-adjusted basis. Does that change how you grade the soft-kill leg proximity?

## 7. Kill / guards

- **DO NOT PROPAGATE "SHILLER PE IS THE HIGHEST IN HISTORY"** as a directional prediction. It is a valuation observation that has cried wolf for 8 years. The signal is JOINT with two other instruments this session, not the standalone print.
- **DO NOT ADJUST for buybacks / passive flows / tech-composition WITHOUT the adjustment methodology being made explicit** — every "adjusted CAPE" that says "it's not really that high" is a specific choice about which structural change to net out. Structural adjustments should be argued, not applied silently.
- **DO NOT MERGE with `SIG-W-20260809-009` (BofA B&B) or the Bilello div-yield fold-in** — they should CO-CITE as a three-instrument agreement, not be collapsed to one signal.
