# ORACLE STATUS

**Updated:** 2026-07-24 (Fri, boot ~12:01 ET / 16:01Z) — **Two triggers now EXTENDING, not just fired.** (1) **Fed-HIKE-2026 66.5%→71.5%** (Δ7d +20.0) — the >66% re-break trigger that fired 7/22 has blown decisively through; a 2026 hike is now the crowd's firm base case (>2/3). (2) **Regime-flip deepening** — disruption-supply spread narrowed AGAIN +30.8→**+25.6pp** entirely via the WTI leg (WTI-$100 14.9%→22.9%, approaching the >25% deepen-trigger), while the barrel-level tell (Kalshi Iran crude prod 77% >2.0mbpd) STILL hasn't moved. 7/29 FOMC in 5 days.
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` + `scripts/kalshi.py pull --log`. Series → `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`. Derived → `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (v2, +25.6pp). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🔴 — the two live theses (oil supply-loss pricing, Fed re-arm) both STEPPED FURTHER this week, not retraced. Supply-RISK pricing keeps rising while physical supply stays flat — the leading-indicator gap is *widening*, not closing. Routable; the barrel-level confirmation (Iran crude <2.0mbpd) has NOT yet printed.

---

## Alerts (read first)

**🔴 FED RE-ARM EXTENDED — hike-2026 now decisively base case (71.5%).** **Fed-HIKE-2026 66.5% (7/22) → 71.5%** (Δ1d +1.0, Δ7d +20.0, $4.6M deep). The >66% re-break trigger didn't just fire (7/22) — it blew through: a 2026 hike is now the crowd's firm base case (>2/3), no longer marginal. **July-meeting-hike 23.2%** (Δ7d +19.4, $18.2M vol; **Kalshi hike-by-July 22%**, Δp −4 — eased slightly, still corroborates); **7/29 FOMC in 5 days**, still hold-leaning but the tail is durable. No-cuts-2026 firmed to 85.0%, 1-cut fading to 9.5%. The energy premium bleeding into the rate path is the same story, now more advanced. NEXT rung: an actual 2026 hike prints OR the 7/29 meeting hikes. → LIQUID, HENRY. (KB-ORC-049.)

**🔴 REGIME-FLIP DEEPENING — spread narrowed again via the WTI leg; barrel-tell still flat.** Disruption-supply spread **+30.8pp (7/22) → +25.6pp** — narrowed AGAIN, and again the *signal* way: **entirely via the supply leg rising.** WTI-$100-war-premium **14.9% → 22.9%** (Δ7d +15.2), now decisively through the >15% supply-loss threshold and **approaching the >25% deepen-trigger.** ⚠️ It spiked to ~44% intraday then retraced (Δ1d −21.8); liq is thinning ($39.5K → $27.7K) — **read the 7d-trend (+15.2), not the single print.** Disruption leg dead flat (Hormuz-normal 51.5% = 48.5% disruption-persists). **CRITICAL — still NO barrel lost:** Kalshi **Iran crude production Jul >2.0mbpd STILL 77%** (unch, thin). The crowd keeps pricing supply *risk* ahead of realized *loss*; the gap is widening. Kalshi Brent >$85 settle-ref eased to 73% (Δp −10). → HAWK, BRENT, FALCON. (KB-ORC-050.)

**🔴 WAR-WIDENING TEMPO SHARPLY UP — corrects the boot read (daily-event legs pulled directly).** The dashboard shows these events as stale ⛔RESOLVED (top-leg = old settled date); pulling the live legs via `event` reveals the real tempo. **Iran-military-action-vs-Gulf-State (daily): Jul 19 & 20 both resolved YES; forward legs now price ~45-56%/day sustained through Jul 31** (today 7/24 47.5%, 7/25 56.5%, 7/27 51%, 7/29 51%), **ALL up Δ7d +13 to +29** across the curve — **real liquidity ($19-30K several legs, NOT thin).** The crowd is pricing a near-daily coin-flip of Iran military action against a Gulf state for the rest of the month. This is the physical mechanism under the rising WTI-$100 war-premium — with no barrel yet lost. ⚠️ Shipping-attack daily leg also ~50% forward BUT thin (liq $41-200, discount) and mixed (7/21 15.7%, 7/23 2.1%). → HAWK, BRENT, FALCON. (KB-ORC-051.)

**🟠 NEW GEOPOLITICAL CATALYST — Trump-Netanyahu meeting spiking (movers).** Polymarket "Trump meets Netanyahu by July 31" **89.5%** (Δ1d +34.5, Δ7d +45.5, $239K vol); "in July 2026" **89.3%** (Δ7d +50.3). A near-certain meeting now priced — an Iran-axis catalyst. Read as context for the escalate/deal bimodal alongside the Gulf-state tempo above, not a standalone signal. → HAWK, BRENT.

