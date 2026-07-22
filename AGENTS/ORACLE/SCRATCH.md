# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-07-22 (Wed ~11:41 ET) — Will-directed boot. Live pull both platforms + derived spread → **the regime-flip tripwire pre-registered 7/17 TRIPPED (the signal way)**: disruption-supply spread collapsed +40.5→+30.8pp entirely via the WTI supply leg rising; WTI-$100 crossed the >15% supply-loss threshold. Fed re-armed hawkish in parallel. Full STATUS/NEXUS_BRIEF/KB rewrite + 2 🔴 outbox routes. **Push DEFERRED** (foreign uncommitted DAEDALUS/FALCON changes in tree — did not pull).
**Last updated:** 2026-07-22 (session-end)

## CHANGES SINCE (what moved, 7/17 → 7/22)
- **🔴 REGIME-FLIP TRIPWIRE TRIPPED.** Disruption-supply spread **+40.5pp → +30.8pp** — collapsed *entirely via the SUPPLY leg*: WTI-$100-war-premium **7.5%→17.8%** (Δ1d +9.2, Δ7d +11.4, deep $672K vol), crossing the pre-set >15% "crowd flips to supply-loss pricing" line. Disruption leg dead flat (Hormuz-normal 51.5% both dates = 48.5% disr). Crowd pricing lost barrels, not just premium (KB-ORC-042).
- **⚠️ BUT no barrel actually lost:** Kalshi Iran-crude-prod Jul >2.0mbpd still **77%** (sanctioned baseline, uncollapsed); Hormuz-closure proxy FELL to 5.7%. Crowd pricing supply RISK ahead of realized LOSS. Corroborators: WTI-$90-intraday 65.6% (+45.8/7d), Brent settle-ref 73% (+6), gold hit $4,150.
- **🔴 Fed re-armed hawkish:** July-meeting-hike **3.6%→21.1%** (Δ1d +9.5, Δ7d +16.8; Kalshi hike-by-July 24%, +12) — meeting 7/29. Fed-HIKE-2026 **51.5%→64.5%** (+14/7d) — **~1.5pp under the >66% re-arm trigger.** No-cuts firmed 84.8%; July-CPI-modal top +16/7d (KB-ORC-043).
- **🟠 Complacency crack deepened:** NEH 72.5%→**66.5%** (−12/7d). Bimodal Iran: US-invade 28.5% (+11) AND US-Iran-deal 34.5% (+11.5) BOTH rose (KB-ORC-044).
- **War tempo mixed:** Iran shipping-attack daily leg just 1.0% on 7/21 (eased that day). Russia advancing hard (Vasylivka 73.5%, +61/1d — OSPREY's, context).

## WHAT I DID
1. Boot reads: `CLAUDE.md`, `SCRATCH.md`, `STATUS.md`, `NEXUS_BRIEF.md`, KB tail. **Did NOT git pull** — foreign uncommitted changes in DAEDALUS + FALCON dirs (protect their work per root protocol).
2. Inbox clean (empty except .gitkeep; WALTER subfolder empty). No signals to process.
3. Live pull both platforms (`polymarket.py pull --log` 36 rows, `kalshi.py pull --log` 12 rows) + `disruption_supply_spread.py` (+30.8pp) + `movers --top 20` discovery sweep.
4. Read the two fired tripwires together → coherent regime-shift story (supply-loss + Fed-hike pricing stepping up together, no realized barrel loss yet).
5. **KB.tsv +3 rows** (KB-ORC-042 regime-flip-tripwire, -043 Fed-rearm, -044 complacency-crack-deepened) — via Python append (%-in-text printf-corruption guard).
6. **STATUS.md full rewrite** (7/22 state, regime-flip + Fed-rearm alerts to top, dashboard all rows, convergence matrix, maintenance).
7. **NEXUS_BRIEF.md full rewrite** (supersedes 7/17; VIEW/CALIBRATION/cross-domain/catalysts all to 7/22).
8. **Outbox:** 🔴 `2026-07-22_to-hawk-brent-falcon_regime-flip-tripwire-tripped.md` + 🔴 `2026-07-22_to-liquid-henry_fed-rearmed-hawkish.md`.

## NEXT SESSION (priority order)
1. **⚠️ WTI $100 supply-leg MONTH-ROLL — DUE ~Aug 1 (9 days).** The July WTI-$100 market ends 2026-08-01. When August opens, **re-pin the new month's WTI-$100 market** in `watchlist.tsv` or the spread's supply leg silently ages out (script hard-exits if legs drift >3d — fails loud, but the re-pin is manual). Same for WTI-$85/$90-intraday and the Jul-31 Hormuz ladder (re-pin an Aug ladder).
2. **🔴 Regime-flip watch — the barrel-level tell:** **Kalshi Iran-crude-production <2.0mbpd** (currently 77% >2.0 = uncollapsed) converts supply-RISK pricing into realized LOSS → immediate HAWK/BRENT/FALCON. Also **WTI-$100 >25%** (deepens regime) OR spread narrowing further via the WTI leg OR Hormuz-closure >30%.
3. **🔴 Fed re-arm — 1.5pp from firing:** Fed-HIKE-2026 **>66%** (currently 64.5%) fires the re-arm → LIQUID/HENRY. July FOMC **7/29** — a hike surprises vs a 21% priced tail.
4. **Roll-watch near-dated:** Fed July mtg + BOJ (7/29, both hold-lean); Iran July legs + Hormuz ladder + Brent settle-ref (7/31); July CPI (8/12, modal top firmed 43.5%).
5. **⚠️ VERIFY: Kalshi US-credit-downgrade reads 4.0% today vs 16% on 7/17** — likely a different market line/ticker got pulled. Verify the specific ticker before treating as a −12pp move.
6. **🟡 Re-run authoritative Kalshi `/events?status=open` sweep** — pin CRE-default/CC-delinquency/Fed-facility the moment any opens (still zero-open; use the authoritative sweep, NOT `search`, KB-ORC-041).
7. **🟡 RED** — still owed current fleet recession probability (GDP/NBER-comparable), carried since 6/13. Not urgent (crowd & fleet both ~11-13%, agree calm).
8. **Daily events display-quirk:** Iran-shipping + Iran-Gulf daily events + Hormuz ladder trip false ⛔RESOLVED (fetcher top-leg = old settled date). Events LIVE — read recent legs via `event`, do NOT re-pin on the flag.

## CARRY-FORWARD
- **Push state: DEFERRED.** Committed local this session; did NOT push and did NOT pull — foreign uncommitted changes in DAEDALUS + FALCON dirs at session start (protecting their work per root "Before pulling"). Push next clean session or when Will clears the tree. Unpushed hashes: *(see git log after commit)*.
- **Watchlists:** Polymarket ~36 live rows (unchanged from 7/17 net; some daily events show ⛔ false-resolved — LIVE, don't re-pin); Kalshi 12 unchanged. Kalshi creds present, unchanged.
- **Files this session:** `workbook/KB.tsv` (+3, KB-ORC-042..044), `STATUS.md` (rewrite), `NEXUS_BRIEF.md` (rewrite), `workbook/ODDS_LOG.tsv` (+36), `workbook/KALSHI_ODDS_LOG.tsv` (+12), `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (+1 row, +30.8pp), `outbox/` (+2 new), `SCRATCH.md` (this).
- **Did NOT touch:** VX.tsv (no clean threshold state-change beyond STATUS alerts — WTI-$100 >15% and hike-2026-near-66% are candidates; deferred, log next session if they hold), MAINTENANCE.md (no structural change this session — pure data), TRADE.md, MEMORY.md, HISTORY.tsv (trajectory didn't need a rewrite; consider `history --write` next session given the WTI move).

## OPEN HYPOTHESES
- **The regime flip is starting but not confirmed.** The clean separation — supply-RISK pricing (WTI-$100 17.8%) rising while physical supply (Iran crude prod 77% >2.0mbpd) stays flat — is the textbook leading-indicator setup. If Iran production drops below 2.0mbpd, risk becomes realized and the whole complex re-rates. If it holds, the WTI-$100 premium is the thing that unwinds. The gap between those two numbers is the single cleanest trade-relevant divergence on the board right now.
- **Fed and oil are now one story.** The hawkish re-arm (hike-2026 +14/7d) is tracking the energy premium, not the labor/growth data (recession flat at 11.5%). If the oil premium unwinds, the Fed tail should deflate with it — they're coupled. Worth watching whether they de-couple (Fed staying hawkish on a different driver = a new signal).
- **Bimodal Iran path (invade AND deal both +11/7d) = the crowd has given up on muddle-through.** Either tail resolving is a big move; the middle is thinning. NEH −12/7d is the sentiment confirmation.
- **VX.tsv threshold logging owed:** WTI-$100 crossed >15% and hike-2026 approaching >66% are both clean threshold state-changes that should get VX rows next session if they hold (deferred this session to prioritize STATUS/NEXUS/routing).
