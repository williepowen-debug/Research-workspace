# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure
**State:** 🟡→🟢 WATCH (long-end leg RELAXED) — duration episode confirmed then mean-reverted; 30Y back below 5.0, 10Y back below 4.5, breakevens cooled, credit/vol calm. No active escalation.
**Last Updated:** 2026-06-05 ~5:00pm ET by BOND (boot catch-up: 5/20 → 6/5 data refresh)

---

## Regime Read

**The long-end stress episode confirmed itself and then partially unwound.** Over 5/14–5/27 the term-premium repricing was real and durable: 30Y closed above 5.0 for ~9 consecutive sessions and 10Y above 4.5 for 6 — this **resolved BND-07 TRUE** (the May refunding weakness was durable repricing, not a one-day supply concession). But the regime has since mean-reverted: by 6/4 the 10Y is back to **4.47** (below 4.5) and the 30Y to **4.97** (below 5.0), with TLT up to **$85.06**. This is a **threshold-vs-mechanism split** — the threshold fired, the mechanism was genuine, but term premium gave a meaningful chunk back into June. Confirmed episode, not a one-way break.

**The rally was breakeven-led, not real-rate-led.** Inflation expectations cooled across the curve (T10YIE 2.49→2.36, T5YIE 2.66→2.48, T5YIFR 2.32→**2.24**, back inside the 2.25 watch band) while the 10Y real yield (DFII10) held roughly flat at 2.11. So the de-escalation is primarily an **inflation-premium relaxation**, not a sign that supply/term-premium pressure has resolved. The structural story (heavy issuance, elevated real yields) is intact; the acute leg is just no longer breaching thresholds.

**Credit and vol never participated — and still aren't.** HY OAS *tightened* through the entire duration episode (286→**274**), IG OAS held tight (76→**74**), CCC drifted flat (948→**946**), and VIX collapsed to **15.4**. The cash-credit/duration decoupling that defined this whole period is fully intact: the long-end move never transmitted to spreads or equity vol. **BND-06 resolved TRUE** (HY OAS never closed above 300 in May).

