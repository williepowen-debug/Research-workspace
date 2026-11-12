# TERRY read — HENRY's negative dealer gamma into Fri 11/13 08:30 ET October PPI: NO CARD

**Written:** 2026-11-12 16:0x EST (from `date`; pulls 16:01–16:04 ET) · TERRY, Claude Code, Claude Opus 5.5 · PROME launch prome-e8 on Will's word (16:00 ET).
**Asked:** a tradeability read on the SIZE of the PPI reaction, not its sign (packet `inbox/processed/2026-11-12_from-PROME_henry-negative-gamma-into-friday-ppi.md`; HENRY 791bfc6caa).
**Verdict:** **NO CARD.** The edge is that negative dealer gamma makes a PPI surprise move the index further than normal. Friday's options already price a move larger than the S&P's average move on a PPI day, the conditional edge cannot be measured tonight, and Will has no way to buy before the 08:30 print unless his broker trades index options overnight, which is unknown.

## 1. What the market prices for Friday (pulled 16:01–16:02 ET, vendor screening marks, finding 5b)

| Item | Figure |
|---|---|
| S&P 500 close 11/12 | 7,592.93 (vendor daily bar, 16:01 ET); ~41 pts under HENRY's flip 7,634 (35d), 7,632 (14d) |
| VIX / one-day VIX (VIX1D) / VIX9D / VIX3M | 18.88 / 15.41 / 17.62 / 20.16 (11/12 closes) |
| One-day VIX as a 1-sigma move | 15.41 / √252 ≈ **0.97%** |
| SPY close | $757.25 |
| SPY Fri 11/13 757 straddle | call 3.00 + put 2.52 mid = **$5.52 ≈ 0.73% of spot** (quotes last traded 15:46–15:47) |
| SPY Mon 11/16 757 straddle | 4.25 + 3.71 = $7.96; Monday alone, by variance subtraction, ≈ $5.74 |

**Read:** Friday (PPI day) is priced about the same as Monday, a day with no scheduled print, and the one-day VIX sits below the 30-day VIX. The market charges no PPI premium.

## 2. What PPI days have actually done (measured; script `ppi_envelope.py` in this folder)

PPI release dates from FRED release 46 (47 dates, 2023-01-18 to 2026-10-15); SPY daily bars from yfinance (981 bars, all 47 dates matched).

| SPY absolute move | PPI days (n=47) median / mean / p75 / p90 / max | All days (n=980) median / mean / p90 | Share of PPI days ≥ 0.73% |
|---|---|---|---|
| Overnight gap (prior close → open) | 0.31 / 0.34 / 0.44 / 0.57 / 1.49% | 0.29 / 0.40 / 0.89% | 6% |
| Close to close | 0.56 / 0.68 / 0.94 / 1.40 / 1.78% | 0.51 / 0.66 / 1.46% | 36% (all days 34%) |
| Open to close | 0.42 / 0.56 / 0.87 / 1.23 / 2.09% | 0.39 / 0.53 / 1.10% | 30% |

Last eight PPI days, close to close: 1.40, 1.22, 0.56, 1.70, 0.40, 0.70, 0.60, 0.28%.

**Read:** over this sample the S&P moves about the same on a PPI day as on any other day. The average PPI-day move (0.68%) is below the straddle's break-even (0.73%). Buying Friday's straddle at Thursday's screen is fair to slightly rich against history. It could pay only if the negative-gamma condition adds more than about 0.05 points to the move.

## 3. Why the conditional cannot carry a card tonight

- **It is not measured.** HENRY's dealer-gamma figures are free-tier estimates with no history; the only part he rates robust is the sign and the flip level. I have no sample of PPI days sorted by dealer-gamma sign to test whether negative gamma enlarges the PPI move. ⚠️ An untested conditional on top of an option priced at fair value is not an edge (RISK_SCORING § 2: never invent p_model).
- **It is public and partly priced.** VIX rose 7.9% on the day (17.49 → 18.88, vendor closes) and VIX1D rose from 12.64 to 15.41. The tape already moved toward the condition HENRY describes.
- **It can reverse before the print.** HENRY: a close back over about 7,634 reverses the read; the chain uses 11/11 open interest; MOC and same-day-expiry flow are not in it. Futures trade overnight (ES=F 7,612.25 at 16:01 ET, vendor, contract not named, construction rule #22, so used here as a quote only).
- **Added since the packet (cited, not mine):** the official Treasury 10-year at 5.10% [11/12] crossed HENRY's 5.0% red line (BOND d7f63e88ce). A hot print with long rates over 5% could plausibly move equities more than history suggests. That is a reason to watch, not a measurement.

## 4. The entry problem

- SPY options stop trading at 16:15 ET; Will is not in session and no card can be approved in that window.
- The print lands at 08:30, before the 09:30 cash open. The only pre-print option vehicles are SPX/XSP options in Cboe's overnight session or CME E-mini options overnight. **Will's broker access to either is UNKNOWN; not inferred.**
- An entry at Friday's 09:30 open buys after the gap. On PPI days the open-to-close move averages 0.56% (median 0.42%). A same-day straddle at the open is the 0–1 DTE frequency trade that construction rule #16 records as this desk's costliest lesson (11 tickets, about −$4,341); its horizon matches the view, and it is still the instrument whose seller usually wins.
- Root rule #6 is not decisive for a straddle (it buys both sides); today was red (S&P −0.35% close to close).

## 5. Re-open conditions (any one, with Will's broker access confirmed)

1. A pre-print at-the-money straddle on SPX/XSP/SPY expiring 11/13 priced at or below **0.56% of spot** (the PPI-day median close-to-close; about $4.25 on SPY at $757): then history alone favours the buyer, max loss = premium, ×1 under the $500 cap.
2. HENRY (owner of dealer flow) produces a dated sample showing PPI or CPI days under negative gamma moved more than the straddle price. That is a study, not owed tonight.

HENRY's hot-print / cool-print sketch had not landed when this was written. It concerns direction, and this read is about size, so it would not change the verdict unless it carried a measured size-of-move figure.

**No order. No card. Nothing put to Will.** SETUPS row `TRY-NOTRADE-PPIGAMMA-NOV12`.
