# HENRY · S&P dealer-gamma map after a hot or a cool October PPI (Fri 11/13 08:30 ET) · for TERRY

**Written:** 2026-11-12 16:07 ET, on PROME's ask (prome-e8, 15:4x ET), after Will's 15:39 ET question. **No prediction, score, band or gate moves. HENRY makes no card; tradeability is TERRY's.**

## Basis (read this first)

| Item | Value | Kind |
|---|---|---|
| S&P close | **7,592.40** (−0.35%), vendor pull 16:06 ET 11/12 | data |
| Flip (14d / 35d) | **7,635 / 7,630**, published 16:06 ET | computed |
| Net dealer gamma at the close | **−$19.9B / −$21.5B per 1%**: NEGATIVE, so dealers amplify moves | computed |
| Put wall | **7,500**, clean #1 at both horizons | computed |
| Call wall | **7,700**, clean #1 at both horizons | computed |
| Today's low | 7,567.36 at 09:33 ET (vendor); not retested by the close | data |
| HENRY yellow line | 7,200 (orange 7,100; red 7,037.04 = −10% from the 10/6 peak) | registered line |
| Rates going in | Treasury par 11/12: 10Y **5.10%** (over my 5.0 red line, card SIG-W-20261112-008), 2Y 4.86%, 30Y 5.43% | data |
| Vol going in | VIX 18.93 (+8.2%), VIX3M 20.20, contango (vendor 16:06 ET) | data |

Chain: Cboe, asof 11/12 = **11/11 open interest** (before the Nvidia news). Free-tier proxy: the sign and the flip are the robust part; the $B assumes dealers are long calls and short puts and is not SpotGamma-grade.

## The computed profile: dealer gamma if the S&P opens at each level

Same chain, re-priced at each spot (`gamma_flip.py --both --spot X`, run 15:50 ET 11/12). **Computed, not judgment.** IV is held at the 15:50 snapshot and open interest at 11/11.

| S&P level | What it is | Net gamma 14d / 35d ($B per 1%) | Dealer hedging |
|---:|---|---:|---|
| 7,750 | | +47.8 / +57.3 | damps |
| **7,700** | call wall | +31.3 / +36.3 | damps, strongly |
| 7,660 | | +13.8 / +15.0 | damps |
| **~7,630–7,635** | **flip** | about 0 | turns over |
| 7,610 | | −10.6 / −13.5 | amplifies |
| **7,592** | **close** | −19.9 / −21.5 (16:06 run) | amplifies |
| **7,567** | today's low | −30.1 / −36.4 | amplifies |
| 7,530 | | −42.7 / −51.5 | amplifies |
| **7,500** | put wall | −50.3 / −60.9 | amplifies |
| 7,450 | | −58.1 / −71.2 | amplifies; the script flags "below put wall, intensified downside feedback" |
| 7,350 | | −61.6 / −78.2 | amplifies, near the trough |
| **7,200** | HENRY yellow line | −54.8 / −73.7 | amplifies |

**Shape:** everything under ~7,632 is amplifying, and the amplification **deepens on the way down to about 7,350–7,450, then eases slightly**. Above the flip, damping builds fast toward 7,700.

⚠️ **One correction to how I put it to Will at 15:4x ET.** I said the put wall "tends to act as a floor." On this computed map it does not damp: 7,500 is where dealer hedging pressure is near its heaviest, and it pushes the same way as the move. That walls sometimes hold, as the Nasdaq's 680 / 28,000 walls did at today's open, is an **observed tendency and my judgment**, not something this model computes. Treat 7,500 as the level where the move either stalls or speeds up, not as support.

## Case A: hot print (final demand m/m 0.5% or more, my HEN-58 yellow line or above)

- **Direction (judgment):** yields up from an already-red 10Y; stocks down. Today's tape fits this: no bond bid on an equity shock, and yields rose with stocks down.
- **Map (computed):** from 7,592 down, dealer hedging is on the **selling** side the whole way, and it gets heavier at each level. Levels in order: 7,567 (today's low, 0.3% down), **7,500 put wall (1.2% down)**, then the deepest amplification near 7,350–7,450 (1.9–3.2% down), and 7,200 (5.2% down, my yellow line).
- **What would make the read wrong:** a hot print where the S&P holds over 7,567 through the first hour, or yields fall after the print, or the VIX falls on the day. Any of these says rates are not driving equities and the amplification is not being used.

## Case B: cool print (0.2% or less; **my judgment line, nothing registered**). In-line is 0.3–0.4%.

- **Direction (judgment):** yields ease and stocks rise.
- **Map (computed):** below the flip, dealers **buy into a rally too**. Amplification works both ways up to ~7,630–7,635, 0.5% up from the close. **Above the flip, hedging turns to damping**, and the damping builds toward the **7,700 call wall (1.4% up)**, where I would expect the rally to slow (judgment).
- **What would make the read wrong:** a cool print with yields down but the S&P failing to reach ~7,630, or reversing below 7,567. That would say the drag is the Nvidia / AI-leadership leg, not rates, and that a good inflation number does not fix it.

**In-line (0.3–0.4%):** no direction from me. At about −$20B per 1% at the close, an ordinary move still travels further than it would in a damped tape.

## Caveats that travel with this file

1. **Open interest is 11/11's**, before the Nvidia news. Thursday's trading changes Friday's map. I can re-run at about 08:00 ET pre-open (implied spot from futures) if PROME wakes me.
2. **IV is held fixed.** In a real selloff IV rises, which spreads gamma across more strikes and likely flattens the trough. The $B at far levels (7,350, 7,200) is the least reliable figure here.
3. **Free-tier $B** (long-call / short-put assumption). The flip, the sign and the wall strikes are the robust reads.
4. **No sizing of the PPI reaction.** I have no computed estimate of how far the S&P moves on a given PPI surprise. The direction mapping (hot means yields up and stocks down) is my judgment.
5. **The 14d window includes the 11/20 monthly expiry**, so walls can migrate into it.
6. **Index weight:** Nvidia's weight in the S&P (~7.5%) is ASSUMED, not read from an index provider. NVDA closed $166.19 (−4.34%, vendor 16:06 ET).

Sources: vendor `FORGE/tools/market-data/fetch.py` (16:06 ET); Cboe chain via `AGENTS/HENRY/scripts/gamma_flip.py`; Treasury par CSV (read 15:54 ET); HEN-58 letter `research/2026-10-29_catchup/PREREG_nov-releases.md`. Ledger: `workbook/PUBLISHED.tsv` 11/12 16:06 ET rows.
