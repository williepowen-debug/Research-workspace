# Product-Side Decoupling — Phase-2 Alpha Lane

**Author:** BRENT
**Created:** 2026-04-17
**Status:** THESIS — research document, not yet a trade proposal
**Related:** `refinery_damage/TRACKER.md`, `REFINERY_UTILIZATION_MAR2026.md`, `STATUS.md` (Phase-2 exit protocol)

---

## THE THESIS IN ONE PARAGRAPH

When the Hormuz crisis unwinds, crude price will flush on the announcement. But **global refining capacity cannot absorb the returning barrels as fast as the paper futures price them**, because ~1.5-2M bpd of real refining capacity is currently damaged across the US (Port Arthur), Gulf (Satorp, Ruwais, Mina Al-Ahmadi, Bazan), Russia (6 facilities), and Australia (Geelong). The result: **crack spreads stay elevated for weeks after crude falls.** Refiners that can still process (Marathon, Phillips 66, HF Sinclair) capture outsized margins on the crude-down/product-sticky gap. This creates a **decoupling trade:** long refiners vs short crude proxy, capturing the crack-spread expansion that must mechanically occur during the transition.

**This is not a directional oil call.** It is a **spread trade** — betting that the ratio of refiner equity to crude proxy expands during the Phase-2 window, regardless of absolute oil direction.

---

## WHY THE DECOUPLING MUST OCCUR

### The mechanics
Crack spread = wholesale product price (gasoline + diesel) − crude cost, per barrel.

On Phase-2 trigger (Hormuz reopens):
1. **Crude falls immediately** — paper market prices in resolution, futures gap down 15-25% (already seen partially on Apr 17 with Brent -12% intraday)
2. **Wholesale product prices fall slower** — refiners sell forward, inventories take time to move, and global product stocks are 3% below 5-yr avg
3. **Crack spread expands** in the interval — the wider the gap between rapid crude drop and lagged product price drop, the larger the refiner margin bonanza
4. **Eventually equalizes** — product prices catch up, crack compresses, refiner margins normalize over ~4-8 weeks

### Why this time is larger than normal
- **Crack spreads already at 95th+ percentile** (3-2-1 LLS $28.91, ULSD $25.83, jet $92+ per `REFINERY_UTILIZATION_MAR2026`)
- **1.5-2M bpd of genuine refining capacity impaired** (see tracker) — capacity can't simply restart to re-absorb crude
- **Global distillate stocks 3% below 5-yr avg** — buyers have been drawing inventory, no cushion
- **Summer driving season approaching** — gasoline demand is about to seasonally peak, not trough
- **"Rockets and feathers" asymmetry** — retail/wholesale prices rise fast on shocks, fall slow on relief. ~20-day lag to flow through (per REFINERY_UTILIZATION_MAR2026)

### The specific single-point exposures
- **ULSD (diesel):** Port Arthur diesel hydrotreater offline. US diesel demand is inelastic (freight, ag, rail, military). **Diesel crack should stay tightest longest.**
- **Jet fuel:** Global jet supply already at 44-month-high wholesale price. Major carriers don't hedge. **Jet crack stickiest — but not tradeable directly in equity.**
- **Gasoline:** Geelong gone (Australia), California PADD 5 structurally shrinking (Wilmington + Benicia = 284K bpd gone). **Gasoline crack sticky regionally but less globally.**

---

## THE TRADE CANDIDATES

### Refiners RANKED by Phase-2 alpha potential

| Ticker | Name | Capacity | Damage Exposure | Thesis Fit |
|---|---|---|---|---|
| **MPC** | Marathon Petroleum | ~3M bpd | Jan 12 Galveston Bay alky fire (resolved) | **BEST CANDIDATE** — large, diversified, no active damage |
| **PSX** | Phillips 66 | ~2M bpd | Borger TX (resolved), Wilmington CA closing | Good — PADD 5 exit is long-term structural gain |
| **DINO** | HF Sinclair | ~680K bpd | No major damage logged | Smaller, potentially overlooked |
| **VLO** | Valero | ~3.2M bpd | **Port Arthur 380K + Ardmore (resolved) + Benicia closing** | **PROBLEMATIC** — own facility damaged, can't capture full crack |
| **PBF** | PBF Energy | ~1M bpd | West coast turnarounds | Mixed |

**Counter-intuitive insight:** Valero (VLO) is **the WORST Phase-2 refiner play** despite being most exposed to the Port Arthur diesel crack, because **its own Port Arthur unit is down** — they can't sell into the elevated crack. Marathon (MPC) and Phillips 66 (PSX) capture the crack WITHOUT the damage offset.

### The pair / spread structure

**Core trade:** Long MPC or basket (MPC + PSX + DINO) / Short USO or WTI proxy
- Target beta neutralization: size short leg to match long leg's oil beta (~0.5-0.7 for refiner equities)
- Hold window: **2-4 weeks from confirmed Phase-2 trigger** — expansion window before crack compression
- Exit: when product prices catch down to crude (monitor wholesale gasoline/diesel vs NYMEX)

