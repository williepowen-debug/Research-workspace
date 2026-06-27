# ORACLE STATUS

**Updated:** 2026-06-27 13:25Z — live pull + trajectory refresh + roll-watch | prior: 2026-06-22
**Domain:** Prediction-market monitoring (Polymarket) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` (Gamma API). Time series → `workbook/ODDS_LOG.tsv`; daily trajectory → `workbook/HISTORY.tsv` (4,796 rows, 33 mkts). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟡 — crowd & fleet still converged on **calm + risk-on** on the macro axis. Two moving pieces: (1) the Fed — a post-FOMC **hawkish overshoot is cooling** (hike-2026 off its ~66% peak to 52%) while higher-for-longer stays pinned (no-cuts 80%); (2) **Iran is a TWO-AXIS split** — nuclear/war de-escalated, but the **Hormuz/shipping axis is actively re-escalating** (Iran struck a ship 6/25, US retaliated 6/26; crowd prices continued attacks 80%+). Macro calm, geopolitical-oil tail live.

---

## Alerts (read first)

**🟢→🟡 SHIFT — Fed hawkish *overshoot* is cooling (NOT a dovish pivot).** Hike-in-2026 **51.5% (Δ7d −14.0, $3.0M deep)** — but `history` shows **Δ30d +21**: it spiked to a ~66% high ~6/20 right after the 6/17 FOMC dots, and has since retraced. My 6/22 reading (61.5%) was near that peak — so the −14/7d is a *pullback within an uptrend*, not a reversal. Corroborated by the rate dist: the **4.0% end-2026 bucket crashed −12.8/7d to 22.1%**, with **3.75% now modal (31.1%)**. July-hike 18.1% (−6.6). **No-cuts holds 79.5% (Δ30d +13, still climbing)** → higher-for-longer is the durable signal; only the *active-hike premium* is deflating. Net for KRE/OZK/WAL CRE-refi: pressure intact, marginal tail easing. → LIQUID, HENRY (via NEXUS_BRIEF).

**🟡 CONFIRM — June CPI consolidating on a *contained* 3.8%.** Modal bucket "3.8%" **52.7% (Δ7d +12.2)** while the 3.9%/4.0% buckets *fell* (−6.5/−0.8). So the +12.2 is rising *certainty on a contained print*, not more inflation — same dovish-at-margin direction as the hike fade. Entropy collapsing onto one rung. Resolves 2026-07-15 → surprise vs 3.8% is the tell. → HENRY.

**🟡 SENTIMENT — Risk-on rotation entrenching.** Best-asset-2026 → **S&P 500 56% (Δ7d +7.5, Δ30d +21)**, Gold fading **26% (−6.0)**, BTC 16.5%. NEH 83.5% (+1.5). BTC-dip-$40K 30.0% (Δ1d −6.0). Crowd firmly risk-on; complacency consistent with the de-risked fleet (not contrarian). → RED, HENRY, VIOLET.

**🟠 IRAN/OIL — TWO-AXIS split (corrected 6/27 via movers-discovery): nuclear de-escalated, but the SHIPPING axis is actively RE-ESCALATING.**
- **Nuclear/grand-war axis = de-escalated:** enrichment-by-Jun30 **1.4%** (res 6/30, dead clause), war-premium WTI-$100-Jun **0.4%** (res 7/1). Deal-components event: Reconstruction 49% / Enrichment-cap 41% / 1yr-moratorium 31.5% / Surrender 19%.
- **Hormuz/shipping axis = RE-ESCALATING (the markets I missed at boot):** Iran's IRGC drone-struck the Singapore-flagged *Ever Lovely* in Hormuz **6/25** despite the 60-day toll-free deal; **US retaliated with strikes 6/26**. Crowd now prices **"Iran successfully targets shipping" 81.5% by-Jun30 → 88.5% by-Jul7 → 93.5% by-Aug31** (newly-created 6/25, ~$260K event). Hormuz-normal-Jun30 collapsed to **3.5% (−7.3/1d)** — *this attack is why*. Hormuz-normal-Jul15 26.5%; normal-by-Dec31 86.5% (year-end normalization still expected).
- **The crowd's read:** shipping harassment ≠ oil-supply shock — continued attacks priced 80%+ while WTI-$100 stays dead (oil reroutes via the Omani-side corridor; one-drone, no-casualties harassment, not a strait closure). **The oil tail is priced through *transit disruption*, not a war-premium spike.** → HAWK/BRENT energy red-team (added `iran-targets-shipping` to watchlist).

**⚪ Citi Q2 provision >$2.9B 71.5% (Δ7d +22.5) — DIAGNOSTIC ONLY ($210 liq).** Too thin to route as signal; watch the drift not the level vs the actual 7/14 print. BAC >$1.4B 37.5% (+0.5). → REGINALD/CARL (FYI).

---

## Signal Dashboard (live 2026-06-27T13:25Z)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: HIKE in 2026** | T1 | **51.5%** | −1.0 | **−14.0** | $3.0M | $202K | overshoot cooling; Δ30d **+21** (off ~66% peak) |
| Fed: hike at July mtg | T1 | 18.1% | +0.6 | −6.6 | $6.3M | $458K | active-hike premium deflating |
| **Fed: NO cuts 2026** | T1 | **79.5%** | +0.2 | −1.6 | $5.6M | $120K | higher-for-longer pinned (Δ30d +13) |
| Fed: 1 cut 2026 | T1 | 12.5% | — | — | $1.9M | $158K | mirror |
| Fed funds end-2026 (modal 3.75%) | T1 | 31.1% | +2.4 | +1.1 | $525K | $10.6K | 4.0% bucket −12.8/7d → modal slid down |
| US inflation >5% 2026 | T1 | 12.5% | — | −1.0 | $271K | $21.6K | tail contained (Δ30d −17) |
| June CPI modal "3.8%" | T1 | **52.7%** | +0.4 | **+12.2** | $90.9K | $15.6K | consolidating on contained print (res 7/15) |
| US recession 2026 | T1 | 11.0% | +0.5 | −1.5 | $1.6M | $24.0K | calm; Δ30d −8, steady slide |
| US bank failure by Jun30 | T1 | 6.1% | −0.4 | −0.4 | $14.5K | $3.4K | ⚠️thin ⏳3d |
| Major bank bailout <2027 | T1 | 9.5% | — | −4.0 | $3.7K | $1.7K | ⚠️thin |
| Which banks fail Jun30 (top) | T1 | 0.5% | +0.4 | +0.1 | $15.3K | $6.2K | ⏳3d, no name priced |
| Citi Q2 prov >$2.9B | T1 | 71.5% | −0.5 | +22.5 | $6.2K | $210 | ⚠️thin diagnostic (res 7/14) |
| BAC Q2 prov >$1.4B | T1 | 37.5% | — | +0.5 | $4.4K | $578 | ⚠️thin diagnostic (res 7/14) |
| US unemployment ladder (top) | T1 | 18.1% | +8.6 | +8.8 | $118K | $1.6K | ⚠️thin ⏮stale — discount the spike |
| Hormuz normal by Dec31 | T1 | 86.5% | −2.5 | −0.5 | $3.1M | $291K | year-end normalization expected |
| China invade Taiwan <2027 | T1 | 5.5% | −0.2 | −0.9 | $37M | $573K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 79.0% | — | +2.5 | $171K | $10.3K | ⏮stale-date |
| Iran ends enrichment Jun30 | T2 | 1.4% | — | −3.1 | $11.9M | $247K | ⏳3d dead clause |
| WTI hits $100 Jun (war) | T2 | 0.4% | +0.1 | −3.0 | $937K | $60.6K | ⏳4d war-premium dead |
| US invade Iran <2027 | T2 | 13.0% | +0.5 | −0.5 | $38.9M | $286K | deep, stable |
| Iran leadership change Dec31 | T2 | 15.5% | −1.0 | — | $3.0M | $80K | easing (Δ30d −13) |
| Russia-Ukraine ceasefire Dec31 | T2 | 40.5% | — | −6.5 | $1.9M | $133K | ceasefire odds slipping |
| China-Philippines clash <2027 | T2 | 13.5% | — | −5.0 | $1.2M | $108K | SCS flashpoint > Taiwan |
| BOJ July decision (hold top) | T2 | 95.5% | +0.1 | −1.7 | $19.4K | $8.2K | hold near-certain → carry catalyst Sept |
| Bitcoin dip $40K by Dec31 | T2 | 30.0% | −6.0 | +2.5 | $1.0M | $53.5K | BTC strength (Δ1d −6) |
| AI bubble burst 2026 | T2 | 18.6% | −0.2 | −1.5 | $2.3M | $16.7K | easing |
| MicroStrategy bankruptcy <2027 | T2 | 6.5% | −0.5 | −1.5 | $179K | $15.5K | modest crypto stress |
| US debt default <2027 | T2 | 1.7% | −0.8 | −1.3 | $15.5K | $52.6K | control |
| Hormuz normal by Jun30 | T2 | 3.5% | −7.3 | −5.9 | $38.1M | $213K | ⏳3d near-term disruption |
| **Nothing Ever Happens 2026** | T3 | **83.5%** | +0.5 | +1.5 | $632K | $40.5K | complacency holds |
| Best asset 2026 (S&P top) | T3 | 56.0% | +2.0 | +7.5 | $178K | $23.8K | risk-on (Δ30d +21) |
| FL Cat-4 hurricane <2027 | T3 | 33.5% | — | +3.5 | $333K | $1.7K | ⚠️thin — season-watch |
| FL Cat-5 hurricane <2027 | T3 | 14.0% | −1.5 | −0.5 | $138K | $1.3K | ⚠️thin — season-watch |

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏳ = resolves ≤7d. ⏮ = live market w/ stale endDate (fetcher trusts `closed`).

---

## Trajectory (daily CLOB backfill — `polymarket.py history`)

The durable view — *how* each figure moved, not just today's level (survives stale point-in-time baselines). Full series → `workbook/HISTORY.tsv`.

| Market | Now | Δ30d | Δ90d | Shape |
|--------|--:|--:|--:|------|
| Fed: NO cuts 2026 | 80% | **+13** | +41 | climbing — higher-for-longer entrenching |
| Fed: HIKE in 2026 | 52% | **+21** | +28 | **uptrend, off ~66% peak (6/20)** — pullback ≠ pivot |
| Fed: hike July mtg | 18% | +14 | +9 | recent jump then fade |
| Fed funds dist (modal 3.75%) | 31% | −12 | −3 | modal slid down off 4.0% |
| Best asset → S&P 500 | 56% | **+21** | +38 | risk-on rotation, gold fading |
| June CPI "3.8%" | 53% | — | — | +45 since create — consolidating on contained print |
| US recession 2026 | 11% | −8 | −24 | steady 9-mo slide |
| US inflation >5% | 12% | −17 | −14 | tail collapsing |
| Iran enrichment Jun30 | 1% | −21 | −27 | ⚡ dead clause |
| Hormuz normal Jun30 | 4% | −36 | — | ⚡ near-term disruption persists |
| Hormuz normal Dec31 | 86% | +2 | — | year-end normalization expected |
| Citi Q2 prov >$2.9B | 72% | — | — | +21 since create (⚠️thin) |

⚡ = `history` round-trip flag. *Re-run: `python3 AGENTS/ORACLE/scripts/polymarket.py history --write`*

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Fed path (hawkish cooling) | 3 | 🟡 | hike 52% (−14/7d but +21/30d), no-cuts 80% | hike re-breaks >66% OR a 2026 hike prints; OR no-cuts <70% (dovish turn) |
| 2 | Risk-on rotation | 2 | 🟡 | S&P best-asset 56% (+21/30d), NEH 83.5% | NEH <30% OR gold re-takes lead |
| 3 | Iran shipping re-escalation | 2 | 🟠 | shipping-attacks 81%+ fwd (Ever Lovely 6/25, US strikes 6/26); Hormuz-Jun 3.5% | WTI-$100 (Jul) >10% (supply shock) OR strait full-closure OR deal-surrender >40% |
| 4 | Bank cluster (agree low) | 1 | ⚪ | ≤9.5% thin; Citi-prov 72% thin-diagnostic | failure vol >$50K OR provisions miss hard 7/14 |
| 5 | Recession (converged) | 1 | ⚪ | 11%, fleet agrees | market turns up OR fleet re-arms cyclical axis |

**State:** Crowd & fleet remain converged on calm + risk-on. ORACLE's forward value: (1) track whether the Fed-hike pullback is just overshoot-correction or the start of a dovish turn (no-cuts <70% would confirm the latter), (2) watch whether HENRY's **dormant structural credit axis re-ignites before the crowd prices it** (the real edge), (3) Iran/Hormuz re-escalation tail via the new deal-component event.

---

## Maintenance flags

- **Roll-watch executed (6/27):** 5 June markets resolve 6/30–7/1. Replacements located + added to `watchlist.tsv`: Iran-enrichment **Jul-31** (7.5%) + **Dec-31** (29.5%) + **US-Iran-deal-2026 event** (deal components); **WTI-July ladder event** ($80 31%→$130 5%); **Hormuz-normal-Jul-15** (26.5%, $4.5M deep); **which-banks-fail-by-EOY-2026 event** (BAC 7.4%, GS 2.5%). **No July single-binary bank-failure market exists yet** — keep watching. June markets kept tracking through 6/30 resolution, drop after.
- **Trajectory refreshed:** `HISTORY.tsv` 4,796 daily rows / 33 markets (`history --write` 6/27).
- **LIQUID figure-check (6/22) closed-ish:** LIQUID picked it up (now in their `processed/`), no formal verify-back; the Polymarket July-hike has since moved 23%→18% anyway.
- **ORACLE now wired into fleet** (WALTER REGISTRY tier-2 row + PROME ownership statement) — the 6/18 wire-in ask is satisfied; 3 stranded 6/18 outbox files archived to `delivered/`.
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.
- **Push policy:** auto-push at closeout via `scripts/safe-push.sh` (ff-gated, single-machine) — CLAUDE.md step 14 updated to match.
- **Kalshi WIRED (6/27):** 2nd real-money source (`scripts/kalshi.py`, `kalshi_watchlist.tsv`, `KALSHI_ODDS_LOG.tsv`). Corroborates Polymarket (recession 10 vs 11, July-hike 18 vs 18) + adds clean U3/CPI reads. Creds outside repo. EXECUTE now runs both fetchers. Gap-fills (CRE default, CC delinquency, Fed facility) pending event-open; no VIX on Kalshi.

---

## BOTTOM LINE

The crowd is **still calm and now firmly risk-on** — S&P best-asset 56% (+21/30d), gold fading, NEH 83.5%, recession 11%, bank cluster benign. The one live mover is the **Fed**: a post-FOMC hawkish *overshoot* is correcting — hike-2026 off its ~66% June-20 peak to 52% (−14/7d) — but the trajectory shows the 30-day trend is still **up (+21)** and no-cuts is pinned at 80% (+13/30d). So this is overshoot-cooling, **not a dovish pivot** (pulling the trajectory is what kept me from misreading the −14 against a peak baseline). Iran is a **two-axis split** — nuclear/grand-war de-escalated (enrichment 1.4%, WTI-$100 0.4%) but the **Hormuz/shipping axis is actively re-escalating** (Iran struck the *Ever Lovely* 6/25, US retaliated 6/26; crowd prices continued attacks 80%+ while keeping the oil war-premium dead — harassment, not a supply shock). A 6/27 movers-discovery surfaced this (my boot watchlist missed it) plus confirmed the macro board is otherwise dead-flat. Honest call: macro = no contrarian fire (watch no-cuts <70% for the dovish tell, and the dormant credit axis); the live tail is the **shipping/Hormuz re-escalation** priced through transit disruption, not a $100 oil spike.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log`*
