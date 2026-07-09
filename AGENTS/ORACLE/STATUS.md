# ORACLE STATUS

**Updated:** 2026-07-09 (Thu ~16:55 ET, PROME-spawned catch-up/diagnostics refresh) — live pull both platforms + roll-watch (2 resolved pins repinned, 2 new adds: Hormuz-closure proxy, US-declares-war proxy) + divergence check vs fleet marks | prior: 2026-07-02 — **7-day gap, own inbox was empty across it.**
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` (Gamma API) + `scripts/kalshi.py pull --log` (CFTC exchange, RSA-PSS). Series → `workbook/ODDS_LOG.tsv` (40 rows this pull) / `KALSHI_ODDS_LOG.tsv` (8 rows). Cross-agent surface → `NEXUS_BRIEF.md`. Divergence detail → `DIVERGENCE_2026-07-09.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟠 — **the crowd repriced the 7/7-7/8 US-Iran truce collapse in real time and materially, but is NOT pricing a supply shock.** Hormuz-normal-by-Dec31 eroded further (82.5%→**61.5%**, −21/7d); the escalation-tail market (US blockade) jumped +17.5/7d to **48.0%** — closely tracking HAWK's own D-rung (46%). Yet WTI-$100 war-premium is still dead (**3.2%**). Separately, Fed-hike-2026 **recrossed above 50%** for the first time since 7/2's "rolling over" call.

---

## What changed since 7/2 (the gap)

The truce collapsed 7/7→7/8 (fleet digest: 80+ US targets struck, Treasury revoked ceasefire oil-relief, Iran hit 3 neutral tankers + fired on Gulf bases). The crowd's forward "Iran targets shipping again" window (pinned 6/29) **resolved YES across every leg** — real confirmation, not a model call. Markets that moved hardest this week:

| Market | 7/2 | 7/9 | Δ7d | Read |
|---|--:|--:|--:|---|
| Hormuz normal by Dec 31 | 82.5% | **61.5%** | **−21.0** | year-end normalization thesis eroding fast |
| US blockade on Iran (top leg) | 30.5% | **48.0%** | **+17.5** | escalation-tail nearly doubled the digest's D-rung read |
| Hormuz 60-ships/day by Jul31 | 55.5% | **12.5%** | **−48.5** | crowd now doubts even partial recovery — reduced regime hardening, not easing |
| Fed: HIKE in 2026 | 46.5% | **50.5%** | **+4.0** | recrossed >50 — partial reversal of the 7/2 "overshoot rolling over" read |
| WTI $80 (Jul) elevated | 11.5% | **33.0%** | **+19.5** | up sharply on the week... |
| WTI $100 (Jul) war premium | 1.6% | **3.2%** | +1.6 | ...but still near-dead — no war-premium spike even after the collapse |
| Nothing Ever Happens 2026 | 84.0% | **79.5%** | −4.0 | complacency ticked down off its series high |

---

## Alerts (read first)

**🟠 IRAN/OIL — truce-collapse repriced hard on shipping/disruption, ZERO on oil supply premium.** Hormuz-normal-Dec31 **61.5% (Δ7d −21.0)**; near-term Hormuz-normal-Jul15 **0.4% (Δ7d −6.0)** — near-certain the disruption persists past its own resolution window. Ships-transit ladder by Jul31: 60/day **12.5% (Δ7d −48.5)**, 80/day **3.7% (Δ7d −15.8)**, 100/day **1.1% (Δ7d −6.9)** — every rung fell, meaning the crowd expects LESS recovery, not more. **NEW Hormuz-closure proxy** (0 ships transit, any date): by-Jul14 **5.4%**, by-Jul31 **12.0% (Δ7d +6.5)** — full closure still a tail (rising, still low) — crowd's read = harassment/disruption, not a clean strait closure. **US blockade on Iran 48.0% (Δ7d +17.5, $210K vol/$64.7K liq)** — closely tracks HAWK's D-rung (46%, digest 7/9) — **see divergence note: this converges, doesn't diverge.** **YET WTI-$100-war-premium still just 3.2%** — the crowd has NOT priced a supply shock despite the collapse; oil moves are being read as transit/diesel-export disruption (Russia + Iran two-root), not barrels lost. → HAWK/BRENT.

