# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure
**State:** 🟡 WATCH — refunding week weak but not failed; public credit still calm
**Last Updated:** 2026-05-13 19:35 ET by PROME

---

## Regime Read

Public bond-market stress is **not confirming cascade yet**. HY OAS remains tight at **282bps**, VIX is below 20, and April corporate issuance was strong. The March BOND short-credit setup has therefore softened materially.

But the “all clear” read is too easy: CCC OAS is still elevated at **937bps**, the 30Y has traded through **5%**, and the May refunding auctions all tailed modestly. This is **duration fatigue**, not failed-auction panic: buyers demanded concession, but indirect demand and dealer take did not confirm a Treasury-demand hole. BOND’s job now is **not to shout crisis**; it is to detect when tight cash credit and calm equities are contradicted by auctions, synthetic credit, or primary-market access.

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| HY OAS | **282bps** | 🟢 | Dashboard/FRED, May 13 | Below 300; short-HY thesis not active. |
| CCC OAS | **937bps** | 🟡 | Dashboard/FRED, May 13 | Still stressed lower-quality credit; not broad contagion alone. |
| IG OAS | **79bps** | 🟢 | FRED `BAMLC0A0CM`, May 8 | IG market still functional. |
| 10Y yield | **4.46%** | 🟡/🟠 | Dashboard/FRED, May 13 | Near 4.5 trigger; duration pressure rising. |
| 2Y yield | **3.90%** | 🟢/🟡 | FRED `DGS2`, May 8 | Curve still positive. |
| 2s10s | **+48bps** | 🟡 | FRED derived, May 8 | Mild bear-steepener risk, not acute. |
| 30Y yield | **~5.0%+ intraday** | 🟠 | Market/news, May 13 | Long-end traded through 5%; not confirmed by auction failure. |
| SOFR-IORB | **-5bps** | 🟢 | Dashboard / FRED, May 13 | No current repo/funding confirmation. |
| HYG | **$79.98** | 🟢 | yfinance, May 11 | Credit ETF not breaking. |
| TLT | **$84.80** | 🔴 | Dashboard, May 13 | Duration weak; auction weakness not enough alone for panic. |
| VIX | **17.88** | 🟢 | Dashboard, May 13 | Equity vol not confirming credit stress. |
| Corp issuance YTD | **$1,013.9B through Apr, +28.2% YoY** | 🟢 | SIFMA result surfaced May 2026 | Primary market not frozen. |

---

## Latest Auction Read

| Date | Tenor | Size | BTC | High Yield | Indirect | Direct | Dealer | Read |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Apr 22 | 20Y reopening | $13B | 2.68 | 4.883% | 59.6% | 20.2% | 8.6% | Healthy BTC; long-end yield high. |
| Apr 23 | 5Y TIPS | $26B | 2.57 | 1.367% | 57.0% | 23.7% | 7.5% | Improved from March stress. |
| Apr 27 | 2Y | $69B | 2.65 | 3.812% | 49.7% | 27.8% | 10.4% | Acceptable. |
| Apr 27 | 5Y | $70B | 2.33 | 3.955% | 64.1% | 13.3% | 11.2% | Soft but not failed. |
| Apr 28 | 7Y | $44B | 2.51 | 4.175% | 51.7% | 26.6% | 10.3% | Acceptable. |
| May 11 | 3Y | $58B | 2.54 | 3.965% | 63.0% | 20.1% | 16.9% | Weak: +0.6bp tail, BTC below 6mo avg, dealer take elevated. |
| May 12 | 10Y | $42B | 2.40 | 4.468% | 64.0% | 24.1% | 12.0% | Weak: +0.4bp tail, 4th consecutive 10Y tail; foreign demand soft vs recent avg. |
| May 13 | 30Y | $25B | 2.30 | 5.046% | 66.6% | 21.7% | 11.7% | Below avg: +0.5bp tail and lower BTC; demand mix not failed. |

