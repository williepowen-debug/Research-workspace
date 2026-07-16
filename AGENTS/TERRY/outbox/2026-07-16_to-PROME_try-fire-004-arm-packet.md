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

## 3. ⚠️ LIVE OPTION MARKS UNAVAILABLE via tool — broker chain required (rule #4). Reference = 7/15 close.
**Re-pulled live at 09:45 ET (15+ min post-open, `--no-cache`) — still no live NBBO.** Diagnostic run confirms a **yfinance feed limitation, not timing/illiquidity:**
- **0 puts** have a 2026-07-16 trade; **ATM bid/ask = 0.00** on even the 56k-OI 83 put and 14k-OI 84 put; `fast_info` TLT spot returns `None`. Only 1 of 23 strikes shows any nonzero quote.
- ⇒ **The tool cannot produce fillable intraday marks today. Live marks REQUIRE Will's broker chain (rule #4).**

**Reference basis = 7/15 prior-session CLOSE (lastPrice), ~1 day stale.** The ATM ladder is clean and monotonic (80=$0.23 · 81=$0.35 · 82=$0.57 · 83=$0.84 · 84=$1.27), so these are real closing marks, usable as a *reference* (NOT a fill). Target 8–12% OTM strikes:

| Strike | Mny% (@83.81) | 7/15 close (ref) | LastTrade [vol] | OI | Reliability |
|---|---|---:|---|---:|---|
| 77 P | −8.1% | **$0.09** | 7/15 [vol 5,050] | 54,506 | good — heavily traded 7/15 |
| 76 P | −9.3% | $0.07 | 7/15 [vol 15] | 2,661 | fair — thin |
| 75 P | −10.5% | $0.05 | 7/15 [vol 23] | 30,195 | fair — thin |
| 74 P | −11.7% | $0.05 | 7/10 [vol 3] | 3,674 | stale (7/10) |

