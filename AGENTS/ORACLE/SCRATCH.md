# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-08-27 (Thu), ONE long session in five phases: **(1)** catch-up boot after **9 dark days (8/19–8/26)** → the T6 deliverable; **(2)** Will-directed file sweep; **(3)** TRADE.md rebuilt as a trajectory surface; **(4)** tool-verification pass; **(5)** the remaining sweep items + Tier-1 fixes + closeout.
**Last updated:** 2026-08-27 ~19:5x ET · **Box:** **desktop** (DESKTOP-BC6EF81, PROME-confirmed). Kalshi **signed** lane LIVE.

## ⚠️ CARRIED FRAMING — do not re-derive from older text

- **🔴 TOMORROW (Fri 8/28) IS T6's LAST GRADEABLE SESSION.** Run `python3 tools/t6_pin.py --write`. **Re-read 8/27 as a SETTLED CLOSE** — today's row is `LIVE-INTRADAY` and provisional, and it *moved 32.0 → 31.0 within four hours of my publishing it*. **The 8/28 reference day is 8/21, close 0.32** — unchanged all day and the only number that decides the grade. NOT FIRED on both legs as of 19:4x (level 31.0 vs `<25%`; 5-session 31 vs 8/20's 29). BOND has adopted everything and is closed out; it recorded the **verdict** rather than chasing the value, deliberately.
- **The 8/21 reference is the CLOSE 0.32, never the 0.35 intraday capture** — ruled on N5 clause (i-b). At an unchanged price the two give **opposite leg-2 verdicts**. BOND adopted it despite it making its own branch harder to confirm.
- **⚠️ Kalshi candle `end_period_ts` is the period END** ⇒ `trading_day = date − 1d`. Verified against two anchors before publishing. **Re-verify if `t6_pin.py` is ever re-pointed at another market.**
- **⛔ THREE PUBLISHED σ ARE RETRACTED (KB-ORC-064 → `CORRECTED`).** Every dH and entropy LEVEL reproduces exactly; every σ was inflated and **three of five are unreachable at any rolling window**. Two classifications withdrawn: Hormuz never crossed k=3; US-Iran-deal was not k=5 urgent. **The directional finding stands in full** — it rests on signs and levels. Reproduce: `python3 tools/metrics.py verify`.
- **`kalshi.py` reports the LAST trade.** On a wide book a single lift of the offer becomes the headline. A `⚠mid X` marker now fires at ≥3¢ spread. **Cite the MID on wide books** (KB-ORC-069). Display-only — **the logged series keeps its last-trade basis on purpose**; a mid/last basis switch mid-series would be its own defect.
- **Disruption-supply spread REGIME is now `v4-sep`.** +45.0pp. The step from +66.7 **is the Aug→Sep WTI leg swap, not supply fear. NEVER chart v4 against v3.** New Sept leg is ⚠️thin at inception ($1.2K vs $706.5K).
- **The 0-ships `⛔RESOLVED` dashboard flag is a FALSE POSITIVE — do not retire that market.** By-date ladder; the settled July rung wins the top-leg selection. Live rungs 8/27: by-Aug-31 11.1%, by-Sep-30 26.0%. Watchlist row is annotated DO-NOT-REPLACE; the warning will keep firing every session.

## WHAT I DID

Commits (12 ORACLE, all on origin): `82c3af234` T6 packet + `t6_pin.py` · `ca1d75096` catch-up boot · `9dfef70f7` NEXUS_BRIEF + memory · `0d66d4ab5` hook trim · `9dd0c49b6` weekday fixes · `64771b24f` sweep fixes · `8113fc027` TRADE.md rebuild · `2e8591695` decoupling packet · `87751dcfa` pathspec memory · `700c674ce` TRADE.md review pass · `04461f09e` tool verification · `b5f7a1642` STATUS evening · `9b20d7e96` Tier-1 · `68f4e73aa` MAINTENANCE.

1. **T6 pinned GAPLESS across 9 dark days** — Kalshi publishes per-market daily candlesticks, so dark sessions were recovered as *real exchange data* instead of marked gaps. New `tools/t6_pin.py` + `workbook/T6_PIN.tsv`.
2. **Full file sweep** (Will-directed) → 10 findings; **8 closed today**, 1 flagged to PROME, 1 deliberately deferred.
3. **TRADE.md rebuilt as a trajectory surface** + `tools/trade_marks.py` / `workbook/TRADE_MARKS.tsv` (190 rows, 14 marks). Segments on slug change and **refuses to difference across an identity break**. Its own review pass then caught **two shape claims that were artifacts of the six displayed columns** — hence the `range` column on every table.
4. **Tool verification: all 14 entry points green**, incl. the 8/8 search regression live against the API. Found + fixed the wide-book mid trap; **its own v1 was defective and fixed the same run.**
5. **Built `tools/metrics.py`** — the metric layer specified since 6/21 with no implementation for 67 days. **First use retracted three of my own σ.**
6. **Tier 1:** all 10 VX rows re-pinned, `LEDGER_GLOB` declared, `outbox/delivered/` retired, local `MEMORY.md` frozen, MAINTENANCE.md backfilled (34-day gap) **and the Tier-1 work logged same-session** so the gap didn't immediately re-open.

## NEXT SESSION (dated, priority-flagged)

1. **🔴 2026-08-28 — T6 GRADES. First call on the session.** `tools/t6_pin.py --write`; re-read 8/27 as a settled close; reference day 8/21 = 0.32.
2. **🔴 2026-08-30 (Sun) — Hormuz weekly resolves.** Re-pin week-of-Aug-31. *(Literal-date gate; the last three re-pins ran 2–4d late.)*
3. **🟠 2026-08-31 (Mon) — FOUR markets resolve:** Hormuz avg-daily-transits, ships-any-day ladder, Houthi-vs-Israel, plus Aug WTI-$100 on 9/01. Re-pin or retire each.
4. **🟠 Kalshi watchlist still carries 9 `[finalized]` dead rows** (July CPI ×3, July U3 ×2, Fed-July ×2, Brent-Jul, Iran-crude) pulling as dead weight every session. **This is the Kalshi half of the roll that only got done on Polymarket.**
5. **🟠 TIER 2, agreed with Will, not started: prototype the spec-has-implementation check** and send to DAEDALUS. "Doc names a computed quantity, no code computes it" — cheap, high-yield, review-only. **Honest limit: it cannot catch 'code exists but computes it wrong'** — that class needs a human pointing a new instrument at old claims, which is exactly how today's σ retraction happened.
6. **🟠 The RE-OPENABLE CLASS (carried since 8/18, still untriaged):** conclusions resting on a pre-fix `kalshi.py search` zero, *only where load-bearing*. Named candidate now flagged in `CLAUDE.md`: **"no standalone VIX market on Kalshi."**
7. **🟠 PROME's 8/17 PortWatch war-regime ask** — sweep KB rows for war-regime PortWatch counts used as evidence. **Carried five sessions.**
8. **🟡 Nominate the near-dated Hormuz normalization legs** (by-Sep-15 1.4%, by-Oct-31 13.5%) — confirm with HAWK/BRENT/FALCON before pinning.
9. **🟡 NEXUS + RED owe the 71.5%→aggregate relabel** (packeted 8/18) — tracking only.
10. **⚪ Archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`** — mutual-reference pair, never ages into retirement eligibility.
11. **⚪ `T6_PIN.tsv` is event-scoped** — once T6 grades, FREEZE it or drop it from `LEDGER_GLOB`. Instruction is in the glob file.

## CARRY-FORWARD

- **Push state: ALL 14 ORACLE commits verified on origin. Nothing unpushed.** *(One commit ahead at close is PROME's Gate C work — deliberately NOT swept; Gate C has its own custody runbook.)*
- **⚠️ I committed outside my dir once today** (`2e8591695` swept 4 of VIOLET's staged deletions). Cause: `git add <files> && git commit -m` — **the add was scoped, the COMMIT had no pathspec**. No data lost; VIOLET + PROME notified; memory extended. **Every commit must use `git commit -F msg <explicit paths>`, including the new-file flow.**
- **VIOLET is live and repeatedly has staged work in the shared index.** Path-scope every commit; `git diff --cached` shows the whole index and looks alarming — verify with `git show --stat` *after*.
- **Coverage sweep run 8/27 → next due ~2026-09-03.**
- **Kalshi lane LIVE + SIGNED on the desktop. Record lane state PER-BOX, never as a fleet fact** — the old `CLAUDE.md` line that did this cost real time in the 8/20 T6 thread.
- **`ledger_staleness` counts HISTORY.tsv in "8 scanned" and prints no row for it** — even with `LEDGER_GLOB` declared. PROME's tool; documented in the glob file, reported not patched.

## OPEN HYPOTHESES

- **Is the complacency decoupling a regime change or a one-week dislocation?** NEH at a series high (85.0) while the best-asset S&P leg broke −15.0pp into gold (+7.0). RED ruled **no weight moves** and is carrying it as *enrichment on the watch, not evidence* — correctly, since NEH is a second descriptor of a calm RED already weights, so counting it would double-count. **Watch whether gold takes the outright lead** (30.5 vs 53.5); that IS the registered tell and it has NOT fired.
- **Why do several past-dated Iran-shipping legs sit unresolved 10+ days** (8/17 52.4%, 8/24 37.5%, 8/25 32.0%) while others settle same-day? If systematic, the daily tempo gauge is less reliable than its volume suggests.
- **Does the crowd's 1.4% by-Sep-15 Hormuz normalization survive contact with physical throughput?** ORACLE owns the crowd read only.
- **Was the Sept-hike bottom at 0.25 (8/14–8/16) a floor or a pause?** Back to ~31 with no threshold crossed either way.