**🟠 COMPLACENCY CRACK STILL ERODING — bimodal Iran persists.** Nothing-Ever-Happens **65.5%** (Δ7d −8.0, was 72.5% on 7/17) — one-way down for three weeks. **US-invade-Iran 29.5%** (Δ7d +7.0, $46.8M deep) AND **US-Iran-deal 31.0%** (Δ7d +8.0) BOTH still rising — escalate and resolve tails fattening together, muddle-through middle thinning. Best-asset-S&P still 67.5% — equity complacency intact even as tail-awareness rises; that gap is the tension. → RED, VIOLET, HENRY.

**⚪ SPREAD READ — v2 = P(Hormuz-disruption 48.5%) − P(WTI-$100 22.9%) = +25.6pp.** Narrowing for two straight reads (+40.5 → +30.8 → +25.6), each time via the WTI supply leg — the exact tell the tool was built to flag. Closure proxy 9.9% (context column, up from 5.7% but still low — no modeled physical shutdown priced). Watch for continued WTI-leg narrowing → deeper into supply-loss regime. (KB-ORC-050.)

**🟠 CLARITY ACT — repricing down toward the Aug 10 deadline.** Polymarket "Clarity Act signed into law 2026" **33.0%** (Δ1d −2.5, Δ7d −1.5, deep $2.6M vol / $70.3K liq) — down from 37% on 7/22, crowd continuing to mark down passage before the **Aug 10 Senate recess deadline**. Base case = NOT signed 2026 (67% no). Aug 10 = catalyst. → BROCK, RED. (KB-ORC-047.)

**🟡 STRUCTURAL CREDIT — quiet.** Kalshi corporate-bankruptcy >750 **83%** steady; US-credit-rating-downgrade-2026 **4.0%** (Δp 0, confirms the 7/22 correction — the 7/17 "16%" was a bad line-read, this ticker is stable at 4%). Recession PM 10.5% / Kalshi 14.0% — converged, calm (Kalshi +4pp on the week but still low). Specific gap-fills (CRE-default, CC-delinquency, Fed-facility) still zero-open. → REGINALD, CARL, LIQUID.

---

