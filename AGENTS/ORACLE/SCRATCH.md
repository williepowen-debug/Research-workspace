# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-06-27 (Sat) — routine boot. Synced (origin==HEAD), inbox empty, live pull (33 mkts), trajectory refresh, **roll-watch executed** (5 June markets resolve 6/30-7/1 → replacements located + added), workbook + cross-agent surface rewritten. Headline: the post-FOMC **hawkish overshoot is cooling, not a dovish pivot** — caught by the trajectory check.
**Last updated:** 2026-06-27

## CHANGES SINCE (what moved, 6/22 → 6/27)
- **Fed hike-2026 51.5% (Δ7d −14)** — BUT `history` shows Δ30d **+21**: it spiked to a ~66% peak ~6/20 (post-FOMC dots) and retraced. My 6/22 reading (61.5%) was near that peak → the −14 is a *pullback within an uptrend*, not a reversal. No-cuts holds 79.5% (Δ30d +13). End-2026 4.0% bucket −12.8/7d → 3.75% modal. July-hike 18.1% (−6.6).
- **June CPI modal "3.8%" 52.7% (Δ7d +12.2)** while 3.9%/4.0% buckets *fell* — crowd consolidating on a *contained* print (not more inflation). Resolves 7/15.
- **Risk-on rotation:** best-asset → S&P 500 56% (Δ30d +21), Gold fading 26% (−6/7d), BTC 16.5%. NEH 83.5%. BTC-dip-$40K 30% (−6/1d).
- **Iran = TWO-AXIS (corrected intra-session 6/27):** nuclear/war de-escalated (enrichment-Jun30 1.4%, WTI-$100 0.4%) BUT **Hormuz/shipping axis RE-ESCALATING** — Iran struck the *Ever Lovely* 6/25, US retaliated 6/26; crowd prices "Iran targets shipping" 81.5% by-Jun30 → 93.5% by-Aug31. Hormuz-normal-Jun30 collapsed to 3.5% (this attack is why). Crowd: harassment ≠ supply shock (WTI-$100 stays dead).

