# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure
**State:** 🟡 WATCH — **de-escalated: the June refunding cleared cleanly and the long-end leg relaxed.** The into-refunding re-firing (10Y 4.53 / 30Y 5.01, real-rate-led, 6/9) did NOT translate to auction stress; the 6/10 10Y was actually strong (indirect 78%), and yields fell back below thresholds (10Y 4.47 / 30Y 4.97 by 6/12). VIX collapsed back (21.2→16.1). Credit calm holds; CCC bifurcation creep stalled. Re-escalation watch stood down.
**Last Updated:** 2026-06-15 ~3:50pm ET by BOND (boot 6/9→6/15 live refresh; June refunding post-mortem — BND-08 resolved FALSE)

---

## Regime Read

**The June refunding was the live test, and it cleared cleanly — the central open question from 6/9 resolved benign.** Yields had backed up into the refunding (10Y 4.53 / 30Y 5.01, real-rate-led, DFII10 2.19 on 6/9) with the 5th-consecutive-10Y-tail streak armed. Instead: **6/10 10Y reopening printed BTC 2.57 (vs 5/12's 2.40) with indirect 78.2% and dealer take DOWN to 9.5%** — a *strong* auction, end-user demand absorbed the supply and broke the tail-streak fear. **6/11 30Y reopening: BTC 2.33 (vs 5/13's 2.30), indirect 60.0%, dealer 14.7%** — orderly, slightly dealer-heavier mix but no outlier repeat. **BND-08 (stress-marker prediction) resolves FALSE**, mirroring BND-05 in May: refunding-stress predictions keep resolving benign. "Expensive, not broken" — duration-at-a-discount demand persists.

