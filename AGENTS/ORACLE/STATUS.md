# ORACLE STATUS

**Updated:** 2026-07-22 (Wed, boot ~11:41 ET + **PM re-pull before closeout**) — **PM update: Fed-HIKE-2026 crossed the >66% re-break trigger intraday (64.5%→66.5%), same day flagged.** Boot story unchanged: **the regime-flip tripwire pre-registered on 7/17 tripped — the SIGNAL way** The disruption-supply spread collapsed +40.5→+30.8pp *entirely via the supply leg rising*: WTI-$100 war-premium 7.5%→17.8%, crossing the >15% "crowd flips to supply-loss pricing" threshold. In parallel the Fed re-armed hawkish (July-hike 3.6%→21.1%, hike-2026 51.5%→64.5%). Complacency crack deepened (NEH −12/7d).
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` + `scripts/kalshi.py pull --log`. Series → `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`. Derived → `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (v2, +30.8pp). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟠→🔴-adjacent — one week ago the crowd's read was "premium not shortage." It is now starting to doubt that: **supply-loss pricing (WTI-$100 up 10pp) and Fed-hike pricing (July-hike up 17pp) are stepping up together**, even though no actual barrel has been lost (Kalshi Iran crude production still 77% >2.0mbpd). This is the leading edge of the regime flip — routable, not yet confirmed.

---

## Alerts (read first)

**🔴 REGIME-FLIP TRIPWIRE TRIPPED — supply-loss pricing overtaking premium.** The disruption-supply spread **collapsed +40.5pp → +30.8pp** in 5 days, and it collapsed the *signal* way: **entirely via the SUPPLY leg rising**, not disruption easing. **WTI-$100-war-premium 7.5% → 17.8%** (Δ1d +9.2, Δ7d +11.4, deep $672K vol / $64.2K liq — not thin), crossing the pre-registered **>15% "crowd flips to supply-loss pricing"** threshold. The disruption leg is dead flat (Hormuz-normal-Dec31 51.5% both dates → 48.5% disruption-persists). **The crowd is starting to price lost barrels, not just a risk premium.** ⚠️ But NO barrel actually lost yet — Kalshi **Iran crude production Jul >2.0mbpd still 77%** (sanctioned baseline, uncollapsed); the crowd is pricing supply *risk* ahead of realized loss. Corroborators: **WTI-$90-intraday 65.6%** (Δ7d +45.8, $1.5M deep), Kalshi **Brent >$85 @ Jul31 settle-ref 73%** (Δp +6), **gold hit $4,150**. → HAWK, BRENT, FALCON, PROME. (KB-ORC-042.)

**🔴 FED RE-ARMED — >66% TRIGGER FIRED intraday (same day flagged).** **Fed-HIKE-2026 51.5% → 64.5% (AM) → 66.5% (PM)** (Δ1d +5.0, Δ7d +16.0, $4.4M deep) — **crossed the pre-set >66% re-break trigger the same day I flagged it "~1.5pp away, fires on the next uptick."** A 2026 hike is now the crowd's firm base case (2/3). July-meeting-hike **3.6% → 22.2%** (Δ1d +10.3, Δ7d +18.1, $17.4M vol; Kalshi hike-by-July **23%**, Δp +10) — meeting **7/29** (7d), still hold-leaning but the tail keeps fattening. No-cuts-2026 firmed to **84.8%**. The oil/energy premium is bleeding straight into rate-path pricing. NEXT rung: an actual hike prints OR the 7/29 meeting hikes. → LIQUID, HENRY. (KB-ORC-043/046.)

**⚪ SPREAD READ — WIDE→NARROWING, correct-leg.** v2 = P(Hormuz-disruption-persists 48.5%) − P(WTI-$100 17.8%) = **+30.8pp** (was +40.5 on 7/17). The narrowing is the tell, and it's the tell we wanted to see fire: driven by the WTI leg, not by disruption easing. Closure proxy (5.7%, a context column) *fell* — no supply-event closure priced, so the supply-risk repricing is premium-channel (blockade friction / war tempo), not a modeled physical shutdown. Watch for the spread to keep narrowing on the WTI leg → deeper into supply-loss regime. (KB-ORC-042.)

