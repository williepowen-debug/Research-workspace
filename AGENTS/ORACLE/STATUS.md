# ORACLE STATUS

**Updated:** 2026-07-31 (Fri, PM sweep ~20:45Z / 16:45 ET) — **BOTH 7/24 🔴 triggers RESOLVED BENIGNLY on FOMC + July resolution, BUT the afternoon sweep flushed out a decomposition surprise: Sept-mtg-specific hike market is deepening +4/1d to 56.5%** ($2.1M vol, deep) — a coin-flip TOWARD a Sept hike hidden under my aggregate Fed-HIKE-2026 66.5%. Amendment routed to LIQUID/HENRY. (1) **Fed re-arm UNFIRED** — hike-2026 71.5%(7/24)→**66.5%** on the 7/29 FOMC hold (9-3 hawkish; Kalshi hike-by-July finalized 18% no-hike). No-cuts firmed 89.3%. (2) **Oil regime-flip DISSOLVED into July resolution** — WTI-$100(Jul) 22.9%→0.1% (resolves 8/1 NO; peak was ~$95). Barrel-tell FIRMED against loss (Kalshi Iran-crude Jul >2.0mbpd 77%→86%). ⚠️ Spread now on **v3 regime** (fresh Aug WTI-$100 leg at 27.5% thin) — non-comparable to v2 series. **Blind-spot flag:** WALTER SIG-W-20260730-003 — 30Y hit 5.244% on 7/29 (highest since 2007), a term-premium move my policy-path markets do not see. Routed to BOND/NEXUS.
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` + `scripts/kalshi.py pull --log`. Series → `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`. Derived → `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (**v3-aug-wti-supply-leg**, +22.0pp baseline). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟡 — both live 7/24 triggers stood down. The 2026-hike tail is still meaningful (66.5%) and the Aug WTI-$100 leg is priced through the *old* deepen line (27.5% vs v2's >25%), but each is fresh — v3 baseline needs 3-day re-check discipline, and the FOMC hold has removed the near-term Fed forcing function. Blind-spot on term-premium acknowledged.

---

## Alerts (read first)

**🟠 FED — AGGREGATE UNFIRED, but SEPT-SPECIFIC DEEPENING (sweep-decomposition finding, PM).** Aggregate Fed-HIKE-2026 **71.5%(7/24) → 66.5%(7/31)** (Δ7d −5.0; $6.1M deep) — trigger cycle done clean on 7/29 FOMC hold. Kalshi hike-by-July FINALIZED 18% no-hike; no-cuts firmed 89.3%. **⚠️ AFTERNOON SWEEP FINDING — Fed +25bps @ Sept mtg (specific) = 56.5%, Δ1d +4.0, Δ7d +3.0** ($2.1M vol / $347.7K liq DEEP) — coin-flip TOWARD a Sept hike, deepening post-FOMC. **Decomposition:** by-Sept cumulative 55.5% (Δ7d −5.5) + by-Oct 60.5% (Δ7d −7.5) DROPPED as July no-hike collapsed into them; Sept-mtg-specific ADDED 3-4pp = **hike-timing TIGHTENED into Sept.** WALTER SIG-W-20260730-003's "Fed hold trims Sept hike bets" (Bloomberg) correct for cumulative; meeting-specific opposite direction. **BLIND-SPOT (routed):** WALTER SIG same signal — 30Y = 5.244% on 7/29 (highest since JULY 2007) = term-premium/inflation-credibility axis my markets don't see. → LIQUID, HENRY (retract + Sept-decomp amend); → BOND, NEXUS (blind-spot). (KB-ORC-052/056.)

**🟡 OIL REGIME-FLIP DISSOLVED — July resolved, barrel-tell FIRMED against loss.** WTI-$100-July **22.9%(7/24) → 0.1%** — resolves 8/1 NO (peak was ~$95, no touch). Barrel-level tell RESOLVED CLEAN AGAINST LOSS: **Kalshi Iran-crude-Jul >2.0mbpd 77%(7/24) → 86%(7/31)** (Δ7d +9) — crowd more confident production stayed above 2.0. Kalshi **Brent >$85 @ Jul31 settle-ref 87%** (Δp +6, ⏳0d, closing hot). AUG CONTRACT PINNED: `will-wti-reach-100-in-august-2026` at **27.5%** ($8.3K ⚠thin liq; $201.8K event vol) — fresh month-start contract with more days-to-touch prices structurally higher; the 27.5% is not a new deepen signal on its own. **REGIME BUMPED** in `disruption_supply_spread.py`: v2→**v3-aug-wti-supply-leg**. v3 spread baseline **+22.0pp**. Thresholds retuned: v2 used >15%/>25% mid-month; v3 uses >30%/>40% for a fresh month-start. → HAWK, BRENT, FALCON (retraction). (KB-ORC-053, VX-ORC-04.)

**🟡 WAR-TEMPO FADED into July resolution.** Iran-military-vs-Gulf-State (Jul daily top) **47.5%(7/24) → 15.0%(7/31)** (Δ1d −24.5, Δ7d −31.0) — sharp fade into month-end. Iran-shipping (Jul daily) shows 51.5% (⚠thin $103 liq, single-print noise). US-invade-Iran **29.5%→23.5%** (Δ7d −6.0, deep $51.0M vol) — escalate leg retreating. US-Iran-deal-2026 top 31%→35.0% (+4/7d) — resolve leg still creeping, no acceleration. Bimodal narrowed on the invade side. **AUG COVERAGE GAP:** Iran-military-vs-Gulf-State Aug daily event has NOT opened yet on Polymarket (searched — only Jul 9-14 legs surface). Aug Iran-shipping daily pinned but thin ($15K event vol vs July's $1M). → HAWK, BRENT, FALCON. (KB-ORC-054.)

**🟠 COMPLACENCY UN-CRACKED.** Nothing-Ever-Happens **65.5%(7/24) → 73.5%** (Δ1d +4.5, Δ7d +5.5) — three-weeks-of-erosion reset, back through the 70% line. Reflects (a) FOMC-hold + (b) oil-premium collapse + (c) bimodal-Iran narrowing on the invade side. Equity complacency intact (best-asset-S&P still 68.0%). → RED, VIOLET. (VX-ORC-05.)

**🟠 CLARITY ACT — fade ACCELERATING into Aug-10 recess.** "Signed into law 2026" **33.0%(7/24) → 24.5%** (Δ1d −3.0, Δ7d −8.0, deep $3.5M vol / $68.9K liq). Down from 37% on 7/22 = cumulative **−13pp over 9 days**. Base case = NOT signed 2026 (75.5% no). Aug-10 Senate recess = the near-term catalyst; failure → mid-Sept re-open at earliest. → BROCK, RED. (KB-ORC-055.)

**⚪ SPREAD READ (v3) — Disruption 49.5% − Supply 27.5% = +22.0pp.** Fresh regime, non-comparable to the v2 series (which ran +40.5→+30.8→+25.6 and then dissolved into July resolution). Watch DIRECTION from this baseline; the level tells us nothing yet. Closure proxy 12.5% (up from 9.9% on 7/24 as Aug tail re-anchors, but low absolute).

**🟡 STRUCTURAL CREDIT — still quiet.** Kalshi corporate-bankruptcy >750 **83%** steady; US-credit-downgrade-2026 **6.0%** (Δp 0). Recession **PM 12.5% / Kalshi 7.0%** — Kalshi eased −2pp on the FOMC-hold + oil relief; converged low. Gap-fills (CRE-default, CC-delinquency, Fed-facility) still zero-open. → REGINALD, CARL, LIQUID.

---

## Signal Dashboard (live 2026-07-31T20:28Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: HIKE in 2026** (aggregate) | T1 | **66.5%** | +1.0 | **−5.0** | $6.1M | $196.7K | 🟡 aggregate trigger UNFIRED on FOMC hold |
| **Fed: HIKE at Sept mtg (specific)** | T1 | **56.5%** | **+4.0** | **+3.0** | $2.1M | $347.7K | 🟠 DEEPENING post-FOMC — coin-flip TOWARD Sept hike (sweep-decomp finding) |
| Fed: HIKE by Sept mtg (cumulative) | T1 | 55.5% | — | **−5.5** | $576.3K | $76.3K | trimmed (July no-hike collapsed in) |
| Fed: HIKE by Oct mtg (cumulative) | T1 | 60.5% | — | **−7.5** | $335.6K | $87.1K | trimmed (same mechanic) |
| **Fed: NO cuts 2026** | T1 | **89.3%** | +0.1 | +4.4 | $6.7M | $147.6K | firming; dovish tell <70% not fired |
| Fed: 1 cut 2026 | T1 | 6.5% | — | −3.0 | $2.3M | $97.6K | fading |
| Fed funds end-2026 (dist, top) | T1 | 31.4% | −0.1 | +0.5 | $530.7K | $7.2K | ⚠thin, steady |
| US inflation >5% 2026 | T1 | 13.0% | +0.5 | −2.0 | $297.4K | $21.8K | easing |
| July CPI modal (top) | T1 | 42.5% | +2.0 | +6.0 | $44.1K | $18.4K | 8/12 print; modal firming |
| **US recession 2026** | T1 | **12.5%** | +1.0 | +2.0 | $1.7M | $16.6K | (Kalshi 7.0%) |
| Major bank bailout <2027 | T1 | 7.5% | — | −3.5 | $4.0K | $645 | ⚠thin |
| US bank failure by Dec 31 2026 | T2 | 72.5% | — | −1.0 | $4.6K | $3.2K | ⚠thin — ANY-bank base-rate |
| Which banks fail EOY (top) | T1 | 3.8% | −0.1 | −0.4 | $7.9K | $10.7K | ⚠thin, no name priced |
| US unemployment ladder (top) | T1 | 10.0% | −1.8 | −1.9 | $121.7K | $1.4K | ⚠thin ⏮stale-date |
| **Hormuz normal by Dec 31** | T1 | **50.5%** | −1.0 | −1.0 | $6.4M | $275.5K | disruption persists (=49.5%), steady |
| China invade Taiwan <2027 | T1 | 4.0% | +0.2 | +0.2 | $39.3M | $594.7K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 86.5% | +1.0 | +1.0 | $215.3K | $47.4K | ⏮stale-date |
| **WTI $100 (Aug) — war premium** | T2 | **28.5%** | −3.5 | — | $8.0K | $8.3K | ⚠thin, RANGE 26.5-50.5% over 5d — currently LOW end; twice through v2 >25% line (50.5% + 43.5%). See KB-ORC-059 |
| US invade Iran <2027 | T2 | **23.5%** | −1.0 | **−6.0** | $51.0M | $1.2M | deep, escalate leg retreating |
| US-Iran deal 2026 (top) | T2 | 35.0% | +5.0 | +4.0 | $82.4K | $6.5K | resolve leg still creeping |
| **Iran mil-action vs Gulf State (Jul, top)** | T2 | **15.0%** | **−24.5** | **−31.0** | $75.5K | $8.8K | ⏳0d — fading into resolution; **Aug event NOT YET OPEN → coverage gap** |
| Iran targets shipping (Aug daily, top) | T2 | 40.5% | −2.5 | — | $122 | $190 | ⚠thin fresh Aug pin (~40%/day, $15K event vol; single-print noise) |
| US declares war on Iran <2027 | T2 | 4.5% | −1.0 | −0.5 | $762.7K | $85.5K | narrow mechanism, low |
| Iran ends enrichment by Dec 31 | T2 | 24.5% | −1.0 | +2.0 | $1.4M | $42.4K | slow reawakening |
| **Iranian regime FALL <2027** | T2 | **8.5%** | — | −1.0 | $23.4M | $587.6K | deep regime-collapse gauge, easing |
| **Venezuela: Delcy out Dec31** | T2 | **7.5%** | −0.5 | −2.0 | $176.1K | $14.2K | oil-relevant regime stability |
| **Hormuz 0-ships closure by Aug31** | T2 | **12.5%** | +0.5 | — | $246 | $2.9K | ⚠thin — closure tail low |
| Bab el-Mandeb closed by Dec31 | T2 | 19.0% | −3.0 | −14.5 | $192.7K | $85.2K | fading; Red-Sea premium off |
| **Houthi mil-action vs Israel by Aug31** | T2 | **31.0%** | — | — | — | $241 | ⚠thin — Red-Sea gap partial fill (sweep pin) |
| Russia-Ukraine ceasefire Dec31 | T2 | 35.5% | — | −1.0 | $2.1M | $122.3K | steady |
| BOJ July decision (top) | T2 | 100.0% | — | — | — | — | ⛔RESOLVED — held |
| AI bubble burst 2026 | T2 | 18.7% | −3.6 | +2.2 | $2.3M | $25.4K | steady |
| **Clarity Act signed 2026** | T2 | **24.5%** | **−3.0** | **−8.0** | $3.5M | $68.9K | Aug-10 recess; fade accelerating (cum. −13pp/9d) |
| MicroStrategy bankruptcy <2027 | T2 | 3.9% | — | −0.1 | $191.0K | $10.0K | control |
| US debt default <2027 | T2 | 2.9% | +0.3 | −2.1 | $16.2K | $5.1K | ⚠thin, control |
| Mamdani freezes NYC rents <2027 | T2 | 89.6% | +0.9 | +0.1 | $283.8K | $14.7K | steady |
| **Nothing Ever Happens 2026** | T3 | **73.5%** | **+4.5** | **+5.5** | $701.9K | $36.0K | 🟠 complacency RESET through 70% |
| Best asset 2026 (S&P top) | T3 | 68.0% | +0.5 | +1.0 | $182.0K | $18.0K | elevated |
| FL: Cat-4 hurricane <2027 | T3 | 22.5% | — | −1.0 | $334.8K | $2.8K | ⚠thin |
| FL: Cat-5 hurricane <2027 | T3 | 10.0% | +0.5 | −2.5 | $138.6K | $524 | ⚠thin |

**Kalshi corroboration (2026-07-31T20:24Z):** recession 7.0% (Δp −2, eased on FOMC-hold); **Fed hike-by-July FINALIZED 18%** (no-hike, FOMC 7/29 held); >4.00%-after-July 1.0%; July CPI YoY >3.3% 58% (Δp 0) / >3.4% 26% / >3.5% 7%; July U3 >4.2% 56% (Δp −2) / >4.3% 10%; **Brent >$85 @ Jul31 settle-ref 87% (Δp +6, closing hot ⏳0d)**; **Iran-crude Jul >2.0mbpd 86% (⚠thin, Δp +1 vs prior; +9/7d — barrel-tell firmed against loss)**; US-credit-downgrade 6.0% (Δp 0); corporate-bankruptcy >750 83%.

**Movers (7/31):** all 9 hits are month-end mechanical (⚙0/1d — BTC/ETH Aug-1 daily resolutions, Colombia CB, WTI-95 July fade, Trump-Putin-insult ⏳0d, Iran-shipping-Jul-28 resolved 0.1% NO). No news-reactive signal this week.

**Coverage sweep (7/31, first since 7/22):** 6 hits — 3 novelty (Bayern Munich, Trump-Greenland, Venezuela-specific components already gauged via Delcy pin); 1 Hormuz-Jul31 near-resolves at 0.1% (already tracked via Dec-31); Hantavirus 3.6% ($806K vol) still on nomination list. **No new pins.**

Δ in pp. ⚠thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate. ⛔ = display-quirk false-RESOLVED on daily/ladder events (event is live; read recent legs via `event`). ⏳ = near-dated resolution. ⚙ = movers-only tag for near-resolve mechanical convergence.

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran → oil supply regime | 2 | 🟡 | v2 regime dissolved benignly 7/31; Aug $100 trading 26.5-50.5% range 5d (currently 28.5% LOW end); v3 baseline +22.0pp = MID-SWING snapshot (spread swings ±15pp on WTI thrash); barrel-tell FIRMED (Kalshi Iran-crude 86%, +9/7d) — no realized loss | Aug WTI-$100 **>45% sustained ≥3 reads** (retuned from >30%) OR Iran-crude <2.0mbpd (unchanged) |
| 2 | Fed path (aggregate retraced, Sept-specific DEEPENING) | 3 | 🟠 | Aggregate 66.5% (trigger cycle done clean) BUT sweep-decomp: Sept-mtg-specific 56.5%, Δ1d +4.0, +3.0/7d deep — hike-timing tightened into Sept | Sept-specific >60% OR <45% OR a 2026 hike prints OR another >66% aggregate re-break |
| 3 | Term-premium / credibility (**BLIND-SPOT**) | ? | ⚠️ | 30Y 5.244% on 7/29 (highest since 2007, WALTER SIG-W-20260730-003); prediction-market lens does NOT see this axis | route to BOND/NEXUS; ORACLE cannot upgrade this itself |
| 4 | Risk-on / complacency (RESET) | 1 | ⚪ | NEH un-cracked 73.5% (+5.5/7d); best-asset-S&P 68.0% intact | NEH <30% OR gold takes best-asset lead |
| 5 | Iran-axis (retreated) | 1 | ⚪ | US-invade −6/7d to 23.5%; Iran regime-fall 8.5% (−1); July daily war-tempo faded | Aug daily-events open deep OR US-invade back >30% |
| 6 | CLARITY Act (Aug-10 deadline) | 3 | 🟠 | 24.5%, cumulative −13pp/9d fade; Aug-10 = deadline; deep $3.5M vol | signed → resolve; not-signed by 8/10 → confirms base case |
| 7 | Recession (converged, calm) | 1 | ⚪ | PM 12.5% / Kalshi 7% — Kalshi eased −2 on FOMC-hold+oil-relief | market turns up OR fleet re-arms cyclical axis |

---

## Maintenance flags

- **⚠️ AUG WATCHLIST ROLL — DONE THIS SESSION.** July → August pins updated: WTI-$100 (`will-wti-reach-100-in-august-2026` @ 27.5%), Iran-shipping daily (`iran-successfully-targets-shipping-onptptpt-20260729163314520` @ ~40%/day thin), Hormuz weekly (`week-of-july-27` — must re-pin week-of-Aug-3 next Sunday). RETIRED: Fed hike-July (FOMC done), Iran-enrichment-Jul31 (resolves today at 0.1%). **COVERAGE GAPS: Iran-military-vs-Gulf-State Aug daily NOT yet open; Houthi Aug daily NOT yet open** — re-check next spawn. Spread REGIME bumped v2→v3-aug-wti-supply-leg — non-comparable to v2 rows.
- **⚠️ HORMUZ WEEKLY RE-PIN OWED (weekly cadence, not monthly).** Format changed from by-Jul31 cumulative-ladder to weekly rolling; current pin `week-of-july-27` covers 7/27-8/2, must re-pin `week-of-aug-3` (or successor) next Sunday. Add to CARRY-FORWARD.
- **🔭 COVERAGE SWEEP — done this session** (last was 7/22; overdue by 2d). No new pins; nominations unchanged (Hantavirus tail, Kalshi coverage analog).
- **v2 candidates open:** #3 forward-curve depth on daily rows (see 7/24 SCRATCH); Kalshi coverage analog; 30d-drift flag on `movers` (CLARITY Act would have surfaced earlier); `/events` tag-based novelty suppression.
- **BLIND-SPOT (documented):** term-premium / inflation-credibility axis (30Y 5.244% on 7/29 is the datum) — my instruments (policy-path Fed markets, deep Iran/oil markets, index-range markets) do not price the credibility mechanism. Route to BOND when it moves; do not try to synthesize from within ORACLE.
- **🟡 RED** — still owed current fleet recession probability (GDP/NBER-comparable), carried since 6/13. Not urgent (crowd converged/calm ~7-13%).
- **Kalshi creds present** (chmod 600, unchanged); gap-fills (CRE-default/CC-delinquency/Fed-facility) still zero-open — re-check via `/events?status=open`, NOT `search`.

---

## BOTTOM LINE

**Both 7/24 🔴 triggers stood down** — the Fed re-arm retraced on the 7/29 FOMC hold (hike-2026 back to the re-break line at 66.5%, hike-by-July FINALIZED 18% no-hike), and the oil regime-flip dissolved into July-contract resolution (WTI-$100 22.9%→0.1%, barrel-tell firmed to 86% >2.0mbpd, no barrel lost). The trigger system worked: fired on a real move, retraced on a real resolution. **A blind-spot appeared**: WALTER's 30Y=5.244% (highest since 2007) on the 7/29 hawkish-hold is a term-premium/inflation-credibility move my hike/cut markets cannot see — routed to BOND/NEXUS. **Fresh regime v3** on the disruption-supply spread (Aug WTI-$100 at 27.5% is structurally higher than the mid-month legacy contract — do not chart across; watch the trend from here). Complacency has un-cracked (NEH +5.5/7d to 73.5%), CLARITY Act fade accelerating (−13pp over 9d into Aug-10). Retracted 7/24's two 🔴 routes to LIQUID/HENRY + HAWK/BRENT/FALCON, added the blind-spot flag to BOND/NEXUS.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log` + `python3 AGENTS/ORACLE/tools/disruption_supply_spread.py`*
