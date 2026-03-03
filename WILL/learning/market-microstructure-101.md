# Market Microstructure 101
**Created:** 2026-03-03 | **Context:** Learned during Hormuz selloff, S&P hit 6,672 intraday

---

## Three Types of Market Analysis

| Type | Question It Answers | What We Use It For |
|------|--------------------|--------------------|
| **Fundamental Analysis** | What SHOULD the price be? | Agent network — hidden CRE, subprime auto, carry unwind, cockroach chain. The WHY. |
| **Technical Analysis (TA)** | What has price DONE? | Charts — double tops, MA crosses, support/resistance, RSI, MACD. The TIMING. |
| **Market Microstructure** | What are participants POSITIONED to do? | Gamma, GEX, CTA triggers, dealer hedging. The MAGNITUDE and MECHANICS. |

**The edge is using all three together.** Any one alone is weak.

- Fundamentals say DOWN (agents, thesis)
- TA says THE TOP IS IN (chart reads — double top, death cross, lower highs)
- Microstructure says HERE'S HOW FAR ($80B CTA trigger, gamma acceleration)

---

## Core Concept: Forced Behavior vs Voluntary Decisions

The key difference between microstructure and everything else: **it's about what participants MUST do, not what they choose to do.**

- TA says "sellers will likely step in"
- Fundamentals say "the bank should decline"
- Microstructure says "these funds MUST sell $80B when this level breaks, whether they want to or not"

CTAs don't have opinions. They don't read charts or 10-Ks. Their algorithm says "50-day MA breached → sell." Mechanical. Predictable. Exploitable.

---

## Key Terms

| Term | What It Means |
|------|---------------|
| **GEX (Gamma Exposure)** | Net gamma positioning of dealers. Positive = they buy dips (cushion). Negative = they sell into drops (amplify). |
| **Gamma Flip** | The price level where GEX goes from positive to negative. Above it = calm. Below it = volatile. |
| **Put Wall** | Strike price with heaviest put open interest. Acts as support — dealers buy here to hedge. Holds until exhausted (typically 2-3 tests in same week). |
| **CTA (Commodity Trading Advisors)** | Trend-following algorithmic funds. Buy above moving averages, sell below. ~$200-300B AUM. Key triggers are 50-day and 200-day MA crossovers. |
| **0DTE (Zero Days to Expiry)** | Options expiring same day. ~65% of SPX volume. Creates massive mechanical buying/selling flows at expiry. Protection disappears at close each day. |
| **Vol-Control** | Funds that target a specific volatility level. When VIX spikes, they mechanically sell equities to reduce exposure. Multi-$T AUM. Fastest responders. |
| **Risk Parity** | Funds that balance risk across asset classes. When correlations change (stocks AND bonds fall together), they deleverage everything. ~$1T AUM. Slowest but largest. |
| **Negative Gamma** | When dealers are net short gamma, they must sell as market falls and buy as it rises — they AMPLIFY moves in both directions. |
| **Positive Gamma** | When dealers are net long gamma, they buy dips and sell rips — they DAMPEN moves. Market feels calm and mean-reverting. |

---

## The Trap Door Model (S&P 500 Levels — Mar 3, 2026)

```
7,000+ ............. Positive gamma (dealers cushion dips)
6,902 ← GAMMA FLIP .. 200-day MA. Below = negative gamma (dealers amplify drops)
6,883 ← 50-DAY MA ... Short-term CTAs sell below this. ALREADY BREACHED.
6,800 ← PUT WALL .... Max put open interest. Support until exhausted (2-3 tests).
                       Broke on close Mar 3 (closed 6,781). Test #1 complete.
6,707 ← CTA TRIGGER . Goldman medium-term level. $80B systematic selling.
                       Hit 6,672 INTRADAY Mar 3 but closed above. NOT triggered.
                       Needs a CLOSING break — intraday doesn't count.
6,475 ← JPM COLLAR .. JPM's quarterly hedge put (JHEQX). Mechanical buy floor.
```

**Current position (Mar 3 close): 6,781** — below gamma flip, below 50-day MA, below put wall. One sustained close below 6,707 triggers the big selling.

---

## The Cascade Sequence

| Order | Who | AUM | What Triggers Them | Speed |
|-------|-----|-----|--------------------|-------|
| 1 | Vol-Control | Multi-$T | 10-day realized vol spike (VIX >25) | Immediate |
| 2 | Short-Term CTAs | ~$100B | Short MA breach (50-day) | Days |
| 3 | Medium-Term CTAs | ~$200B | 50/200 DMA cross, sustained close below 6,707 | 1-4 weeks |
| 4 | Risk Parity | ~$1T | Cross-asset correlation breakdown (stocks + bonds fall together) | Weeks-months |

**Where we are Mar 3:** Stage 1 (vol-control) activated (VIX 26.43). Stage 2 (short-term CTAs) activated (50-day MA broken). Stage 3 (medium-term CTAs) armed but NOT triggered (6,707 needs closing break). Stage 4 not yet.

---

## Key Rules

1. **Closing price matters, not intraday.** CTA algos trigger on daily closes, not intraday touches.
2. **0DTE protection resets daily.** Today's gamma cushion expires at close. Tomorrow opens naked.
3. **Put wall erosion:** 2-3 tests in same week typically exhausts the gamma support at that strike.
4. **Equity cannot bottom until HY OAS peaks** (HENRY rule H4, 85% confidence). Credit leads equities.
5. **The recovery tells you the regime.** If a -2.5% drop recovers to flat, check whether it was mechanical (0DTE expiry) or real buying. If mechanical, the selling resumes next day.

---

## How to Track (Free Sources)

| Data | Source | What It Shows |
|------|--------|---------------|
| SPX Put/Call OI by strike | CBOE (free, daily) | Where put walls are |
| VIX term structure | VIXcentral.com | Contango = calm, backwardation = panic |
| DIX (Dark Index) | Squeezemetrics | <40% = institutional selling |
| 50-day / 200-day MA | Any charting tool | CTA trigger levels |
| HY OAS | FRED (ICE BofA) | Credit stress — leads equity |

---

## How This Connected to Our Trades (Mar 3)

- KRE $66P Mar 13: If S&P breaks 6,707 → CTA selling → risk-off cascade → regionals get crushed → KRE $62-63 → this put prints 2-3x
- WAL $77.5P Mar 20: WAL drops faster than index in risk-off (specific vulnerability + sector beta)
- IWM $250P: Small caps get hit hardest in mechanical selloffs — liquidity dries up first
- HYG $75P: Credit leads equity. HY OAS must peak before stocks bottom. Our credit put is the anchor.

---

*Revisit this before any major selloff or catalyst. The levels change as options expire and new ones are written — check HENRY's STATUS.md for current levels.*
