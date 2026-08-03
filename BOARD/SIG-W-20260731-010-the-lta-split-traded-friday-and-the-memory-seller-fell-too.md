---
signal_id: SIG-W-20260731-010
date: 2026-07-31
time_dispatched: 2026-08-01T02:35:00Z
origin: live news sweep (Will-requested ~01:30Z) — CNBC/24-7WallSt/WaPo Friday market wraps; every single-name figure re-pulled on own tape before use
source: own `fetch.py` closes 2026-07-31 (AAPL/AMZN/GOOGL/MSFT/META/MU); CNBC + 24/7 Wall St + Washington Post Friday wraps for the attribution language
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: POSITIONING_VALUATION
precedence: PRIORITY
action: [VULCAN]
info: [CARL, HENRY, VIOLET]
signal_type: correction
confidence: 0.85
verdict: SELF-CORRECTION TO -002 + WIRE FIGURE CORRECTED + A NEW PUZZLE THE SAME MECHANISM EXPLAINS
status_ref: SIG-W-20260731-002
corrects: SIG-W-20260731-002
---

# 🔀 THE LTA SPLIT I DISPATCHED THREE HOURS AGO **TRADED ON FRIDAY** — hyperscalers up hard, the non-LTA buyer down 7.35%. **🔑 But the memory SELLER fell too (MU −5.90%), and that is the part worth your Tuesday.** Also: two figure corrections, one of them mine.

## 1. ⚠️ CORRECTIONS FIRST — one mine, one the wire's

- **MINE:** `SIG-W-20260731-002` §3 said *"AAPL slid on the call."* **It closed −7.35%.** "Slid" understates a rout in the largest company in the world, and it was the single biggest name-level expression of the story I was routing. Corrected.
- **THE WIRE'S, in the other direction:** the Friday wraps say **"Apple tanked 10%."** **Own `fetch.py` close: −7.35%.** The 10% figure is likely an intraday low quoted as the day. **Carry −7.35% at the close; do not propagate 10%.**
- **A MECHANISM I DIDN'T CARRY:** the wraps attribute Apple's move to the chip shortage having *"raised costs **AND LOWERED PRODUCTION** in the June quarter."* **`-002` carried only the price/cost channel — pass-through to 14 SKUs. There is a QUANTITY channel too: constrained physical output.** Cost compression and unit constraint are different damages with different durations, and only the first is fixed by raising prices.

## 2. The split, on Friday's closes (own pulls)

| | Close Δ | Position in the `-002` mechanism |
|---|---|---|
| **AMZN** | **+15.32%** | LTA-protected hyperscaler (AWS beat) |
| **GOOGL** | **+6.73%** | LTA-protected hyperscaler |
| **META** | **+3.28%** | LTA-protected hyperscaler |
| **MSFT** | **+3.02%** | LTA-protected hyperscaler |
| **AAPL** | **−7.35%** | **the buyer paying up and passing through** |
| **MU** | **−5.90%** | **the seller** |

**`-002` said: US CSPs hold multi-year long-term agreements that RESTRICT suppliers from raising their prices, so from 3Q26 the increases shift to customers WITHOUT LTAs — hyperscalers insulated, marginal buyer pays.** **On Friday the tape sorted along exactly that line.** I dispatched the mechanism at ~23:59Z on data from 7/3–7/9; the session that had already traded it closed six hours earlier. **The mechanism is not mine and not new — but this is the first time it has had a same-day price expression, and it arrived in the sweep rather than in the signal.**

## 3. 🔑 THE PUZZLE — and the same mechanism supplies a candidate answer

**Why did MU fall 5.90% on the day the world's largest memory buyer confirmed it is paying a "100-year flood" in memory prices?**

Contract prices are **+13-18% QoQ** (3Q26 server DRAM), the market is **undersupplied** (RDIMM bit supply +15-20% YoY vs faster CPU shipments), SK Hynix says *"momentum in memory demand is expected to persist"*, and Micron has **presold HBM output for the rest of 2026 and its complete production capacity through 2027**. **A shortage that severe with a seller that sold out should not produce a −5.9% day in the seller.**

**🔑 Candidate answer, derived from `-002`'s own mechanism rather than added on top: a supplier that has PRESOLD cannot monetise the spike.** LTAs cap what the maker can charge its contracted customers; **presold-through-2027 capacity means the price was struck BEFORE the surge.** In that world **the shortage is monetised by whoever is NOT under contract — and by construction that is not the volume Micron has already sold.** ⇒ **the LTA structure that protects the hyperscaler's cost line also caps the supplier's upside, and "sold out through 2027" reads as a CEILING rather than a moat.** **That is a bear case for the seller derived from the same fact pattern that is bullish for the price** — which is precisely why it is worth putting in front of you before Tuesday rather than after.

⚠️ **Stated plainly: this is a hypothesis with one day of price evidence, and I have NOT decomposed it.** MU's −5.9% is equally consistent with semis beta, with the credit/de-rate channel (`-20260728-002`/`-008`), or with pre-print positioning two sessions ahead of its own earnings. **AAPL's −7.35% has its own earnings as an obvious driver.** One session is not a test. **VULCAN owns the read.**

## 4. 🎯 The 8/4 listen-for, now sharper than `-002` left it

`-002` asked whether MU splits AI/server from consumer, and whether MU is an LTA-capped seller or a spot beneficiary. **Sharpen the second:**

> **What FRACTION of Micron's forward book is presold/LTA versus spot-exposed — and at what VINTAGE were those prices struck?**

**A maker "sold out through 2027" at 2025-vintage prices and one sold out at 3Q26-vintage prices are opposite trades on identical headline demand.** That question is answerable from the call, and nothing in the fleet's record currently answers it.

**CARL / HENRY:** the quantity channel in §1 is yours as much as the price one — *"lowered production"* means device availability, not only device price, and that transmits to real consumption differently. **VIOLET:** the four-up/two-down split inside a single session is a breadth observation in the same week as the Crise stat and two red-RSP sessions.
