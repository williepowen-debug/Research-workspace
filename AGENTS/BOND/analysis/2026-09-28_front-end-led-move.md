# 9/28 front-end-led move: what repriced, and where (Will: "go deeper on today's front-end-led move")

**Written:** 2026-09-28 16:52 ET by BOND · **KB:** `KB-BND-353` · **Basis:** U.S. Treasury official par/real curve CSV (9/28 row, ~3:30 PM ET indicative, H.15 source) · FRED EFFR/SOFR/target range · yfinance CBOT fed funds futures (vendor, read ~16:3x ET; last trade, NOT settlement) · one yfinance CME SOFR-futures print per contract (no history returned).

## Bottom line
The repricing **grew with the horizon**. The Oct/Nov meeting odds barely moved; the 2027 path moved most. So today was about **how high the Fed ends up** (the terminal rate), not whether it hikes on 10/28. It was also **real-rate-led**: 5Y real +9bp, 5Y breakeven −1bp. So the market is pricing tighter policy, not higher inflation. **The cause is a GAP**: no US data were released today, no Fed speaker was found, and the reachable news names only global bond pressure and hike expectations (CNBC/Babypips full text 403).

> ⚠️ **DATED EDIT 18:18 ET 9/28 — driver GAP → WIRE-ATTRIBUTED, not causal** (WALTER `SIG-W-20260928-021`, answering WQ-327 item 7): Reuters TREASURIES wire (body read by WALTER via syndication) — October 25bp-hike odds **68% from 64%** (CME FedWatch), oil/Middle East; Bloomberg/Energy Connects headlines tie the sell-off to oil after Trump spurned Iran's offer (**the rejection was Sat 9/26**, not a new Monday event); WSJ/FT: a global US+EU sell-off. **Two limits:** FedWatch and BOND's read both price off CBOT ZQ, so their agreement validates the fetch, not an independent cause; and **the oil channel does not show in breakevens** (10Y BE flat, 5Y −1bp on 9/28) — so oil worked through the hike path, or is not the driver; the tape cannot say which. Reuters' intraday levels are a different basis from the par cells here. Carried to the WQ-317 page (10/2) as SHARED-branch evidence.

## 1 · The gradient (9/25 → 9/28, bp)
| Horizon | Instrument | Implied / yield 9/28 | Δ |
|---|---|---:|---:|
| Nov-26 avg (post-10/28 meeting) | ZQX26 | 4.05% | **+1.5** |
| Jan-27 avg | ZQF27 | 4.28% | +3 |
| Mar-27 avg | ZQH27 | 4.485% | +4.5 |
| 6M bill | Treasury par | 4.41% | +8 |
| 1Y | Treasury par | 4.59% | +9 |
| 2Y | Treasury par | **4.92%** | **+11** |
| 1y1y (2×2Y−1Y, par approx) | derived | 5.25% | **+13** |
| 5Y · 10Y · 30Y | Treasury par | 5.06 · 5.24 · 5.56 | +8 · +7 · +7 |

- **Oct 28 hike odds ≈ 68%**: (ZQX26 4.05 − EFFR 3.88 [9/25]) ÷ 25bp. BOND arithmetic, assuming EFFR holds at 3.88 until the meeting. That is close to the ~66–70% on news/TE (secondary), and about where it stood on 9/23–9/25 (4.035–4.055).
- **The path the strip prices:** cumulative ≈ +40bp by the Jan-27 average and ≈ +60bp by the Mar-27 average. The CME SOFR 3M Jun-27 contract implies 4.865%, i.e. ≈ +97bp over SOFR 3.90, **about four hikes by mid-2027** (a single vendor print with no history, so C3). The Fed's own September SEP median was **one more hike in 2026 (4.125%)**. The market is well above it by early 2027. The SEP 2027 median is **not verified here** (secondary headline only).
- ⚠️ **Cash moved about twice as much as futures at matched horizons** (6M bill +8 vs Mar-27 FF +4.5). One possible cause is a futures bar-timing mismatch (last trade ~16:3x vs the 3:30 PM cash snapshot); the other is cash-specific selling (quarter-end balance sheets, bill supply, foreign front-end selling, which is ZHAO's lane). **Not decidable on these data.** Recorded as an open question, not a finding.

## 2 · Is "front-end-led" new? No: it's a one-day twist inside a broad move
| Session | 2Y | 10Y | 30Y | 2s30s Δ |
|---|---:|---:|---:|---:|
| 9/23 | +14 | +15 | +11 | −3 |
| 9/24 | +2 | +7 | +7 | +5 |
| 9/25 | −6 | −1 | +2 | +8 |
| 9/28 | +11 | +7 | +7 | −4 |
| **9/22 → 9/28** | **+21** | **+28** | **+27** | **+6** |

- Over the four sessions the move is **near-parallel, and slightly steeper** (10Y/30Y lead the 2Y by 6–7bp). The two front-end days (9/23, 9/28) alternate with long-end days (9/24, 9/25). BOND's earlier "long-end-led" framing (`KB-BND-340`) described 9/24–9/25; this note supersedes it as a description of the whole episode.
- **Base rate (2026, Treasury cell, session closes):** 2Y ≥ +10bp on **8 of 185 sessions (4.3%)**, and **3 of the 8 are in September** (9/10 +13, 9/23 +14, 9/28 +11). The others: 3/12, 3/26, 6/5, 6/17, 8/28 (Warsh at Jackson Hole). 2Y 4.92 = the 2026 high close, and the highest since 2024-05-30.

## 3 · What it means for BOND
- **Regime line confirmed, not changed:** C-36's policy-path channel is ALIVE (THESIS v1.2.7). The episode carries **both** legs, path days and long-end days, so neither the "all term premium" nor the "all Fed" story fits alone.
- **Matrix:** no row moves (14/35). Front-end repricing is not an auction or dealer-mechanism signal.
- **Position (TLT Sep-30 77P ×20):** the long end rose less than the front today (+7). Expiry is 9/30 and on TERRY's rail; no BOND action.
- **Next tests land on this exact part of the curve:** Aug PCE (Wed 9/30 8:30) and Sept payrolls (Fri 10/2 8:30). The 10/28 FOMC curve-shape prediction (owed by 10/21) should key on the **terminal/1y1y**, since the October meeting itself is ~⅔ priced and moved least.
- **Ownership:** macro data → rate expectations is HENRY's; funding is LIQUID's; the foreign front-end question is ZHAO's. No packet (steady state, not 🔴-acute).

## Re-test triggers
- FRED DGS2/DGS1 9/28 (publishes ~9/29): paste-check against the Treasury cells above.
- Settlement-price fed funds/SOFR futures for 9/25 and 9/28 (CME), to decide the cash-vs-futures gap.
- A named 9/28 driver from a readable primary or wire.
