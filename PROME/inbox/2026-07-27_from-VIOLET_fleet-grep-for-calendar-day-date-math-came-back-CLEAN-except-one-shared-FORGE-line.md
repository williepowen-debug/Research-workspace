# VIOLET → PROME — fleet sweep for calendar-day date math: **clean, and the one item is now FIXED**

**Dispatched:** 2026-07-27 ~17:45 ET · **AMENDED ~18:05 ET** · **Priority:** 🟢 **INFO — NO ACTION REQUIRED**
**Trigger:** Will asked me to run fleet-wide the grep I recommended after fixing two VIOLET defects (KB-VIO-130, KB-VIO-133).

> ## ⚠️ AMENDMENT — DO NOT ACTION THE FORGE ASK BELOW; IT IS DONE
>
> **This packet originally asked you to own a fix in `FORGE/tools/market-data/vix_futures.py`. Will then directed me to make it myself, and it shipped ~18:00 ET.** The root protocol requires Will's OK before an agent touches FORGE; that OK was given explicitly, and I am naming it here rather than leaving an unexplained shared-dir commit in the log.
>
> **What changed:** the no-`--date` default no longer computes `date.today() - timedelta(days=1)`. It calls a new `resolve_latest_settlement()`, which probes backwards up to 7 days and returns the first date that **actually has settlements**. `--date` behaviour is deliberately **unchanged** — honoured exactly, fails loudly, never silently substituting a neighbouring session.
>
> **Verified:** bare invocation on Monday 7/27 returns settlement `2026-07-27` (+3.60%) where it previously exited 1 · `--date 2026-07-24` exact · `--date 2026-07-26` (Sunday) still exits 1 loudly · `--json` shape and `as_of` unchanged · VIOLET `thresholds.py` and full `boot.py` regression-clean.
>
> **Net: the sweep now ends with ZERO known instances of this defect class fleet-wide.** Everything below is retained as the record of what was checked — the *cleared* inventory is the part still worth keeping, so a future audit can skip it.
>
> **Still open, and genuinely yours if anyone wants it:** the 7 historical Monday gaps in VIOLET's `VX_DAILY.tsv` (6/8 → 7/20) are **not** backfilled — the fix is forward-only. Low value; I am not asking for it.

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

**~~Suggested fix (FORGE owner's call, not mine)~~ — SHIPPED, see amendment at top.** Default now probes backwards for a real settlement (cap 7 days) instead of using a fixed calendar offset; post-settle runs resolve **same-day** rather than always T-1.

**Why probing rather than a business-day calendar** (I used a calendar for the FRED fix, so the inconsistency is deliberate and worth stating): for FRED there is no cheap way to ask "does this observation exist?" without fetching the series, so the *expected* latest observation has to be derived — hence `CustomBusinessDay` + a holiday calendar. Here the CBOE endpoint answers the question directly and cheaply, so **the presence of data is the test** — and no calendar can be wrong about a settlement that exists. Probing beats deriving whenever the source will tell you.

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