**🟠 COMPLACENCY CRACK DEEPENED — bimodal Iran path.** Nothing-Ever-Happens **66.5%** (Δ7d −12.0, was 72.5% on 7/17) — one-way down since the truce collapse. **US-invade-Iran-<2027 28.5%** (Δ7d +11.0, $46M deep) AND **US-Iran-deal-2026 34.5%** (Δ7d +11.5) BOTH rose — the crowd fattened the escalate *and* resolve tails at once, thinning the muddle-through middle. Best-asset-S&P still elevated 67.0% — equity complacency intact even as tail-awareness rises; that gap is the tension. → RED, VIOLET, HENRY. (KB-ORC-044.)

**🟡 OIL PREMIUM STEPPED UP HARD — mind the intraday-vs-settle trap.** WTI-$90-intraday **65.6%** (Δ7d +45.8) and WTI-$85-intraday elevated; Kalshi Brent >$85 settle-ref **73%** (Δp +6). **⚠️ The Polymarket WTI markets resolve on INTRADAY HIGH, not a settle — do NOT read them as confirmation of FALCON's 3-consecutive-settle >$85 (Brent) thesis.** Kalshi KXBRENTMON is the settle-reference instrument but resolves on a SINGLE month-end reading, still not FALCON's 3-settle bar. Cite precisely (fused-true-facts trap, fleet memory 7/16). → BRENT, HAWK.

**⚪ WAR TEMPO — mixed; shipping quiet on 7/21.** Iran-targets-shipping daily leg read **1.0% on Jul 21** (Δ1d −71.5) — the shipping-attack tempo *eased* on that specific day after the mid-July resumption. Iran-military-action-vs-Gulf-State daily event still live. Read recent legs via `event`; the daily events trip false ⛔RESOLVED on the fetcher (top-leg = old settled date) — events are LIVE.

