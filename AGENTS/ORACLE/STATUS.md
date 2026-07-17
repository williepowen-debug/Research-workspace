# ORACLE STATUS

**Updated:** 2026-07-17 (Fri ~10:05 ET, Will-directed boot after a **7-day gap** [last session 7/9]) — live pull both platforms + roll-watch (4 resolved pins) + **the escalation tail FIRED** (US blockade on Iran resolved YES) + disruption-supply spread **rebuilt v2** (v1 leg resolved out from under it) + 4 new markets pinned (Iran-Gulf daily, WTI-$85, Bab-el-Mandeb, Houthi).
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence
**Data:** live via `scripts/polymarket.py pull --log` + `scripts/kalshi.py pull --log`. Series → `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`. Derived → `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (v2, +40.5pp). Cross-agent surface → `NEXUS_BRIEF.md`. Metrics → `PREDICTION_MARKET_METRICS.md`.
**State:** 🟠 — **the escalation tail resolved YES: the US blockaded Iran (announced 7/13, enforced 7/14 16:00 ET).** The crowd repriced hard on disruption but only mildly on supply — WTI-$100 war-premium doubled (3.2%→7.5%) yet is still only ~8%, so this is still a **premium story, not a shortage story**, independently matching FALCON's read. Complacency finally cracked (Nothing-Ever-Happens −10/7d). July Fed meeting now priced a near-certain hold (July-hike 14.5%→3.6%).

---

## Alerts (read first)

**🔴 ESCALATION TAIL FIRED — US blockade on Iran RESOLVED YES.** Announced Mon 7/13; USN enforcement in effect Tue 7/14 16:00 ET (CNN/Axios/NBC). Polymarket settled 100% across all forward legs ($1.9M vol Jul-31 leg, liq drained); past-dated Jun-30 leg at 0% = true-resolution signature, not the ladder display quirk. **CALIBRATION WIN for HAWK:** on 7/9 this market read 48.0% and HAWK's independent ladder D-rung read 46% (KL≈0.001 bits) — that ~47% two-source consensus **resolved YES within 4 days.** One event isn't a track record, but it's a rare scored point for the ladder method. FALCON's 7/17 note independently treats the blockade as live fact (US interdicted the *Belma* en route to Kharg). → HAWK, BRENT, FALCON, PROME. (KB-ORC-033; leg retired from watchlist + spread tool.)

**🟠 DISRUPTION REPRICED HARD, SUPPLY ONLY MILDLY — still premium, not shortage.** Hormuz-normal-Dec31 61.5%→**51.5%** (Δ7d −11.0); 30-ships-transit-Jul31 **collapsed −66.2/7d**; every ladder rung fell (crowd expects less recovery). WTI-$100-war-premium **3.2%→7.5%** (Δ7d +5.0) — more than doubled but **still only ~8%**. The crowd reads this as premium/harassment, not barrels lost — independently reproducing FALCON's "the decoupling broke on RISK PREMIUM, not one lost barrel" (four supply *events* this week, zero lost supply). Crowd convergence with FALCON's official PortWatch data (five consecutive sub-18/day transit prints 7/8-7/12). **Reconciled to BRENT's canonical 88-ships/day baseline (denominator ruling, ~140 rejected as peak-day artifact): the ladder rungs = 30/40/50/60/80/100 ships = 34/45/57/68/91/114% of normal on any single day — crowd prices only 30.6% odds of even ONE day at 34% of normal by Jul31, corroborating BRENT/FALCON's live 10/88=11% print.** → HAWK, BRENT, FALCON. (KB-ORC-034, KB-ORC-038.)

**⚪ SPREAD TOOL REBUILT v2 — was broken by its own success.** v1's disruption leg (P(US blockade)) resolved YES → pinned 100% forever → the tool crashed on the drained-liquidity null. v2 = **P(Hormuz transit disruption persists, =1−P(normal-Dec31)) − P(WTI $100 war premium)** = 48.5% − 7.5% = **+40.5pp** (2026-07-17). Closure proxy (16.5%) demoted to a context column (a full closure is a *supply* event — wrong side of the spread). Guards added: hard-exit on resolved/drained/thin leg + WTI-month drift. WIDE = premium not shortage; COLLAPSING (read *which* leg) = supply fear catching up = HAWK/BRENT/FALCON tripwire. (KB-ORC-035.)

**🟠 WAR-WIDENING TEMPO — two new daily-cadence markets pinned.** Iran-targets-shipping (on-date): **0% Jul 6-13, then FIRED Jul 14 (98%) + Jul 17 (82%)** — attacks resumed the *same day* the blockade took effect after ~a week quiet. Iran-military-action-vs-Gulf-State ($1.7M, previously untracked): Iran striking neighbours every ~2-3d (Jul 9/12/14/17 YES). This is the widening-of-the-war axis and the cleanest daily tempo gauge on the board. Corroborates FALCON's WSJ read (Iran attacking the bypass/shuttle runs). → HAWK, BRENT, FALCON. (KB-ORC-036.)

**🟡 OIL PREMIUM STEPPED UP A THRESHOLD — but mind the trap.** "WTI hits $85 (July)" **57.5% (Δ7d +42.0, $1.0M vol)** — pinned. **⚠️ This resolves on INTRADAY HIGH, not a settle. Do NOT read it as confirmation of FALCON's $85 thesis** — FALCON's bar is 3 consecutive *settles* >$85 (Brent), of which zero have printed (high settle $84.95). Different question; welding them is the fused-true-facts trap (fleet memory 7/16). Tracked as an oil-premium tell on its own terms only. → BRENT, HAWK.

**🟡 NEW CHOKEPOINT COVERAGE — Bab el-Mandeb + Houthi pinned.** Bab-el-Mandeb-closed ($6.2M deep event): by-Dec31 **31.5% (Δ7d +10.5)**. Houthi-targets-shipping: by-Aug31 **57.0% (Δ7d +36.5)**. Both were untracked; they complete the shipping-disruption axis (Red Sea / Suez feed) alongside Hormuz. → HAWK, BRENT.

**🟡 FED — July meeting now a near-certain HOLD; 2026-hike tail still live.** July-hike **14.5%→3.6%** (Δ7d −10.9, $14.6M vol) — the meeting is priced as a hold. But Fed-HIKE-2026 still **51.5%** and No-cuts-2026 firmed to **83.7%** (Δ7d +6.0) — dovish tell (<70%) firmly not fired; if anything the crowd got *less* dovish on the week. → LIQUID, HENRY.

**🟡 CPI — July market prices a DISINFLATION step-down even as energy reprices.** July-CPI-modal (pinned, replaces resolved June event): modal **3.4% (31.0%)** / 3.3% (27.5%) / 3.5% (15.0%) — below June's ~3.7% print. Crowd expects CPI to *fall* while the oil/Hormuz premium reprices — a genuine tension, HENRY's to adjudicate. ⚠️thin ($6.1K liq). Kalshi June finalized: >3.6% 99% / >3.8% 26% (June ~3.7%). → HENRY, LABOR. (KB-ORC-037.)

**⚪ SENTIMENT — complacency cracked for real this time.** Nothing-Ever-Happens **72.5% (Δ7d −10.0)** — down a full 10pp, the clearest tail-risk-awakening tell since the truce collapse (was only −4/7d on 7/9). Best-asset-S&P still elevated **68.5%**. → RED, VIOLET, HENRY.

---

## Signal Dashboard (live 2026-07-17T14:10Z, Polymarket unless noted)

| Market | Tier | Prob | Δ1d | Δ7d | Vol | Liq | Read |
|--------|:--:|--:|--:|--:|--:|--:|------|
| **Fed: hike at July mtg** | T1 | **3.6%** | −0.2 | **−10.9** | $14.6M | $464.2K | July now priced a hold |
| **Fed: HIKE in 2026** | T1 | **51.5%** | — | — | $4.2M | $121.4K | tail still live |
| **Fed: NO cuts 2026** | T1 | **83.7%** | −0.1 | **+6.0** | $6.3M | $151.1K | dovish tell <70% firmly not fired |
| Fed: 1 cut 2026 | T1 | 12.5% | — | −2.0 | $2.1M | $135.0K | fading |
| Fed funds end-2026 (dist, top) | T1 | 30.9% | — | −1.1 | $529.7K | $12.5K | steady |
| US inflation >5% 2026 | T1 | 12.5% | — | −1.0 | $282.4K | $24.6K | contained |
| **July CPI modal (top, 3.4%)** | T1 | **31.0%** | −3.5 | — | $4.2K | $6.1K | ⚠️thin — disinflation step-down priced |
| US recession 2026 | T1 | 11.5% | +1.5 | +1.5 | $1.7M | $16.5K | calm (Kalshi 12.0%) |
| Major bank bailout <2027 | T1 | 11.5% | — | +0.5 | $3.8K | $1.4K | ⚠️thin, benign |
| Which banks fail EOY (top) | T1 | 3.6% | — | −0.2 | $280 | $1.3K | ⚠️thin, no name priced |
| US unemployment ladder (top) | T1 | 13.6% | −0.1 | +1.0 | $119.7K | $1.6K | ⚠️thin ⏮stale-date |
| **Hormuz normal by Dec 31** | T1 | **51.5%** | −5.0 | **−11.0** | $5.3M | $258.5K | disruption persists (=48.5% disr) |
| China invade Taiwan <2027 | T1 | 3.8% | — | −0.2 | $38.6M | $746.2K | deep, low |
| China GDP 2026 (sub-5% top) | T1 | 85.5% | — | +5.5 | $198.1K | $45.4K | ⏮stale-date |
| **US blockade on Iran** | T2 | **RESOLVED YES** | — | — | $1.9M | — | ⛔ FIRED 7/14 — see alert |
| **Iran targets shipping (daily)** | T2 | Jul14 98%, Jul17 82% | — | — | $76.2K | — | ⛔display-quirk flag; event LIVE |
| **Iran mil action vs Gulf St (daily)** | T2 | Jul17 94%, Jul18 61.5% | — | — | $126.1K | — | ⛔display-quirk flag; event LIVE — war widening |
| **Hormuz ladder 30-ships/day Jul31** | T2 | **30.6%** | −1.8 | **−66.2** | $338.8K | $49.1K | =34% of 88-normal on any 1 day; recovery-doubt hardening |
| Hormuz ladder 40-ships/day Jul31 | T2 | 11.5% | −2.0 | −59.5 | $78.2K | $37.1K | =45% of 88-normal; (80-rung=91% at 1.3%) |
| **Hormuz 0-ships closure by Jul31** | T2 | **16.5%** | +9.8 | **+7.5** | $198.7K | $27.0K | closure tail rising, still low |
| **WTI $100 (Jul) — war premium** | T2 | **7.5%** | +0.8 | **+5.0** | $406.1K | $84.4K | doubled but still ~8% — no shortage priced |
| **WTI $85 (Jul) — intraday high** | T2 | **57.5%** | +3.0 | **+42.0** | $1.0M | $39.2K | ⚠️INTRADAY not settle — NOT FALCON's $85 |
| **Bab el-Mandeb closed by Dec31** | T2 | **31.5%** | −0.5 | **+10.5** | $41.7K | $59.7K | NEW — Red Sea chokepoint |
| **Houthi targets shipping by Aug31** | T2 | **57.0%** | +7.5 | **+36.5** | $33.7K | $11.6K | NEW — Red Sea leg |
| US invade Iran <2027 | T2 | 22.5% | −1.0 | +6.0 | $43.7M | $686.9K | deep, rising |
| US declares war on Iran <2027 | T2 | 4.5% | −0.5 | −1.0 | $660.6K | $87.4K | narrow mechanism, low |
| Iran leadership change Dec31 | T2 | 19.5% | −1.0 | +2.5 | $3.3M | $69.9K | firming |
| Iran ends enrichment by Dec 31 | T2 | 19.5% | −3.0 | −3.0 | $1.3M | $99.3K | fading |
| US-Iran deal 2026 (top) | T2 | 28.0% | −1.0 | −7.5 | $64.8K | $13.9K | slipping (collapse repriced away deal hopes) |
| Russia-Ukraine ceasefire Dec31 | T2 | 36.5% | −1.5 | −4.0 | $2.0M | $126.4K | slipping |
| China-Philippines clash <2027 | T2 | 10.5% | — | −1.0 | $1.5M | $69.0K | easing |
| BOJ July decision (hold top) | T2 | 98.7% | — | +0.1 | $63.0K | $9.9K | hold near-certain |
| AI bubble burst 2026 | T2 | 16.7% | −0.5 | +1.5 | $2.3M | $25.0K | steady |
| MicroStrategy bankruptcy <2027 | T2 | 4.1% | −0.1 | −0.1 | $186.7K | $15.7K | control |
| US debt default <2027 | T2 | 3.9% | +0.1 | +0.4 | $15.9K | $4.8K | ⚠️thin, control |
| **Mamdani freezes NYC rents <2027** | T2 | 91.8% | +0.1 | −0.1 | $276.7K | $31.2K | steady, near-certain |
| **Nothing Ever Happens 2026** | T3 | **72.5%** | — | **−10.0** | $664.1K | $40.5K | complacency cracked |
| Best asset 2026 (S&P top) | T3 | 68.5% | +1.0 | +2.0 | $180.7K | $19.7K | elevated |
| FL: Cat-4 hurricane <2027 | T3 | 22.0% | — | — | $334.3K | $2.2K | ⚠️thin |
| FL: Cat-5 hurricane <2027 | T3 | 12.5% | — | −4.0 | $137.8K | $1.6K | ⚠️thin |

**Kalshi corroboration (2026-07-17T14:10Z):** recession 12.0% (Δp +2.0, 2.9M vol/807.5K OI); July-hike (>3.75%) 4.0% (Δp −3.0) — matches PM's July-hold read; >4.00% 1%; June CPI >3.6% 99% / >3.8% 26% [finalized ~3.7%]; June U3 >4.2% 82% [finalized].

Δ in pp. ⚠️thin = liq < $5K (do not mark on one print; ≥3-day re-check). ⏮ = live market w/ stale endDate. ⛔ = display-quirk false-RESOLVED on daily/ladder events (event is live; read recent legs via `event` command).

---

## Convergence Matrix

| # | Market | Score | Status | Key Signal | Upgrade Trigger |
|---|--------|:--:|:--:|------------|-----------------|
| 1 | Iran escalation (blockade FIRED) | 4 | 🔴 | US blockade RESOLVED YES 7/14; shipping attacks resumed same day; Gulf-state strikes every 2-3d; disruption spread +40.5pp | WTI-$100 >15% (supply shock) OR Hormuz-closure >30% OR Bab-el-Mandeb closes |
| 2 | Oil premium (rising, not shortage) | 2 | 🟠 | WTI-$100 doubled to 7.5% but still low; WTI-$85-intraday 57.5% | WTI-$100 >15% = crowd flips to supply-loss pricing |
| 3 | Fed path (July hold, tail live) | 2 | 🟡 | July-hike 3.6% (hold priced); hike-2026 51.5%; no-cuts firmed 83.7% | hike-2026 >66% (re-arm) OR no-cuts <70% (dovish turn) |
| 4 | Risk-on / complacency crack | 2 | 🟠 | NEH −10/7d (real crack); S&P best-asset still 68.5% | NEH <30% OR gold retakes best-asset lead |
| 5 | Recession (converged, calm) | 1 | ⚪ | PM 11.5% / Kalshi 12.0% — fleet & crowd agree | market turns up OR fleet re-arms cyclical axis |

---

## Maintenance flags

- **Roll-watch executed (7/17) — 4 resolved pins:** June CPI → July CPI event; Iran-targets-shipping (by-date) + US-blockade → **both resolved YES**, replaced by the daily-cadence on-date events (blockade retired outright, it's a one-time fire); Hormuz ladder Jul-31 top leg settled (event still live). **4 new adds:** Iran-Gulf-State daily, WTI-$85-intraday, Bab-el-Mandeb, Houthi.
- **Display-quirk false-RESOLVED** on the two daily events (Iran-shipping, Iran-Gulf) + the Hormuz ladder — fetcher's top-leg = old settled daily date; events are LIVE. Annotated in watchlist; read recent legs via `event`. Do NOT re-pin on the flag.
- **Spread tool v2 rebuilt** — WTI supply leg has a **manual month-roll** owed action (re-pin the new month's WTI $100 market when the front month turns; script hard-exits if legs drift >3d). Cadence + warnings now homed in `CLAUDE.md` (PROME/DAEDALUS PAT-041 finding, inbox 7/10 — closed).
- **PROME inbox item (7/10) processed & closed:** DAEDALUS's two owner-lane durability flags on the spread tool (home the cadence durably + note the WTI month-roll) — both done in this session's CLAUDE.md edits.
- **7/9→7/17 gap:** own inbox had one PROME durability note (processed); no domain-agent signal backlog.
- **Kalshi creds present** (chmod 600, unchanged); lane LIVE. Structural-credit gap-fills (KXCREDEFMAX etc.) NOT re-checked this session — carried to next (was comprehensively zero-open 7/9).
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.

---

## BOTTOM LINE

The escalation tail HAWK and the crowd both priced at ~47% on 7/9 **resolved YES within four days**: the US announced a naval blockade of Iran on 7/13, enforced 7/14 at 16:00 ET. That's a rare scored point for HAWK's ladder method (KL≈0.001 bits at the 7/9 mark). But the crowd's read of the *consequence* is disciplined and matches FALCON exactly: it repriced disruption hard (Hormuz-normal −11/7d, transit ladder −66/7d) and supply only mildly (WTI-$100 doubled but sits at just 7.5%). **This is still a risk-premium story, not a lost-barrels story** — four "supply events" this week, zero lost supply. The disruption-supply spread, rebuilt to survive the blockade's resolution, reads +40.5pp — wide, i.e. premium without shortage; a *collapse* of that spread (specifically the WTI leg rising) is the regime-flip tripwire. The one genuinely new development is tempo: Iran resumed shipping attacks the same day the blockade hit, and is striking Gulf states every 2-3 days — the war is widening even as the oil market stays calm. Complacency finally registered it (Nothing-Ever-Happens −10/7d).

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log` + `python3 AGENTS/ORACLE/tools/disruption_supply_spread.py`*