**🟡 FED — hike tail recrossed >50%, partial reversal of 7/2's "rolling over" call.** Fed-HIKE-2026 **50.5% (Δ1d −10.0, Δ7d +4.0)** — back above 50 for the first time since 7/2. July-hike itself still contained (PM **14.5%** Δ7d +4.9; Kalshi **15%** Δp −5.0 intraday, noisy) but up cross-platform from the 7/2 ~9.7%/14% base. **No-cuts-2026 still pinned 78.5% (Δ1d −0.5, Δ7d +1.0)** — dovish tell (<70%) still not fired. Not scored as a fleet-mark divergence (digest cites no explicit Fed-hike fleet probability) — routed as a fresh watch item. → LIQUID, HENRY.

**🟡 MACRO PRINTS — June CPI (7/14) and U3 gap-filled, resolves next week.** Kalshi June CPI YoY >3.5% **98%** / >3.6% **96%** / >3.8% **21%**; PM modal-3.8% (top leg) **48.7% (Δ7d +0.9)**, thin-ish $16.4K liq. June U3 >4.2% **82%** / >4.3% **25%** [finalized 7/2, unchanged]. Resolves 7/14-15; surprise vs the 3.6-3.8 range is the tell. → HENRY, LABOR.

**⚪ BANK PROVISIONS — Citi print swung hard on thin liquidity, discount it.** Citi Q2 prov >$2.9B **31.5% (Δ1d −25.5, Δ7d −27.5, only $2.7K liq)** — collapsed from 60% (7/2); **thin, single-print risk, do not mark** — re-check before 7/14. BAC >$1.4B **44.5% (Δ1d +1.0)**, liq **$12** — effectively no depth, meaningless. → REGINALD/CARL (FYI only).

**⚪ SENTIMENT — risk-on still near series highs, ticked down modestly.** Best-asset-2026 (S&P) **70.5% (Δ7d +3.5)** — new series high; Nothing-Ever-Happens **79.5% (Δ7d −4.0)** — off its 84% high, the one soft tell that the truce-collapse registered in the crowd's tail-risk pricing, though still very elevated. Mamdani NYC rent-freeze **91.9% (Δ7d −1.8)** — steady, near-certain. → RED, VIOLET, HENRY.

---

## Divergence read vs fleet marks (full detail → `DIVERGENCE_2026-07-09.md`)

| Fleet mark | Value | Market analog | Value | Gap | KL bits | Read |
|---|--:|---|--:|--:|--:|---|
| HAWK ladder D-rung | 46% | US blockade on Iran (Dec 31) | 48.0% ($64.7K liq) | −2pp | **≈0.001** | **CONVERGES** — noise-level, real-money cross-check confirms HAWK independently |
| BRENT durable-sustain | ~0.55 | *(no resolution-matched market)* | — | — | not computable | **coverage gap** — nearest bracket (WTI $80-Jul, 33.0%) tests a harder bar (~Brent $85 equiv), not comparable |

**No material market-vs-fleet divergence found** on the two named comparators this session. The one live watch item is the Fed-hike-2026 recross >50% (not scored — no fleet-side Fed-hike mark to diff against).

---

