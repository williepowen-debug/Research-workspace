COLDREADER · AGENTS/OSPREY/scripts/strike_feed.py (+ strike_feed_config.json, feed/README.md; patch 46d6f6dea) · 15775 B (py; config 2642 B, README 4056 B, wc -c) · 14 claims
Stamp: 2026-10-09 10:30 EDT (`date`). Read-only: fixtures ran on scratch COPIES of pre-patch (46d6f6dea^) and post-patch code under `python3 -I -B`, fetch() monkeypatched, out_dir/ledger in scratch; no network; `git status -- AGENTS/OSPREY/` clean after.
SCORE: 7/14 ✅ · 4 ⚠️ · 3 ❌

❌ 3 Owner's TESTED evidence: "TESTED (the 10/9 run shows the bulletin row PRESENT)" (spawn brief) — the 10/9 row does not exercise the patch. FEED_CANDIDATES_2026-10-09.tsv:3 `2026-10-09	2026-10-04	palaemon	Maritime Security Report: 28th September - 4th October 2026`: a cross-month slug is dated by its LAST day (10/04) ≥ cutoff 2026-09-29, so pre-patch line `if it["date"] and it["date"] < cutoff:` (46d6f6dea^ :199) keeps it too. Fixture `owner_1009_actual`: pre = 1 row, post = 1 row, identical. Owner needs: evidence from a run where the bulletin date < cutoff (only a within-month slug read ≥10 d later qualifies).
❌ 9 strike_feed.py:199 "follow_newest (the dated-window BULLETIN) is NEVER age-filtered" (one item) vs :203 `and not src.get("follow_newest")` keyed on the SOURCE, while :185 `items = [newest]` runs only on body-fetch success — on the :186-187 FETCH_FAILED (newest post) path every index link stays in `items` and none is age-filtered. Fixture X1 (index of 4 bulletins Oct/Oct/Jun/May, body 503): pre = FETCH_FAILED + 2 rows; post = FETCH_FAILED + 4 BULLETIN rows incl. 2026-06-01 and 2026-05-04. Patch-introduced; loud not silent (NOT_READ=1), but it is a stale-row flood the claim does not describe. Owner needs: exemption scoped to the single followed item.
❌ 10 Case (d) stale feed. strike_feed.py:202 states the defect as "a source that yields no row looks like a quiet week"; :227 "FETCH_FAILED / EMPTY_FEED / PARSER_STALE mean the source was NOT read (absent ≠ quiet)"; :242 NOT_READ counts only those three prefixes. Post-patch a bulletin dated 2026-06-01 (4 months stale) emits `BULLETIN — read manually`, summary `palaemon: 1 items, 1 kept`, NOT_READ=0 — the SAME label/count as a fresh bulletin; only the raw pub_date differs (fixture d_stale_months; pre-patch: 0 rows, silent). Not silence any more, but no marker: a dead publisher now reads as a read source. Same mechanism, worse, in X2 (an older "Most read" link precedes the newest in document order; :179 `newest = items[0]`): post emits the June bulletin as the week's BULLETIN and the real 10/05 bulletin is silently discarded at :185. Owner needs: a run-date-vs-bulletin-date staleness marker that counts toward NOT_READ.

