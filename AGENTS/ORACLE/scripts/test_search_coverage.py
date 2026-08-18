#!/usr/bin/env python3
"""Regression test for the kalshi.py `search` false-negative defect (fixed 2026-08-18).

No live API calls -- pure fixture. Reproduces the exact 8/17 failure mode (search
for a BOJ market that is genuinely open, gets 0 hits) and proves two things:

  1. The OLD algorithm (paginated /markets, `status=open`) returns ZERO hits for a
     term that is genuinely present, at BOTH its old default page cap (6) and a
     much larger one (20) -- because Kalshi's auto-generated multivariate/
     combinatorial "MVE shard" parlay markets dominate a flat /markets scan badly
     enough that no practical page cap clears them. The old algorithm is kept
     here verbatim (as it shipped through 8/17) so the regression doesn't depend
     on git history.
  2. The NEW algorithm (paginated /events, which is not polluted by the shard
     firehose -- confirmed empirically against the live API on 2026-08-18, see
     kalshi.py cmd_search docstring) finds the same market, and FAILS LOUD
     (explicit "NOT CERTIFIED" text + exit code 2) rather than silently
     returning a partial scan as if it were a clean zero, whenever the page cap
     is hit before the open-event universe is exhausted.

Run: python3 scripts/test_search_coverage.py
"""
import sys, os, io, contextlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kalshi  # noqa: E402

TARGET_TICKER = "KXCBDECISIONJAPAN-26SEP17-H25"
TARGET_TITLE = "Bank Of Japan policy interest rate decision"
QUERY = "bank of japan"

JUNK_PAGES = 20          # far past the old default cap (6); the firehose still wins
JUNK_PER_PAGE = 1000

EVENT_PAGES = 5          # open-event universe in this fixture
EVENT_PER_PAGE = 200
TARGET_EVENT_PAGE = 4    # 0-indexed, last page -- present, but only reachable if not capped early


def fake_get(path, params=None, tries=3):
    """Stand-in for kalshi._get. /markets is an all-junk firehose that never
    contains the target (mirrors the live MVE-shard flood); /events is clean
    and puts the target on its last page."""
    params = params or {}
    cur = params.get("cursor")
    page = int(cur[1:]) if cur else 0

    if path == "/markets":
        mkts = [{"ticker": f"KXMVECROSSCATEGORY-SHARD1-FAKE{page}-{i}",
                 "title": "", "yes_sub_title": "", "subtitle": ""}
                for i in range(JUNK_PER_PAGE)]
        cursor = f"c{page + 1}" if page + 1 < JUNK_PAGES else None
        return {"markets": mkts, "cursor": cursor}

    if path == "/events":
        if page == TARGET_EVENT_PAGE:
            evs = [{
                "title": TARGET_TITLE, "sub_title": "", "event_ticker": "KXCBDECISIONJAPAN",
                "series_ticker": "KXCBDECISIONJAPAN", "category": "World",
                "markets": [{
                    "ticker": TARGET_TICKER, "title": TARGET_TITLE, "yes_sub_title": "H25",
                    "last_price_dollars": "0.7450", "yes_bid_dollars": "0.7400",
                    "yes_ask_dollars": "0.7500", "volume_fp": "31792.0",
                    "open_interest_fp": "21061.0", "close_time": "2026-09-17T00:00:00Z",
                    "status": "active",
                }],
            }]
        else:
            evs = [{"title": "Unrelated event", "sub_title": "", "event_ticker": f"KXNOISE-{page}-{i}",
                     "series_ticker": "KXNOISE", "category": "Misc", "markets": []}
                    for i in range(EVENT_PER_PAGE)]
        cursor = f"c{page + 1}" if page + 1 < EVENT_PAGES else None
        return {"events": evs, "cursor": cursor}

    raise AssertionError(f"unexpected path in fixture: {path}")


def old_cmd_search(query, pages_cap):
    """The algorithm as it shipped through 2026-08-17 -- kept verbatim (module-
    level `_get` calls swapped for the fixture) so this test proves the OLD code
    fails without depending on git history to resurrect it."""
    q = query.lower()
    found, cursor, pages = [], None, 0
    while pages < pages_cap:
        params = {"status": "open", "limit": 1000}
        if cursor:
            params["cursor"] = cursor
        d = fake_get("/markets", params=params)
        for m in d.get("markets", []):
            hay = f"{m.get('title', '')} {m.get('subtitle', '')} {m.get('yes_sub_title', '')} {m.get('ticker', '')}".lower()
            if q in hay:
                found.append(m)
        cursor = d.get("cursor")
        pages += 1
        if not cursor or not d.get("markets"):
            break
    return found, pages


def run_new_search(pages_cap):
    class Args:
        query = QUERY
        n = 12
        pages = pages_cap

    buf = io.StringIO()
    exited = None
    try:
        with contextlib.redirect_stdout(buf):
            kalshi.cmd_search(Args())
    except SystemExit as e:
        exited = e.code
    return buf.getvalue(), exited


def run():
    failures = []

    def check(cond, msg):
        (print(f"PASS: {msg}") if cond else (failures.append(msg), print(f"FAIL: {msg}")))

    # 1. OLD algorithm: false negative at its old default cap.
    old_found, old_pages = old_cmd_search(QUERY, pages_cap=6)
    check(old_found == [], f"old algorithm (6-page cap) finds 0 hits on a term known present "
                            f"({old_pages} pages scanned, all junk) -- reproduces the 8/17 false negative")

    # ... and it doesn't get saved by just raising the cap -- the firehose outlasts it.
    old_found_big, _ = old_cmd_search(QUERY, pages_cap=JUNK_PAGES)
    check(old_found_big == [], f"old algorithm still finds 0 hits even at a {JUNK_PAGES}-page cap "
                                f"(bigger cap alone does not fix it)")

    # 2. NEW algorithm, monkeypatched onto the same fixture: finds it, certifies coverage.
    orig_get = kalshi._get
    kalshi._get = fake_get
    try:
        out, exited = run_new_search(pages_cap=70)
        check(TARGET_TICKER in out, "new algorithm (default 70-page cap) finds the target ticker")
        check("CERTIFIED" in out and "NOT CERTIFIED" not in out,
              "new algorithm reports coverage CERTIFIED when the event universe is exhausted")
        check(exited is None, f"new algorithm exits cleanly (no sys.exit) when coverage is certified, got {exited!r}")

        # 3. Fail-loud path: cap pages one short of the page carrying the target.
        out2, exited2 = run_new_search(pages_cap=TARGET_EVENT_PAGE)
        check(TARGET_TICKER not in out2, "capped run does not reach the target page (test is well-formed)")
        check("NOT CERTIFIED" in out2, "capped run prints an explicit NOT CERTIFIED warning")
        check(exited2 == 2, f"capped run exits 2 (fails loud) instead of returning a silent zero, got {exited2!r}")
    finally:
        kalshi._get = orig_get

    print()
    if failures:
        print(f"{len(failures)} FAILURE(S)")
        sys.exit(1)
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    run()
