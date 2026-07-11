# MOVE-Led Vol-Hedge Fresh Look — 2026-07-11 (Sat, weekend; all levels Fri-close vintages)

**Trigger:** Will-approved execution of the fresh look queued since 7/10 (PROME canon), scoped in `reports/2026-07-11_domain-sweep.md` §3. **Context ruling stands:** GATE-VIO-110 (VIX-calls tail hedge) = LAPSED (Will, 7/9); any hedge that re-opens is rates-vol/duration-shaped (TERRY's construction lane). This memo is the vol read + registered conditions. **NO trade recommendation is made here.**

**KB row:** KB-VIO-116. **Author:** VIOLET. **Written:** 2026-07-11 ~15:45 ET.

---

## 1. HEADLINE FINDING — the queued premise is stale: MOVE REVERSED

The queued fresh look was premised on "MOVE 72.41 [7/8], 3 sessions up, unreversed." That was true as of VIOLET's 7/9 ~14:30 ET session (no 7/9 tick was publishable yet). It is no longer true:

| Date | MOVE close | Δ | Source/verification |
|---|---|---|---|
| 7/6 | ~65.4–65.8 | base | yf history + 1h bars [7/9 session, web cross-checked investing.com/CNBC] |
| 7/7 | 70.25 | +6.8% | same chain, web-verified 7/9 session |
| 7/8 | **72.41** | +3.1% — **cycle peak** | same chain, web-verified 7/9 session |
| 7/9 | **68.89** | **−4.9% — streak BROKEN** | yf fast_info prev_close + 1h intraday bars, this session |
| 7/10 | **69.55** | +1.0% partial rebound | yf fast_info last_price, this session; **independently converged by PROME's FORGE `fetch.py price ^MOVE` pull (69.55 [7/10]), same day** |

**Verification chain (like-for-like, per PROME's cross-source caution):** all five prints come from the same Yahoo/yfinance feed family. Yahoo's ^MOVE daily-history rows are sparse/lag-labeled (daily rows end 7/2 = 65.40), so the reconstruction uses the 1h intraday step-series (65.40 → 65.76 → 70.25 → 72.41 → 68.89 as last-of-day values 7/6–7/10) reconciled with fast_info (last 69.55 / prev 68.89) under ICE's known T+1 posting pattern. Two date-label models exist (±1 day on the last prints); **both agree on the ordinal fact**: peak 72.41 → drop to 68.89 → Friday value 68.9–69.6, i.e. **−4.0 to −4.9% off the peak, ~40–50% retrace of the whole 65.4→72.41 climb**. The 7/7=70.25 / 7/8=72.41 anchor was web-cross-checked (investing.com, CNBC) in the 7/9 session; PROME's independent FORGE pull converges on 69.55 [7/10]. Weekend web re-verification attempted this session (CNBC, MacroMicro, streetstats) — all 403/JS-walled; residual risk is the ±1-day date labeling only, not the reversal itself.

*(Tooling note: FORGE `fetch.py price ^MOVE` now works for future pulls — sparse-history caveat stands. VIOLET's own repeatable-pull wiring, SCRATCH item #5, remains open; use the 1h-bar + fast_info method above until scripted.)*

## 2. Friday-close tape — both sides of the divergence, stamped

| Metric | 7/9 close | 7/10 close | Read |
|---|---|---|---|
| MOVE | 68.89 | 69.55 | Reversed off 72.41 peak; still +6% above the 65.4 base — elevated, no longer escalating |
| VIX | 15.84 | **15.03** | Below the pre-war-night level (16.13 [7/7]) — full round-trip and then some |
| VIX9D | 12.50 | **11.15** | VIX9D/VIX **0.742** — front-end maximally calm into CPI week |
| VIX3M | 18.99 | 18.57 | VIX3M/VIX **1.236** — steepest contango of the cycle (7/1: 1.155, 7/9: 1.199) |
| VVIX | 88.78 | 87.28 | Well under the 100/120 lines, falling |
| SKEW | 144.67 | **144.27** | **Two consecutive closes <145** (first sub-145 since 6/29's 144.46) — the yellow line is broken from below, tail bid still fading |
| Single-stock put/call | — | **0.71 [7/10]** | Record low (10-yr avg 12, 2020 peak 34) [WALTER SIG-W-20260709-015] |

All above: yfinance daily history + fast_info, pulled 2026-07-11 ~15:35 ET (weekend — nothing live). **Vintage correction:** the canon stamp "SKEW 144.67 [7/10]" is off by one day — 144.67 was the **7/9** close; 7/10 closed **144.27**. Same direction, marginally deeper.

**Not pullable this weekend (registered gaps):** COT VIX 7/10 report (first post-shock positioning read — boot-time `cftc_cot.py` next session); fresh CCC/dispersion prints for 7/9–7/10 (FRED T+1, post ~7/13-7/14); GEX flip band (EXPIRED per HENRY 7/10 — repull owed 7/14 AM); M1:M2 futures settle.

## 3. Is this a genuine cross-instrument setup? — the answer changed shape

**The acute divergence (the thing that was queued) is NO longer live.** The setup as queued was: rates-vol rising unreversed while equity-vol round-trips — two instruments actively moving apart. MOVE's −4.9% break on 7/9 ended that. Rates-vol blinked first, consistent with the broader cooling root PROME flags (truce-collapse premium unwinding: energy DENY, JPY covering, calm HY).

**What remains is a LEVEL configuration, not a momentum divergence:**
- MOVE at 69.55 is still +6% above its pre-refunding base (65.4) — the rates-vol complex kept *some* of the auction-week repricing; it did not round-trip the way VIX did.
- The equity side is at cycle-calm extremes on *every* gauge simultaneously: VIX 15.03, VIX9D/VIX 0.742, contango 1.236 (cycle-steepest), VVIX 87.3, SKEW sub-145 two days running, and single-name downside hedging at a **record** low (0.71).
- **The WALTER single-stock/index split ask, answered:** single-name put/call 0.71 (record low) against index SKEW 144.27 (still elevated historically, but 10.5pts off the 7/1 cycle high and now under its own yellow line) = the two-tier hedge structure of KB-VIO-108 (wings-rotation: index-tail bid held while single-name protection was abandoned) is now **unwinding from both ends** — the index tail bid is fading toward the single-name floor rather than the split widening. That is complacency **deepening and broadening**, not hedged-resilience rotating.

**Verdict:** this is a **cheap-convexity-into-a-hard-catalyst configuration, not a stress-transmission signal.** Nothing is transmitting right now — MOVE's reversal removed the one actively-moving leg. But the price of being wrong has rarely been lower on the equity surface (record-low single-name protection, sub-145 SKEW, cycle-steepest contango), and the catalyst is dated and compound: **CPI 7/14 + Citigroup & Wells Fargo Q2 the same morning** (JPM 7/15), with the gamma band EXPIRED (unknown cushion) and Gate B (CPI gamma-tripwire, HENRY) re-arming exactly there.

## 4. What a hedge expression would LOOK like (shape only — TERRY owns construction)

Per Will's 7/9 ruling, the lane is **rates-vol/duration-shaped, not VIX-calls**:

- **Instrument class:** long rates-vol convexity / duration-tail expression (payer-swaption-shaped, or listed proxies: TLT puts / TLT put spreads; TERRY's live card from the 7/9 disposition is the vehicle reference). The rationale for the lane is unchanged: the standing wrong-instrument caveat (KB-VIO-112/115) — a rates/oil-class shock shows in MOVE before VIX, and the positive-gamma cushion dampens the equity leg only for *level* moves, not rate shocks.
- **Why NOT VIX-calls, even at these prices:** the equity surface is cheap *because* the transmission channel doesn't run through it first. A VIX expression pays only on the second leg (equity gap through the flip band); the first leg is rates. Cheapness alone doesn't fix the instrument mismatch that GATE-VIO-110's postmortem established.
- **The equity-side caveat worth carrying:** record-low single-name hedging (0.71) means if the second leg DOES arrive, there is no private cushion under single names — amplification, not absorption. That argues any second-leg equity expression is a *follow-on* decision keyed to HENRY's re-pulled flip band on 7/14 AM, not something to pre-build now.

## 5. REGISTERED CONDITIONS (pre-CPI, falsifiable, adjudicate at next session)

**FIRE — re-open the hedge conversation (route: PROME → TERRY for construction; still requires Will [Approve] on any packet):**
- **F1:** MOVE closes **> 72.41** (re-takes the cycle peak) on any session through CPI+1 (7/15). The reversal thesis is wrong; rates-vol escalation resumed into the catalyst.
- **F2 (CPI-day compound):** hot CPI **and** SPX gaps below HENRY's re-pulled 7/14 AM flip band (Gate B re-arm — negative gamma amplification live) — this is the second-leg trigger, and it fires the *equity-side follow-on* question, not just the rates-vol one.
- **F3 (rates leg without CPI):** 10Y through **4.60** with MOVE > 70 before 7/14 (auction-tail/term-premium resumption independent of the print).

**NO-FIRE / stand down (divergence resolved benign):**
- **N1:** MOVE closes **< 66** (round-trip to the pre-refunding base) — the whole auction-week repricing unwinds; the level configuration collapses to plain calm.
- **N2:** SKEW recovers **> 148** with VIX bid (re-hedging = normalization of the complacency extreme — removes the cheap-convexity rationale from the equity side).

**CPI 7/14 branch map:**
- **In-line/cool CPI:** expect MOVE fade toward N1; complacency extends; this channel produces no hedge case — attention rotates to the 7/22–7/29 megacap earnings stack (VULCAN S1 seam, Path-B).
- **Hot CPI:** F2/F3 territory. Watch order: MOVE/10Y first (the leading instrument), flip band second, VIX complex last (it will be the *lagging* confirmation, per the whole point of this cycle's caveat).
- **Either branch:** COT 7/10 + fresh CCC/dispersion prints (postable 7/13-7/14) grade the positioning/credit context before the print lands — first pulls of the next session.

**Today's disposition: NO-FIRE.** The acute divergence broke benign-side on 7/9 (MOVE reversal = the exact no-fire condition pre-scoped in the sweep §3). The level configuration + record complacency extremes + dated compound catalyst justify the registered conditions above — not a packet.

---

*Sources: yfinance (^MOVE, ^VIX, ^VIX9D, ^VIX3M, ^VIX6M, ^VVIX, ^SKEW — daily history + fast_info + 1h bars), pulled 2026-07-11 ~15:35 ET; MOVE 7/7-7/8 anchor web-verified in the 7/9 session (investing.com, CNBC); PROME FORGE convergence pull 7/11 (69.55 [7/10]); single-stock put/call 0.71 [7/10] via WALTER SIG-W-20260709-015 (BOARD ref within). Weekend memo — no level herein is live.*
