# ARM PACKET → PROME → Will [Approve] — TRY-FIRE-004 (TLT duration-short / puts)
**From:** TERRY · **Date:** 2026-07-16 (~09:35 ET, markets open) · **Gate:** GATE-TERRY-ARM2 = FIRED (arm-#2 5-of-5 completed Mon 7/13)
**Consequence executed:** arm-#2 fired → TERRY arms TRY-FIRE-004 → **this packet → Will [Approve] + live broker book.**
**Terry verdict:** **CONDITIONAL — armed as registered; NOT a chase-it-now recommendation.** Fill discipline + live marks caveats below.
**Confidence in trade structure:** LOW/contingent (readiness, not a lean — per the card's standing disposition).

---

## 0. Pre-registration note (why this packet exists at all)
Arm-#2 (VX-BND-05 10Y-sustain) is a **pre-registered gate**. It fired; the registered consequence is that I arm the card and hand Will a packet. **The arm executes as registered** — the new context below (cool June CPI, MOVE round-trip, TLT at range lows) goes IN the packet as decision context, **not** as a reason to skip the arm. Whether Will *fills* is a separate decision this packet informs.

## 1. Independent arm-#2 verification (FRED DGS10 direct, pulled 2026-07-16 ~09:31 ET)
Semantics applied per BOND co-ratification (2dp DGS10, ≥ inclusive, holidays neither count nor reset, official governs over ^TNX).

| Date | DGS10 (official) | ≥4.50? | Consecutive count |
|---|---:|---|---|
| 7/6 | 4.48 | NO | 0 (reset) |
| 7/7 | 4.55 | YES | 1 |
| 7/8 | 4.56 | YES | 2 |
| 7/9 | 4.54 | YES | 3 |
| 7/10 | 4.56 | YES | 4 |
| **7/13** | **4.62** | YES | **5 ✅ COMPLETE** |
| 7/14 | 4.58 | YES | 6 (streak intact) |

**Verdict: 5-of-5 CONFIRMED, HIGH confidence. Matches PROME/BOND exactly.** 7/3 holiday ("." in FRED) correctly neither counted nor reset. Streak still live through 7/14 (arm-#2 has not disarmed — no close <4.50). Consumer note: the 7/8 official is **4.56** (the 4.57 in some older artifacts was a ^TNX read — count-neutral).

## 2. Live tape (pulled 2026-07-16 ~09:32–09:35 ET, FORGE fetch.py)
| Instrument | Level | Δ vs prev | Read |
|---|---:|---|---|
| TLT | **$83.80** | −0.52% | RED day; at/near **low of 6-day range** (84.49 [7/9] → 83.80) |
| 10Y (^TNX) | 4.59 | +0.9% | above the 4.50 sustain line, pushing higher — thesis moving in real time |
| 30Y (^TYX) | 5.12 | +0.65% | term-premium channel live |
| MOVE (^MOVE) | 68.48 | — | rates-vol round-tripped: spiked **77.77 [7/14 CPI day, 1h-bar]** then faded (see §6) |
| VIX | 16.17 | +3.19% | still cycle-calm |

**TLT 6-session tape:** 84.36 (7/8) · 84.49 (7/9) · 84.47 (7/10) · 83.97 (7/13) · 84.08 (7/14) · 84.24 (7/15) · **83.80 (7/16)**. Grinding lower; today gapped down and sits at range lows.

## 3. ⚠️ LIVE OPTION MARKS NOT AVAILABLE (rule #4 blocker — read before sizing)
At 09:32 ET the TLT Sep-18 put chain (yfinance, `--no-cache`) returns **bid/ask = 0.00 across all strikes**, last-trades stamped **7/15** (yesterday), and a **broken IV field (6.25% floor)**. Options have not traded today yet (first minutes after open). **These are NOT fillable marks.** Stale last-prices below are indicative only:

| Strike | Moneyness | Stale lastPrice [7/15] | OI | Vol |
|---|---|---:|---:|---:|
| 77 P | −8.1% | $0.09 | 54,506 | 5,050 |
| 76 P | −9.3% | $0.07 | 2,661 | 15 |
| 75 P | −10.5% | $0.05 | 30,195 | 23 |
| 74 P | −11.7% | $0.05 | 3,674 | 3 |

The penny prints + broken IV are **not trustworthy** (a Sep 63-DTE 8% OTM TLT put on realistic ~12–14% IV should be worth materially more than $0.09). **REQUIREMENT: pull a live chain once options trade today (re-run `chain_fetch.py TLT 2026-09-18 --type put --no-cache`, ~15–30 min post-open) OR read Will's live broker chain BEFORE any fill.** Sizing below is a formula, not a filled number.

## 4. Structure (pre-locked in ZONE 1 — honored)
- **Instrument:** TLT puts, outright. **Expiry: 2026-09-18** (Sep monthly; captures the July-CPI/TIC window + buffer, 63 DTE).
- **Strike ladder (8–12% OTM at TLT 83.80):** **74 / 75 / 76 / 77** puts.
  - Best listed liquidity: **77 P** (OI 54.5k, today's most active) and **75 P** (OI 30k).
- **Rationale (card ZONE 1):** convex expression of a term-premium/inflation duration shock; beats outright TLT short (unbounded/margin) and long-dated puts (wrong tenor for a velocity catalyst).

## 5. Sizing framework ($500 max-loss cap, rule: contracts = floor(500 / (mark × 100)))
Fill the mark column at live-pull time; the position is defined-risk (max loss = premium paid, hard-capped $500):

| If live mark = | Contracts (≤$500) | Actual $ at risk |
|---:|---:|---:|
| $0.10 | 50 | $500 |
| $0.20 | 25 | $500 |
| $0.30 | 16 | $480 |
| $0.50 | 10 | $500 |

`risk_calc.py --premium <live_mark> --max-loss 500` at fire. **Max loss cannot exceed premium paid.** Note: at deep-OTM strikes each contract is low-delta (~5–10Δ), so this is a **convex tail bet** — cheap, low hit-rate, needs a large TLT move (≥8–12% to Sep) to pay.

## 6. Decision context — what changed since the card was scoped (goes IN, doesn't veto the arm)
- **June CPI (7/14) printed COOL** — headline −0.42% MoM (outright deflationary month), core −0.02% [FRED CPIAUCSL/CPILFESL] — **yet the 10Y HELD the 4.50 line** (4.62 pre-print → 4.58 post). This is the bull case for the *re-scoped* thesis: yields sustaining despite a cool print = **term premium, not inflation expectations**. The demand-hole leg was already refuted (7/9 auction); this is the term-premium/inflation-channel card.
- **Rates-vol round-tripped, it didn't just fade:** MOVE 1h-bars show **69.55 [7/13] → 77.77 [7/14 CPI day, above the 72.41 cycle peak] → 75.03 [7/15] → 68.48 [7/16 live]** (±1-day label caveat per VIOLET). The vol event **already happened around CPI and has deflated** — which is a tailwind for *buying* puts now (IV coming off), but a headwind for the acute-catalyst framing (the CPI catalyst has passed).
- **Next catalysts:** (a) **May TIC today 4:00 PM ET** = arm-#3 (grading template pre-staged, see companion file); (b) the **JULY CPI (mid-Aug)** now carries the Hormuz/Brent oil shock (Brent ~$86 [7/16]) — the inflation leg the card was re-scoped to. Sep-18 expiry covers both.

## 7. Why-not / counter-trade (the honest TERRY case against filling *today, as structured*)
1. **Entry breaks rule #6 (puts on green days).** TLT is RED (−0.52%) and at **range lows** — buying puts here chases the breakdown. Cleaner entry: wait for a green TLT bounce toward **84.2–84.5** to buy without chasing. *Partial offset:* the vol axis is favorable (MOVE 77→68.48 = IV deflating), so puts are cheaper on vol even as spot falls. Net: prefer scaling / a green-day fill over a market-open chase.
2. **Primary acute catalyst already passed** (CPI 7/14, cool). The next dated driver is diffuse (mid-Aug July CPI); Sep expiry has time but the near-term convex catalyst is gone until TIC (today 4pm) / next CPI.
3. **Deep-OTM structure is a low-delta lottery ticket** needing a ≥8–12% TLT move by Sep. For a *term-premium grind* (not a crash), a closer strike (80–81 P, 3–5% OTM) or a **put debit spread** would express the view with more delta per dollar. The card pre-locked 8–12% OTM — I honor it as primary but flag the spread/closer-strike alternative as worth Will's consideration.
4. **Position truth is OFF-repo (rule #4).** `[POSITION_STATE_UNKNOWN]` — Will must confirm no existing TLT/duration exposure that this doubles or offsets (note the VIO-116 rates-vol hedge lands in the *same lane* — see companion memo; avoid double-counting duration-short risk).

## 8. Execution checklist (must all be TRUE before fill)
- [ ] Arm-#2 fired — **YES (verified §1)**
- [ ] Live option marks pulled <15 min old — **NO (blocked, §3) → re-pull required**
- [ ] Green/red check (rule #6) — **RED day, flagged (§7.1)**
- [ ] Liquidity OK (77/75 P deep) — pending live spread confirm
- [ ] Max loss ≤ $500 — **YES (defined-risk, §5)**
- [ ] Position truth known — **NO → Will's broker book required**

## Decision
**Terry verdict: CONDITIONAL.** The arm is executed as registered. To fill: (a) re-pull live marks, (b) confirm no conflicting book, (c) prefer a green-day / scaled entry over chasing today's red open, (d) consider spread/closer-strike if expressing a grind rather than a tail.

[ ] APPROVE (fill per §4–5 at live marks)  [ ] APPROVE-MODIFIED (spread / closer strike / green-day scale)  [ ] REJECT / HOLD

**APPROVAL REQUIRED — Will must approve/reject before execution. TERRY never executes.**
