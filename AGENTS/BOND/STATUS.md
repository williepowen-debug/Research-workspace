# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure
**State:** 🟡 WATCH — June refunding **cleared**; long-end episode relaxed. "Expensive, not broken" held. Re-armable at the 6/16 20Y / 6/17 FOMC.
**Last Updated:** 2026-06-15 ~live by BOND (post-June-refunding refresh + thesis/ migration)
**Thesis:** full durable thesis, transmission channels, exit rules, position view → `thesis/THESIS.md` (v1.0)

---

## Regime (one-line)

The bond market is **clearing at price** — the May–June long-end term-premium episode (BND-07) relaxed post-refunding; macro credit calm but bifurcating underneath (CCC/energy); credit-leads-equity inactive. **Composite 11/35** (↓ from 12 on 6/9 — long-end/duration 3→2). Full read: `thesis/THESIS.md`.

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| HY OAS | **271bps** | 🟢 | FRED `BAMLH0A0HYM2`, 6/12 | −4 vs 6/8; calm held through refunding. **Caveat: top-only** — CCC/energy out of the calm. |
| CCC OAS | **948bps** | 🟡 | FRED `BAMLH0A3HYC`, 6/12 | ~flat; bifurcation didn't widen but didn't heal. Above-900 watch. |
| IG OAS | **74bps** | 🟢 | FRED `BAMLC0A0CM`, 6/12 | −1; market functional. |
| 10Y yield | **4.47%** | 🟡 | yfinance `^TNX`, 6/15 | **Back below 4.5** (peaked 4.55 on 6/10 auction day, rallied to 4.45 on 6/11). |
| 30Y yield | **4.97%** | 🟡 | yfinance `^TYX`, 6/15 | **Back below 5.0** (5.03 on 6/10, 4.95 post-30Y-auction 6/11). |
| 5Y yield | **4.19%** | 🟢 | yfinance `^FVX`, 6/15 | Belly eased. |
| 2Y yield | **4.09%** | 🟢 | FRED `DGS2`, 6/12 | Front-end anchored. |
| TLT | **$85.75** | 🟢 | yfinance, 6/15 | +0.64 vs 6/9; duration relief as yields eased. |
| VIX | **16.1** | 🟢 | yfinance `^VIX`, 6/15 | **−5.1 vs 6/9 (21.2)** — Hormuz war-risk premium out (Brent −13%). Equity-vol, not credit. |
| KRE | **$72.17** | 🟢 | yfinance, 6/15 | +1.1; banks firm. |
| HYG | **$80.06** | 🟢 | yfinance, 6/15 | +0.5; no cash-credit transmission. |
| SOFR−IORB | **~0bps** | 🟢 | FRED `SOFR` 3.65 / `IORB` 3.65, 6/12 | No funding stress; refunding didn't strain repo. |
| 10Y TIPS (DFII10) | **2.16%** | 🟡 | FRED `DFII10`, 6/11 | −5bp off the 2.21 auction-day peak; real-rate pressure eased — the re-fire driver reversed. |
| 10Y breakeven (T10YIE) | **2.31%** | 🟢 | FRED `T10YIE`, 6/12 | −4bp; inflation premium easing (oil). |
| 5Y breakeven (T5YIE) | **2.39%** | 🟢 | FRED `T5YIE`, 6/12 | −8bp vs 6/8. |
| 5Y5Y fwd infl (T5YIFR) | **2.23%** | 🟢 | FRED `T5YIFR`, 6/12 | Inside band; anchored. |
| Energy HY OAS | *285 [STALE Apr 28]* | 🟡 | LIQUID owns | Do not refresh here — pull from LIQUID. Plausibly >300; re-check now that VIX/Brent eased. |
| Corp issuance YTD | *$1,013.9B/Apr, +28% YoY [STALE]* | 🟢 | SIFMA | Primary market not frozen; refresh May data from SIFMA. |

---

## Latest Auction Read — June refunding (cleared)

| Date | Tenor | Size | BTC | High Yield | Indirect | PD | Read (vs reopened May line) |
|---|---|---:|---:|---:|---:|---:|---|
| 6/9 | 3Y (new) | $58B | 2.64 | 4.192% | 63.4% | 15.2% | Solid front-end; PD take a touch elevated. Least informative of the three. |
| **6/10** | **10Y (reopen 5/12)** | $39B | **2.57** | 4.538% | **78.0%** | **9.4%** | **Strong** — vs 5/12 (BTC 2.40 / ind 64% / PD 12.0%) demand **improved** across the board; dealers barely absorbed. |
| **6/11** | **30Y (reopen 5/13)** | $22B | **2.33** | 5.020% | **59.8%** | 14.7% | **Soft but orderly** — vs 5/13 (BTC 2.30 / ind 66.6% / PD 11.7%) BTC ~flat, indirect **weaker**, PD higher. No demand hole; 30Y rallied 8bp same-day. |

**Read:** no stress markers. 10Y reopening was the standout (record-ish indirect, minimal dealer take); 30Y soft internals but BTC held >2.3 and cleared. **BND-08 resolves FALSE** (no demand hole; 30Y borderline — indirect 59.8% a hair under 60%, tail small-but-unpinned). Consistent with term-premium digestion — "expensive, not broken." *(Full May calendar archived in thesis/ + domain/.)*

---

## Convergence Matrix

