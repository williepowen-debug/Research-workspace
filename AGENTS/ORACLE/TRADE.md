# ORACLE — TRADE (how prediction-market odds inform positions)

**Updated:** 2026-08-12 (live-reads table refreshed 7/22 → 8/12 off a same-session pull, closing DAEDALUS's 8/11 refresh-or-freeze flag — the file had carried 7/22 figures onto a routing surface for 21 days and would not have self-flagged until ~8/21). ORACLE does **not** size or execute — it supplies the crowd-implied probability so trade owners can (a) anchor predictions to *surprise-vs-pricing*, not headline outcomes, and (b) sanity-check thesis odds against real money.

> **Discipline (memory: thin-liquidity + anchor-to-surprise):** never let a single thin-market print move a position mark. The tradeable reaction lives in the *deviation from what's priced* — supply the priced baseline, not a directional call.
>
> ⚠️ **This table is a DATED SNAPSHOT, not a live feed.** Every row is stamped to the pull below. **`STATUS.md` is the live home** — if this header is more than a few days old, re-pull rather than cite. *(The 7/22→8/12 rot that DAEDALUS caught is the reason this warning exists: a routing surface with no self-flag is exactly where superseded odds go unnoticed.)*

---

## Live reads → position implications

| Market (live, **2026-08-12T16:43Z**) | Reads onto | Implication |
|---|---|---|
| **Fed no-cuts 85.5%** (−3.1/7d) · **Fed-hike-2026 54.5%** (−8.0/7d, −17.0 vs 7/24) · Sept-mtg-hike **33.5%** (−13.0/7d) | KRE / OZK / WAL shorts | **STILL SUPPORTIVE, BUT THE CONVICTION LEG IS GONE — RE-KEY, DO NOT INVERT.** The >66% re-break trigger has UNFIRED and the hike path de-rated hard: 71.5% (7/24) → 54.5%. ⚠️ **This is NOT a dovish turn** — a hike remains *modal* and no-cuts is 85.5%, so higher-for-longer (the actual CRE-refi/NIM mechanism) is intact; what died is "hike is the firm base case (>2/3)." Kalshi corroborates: Dec-level book mid **57.0%**, Sept **35.0%**. **Timing matters for attribution: −12.0pp of the −17.0 came from the 7/29 FOMC hold + the 8/7 payroll print; today's CPI only −5.0pp.** |
| **WTI-$100 (Aug) 12.5%** (+5.0/7d) · **Hormuz-normal-Dec31 46.5%** (−15.0/7d, $7.9M deep) · US-invade-Iran 18.5% (+3.0) | BRENT / HAWK / FALCON energy | **PREMIUM, NOT SHORTAGE — and the reopening is being priced OUT, not in.** v3 disruption−supply spread **+41.0pp** (series high). The crowd holds an indefinite low-throughput grind: end-August 0-20-transits bucket **82.5%** (+45.0/7d), ships-any-day ladder **25.0%** (−44.0/7d). ⚠️ **The month-stamped WTI leg widens the spread MECHANICALLY on time decay** (expires 9/1, no Sept market exists yet) — part of +41.0 is calendar, not risk. **BRENT/FALCON own the throughput adjudication; this row supplies the priced baseline only.** |
| **Recession 8.5%** (Kalshi 10.0%) | Whole bear book | **Caution flag, still live, still converged** (~1.5pp cross-platform). Crowd remains calm. If it is right, equity-stress positions are early/oversized. RED owns the adjudication — **still owed a current fleet recession number, carried since 6/13.** |
| **US bank failure by Dec 31 69.5%** (⚠️thin $2.8K) · named-bank-EOY **3.6%** (⚠️thin) | REGINALD / WAL / OZK bank shorts | **Broad-scope gauge only — thin, and unchanged in substance.** The Dec-31 binary asks "ANY US bank failure" (small-bank failures are common → ~70% is unremarkable), a different question from named-bank-EOY (top 3.6%). **No name is priced.** Do not mark on either thin print. |
| **Nothing Ever Happens 79.5%** (−2.5/7d) · best-asset-S&P 68.0% (−2.5) | VIOLET vol / tail hedges | **⚠️ SIGN FLIP VS THE 7/22 ROW — READ THIS ONE CAREFULLY.** The old row said "complacency crack deepened" at 66.5%. **It did not persist: NEH round-tripped to 79.5%, near its series high.** Complacency is now *elevated*, not cracking — the opposite implication for tail hedges. Anyone who carried the 7/22 read for the last three weeks had the sign backwards, which is precisely the cost of an unstamped routing surface. |

---

## Standing rule for downstream agents

When ORACLE hands you a market probability:
1. **Is your trigger outcome already priced?** If yes, re-key your prediction to "more X than priced" (anchor-to-surprise).
2. **Is the market thin (⚠️ flag)?** If yes, treat any move as unconfirmed until a ≥3-day re-check + an independent source (OIS/dealer/Bloomberg) agrees.
3. **Divergence ≠ direction.** A gap vs thesis is a question for RED, not an automatic position change.

*No position is opened or sized from this file. Owners: FORGE / the named domain agent.*
