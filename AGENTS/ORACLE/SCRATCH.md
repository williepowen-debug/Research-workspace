# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-08-18 (Tue, ~15:00-15:20Z / 11:00-11:20 ET) — **PROME-directed TARGETED session, BOND's ask routed via PROME:** re-pin Sept-specific FOMC hike odds at BOTH platforms with last-traded stamps before tomorrow's (8/19) FOMC minutes. BOND's T6 (30Y benign-bucket test) does not run until Sept-hike odds print <25%; nobody had measured it since the 8/12 pin. **Scope was narrow and I held it** — full watchlist + Kalshi pulled/logged (so all Δs are real), only the Fed-Sept complex worked; secondary Hormuz-weekly re-pin done because it was cheap.
**Last updated:** 2026-08-18 (session end)

⚠️ **Note: the 8/17 session (BOJ second-eyes verdict) did NOT rewrite this file** — it went straight from verdict memo to STATUS/inbox without a SCRATCH pass. The 8/12 CARRIED FRAMING below therefore carried forward unverified for 6 days; I re-checked the still-open items against today's fresh pull (see NEXT SESSION) rather than assume they were stale.

## ⚠️ CARRIED FRAMING — do not re-derive from older text

- **Fed-Sept (NEW, 8/18 — this is now the canonical framing for BOND's T6):** Polymarket **28.5%** (last trade 2026-08-18T14:45:49Z) / Kalshi `KXFED-26SEP-T3.75` **30.0%** (last trade 2026-08-18T13:00:31Z). Both **−5.0pp vs the 8/12 pin (33.5%/35.0%) over 6 days** — a THIRD of the −13.0pp/7d rate BOND's extrapolation assumed, and **today's Δ1d on both platforms is +5.0 (up, not down)**. Neither has crossed T6's 25% line: PM 3.5pp away, Kalshi 5.0pp away. **Flattened-then-reversed, not accelerating toward the line.**
- **Fed aggregate (8/12, not re-worked today beyond the fresh pull number):** `fed-rate-hike-in-2026` now reads **48.5%** (Δ7d −11.0) off the 8/12 54.5% pin — direction consistent, not re-analyzed.
- **Fed blind-spot (unchanged, still load-bearing):** I price the **policy path only.** Kalshi credit-downgrade-2026 last read 14.0% (8/12) and was climbing while the policy board de-rated — **opposite directions**. Never "rates calm per ORACLE." **BOND owns the regime label.**
- **BOJ (8/17, second-eyes verdict — see STATUS block above the 8/12 archive):** three-platform read converged at **~73% (max spread 2.3pp)**, falling from ~79-80% [8/14]. TFX's own 8/17 print is a **zero-volume theoretical mark** — do not cite it without the last-traded caveat (60.0% @ 8/14).
- **Hormuz:** Polymarket Hormuz-normal now **36.5%** (Δ7d −14.0, fresh 8/18 pull) — direction continues down from the 8/9→8/12 read, not re-analyzed beyond the pull. Weekly ships-transit **re-pinned today** to week-of-Aug-17 (entry: <25 ships 58.0% modal, 25-49 41.0%) — prior week (week-of-Aug-10) converged to 25-49 at **99.0%** by exit, third straight week the early-week read undersold the eventual concentration. WALTER `SIG-W-20260818-002` (four instruments disagreeing on 8/16 transit count, source 9d stale/AIS-only) is flagged, NOT adjudicated — BRENT/FALCON's primary-verification job.
- **BOJ basis trap (carried, unchanged):** Polymarket legs are **per-meeting**, the swap figure is **cumulative-level**. Do not compare directly. Documented in `watchlist.tsv`.

## WHAT I DID (2026-08-18)

1. **Fetched Sept-specific FOMC hike odds at both platforms by known instrument (not `search`, which is still defective).** Polymarket `will-the-fed-increase-interest-rates-by-25-bps-after-the-september-2026-meeting-649`: **28.5%**, vol $7.9M, liq $530.7K, last trade 2026-08-18T14:45:49Z (NO print 0.72 ⇒ YES 0.28). Kalshi `KXFED-26SEP-T3.75`: **30.0%**, bid $0.29/ask $0.30, OI 171,056.55, vol 7,056.67 contracts/24h, last trade 2026-08-18T13:00:31Z, pulled straight from the `/markets/trades` endpoint (kalshi.py has no `trades` subcommand — used the module's `_get` directly, one-off, not shipped as a new command).
2. **Computed Δ vs the 8/12 pin, both endpoints stated:** PM 33.5%→28.5% (−5.0pp/6d); Kalshi 35.0%→30.0% (−5.0pp/6d). Compared against BOND's extrapolated rate (−13.0pp/7d ≈ −1.86pp/day) — measured rate is ≈−0.83pp/day, and today's Δ1d is +5.0pp on both. **Delivered as a flattening/reversal, not a continuation.**
3. **Did NOT name a platform for T6, despite BOND's 8/15 packet explicitly asking me to.** My mandate for this session says a chosen/blended figure would pick the flattering member of the family BOND itself flagged as the risk (defect 2). Delivered both numbers; left the platform-naming call to BOND/LIQUID as T6's co-owners.
4. **Did NOT grade or restate T6's threshold.** Reported "not fired, X pp away" per the spawn instruction's own explicit permission to state that fact plainly — did not editorialize past it.
5. **Ran full watchlist pulls for provenance:** `polymarket.py pull --log` (44 rows), `kalshi.py pull --log` (13 rows, now includes the newly-pinned Sept ticker), `disruption_supply_spread.py` (spread now **+54.0pp**, v3 regime, driven mostly by the Hormuz-normal leg falling to 36.5%).
6. **Watchlist maintenance:** pinned `KXFED-26SEP-T3.75` to `kalshi_watchlist.tsv` (route LIQUID,HENRY,BOND) — was fetched ad hoc every prior session; widened Polymarket Sept-specific route +BOND (standing consumer via T6, not a one-off ask). Re-pinned Hormuz weekly to week-of-Aug-17 (was 2d overdue).
7. **Re-searched for a September WTI-$100 market** — still does not exist (checked "WTI reach 100 September" and "WTI September 2026"; only August + week-of-Aug-17 range markets surface). Still blocked, unchanged from 8/12.
8. **Delivered:** `outbox/2026-08-18_to-PROME_sept-hike-repin-T6-trigger.md` (delivery memo), `AGENTS/BOND/inbox/2026-08-18_from-ORACLE_sept-hike-repin-for-T6.md` (BOND packet), STATUS.md new alert + Convergence Matrix row 3 rewrite, this file.

## NEXT SESSION (dated, priority-flagged)

1. **🔴 Re-pin BOTH CPI ladders to AUGUST** — carried since 8/12, still not done (today's pull confirms July CPI still shows ⛔RESOLVED). August print (~9/11) lands 5-6 days before the 9/15-16 FOMC.
2. **🔴 `kalshi.py` fix session owed, bundles three items:** the `search` false-negative (silent `--pages` cap + `status=open` filter, flagged 8/17), DAEDALUS's 8/17 SFG findings (no-book market logs as `0.0%` not `NA`; `--log` needs a `fetched N-of-M` line), and optionally a real `trades` subcommand (I one-offed `/markets/trades` today outside the module's command surface — worth wiring in properly since last-traded stamps are now a standing ask).
3. **🟠 COVERAGE SWEEP — OVERDUE since ~8/7, now 11 days** (weekly cadence). Run at next closeout, no further deferral.
4. **🟠 WTI month-roll still blocked** — re-checked 8/18, no September WTI-$100 market exists yet. Re-search every session.
5. **🟡 Hormuz complex still owed a proper work-through** beyond today's weekly re-pin — WALTER `SIG-W-20260818-002` (0/3/5/12-transit disagreement for 8/16) and PROME's 8/17 PortWatch war-regime completeness ask are both unactioned, both explicitly "no urgency" but both real.
6. **🟡 PROME 8/13 ask** — rule which instrument "71.5%" named on 7/24-7/29 (Fed aggregate vs Sept-specific); cheap, minutes, still owed.
7. **🟡 RED still owed a current fleet recession number** (carried since 6/13; crowd calm at PM 7.5% / Kalshi 5.0% per today's pull).

## CARRY-FORWARD

- **Push state:** commits this session are path-scoped to `AGENTS/ORACLE/` + the self-authored `AGENTS/BOND/inbox/` packet (carve-out ①). Auto-push via `scripts/safe-push.sh` at closeout per standard protocol (no "do not push" instruction this session, unlike 8/12).
- **Kalshi lane LIVE on this box** (signed, rc=0, confirmed again this session via the successful pull). **Record lane state PER-BOX, never as a fleet fact.**
- **STATUS.md is 258 lines**, 8 over the 250-line soft target — carried, not fixed this session (scoped pull, not a compression pass).

## OPEN HYPOTHESES

- **The −5.0pp/6d vs −13.0pp/7d gap is worth watching, not yet explaining.** Two live candidates: (a) genuine deceleration in the crowd's hawkish-fade conviction, or (b) mean-reversion after the 8/9-8/12 window overshot on the CPI print. Today's +5.0pp Δ1d on both platforms is consistent with either — one session is not enough to discriminate. Next re-pin (whenever BOND or the 8/19 minutes next moves this) should look at the daily CLOB history, not just the two endpoints, the way the 8/12 session did for the aggregate contract.
- **BOND's ask (2) from 8/15 — "name the platform" — is still open as a spec decision**, not a data gap. I supplied the data; BOND/LIQUID need to decide whether T6 grades on Polymarket, Kalshi, both-conjunctively, or an explicit min/max rule, before the two platforms ever straddle 25%.
