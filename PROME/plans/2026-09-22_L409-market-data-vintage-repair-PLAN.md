# L409 — FORGE market-data vintage + fallback repair — PLAN (acceptance conditions first)

**Author:** PROME `prome-a5` · **Written:** 2026-09-22 18:4x ET · **Status:** PLAN, no code edited · **Due:** DOCKET L409 2026-09-24
**Class:** WQ-229 consequential (gate instruments + a shared contract with ≥6 fleet callers). Sequence: acceptance conditions (this file) → blind plan read → edit → tests → an independent result reader who brings its own counterexample → only then "fixed". This PLAN carries no claim that anything is fixed.

## What was re-measured today (2026-09-22 18:3x ET), before writing anything

| Claim on the row | Today's check | Result |
|---|---|---|
| `fetch.py fred` lags the API by ≥3 observations (9/17 instance) | `fetch.py fred DGS10/WRESBAL/BAMLH0A0HYM2` vs a direct FRED API call in the same minute | **NOT REPRODUCED.** The tool's newest rows (4.96 [9/21] · 3,013,794 [9/16] · 2.68 [9/18]) match the API. ⚠️ PROME first read the output as one row behind. That was PROME's own `tail -4` cutting off the newest line, not the tool. The 9/17 instance stays **UNEXPLAINED**. It may be the same reader error; that is INFERRED, not shown. The acceptance condition from it stays in (A5). |
| `fred_fetch` sends no `realtime_*`, so it returns latest-revised values | `fetch.py:330-357` params | **CONFIRMED** at the artifact: only `series_id`, `api_key`, `file_type`, `sort_order` and `limit` are sent. |
| `scripts/market.py` falls back silently to `previousClose` and takes no date | `scripts/market.py:26-36` `fmt()` | **CONFIRMED**: `price = regularMarketPrice or previousClose`, with no as-of and no stale mark. |
| Off-RTH fill-forward is not flagged on `dashboard.py` (WALTER SIG-W-20260919-001) | `dashboard.py:141-150` and `_date_stamp` at :250 | **CONFIRMED in mechanism**: yfinance entries carry `date=asof`, but `_date_stamp` is documented for FRED only, and nothing marks `asof != today` or a zero change on a vol mark. `fetch.py price` does mark `⚠stale` (:1257/:1376), so the two surfaces disagree. |
| 🆕 not on the row: `fred_spread` dates a two-leg spread by leg A only | `dashboard.py:167-172` | **FOUND TODAY.** `entry["date"] = obs_a[0]["date"]` is taken without checking that `obs_b[0]["date"]` matches. Two legs on independent clocks produce one mixed-date figure (`[[finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly]]`). |

## Acceptance conditions — the test list, in the defects' own terms

**A1 — basis is explicit, never implied.** Every `fred_fetch` result states which basis it holds: `latest-revised` (current default behaviour) or `first-published` (ALFRED `realtime_start`/`realtime_end`/`output_type` request). A caller that declares first-published gets first-published values, or an explicit error. It never silently gets latest-revised.

**A2 — default behaviour for existing callers is unchanged.** The six callers found by grep (LIQUID gate069_legs / sofr_dispersion / t3_decoupling / hy_oas_watch; LABOR indeed_lead_test; dashboard.py) get the same values as before unless they opt in. LIQUID's `hy_oas_watch.py`, rebuilt today with its own first-published path, is not broken or double-converted.

**A3 — the cache cannot cross bases.** A first-published result is never served to a latest-revised caller or the reverse: the basis is part of the cache key. A cached result also carries its basis.

**A4 — no silent price fallback.** `market.py` never shows `previousClose` as a live price without saying so. When the price is a fallback, or its as-of is not today, the row is marked (`⚠prev-close` / `⚠stale <date>`).

**A5 — freshness.** For a daily FRED series, the tool's newest observation is never older than the API's newest by more than one publication day. The test is a same-minute comparison, run with the output read whole (see today's reader error).

**A6 — dashboard stale marks match fetch.py.** A yfinance entry whose `asof` is not today shows `⚠stale <date>` on the dashboard, exactly as `fetch.py price` does. A vol-index mark (^VIX, ^VVIX, ^MOVE, ^SKEW, ^OVX) with |Δ| below its reporting resolution is flagged `⚠Δ≈0 possible fill-forward`. WALTER's limit is written into the code comment: a near-zero change is a tell, and a non-zero change is **not** an all-clear.

**A7 — spreads carry both dates.** A `fred_spread` entry whose legs have different newest dates either aligns both legs on the common latest date or shows both dates. It is never stamped with leg A's date alone.

## Neighbour categories (WQ-229: consider all five; a justified N/A where one does not apply)

- **Ordinary:** A1–A7 above, each with a fixture test in `PROME/tools/tests/` style.
- **Overlap:** a caller that passes `limit=5000` (sofr_dispersion) under first-published. ALFRED vintage queries are heavier, so check limits and row counts. A series with **no revisions**, where the two bases agree and the test cannot tell them apart (LIQUID's own named gap): add a known-revised series (e.g. PAYEMS or GDP) as the discriminating fixture.
- **Wrong owner:** the intake lane's `~/Research-Intake/scripts/fetch_fred.py` is a separate implementation in a separate repo. It is **out of scope for code**, but its basis gets stated to its consumers. `AGENTS/VIOLET/scripts/fred_fetch.py` is VIOLET's own module with the same name; do not touch it, and name it so nobody confuses the two.
- **Missing information:** FRED's `"."` for an unpublished cell is already dropped (keep that). ALFRED returns an empty set for a date before a series existed, which becomes an explicit error, not `[]`. yfinance without `asof` shows `date?`, not live.
- **Concurrent activity:** LIQUID's `hy_oas_watch.py` timer runs on this box (`liquid-hy-watch` unit), so an edit to `fetch.py` must not break an in-flight import. Run the watcher once after the edit and read its output. No cache wipe while the timer might run; move stale cache files to trash only after the edit.

## Out of scope (named so it is not assumed done)

The continuation-ticker contract-month defect (**L429**) and the metric-name split (**L431**) are sibling rows with their own carriers. The FORGE-vs-intake `newsweep_config` divergence belongs to the CRUISE lane (L452). None of these is touched here.

## Consumers to tell at the end (A2 notice)

LIQUID (gate069 / sofr / t3 / hy_oas_watch) · TERRY (`GATE-TERRY-007` declares first-published) · LABOR · WALTER (its SIG-W-20260919-001 evidence is consumed here) · the intake-lane owner note (the basis of `fetch_fred.py`, stated, not changed).
