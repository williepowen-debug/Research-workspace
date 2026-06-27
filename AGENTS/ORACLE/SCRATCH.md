# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-06-27 (Sat) — boot + routine closeout, then a long Will-driven working session: movers-discovery → **Iran two-axis correction**; **Kalshi wired** (2nd real-money source); **`movers` command** built + tightened; git-protocol **fleet-aligned**. ~11 commits, all swept to origin via push-train.
**Last updated:** 2026-06-27 (session-end closeout)

## CHANGES SINCE (what moved, 6/22 → 6/27)
- **Fed = hawkish OVERSHOOT cooling, NOT a pivot.** hike-2026 51.5% (Δ7d −14 but **Δ30d +21**, off ~66% Jun-20 peak); no-cuts 79.5% (Δ30d +13) pinned. Dovish tell to watch = **no-cuts <70%** (hasn't happened).
- **June CPI** consolidating on a contained **3.8%** (Polymarket modal 52.7%; Kalshi >3.6% 97% / >3.8% 27% → leans 3.6-3.7). Resolves 7/14-7/15.
- **Risk-on rotation:** S&P best-asset 56% (Δ30d +21), gold fading 26%, NEH 83.5%, BTC-dip fading.
- **Iran = TWO-AXIS:** nuclear/war de-escalated (enrichment 1.4%, WTI-$100 0.4%) BUT **Hormuz/shipping RE-ESCALATING** — Iran struck *Ever Lovely* 6/25, US retaliated 6/26; crowd prices "Iran targets shipping" 81.5% by-Jun30 → 93.5% by-Aug31. Crowd: harassment ≠ supply shock (oil tail = transit disruption, not war-premium spike).

## WHAT I DID
1. Live pull (33 mkts) + trajectory refresh (HISTORY 4,796 rows); STATUS/NEXUS/SCRATCH rewrites; KB +4 (009/011 superseded); VX refreshed + Fed-hike row.
2. **Trajectory check** reframed the Fed −14 as overshoot-cooling not reversal (baseline was near peak) → auto-memory `finding_delta_vs_own_prior_local_extreme`.
3. **Roll-watch:** +6 Polymarket July/EOY replacements (Iran deal-components, WTI-July ladder, Hormuz-Jul15, banks-fail-EOY).
4. **Movers-discovery** (Will-asked) → surfaced **Iran-targets-shipping** (added to watchlist; STATUS/NEXUS/KB-018 corrected to two-axis; VX-ORC-04 re-armed 🟠) and **Venezuela 99%** (news-checked = earthquake relief, NOT oil — not added).
5. **Kalshi WIRED** — `scripts/kalshi.py` (trade-api v2, RSA-PSS, read-only) + `kalshi_watchlist.tsv` (8 mkts) + `workbook/KALSHI_ODDS_LOG.tsv`. Creds in `~/.config/kalshi/` (outside repo). Corroboration: recession 10 vs 11, July-hike 18 vs 18. KB-ORC-019. CLAUDE.md/MAINTENANCE updated.
6. **`movers` command** built into `polymarket.py` (domain filter, sports/election exclusion, ⚙ near-resolve flag) + tightened (slug-checking; weather/esports/MMA excluded; ~80→45 hits on `--all`).
7. **Git-protocol fleet-alignment** (Will-directed): step 14 aligned to canonical (BOND-pattern [[refs]], push-train, commit examples, OpenClaw-cut note). Confirmed no `git reset HEAD`, no git footer, no OpenClaw/VPS deps. PROME's lazy-sweep explicitly skipped ORACLE as self-swept.
8. Auto-memory `finding_verify_live_api_schema_over_docs` (this closeout).

## NEXT SESSION (priority order)
1. **🟡 RED** — still owed a current GDP/NBER-comparable fleet recession number (carried since 6/13). Divergence math depends on it.
2. **Roll-watch / drop resolved (post 6/30-7/1):** comment out resolved June rows — Polymarket (Iran-Jun30, bank-failure-Jun30, named-bank-Jun30, Hormuz-Jun30, WTI-$100-Jun) + Kalshi (June CPI 7/14, June U3 7/2). Replacements tracking. Re-search a July single-binary bank-failure market (none existed 6/27).
3. **🟢 Kalshi gap-fill prize:** re-check **CRE default (KXCREDEFMAX), credit-card delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY)** for newly-opened events to pin — the structural-credit-axis tells Polymarket lacks. No open event 6/27.
4. **Fed dovish-tell:** no-cuts breaks <70% = the real dovish turn (vs current overshoot-cooling). Hike re-break >66% = hawkish re-arm. → LIQUID/HENRY.
5. **Iran shipping axis** (energy red-team HAWK+RED): watch WTI-$100-July (supply-shock confirm) + Hormuz transit. Crowd prices continued attacks 80%+.
6. **Kalshi:** no VIX market (gap persists). **movers:** run as the standing discovery sweep each session.

## CARRY-FORWARD
- **Push state:** this closeout committed + safe-pushed (push-train sweeps 4 pending other-agent commits — PROME fleet-audit + WALTER batch — plus mine). Should land `ahead=0`.
- **Watchlists:** Polymarket ~40 (+iran-shipping); Kalshi 8 (corroboration set). Kalshi creds `~/.config/kalshi/{key_id.txt,private_key.pem}` (chmod 600, NEVER in repo).
- **Tooling:** `polymarket.py` = search/market/event/pull/history/**movers**; `kalshi.py` = status/search/market/event/series/pull. Both fetchers run at every EXECUTE.
- **Stale-date markets** (China-GDP, unemployment ladder) shown ⏮ not RESOLVED — don't roll on the bogus endDate.

## OPEN HYPOTHESES
- **The dovish turn hasn't started** — Fed move is overshoot-correction (no-cuts still 80%). Watch no-cuts <70%, not the noisier hike-2026 series.
- **Residual edge = dormant structural credit axis** re-igniting before the crowd prices it. The Kalshi CRE-default / CC-delinquency markets (when they open) are the cleanest forward read on this — Polymarket can't see it.
- **Cross-platform divergence** is now a live tool: Polymarket vs Kalshi on the same event. Today they agree (calm); a future split is itself signal.
- **Risk-on may be over-extended** (S&P best-asset +21/30d + NEH 83.5%) — lots of complacency to unwind if the structural axis fires.
