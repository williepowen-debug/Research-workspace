# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-07-02 (Thu, ~1:30–2:30 PM ET) — boot + closeout after 5-day gap (last session 6/27), THEN a Will-driven working session: dual-source liveness confirm → 17:51Z re-pull (flat) → **volume/sentiment anomaly sweep** → 2 findings routed (Mamdani NYC rent-freeze → REGINALD; US-blockade-Iran tail → HAWK/BRENT). 3 commits, all pushed.
**Last updated:** 2026-07-02 (session-end, post volume-sweep)

## CHANGES SINCE (what moved, 6/27 → 7/2)
- **Fed hawkish overshoot ROLLING OVER onto HOLD (not a dovish pivot).** July-hike collapsed 18.1%→**9.7%** (−10.5/7d, −9/1d) — essentially priced out; hike-2026 51.5%→**46.5%** (broke <50); end-2026 modal now **HOLD 3.75% (25.5%)** w/ multi-hike ≥4.5% faded to 8.0%. Kalshi corroborates (July-hike 14% −6, >4.00% 1%). **No-cuts still 77.5%** (dovish tell = <70%, NOT fired). Trajectory: hike-2026 uptrend *flattening* (+11/30d, down from +21) — spike rolling over, not reversing.
- **Iran two-axis CONFIRMED w/ physical data.** Hormuz traffic materially reduced ("20-40 avg daily" 97.2% +65.8/7d; "60 ships any day" 0.9%; forward 100/day-normal only 9% for July); Hormuz-normal-Jul15 8.5% (−29/7d); diplomacy collapsing (deal-components −25/7d to 38.5%, enrichment-Dec −24/30d). by-Jun27 attack **resolved YES** → fresh forward window (by-Jul31 46.5%, by-Aug31 69%). **NEW: US-blockade-on-Iran 30.5% by-Dec ($780K deep)** = regime-change tripwire. **Oil STILL calm** (WTI-$100-Jul 1.6%, $80 11.5%) — no supply premium.
- **Risk-on at SERIES HIGH.** Best-asset S&P 56%→**67.5%** (+13/7d, +28/30d, +49/90d, at range top); NEH 84% (at high). Deepest/most-persistent board trend.
- **June U3 finalized ~4.2%** (Kalshi >4.2% 82% [finalized 7/2]) — mild labor tick. June CPI contained 3.6-3.8 (PM modal-3.8% 45.9% −6.8, dist spreading; Kalshi >3.8% 31% +8). Res 7/14-15.
- **Bank provisions diagnostic drift:** Citi Q2 >$2.9B 71.5%→60%, BAC >$1.4B 37.5%→43% (+6/7d). Both thin (≤$434 liq). Bank cluster benign.

## WHAT I DID
1. Live pull both platforms (Polymarket 36 mkts + Kalshi 8) + trajectory refresh (HISTORY 4,856 rows / 36 mkts); movers discovery sweep (16 hits).
2. **Roll-watch executed** — dropped 6 resolved June markets; **repinned 2 broken pins**: WTI-July-ladder event (returned 100% RESOLVED) → two live legs ($100 war-premium `will-wti-reach-100-in-july-2026-928` 1.6%, $80 elevated `will-wti-reach-80-in-july-2026-791` 11.5%); iran-targets-shipping-Jun27 (resolved YES) → fresh forward event `...byptptpt-20260629202434609` (by-Jul31 46.5%). **2 new adds**: US-blockade-on-Iran `us-announces-blockade-on-iran-byptptpt-20260622191049039` + Hormuz ships-transit ladder `...by-july-31-20260626152655081`. All verified resolving cleanly.
3. **STATUS full rewrite** (alerts→top, dashboard, trajectory, convergence, maintenance). **NEXUS_BRIEF full refresh** (mandatory). **KB +4** (020 Fed / 021 Iran-two-axis / 022 risk-on / 023 Kalshi-corroboration; marked **018 SUPERSEDED**). **VX rewrite** (all 8 rows refreshed + added VX-ORC-09 risk-on).
4. **Fixed stale CLAUDE.md Kalshi-creds note** — the 7/1 "creds MISSING" flag was wrong; creds present + chmod 600, Kalshi lane LIVE. Corrected to ✅ 7/2.
5. Fixed STATUS BTC-dip row (pin broke, no CLOB token) — showed honest n/a not a proxy number.
6. **Confirmed both data sources live** (Will asked) — Polymarket (Gamma, no-auth) + Kalshi (`exchange_active:true`). 17:51Z re-pull both platforms = **flat vs 17:26Z boot snapshot** (only Fed 1-cut +1 to 15.5%); logged fresh time-series points, no analytical churn.
7. **Volume/sentiment anomaly sweep** (Will asked: surprising changes / insider positioning). Method: `movers --all` (market-wide, price-ranked) + diffed ODDS_LOG cumulative volume across pulls for %-surge. Verdict: **NO insider smoking gun** (every big move has a public driver; no liquid-move-without-news; deep tails flat). But found: (a) Fed July-hike = biggest genuine volume surge (**46% of lifetime vol in 5d**, deep, directional) → dovish repricing is HIGH-conviction money; (b) **off-radar credit signal — Mamdani NYC rent-freeze 93.8% (+54.8/7d, $275K)** → NYCB/Flagstar-2024 multifamily collateral path; (c) US-blockade-Iran tail 30.5% by-Dec (~$780K deep) = the shipping→supply-shock bridge.
8. **Routed both** — Mamdani → watchlist + KB-024 + STATUS(alert+row) + NEXUS(sending) + **outbox to REGINALD**; US-blockade → **outbox to HAWK/BRENT**. Both flagged as sentiment shifts NOT insider tells (public drivers, moderate liq).

