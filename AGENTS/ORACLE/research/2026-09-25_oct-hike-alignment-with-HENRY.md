# October FOMC hike: prediction venues vs fed funds futures, aligned (ORACLE half)

**Ask:** PROME packet `inbox/2026-09-25_from-PROME_bounded-follow-up-…` (Will's item 4, 01:01 ET 9/25), commit `40915c8c0`. **Peer:** HENRY (`henry-68`) owns the futures half, in `AGENTS/HENRY/research/2026-09-24_fedwatch-method-october-odds.md` and `…/2026-09-25_rates-move-and-hike-alignment.md`.
**Built:** 2026-09-25 ~05:0x–05:2xZ (01:0x–01:2x ET). Venue histories were read from each exchange's own record, not re-typed from STATUS.

## Verdict
**One same-time, same-event, same-units comparison exists: expected change in basis points at 15:00 ET on 9/24.** Futures **+18.0bp**, Polymarket **+16.5bp**, Kalshi **+16.1 to +16.6bp**. The venues sit **~1.5–2bp under futures, ≈6–8pp in hike-probability terms.** The ~11–12pp in KB-ORC-097 compared a secondary 77.5% at an unknown time with venue prices from 21:35 ET, so it is **superseded**.
**Two things cannot be matched:**
- **(a)** P(hike) as a probability, because futures only price an expected change.
- **(b)** The exact event. Futures measure average November EFFR. The venues resolve on the upper bound published after 10/28.

The 1.5–2bp residual is the same size as (b)'s basis terms, so **it is not a disagreement.**

## 1. Contracts: resolution event and source (read at the primary, 2026-09-25 ~05:04Z)
| Venue | Contract | Resolves on | Source |
|---|---|---|---|
| Polymarket | event `fed-decision-in-october-20260617190323537` ($13.4M vol). 5 mutually exclusive branches | Change in the **upper bound** vs pre-meeting level, "after the October 2026 meeting". Non-grid moves are **rounded up to the nearest 25**. No statement by the next meeting ⇒ "No change" | FOMC statement for the 10/27–28 meeting (federalreserve.gov) |
| Kalshi | `KXFED-26OCT-T{x}` ladder, "upper bound **above x%** following the Oct 28, 2026 meeting" (cumulative, 11 strikes) | Upper bound published after 10/28 | Fed official website. Expires 2:05 PM ET after the statement, or 1 week after the meeting |
| Futures (HENRY) | ZQX26, November 30-day fed funds | **Average EFFR over November**. No November FOMC ⇒ prices the 10/28 decision **plus any intermeeting move** | CME. HENRY's read = vendor last trade ≤15:00 ET, **not settlement** |

## 2. Hike-size branches: one contract or a sum?
| Venue | Branches | P(any hike) | Size resolution |
|---|---|---|---|
| Polymarket | −50+ · −25 · hold · **+25 (exactly)** · **+50+ (open-ended)** | **Sum** of +25 and +50+. The branches sum to 1.0075–1.0085, so they are normalised | +50+ counted at 50bp, which is a **lower bound** |
| Kalshi | Cumulative "above" rungs: P(cut)=1−P(>3.75) · hold=P(>3.75)−P(>4.00) · +25=P(>4.00)−P(>4.25) · **≥+50 = P(>4.25)** | **One contract**: P(>4.00) = P(≥+25) | `>4.25` **is the whole ≥+50 mass** (all larger moves included). At a 1/2¢ book it sits at the **tick floor**, so it is an upper bound, not an estimate |
| Futures | none: a single expected rate | not observable | HENRY's 72% **assumes** a binary 25bp-or-hold outcome |

⇒ **The size dimension is aligned in expected bp, not in P(hike)**, per HENRY's proposal: E = 25·P(+25) + 50·P(≥+50) − 25·P(−25) − 50·P(−50+).

## 3. Same-time comparison (15:00 ET 9/24 = 19:00Z)
| Source | Stamp | Branches (hold / +25 / ≥+50 / cut) | **E[Δ] bp** | P(≥+25) |
|---|---|---|---|---|
| **Futures ZQX26** (HENRY) | last trade ≤15:00 ET | n/a | **+18.0** (±0.5; 0.005 quote) | "72%" only under the binary assumption |
| **Polymarket** | CLOB `prices-history` 1-min, print 18:59Z | 33.25 / 65.01 / 0.94 / 0.80 (normalised) | **+16.5** | 66.0 |
| **Kalshi** | hourly candle ending 19:00Z, bid/ask close mids: `>4.00` 63/65¢, `>4.25` 1/2¢ (last quote 17:00Z), `>3.75` 99/100¢ | 35.5 / 62.5 / 1.5 / 0.5 | **+16.1 to +16.6** (tick-floor tails ±0.5) | 64.0 |

**Our pull stamp for reference (9/25 01:35–01:48Z = 21:35–21:48 ET):** Polymarket E **+16.7bp** (65.9 / 1.0 on +25 / +50+). Kalshi E **+17.1bp** (`>4.00` 67/68¢). HENRY is re-reading ZQX26 at this stamp, but the **evening futures session is thin** (~2.5K volume vs 183K in regular hours), so 15:00 ET is the better-anchored pair.

## 4. What cannot be aligned and why (the event basis; HENRY's domain, named here)
1. **EFFR vs upper bound.** Futures price where EFFR trades inside the range. HENRY assumes EFFR sits 12bp under the top (3.88 in 3.75–4.00) and moves one-for-one with a hike. Month-end or quarter-end EFFR drift moves the implied figure. The venues never see EFFR.
2. **Intermeeting moves.** These are in the November average, and the venues exclude them. Tiny, but the direction is toward a higher futures figure.
3. **Futures risk premium.** Fed funds futures carry a term/risk premium that biases them hawkish in a hiking cycle. Size unmeasured here.
4. **Settlement vs last trade.** HENRY's price is a vendor last trade, not the CME settlement.

⇒ These four are each about 0.5–2bp. The 1.5–2bp residual is **within them**. **Do not quote "venues lag futures by X" as a finding.** Quotable: *at matched time, both venues price roughly +16–17bp, and futures price about +18bp before basis adjustments.*

## 5. Consequences on ORACLE surfaces
- KB-ORC-097 ("~11–12pp below CME") → **SUPERSEDED** by KB-ORC-100.
- STATUS Alert 1 and NEXUS_BRIEF lead now carry the aligned figures.
- VX-ORC-08 is not re-graded. Its alert cell is a P(hike) threshold on the venue, and this comparison does not change the venue level.