**Alternative structures:**
- **Crack spread futures** (CME RBOB-Crude or ULSD-Crude) — pure exposure, no equity noise. Requires futures brokerage.
- **Long XLE short USO** — blunter; XLE has producers AND refiners, so decoupling signal is diluted
- **Long refiner call spreads** — captures upside asymmetrically, IV is elevated but refiner IV lower than USO IV (LESSONS #15 applies less here than on crude puts)

### Entry trigger (when to put it on)
1. **Talk-2 announcement with signed framework** (not just verbal agreement)
2. AND Dated Brent prints for Apr 15-17 show physical market cracking (Dated <$115)
3. AND Hormuz physical flow confirmed — Lloyd's List shows tanker transits resuming, not just rhetoric
4. **NOT today (Apr 17)** — physical market isn't confirming paper. Today's -12% is announcement volatility, not Phase-2 confirmation.

### Exit trigger
- Wholesale gasoline (RBOB) crack compresses to <$15/bbl (from current $22+)
- OR crude rebounds above $95 (means Phase-2 was wrong, reverse the whole trade)
- OR 6 weeks elapsed (crack spreads historically normalize within this window post-shock resolution)

---

## RISKS / WHAT KILLS THIS TRADE

### 1. Phase-2 doesn't materialize (Path A wins)
- Ceasefire fails Apr 22, strikes resume, Hormuz closes further
- Crude goes UP, refiner stocks go DOWN (demand destruction fear)
- Full reversal of setup
- **Mitigation:** don't enter until PHYSICAL Dated Brent confirms, not paper futures

### 2. Refiners restart faster than expected
- Port Arthur's hydrotreater back online in 2-3 weeks (not 6-8)
- Gulf refineries have spare units that come back online with crude
- Crack spreads compress faster than modeled → window closes to 1-2 weeks
- **Mitigation:** tighter hold window; watch Port Arthur restart news daily

### 3. Consumer demand destruction hits product demand
- If Phase-2 is driven by demand collapse (not resolution), product prices fall WITH crude
- Crack spreads don't expand — they stay flat or compress
- This is the Hamilton-analog risk; see `demand_destruction/HAMILTON.md`
- **Mitigation:** check EIA gasoline YoY, ATA truck tonnage, airline capacity. If demand indicators turn negative while crude falls, don't enter.

### 4. China / India refiner surge undercuts US/AU/EU refiners
- If Asian refiners ramp up to absorb returning crude, global product supply normalizes faster
- Our tracker has ZERO India/China refinery data — **this is a data gap, not confirmed absence**
- **Mitigation:** actively chase Indian/Chinese refinery operational data before entering

### 5. Refinery equities already priced this
- Refiners have rallied hard through Q1 alongside crack spreads
- MPC, VLO, PSX already near multi-year highs
- "Buy the decoupling" may already be priced in via YTD refiner outperformance
- **Mitigation:** check MPC/USO ratio vs 6-month, 12-month — if already at highs, the decoupling trade has been front-run

---

## METRICS TO TRACK DAILY

| Metric | Current (Apr 17) | Phase-2 trigger watch | Trade entry watch |
|---|---|---|---|
| Dated Brent (physical) | ~$132 (Apr 9-11) | <$115 = cracking | <$110 = trigger |
| Brent M1-M3 spread | ~$8-12 | <$5 = resolution | <$3 = full flush |
| ULSD crack spread (GY) | $25.83 (early Mar) | Stable or rising | Rising on crude down |
| 3-2-1 crack (LLS) | $28.91 (early Mar) | Stable | Rising on crude down |
| VLO/USO ratio | [track daily] | Neutral | Rising (decoupling) |
| MPC/USO ratio | [track daily] | Neutral | Rising (decoupling) |
| Refiner IV (vs historic) | TBD | TBD | Lower = better for long calls |

---

## HISTORICAL ANALOGS

### 2022 Russia/Ukraine shock → unwind
- Feb-Jun 2022: crude rallied to $120+, crack spreads blew out to $60+
- Jun-Sep 2022: crude fell from $120 to $80, crack spreads stayed at $40+ for ~8 weeks before compressing
- Refiner equities (VLO, MPC) outperformed XLE by 15-30% during the Jun-Sep window
- **This is the closest analog for what Phase-2 unwind should look like**

### 2008 commodity super-cycle
- Jul-Dec 2008: crude fell from $147 to $33 in 5 months
- Crack spreads compressed alongside crude as **demand destruction** was the driver, not resolution
- Refiner equities underperformed — this was NOT a decoupling regime
- **Cautionary tale:** if Phase-2 is demand-driven not resolution-driven, decoupling fails

### 2014-2016 shale glut
- Crude fell from $110 to $27 over 18 months
- Gradual, not shock — crack spreads stayed in normal ranges
- Refiner equities tracked crude
- **Not analogous** — our situation is shock-resolution, not secular oversupply

---

## NEXT STEPS

1. **Set up VLO/USO and MPC/USO ratio charts** — need baseline for entry signal
2. **Track Port Arthur restart news daily** — primary catalyst for crack compression
3. **Chase Indian/Chinese refiner data** — biggest blind spot (agent dispatched Apr 17)
4. **If Phase-2 trigger confirms, produce trade proposal with sizing + specific entry structure** — this doc is thesis, not proposal
5. **Monitor post-Apr-17 incident cadence** — if refinery strikes continue, Phase-2 is theater and trade is off

---

## LIVE CONFIRMATION — Apr 17 intraday tape

Checked refiner equities vs crude live at ~12:30 EDT (the same "announcement volatility" session):

| Ticker | Change | Ratio to USO |
|---|---|---|
| USO (crude proxy) | **-9.71%** | baseline |
| **MPC** (Marathon — no active damage) | **-5.01%** | **0.52** — down half as much as crude |
| **PSX** (Phillips 66 — modest exposure) | **-4.38%** | **0.45** — best decoupling |
| **DINO** (HF Sinclair) | **-5.85%** | 0.60 |
| **VLO** (Valero — has Port Arthur damage) | **-8.46%** | 0.87 — tracking crude closely, **as thesis predicts** |
| **PBF** | **-14.36%** | 1.48 — WORSE than crude (investigate — company-specific issue?) |
| XLE (broad energy) | -3.53% | 0.36 — has producer exposure that gains on lower crude |

**Two things to notice:**
1. **The decoupling is already visible on an announcement day** — MPC and PSX both down ~half as much as crude. Market is pricing the thesis in real-time.
2. **The MPC > VLO rank works as predicted** — VLO is tracking crude much closer (0.87 ratio) because its damaged Port Arthur asset can't capture the crack. MPC at 0.52 is the divergence we predicted.

**What this means for entry:**
- The alpha isn't "be long refiners" — that's already moving. The alpha is **MPC (or PSX) LONG / VLO SHORT** — the inter-refiner spread. This captures the damage-differential directly.
- Or: **MPC LONG / USO SHORT** — still captures the product/crude spread.
- **Position PBF carefully** — down 14% is an outlier; don't assume without company-specific diligence.

This is a same-day snapshot, not a pattern. Need 3-5 sessions to confirm the ratio holds.

---

## 6-MONTH BASELINE — Apr 17 PM (resolves the "already priced in?" caveat)

Pulled via `scripts/refiner_ratios.py` — 6-mo daily close-to-close ratios vs USO:

| Ticker | Today ratio | 6-mo μ | 6-mo σ | z-score | 1d Δ | Signal |
|---|---|---|---|---|---|---|
| PSX | 1.348 | 1.795 | 0.224 | **-1.99** | +3.82% | 🟢 REVERTING |
| MPC | 1.842 | 2.396 | 0.304 | **-1.83** | +2.43% | 🟢 REVERTING |
| DINO | 0.493 | 0.648 | 0.100 | **-1.56** | +3.11% | 🟢 REVERTING |
| VLO | 1.927 | 2.339 | 0.229 | **-1.80** | +0.33% | 🟡 COMPRESSED |
| PBF | 0.320 | 0.430 | 0.053 | **-2.06** | -5.47% | 🟡 COMPRESSED |

**Finding:** The honest caveat above ("may already be trading at decoupling premiums") is **resolved in the thesis's favor.** All 5 refiner/USO ratios are 1.5–2.1 standard deviations BELOW their 6-month mean — the opposite of priced-in. Through the Hormuz squeeze (Nov 2025–Apr 2026), USO materially outperformed refiners → ratios compressed.

**Reframe:** The trade isn't "buy refiners because decoupling is new" — it's **"buy compressed refiner/crude ratios because mean reversion back toward the 6-mo average delivers 30-50% relative outperformance as crude flushes in Phase 2."** Today's day-one move (MPC +2.4%, PSX +3.8%, DINO +3.1% ratio gains) is the start of that reversion, not the whole of it.

**VLO as predicted:** only +0.33% ratio gain despite thesis calling it the weakest refiner play (Port Arthur damage). Consistent.

**PBF still an outlier** — ratio down on a day refiners as a group reverted up. Requires company-specific dig before including in any trade.

**Reversion target:** if ratios snap halfway back to 6-mo mean, implied outperformance of MPC vs USO ≈ +15%, PSX vs USO ≈ +17%. Full reversion ≈ +30% each.

---

## BOTTOM LINE FOR WILL

Today (Apr 17) is NOT the entry signal. The -12% intraday paper move is announcement volatility; physical market is not confirming. But **this is the setup window** — the thesis says that IF Phase-2 becomes real in the next 2-3 weeks, refiner equities (MPC best, PSX second, NOT VLO) will materially outperform crude on the way down for a 2-4 week window. Position size should be modest (2-4% of oil-allocated capital) because it's a transition-window trade, not a core long.

The trade would be **complementary to existing USO long** — doesn't require exiting USO before Phase-2, because if Phase-2 arrives, USO gets exited anyway per `PHASE2_EXECUTION_2026-04-17.md` playbook. Refiner long is what you put on AS you exit USO.

**Key honest caveat:** I have not lived-tested this against refiner equity pricing today. VLO/MPC may already be trading at decoupling premiums that price this thesis in. First analytical step before any trade: pull MPC/USO, PSX/USO, VLO/USO ratios and compare to 6-mo / 12-mo history.