## NEXT SESSION (priority order)
1. **🟡 RED** — still owed a current GDP/NBER-comparable fleet recession number (carried since 6/13). Not urgent (crowd & fleet both calm, no live divergence) but the divergence math depends on it.
2. **🟢 BTC-dip $40K repin** — dashboard row's slug lost its CLOB token; re-search a clean Dec-31 BTC-dip market. Low priority (BTC strong).
3. **🟢 Kalshi gap-fill prize:** re-check **CRE default (KXCREDEFMAX), CC delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY)** for newly-opened events — the structural-credit axis PM can't see (the real edge if it re-ignites). No open event as of last check.
4. **Fed dovish-tell:** **no-cuts <70%** = the real dovish turn (currently 77.5%, slipping). Hike re-break >66% = hawkish re-arm. → LIQUID/HENRY.
5. **Iran shipping axis:** watch **US-blockade-on-Iran** (30.5% Dec, the regime-change tripwire) + **WTI-$100-July** (supply-shock confirm, 1.6%) + Hormuz physical-traffic ladder. Fresh-attack by-Jul31 46.5%.
6. **Near-dated resolutions (7/14-15):** Citi/BAC provisions + June CPI. Watch surprise-vs-priced. **Jul 29:** Fed + BOJ.
7. **movers:** run as the standing discovery sweep each session.
8. **🟠 Mamdani follow-up:** watch for REGINALD's reply (outbox `2026-07-02_to-reginald_mamdani-nyc-rent-freeze.md`) + track the Mamdani trajectory each session (accel toward 100 or reversal = the tell). NYC multifamily → NYCB/Flagstar collateral.
9. **🟢 TOOL BUILD — volume-ranked market-wide scan.** Coverage gap found this session: `movers` is *price-move*-ranked, so it misses a big volume dump that DIDN'T move price (the purest Type-4 insider tell — "$500K into a 2% market, still 2%"). Add a `polymarket.py` mode that ranks untracked markets by recent volume (volume24hr / lifetime), not price-change. Will greenlit building it.
10. **🟢 MEMORY.md is STALE** — tail still says "Kalshi not wired," "push deferred to a Will window," "bank-failure-Jun30 resolves 6/30." All outdated (Kalshi wired 6/27, auto-push live, market resolved). Refresh or archive; SCRATCH is the live handoff.

## CARRY-FORWARD
- **Push state:** all pushed, `ahead=0`. This session's commits: **d97e2d34** (boot closeout) → **47bab79c** (17:51Z fresh points) → **b48d47b7** (Mamdani/blockade routing) → [this final SCRATCH/NEXUS closeout]. **NOTE:** DEWEY + WALTER have uncommitted working-tree changes (DEWEY active concurrently on this box) — NOT mine, left untouched; committed only explicit `AGENTS/ORACLE/` pathspecs. Did NOT pull (uncommitted work outside my dir).
- **Watchlists:** Polymarket ~34 live (post roll-watch); Kalshi 8. Kalshi creds `~/.config/kalshi/{key_id.txt,private_key.pem}` (chmod 600, present, NEVER in repo).
- **Tooling:** `polymarket.py` = search/market/event/pull/history/movers; `kalshi.py` = status/search/market/event/series/pull. Both run at every EXECUTE.
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.

## OPEN HYPOTHESES
- **The dovish turn still hasn't started** — Fed move is overshoot-→-hold (no-cuts still 77.5%). The market removed *hike urgency*, not higher-for-longer. Watch no-cuts <70%, not the noisier hike series.
- **Residual edge = dormant structural credit axis** re-igniting before the crowd prices it. Nothing on either platform prices it yet. Kalshi CRE-default / CC-delinquency (when they open) = cleanest forward read.
- **Risk-on is over-extended** (best-asset +49/90d at series high, NEH 84%) — a full quarter of complacency to unwind if the structural axis fires. The more extended, the sharper the potential unwind.
- **Iran shipping = the live tail, priced as transit-disruption not supply-shock.** The US-blockade market (30.5% Dec) is the crowd's regime-change probability — the thing to watch for the harassment→supply-shock flip that would finally move oil.
- **Cross-platform divergence** is a live tool: PM vs Kalshi on the same event. Today they agree (calm) — a future split is itself signal.