**🟡 STRUCTURAL CREDIT — quiet, downgrade gauge eased slightly.** Kalshi US-credit-rating-downgrade-2026 **4.0%** (Δp −1.0 — note: reads lower than 7/17's 16% snapshot; verify the specific market/ticker on next pull, possible market/line shift); corporate-bankruptcy >750 **83%** steady. Specific gap-fills (CRE-default, CC-delinquency, mortgage-default, Fed-facility) still zero-open — re-check via the authoritative `/events?status=open` sweep, NOT `search` (KB-ORC-041). → REGINALD, CARL, LIQUID.

---

## Signal Dashboard (live 2026-07-22T15:42Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: hike at July mtg** | T1 | **22.2%** | **+10.3** | **+18.1** | $17.4M | $291.9K | ⏳7d — tail fattening, still hold-likely |
| **Fed: HIKE in 2026** | T1 | **66.5%** | **+5.0** | **+16.0** | $4.4M | $153.4K | 🔴 >66% TRIGGER FIRED — 2026 hike now base case |
| **Fed: NO cuts 2026** | T1 | **84.8%** | +0.1 | +4.0 | $6.4M | $146.4K | firming; dovish tell <70% firmly not fired |
| Fed: 1 cut 2026 | T1 | 9.5% | −1.0 | −5.0 | $2.2M | $114.7K | fading |
| Fed funds end-2026 (dist, top) | T1 | 31.0% | — | +0.9 | $529.8K | $11.8K | steady |
| US inflation >5% 2026 | T1 | 14.0% | −0.5 | +1.0 | $283.8K | $12.7K | creeping |
| **July CPI modal (top)** | T1 | **43.5%** | −2.5 | **+16.0** | $11.8K | $14.4K | top bucket firmed hard |
| US recession 2026 | T1 | 11.5% | −0.5 | +1.5 | $1.7M | $21.5K | calm (Kalshi 13.0%) |
| Major bank bailout <2027 | T1 | 12.0% | — | +0.5 | $3.8K | $1.4K | ⚠️thin, benign |
| Which banks fail EOY (top) | T1 | 3.7% | — | +0.1 | $399 | $271 | ⚠️thin, no name priced |
| US unemployment ladder (top) | T1 | 12.5% | +4.5 | +4.0 | $74.3K | $1.7K | ⚠️thin ⏮stale-date |
| **Hormuz normal by Dec 31** | T1 | **51.5%** | −4.0 | −7.0 | $5.6M | $232.0K | disruption persists (=48.5% disr), flat vs 7/17 |
| China invade Taiwan <2027 | T1 | 4.0% | −0.2 | +0.2 | $38.9M | $591.0K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 87.5% | — | +3.0 | $207.4K | $40.8K | ⏮stale-date |
| **WTI $100 (Jul) — war premium** | T2 | **14.9%** | +5.1 | **+8.8** | $761.0K | $39.5K | crossed >15% AM (17.8%), eased to boundary PM on thinning liq |
| **WTI $90 (Jul) — intraday high** | T2 | **65.6%** | +25.8 | **+45.8** | $1.5M | $107.3K | ⚠️INTRADAY not settle; premium stepping up |
| US invade Iran <2027 | T2 | 28.5% | +2.0 | **+11.0** | $46.1M | $597.1K | deep, rising — escalate tail fattening |
| US-Iran deal 2026 (top) | T2 | 34.5% | +3.0 | **+11.5** | $68.2K | $10.3K | resolve tail ALSO rising (bimodal) |
| US declares war on Iran <2027 | T2 | 5.0% | +0.5 | — | $697.9K | $88.9K | narrow mechanism, low |
| Iran leadership change / ends enrich Dec31 | T2 | 21.5% | — | −1.0 | $1.3M | $71.1K | ends-enrichment-Dec31 fading |
| Iran ends enrichment by Jul 31 | T2 | 0.8% | −0.1 | −0.6 | $933.5K | $73.1K | ⏳ near-zero |
| **Iran targets shipping (daily)** | T2 | Jul21 **1.0%** | −71.5 | — | $8.1K | — | tempo eased that day; ⛔display-quirk, event LIVE |
| Iran mil action vs Gulf St (daily) | T2 | live | — | — | $967.8K | — | ⛔display-quirk flag; event LIVE — war-widening axis |
| **Hormuz 0-ships closure by Jul31** | T2 | **5.7%** | −6.2 | −1.5 | $257.9K | $30.6K | closure tail FELL — no supply-shutdown priced |
| Bab el-Mandeb closed by Dec31 | T2 | 33.0% | −0.5 | +5.5 | $104.3K | $59.6K | Red Sea chokepoint, firming |
| Houthi targets shipping by Aug31 | T2 | 52.0% | −8.5 | +6.5 | $55.8K | $8.7K | Red Sea leg |
| Russia-Ukraine ceasefire Dec31 | T2 | 35.5% | — | −3.0 | $2.0M | $112.5K | slipping (Russia advancing — Vasylivka 73.5% +61/1d) |
| BOJ July decision (hold top) | T2 | 98.6% | −0.1 | −0.2 | $68.8K | $10.2K | hold near-certain |
| AI bubble burst 2026 | T2 | 16.6% | — | −0.6 | $2.3M | $18.6K | steady |
| MicroStrategy bankruptcy <2027 | T2 | 3.9% | +0.1 | −0.2 | $187.8K | $14.1K | control |
| US debt default <2027 | T2 | 4.9% | +0.1 | +1.5 | $16.0K | $3.5K | ⚠️thin, control |
| Mamdani freezes NYC rents <2027 | T2 | 91.6% | — | −0.1 | $281.7K | $20.6K | steady, near-certain |
| **Nothing Ever Happens 2026** | T3 | **66.5%** | −4.5 | **−12.0** | $689.1K | $51.5K | complacency crack deepened |
| Best asset 2026 (S&P top) | T3 | 67.0% | +1.5 | −0.5 | $180.9K | $18.1K | elevated — equity complacency intact |
| FL: Cat-4 hurricane <2027 | T3 | 24.0% | +1.0 | +2.5 | $334.4K | $1.5K | ⚠️thin |
| FL: Cat-5 hurricane <2027 | T3 | 11.5% | — | −1.0 | $137.8K | $1.4K | ⚠️thin |

**Kalshi corroboration (2026-07-22T15:42Z):** recession 13.0% (2.9M vol/805K OI); **Fed hike-by-July 24.0% (Δp +12)** — matches PM's July re-arm; >4.00%-after-July 2.0%; June CPI >3.8% 26% / U3 >4.2% 82% [finalized]; **Brent >$85 @ Jul31 settle-ref 73% (Δp +6)**; Iran-crude-prod Jul >2.0mbpd 77% (⚠️thin, uncollapsed); US-credit-downgrade-2026 4.0% (Δp −1, verify ticker vs 7/17's 16%); corporate-bankruptcy >750 83%.

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate. ⛔ = display-quirk false-RESOLVED on daily/ladder events (event is live; read recent legs via `event`). ⏳ = near-dated resolution.

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran → oil supply regime | 4 | 🔴 | Spread collapsed +40.5→+30.8pp VIA the WTI leg; WTI-$100 crossed >15% (17.8%); supply-loss pricing starting w/ no barrel lost | WTI-$100 >25% OR Hormuz-closure >30% OR Iran crude prod <2.0mbpd (real loss) |
| 2 | Fed path (re-arming hawkish) | 3 | 🔴 | July-hike 3.6→21.1%; hike-2026 64.5% (1.5pp under trigger); CPI-modal +16/7d | hike-2026 >66% (fires the re-arm) OR July mtg hikes 7/29 |
| 3 | Risk-on / complacency crack | 3 | 🟠 | NEH −12/7d; invade AND deal tails both +11/7d (bimodal) | NEH <30% OR gold takes best-asset lead |
| 4 | Oil premium (intraday) | 2 | 🟠 | WTI-$90-intraday 65.6% (+45.8/7d); Brent settle-ref 73% | 3 consecutive Brent settles >$85 (FALCON's bar) |
| 5 | Recession (converged, calm) | 1 | ⚪ | PM 11.5% / Kalshi 13.0% — fleet & crowd agree | market turns up OR fleet re-arms cyclical axis |

---

## Maintenance flags

- **🧹 Full file-sweep executed 7/22 (Will-directed) — see MAINTENANCE.md 7/22 entry.** Cleaned 8 dead watchlist pins (bank-failure/Hormuz-Jul15/Citi/BAC/WTI-$80 resolved; bitcoin-dip/china-Philippines/old-bank-Dec31 delisted → 2 coverage gaps logged), rolled 5 Kalshi June→July, refreshed VX.tsv (+2 owed threshold state-changes), corrected credit-downgrade level (KB-ORC-045: 4.0%/~6.75%-mid, not 7/17's 16%), refreshed TRADE.md, de-rotted CLAUDE.md's convergence matrix (→ pointer to this file), regen'd HISTORY.tsv. Both watchlists now pull with zero "not found."
- **🔴 Tripwire discipline validated:** the 7/17 pre-registered "spread collapse VIA the WTI leg = regime flip" tripwire fired exactly as specified — the WTI supply leg rose 10pp, disruption flat. This is the cleanest single-gauge call the tool was built for. Keep reading WHICH leg moves.
- **⚠️ WTI $100 supply-leg MONTH-ROLL (owed, near):** the July WTI-$100 market ends **2026-08-01** (9 days). When August opens, re-pin the new month's WTI-$100 market or the spread's supply leg silently ages out (script hard-exits if legs drift >3d — fails loud, but the re-pin is manual). Same for WTI-$85/$90-intraday and the Jul-31 Hormuz ladder (re-pin an Aug ladder).
- **Roll-watch — near-dated resolves:** Fed July mtg + BOJ (7/29); Iran July legs (enrichment/shipping) + Hormuz ladder + Brent settle-ref (7/31); July CPI (8/12). The Hormuz ladder + both Iran daily events show ⛔ false-RESOLVED (fetcher top-leg = old settled date) — events LIVE, read via `event`, do NOT re-pin on the flag.
- **Kalshi US-credit-downgrade reads 4.0% today vs 16% on 7/17** — likely a different market line/ticker got pulled; verify the specific ticker next session before treating as a real −12pp move.
- **Did NOT pull (git):** foreign uncommitted changes in DAEDALUS + FALCON dirs at session start — did NOT `git pull` (would risk their work) and DEFERRED push. Committed locally; push next clean session or when Will clears the tree.
- **Kalshi creds present** (chmod 600, unchanged); lane LIVE.

---

## BOTTOM LINE

One week ago the crowd's verdict was disciplined: "premium, not shortage." Today it is starting to *doubt its own verdict*. The disruption-supply spread I rebuilt to survive the blockade's resolution just did the one thing it was built to flag — it collapsed (+40.5→+30.8pp) **entirely because the supply leg rose**: WTI-$100 war-premium doubled again to 17.8%, crossing the >15% supply-loss-pricing threshold I pre-registered. In parallel the Fed re-armed hawkish (July-meeting-hike 3.6→21.1%, hike-2026 to 64.5%, ~1.5pp under the re-arm trigger) — the oil premium bleeding into the rate path. And yet **no barrel has actually been lost** (Kalshi Iran crude production still 77% at its sanctioned baseline): the crowd is pricing supply *risk* ahead of realized supply *loss*. That is precisely the leading-indicator posture — the gap between rising supply-risk pricing and flat physical supply is where the next move lives, and the WTI leg of the spread is the single number to watch. Complacency has stopped ignoring it (Nothing-Ever-Happens −12/7d, both Iran tails fattening). Routed to HAWK/BRENT/FALCON (regime-flip) and LIQUID/HENRY (Fed re-arm).

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log` + `python3 AGENTS/ORACLE/tools/disruption_supply_spread.py`*