## Signal Dashboard (live 2026-07-24T16:01Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: HIKE in 2026** | T1 | **71.5%** | +1.0 | **+20.0** | $4.6M | $157.5K | 🔴 trigger EXTENDED — 2026 hike now firm base case (>2/3) |
| **Fed: hike at July mtg** | T1 | **23.2%** | −2.1 | **+19.4** | $18.2M | $191.2K | ⏳5d (7/29) — tail durable, still hold-likely |
| **Fed: NO cuts 2026** | T1 | **85.0%** | +0.5 | +1.4 | $6.4M | $146.1K | firming; dovish tell <70% not fired |
| Fed: 1 cut 2026 | T1 | 9.5% | −1.0 | −2.0 | $2.2M | $98.1K | fading |
| Fed funds end-2026 (dist, top) | T1 | 30.8% | −0.1 | −0.2 | $529.9K | $11.0K | steady |
| US inflation >5% 2026 | T1 | 15.0% | +1.0 | +2.5 | $286.3K | $14.6K | creeping |
| July CPI modal (top) | T1 | 38.5% | −2.5 | +7.5 | $18.2K | $11.9K | ⚠️thin; top bucket eased off 43.5% |
| US recession 2026 | T1 | 10.5% | −0.5 | −1.0 | $1.7M | $18.4K | calm (Kalshi 14.0%) |
| Major bank bailout <2027 | T1 | 11.5% | — | +0.5 | $3.8K | $1.2K | ⚠️thin, benign |
| US bank failure by Dec 31 2026 | T2 | 74.0% | +1.0 | — | $3.2K | $4.5K | ⚠️thin — ANY-bank base-rate, not a name |
| Which banks fail EOY (top) | T1 | 4.2% | +3.1 | +3.1 | $616 | $985 | ⚠️thin, no name priced |
| US unemployment ladder (top) | T1 | 11.9% | — | −1.6 | $120.5K | $3.4K | ⚠️thin ⏮stale-date |
| **Hormuz normal by Dec 31** | T1 | **51.5%** | +2.0 | — | $5.8M | $245.4K | disruption persists (=48.5% disr), flat |
| China invade Taiwan <2027 | T1 | 3.9% | — | +0.1 | $39.0M | $567.5K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 85.5% | — | — | $211.5K | $38.3K | ⏮stale-date |
| **WTI $100 (Jul) — war premium** | T2 | **22.9%** | −21.8 | **+15.2** | $932.4K | $27.7K | 🔴 supply leg; through >15%, nearing >25%. Intraday spike-retrace — read 7d-trend, liq thinning |
| US invade Iran <2027 | T2 | 29.5% | — | **+7.0** | $46.8M | $687.4K | deep, escalate tail still fattening |
| US-Iran deal 2026 (top) | T2 | 31.0% | +1.0 | **+8.0** | $79.8K | $7.2K | resolve tail ALSO rising (bimodal) |
| **Iran mil-action vs Gulf State (daily)** | T2 | 7/24 **47.5%** | — | **+13 to +29** | $19-30K/leg | real | 🔴 war-widening; ~50%/day sustained thru 7/31, 7/19+20 YES (via `event`; ⛔dash-quirk) |
| Iran targets shipping (daily) | T2 | 7/24 32.5% | — | — | thin | $41-200 | ⚠️thin forward legs ~50% but low-liq; 7/23 2.1% mixed (via `event`) |
| US declares war on Iran <2027 | T2 | 5.0% | +0.5 | +0.5 | $700.3K | $85.2K | narrow mechanism, low |
| Iran ends enrichment by Dec 31 | T2 | 22.5% | +0.5 | +3.0 | $1.4M | $69.8K | firming |
| Iran ends enrichment by Jul 31 | T2 | 0.8% | — | −0.3 | $938.8K | $72.1K | ⏳ near-zero |
| **Iranian regime FALL before 2027** | T2 | **9.5%** | — | — | $23.0M | $708.2K | deep regime-collapse gauge; escalation ≠ collapse priced |
| **Venezuela: Delcy out Dec31** | T2 | **9.5%** | — | +0.5 | $174.6K | $13.9K | oil-relevant regime-stability |
| **Hormuz 0-ships closure by Jul31** | T2 | **9.9%** | +1.4 | −5.6 | $274.0K | $25.7K | closure tail low — no supply-shutdown priced |
| Bab el-Mandeb closed by Dec31 | T2 | 33.5% | −2.0 | +2.0 | $142.5K | $44.5K | Red Sea chokepoint |
| Russia-Ukraine ceasefire Dec31 | T2 | 36.5% | +1.0 | — | $2.0M | $110.9K | Russia advancing |
| BOJ July decision (hold top) | T2 | 97.8% | +1.0 | −1.0 | $82.4K | $7.3K | ⏳7d hold near-certain |
| AI bubble burst 2026 | T2 | 16.4% | −0.2 | −0.8 | $2.3M | $15.7K | steady |
| **Clarity Act signed 2026** | T2 | **33.0%** | −2.5 | −1.5 | $2.6M | $70.3K | crypto bill; Aug 10 recess deadline, marking down |
| MicroStrategy bankruptcy <2027 | T2 | 3.9% | — | −0.2 | $190.2K | $8.4K | control |
| US debt default <2027 | T2 | 5.0% | −0.1 | +1.1 | $16.0K | $2.5K | ⚠️thin, control |
| Mamdani freezes NYC rents <2027 | T2 | 89.4% | −0.8 | −2.4 | $283.8K | $20.1K | steady |
| **Nothing Ever Happens 2026** | T3 | **65.5%** | −1.0 | **−8.0** | $690.1K | $21.2K | complacency crack still eroding |
| Best asset 2026 (S&P top) | T3 | 67.5% | — | −1.0 | $181.0K | $17.6K | elevated — equity complacency intact |
| FL: Cat-4 hurricane <2027 | T3 | 23.5% | −0.5 | +1.5 | $334.5K | $7.6K | ⚠️thin |
| FL: Cat-5 hurricane <2027 | T3 | 13.0% | +0.5 | +0.5 | $137.9K | $3.4K | ⚠️thin |

**Kalshi corroboration (2026-07-24T16:01Z):** recession 14.0% (2.9M vol/806K OI, Δp +4); **Fed hike-by-July 22.0% (Δp −4)** — corroborates PM's 23.2%; >4.00%-after-July 1.0%; July CPI YoY >3.3% 63% (Δp −6) / >3.4% 30% / >3.5% 7%; July U3 >4.2% 57% / >4.3% 13%; **Brent >$85 @ Jul31 settle-ref 73% (Δp −10, easing)**; **Iran-crude-prod Jul >2.0mbpd 77% (⚠️thin, UNCHANGED — barrel-tell flat)**; US-credit-downgrade 4.0% (Δp 0); corporate-bankruptcy >750 83%.

