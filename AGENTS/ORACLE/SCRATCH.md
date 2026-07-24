# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-07-24 (Fri, ~12:01 ET) — routine Friday boot + full closeout. Both live triggers from 7/22 EXTENDED (didn't retrace): Fed-hike-2026 blew through the >66% line to 71.5%, and the regime-flip spread narrowed a second time via the WTI leg to +25.6pp — barrel-tell still flat. Two 🔴 follow-up routes sent.
**Last updated:** 2026-07-24 (session-end, full closeout)

## CHANGES SINCE (what moved, 7/22 → 7/24)
- **🔴 FED RE-ARM EXTENDED.** Fed-HIKE-2026 **66.5% → 71.5%** (Δ1d +1.0, Δ7d +20.0, $4.6M deep) — the >66% re-break trigger fired 7/22 and has now blown decisively through; a 2026 hike is the crowd's firm base case (>2/3), no longer marginal. July-meeting-hike 22.2%→**23.2%** (Δ7d +19.4, $18.2M; Kalshi hike-by-July 22%, Δp −4 — eased slightly, still corroborates). 7/29 FOMC in 5d. No-cuts 85.0%, 1-cut fading 9.5%. (KB-ORC-049.)
- **🔴 REGIME-FLIP DEEPENING.** Disruption-supply spread **+30.8pp → +25.6pp** — narrowed AGAIN entirely via the WTI supply leg. WTI-$100-war-premium **14.9% → 22.9%** (Δ7d +15.2), now decisively through >15% and approaching the >25% deepen-trigger. ⚠️ Spiked ~44% intraday then retraced (Δ1d −21.8); liq thinning $39.5K→$27.7K — read the 7d-trend, not the print. Disruption leg flat (Hormuz-normal 51.5%). **CRITICAL: Kalshi Iran crude prod Jul >2.0mbpd STILL 77% (unch)** — barrel-tell has not moved; supply-RISK pricing rising against flat physical supply, gap widening. Kalshi Brent settle-ref eased 73% (Δp −10). (KB-ORC-050.)
- **🔴 WAR-WIDENING TEMPO SHARPLY UP (found on Will's "all updated?" check — corrects the boot read).** Pulled the daily war-tempo events' LIVE legs via `event` (dashboard shows only their stale ⛔RESOLVED settled leg). **Iran-mil-action-vs-Gulf-State: Jul 19 & 20 YES; forward legs ~45-56%/day sustained thru 7/31** (today 47.5%, up Δ7d +13 to +29 across the curve, REAL liq $19-30K/leg). Near-daily coin-flip of Iran action vs a Gulf state for the rest of July = the physical mechanism under the WTI-$100 premium, no barrel lost. Shipping leg ~50% forward but THIN ($41-200) + mixed. (KB-ORC-051.) My boot STATUS/NEXUS "war tempo mixed/quiet" line was WRONG — corrected in-session.
- **🟠 NEW catalyst:** Trump-Netanyahu-meet-July **89.5%** (Δ1d +34.5, Δ7d +45.5, $239K) surfaced by `movers` — meeting priced near-certain within the week. Iran-axis context.
- **🟠 Complacency crack still eroding:** NEH 66.5%→**65.5%** (Δ7d −8.0, three weeks one-way). Bimodal Iran persists: US-invade 29.5% (+7/7d) AND US-Iran-deal 31.0% (+8/7d) both rising.
- **🟠 CLARITY Act** 37%→**33.0%** (Δ7d −1.5, deep $2.6M) — crowd continuing to fade passage before the Aug-10 recess deadline.
- **Quiet/confirmed:** recession PM 10.5% / Kalshi 14.0% (calm); US-credit-downgrade 4.0% Δp 0 (confirms the 7/22 correction — 7/17's "16%" was a bad line-read); corporate-bankruptcy 83%.

## WHAT I DID
1. Boot reads: `CLAUDE.md`, `SCRATCH.md`, `STATUS.md`, `NEXUS_BRIEF.md`, KB/VX tails. Git: clean tree (only untracked DEWEY file, not mine) → `git pull --rebase` (up to date, nothing to pull).
2. Inbox clean (empty except .gitkeep; WALTER subfolder empty). No signals to process.
3. Live pull both platforms (`polymarket.py pull --log` 40 rows, `kalshi.py pull --log` 12 rows) + `disruption_supply_spread.py` (+25.6pp) + `movers --top 18` (surfaced Trump-Netanyahu).
4. **KB.tsv +2 rows** (KB-ORC-049 Fed-rearm-extended, -050 regime-flip-deepening) — via Python append (%-in-text printf-corruption guard).
5. **VX.tsv** — updated VX-ORC-04 (regime deepening, spread +25.6), -05 (NEH 65.5%), -07 (WTI intraday spike-retrace + Fed +20/7d + Bibi), -08 (Fed-hike EXTENDED to 71.5%).
6. **STATUS.md full rewrite** (7/24 state, both extended-trigger alerts to top, dashboard 40 rows, convergence matrix, maintenance).
7. **NEXUS_BRIEF.md full rewrite** (supersedes 7/22; VIEW/CALIBRATION/cross-domain/catalysts all to 7/24).
8. **Outbox:** 🔴 `2026-07-24_to-liquid-henry_fed-rearm-extended.md` + 🔴 `2026-07-24_to-hawk-brent-falcon_regime-deepening-bibi-catalyst.md`.

## NEXT SESSION (priority order)
1. **⚠️ WTI $100 supply-leg MONTH-ROLL — DUE ~Aug 1 (8 days).** July WTI-$100 (`will-wti-reach-100-in-july-2026-928`) ends 2026-08-01. When August opens, **re-pin the new month's WTI-$100 market** in `watchlist.tsv` or the spread's supply leg silently ages out (script hard-exits if legs drift >3d — fails loud, but the re-pin is manual). Same for the Jul-31 Hormuz ladder (re-pin an Aug ladder) + Iran July legs.
2. **🔴 Regime-flip watch — the barrel-level tell:** **Kalshi Iran-crude-production <2.0mbpd** (currently 77% >2.0 = uncollapsed, flat 3 reads) converts supply-RISK pricing into realized LOSS → immediate HAWK/BRENT/FALCON. Also **WTI-$100 >25%** (deepens regime — now only ~2pp away) OR spread narrowing further via the WTI leg OR Hormuz-closure >30% (now 9.9%).
3. **🔴 Fed re-arm — next rung:** trigger fired 7/22 and extended 7/24 to 71.5%. NEXT rung = an actual 2026 hike prints OR the **7/29 FOMC** hikes (23.2% priced Polymarket / 22% Kalshi — still a surprise, but durable). Watch hike-2026 extend (>75%) OR fade back under 66%. → LIQUID/HENRY.
4. **Roll-watch near-dated (all ⏳ within a week):** Fed July FOMC + BOJ (7/29, both hold-lean); Trump-Netanyahu-meet + Iran July legs (enrichment/shipping) + Hormuz ladder + Brent settle-ref (7/31); **CLARITY Act Aug-10 Senate recess deadline** (33%, → BROCK/RED); July CPI (8/12, modal top eased 38.5%).
5. **⛔ Daily-event display quirk — RE-PIN OWED (carried several sessions):** Iran-shipping, Iran-Gulf-state, Hormuz-transit-ladder, Houthi-shipping all trip false ⛔RESOLVED (fetcher top-leg = old settled date). Parent events LIVE — read recent legs via `event`. Re-pin fresh current-week legs at next roll-watch to clear the noise. Do NOT re-pin on the flag alone.
6. **🔭 COVERAGE SWEEP — weekly, NEXT DUE ~7/29** (last run 7/22). Run at closeout if >7d since. Pending un-actioned nominations: Hantavirus-pandemic tail (flagged to fleet, awaiting owner); Kalshi coverage analog (v2 build candidate). v2 build candidates: 30d-drift flag on `movers`, /events tag suppression.
7. **🟡 RED** — still owed current fleet recession probability (GDP/NBER-comparable), carried since 6/13. Not urgent (crowd & fleet both ~10-14%, agree calm).
8. **🟡 Kalshi gap-fills** — CRE-default/CC-delinquency/Fed-facility still zero-open; re-check via authoritative `/events?status=open` sweep, NOT `search` (KB-ORC-041). Pin the moment any opens.

## CARRY-FORWARD
- **Push state: pending this session's commit + safe-push (see below).** Prior session (7/22) confirmed ALL ORACLE COMMITS PUSHED clean. This session's commit is the only unpushed one at closeout.
- **Watchlists:** Polymarket 40 rows pulled (some daily events show ⛔ false-resolved — LIVE, don't re-pin; re-pin owed per NEXT #5). Kalshi 12 unchanged. Kalshi creds present (chmod 600), unchanged.
- **Files this session:** `workbook/KB.tsv` (+2, KB-ORC-049/050), `workbook/VX.tsv` (4 rows updated), `STATUS.md` (rewrite), `NEXUS_BRIEF.md` (rewrite), `workbook/ODDS_LOG.tsv` (+40), `workbook/KALSHI_ODDS_LOG.tsv` (+12), `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (+1 row, +25.6pp), `outbox/` (+2 new), `SCRATCH.md` (this).
- **Did NOT touch:** MAINTENANCE.md (no structural change this session — pure data + routing), TRADE.md, MEMORY.md, HISTORY.tsv (trajectory didn't need a rewrite; consider `history --write` next session if the WTI leg keeps moving into its roll).

## OPEN HYPOTHESES
- **The regime flip is deepening but still not confirmed.** Two consecutive spread-narrowing reads via the WTI leg, WTI-$100 now ~2pp from the >25% deepen-trigger — but Iran crude production (Kalshi, 77%) has been dead flat for three reads. The clean separation (supply-RISK pricing rising, physical supply flat) is the textbook leading-indicator setup, and the gap is *widening*. If Iran production drops <2.0mbpd, risk becomes realized and the whole complex re-rates. If it holds, the WTI-$100 premium is the thing that unwinds. Still the single cleanest trade-relevant divergence on the board.
- **Fed and oil are ONE story, and both accelerated.** hike-2026 +20/7d is tracking the energy premium, not labor/growth (recession flat 10.5%). If the oil premium unwinds, the Fed tail should deflate with it — they're coupled. Watch whether they de-couple (Fed staying hawkish on a different driver = a new signal).
- **Bimodal Iran (invade AND deal both rising) = the crowd has given up on muddle-through.** Either tail resolving is a big move; the middle keeps thinning (NEH −8/7d). The Trump-Netanyahu meeting (89.5%) may be the near-term fork — watch which leg it feeds.
- **WTI-$100 leg thinning ($27.7K liq) into its 8/1 roll — the intraday whipsaws (44%→22.9%) will get worse.** The 7d-trend is the read; don't over-react to the daily. This is also the month-roll deadline forcing function.
