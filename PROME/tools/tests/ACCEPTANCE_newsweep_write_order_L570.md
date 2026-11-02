# ACCEPTANCE CONDITIONS — news collector write order (DOCKET L570)

**Written BEFORE any edit** (WQ-229). **Author:** PROME `prome-40`, 2026-11-02 (clock: the commit time of this file). **Owner:** PROME (RESEARCH-INTAKE is PROME-built). **Consumer:** WALTER (reads `data/<date>/news.json`). **Origin:** read 3 of the L569 episode (`ACCEPTANCE_newsweep_leg_counters_L569.md` § Disposition). Own episode, materially different defect from L569.

reads: 0

## The defect, in its own terms

`Research-Intake/scripts/fetch_newsweep.py::fetch` writes `news_seen.json` (every newly saved headline marked seen) BEFORE it serializes and writes `data/<day>/news.json`. If anything raises between the two writes (a row whose `label` is not JSON-serializable, a disk error), the job raises; `collect.py` retries once; on the retry every one of those headlines is in `news_seen.json`, so it is skipped as already seen, `news.json` is written with zero items and the job reports `ok`. The run's headlines are lost and nothing says so. Separately, `_load_seen` turns a corrupt or non-dict `news_seen.json` into `{}` silently, which re-reports up to 14 days of headlines as new.

## Scope

In: the write path and `_load_seen` in `fetch_newsweep.py`. Out: classification, routing, dedup rules (DEDUP_DAYS, key form), counters (L569), queries, retry policy in `collect.py`, the `news.json` item shape.

## The conditions

**W1 — no headline is marked seen unless its run's `news.json` was written.** If serializing or writing `news.json` fails, `news_seen.json` is byte-identical to its state before the run, and the job returns `status: error` naming the failure (it does not raise past `fetch`).

**W2 — a retry after a W1 failure re-collects.** With the same inputs, the second attempt sees the headlines as unseen (none counted `dropped_already_seen` because of the failed attempt).

**W3 — ordinary runs are unchanged (neighbour: ORDINARY).** On healthy inputs the edited collector writes the same `news.json` bytes and the same `news_seen.json` content as HEAD, and returns the same dict.

**W4 — a failure AFTER `news.json` is written fails safe (neighbour: OVERLAP).** If `news.json` is written and the `news_seen.json` write then fails, the job returns `status: error`; the headlines already in `news.json` may be reported again next run (duplicates are the safe direction; loss is not). Neither file is left half-written (temp file + atomic replace).

**W5 — a corrupt or non-dict `news_seen.json` fails loud (neighbour: MISSING INFORMATION).** A seen file that is not valid JSON, or valid JSON that is not an object, makes the job return `status: error` with a reason naming the file; the file is not overwritten. A MISSING seen file is a first run: `{}`, no error.

**W6 — wrong owner: N/A.** One writer (the GitHub Actions job, or a local run by PROME); the tool has no owner ambiguity.

**W7 — concurrent activity: N/A, justified.** The lane runs as one scheduled job; two concurrent runs are not a supported configuration and were not before the edit. The atomic replace (W4) means a concurrent reader of either file sees the old or the new whole file, never a partial one.

## Tests

`Research-Intake/scripts/test_newsweep_write_order.py` — fixtures only, no network (requests and config monkeypatched). One test per W1–W5.
