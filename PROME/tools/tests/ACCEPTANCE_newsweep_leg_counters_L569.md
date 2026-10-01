# ACCEPTANCE CONDITIONS — news collector per-leg counters (DOCKET L569)

**Written BEFORE any edit** (WQ-229 repair-completion discipline). **Author:** PROME `prome-2f`, 2026-10-01 (clock: the commit time of this file). **Owner:** PROME (RESEARCH-INTAKE is PROME-built). **Finder / consumer:** WALTER, packet `PROME/inbox/2026-10-01_from-WALTER_newsweep-silent-google-leg-failure-collector-counters.md`. **Spec refinement:** CATO `817e5be69`. **Class:** WQ-229 consequential — a shared contract (`liveness.json` is read by WALTER's `walter_doctor.py` and `intake_scan.py`) and a defect that has already recurred (2026-09-17 and 2026-09-30).

reads: 1
- 2026-10-01 15:4x ET — RESULT read, `l569-reader` (Opus, general-purpose, own counterexamples run on fixtures): 28 claims · 19 ✅ / 6 ⚠️ / 3 ❌ (ACTION 2 · BASIS 1). Ledger: session scratchpad `l569_read1.md`; the ❌ rows and the ⚠️ residue are reproduced under Disposition. All three ❌ fixed in ONE pass after the read; that pass is UNREVIEWED until read 2.

## The defect, in its own terms

`Research-Intake/scripts/fetch_newsweep.py` wraps every Google News request and every RSS feed in `try/except Exception: pass`, and `_parse_rss` returns an empty list on a parse error. Nothing is counted. A run in which the whole Google News leg returns nothing reports `status: ok` with `errors: []`, and the consumer cannot tell an outage from a quiet day. Cause on the runner for 9/17 and 9/30: UNKNOWN (rate limiting is a guess). This repair makes the next occurrence name its own cause; it does not fix the cause.

## Scope

In: counters and status inside `fetch_newsweep.py`; the News line of `collect.py::render_summary` (it prints only when `status == "ok"` today, so a degraded run would lose its line). Out: classification, routing, dedup rules, query lists, retry policy, the lane's overall `status` rule (it keys on `error` only; consumers already read per-job status), WALTER's consumer tools.

## The conditions — properties, not symptom restatements

**A1 — requests are counted per leg.** For each leg that runs (`google_news`, `rss`): attempted, succeeded, failed, and failed broken down by exception class name. attempted = succeeded + failed.

**A2 — responses are counted per leg.** Every succeeded request lands in exactly one of: `parsed` (a feed document with at least one titled item), `valid_empty` (a feed document with none), `malformed` (not parseable as XML, or XML that is not an RSS 2.0 document — an Atom or RSS 1.0 document counts malformed here, because this parser reads only plain `<item>` elements and would otherwise report a live feed as quiet; amended after read 1). succeeded = parsed + valid_empty + malformed.

**A3 — headlines are accounted for per leg, and the account closes.** retrieved = dropped_over_cap + dropped_within_run_dup + dropped_already_seen + dropped_noise_known + dropped_processing_error + saved (the processing-error stage added after read 1: a headline whose classification raises is counted with its exception class, never lost and never fatal). The per-source cap (`MAX_ARTICLES_PER_SOURCE`) is a stage of its own: without it the chain does not sum. Sum of `saved` over legs = the job's `new`.

**A4 — a failing leg is never `ok`.** Job `status` is `degraded` when, for any leg that runs, failed + malformed + dropped_processing_error > 0 or retrieved = 0. `degraded_reasons` names each leg and why. `ok` is returned only when no leg trips.

**A5 — a quiet day is not an outage (neighbour: ORDINARY).** Every request succeeds, many headlines are retrieved, all are already seen, zero are saved ⇒ `ok`. Zero saved alone never degrades.

**A6 — a partial failure shows (neighbour: OVERLAP of success and failure in one leg).** One Google query raises while the others succeed ⇒ `degraded`, the failure counted with its class, the other queries' headlines still saved, `news.json` and `news_seen.json` still written.

**A7 — a headline in two legs is counted once as saved (neighbour: OVERLAP).** The same title from Google and from an RSS feed: saved in the first leg, `dropped_within_run_dup` in the second; A3 holds in each leg.

**A8 — a 200 that is not a feed is malformed, not empty (neighbour: MISSING INFORMATION).** An HTML block page (not well-formed XML) and a well-formed XML document whose root is not a feed both count `malformed`. A real feed with zero items counts `valid_empty` and does not by itself degrade.

**A9 — the web-scrape leg is reported as what it is.** The spec names three legs; this collector has never run the scrape leg (the config list is inert here). It is reported `not_run` with the reason, carries no counters, and never contributes to `ok` or `degraded`. No fabricated zeros.

**A10 — the existing contract is unchanged.** The keys `status`, `new`, `skipped_already_seen`, `by_class`, `alerts`, `saved` keep their meaning; `news.json` item shape is unchanged; the same inputs save the same items as before the edit, EXCEPT the A8 class (amended after read 1: a well-formed non-feed XML body that happens to contain `<item><title>` was saved before and is counted malformed now, by design). One bad item or one bad config row never takes the run down (the unedited collector tolerated both silently; the edit must tolerate both and count them): an exception in classification is a `dropped_processing_error`, a config row from which no URL can be built is a failed request. A whole-run exception outside those two still returns `status: error`.

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

**After read 1 (2026-10-01): IMPLEMENTED · TESTED (author's suite, `grep -c 'check(' scripts/test_newsweep_counters.py` for the count; shown to fail on the unedited collector) · NOT yet INDEPENDENTLY VERIFIED — the fix pass below is unreviewed.**

Read 1's three ❌ and their fixes:
1. ACTION — a raise inside classification, or a query row with no `query` key, went to the whole-run handler: `status: error`, nothing written, and `collect.py` retried the whole job. Fixed: per-item try in `add` (counted stage + class), URL built inside the counted request try. Tests added from the reader's counterexamples.
2. ACTION — `FEED_ROOTS` accepted Atom and RSS 1.0 roots while the parser reads only `<item>`, so such a feed read `valid_empty` and `ok`. Fixed: RSS 2.0 root only; Atom fixture test added.
3. BASIS — A10 claimed identical output for identical inputs; untrue for the A8 class. A10 amended above.

Declared residue (read 1 ⚠️, not fixed):
- `failed_by_class` records `HTTPError` without the status code, so a 429 and a 503 look alike — short of the aim of naming the cause.
- A leg where most queries return valid-but-empty feeds and one returns items stays `ok`.
- WALTER's `intake_scan.py` coverage-anomaly message hard-codes "while newsweep reported ok"; untrue on a degraded job. WALTER's file — flagged to WALTER, not edited.
- `_parse_rss` now has no caller; the test file leaves its temp directories behind.
- The live cause of the 9/17 and 9/30 runs stays UNKNOWN (unchanged).
