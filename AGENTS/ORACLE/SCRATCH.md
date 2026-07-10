# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-07-09 (Thu, ~16:55-21:10 ET) — PROME-spawned catch-up/diagnostics refresh after a 7-day gap (last session 7/2; own inbox was empty across the gap — no domain-agent backlog to drain). Live pull both platforms → roll-watch (2 resolved pins repinned, 2 new adds) → divergence check vs fleet marks (HAWK ladder, BRENT sustain) named by PROME's spawn prompt → STATUS/NEXUS_BRIEF/KB refresh + dedicated divergence file.
**Session arc (cont'd):** 2026-07-09 ~21:30-22:00 ET — second PROME spawn same evening, Will-directed Tier-3 open-threads build (own `OPEN_THREADS_2026-07-09.md` #2 coverage gaps + #3 disruption-vs-supply spread). Structural-credit sweep both platforms (comprehensive, confirmed named gap) → 2 new bank-failure markets found/pinned → built + ran `tools/disruption_supply_spread.py` (first value logged).
**Last updated:** 2026-07-09 (session-end, second spawn)

## CHANGES SINCE (what moved, 7/2 → 7/9)
- **US-Iran truce COLLAPSED 7/7→7/8** (per PROME digest) — crowd repriced hard on the **disruption axis**, barely at all on the **supply axis**. Hormuz-normal-Dec31 82.5%→**61.5%** (−21/7d); ships-transit ladder every rung fell (60/day −48.5, 80/day −15.8, 100/day −6.9 — crowd expects LESS recovery); US-blockade-on-Iran 30.5%→**48.0%** (+17.5/7d). **YET WTI-$100-war-premium only 1.6%→3.2%** — still near-dead.
- **Iran forward shipping window (6/29 pin) RESOLVED YES across every leg** — organic confirmation Iran did hit shipping again (3 neutral tankers per digest). Repinned to fresh 7/7-created event.
- **Fed-hike-2026 recrossed >50%** (46.5%→**50.5%**, +4.0/7d) — partial reversal of the 7/2 "overshoot rolling over" call. July-hike up cross-platform too (PM 9.7%→14.5%, Kalshi 14%→15%). No-cuts still pinned 78.5% (dovish tell not fired).
- **Risk-on cooled off its series high**: NEH 84%→**79.5%** (−4/7d) — first soft tail-risk tell since the collapse; best-asset-S&P still made a new high (70.5%).
- **Citi Q2 prov swung hard on thin liquidity**: 60%→31.5% (−27.5/7d, only $2.7K liq) — do not mark, re-check before 7/14.
- **DIVERGENCE CHECK (the spawn's core ask):** HAWK ladder D-rung (46%) vs "US blockade on Iran" market (48.0%, $64.7K liq) → **CONVERGES** (KL≈0.001 bits, gap −2pp) — real-money independently confirms HAWK's ladder. BRENT durable-sustain (~0.55, Brent >$75 thru Fri settle) → **no resolution-matched market exists** on either platform; nearest bracket (WTI $80-Jul, 33.0%) tests a materially harder bar — flagged as a coverage gap, not a dislocation. **No material divergence found on either named comparator.**

## WHAT I DID
1. Boot reads: `AGENTS/ORACLE/CLAUDE.md`, `STATUS.md`, `PREDICTION_MARKET_METRICS.md`, PROME's `PROME/packets/2026-07-09_current-events-digest.md`. Confirmed inbox/outbox empty (no backlog).
2. Live pull both platforms (`polymarket.py pull --log` 38→40 rows after repin; `kalshi.py pull --log` 8 rows).
3. Discovery: `movers` sweep (1 hit, Trump-Truth-Social, not domain-relevant); targeted `search` for "Hormuz closure," "Iran war," found the **0-ships-transit-Hormuz** closure-proxy ladder and **US-declares-war-on-Iran** market — both new adds, direct answers to the spawn's "Hormuz closure markets" ask.
4. **Roll-watch executed:** Iran-targets-shipping (6/29 pin) confirmed fully RESOLVED YES via `event` command → repinned to fresh 7/7 event (`...byptptpt-20260707223842830`). Hormuz ships-transit ladder (6/26 pin) investigated — confirmed a **display-quirk false-RESOLVED** (top leg = 40-ships/day settled at 100% w/ drained liq, but the event itself is open; real rungs still live) — documented in watchlist, kept the pin.
5. **2 new watchlist rows added:** Hormuz 0-ships closure proxy (by-Jul14/31), US-declares-war-on-Iran (Dec31).
6. **Divergence math run** per `PREDICTION_MARKET_METRICS.md` §3 (KL formula) for HAWK D-rung vs blockade market; BRENT sustain flagged as not-computable (resolution-criteria mismatch, anti-pattern-avoidance per §10).
7. **STATUS.md full rewrite** (7/2→7/9 delta table, alerts reordered, divergence-vs-fleet table added, dashboard refreshed all 40 rows, convergence matrix updated, maintenance flags).
8. **NEXUS_BRIEF.md refreshed** (header/VIEW/CALIBRATION/cross-domain sends/forward catalysts all updated to 7/9 state; convergence framed explicitly for peers).
9. **KB.tsv +3 rows** (KB-ORC-025 Iran-shipping-repin+ladder-confirm, KB-ORC-026 the divergence-check math, KB-ORC-027 Fed-hike-recross watch item).
10. **New file `DIVERGENCE_2026-07-09.md`** — dedicated divergence write-up (the spawn's explicit deliverable) with full KL math and the coverage-gap finding on BRENT.

### Second spawn (~21:30-22:00 ET) — Tier-3 open-threads build
11. Read `AGENTS/ORACLE/CLAUDE.md`, `OPEN_THREADS_2026-07-09.md`, `PREDICTION_MARKET_METRICS.md` per the spawn brief.
12. **Structural-credit sweep — Kalshi:** confirmed the 7 gap-fill series (KXCREDEFMAX, KXCCDELINQ, KXCCCHGOFF, KXFEDFACILITY, KXBALANCESHEET) all exist via `series --category Economics/Financials`, then ran 14 keyword `search` queries (delinquency, charge-off, commercial real estate, facility, balance sheet, auto-loan, credit rating, bankrupt, credit crunch, SOFR, yield curve, etc.) — **0 open markets** on every query (search scans up to 6 pages/6K open markets per query). Also found KXAUTODELQ, YINVERT, KX10Y2YDATE, KXCREDITRATING, KXBANKRUPTCY, KXCREDITC (SOFR credit-crunch) as additional relevant series, also zero open events.
13. **Structural-credit sweep — Polymarket:** 12 keyword `search` queries, same axes — no dedicated CRE-default/delinquency/charge-off/yield-curve-inversion market found. Only proxies: single-name bank provision-for-credit-losses binaries (already tracked) + named-bank failure/bailout events.
14. **Found + pinned 2 new Polymarket markets** during the "bank failure" search leg: "US bank failure by Jul 31?" (18.0%, fills the exact gap flagged 7/2) and "US bank failure by Dec 31, 2026?" (66.0%, thin) — added to `watchlist.tsv`, pulled live via `polymarket.py pull --log` to log into `ODDS_LOG.tsv`.
15. **Built `tools/disruption_supply_spread.py`** (new dir `tools/`) — computes P(US blockade on Iran) − P(WTI $100 Jul war-premium) from `ODDS_LOG.tsv`, family-prefix slug matching (survives rollover), same-day pairing check with a STALE-PAIRED warning if legs come from different pull days, appends to new `workbook/DISRUPTION_SUPPLY_SPREAD.tsv`. Ran it twice (before/after the fresh pull) — both times **+44.8pp** (48.0-48.5% blockade vs 3.2-3.7% WTI-$100), confirming stability across two pulls ~4hr apart.
16. Full second `polymarket.py pull --log` (42 rows, +2 for the new bank markets) + `kalshi.py pull --log` (8 rows, unchanged watchlist) to refresh everything before closing.
17. **KB.tsv +5 rows** (KB-ORC-028/029 the coverage-gap finding both platforms, KB-ORC-030/031 the two new bank markets, KB-ORC-032 the spread launch).
18. STATUS.md updated in place (new alerts block for tonight's 3 items, dashboard rows for the 2 new markets, maintenance flags updated from "still pending" to "comprehensively re-checked, confirmed gap").

## NEXT SESSION (priority order)
1. **🟡 RED** — still owed current fleet recession probability (GDP/NBER-comparable), carried since 6/13. Not urgent (crowd & fleet both calm).
2. **🟠 Watch the WTI-$100-July / Hormuz-closure-proxy tripwire** — if either breaks (WTI-$100 >10% or closure-proxy >30%), that's the harassment→supply-shock regime flip HAWK/BRENT need to know immediately, not at next scheduled pull.
3. **🟡 Re-check two thin/moderate-liq single-day swings before treating as real:** Citi Q2 prov (Δ7d −27.5 on $2.7K liq) and WTI $80-Jul (Δ1d −24.5 on $20.8K liq).
4. **🟢 If a Brent-denominated or lower-threshold WTI market opens**, pin it immediately — it becomes the clean BRENT-sustain cross-check that doesn't currently exist.
5. **🟢 Structural-credit gap-fill prize:** re-check CRE default (KXCREDEFMAX), CC delinquency (KXCCDELINQ), Fed facility (KXFEDFACILITY), + the other 7 series found 7/9 (KXCCCHGOFF, KXBALANCESHEET, KXAUTODELQ, YINVERT, KX10Y2YDATE, KXCREDITRATING, KXBANKRUPTCY) — comprehensively confirmed zero open events on either platform 7/9 ~21:55 ET (KB-ORC-028/029); re-check each session, this is the highest-value gap-fill in ORACLE's coverage.
5b. **🟡 Disruption-vs-supply spread — run every session** after `polymarket.py pull --log`: `python3 tools/disruption_supply_spread.py`. Watch for the spread COLLAPSING (blockade cooling or WTI-$100 rising) — that's HAWK/BRENT's regime-flip tripwire.
5c. **🟡 US bank failure by Jul 31 (18.0%, thin $7.0K liq)** — 3-day re-check before trusting a trend; and flag the Dec-31 binary's 66% vs the EOY named-bank event's ~2.6% top leg to REGINALD if it persists past next pull (likely just scope difference, not yet confirmed).
6. **Fed dovish-tell:** no-cuts <70% (dovish turn) OR hike-2026 >66% (re-arm) → LIQUID/HENRY.
7. **Near-dated resolutions (7/14-15):** Citi/BAC provisions + June CPI. **Jul 29:** Fed + BOJ. **Jul 31:** Iran shipping/blockade/closure legs.
8. **BTC-dip $40K repin** still pending (low priority, BTC strong) — carried multiple sessions now, consider dropping from NEXT SESSION if not addressed by 7/16.

## CARRY-FORWARD
- **Push state:** NOT pushed this session per spawn instructions (commit-local only, no push, both spawns). Commit hashes: *(see this session's git log after commit)*.
- **Watchlists:** Polymarket ~38 live rows (post second spawn: +2 new bank-failure markets); Kalshi 8 unchanged (no gap-fill events open yet). Kalshi creds confirmed present, unchanged since 7/2.
- **Files this session (first spawn):** `STATUS.md` (rewrite), `NEXUS_BRIEF.md` (refresh), `watchlist.tsv` (roll-watch + 2 adds), `workbook/ODDS_LOG.tsv` (+40 rows), `workbook/KALSHI_ODDS_LOG.tsv` (+8 rows), `workbook/KB.tsv` (+3 rows), `DIVERGENCE_2026-07-09.md` (new).
- **Files this session (second spawn):** `tools/disruption_supply_spread.py` (new), `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (new, 2 rows), `watchlist.tsv` (+2 bank-failure markets), `workbook/ODDS_LOG.tsv` (+2 rows for new markets across 2 pulls), `workbook/KALSHI_ODDS_LOG.tsv` (+8 rows re-pull), `workbook/KB.tsv` (+5 rows KB-ORC-028..032), `STATUS.md` (in-place updates: 3 new alerts, dashboard rows, maintenance flags), `NEXUS_BRIEF.md` (in-place updates: as-of stamp, calibration, cross-domain sends, forward catalysts), `SCRATCH.md` (this file).
- **Did NOT touch:** VX.tsv (no threshold state-changes this session beyond what's already reflected in STATUS alerts — deferred, not skipped for cause), MAINTENANCE.md, TRADE.md, MEMORY.md.

## OPEN HYPOTHESES
- **Disruption ≠ supply shock, and the crowd is drawing that line sharply.** Every Hormuz/shipping market moved hard this week; every oil-supply-premium market barely moved. This is the crowd independently reconstructing the fleet's own two-root (Iran harassment + Russia diesel-export) framing without being told.
- **HAWK's ladder methodology just got an unusually clean real-money audit** (KL≈0.001 bits vs the blockade market, $64.7K real liquidity) — worth citing if anyone questions the ladder's calibration.
- **BRENT's sustain thesis is flying without an independent instrument check** — not a red flag on the thesis itself, but a genuine blind spot in ORACLE's coverage that should close the moment a matching market appears.
- **The Fed-hike recross is the one loose thread against the "everything else unfired" regime** — worth flagging to LIQUID/HENRY even though it's not a scored divergence; could be an early energy-shock→inflation-expectations tell.