## WHAT I DID (this closeout)
1. Live `pull --log` (33 mkts → ODDS_LOG) + `history --write` (HISTORY.tsv now 4,796 rows / 33 mkts).
2. **Decoded the "(top)" event markets:** June-CPI (modal 3.8%), Fed-funds-dist (modal slid to 3.75%, 4.0% bucket −12.8/7d), best-asset (S&P leads). Resolved the CPI-vs-hike "paradox" — both point dovish-at-margin.
3. **Trajectory check** reframed the Fed move from "reversal" → "overshoot cooling" (the −14/7d sat against a peak baseline).
4. **Roll-watch executed** — located + added 6 replacement surfaces to `watchlist.tsv`: Iran-enrich Jul-31 + Dec-31 + **US-Iran-deal-2026 components event**; **WTI-July ladder event**; **Hormuz-Jul-15**; **which-banks-fail-by-EOY-2026 event**. (No July single-binary bank-failure market exists yet.)
5. **Workbook:** KB-ORC-014/015/016/017 appended; KB-ORC-009 & 011 marked SUPERSEDED. VX.tsv refreshed to current (all rows 6/27, +new VX-ORC-08 Fed-hike).
6. **STATUS + NEXUS_BRIEF** full rewrites (current state, alerts to top).
7. **Outbox cleanup:** archived 3 stranded 6/18 files → `outbox/delivered/` (2 retracted/wrong: Iran-deescalation, recession-divergence; 1 satisfied: wire-into-fleet — ORACLE now in WALTER REGISTRY + PROME STATUS).
8. **CLAUDE.md step 14** swapped "defer push" → "auto-push at closeout via safe-push.sh" (lazy-swept to the 6/26 single-machine policy).
9. Auto-memory: `finding_delta_vs_own_prior_local_extreme` (trajectory-context before calling a reversal).
10. **Movers-discovery (Will-asked, post-closeout):** scanned Polymarket beyond watchlist (scratchpad `movers*.py` — order-by-volume + order-by-price-change, domain-filtered). Findings: (a) macro board dead-flat (no fed/recession/bank/inflation movers — confirms calm); (b) **Iran-targets-shipping** event 81%+ fwd (Ever Lovely struck 6/25, US strikes 6/26) → added to watchlist + corrected STATUS/NEXUS/KB-018 to two-axis; VX-ORC-04 re-armed 🟠; (c) Venezuela "US forces again" 99% (+94/7d) = **earthquake disaster relief**, NOT oil escalation (news-checked) — not added. Most other big movers = mechanical month-end crypto/silver/WTI settlement resolutions.
11. **Kalshi wired (Will-driven, 6/27):** built `kalshi.py` + `kalshi_watchlist.tsv` + `KALSHI_ODDS_LOG.tsv`; first pull confirms strong cross-platform corroboration (recession 10/11, July-hike 18/18) + adds clean U3/CPI reads where PM thin. Creds secured outside repo. CLAUDE.md/MAINTENANCE updated; KB-ORC-019. (Live-verified gotchas: base=api.elections.kalshi.com, fields=*_dollars/*_fp, prices via /markets not nested /events, depth=OI.)

## NEXT SESSION (priority order)
1. **🟡 RED** — still owed a *current* GDP/NBER-comparable fleet recession number (carried since 6/13). Divergence math depends on it.
2. **Roll-watch / drop resolved:** after 6/30-7/1, comment out the resolved June rows in `watchlist.tsv` (Iran-Jun30, bank-failure-Jun30, named-bank-Jun30, Hormuz-Jun30, WTI-$100-Jun). Replacements already tracking. Re-search a July single-binary bank-failure market (none existed 6/27).
3. **Fed dovish-tell watch:** if **no-cuts breaks <70%** that's the real dovish turn (vs the current overshoot-cooling). Hike re-break >66% = hawkish re-arm. → LIQUID/HENRY.
4. **Energy red-team (HAWK+RED, spawned 6/26):** the new US-Iran-deal-components event + WTI-July ladder + Hormuz-Jul15 are their best crowd surfaces — surfaced in NEXUS_BRIEF FORWARD CATALYSTS. Feed actively if they pull me in.
5. **Jul 14 Citi/BAC provisions, Jul 15 June-CPI:** crowd central estimate vs actual prints. Citi-prov is $210-liq — diagnostic only.
6. **Kalshi WIRED ✅ (6/27).** `scripts/kalshi.py` (trade-api v2, RSA-PSS, read-only) + `kalshi_watchlist.tsv` (8 mkts) + `workbook/KALSHI_ODDS_LOG.tsv` (separate schema). Creds in `~/.config/kalshi/` (outside repo). **Corroboration:** recession Kalshi 10% vs PM 11% (Kalshi 2.6M vol — far deeper); July-hike 18% vs PM 18.1%. **Adds where PM thin:** June U3 modal ~4.2%, June CPI contained (>3.6% 97%, >3.8% 27%). **Next on Kalshi:** (a) roll near-dated June CPI/U3 (resolve 7/2, 7/14) like Polymarket; (b) re-check gap-fill series for open events to pin — CRE default (KXCREDEFMAX), CC delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY) — these are the structural-credit-axis tells PM lacks; (c) no VIX market on Kalshi (gap persists). EXECUTE now runs both fetchers.

## CARRY-FORWARD
- **Push state:** this closeout committed + auto-pushed via `scripts/safe-push.sh` (ff-gated, single-machine). If safe-push aborted non-ff (cross-machine), commits are local-only — flag Will, do NOT force.
- **Watchlist now ~39 markets** (34 + 6 roll replacements − overlap); June rows still tracking through 6/30 resolution. `HISTORY.tsv` 4,796 daily rows.
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.
- **Unemployment ladder top +8.6/1d** was a thin ($1.6K) single-print spike — discounted, not marked.
- **LIQUID figure-check** closed-ish (picked up, no verify-back; market moved 23%→18%).

## OPEN HYPOTHESES
- **The dovish turn hasn't started yet** — the Fed move is overshoot-correction (no-cuts still 80%). The real signal would be **no-cuts <70%**. Watch that line, not the noisier hike-2026 series.
- **Residual edge = dormant structural credit axis** (HENRY) re-igniting before the crowd prices it — watch for the first market move that front-runs it (Citi/BAC provisions into 7/14 are the nearest candidate, but thin).
- **South China Sea > Taiwan** still holds: China-Philippines clash 13.5% prices above Taiwan-invasion 5.5% — the crowd's near-term China flashpoint.
- **Risk-on may be over-extended:** S&P best-asset +21/30d + NEH 83.5% = a lot of complacency to unwind if the dormant axis fires.