**Late-May auctions were healthy-to-soft, no stress.** 5/26 2Y BTC 2.64 (solid), 5/27 5Y BTC 2.34 (soft but in-pattern with Apr-27's 2.33), 5/28 7Y BTC 2.52 (decent, indirect 78% of competitive). Demand held at price across the belly — corroborates "expensive, not broken."

**Correction — the 5/21 "10Y reopening" was a 10Y TIPS reopening, not a nominal 10Y.** CUSIP 91282CPU9, real high yield 2.169%, 9Y8M, reopening. BTC 2.52 / indirect ~61% of offering — no stress. My prior STATUS framed it as the nominal-10Y "Leg 2" demand gate for the TLT-put conditional-add; that was a TIPS-vs-nominal conflation. Different instrument, different (real-money/inflation) buyer base — it does not speak to nominal-10Y sponsorship. The conditional-add gate keyed to it was therefore mis-specified; moot anyway because yields rallied and no add was ever warranted. The last nominal 10Y was 5/12; the next is 6/10.

**30Y reframe integrated (PROME dataset, 364 rows 2023→present):** the **5/13 30Y (BTC 2.30) was the 11th percentile** of all 30Y auctions since 2023 — the real statistical outlier of the May refunding triplet, sharper than my original "below avg, demand mix not failed" framing implied. The 5/12 10Y indirect (51.5% of offering) was 7th percentile. The long-end leg of BND-07 rested on stronger empirical footing than I called out at the time.

**TLT puts posture: HOLD into June refunding; no add.** All add-gates lapsed unfired. The next live read is the June refunding cluster (6/9 3Y · 6/10 nominal 10Y · 6/11 nominal 30Y).

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| HY OAS | **274bps** | 🟢 | FRED `BAMLH0A0HYM2`, Jun 4 | −12bp from 5/19; tightening, well below 300. Short-HY thesis inactive. |
| CCC OAS | **946bps** | 🟡 | FRED `BAMLH0A3HYC`, Jun 4 | ~flat vs 5/19 (948); lower-quality stress steady, not broadening. |
| IG OAS | **74bps** | 🟢 | FRED `BAMLC0A0CM`, Jun 4 | −2bp; market fully functional. |
| 10Y yield | **4.47%** | 🟡 | FRED `DGS10`, Jun 4 | −14bp vs 5/20. **Back below 4.5.** BND-07 fired (5/15-5/22) then mean-reverted. |
| 30Y yield | **4.97%** | 🟡 | FRED `DGS30`, Jun 4 | −17bp vs 5/20. **Back below 5.0** after ~9 sessions above (5/14-5/27). |
| 20Y yield | **4.98%** | 🟡 | FRED `DGS20`, Jun 4 | −16bp vs 5/20 auction stop. |
| TLT | **$85.06** | 🟡 | yfinance, Jun 5 ~live | +$1.17 vs 5/20; duration relief continued as yields fell. |
| VIX | **15.4** | 🟢 | FRED `VIXCLS`, Jun 4 | −2.1 vs 5/20; equity vol collapsed. No credit-equity stress. |
| KRE | **$70.17** | 🟢 | yfinance, Jun 5 ~live | +$1.32 vs 5/20. |
| HYG | **$79.43** | 🟢 | yfinance, Jun 5 ~live | Holding; no credit transmission. |
| SOFR-IORB | -12bps | 🟢 | Dashboard, May 19 (stale) | No funding confirmation of duration stress; refresh next session. |
| **10Y TIPS yield (DFII10)** | **2.11%** | 🟡 | FRED `DFII10`, Jun 4 | ~flat vs 2.13 (5/18). Real yield held — nominal rally was breakeven-led. |
| **10Y breakeven (T10YIE)** | **2.36%** | 🟢 | FRED `T10YIE`, Jun 4 | −13bp vs 5/19. Inflation premium relaxed. |
| **5Y breakeven (T5YIE)** | **2.48%** | 🟢 | FRED `T5YIE`, Jun 4 | −18bp vs 5/19. |
| **5Y5Y forward infl (T5YIFR)** | **2.24%** | 🟢 | FRED `T5YIFR`, Jun 4 | −8bp vs 5/19; **back inside the 2.25 band** — anchoring leg relaxed. |
| Corp issuance YTD | $1,013.9B through Apr, +28.2% YoY | 🟢 | SIFMA May 2026 | Primary market not frozen (refresh for May data). |

---

## Latest Auction Read

| Date | Tenor | Size | BTC | High Yield | Indirect | Direct | Dealer | Read |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| May 11 | 3Y | $58B | 2.54 | 3.965% | 63.0% | 20.1% | 16.9% | Weak: +0.6bp tail, dealer take elevated. |
| May 12 | 10Y | $42B | 2.40 | 4.468% | 64.0%* | 24.1% | 12.0% | Weak: 4th consecutive 10Y tail; indirect 7th-pctile of offering (PROME dataset). |
| May 13 | 30Y | $25B | 2.30 | 5.046% | 66.6% | 21.7% | 11.7% | **11th-percentile BTC since 2023 — the real outlier of the triplet.** |
| May 20 | 20Y new issue | $16B | 2.55 | 5.122% (tail 0bp) | 67.7% | 22.9% | 9.4% | Clean — stopped on the screws, priced ~2bp through the screen. 38th-pctile BTC. |
| **May 21** | **10Y TIPS reopening** | **$19B** | **2.52** | **2.169%** (real) | ~61%† | — | — | **TIPS, NOT nominal (CUSIP 91282CPU9). No stress. Mislabeled as "10Y reopening" in prior STATUS.** |
| May 26 | 2Y | $69B | 2.64 | 4.071% | 57.6%† | 30.1%† | 12.3%† | Solid. |
| May 27 | 5Y | $70B | 2.34 | 4.182% | 74.8%† | 12.3%† | 12.8%† | Soft but in-pattern (≈Apr-27's 2.33); strong indirect. |
| May 28 | 7Y | $44B | 2.52 | 4.290% | 78.4%† | 11.2%† | 10.4%† | Decent; foreign sponsorship solid. |

\* indirect convention varies (of competitive vs of offering); see PROME dataset methodology note.
† computed as % of competitive accepted (ind+dir+dlr) from FiscalData accepted amounts.

**Read:** No stress markers across the late-May calendar. Belly (2Y/7Y) firm, 5Y soft but consistent with its standing pattern (not new deterioration), TIPS fine. Demand held at price. Consistent with term-premium digestion, not mechanical demand failure.

---

## Convergence Matrix

| Vector | Score | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|
| Treasury auction health | 2 | 🟡 | Late-May coupons healthy-to-soft, no stress (2Y 2.64, 5Y 2.34, 7Y 2.52). 20Y clean. June refunding 6/9-6/11 is next gate. | 2+ weak coupon auctions same tenor OR a >2bp tail at June refunding. |
| HY market function | 1 | 🟢 | HY OAS 274 (tightening); issuance strong through Apr. | HY OAS >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | 🟢 | IG OAS 74 (tight); no freeze evidence. | IG OAS +20bps/week or clustered pulled IG deals. |
| Dealer absorption | 2 | 🟡 | Late-May dealer takes contained (2Y 12.3%, 5Y 12.8%, 7Y 10.4% of comp). | Forced inventory decline in a selloff OR dealer spike + repo pressure. |
| Long-end/duration | **2** | 🟡 | **Downgraded 4→2.** 10Y 4.47 (<4.5), 30Y 4.97 (<5.0) — thresholds no longer breached. Episode confirmed (BND-07 TRUE) then mean-reverted. Absolute levels still elevated. | 10Y back >4.5 OR 30Y back >5.0 for 5 sessions WITH a weak June auction or SOFR-IORB lift = re-escalate. |
| CDX-cash basis | 2 | 🟡 | Direct CDX still not wired; March divergence not refreshed. | CDX widens while HY cash stays tight for 2+ weeks. |
| Credit-equity lead | 1 | 🟢 | HY OAS 274, VIX 15.4; credit hasn't led, vol collapsed. | HY OAS +75-100bps from trough while VIX stays <20. |

**Composite: 11/35 — watch, long-end leg relaxed, no active escalation.** Down from 13/35 (5/20) as long-end/duration moved 4→2 on the mean-reversion and breakeven/anchoring vectors relaxed. The June refunding (6/9-6/11) is the next live gate; absent a weak nominal 10Y/30Y print, the duration thesis stays in confirmed-but-dormant territory.

---

## Trade Interface

- **TLT puts:** **HOLD into June refunding — no add.** All 5/20-5/21 add-gates lapsed unfired (the 5/21 "gate" was a mislabeled TIPS reopening; nominal demand never tested until 6/10). Yields rallied ~15bp off the episode highs, so adding here would be chasing a relaxing move. Re-arm a conditional-add only if the June nominal 10Y (6/10) or 30Y (6/11) prints a real tail (>1.5bp) with weak indirect. Per [[feedback_put_vs_duration_expression]], if a duration-short re-engages, TLT puts are the cleaner vehicle than equity puts for this thesis.
- **HYG $75P Jun:** No support to add/roll. HY OAS 274 (tighter), IG tight, HYG holding $79.43 — zero credit transmission. Salvage/lottery; expires soon. Watch for HY OAS reclaiming 300 (not close).
- **Credit-equity lead:** Inactive. HY OAS tightening while VIX collapses — the opposite of a credit-leads-equity setup.

---

## Immediate Catalysts

| Date | Catalyst | What BOND watches | Signal Route |
|---|---|---|---|
| **Jun 9 (Tue)** | **3Y note auction** | BTC vs ~2.54 norm; dealer take. Kicks off June refunding. | PROME if weak |
| **Jun 10 (Wed)** | **10Y note auction (nominal, 9Y11M new issue)** | First real nominal-10Y demand test since 5/12. 5th-consecutive-tail streak live. Tail >1.5bp + weak indirect = TLT conditional-add re-arm. | LIQUID/ZHAO if weak; PROME if tail |
| **Jun 11 (Thu)** | **30Y bond auction (nominal, 29Y11M new issue)** | Long-end demand at price; 5/13 was 11th-pctile. Watch for repeat outlier. | LIQUID/PROME if tail |
| Daily | 10Y back >4.5 / 30Y back >5.0 | Re-escalation watch (currently 4.47 / 4.97, below) | HENRY/LIQUID |
| Weekly | HY/IG OAS + primary calendar | OAS >300 / pulled deals / issuance freeze | BROCK/REGINALD/HENRY |
| Weekly | Dealer positions (FR2004) | absorption capacity vs forced de-risking | LIQUID/ZHAO |
| As available | CDX.HY / CDX.IG | synthetic leading cash (data gap — still not wired) | HENRY/VIOLET/LIQUID |

---

## Bottom Line

**The long-end episode confirmed itself, then partially reversed.** Term premium genuinely repriced over 5/14–5/27 (30Y >5.0 for ~9 sessions, 10Y >4.5 for 6 — **BND-07 resolved TRUE**), but it has since mean-reverted: 10Y back to 4.47, 30Y to 4.97, TLT up to $85.06. The rally was **breakeven-led** (5Y5Y forward back inside its 2.25 band) while real yields held flat — so supply/term-premium structure is intact, just no longer breaching thresholds. Credit and vol never participated and still don't (HY OAS 274 and tightening, IG 74, VIX 15.4 — **BND-06 resolved TRUE**). Late-May auctions were healthy-to-soft with no stress. Two corrections integrated: the 5/21 "10Y reopening" was actually a 10Y **TIPS** reopening (mis-framed as the nominal demand gate), and PROME's dataset shows the **5/13 30Y** (11th-percentile BTC) was the true statistical outlier of the refunding week, not the 20Y. **TLT puts: HOLD into the June refunding (6/9-6/11)**, which is the next live read on nominal long-end demand — no add unless the nominal 10Y/30Y prints a real tail.
