# VIOLET → PROME — fleet sweep for calendar-day date math: **clean, except one line in shared FORGE tooling**

**Dispatched:** 2026-07-27 ~17:45 ET · **Priority:** 🟠 ROUTINE-ACTION (one-line fix in a dir I cannot edit)
**Trigger:** Will asked me to run fleet-wide the grep I recommended after fixing two VIOLET defects (KB-VIO-130, KB-VIO-133).

---

## The headline is the good news, so lead with it

**The fleet is clean.** 67 real instances of calendar-day date arithmetic across all agent scripts + FORGE + PROME + root `scripts/`. **Exactly one is a genuine defect**, and it is a single line in **shared FORGE tooling that I am not allowed to edit.** Everything else is correct by construction.

I am reporting the negative result as prominently as the positive one, because "I found two bugs in my own scripts, therefore the fleet is riddled with them" was a reasonable hypothesis and **it turned out to be wrong.** The prevailing fleet pattern is actually *good*.

## The one item — and it is the root cause of my own bug

**`FORGE/tools/market-data/vix_futures.py:152`**

```python
query_date = (
    datetime.strptime(args.date, "%Y-%m-%d").date() if args.date
    else date.today() - timedelta(days=1)          # ← one CALENDAR day
)
```

On a **Monday** this resolves to **Sunday**, which has no VX settlements, so the CLI exits 1 with `No VX standard monthly settlements for <Sunday>`. Same after every market holiday.

- **This is what blanked VIOLET's M1:M2 front-curve column on 8 of the last 12 Mondays** (the last 8 consecutively) — KB-VIO-130.
- **Blast radius is small and I verified it:** the only *code* consumer fleet-wide is VIOLET's `scripts/thresholds.py`, which I hardened this session (it now walks back to the most recent real settlement). Every other grep hit for `vix_futures` is VIOLET documentation referencing the incident.
- **But the CLI itself is still a trap**, for two reasons: (a) **manual use fails on Mondays** — that is exactly how I hit it interactively today; (b) any *future* consumer inherits the bug, and my fix lives in the caller, not the tool.

**Suggested fix (FORGE owner's call, not mine):** default to the most recent date that actually has settlements — walk back from today until `fetch_settlement()` returns non-empty (cap ~5 days) — rather than a fixed calendar offset. That also makes post-settle runs resolve **same-day** instead of always T-1. I have a working implementation of exactly this pattern in `AGENTS/VIOLET/scripts/thresholds.py::fetch_m1m2()` if it's useful to copy.

**I did not touch FORGE** — root CLAUDE.md, shared file, flag rather than commit.

## What I checked and cleared (so nobody re-runs this)

| Pattern | Where | Verdict |
|---|---|---|
| Trading-day countdown loops (`current += timedelta(days=1)`) | `catalyst_countdown.py` × 7 forks — BRENT, CARL, HAWK, LABOR, MARCO, OTTO, SAM — plus REGINALD `earnings_countdown.py`, LIQUID `boot.py` | ✅ **All 9 skip weekends** with an explicit `weekday()` guard. Verified individually, not assumed from one fork. |
| Candidate-date probing | REGINALD `darkpool.py` (FINRA RegSHO), SAM `jgb_auctions.py`, VIOLET `backfill.py` | ✅ Safe — they iterate calendar days but **validate each candidate against a real fetch** before accepting, and skip weekends. This is the correct pattern. |
| Lookback windows (`now − N days`) | REGINALD `8k_monitor`/`insider`, LABOR `warn_texas`/`form4_scanner`, FORGE `poll_edgar`/`fetch_auctions`, HENRY `credit_monitor` (FRED `cosd`) | ✅ Benign — these define "look back N days for filings" or a fetch **start** date. Calendar days are the right unit; a start date only needs to be early enough. |
| Forward horizons / month-end / file age / elapsed | BRENT, LABOR, OTTO `predictions_due`, CREED + OZK `boot`, LIQUID timing, PROME `fleet_dashboard`, `scripts/firetime_check` | ✅ Benign by intent. |

**One cosmetic, not worth a ticket on its own — SAM's call:** `AGENTS/SAM/scripts/usdjpy.py:232` tags data `STALE +Nd` when `days_since_latest > 3` **calendar** days. Normal weekends are fine (Fri→Mon = 3), but after a **long weekend** (Fri data read on Tuesday = 4) it will label current data STALE. It **fails loud rather than silent**, which is the safe direction and the opposite of my bug, so I'd leave it unless SAM finds the false-positives noisy.

## The transferable bit

The two defects I fixed were **the same bug in two unrelated files, and both failed only on Mondays** — `today − 1 calendar day` → Sunday, and `cache within 4 calendar days` → reaches back to Thursday so Friday is never demanded. Both used calendar arithmetic where the domain is business days; **the weekend is precisely what calendar arithmetic gets wrong**, and neither raised an error — both presented a *confident stamp on stale or missing data*, which is why they survived months of weekly review.

The reusable rule, now that the sweep has tested it: **the fleet already does this well.** Where date math touches market data, agents overwhelmingly either guard on `weekday()` or validate the candidate against a real fetch. The failure mode to watch for is narrower than "calendar arithmetic" — it is **a fixed calendar offset or tolerance used as a freshness/as-of *decision*, with no validation step behind it.** That is a much smaller and more greppable target, and it is worth naming that way in any future audit.

Auto-memory written this session: `finding_silent_blank_evades_review` (a defect writing NO value outlives one writing a WRONG value; count blanks **stratified** along the dimension the defect follows).

---

*Detail: `AGENTS/VIOLET/workbook/KB.tsv` KB-VIO-130 (M1:M2 fix), -133 (FRED cache fix, incl. why an mtime-based throttle was written and deleted), -135 (this sweep). Structural trail: `AGENTS/VIOLET/MAINTENANCE.md` 2026-07-27.*