## Signal Dashboard (live 2026-07-09T20:51-54Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: hike at July mtg** | T1 | **14.5%** | −7.1 | **+4.9** | $11.3M | $348.1K | up cross-platform (Kalshi 15%) |
| **Fed: HIKE in 2026** | T1 | **50.5%** | **−10.0** | **+4.0** | $3.7M | $94.6K | recrossed >50 |
| **Fed: NO cuts 2026** | T1 | **78.5%** | −0.5 | +1.0 | $5.9M | $118.2K | dovish tell <70% not fired |
| Fed: 1 cut 2026 | T1 | 15.5% | — | +1.0 | $2.0M | $117.4K | steady |
| Fed funds end-2026 (dist, top) | T1 | 32.6% | −3.6 | +7.3 | $527.4K | $10.3K | mass drifting |
| US inflation >5% 2026 | T1 | 13.5% | — | +0.5 | $279.4K | $24.3K | contained |
| June CPI modal (top) | T1 | 48.7% | −1.8 | +0.9 | $110.0K | $16.4K | res 7/15 |
| US recession 2026 | T1 | 10.0% | −0.5 | −1.5 | $1.7M | $19.1K | calm (Kalshi 10.0%, Δp −1.0) |
| Major bank bailout <2027 | T1 | 11.5% | +0.5 | — | $3.7K | $2.4K | ⚠️thin, benign |
| Which banks fail EOY (top) | T1 | 2.6% | +0.2 | +0.1 | $205 | $331 | ⚠️thin, no name priced |
| **Citi Q2 prov >$2.9B** | T1 | **31.5%** | **−25.5** | **−27.5** | $7.0K | $2.7K | ⚠️thin — single-print swing, re-check |
| BAC Q2 prov >$1.4B | T1 | 44.5% | +1.0 | +1.5 | $5.2K | $12 | ⚠️no depth |
| US unemployment ladder (top) | T1 | 12.5% | +2.8 | +0.2 | $119.6K | $1.5K | ⚠️thin ⏮stale-date |
| **Hormuz normal by Dec 31** | T1 | **61.5%** | +3.0 | **−21.0** | $4.7M | $259.0K | eroding fast |
| China invade Taiwan <2027 | T1 | 4.0% | −0.1 | +0.5 | $38.2M | $756.3K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 80.0% | −0.5 | +1.5 | $176.6K | $10.5K | ⏮stale-date |
| **US blockade on Iran (top)** | T2 | **48.0%** | +2.0 | **+17.5** | $210.0K | $64.7K | ≈HAWK D-rung — converges |
| **Iran targets shipping (top, by-Aug31)** | T2 | **84.5%** | −6.5 | — | $6.4K | $12.1K | old window resolved YES; repinned |
| Iran targets shipping by-Jul31 | T2 | 54.5% | −30.0 | — | — | $4.6K | ⚠️thin, single-print |
| Iran targets shipping by-Jul12 | T2 | 26.0% | — | — | — | — | near-term |
| **Hormuz 0-ships closure by Jul31 (NEW)** | T2 | **12.0%** | +1.8 | **+6.5** | $94.0K | $36.6K | closure tail rising, still low |
| Hormuz 0-ships closure by Jul14 | T2 | 5.4% | −0.4 | +2.2 | $42.9K | $45.4K | near-term, low |
| Hormuz ladder 60/day by Jul31 | T2 | 12.5% | −2.0 | **−48.5** | $106.7K | $44.0K | recovery-doubt hardening |
| Hormuz ladder 80/day by Jul31 | T2 | 3.7% | −0.4 | −15.8 | $43.6K | $92.3K | same |
| Hormuz ladder 100/day by Jul31 | T2 | 1.1% | −0.4 | −6.9 | $27.5K | $67.4K | same |
| Hormuz normal by Jul 15 | T2 | 0.4% | −0.1 | −6.0 | $8.4M | $367.8K | near-dead |
| Iran ends enrichment by Jul 31 | T2 | 1.8% | +0.1 | −1.8 | $881.0K | $108.0K | dead |
| Iran ends enrichment by Dec 31 | T2 | 22.5% | — | −7.0 | $1.3M | $90.2K | fading further |
| US-Iran deal 2026 (Recon.Funding top) | T2 | 38.5% | +9.0 | −0.5 | $63.6K | $33.7K | flat on week; Δ1d likely noise |
| US invade Iran <2027 | T2 | 15.5% | +1.0 | +2.0 | $40.2M | $729.4K | deep, stable |
| **US declares war on Iran <2027 (NEW)** | T2 | **5.5%** | — | — | $633.7K | $102.1K | narrow/rare mechanism, not comparable to blockade read |
| Iran leadership change Dec31 | T2 | 16.5% | +1.0 | +1.0 | $3.1M | $78.0K | steady |
| Russia-Ukraine ceasefire Dec31 | T2 | 40.5% | — | −1.0 | $2.0M | $151.7K | slipping |
| China-Philippines clash <2027 | T2 | 11.5% | −3.0 | −2.0 | $1.3M | $124.6K | easing |
| BOJ July decision (hold top) | T2 | 96.5% | −1.0 | −0.8 | $40.0K | $12.9K | hold near-certain |
| **WTI hits $80 (Jul)** | T2 | **33.0%** | **−24.5** | **+19.5** | $307.9K | $20.8K | ⚠️moderate-liq swing, re-check |
| WTI hits $100 (Jul) — war premium | T2 | 3.2% | −2.5 | +1.7 | $158.3K | $37.4K | still near-dead |
| AI bubble burst 2026 | T2 | 15.2% | −0.3 | −2.9 | $2.3M | $23.8K | easing |
| MicroStrategy bankruptcy <2027 | T2 | 4.0% | −0.5 | −0.5 | $185.8K | $16.1K | control |
| US debt default <2027 | T2 | 3.4% | — | +0.1 | $15.8K | $6.9K | control |
| **Mamdani freezes NYC rents <2027** | T2 | 91.9% | +0.2 | −1.8 | $276.3K | $33.2K | steady, near-certain |
| **Nothing Ever Happens 2026** | T3 | **79.5%** | −4.0 | **−4.0** | $646.7K | $41.7K | off series high |
| **Best asset 2026 (S&P top)** | T3 | **70.5%** | +1.5 | **+3.5** | $180.3K | $18.9K | new series high |
| FL: Cat-4 hurricane <2027 | T3 | 27.0% | −1.0 | −9.0 | $333.8K | $2.7K | ⚠️thin |
| FL: Cat-5 hurricane <2027 | T3 | 16.0% | — | — | $137.6K | $2.5K | ⚠️thin |