| Vector | Score | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|
| Treasury auction health | 2 | 🟡 | June refunding cleared (10Y strong, 30Y soft-orderly); below-median but functional. | 2+ weak same-tenor OR >2bp tail at **6/16 20Y**. |
| HY market function | 1 | 🟢 | HY OAS 271 flat. Bifurcation caveat (CCC 948, energy HY stale via LIQUID). | HY >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | 🟢 | IG OAS 74; no freeze. | +20bps/wk OR clustered pulled deals. |
| Dealer absorption | **3** | 🟠 | FR2004 (5/27) long-end inventory near/at record — 11–21Y $67.0B all-time high (*stock*). June *flow* mixed (10Y PD 9.4% benign; 30Y/3Y ~15%). | Forced inventory decline in a selloff OR FR2004 fresh highs + weak auction. |
| Long-end / duration | **2** | 🟡 | **↓3→2.** 10Y 4.47 / 30Y 4.97 back below thresholds; real-rate move reversed (DFII10 2.21→2.16); auctions cleared. | 10Y >4.5 OR 30Y >5.0 held **5 sessions** WITH a weak auction or SOFR-IORB lift → back to 3. |
| CDX-cash basis | 1 | 🟢 | Proxy (`monitors/cdx_proxy.py`) no divergence at cash. | Proxy z20 < −1.5 while HY tight, OR VIOLET reports skew steepening. |
| Credit-equity lead | 1 | 🟢 | HY tight while VIX *fell* — equity-vol-led, setup inactive. | HY OAS +75–100bp from trough while VIX <20. |

**Composite: 11/35** (↓ from 12 on 6/9). Single driver: long-end/duration 3→2 as the June re-fire relaxed and the refunding cleared. Re-escalation watch **relaxed, not stood-down** — re-armable at the 6/16 20Y / 6/17 FOMC. HY "calm" carries the bifurcation caveat. Dealer-inventory stock is the one durable elevated vector.

---

## Trade Interface (full view in `thesis/THESIS.md`)

- **TLT puts — HOLD, no add.** June conditional-add gates lapsed **unfired** (auctions cleared, yields eased — adding here chases a relaxing move). Re-arm only on a real tail (>1.5bp + weak indirect) at the **6/16 20Y**, or 10Y/30Y back above thresholds 5 sessions. Cleaner vehicle than equity puts if duration re-engages.
- **HYG $75P Jun — salvage / near-expiry.** Zero transmission (HY 271, HYG firm). Reopen only on HY OAS >300 w/ velocity.
- **Credit-equity lead — inactive.** Reactivate on HY OAS +75–100bp from trough while VIX <20.

---

## Exit / Falsification (full set → `thesis/THESIS.md`)

- **Thesis kill (exit all duration shorts):** a genuine auction **demand hole** — BTC <2.3 **and** tail >2bp **and** dealer take spikes **and** SOFR-IORB turns positive. OR 10Y back below **4.15** sustained 3 sessions with clean auctions (term-premium thesis spent). *None firing; SOFR-IORB ~0.*
- **TLT puts:** kill if 10Y <4.15 **and** 30Y <5.0 for 3 sessions **and** a clean refunding. Re-arm conditional-add on a real tail (>1.5bp + indirect <60%) at a coupon auction — next is the **6/16 20Y**.
- **Convergence downgrade:** long-end →2 (✅ met 6/15); dealer absorption →2 when next FR2004 (~6/23) shows long-end inventory off the highs.
- **Time-based:** each coupon cluster (refunding weeks + 20Y/TIPS) re-grades auction-health + long-end; 60-DTE review on any options position.

---

## Immediate Catalysts

| Date | Catalyst | What BOND watches | Route |
|---|---|---|---|
| **6/16 (Tue)** | **20Y bond reopening** (CUSIP 912810UV8) | First coupon since refunding. BTC/tail/indirect vs norms. Tail >1.5bp + weak indirect = **TLT add re-arm**. | PROME/LIQUID if tail |
| **6/17 (Wed)** | **FOMC — statement 2pm ET** | Dots/bias shift; hawkish read → long-end / term-premium pressure. Rate-expectations read is HENRY's; BOND owns the long-end consequence. | HENRY/PROME |
| 6/18 (Thu) | 4Y10M TIPS reopen | Real-money / inflation demand read. | — |
| Daily | 10Y >4.5 / 30Y >5.0 | Re-escalation watch **RELAXED, re-armable**. 5 sessions + weak auction = escalate. | HENRY/LIQUID |
| Watch | Energy HY OAS / CCC bifurcation | Confirm energy HY >300 (stale 285 Apr 28, via LIQUID); CCC 948. | BRENT/LIQUID (pull) |
| Watch | Treasury buyback long-end accept-cap | Lift = YCC-lite / stealth suppression = direct TLT-puts event. Not current policy. | LIQUID/PROME if lifts |
| Weekly | Dealer positions (FR2004) | Absorption capacity vs forced de-risk. | LIQUID/ZHAO |

---

## Bottom Line

**The June refunding cleared and the long-end episode relaxed — "expensive, not broken" held a fourth straight resolution.** 10Y 4.47 / 30Y 4.97 back below thresholds, VIX 16, macro credit calm (HY 271), composite **11/35**. The 10Y (6/10) printed **strong** (BTC 2.57, indirect 78%, PD 9.4%); the 30Y (6/11) **soft but orderly** (BTC 2.33, indirect 59.8%) — no demand hole, so **BND-08 resolves FALSE**. **TLT puts HOLD, no add** — the conditional-add gates lapsed unfired. **Next 48h is the live gate: the 6/16 20Y reopening and the 6/17 FOMC** — a weak 20Y or a hawkish FOMC re-arms the long-end watch; absent that, the relaxation stands.