**May refunding read:** all three coupon auctions tailed modestly and bid/covers were below recent averages. This is **yellow duration fatigue**, not red auction dysfunction: tails were small (<1bp), indirect demand stayed around/above 63%, dealer take did not spike catastrophically, and SOFR-IORB remains calm.

---

## Convergence Matrix

| Vector | Score | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|
| Treasury auction health | 4 | 🟡 | May refunding was weak across 3Y/10Y/30Y: small tails and below-average BTCs, but no >2bp tail or dealer spike. | Upgrade to orange/red on BTC <2.3 with dealer spike, tail >2bps, or funding stress. |
| HY market function | 1 | 🟢 | HY OAS 281; issuance strong through Apr. | HY OAS >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | 🟢 | IG OAS 79; no broad IG freeze evidence. | IG OAS +20bps/week or clustered pulled IG deals. |
| Dealer absorption | 3 | 🟡 | Dealer take manageable; prior ~$550B net Treasury position remains capacity-used marker. | Forced inventory decline during selloff or weak auctions + repo pressure. |
| Long-end/duration | 4 | 🟠 | 30Y traded through 5%, 10Y near 4.5, TLT weak; 30Y auction only modestly tailed. | 10Y >4.5 for 5 sessions; 30Y >5 sustained with bigger auction tails. |
| CDX-cash basis | 2 | 🟡 | Direct CDX not wired; March divergence needs refresh. | CDX widens while HY cash stays tight for 2+ weeks. |
| Credit-equity lead | 1 | 🟢 | HY OAS tight and VIX <20; no public-credit lead. | HY OAS +75-100bps from trough while VIX stays <20. |

**Composite:** **16/35 — watch / yellow duration fatigue, not active credit stress.** BOND’s crisis thesis is on probation; the structural thesis survives, but current public-market evidence is still insufficient for broad short-credit reactivation.

---

## Trade Interface

- **HYG $75P Jun:** BOND no longer supports adding or rolling on current data. HY OAS <300 and strong issuance invalidate the Mar 26 entry logic for fresh premium. Existing position is only salvage/lottery unless HY OAS reclaims 300 quickly.
- **TLT puts:** BOND supports **watch/conditional hold if already owned**, not aggressive add. Duration pressure is real: 30Y traded above 5%, 10Y is near 4.5, and refunding week was weak. But tails were small and auctions did not fail; conviction rises only if weakness persists or funding stress appears.
- **Credit-equity lead:** inactive. Re-activates only with HY OAS >300 and widening velocity, ideally while VIX remains complacent.

---

## Immediate Catalysts

| Date | Catalyst | What BOND watches | Signal Route |
|---|---|---|---|
| **May 12** | 10Y auction | ✅ Weak but not failed: 4.468%, +0.4bp tail, BTC 2.40, indirect 64.0%, dealer 12.0% | Note to LIQUID/ZHAO; no crisis signal |
| **May 13** | 30Y auction | ✅ Below avg but not failed: 5.046%, +0.5bp tail, BTC 2.30, indirect 66.6%, dealer 11.7% | Watch long-end; no demand-hole confirmation |
| Weekly | HY/IG OAS + primary calendar | OAS >300 / pulled deals / issuance freeze | BROCK/REGINALD/HENRY |
| Weekly | Dealer positions | absorption capacity vs forced de-risking | LIQUID/ZHAO |
| As available | CDX.HY / CDX.IG | synthetic leading cash | HENRY/VIOLET/LIQUID |

---

## Bottom Line

BOND should be treated as **watchful but de-risked**. Public credit is not confirming the private-credit stress yet. The live edge is the contradiction hunt: if FSK/BDC marks are deteriorating while HY cash and VIX stay calm, BOND needs auction weakness, CDX widening, or primary-market failures to prove public-market transmission. Without that, HYG June downside is stale. Duration shorts have support from price/yield pressure, but refunding week delivered only yellow confirmation, not a red auction break.
