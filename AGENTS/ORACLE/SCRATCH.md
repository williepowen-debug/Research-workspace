# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-08-27 (Thu), single full catch-up boot after **9 dark days (8/19–8/26)**. Will's framing: *"you have been dark for a few days so we will need to update most of our tracking."* Full re-pull both platforms, four watchlist rolls, the overdue coverage sweep, one registered-test deliverable (T6), and two self-found instrument defects.
**Last updated:** 2026-08-27 ~15:0x ET
**Box:** **desktop** (DESKTOP-BC6EF81, PROME-confirmed in-session 8/27). Kalshi **signed** lane LIVE.

## ⚠️ CARRIED FRAMING — do not re-derive from older text

- **T6 (registered, co-owned LIQUID/BOND — LAST GRADEABLE SESSION Fri 2026-08-28):** ORACLE **COMMITTED to both legs** (cadence + gap-marking) ⇒ Kalshi `KXFED-26SEP-T3.75` **stays canonical**. Ledger `workbook/T6_PIN.tsv`, **ZERO marked gaps** — the dark days were recovered as **real exchange data** via Kalshi daily candlesticks, not marked as gaps. **NOT FIRED on either leg:** level 32.0% vs `<25%` (+7.0pp); 5-session leg 0.32 vs 8/20 close 0.29 (NOT BELOW).
- **🔴 THE ADJUDICATION THAT MOVES A GRADED NUMBER:** PROME's day-1 provisional capture `last_price $0.35` (8/21 11:14:58 EDT) is **authentic but is the day's INTRADAY HIGH** — hourly candles: 8/21 opened 0.29, peaked 0.35 in the 11:00–12:00 EDT hour, **closed 0.32**. **Ruled the exchange daily CLOSE pin-canonical** on N5 clause **(i-b)** (Will 8/13). **At an unchanged 0.32 the two candidate references give OPPOSITE leg-2 verdicts on the 8/28 path.** The ruling makes T6 *harder* to fire — disclosed as running against the more eventful outcome.
- **⚠️ DAY-ALIGNMENT, the thing that could silently corrupt every T6 number:** Kalshi stamps a candle with the **END** of its period, so the candle labelled `8/28T00:00` is the **8/27 session** ⇒ `trading_day = date(end_period_ts) − 1d`. **Verified against two independent anchors before publishing:** 8/18 close 0.30 reproduces ORACLE's own live 8/18 pin (30.0%), and 8/27 close 0.32 reproduces today's live pull **with OI matching exactly (230,891)**. **Re-verify if `t6_pin.py` is ever re-pointed at another market — do not assume the shift.**
- **Today's 8/27 pin row is itself PROVISIONAL** (captured 14:41 EDT mid-session) under the same clause (i-b) applied to PROME's. It settles tonight. **Whoever grades 8/28 must re-read 8/27 as a close, not adopt that cell.**
- **Kalshi publishes per-market daily candlesticks** — `/series/{S}/markets/{T}/candlesticks?period_interval=1440`, fields are `*_dollars`. **This is the general capability that made a zero-gap ledger possible after 9 dark days, and it is not wired into `kalshi.py`** (no `history` subcommand). Generalizing it is the single highest-value tooling item on the queue.
- **`tools/disruption_supply_spread.py` REGIME bumped `v3-aug` → `v4-sep`.** Spread reads **+45.0pp**, down from +66.7 — **that step is the August→September WTI leg swap (0.8% w/ 5 days left → 22.5% w/ a full month), NOT supply fear catching up. NEVER chart v4 against v3.** ⚠️ The new Sept leg is **THIN at inception** ($1.2K vol vs August's $706.5K) — the supply leg is now single-print-unreliable.

## WHAT I DID

Commits: `82c3af234` (T6 packet + `tools/t6_pin.py` + `workbook/T6_PIN.tsv`, delivered to BOND/LIQUID/PROME inboxes) + this closeout's commits.

1. **Full re-pull both platforms** — Polymarket 43 rows, Kalshi 14 rows, both `pull --log`. Ran `disruption_supply_spread.py` (required every session).
2. **T6 deliverable** — built `tools/t6_pin.py` (regenerable, self-gap-marking), filed `workbook/T6_PIN.tsv`, adjudicated the close-vs-intraday reference, packeted + doorbelled all three live recipients (BOND, LIQUID, PROME all live).
3. **Four watchlist rolls** — July→**August CPI** (headline annual; deliberately **not** the Core ladder — that would be a silent basis change), Aug→**Sept WTI-$100** (+ REGIME bump), Hormuz weekly →wk-of-8/24, bank-failure binary → relisted `-20260824` slug (clears the ⛔PINNED-BUT-NOT-FOUND).
4. **🟠 Found + fixed a six-session silent-stale defect in my own tool** — the spread's closure context column logged a **settled July-31 rung at 100%** from 8/09 through today (last honest value 10.50 on 8/02). The `RESOLVED_PROB` guard **existed and was correct — it had never been wired to that column.** Now suppressed-and-marked. → KB-ORC-071
5. **Diagnosed the false `⛔RESOLVED` alarm** on the 0-ships market (same top-leg-of-a-ladder root cause). **The event is live** — acting on the warning would have retired a live instrument. Watchlist row annotated DO-NOT-REPLACE.
6. **Coverage sweep run** (20d overdue) — 9 hits, **no new macro themes**; clock reset.
7. **Hormuz normalization term structure** surfaced: by-Sep-15 **1.4%** / Oct-31 13.5% / Nov-30 22.0% / Dec-31 32.5% — ORACLE pins only the far leg. → KB-ORC-072
8. **STATUS.md rewritten 301 → 110 lines** (the >250 flag carried since 8/18 is cleared). KB-ORC-070/071/072; VX-ORC-07/08 updated, **VX-ORC-10 added** (T6 pin state).

## NEXT SESSION (dated, priority-flagged)

1. **🔴 2026-08-28 IS T6's LAST GRADEABLE SESSION.** Run `python3 tools/t6_pin.py --write`, pin 8/28, and **re-read 8/27 as a settled close** (today's row is provisional). If ORACLE is dark, **any desk can run it** — PROME has this on its 8/28 cluster line.
2. **🟠 Kalshi watchlist carries 9 `[finalized]` dead rows** (July CPI ×3, July U3 ×2, Fed-July ×2, Brent-Jul, Iran-crude) pulling as dead weight every session — **roll to August/September events or freeze.** This is the Kalshi half of the roll that only got done on Polymarket today.
3. **🟠 Generalize the candlestick backfill into `kalshi.py`** as a `history` subcommand. Today proved a dark desk can reconstruct a *gapless* daily record; that capability should not live only inside `t6_pin.py`. Would also retire the "record lane state per-box" fragility for any future pin ask.
4. **🟡 Nominate the near-dated Hormuz normalization legs** (by-Sep-15, by-Oct-31) for pinning — confirm with HAWK/BRENT/FALCON first per the coverage-sweep rule; do not pin unilaterally.
5. **🟠 The RE-OPENABLE CLASS (carried from 8/18, untriaged):** past conclusions that treated a `kalshi.py search` zero as verified absence, *only where the zero was load-bearing*. Named candidates in `CLAUDE.md` § DATA COLLECTION (VIX/vol gap, credit-stress gap-fills).
6. **🟠 PROME's 8/17 PortWatch war-regime completeness ask** — sweep KB rows for war-regime PortWatch Hormuz counts used as evidence; tag or clear. **Carried four sessions now.**
7. **🟡 NEXUS + RED still owe the 71.5%→aggregate relabel** (packeted 8/18; not mine to close, tracking only).
8. **🟡 RED still owed a current fleet recession number** (carried since 6/13; crowd calm at PM 8.5% / Kalshi 7.0%).
9. **⚪ Past-dated Iran-shipping legs unresolved** (8/17 52.4%, 8/24 37.5%, 8/25 32.0%) — awaiting resolution, not live probabilities. Re-check whether they ever settle; if they don't, the daily-cadence event's resolution reliability is itself a finding.
10. **⚪ Minor tool note:** sports slugs (`lal-bar-bil-*`) leaked past `coverage`'s ex-sports filter.