**Movers (7/24):** Trump-Netanyahu-meet-July **89.5%** (Δ7d +45.5) → HAWK/BRENT context; rest = SPY daily closes (⚙mechanical) + Dow-"Carbon" novelty.

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate. ⛔ = display-quirk false-RESOLVED on daily/ladder events (event is live; read recent legs via `event`). ⏳ = near-dated resolution.

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran → oil supply regime | 4 | 🔴 | Spread narrowed AGAIN +30.8→+25.6pp VIA the WTI leg; WTI-$100 22.9% nearing >25%; supply-RISK pricing rising, barrel-tell (Iran crude 77%) flat — gap widening | WTI-$100 >25% OR Hormuz-closure >30% OR Iran crude prod <2.0mbpd (real loss) |
| 2 | Fed path (re-arming hawkish) | 4 | 🔴 | hike-2026 66.5→71.5% (Δ7d +20, decisively base case); July-mtg-hike 23.2%; the >66% trigger EXTENDED not just fired | an actual 2026 hike prints OR 7/29 FOMC hikes |
| 3 | Risk-on / complacency crack | 3 | 🟠 | NEH −8/7d (three weeks one-way); invade (+7) AND deal (+8) tails both rising | NEH <30% OR gold takes best-asset lead |
| 4 | Iran-axis catalyst (Trump-Bibi) | 2 | 🟠 | Trump-Netanyahu-meet-July 89.5% (+45.5/7d) — meeting now priced near-certain | meeting outcome → escalate vs deal leg resolves |
| 5 | Recession (converged, calm) | 1 | ⚪ | PM 10.5% / Kalshi 14.0% — fleet & crowd agree | market turns up OR fleet re-arms cyclical axis |

---

## Maintenance flags

- **⚠️ WTI $100 supply-leg MONTH-ROLL — DUE ~Aug 1 (8 days).** The July WTI-$100 market (`will-wti-reach-100-in-july-2026-928`) ends **2026-08-01**. When August opens, re-pin the new month's WTI-$100 market in `watchlist.tsv` or the spread's supply leg silently ages out (script hard-exits if legs drift >3d — fails loud, but the re-pin is manual). Same for the Jul-31 Hormuz ladder (re-pin an Aug ladder) and Iran July legs.
- **⛔ Daily-event display quirk — re-pin owed.** Iran-shipping, Iran-Gulf-state, Hormuz-transit-ladder, Houthi-shipping all trip false ⛔RESOLVED (fetcher top-leg = old settled date). Parent events are LIVE — read recent legs via `event`. These have carried several sessions; re-pin fresh current-week legs at next roll-watch pass to clear the noise.
- **WTI-$100 leg thinning ($27.7K liq, was $64K on 7/17).** As it approaches its 8/1 resolution, single prints get noisier (7/24 saw a ~44%→22.9% intraday round-trip). Read the 7d-trend, not the daily. Confirms the memory-banked "thin/thinning liquidity discipline."
- **🔭 COVERAGE SWEEP — weekly, NEXT DUE ~7/29** (last run 7/22). Run at closeout if >7d since. Pending un-actioned nominations: Hantavirus-pandemic tail (flagged to fleet, awaiting owner); Kalshi coverage analog (v2 build candidate).
- **🟡 RED** — still owed current fleet recession probability (GDP/NBER-comparable), carried since 6/13. Not urgent (crowd & fleet both ~10-14%, agree calm).
- **Kalshi creds present** (chmod 600, unchanged); lane LIVE. Specific gap-fills (CRE-default/CC-delinquency/Fed-facility) still zero-open — re-check via authoritative `/events?status=open` sweep, NOT `search` (KB-ORC-041).

---

## BOTTOM LINE

Both live theses stepped further this week — neither retraced. **The Fed re-arm didn't just fire, it extended**: hike-2026 blew from 66.5% through to 71.5% (Δ7d +20), so a 2026 hike is now the crowd's firm base case (>2/3), and the 7/29 FOMC is five days out. **The oil regime-flip deepened**: the disruption-supply spread narrowed for a second straight read (+40.5 → +30.8 → +25.6pp), each time via the WTI supply leg — WTI-$100 now 22.9%, decisively through the >15% supply-loss line and nearing the >25% deepen-trigger. And the single cleanest divergence on the board is *widening*: the crowd keeps pricing supply **risk** while the barrel-level tell (Kalshi Iran crude production, 77% >2.0mbpd) hasn't budged — supply-risk pricing rising against flat physical supply is the textbook leading-indicator posture, and the gap between them is where the next move lives. A new Iran-axis catalyst printed too — Trump-Netanyahu-meet-July spiked to 89.5% (+45/7d). Complacency has stopped ignoring all this (NEH −8/7d, both Iran tails fattening). Routed: HAWK/BRENT/FALCON (regime deepening) + LIQUID/HENRY (Fed extension).

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log` + `python3 AGENTS/ORACLE/tools/disruption_supply_spread.py`*
