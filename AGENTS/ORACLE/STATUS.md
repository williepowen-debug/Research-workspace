# ORACLE STATUS

**Updated:** 2026-07-02 (Thu ~13:30 ET) — live pull (both platforms) + trajectory refresh + roll-watch (6 June mkts dropped, 5 repinned/added) | prior: 2026-06-27
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` (Gamma API) + `scripts/kalshi.py pull --log` (CFTC exchange, RSA-PSS). Series → `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`; daily trajectory → `workbook/HISTORY.tsv` (4,856 rows, 36 mkts). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟡 — crowd & fleet still converged on **calm + deepening risk-on**. Three live pieces: (1) the **Fed hawkish overshoot is genuinely rolling over** — July hike essentially priced out, hike-2026 broke <50, big-hike tail dying — but settling onto **HOLD-all-year, not a dovish pivot** (no-cuts still 77.5%); (2) **Iran two-axis CONFIRMED with physical data** — Hormuz traffic materially reduced and staying reduced through July, diplomacy collapsing, a new US-blockade tail — **yet oil prices zero supply premium**; (3) **risk-on at a series high** (S&P best-asset 67.5%, +49/90d). Macro calm, geopolitical-oil tail live-but-contained.

---

## Alerts (read first)

**🟡 FED — active-hike overshoot rolling over onto HOLD (NOT a dovish pivot).** July-hike **9.7% (Δ1d −9.0, Δ7d −10.5, $9.3M)** — essentially priced out. Hike-in-2026 **46.5% (Δ7d −6.0)** broke below 50. End-2026 dist: **modal = HOLD 3.75% (25.5%)**, one-hike 4.0% (24.2%), **multi-hike ≥4.5% faded to 8.0% (Δ7d −3.1)** — the big-hike tail is dying. **Kalshi corroborates:** July-hike (>3.75%) 14% (Δp −6), >4.00% 1%. BUT **no-cuts holds 77.5% (Δ7d −1.8)** and trajectory shows hike-2026's 30-day trend merely *flattening* (Δ30d +11, down from +21) — so higher-for-longer is intact; the market removed the *hike urgency* and is pricing a long hold. **Dovish tell = no-cuts <70% (not fired).** CRE/OZK/WAL-refi pressure intact, marginal hike-tail easing. → LIQUID, HENRY.

**🟠 IRAN/OIL — two-axis CONFIRMED with physical-traffic data; shipping disrupted, oil calm.**
- **Shipping axis (real & persistent):** Hormuz traffic materially reduced — "20-40 avg daily transits" **97.2% (+65.8/7d)**, "60 ships any day by Jun30" collapsed to **0.9%**; forward ships-ladder-by-Jul31 shows 40/day 86%, 60/day 55.5%, **100/day (normal) only 9%** → reduced regime persists through July. Hormuz-normal-Jul15 **8.5% (Δ7d −29)**.
- **Diplomacy fading:** US-Iran deal-components top **38.5% (Δ7d −25)**; enrichment-by-Dec 30% (Δ30d −24). The negotiated-settlement path is losing the crowd.
- **Forward attacks reset (by-Jun27 attack resolved YES):** fresh "Iran targets shipping again" by-Jul7 14% / by-Jul31 46.5% / by-Aug31 69% — ~coin-flip July, likely by end-Aug.
- **NEW escalation tail:** "US announces blockade on Iran" **12.5% by-Jul31 / 30.5% by-Dec31** ($780K deep). This is the regime-change watch — harassment → supply shock.
- **YET oil prices ZERO supply premium:** WTI-$100-July **1.6%**, $80-July **11.5%** (both −48/−55 over 7d). Strait open, tankers reroute/reduced-volume, no barrels lost. **The oil tail remains priced through transit disruption, not a war-premium spike.** → HAWK/BRENT energy red-team.

**🟠 SENTIMENT — risk-on at a series high; complacency deepening.** Best-asset-2026 → **S&P 500 67.5% (Δ1d +5.0, Δ7d +13.0, Δ30d +28, Δ90d +49)** — sitting at the top of its range [9-68]. **Nothing-Ever-Happens 84.0%** (Δ30d +10, Δ90d +48, at series high). Gold fading, BTC-above-$50K near-certain. This is the deepest, most-persistent trend on the board — a full-quarter risk-on entrenchment. The more extended, the more there is to unwind if the dormant structural-credit axis fires. Contrarian tell = NEH <30% (not close). → RED, VIOLET, HENRY.

**🟡 MACRO PRINTS — June U3 finalized ~4.2%, June CPI contained.** Kalshi **June U3 >4.2% 82% / >4.3% 25% [finalized today 7/2]** → ~4.2%, a mild labor tick (LABOR/HENRY own the analysis; ORACLE observes the market converged). **June CPI contained:** Kalshi >3.6% 94% / >3.8% 31% (Δp +8); PM modal-3.8% **45.9% (Δ7d −6.8)** — distribution spreading with a modest upside tail, still 3.6-3.8. Resolves 7/14-15; surprise vs 3.7-3.8 is the tell. → HENRY, LABOR.

**⚪ BANK PROVISIONS — diagnostic drift into 7/14 (thin).** Citi Q2 prov >$2.9B **60.0%** (was 71.5% on 6/27, $434 liq); BAC >$1.4B **43.0% (Δ7d +6.0, $124 liq)**. Both too thin to route as signal — watch drift vs the actual 7/14 print, not the level. Bank cluster otherwise benign (bailout 11%, named-EOY 2.9%). → REGINALD/CARL (FYI).

---

## Signal Dashboard (live 2026-07-02T17:26Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: hike at July mtg** | T1 | **9.7%** | **−9.0** | **−10.5** | $9.3M | $737K | July hike priced out (Kalshi 14%) |
| **Fed: HIKE in 2026** | T1 | **46.5%** | — | **−6.0** | $3.4M | $166K | broke <50; trend flattening (Δ30d +11) |
| **Fed: NO cuts 2026** | T1 | **77.5%** | −0.6 | −1.8 | $5.7M | $114K | higher-for-longer pinned; dovish tell <70% |
| Fed: 1 cut 2026 | T1 | 14.5% | +3.0 | +1.0 | $1.9M | $152K | cut odds ticking up |
| Fed funds end-2026 (modal 3.75% HOLD) | T1 | 25.5% | — | −2.5 | $527K | $12K | one-hike 4.0% 24.2%; ≥4.5% 8.0% (−3.1) |
| US inflation >5% 2026 | T1 | 13.5% | +1.0 | +1.0 | $274K | $23K | tail contained (Δ30d −18) |
| June CPI modal "3.8%" | T1 | 45.9% | −0.9 | **−6.8** | $98K | $18K | dist spreading; contained (res 7/15) |
| US recession 2026 | T1 | 11.5% | — | +1.0 | $1.6M | $37K | calm (Kalshi 8.0%, Δp −4) |
| Major bank bailout <2027 | T1 | 11.0% | — | +1.5 | $3.7K | $2.0K | ⚠️thin, benign |
| Which banks fail EOY (top) | T1 | 2.9% | −0.3 | −2.6 | $3.1K | $9.7K | no name priced |
| Citi Q2 prov >$2.9B | T1 | 60.0% | +1.0 | −0.5 | $6.3K | $434 | ⚠️thin diagnostic (res 7/14) |
| BAC Q2 prov >$1.4B | T1 | 43.0% | — | +6.0 | $4.4K | $124 | ⚠️thin diagnostic (res 7/14) |
| US unemployment ladder (top) | T1 | 11.1% | −11.7 | +1.1 | $119K | $2.4K | ⚠️thin ⏮stale-date — discount |
| Hormuz normal by Dec31 | T1 | 82.5% | +1.0 | −6.0 | $3.4M | $420K | year-end normalization eroding |
| China invade Taiwan <2027 | T1 | 3.5% | — | −2.1 | $37.7M | $834K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 78.5% | — | −1.0 | $172K | $12K | ⏮stale-date |
| **Iran targets shipping (by-Aug31)** | T2 | **69.0%** | −16.5 | — | $5.7K | $20K | reset fwd window (by-Jul31 46.5%) |
| **US blockade on Iran (by-Dec31)** | T2 | **30.5%** | — | −6.5 | $113K | $73K | NEW escalation tail (deep) |
| Hormuz ships-ladder by-Jul31 (40/day) | T2 | 86.1% | −8.4 | — | $63K | $72K | 60/day 55.5%, 100/day 9% |
| WTI hits $100 (Jul) — war premium | T2 | 1.6% | −1.5 | −48.9 | $39K | $127K | oil war-premium dead |
| WTI hits $80 (Jul) — elevated | T2 | 11.5% | −6.5 | −55.5 | $28K | $16K | oil calm, no supply shock |
| Hormuz normal by Jul15 | T2 | 8.5% | −5.0 | −29.0 | $5.9M | $289K | near-term disruption priced |
| Iran ends enrichment by Dec31 | T2 | 29.5% | — | −1.0 | $1.2M | $69K | deal path fading (Δ30d −24) |
| Iran ends enrichment by Jul31 | T2 | 3.6% | −0.5 | −3.9 | $812K | $91K | dead near-term |
| US invade Iran <2027 | T2 | 13.5% | — | — | $39.1M | $533K | deep, stable |
| Iran leadership change Dec31 | T2 | 15.5% | — | −2.0 | $3.0M | $91K | easing (Δ30d −12) |
| Russia-Ukraine ceasefire Dec31 | T2 | 41.5% | −2.0 | −2.5 | $1.9M | $158K | ceasefire odds slipping |
| China-Philippines clash <2027 | T2 | 13.5% | — | — | $1.2M | $114K | SCS flashpoint > Taiwan |
| BOJ July decision (hold top) | T2 | 97.2% | +0.9 | +5.3 | $32K | $23K | hold near-certain (Δ30d +25) |
| Bitcoin dip $40K by Dec31 | T2 | n/a | — | — | — | — | ⛔pin broke (no CLOB token) — repin pending; BTC >$50K near-certain |
| AI bubble burst 2026 | T2 | 17.8% | −1.2 | −1.3 | $2.3M | $21K | easing |
| MicroStrategy bankruptcy <2027 | T2 | 4.5% | −2.5 | −2.5 | $182K | $16K | modest crypto stress |
| US debt default <2027 | T2 | 3.4% | −0.1 | +0.9 | $16K | $5.3K | control |
| **Nothing Ever Happens 2026** | T3 | **84.0%** | −0.5 | +0.5 | $637K | $46K | complacency at series high |
| **Best asset 2026 (S&P top)** | T3 | **67.5%** | +5.0 | **+13.0** | $179K | $24K | risk-on (Δ30d +28, Δ90d +49) |
| FL: Cat-4 hurricane <2027 | T3 | 36.0% | −1.5 | +3.0 | $333K | $2.1K | ⚠️thin — season-watch |
| FL: Cat-5 hurricane <2027 | T3 | 16.0% | — | +1.5 | $138K | $2.0K | ⚠️thin — season-watch |

**Kalshi corroboration (2026-07-02T17:27Z):** recession 8.0% (Δp −4, 2.7M vol/834K OI); July-hike (>3.75%) 14% (Δp −6); >4.00% 1%; June U3 >4.2% 82% [finalized]; June CPI >3.6% 94% / >3.8% 31% (Δp +8).

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate. *BTC-dip $40K row is the Dec-31 dip market (repin pending; BTC currently strong).

---

## Trajectory (daily CLOB backfill — `polymarket.py history`, 4,856 rows / 36 mkts)

The durable view — *how* each figure moved, not just today's level. Full series → `workbook/HISTORY.tsv`.

| Market | Now | Δ30d | Δ90d | Shape |
|--------|--:|--:|--:|------|
| Best asset → S&P 500 | 68% | **+28** | **+49** | relentless risk-on, at series high [9-68] |
| Nothing Ever Happens | 84% | +10 | +48 | complacency at series high [30-84] |
| Fed: NO cuts 2026 | 77% | +8 | +39 | climbing (decel) — higher-for-longer entrenched |
| Fed: HIKE in 2026 | 46% | +11 | +23 | uptrend **flattening** (was +21/30d) — spike rolling over |
| Fed funds dist (modal 3.75% HOLD) | 26% | −10 | −3 | mass sliding down off the hike buckets |
| BOJ July hold | 97% | +25 | — | hold hardened |
| US recession 2026 | 12% | −10 | −24 | steady 9-mo slide |
| US inflation >5% | 14% | −18 | −12 | tail collapsing |
| Iran enrichment Dec31 | 30% | −24 | +1 | ⚡ deal path fading |
| Iran leadership change | 16% | −12 | −37 | ⚡ easing |
| Hormuz normal Jul15 | 8% | — | — | ⚡ near-term disruption persists |
| Hormuz normal Dec31 | 82% | +6 | — | year-end normalization (eroding −6/7d) |

⚡ = `history` round-trip/spiky flag (headline-driven). *Re-run: `python3 AGENTS/ORACLE/scripts/polymarket.py history --write`*

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Fed path (overshoot → HOLD) | 3 | 🟡 | July-hike 9.7% (−10.5/7d), hike-2026 46.5% (<50), no-cuts 77.5% | hike re-breaks >66% OR a 2026 hike prints; OR **no-cuts <70% (dovish turn)** |
| 2 | Risk-on rotation | 3 | 🟠 | S&P best-asset 67.5% (+49/90d, series high), NEH 84% | NEH <30% OR gold re-takes best-asset lead |
| 3 | Iran shipping disruption | 2 | 🟠 | traffic ~20-40/day (97%), reduced regime thru July, US-blockade tail 30.5% Dec; oil calm | **WTI-$100-Jul >10% (supply shock)** OR US-blockade fires OR strait full-closure |
| 4 | Bank cluster (agree low) | 1 | ⚪ | ≤11% thin; Citi-prov 60% / BAC 43% thin-diagnostic | failure vol >$50K OR provisions miss hard 7/14 |
| 5 | Recession (converged) | 1 | ⚪ | PM 11.5% / Kalshi 8.0%, fleet agrees | market turns up OR fleet re-arms cyclical axis |

**State:** Crowd & fleet remain converged on **calm + deepening risk-on**. ORACLE's forward value: (1) track whether the Fed overshoot-→-hold is the terminal read or the first leg of a dovish turn (**no-cuts <70%** confirms the latter), (2) watch whether HENRY's **dormant structural credit axis re-ignites before the crowd prices it** (the real edge — nothing pricing it yet), (3) the Iran shipping/Hormuz tail via the **US-blockade** escalation market + WTI-$100 supply-shock gauge.

---

## Maintenance flags

- **Roll-watch executed (7/2):** 6 June markets dropped (bank-failure-Jun30, named-bank-Jun30, enrichment-Jun30, WTI-$70/$100-Jun, Hormuz-normal-Jun30). **2 broken pins repinned** — WTI-July-ladder event (returned 100% RESOLVED) → two live legs ($100 war-premium 1.6%, $80 elevated 11.5%); iran-targets-shipping-Jun27 (resolved YES) → fresh forward event (by-Jul31 46.5%). **2 new adds** — US-blockade-on-Iran ($780K, 30.5% Dec) + Hormuz physical ships-transit ladder (40/day 86%). All verified resolving cleanly.
- **Kalshi creds PRESENT (fixed 7/2):** the CLAUDE.md 7/1 "creds MISSING" flag is stale — `~/.config/kalshi/{key_id.txt,private_key.pem}` both present + chmod 600; Kalshi lane LIVE. CLAUDE.md note corrected.
- **Trajectory refreshed:** `HISTORY.tsv` 4,856 daily rows / 36 markets (`history --write` 7/2).
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.
- **Kalshi gap-fills still pending event-open:** CRE default (KXCREDEFMAX), credit-card delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY) — the structural-credit-axis tells PM lacks. Re-check each session.
- **BTC-dip $40K** dashboard row needs a clean repin (Dec-31 market); BTC currently strong so low-priority.

---

## BOTTOM LINE

The crowd is **calm and firmly risk-on**, and the risk-on trend is now the deepest thing on the board — S&P best-asset 67.5% (+49/90d, at series high), NEH 84% (at series high), recession 11.5% (Kalshi 8%), bank cluster benign. The one macro mover is the **Fed**: the post-FOMC hawkish overshoot is **genuinely rolling over** — July hike priced out (9.7%/14% cross-platform), hike-2026 below 50, the multi-hike tail dying — but this is the market settling onto **HOLD-all-year, not a dovish pivot**: no-cuts is still pinned at 77.5% (the dovish tell is <70%, not fired) and the hike-2026 uptrend is *flattening*, not reversing. Iran is a **two-axis split now confirmed with physical data**: Hormuz traffic is materially reduced (~20-40/day, 97%) and expected to stay reduced through July, diplomacy is collapsing (deal-components −25/7d), a new US-blockade tail sits at 30.5% by year-end — **yet oil prices zero supply premium** (WTI-$100-July 1.6%). Honest call: macro = no contrarian fire (watch no-cuts <70% and the dormant credit axis); the live tail is the **shipping/Hormuz disruption**, priced through transit not a $100 oil spike, with the US-blockade market as the regime-change tripwire.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log`*