**77 P ($0.09, 7/15) is the most reliable reference** (the day's most active). TLT is −0.51% today → live put marks likely a touch *higher* than the 7/15 ref (fewer contracts per $500). **Confirm the live bid/ask on Will's broker before any fill** — at penny premiums a 1–2¢ difference swings contract count ±20–40%.

## 4. Structure (pre-locked in ZONE 1 — honored)
- **Instrument:** TLT puts, outright. **Expiry: 2026-09-18** (Sep monthly; captures the July-CPI/TIC window + buffer, 63 DTE).
- **Strike ladder (8–12% OTM at TLT 83.80):** **74 / 75 / 76 / 77** puts.
  - Best listed liquidity: **77 P** (OI 54.5k, today's most active) and **75 P** (OI 30k).
- **Rationale (card ZONE 1):** convex expression of a term-premium/inflation duration shock; beats outright TLT short (unbounded/margin) and long-dated puts (wrong tenor for a velocity catalyst).

## 5. Sizing ($500 max-loss cap; contracts = floor(500 / (mark × 100)))
Defined-risk — max loss = premium paid, hard-capped $500. **Sized off the 7/15 reference (§3); re-run `risk_calc.py --premium <live_broker_mark> --max-loss 500` at fill:**

| Strike | Ref mark [7/15] | Contracts @ ref | Cost @ ref | Note |
|---|---:|---:|---:|---|
| **77 P** (rec) | $0.09 | **55** | $495 | most reliable ref; best OI/liquidity |
| 76 P | $0.07 | 71 | $497 | thin recent volume |
| 75 P | $0.05 | 100 | $500 | thin; penny-sensitive |

**Live-mark sensitivity (why the broker mark matters):** if today's live 77 P prints $0.11 → 45 contracts ($495); $0.13 → 38 ($494). TLT −0.5% today pushes puts up, so expect *fewer* than 55. **Structural read:** each 8–12% OTM contract is low-delta (~5–10Δ) — this is a **convex tail bet** (cheap, low hit-rate, needs a ≥8–12% TLT move to ~74–77 by Sep 18). 55× the 77 P ≈ ~300–550 share-equiv of short-TLT delta = a defined-risk lottery on a duration shock, not a core short.

## 6. Decision context — what changed since the card was scoped (goes IN, doesn't veto the arm)
- **June CPI (7/14) printed COOL** — headline −0.42% MoM (outright deflationary month), core −0.02% [FRED CPIAUCSL/CPILFESL] — **yet the 10Y HELD the 4.50 line** (4.62 pre-print → 4.58 post). This is the bull case for the *re-scoped* thesis: yields sustaining despite a cool print = **term premium, not inflation expectations**. The demand-hole leg was already refuted (7/9 auction); this is the term-premium/inflation-channel card.
- **BOND rates decomposition (co-grade memo 7/16) — WHY the line held is quantified: it's an 86%-REAL-yield move.** DGS10 = DFII10 (real) + T10YIE (breakeven); the +14bp 7/6→7/13 climb above 4.50 was **+12bp DFII10 (real, 86%)** vs **+2bp breakeven (14%)**, with 5Y5Y forward inflation dead-anchored at 2.21. A cool backward CPI *can't* break a line that inflation expectations weren't holding up. DFII10 at **2.36 [7/13]** = series high, ~14–17bp under BOND's 2.50 real-stress re-arm. Front end co-moved (**2Y +13bp through the deflationary print**) = hawkish-hold pricing, not cuts-sooner. **Directional support for the trade.**
- **The oil shock loads the JULY print, not June** — Hormuz closed 7/11–12, Brent ~$71→$86 (≈+21%) ≈ **+0.4–0.6pp to July headline MoM from gasoline alone** (BOND), releasing ~mid-Aug (after FOMC 7/28–29, which nonetheless sees Brent $86 + Hormuz closed feeding the inflation-risk premium). This is the inflation leg the card was re-scoped to. **BOND verdict: 4.50-sustain through FOMC is WELL-SUPPORTED; main falsifier = fast Hormuz de-escalation → Brent retrace → DFII10 eases back to the line.** That falsifier is the trade's key thesis-invalidation to watch.
- **Rates-vol round-tripped, it didn't just fade:** MOVE 1h-bars show **69.55 [7/13] → 77.77 [7/14 CPI day, above the 72.41 cycle peak] → 75.03 [7/15] → 68.48 [7/16 live]** (±1-day label caveat per VIOLET). The vol event **already happened around CPI and has deflated** — which is a tailwind for *buying* puts now (IV coming off), but a headwind for the acute-catalyst framing (the CPI catalyst has passed).
- **Next catalysts:** (a) **May TIC today 4:00 PM ET** = arm-#3 (grading template pre-staged, see companion file); (b) the **JULY CPI (mid-Aug)** now carries the Hormuz/Brent oil shock (Brent ~$86 [7/16]) — the inflation leg the card was re-scoped to. Sep-18 expiry covers both.

## 7. Why-not / counter-trade (the honest TERRY case against filling *today, as structured*)
1. **Entry breaks rule #6 (puts on green days).** TLT is RED (−0.52%) and at **range lows** — buying puts here chases the breakdown. Cleaner entry: wait for a green TLT bounce toward **84.2–84.5** to buy without chasing. *Partial offset:* the vol axis is favorable (MOVE 77→68.48 = IV deflating), so puts are cheaper on vol even as spot falls. Net: prefer scaling / a green-day fill over a market-open chase.
2. **Primary acute catalyst already passed** (CPI 7/14, cool). The next dated driver is diffuse (mid-Aug July CPI); Sep expiry has time but the near-term convex catalyst is gone until TIC (today 4pm) / next CPI.
3. **Deep-OTM structure is a low-delta lottery ticket** needing a ≥8–12% TLT move by Sep. For a *term-premium grind* (not a crash), a closer strike (80–81 P, 3–5% OTM) or a **put debit spread** would express the view with more delta per dollar. The card pre-locked 8–12% OTM — I honor it as primary but flag the spread/closer-strike alternative as worth Will's consideration.
4. **Position truth is OFF-repo (rule #4).** `[POSITION_STATE_UNKNOWN]` — Will must confirm no existing TLT/duration exposure that this doubles or offsets (note the VIO-116 rates-vol hedge lands in the *same lane* — see companion memo; avoid double-counting duration-short risk).

## 8. Execution checklist (must all be TRUE before fill)
- [ ] Arm-#2 fired — **YES (verified §1)**
- [ ] Live option marks pulled <15 min old — **NO — tool can't serve live TLT option NBBO (re-pulled 09:45 ET, still 0.00; §3). Will's broker chain required.**
- [ ] Green/red check (rule #6) — **RED day (TLT −0.51% @09:45), flagged (§7.1)**
- [ ] Liquidity OK (77/75 P deep) — pending live spread confirm
- [ ] Max loss ≤ $500 — **YES (defined-risk, §5)**
- [ ] Position truth known — **NO → Will's broker book required**

## Decision
**Terry verdict: CONDITIONAL.** The arm is executed as registered. To fill: (a) re-pull live marks, (b) confirm no conflicting book, (c) prefer a green-day / scaled entry over chasing today's red open, (d) consider spread/closer-strike if expressing a grind rather than a tail.

[ ] APPROVE (fill per §4–5 at live marks)  [ ] APPROVE-MODIFIED (spread / closer strike / green-day scale)  [ ] REJECT / HOLD

**APPROVAL REQUIRED — Will must approve/reject before execution. TERRY never executes.**