⚠️ 6 Commit 46d6f6dea "Fixture: stale bulletin kept, stale RSS filtered; PASSES on patch, FAILS on HEAD" and L309 eval :45 — NO test file exists (`ls AGENTS/OSPREY/scripts/` = strike_feed.py, strike_feed_config.json, __pycache__; no strike_feed test found under AGENTS/PROME/scripts). TESTED is unreproducible by a stranger; this read's own fixture confirms the named reproduction only (claim 4).
⚠️ 7 L309_STRIKE_FEED_EVALUATION_2026-10-08.md:45 "BULLETIN row is absent on 3 of 4 on-host v2 runs (9/19, 9/20, 9/24)" — on host, FEED_CANDIDATES exist only for 09-15, 09-16, 09-29, 10-09; MATCHES_* cannot carry BULLETIN rows by construction (:220 writes only rows with `carry`). The on-host 9/29 file has NO palaemon row at all and is not named. Evidence base for the 3/4 count does not resolve from disk; 9/24 is itself UNKNOWN per the owner — the patch is not shown to cover every observed absence.
⚠️ 11 Case (c) undated slug: row emitted with blank pub_date, `BULLETIN — read manually`, NOT_READ=0 (same pre/post). README:14 says undated rows read `UNDATED`; bulletin rows never do (:210 overwrites match). A stranger cannot tell "date unparseable" from "date parsed" except by a blank cell, and an undated stale bulletin is unmarked forever.
⚠️ 12 strike_feed.py:183-184 appends "[body not machine-readable — client-rendered page; open the URL]" to `summary`, which is never written (COLS :28 has no summary column; grep of fixture output = 0). Fixture X4 (body HTTP 200, empty string = bot-block stub) → row identical to a successful read (`BULLETIN`, NOT_READ=0). Pre-existing, same class.

✅ 1 :11-12 "Fetch failures are ROWS" — (a) 404 and connection-refused → FETCH_FAILED row, NOT_READ=1 (pre=post).
✅ 2 :192-195 EMPTY_FEED for every kind — (b) empty body and 200-with-no-matching-links → EMPTY_FEED row, NOT_READ=1 (pre=post).
✅ 4 :203 patch fixes the named reproduction — fixture owner_withinmonth_10d (21st-27th-september-2026, dated 09-21 < cutoff 09-29): pre 0 rows, post 1 row.
✅ 5 :200 "a within-month bulletin is dated by its FIRST day" — regex :89 verified (21st-27th-sep → 09-21); cross-month dates by LAST day (28th-sep-4th-oct → 10-04).
✅ 8 Config :4-8 palaemon html_index, link_pattern "maritime-security-report", follow_newest true — matches README:36 and the 10/9 row URL.
✅ 13 militarnyi repoint (config :35) — 10/9 run carries 3 militarnyi rows and 0 NOT_READ rows (not network-verified; consistent with README:35).
✅ 14 README:13 BULLETIN = client-rendered dated-window source → read manually; consistent with :208-210.

COUNTEREXAMPLES (fixture · pre-patch · post-patch · expected)
a_404 / a_conn · FETCH_FAILED row · same · ✅ as expected
b_empty / b_nomatch · EMPTY_FEED row · same · ✅
c_undated · BULLETIN row, blank date · same · ⚠️ unmarked
d_stale_months (06-01) · 0 rows SILENT · BULLETIN row, NOT_READ=0, no marker · ❌ expected a staleness marker
X1 body fetch 503 · FETCH_FAILED + 2 rows · FETCH_FAILED + 4 rows incl. May/June · ❌ patch widened exemption to the whole index
X2 older link first in document order · 0 rows silent · stale June row shown as the bulletin, real 10-05 bulletin silently dropped · ❌
X3 slug year typo 2062 · BULLETIN row dated 2062-10-05 · same · no defect (row visible; no future-date guard)
X4 body 200 empty (bot-block) · BULLETIN row · same · ⚠️ marker :184 never reaches output
owner_1009_actual · row present · row present · ❌ the 10/9 evidence cannot discriminate pre from post

POINTERS: 5/5 resolve (strike_feed.py, config, README, L309 eval, FEED_CANDIDATES_2026-10-09.tsv); the commit's fixture has no path → not on disk.
ONE-LINE VERDICT: STILL UNRESOLVED — the patch fixes its named reproduction (within-month bulletin read ≥10 d late now yields a row), but its TESTED evidence (10/9 row) would pass on the unpatched code, there is no committed test, the exemption covers the whole index on a body-fetch failure, and a months-stale or mis-ordered bulletin now reads as a live read with NOT_READ=0.