**Post-auction, the long-end leg relaxed.** Yields fell back below thresholds: **10Y 4.47, 30Y 4.97** (6/12) — both under 4.5/5.0. The real-rate move that drove the 6/5-6/9 back-up **reversed** (DFII10 2.19→2.16), i.e. the supply/term-premium pressure ebbed once the supply cleared rather than persisting. This was the transient, threshold-fires-then-mean-reverts pattern (sibling of BND-07's episode), not a one-way break. VIX collapsed back to **16.1** from 21.2.

**Credit stayed calm and the bifurcation creep stalled.** Macro HY OAS **271** (tighter from 275), IG **74**, CCC **948** (flat, no further widening over the window). The CCC quality-bifurcation watch holds at the line but isn't accelerating. No cash-credit transmission; HYG firm ($80.07). The credit-leads-equity setup stays inactive — and with VIX back to 16, even the equity-vol leg that woke in early June has gone back to sleep.

**The dealer-thin-backstop thesis was NOT tested to failure.** The structural setup was real — NY Fed FR2004 (5/27) showed dealer long-end inventory near/at record (11-21Y $67.0B all-time high), and the buyback long-end offer/accept ratio at ~13x corroborated duration-dumping. But the refunding cleared with **low dealer takedowns** (10Y dealer 9.5%, the strongest end-user mix of the three), meaning end-users absorbed the supply and the thin backstop was never the binding constraint. Structural inventory is still elevated (data 2wk-lagged, refresh due ~6/23) but the acute concern eased. Dealer absorption downgraded 3→2.

**Treasury buyback posture unchanged — business-as-usual.** $2B long-end accept cap held flat (9 consecutive quarters, never lifted); the elevation remains on the *market* side (dealer duration-dumping), not Treasury behavior. YCC-lite bright-line (first lift of the $2B long-end cap) is NOT current policy. No change since 6/9.

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| HY OAS | **271bps** | 🟢 | FRED `BAMLH0A0HYM2`, Jun 12 | -4 vs 6/8; calm. CCC bifurcation creep stalled — caveat eased. |
| CCC OAS | **948bps** | 🟡 | FRED `BAMLH0A3HYC`, Jun 12 | Flat vs 6/8 (949); no further widening. Above 900 watch holds. |
| IG OAS | **74bps** | 🟢 | FRED `BAMLC0A0CM`, Jun 12 | -1bp; tight, market functional. |
| 10Y yield | **4.47%** | 🟡 | yfinance `^TNX`, Jun 12 | **Back BELOW 4.5** (was 4.53 on 6/9). Refunding cleared; re-firing relaxed. |
| 30Y yield | **4.97%** | 🟡 | yfinance `^TYX`, Jun 12 | **Back BELOW 5.0** (was 5.01 on 6/9). 6/11 auction cleared orderly. |
| 5Y yield | **4.19%** | 🟢 | yfinance `^FVX`, Jun 12 | -6bp vs 6/9; belly eased. |
| TLT | **$85.74** | 🟡 | yfinance, Jun 12 | +$0.63 vs 6/9; duration relief as yields fell back. |
| VIX | **16.1** | 🟢 | yfinance `^VIX`, Jun 12 | **-5.1 vs 6/9 (21.2).** Equity vol went back to sleep. |
| KRE | **$72.29** | 🟢 | yfinance, Jun 12 | +$1.21 vs 6/9; banks holding (note -1.12 on the day, within range). |
| HYG | **$80.07** | 🟢 | yfinance, Jun 12 | Firm; no cash-credit transmission. |
| SOFR | **3.65%** | 🟢 | FRED `SOFR`, Jun 12 | No funding stress; no duration-stress confirmation from funding. |
| **10Y TIPS (DFII10)** | **2.16%** | 🟡 | FRED `DFII10`, Jun 11 | **-3bp vs 6/5 peak (2.19).** Real-rate back-up REVERSED — supply/term-premium pressure ebbed. |
| **10Y breakeven (T10YIE)** | **2.31%** | 🟢 | FRED `T10YIE`, Jun 12 | ~flat; inflation premium not the driver. |
| **5Y5Y forward infl (T5YIFR)** | **2.23%** | 🟢 | FRED `T5YIFR`, Jun 12 | Inside the 2.25 band — anchoring leg relaxed. |
| Corp issuance YTD | $1,013.9B through Apr, +28.2% YoY | 🟢 | SIFMA May 2026 | Primary market not frozen (refresh for May data). |

---

## Latest Auction Read

| Date | Tenor | BTC | High Yield | Indirect | Direct | Dealer | Read |
|---|---:|---:|---:|---:|---:|---:|---|
| May 12 | 10Y | 2.40 | 4.468% | 64.0%* | 24.1% | 12.0% | Weak: 4th consecutive 10Y tail; indirect 7th-pctile of offering. |
| May 13 | 30Y | 2.30 | 5.046% | 66.6% | 21.7% | 11.7% | 11th-percentile BTC since 2023 — the May outlier. |
| May 20 | 20Y new | 2.55 | 5.122% (0bp tail) | 67.7% | 22.9% | 9.4% | Clean — stopped on the screws. |
| **Jun 9** | **3Y** | **2.64** | **4.192%** | **63.7%** | **21.0%** | **15.3%** | **Solid** (>2.54 norm). Front-end. |
| **Jun 10** | **10Y reopen** | **2.57** | **4.538%** | **78.2%** | **12.3%** | **9.5%** | **STRONG — BTC up vs 5/12 (2.40), indirect 78%, dealer take DOWN. Broke the 5th-tail-streak fear.** |
| **Jun 11** | **30Y reopen** | **2.33** | **5.020%** | **60.0%** | **25.3%** | **14.7%** | **Orderly — BTC ≈ 5/13 (2.30), no outlier repeat. Slightly dealer-heavier mix.** |

\* indirect convention varies (of competitive vs of offering). June % are of accepted (ind+dir+dlr), FiscalData.

**Read:** The June refunding cleared cleanly — the 10Y notably the strongest demand mix of the three (indirect 78%). No stress markers; demand held at price. The into-refunding back-up was concession that drew buyers, not a demand failure. Confirms "expensive not broken." Next nominal coupon supply: July refunding cycle.

---

## Convergence Matrix

| Vector | Score | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|
| Treasury auction health | 2 | 🟡 | June refunding cleared cleanly (3Y BTC 2.64, 10Y BTC 2.57/ind 78%, 30Y BTC 2.33). Demand-at-a-discount but orderly. | 2+ weak coupon auctions same tenor OR a >2bp tail at a future refunding. |
| HY market function | 1 | 🟢 | HY OAS 271 (tighter). CCC 948 flat — bifurcation creep stalled. | HY OAS >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | 🟢 | IG OAS 74 (tight); no freeze evidence. | IG OAS +20bps/week or clustered pulled IG deals. |
| Dealer absorption | **2** | 🟡 | **Downgraded 3→2.** Refunding cleared with LOW dealer takedowns (10Y 9.5%) — end-users absorbed supply, thin backstop never binding. Structural FR2004 inventory still elevated (5/27, near record) but not forced; data refresh due ~6/23. | FR2004 long-end at fresh highs + weak auction, OR forced inventory decline in a selloff, OR dealer spike + repo pressure. |
| Long-end/duration | **2** | 🟡 | **Downgraded 3→2.** 10Y 4.47 / 30Y 4.97 — back below thresholds. Real-rate back-up reversed (DFII10 2.19→2.16). Re-firing leg relaxed post-refunding. Levels still absolutely elevated. | 10Y >4.5 OR 30Y >5.0 held **5 sessions** WITH a weak auction or SOFR-IORB lift = escalate to 3. |
| CDX-cash basis | 1 | 🟢 | HYG/IEF proxy, no divergence at cash level. Synthetic/options leg handed to VIOLET. | Proxy z20 < -1.5 while HY OAS tight, OR VIOLET reports HYG put-skew steepening vs flat cash. |
| Credit-equity lead | 1 | 🟢 | HY OAS 271 tight, VIX back to 16.1 — both legs asleep. | HY OAS +75-100bps from trough while VIX stays <20. |

**Composite: 10/35 — watch, de-escalated.** Down from 12/35 (6/9): long-end/duration 3→2 (yields back below thresholds, real-rate move reversed) and dealer absorption 3→2 (refunding cleared with low dealer takedowns; thin backstop never binding). The two upgrades from 6/9 both reversed because the event they anticipated — auction stress at the refunding — didn't happen. The system is back to its baseline "expensive, not broken" read: long end elevated in level but functioning, credit calm, no transmission active. Next nominal supply test is the July refunding.

---

## Trade Interface

- **TLT puts:** **HOLD — conditional-add never armed, correctly.** The 6/10 nominal 10Y / 6/11 30Y re-arm trigger (real tail >1.5bp + weak indirect) did NOT fire — both auctions cleared cleanly, the 10Y was strong. Yields fell back below thresholds post-refunding. No add was warranted and none was made. Re-arm only on a fresh sustained break (10Y >4.5 / 30Y >5.0 held 5 sessions WITH a weak auction). Per [[feedback_put_vs_duration_expression]], TLT puts remain the cleaner vehicle than equity puts if a duration-short re-engages.
- **HYG $75P Jun:** No support. HY OAS 271 (tighter), IG tight, HYG firm $80.07 — zero credit transmission. Salvage/lottery; near expiry. Watch only for HY OAS reclaiming 300.
- **Credit-equity lead:** Inactive. Both credit and equity-vol legs asleep (HY 271 tight, VIX 16).

---

## Immediate Catalysts

| Date | Catalyst | What BOND watches | Signal Route |
|---|---|---|---|
| **Done 6/9-6/11** | **June refunding (3Y/10Y/30Y)** | **CLEARED CLEANLY.** No stress markers; 10Y strong (ind 78%). BND-08 FALSE. | — |
| ~Jun 23 | FR2004 dealer-positioning refresh | Whether long-end inventory eased off the 5/27 near-record or built further. | LIQUID/ZHAO |
| Daily | 10Y >4.5 / 30Y >5.0 sustained | **Re-escalation watch STOOD DOWN** (4.47 / 4.97, below thresholds). Re-arm on 5 sessions above + weak auction. | HENRY/LIQUID |
| Watch | Energy HY OAS / CCC bifurcation | CCC 948 flat (creep stalled). Confirm energy HY vs 300 (stale 285, Apr 28). | BRENT (pull) / LIQUID |
| Watch | **Treasury buyback accept-cap** | Unchanged — $2B long-end cap held (9 quarters). **Trigger: cap LIFTED on long buckets = YCC-lite = direct TLT-puts event.** Not current policy. | LIQUID/HENRY/PROME if cap lifts |
| ~Jul | July refunding cycle | Next nominal coupon supply test. | PROME/LIQUID |
| Weekly | HY/IG OAS + primary calendar | OAS >300 / pulled deals / issuance freeze | BROCK/REGINALD/HENRY |
| As available | CDX.HY / CDX.IG | synthetic leading cash (data gap — still not wired) | HENRY/VIOLET/LIQUID |

---

## Bottom Line

**The June refunding was the live test and it cleared cleanly — BOND de-escalates.** The into-refunding back-up (10Y 4.53 / 30Y 5.01, real-rate-led, 6/9) drew buyers rather than breaking: the **6/10 10Y was strong** (BTC 2.57 vs May's 2.40, indirect 78%, dealer take down to 9.5%), the **6/11 30Y was orderly** (no outlier repeat), and **BND-08 (stress-marker) resolves FALSE** — the same benign outcome as May's BND-05. Post-auction, yields fell **back below thresholds (10Y 4.47 / 30Y 4.97)**, the real-rate move **reversed** (DFII10 2.19→2.16), and **VIX collapsed to 16.1**. The dealer-thin-backstop concern was real structurally but never binding — end-users absorbed the supply. Long-end/duration and dealer absorption both downgraded 3→2; composite 12→10. Credit stays calm (HY 271, CCC 948 flat). **TLT puts: HOLD — the conditional-add correctly never armed.** Back to baseline "expensive, not broken"; next nominal supply test is the July refunding.
