# ACCEPTANCE CONDITIONS — news collector per-leg counters (DOCKET L569)

**Written BEFORE any edit** (WQ-229 repair-completion discipline). **Author:** PROME `prome-2f`, 2026-10-01 (clock: the commit time of this file). **Owner:** PROME (RESEARCH-INTAKE is PROME-built). **Finder / consumer:** WALTER, packet `PROME/inbox/2026-10-01_from-WALTER_newsweep-silent-google-leg-failure-collector-counters.md`. **Spec refinement:** CATO `817e5be69`. **Class:** WQ-229 consequential — a shared contract (`liveness.json` is read by WALTER's `walter_doctor.py` and `intake_scan.py`) and a defect that has already recurred (2026-09-17 and 2026-09-30).

reads: 0

## The defect, in its own terms

`Research-Intake/scripts/fetch_newsweep.py` wraps every Google News request and every RSS feed in `try/except Exception: pass`, and `_parse_rss` returns an empty list on a parse error. Nothing is counted. A run in which the whole Google News leg returns nothing reports `status: ok` with `errors: []`, and the consumer cannot tell an outage from a quiet day. Cause on the runner for 9/17 and 9/30: UNKNOWN (rate limiting is a guess). This repair makes the next occurrence name its own cause; it does not fix the cause.

## Scope

In: counters and status inside `fetch_newsweep.py`; the News line of `collect.py::render_summary` (it prints only when `status == "ok"` today, so a degraded run would lose its line). Out: classification, routing, dedup rules, query lists, retry policy, the lane's overall `status` rule (it keys on `error` only; consumers already read per-job status), WALTER's consumer tools.

## The conditions — properties, not symptom restatements

**A1 — requests are counted per leg.** For each leg that runs (`google_news`, `rss`): attempted, succeeded, failed, and failed broken down by exception class name. attempted = succeeded + failed.

**A2 — responses are counted per leg.** Every succeeded request lands in exactly one of: `parsed` (a feed document with at least one titled item), `valid_empty` (a feed document with none), `malformed` (not parseable as XML, or XML that is not a feed document). succeeded = parsed + valid_empty + malformed.

**A3 — headlines are accounted for per leg, and the account closes.** retrieved = dropped_over_cap + dropped_within_run_dup + dropped_already_seen + dropped_noise_known + saved. The per-source cap (`MAX_ARTICLES_PER_SOURCE`) is a stage of its own: without it the chain does not sum. Sum of `saved` over legs = the job's `new`.

**A4 — a failing leg is never `ok`.** Job `status` is `degraded` when, for any leg that runs, failed + malformed > 0 or retrieved = 0. `degraded_reasons` names each leg and why. `ok` is returned only when no leg trips.

**A5 — a quiet day is not an outage (neighbour: ORDINARY).** Every request succeeds, many headlines are retrieved, all are already seen, zero are saved ⇒ `ok`. Zero saved alone never degrades.

**A6 — a partial failure shows (neighbour: OVERLAP of success and failure in one leg).** One Google query raises while the others succeed ⇒ `degraded`, the failure counted with its class, the other queries' headlines still saved, `news.json` and `news_seen.json` still written.

**A7 — a headline in two legs is counted once as saved (neighbour: OVERLAP).** The same title from Google and from an RSS feed: saved in the first leg, `dropped_within_run_dup` in the second; A3 holds in each leg.

**A8 — a 200 that is not a feed is malformed, not empty (neighbour: MISSING INFORMATION).** An HTML block page (not well-formed XML) and a well-formed XML document whose root is not a feed both count `malformed`. A real feed with zero items counts `valid_empty` and does not by itself degrade.

**A9 — the web-scrape leg is reported as what it is.** The spec names three legs; this collector has never run the scrape leg (the config list is inert here). It is reported `not_run` with the reason, carries no counters, and never contributes to `ok` or `degraded`. No fabricated zeros.

**A10 — the existing contract is unchanged.** The keys `status`, `new`, `skipped_already_seen`, `by_class`, `alerts`, `saved` keep their meaning; `news.json` item shape is unchanged; the same inputs save the same items as before the edit. A whole-run exception still returns `status: error`.

**A11 — the summary keeps its News line on a degraded run,** marked as degraded with the reasons.

## Neighbour categories (README contract)

| Category | Disposition |
|---|---|
| Ordinary | A1–A3, A5 |
| Overlap | A6, A7 |
| Wrong owner | N/A — one lane, one writer; no ownership perimeter in the counted data |
| Missing information | A8, A9; a leg with no configured sources retrieves 0 ⇒ degraded, loud |
| Concurrent activity | N/A — the workflow runs in a single `collect` concurrency group; the collector is the only writer of `liveness.json` and `news_seen.json` |

## Tests

`Research-Intake/scripts/test_newsweep_counters.py` — fixtures only, network patched out, temp directories; run first against the unedited collector to show the conditions FAIL there (the guard is falsified before it is trusted).

## Known limits, stated before the edit

- A4's strict rule makes a single timed-out query degrade the job. If that proves a daily occurrence the consumer line becomes noise; the remedy is a retry or a threshold, and that is a separate change with the owner's (WALTER's) word, not a loosening here.
- The cause of the 9/17 and 9/30 zero-Google runs stays UNKNOWN until a run fails with counters in place.
- The lane's overall `status` stays `ok` on a degraded job (unchanged rule); consumers read per-job status.

## Disposition

*(filled after implementation and the independent read)*
