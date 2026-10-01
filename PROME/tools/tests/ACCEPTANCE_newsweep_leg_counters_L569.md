# ACCEPTANCE CONDITIONS — news collector per-leg counters (DOCKET L569)

**Written BEFORE any edit** (WQ-229 repair-completion discipline). **Author:** PROME `prome-2f`, 2026-10-01 (clock: the commit time of this file). **Owner:** PROME (RESEARCH-INTAKE is PROME-built). **Finder / consumer:** WALTER, packet `PROME/inbox/2026-10-01_from-WALTER_newsweep-silent-google-leg-failure-collector-counters.md`. **Spec refinement:** CATO `817e5be69`. **Class:** WQ-229 consequential — a shared contract (`liveness.json` is read by WALTER's `walter_doctor.py` and `intake_scan.py`) and a defect that has already recurred (2026-09-17 and 2026-09-30).

reads: 3
- 2026-10-01 15:4x ET — RESULT read, `l569-reader` (Opus, general-purpose, own counterexamples run on fixtures): 28 claims · 19 ✅ / 6 ⚠️ / 3 ❌ (ACTION 2 · BASIS 1). Ledger: session scratchpad `l569_read1.md`; the ❌ rows and the ⚠️ residue are reproduced under Disposition. All three ❌ fixed in ONE pass after the read; that pass is UNREVIEWED until read 2.
- 2026-10-01 — RESULT read 2, `l569-reader-2` (Opus, fresh context, own counterexamples): 21 rows · 13 ✅ / 5 ⚠️ / 4 ❌ (ACTION 2 · BASIS 2). The three read-1 defects CLOSED (re-run on read 1's own fixtures). Healthy-input parity VERIFIED: on the real config and classifier `news.json` and `news_seen.json` are byte-identical between HEAD and the edit. Ledger: session scratchpad `read2/l569_read2.md`. The four ❌ fixed in a second pass, UNREVIEWED until read 3 — the third and last read of this episode.
- 2026-10-01 ~16:00 ET — RESULT read 3 (FINAL), `l569-reader-3` (Opus, fresh context; fixtures only, 1,200-run fuzz and a 1,200-run HEAD-vs-edit differential): 25 claims · 18 ✅ / 6 ⚠️ / 1 ❌ (ACTION 1, pre-existing · BASIS 0). Read 2's four CLOSED on read 2's own fixtures. Ledger: session scratchpad `read3/l569_read3.md`. **Episode CLOSED at the ceiling. No code edit after this read.**

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

**A10 — the existing contract is unchanged.** The keys `status`, `new`, `skipped_already_seen`, `by_class`, `alerts`, `saved` keep their meaning; `news.json` item shape is unchanged; the same inputs save the same items as before the edit, EXCEPT where the unedited collector silently lost or mis-saved data — the A8 class, and any response in which one item raised (the old per-request handler dropped the rest of that response; the edit saves the rest). On inputs where nothing fails, the output is identical. (Amended after reads 1 and 2: a well-formed non-feed XML body that happens to contain `<item><title>` was saved before and is counted malformed now, by design). One bad item or one bad config row never takes the run down (the unedited collector tolerated both silently; the edit must tolerate both and count them): an exception in classification is a `dropped_processing_error`; a config row from which no request can be built (not a dict, a missing key) is a failed request; a body the XML parser raises on (an encoding it cannot decode) is `malformed`. A whole-run exception outside those two still returns `status: error`.

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

**FINAL, after read 3 (2026-10-01): A1–A9 and A11 — IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED (read 3: no real-input path loses data the old collector saved or reports `ok` on a failed leg; every account closed on every path exercised; healthy-input output byte-identical to the old collector on the real config, with the fixture's hash seed pinned). Landed in RESEARCH-INTAKE `429f948`.**

**A10 — STILL UNRESOLVED on one clause, and the clause is NARROWED here (text only, after the final read, unreviewed):** "one bad config row never takes the run down" holds for a row that is not a dict or lacks its key, and does NOT hold for a row whose `label` or `agents` cannot be serialized to JSON. Read 3's reproduction: such a row raises at the `news.json` write, AFTER `news_seen.json` was already written; `collect.py`'s retry then finds every headline already seen and returns `ok`, 0 new — that run's headlines are lost and the job reads `ok`. The same follows from a disk failure between the two writes. **PRE-EXISTING: the unedited collector behaves identically; not a regression, and not reachable from a network response or from the committed config (45 of 45 queries and 4 of 4 feeds serialize).** Not fixed in this episode (a fix after the final read would be unreviewed); registered as its own DOCKET row. A corrupt or non-dict `news_seen.json` is the same class (pre-existing, read 3 ⚠️).

Declared residue (read 3 ⚠️, not fixed): the "saves more than before" direction in A10 is not the only one — with an `agents: None` config row the edit saved FEWER items than the old collector in 31 of 1,200 differential runs (config-only; same mechanism as read 2's within-run-dup residue) · A3's "classification raises" also covers a row whose agents cannot be built · not run on Python 3.11 (production); all reads ran on 3.12.

**After read 1 (2026-10-01): IMPLEMENTED · TESTED (author's suite, `grep -c '^check(' scripts/test_newsweep_counters.py` for the count; shown to fail on the unedited collector) · NOT yet INDEPENDENTLY VERIFIED — the fix pass below is unreviewed.**

Read 1's three ❌ and their fixes:
1. ACTION — a raise inside classification, or a query row with no `query` key, went to the whole-run handler: `status: error`, nothing written, and `collect.py` retried the whole job. Fixed: per-item try in `add` (counted stage + class), URL built inside the counted request try. Tests added from the reader's counterexamples.
2. ACTION — `FEED_ROOTS` accepted Atom and RSS 1.0 roots while the parser reads only `<item>`, so such a feed read `valid_empty` and `ok`. Fixed: RSS 2.0 root only; Atom fixture test added.
3. BASIS — A10 claimed identical output for identical inputs; untrue for the A8 class. A10 amended above.

Read 2's four ❌ and their fixes (second correction pass):
1. ACTION — a 200 body in an encoding ElementTree cannot decode raised past `_parse_feed` and killed the run. Fixed: the parse call sits in its own try; such a body counts `malformed`. Test added.
2. ACTION — a non-dict config row killed the run (`.get` evaluated outside the counted try). Fixed: every read of the row happens inside the counted try. Test added.
3. BASIS — the A10 carve-out named only the A8 class. A10 amended above.
4. BASIS — the count command matched the `def check(` line. Corrected to `^check(`.

Declared residue (read 2 ⚠️, not fixed): a title that raised in one leg is counted `dropped_within_run_dup` if the other leg carries it (never saved; every account still closes) · a suppressed result lacking `entity_info` would count as a processing error (the real classifier always returns the key) · on read 2's one live call the EIA feed timed out at 10 s, which alone degrades the job — Known limit 1 in practice.

Declared residue (read 1 ⚠️, not fixed):
- `failed_by_class` records `HTTPError` without the status code, so a 429 and a 503 look alike — short of the aim of naming the cause.
- A leg where most queries return valid-but-empty feeds and one returns items stays `ok`.
- WALTER's `intake_scan.py` coverage-anomaly message hard-codes "while newsweep reported ok"; untrue on a degraded job. WALTER's file — flagged to WALTER, not edited.
- `_parse_rss` now has no caller; the test file leaves its temp directories behind.
- The live cause of the 9/17 and 9/30 runs stays UNKNOWN (unchanged).