**Kalshi corroboration (2026-07-09T20:51Z):** recession 10.0% (Δp −1.0, 2.8M vol/819.6K OI); July-hike (>3.75%) 15% (Δp −5.0); >4.00% 1%; June CPI >3.5% 98% / >3.6% 96% / >3.8% 21%; June U3 >4.2% 82% / >4.3% 25% [both finalized].

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate.

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran shipping/Hormuz disruption | 3 | 🟠 | Hormuz-normal-Dec31 61.5% (−21/7d), blockade 48.0% (+17.5/7d, ≈HAWK D46), ladder rungs all sliding down; oil STILL calm (WTI-$100 3.2%) | WTI-$100-Jul >10% (supply shock) OR blockade fires OR closure-proxy >30% |
| 2 | Fed path (partial re-hawkish) | 2 | 🟡 | hike-2026 50.5% (+4.0/7d, recrossed >50); no-cuts 78.5% (dovish tell not fired) | hike-2026 >66% (re-arm) OR no-cuts <70% (dovish turn) |
| 3 | Risk-on rotation | 2 | 🟠 | S&P best-asset 70.5% (new high) but NEH ticked down −4/7d off its high | NEH <30% OR gold retakes lead OR NEH continues sliding |
| 4 | Bank cluster (thin, drifting) | 1 | ⚪ | Citi-prov 31.5% (−27.5/7d, thin) / BAC 44.5% (thin, no depth) | provisions miss hard 7/14 OR failure vol >$50K |
| 5 | Recession (converged) | 1 | ⚪ | PM 10.0% / Kalshi 10.0% — fleet & crowd agree | market turns up OR fleet re-arms cyclical axis |

---

## Maintenance flags

- **Roll-watch executed (7/9):** Iran-targets-shipping forward window (6/29 pin) **RESOLVED YES across all legs** → repinned to fresh 7/7-created event (by-Jul12/15/31/Aug31). Hormuz ships-transit ladder (6/26 pin) shows a **display quirk**: its "top" leg (40-ships/day) is at 100% with drained liquidity, tripping a false ⛔RESOLVED flag on the dashboard — the event itself is still open; the real signal lives in the 50/60/80/100-ship rungs, which are all still live and moving. **2 new adds:** Hormuz 0-ships closure proxy (direct answer to "Hormuz closure markets"), US-declares-war-on-Iran proxy.
- **7/2→7/9 gap:** own inbox was empty across the gap (no domain-agent signals queued); this was a scheduled diagnostics refresh, not a backlog drain.
- **Kalshi creds confirmed present** (chmod 600, unchanged since 7/2 fix); Kalshi lane LIVE.
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.
- **Kalshi gap-fills still pending event-open:** CRE default (KXCREDEFMAX), credit-card delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY) — re-check each session.
- **BTC-dip $40K** dashboard row still needs a clean repin (Dec-31 market); low-priority, BTC strong.
- **Two thin-liquidity swings this pull need a re-check before next session:** Citi Q2 prov (Δ7d −27.5 on $2.7K liq) and WTI $80-Jul (Δ1d −24.5 on $20.8K liq, moderate not thin but still a big single-day move).

---

## BOTTOM LINE

The crowd repriced the 7/7-7/8 US-Iran truce collapse **hard on the shipping/disruption axis and barely at all on oil supply**: Hormuz-normal-by-Dec31 eroded 21pp in a week, every ships-transit-ladder rung fell (the crowd expects LESS recovery, not more), and the escalation-tail "US blockade" market jumped to 48.0% — landing almost exactly on HAWK's own D-rung (46%), an unusually clean independent cross-check (KL≈0.001 bits). Yet WTI-$100-July war-premium sits at just 3.2%, unchanged in kind since 7/2 — **the crowd still reads this as transit/diesel-export disruption, not barrels lost**, consistent with the fleet's own two-root (Iran + Russia) framing. BRENT's specific durable-sustain thesis (~0.55, Brent >$75 through Friday) has **no resolution-matched market to check it against** — a coverage gap, not a disagreement. The one thing moving against the "calm" 7/2 read is the Fed: hike-2026 recrossed above 50% for the first time in weeks, though no-cuts (78.5%) still holds the dovish tell shut. Risk-on cooled marginally off its series high (NEH −4/7d) — the first soft tell that the crowd's tail-risk pricing noticed the collapse at all.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log`*