## CARRY-FORWARD

- **Push state:** see the closeout commits below; `safe-push.sh` run at closeout — confirm the literal `Pushed.` line, and note a rebase would rewrite unpushed hashes (verify by subject if one goes missing).
- **Coverage sweep:** run 2026-08-27, **next due ~2026-09-03**.
- **VIOLET had staged/uncommitted work in the shared index at boot** (in-flight, another live session). **Origin was 0-behind/0-ahead so no pull was needed** — the "before pulling" hazard never arose. My path-scoped commit correctly left VIOLET's staged renames untouched; `git diff --cached --stat` showed them (it reads the whole shared index) while `git show --stat` confirmed my commit held only my 6 files. **Do not read a fat `--cached` stat as a leak — verify with `git show`.**
- **Kalshi lane LIVE and SIGNED on the desktop.** Record lane state **PER-BOX**, never as a fleet fact.
- `kalshi.py search` costs ~8-11s per call (52 round-trips).

## OPEN HYPOTHESES

- **The Sept-hike series bottomed at 0.25 on 8/14–8/16 and has ground back +7pp.** Whether that is genuine hawkish re-rating or mean-reversion after the 8/13–8/14 overshoot is unresolved — the 8/12 entry called the de-rating "extended" and it did not continue, which is recorded, not quietly replaced.
- **Why do several past-dated Iran-shipping legs sit unresolved for 10+ days** while others settle same-day? If it is systematic, the daily-cadence tempo gauge is less reliable than its volume suggests.
- **Does the crowd's 1.4% by-Sep-15 Hormuz normalization survive contact with the physical throughput data?** ORACLE owns the crowd read only; BRENT/FALCON own whether the tape agrees.
