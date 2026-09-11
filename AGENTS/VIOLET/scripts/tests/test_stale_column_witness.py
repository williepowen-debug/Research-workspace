#!/usr/bin/env python3
"""Regression test for the `thresholds.py` stale-column guard's WITNESS.

WHY THIS EXISTS (KB-VIO-283)
-----------------------------
The guard answers one question — "does this quote belong to TODAY?" — and it
answered it from a 5-MINUTE INTRADAY bar feed (`last_bar_et_date`). ^SKEW
publishes EOD ONLY and therefore has no same-day intraday bar AT ANY HOUR, so
the witness returned T-1 for ^SKEW on every post-close run while returning T
correctly for the five series that do quote intraday.

On 2026-09-11 at 17:31 ET the guard suppressed a REAL ^SKEW close of 154.49 and
printed "the quote belonged to a PRIOR session". That was false — the 9/10 close
was 147.02, so the value was neither a forward-fill nor a prior quote. It was a
genuine print the witness could not see. 154.49 is above the 150 FT-10 line on a
sustain-4 counter, three sessions before FOMC.

The fix makes CBOE's `last_trade_time` — the publisher's own staleness signal —
the witness, and takes the VALUE from the same call so a CBOE timestamp is never
used to certify a yfinance value.

⚠️ THE RISK THIS TEST EXISTS TO BOUND
--------------------------------------
The fix makes a guard fire LESS. That is exactly how a guard gets loosened into
uselessness — trading loud-and-safe for silent-and-certifying
([[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]).
So the property under test is NOT "it stopped blanking ^SKEW". It is that the
guard STILL suppresses a genuinely stale pre-open quote (B, C) — the original
KB-VIO-139 defect that nearly false-tripped a live exit guard — while ceasing to
suppress a real post-close print (A). And that it still NEVER deletes a value it
merely cannot verify (E), the fail-safe direction.

FROZEN AND OFFLINE: the clock, the publisher and the mirror are all fixtures.
No network, no live ledger, no other agent's directory. Cannot rot.

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/tests/test_stale_column_witness.py
"""
from __future__ import annotations

import sys
import types
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import thresholds as th  # noqa: E402

ET = ZoneInfo("America/New_York")
SKEW_9_11, SKEW_9_10 = 154.49, 147.02   # the real pair that exposed this
VIX_9_11 = 15.84


class FrozenDT(datetime):
    """Freezes only `now()`; fromisoformat and the rest stay real."""
    _now: datetime = datetime(2026, 9, 11, 17, 31, tzinfo=ET)

    @classmethod
    def now(cls, tz=None):
        return cls._now.astimezone(tz) if tz else cls._now


class R:
    def __init__(self) -> None:
        self.ok, self.n = True, 0

    def check(self, label: str, got, want) -> None:
        self.n += 1
        good = got == want
        print(("  ✅ " if good else "  ❌ ") + f"{label}  [got {got!r}, want {want!r}]")
        self.ok = self.ok and good


def fake_yf(price_by_sym: dict) -> types.ModuleType:
    """Stand-in yfinance module: fetch_spot imports it INSIDE the function."""
    m = types.ModuleType("yfinance")

    class _T:
        def __init__(self, sym):
            self.fast_info = {"lastPrice": price_by_sym[sym]}

    m.Ticker = _T
    return m


def run(tickers: dict, quotes: dict, *, bar_dates=None, yf_prices=None, when=None):
    """Drive fetch_spot against fixture publisher + fixture mirror."""
    th.datetime = FrozenDT
    if when:
        FrozenDT._now = when
    th.TICKERS = tickers
    th.cboe_quote = lambda sym, timeout=12.0: quotes.get(sym)
    th.last_bar_et_date = lambda sym: (bar_dates or {}).get(sym)
    sys.modules["yfinance"] = fake_yf(yf_prices or {})
    try:
        return th.fetch_spot()
    finally:
        FrozenDT._now = datetime(2026, 9, 11, 17, 31, tzinfo=ET)


def main() -> int:
    r = R()
    real_tickers, real_cboe, real_bar, real_dt = (
        th.TICKERS, th.cboe_quote, th.last_bar_et_date, th.datetime)

    Q = lambda v, d: {"value": v, "et_date": d, "prev_close": None}  # noqa: E731

    print("\n--- A. POST-CLOSE, EOD-ONLY series: real print must SURVIVE (the 9/11 regression) ---")
    out = run({"skew": "^SKEW"}, {"^SKEW": Q(SKEW_9_11, date(2026, 9, 11))})
    r.check("skew value kept", out["skew"], SKEW_9_11)
    r.check("not flagged stale", out.get("skew_stale"), None)
    r.check("sourced from the publisher", out["skew_src"], "CBOE")

    print("\n--- B. PRE-OPEN, EOD-ONLY series: stale quote must STILL be suppressed (KB-VIO-139) ---")
    out = run({"skew": "^SKEW"}, {"^SKEW": Q(SKEW_9_10, date(2026, 9, 10))},
              when=datetime(2026, 9, 11, 8, 5, tzinfo=ET))
    r.check("value NULLed", out["skew"], None)
    r.check("flagged stale", out.get("skew_stale"), True)
    r.check("suppressed value reported, not lost", out.get("skew_suppressed_value"), SKEW_9_10)
    r.check("witnessed date carried for the message", out.get("skew_stale_date"), "2026-09-10")

    print("\n--- C. PRE-OPEN, INTRADAY series: ^VIX does quote pre-open, must be KEPT ---")
    out = run({"vix": "^VIX"}, {"^VIX": Q(VIX_9_11, date(2026, 9, 11))},
              when=datetime(2026, 9, 11, 8, 5, tzinfo=ET))
    r.check("vix kept pre-open", out["vix"], VIX_9_11)
    r.check("not flagged stale", out.get("vix_stale"), None)

    print("\n--- D. publisher UNREACHABLE -> falls back to the mirror, still date-checked ---")
    out = run({"skew": "^SKEW"}, {}, bar_dates={"^SKEW": date(2026, 9, 11)},
              yf_prices={"^SKEW": SKEW_9_11})
    r.check("fell back to yfinance", out["skew_src"], "yfinance")
    r.check("value kept", out["skew"], SKEW_9_11)
    out = run({"skew": "^SKEW"}, {}, bar_dates={"^SKEW": date(2026, 9, 10)},
              yf_prices={"^SKEW": SKEW_9_10})
    r.check("fallback still suppresses a stale mirror quote", out["skew"], None)

    print("\n--- E. FAIL-SAFE: unverifiable is NOT stale — a value must never be deleted ---")
    out = run({"skew": "^SKEW"}, {}, bar_dates={}, yf_prices={"^SKEW": SKEW_9_11})
    r.check("value KEPT when date unverifiable", out["skew"], SKEW_9_11)
    r.check("flagged unverified", out.get("skew_unverified"), True)
    r.check("NOT flagged stale", out.get("skew_stale"), None)

    print("\n--- F. ABLATION: the OLD witness is what suppressed the real print ---")
    # The pre-fix guard used last_bar_et_date alone. ^SKEW is EOD-only, so its
    # intraday feed still reads 9/10 at 17:31 on 9/11 — a guaranteed miss.
    out = run({"skew": "^SKEW"}, {}, bar_dates={"^SKEW": date(2026, 9, 10)},
              yf_prices={"^SKEW": SKEW_9_11})
    r.check("old-witness path NULLs the real 154.49", out["skew"], None)
    r.check("...and would have reported it as stale", out.get("skew_stale"), True)
    r.check("new witness on the SAME session keeps it",
            run({"skew": "^SKEW"}, {"^SKEW": Q(SKEW_9_11, date(2026, 9, 11))})["skew"], SKEW_9_11)

    print("\n--- G. cboe_quote fails CLOSED to None (never a bogus date) on bad payloads ---")
    th.cboe_quote = real_cboe
    import urllib.request as u
    real_open = u.urlopen

    class _Resp:
        def __init__(self, b): self.b = b
        def read(self): return self.b
        def __enter__(self): return self
        def __exit__(self, *a): return False

    cases = [
        ("no last_trade_time", b'{"data":{"close":154.49}}'),
        ("close is 0 (index has not printed)",
         b'{"data":{"close":0,"last_trade_time":"2026-09-11T17:00:47"}}'),
        ("close missing", b'{"data":{"last_trade_time":"2026-09-11T17:00:47"}}'),
        ("unparseable timestamp",
         b'{"data":{"close":154.49,"last_trade_time":"not-a-time"}}'),
        ("malformed json", b'{{{'),
        ("no data key", b'{}'),
    ]
    for label, body in cases:
        u.urlopen = lambda *a, **k: _Resp(body)
        r.check(f"{label} -> None", th.cboe_quote("^SKEW"), None)
    u.urlopen = lambda *a, **k: _Resp(
        b'{"data":{"close":154.49,"prev_day_close":147.02,'
        b'"last_trade_time":"2026-09-11T17:00:47"}}')
    got = th.cboe_quote("^SKEW")
    r.check("good payload parses value", got and got["value"], SKEW_9_11)
    r.check("good payload parses ET date", got and got["et_date"], date(2026, 9, 11))
    r.check("good payload carries prev_close", got and got["prev_close"], SKEW_9_10)
    u.urlopen = real_open

    th.TICKERS, th.cboe_quote, th.last_bar_et_date, th.datetime = (
        real_tickers, real_cboe, real_bar, real_dt)
    print(f"\n{'ALL ' + str(r.n) + ' CHECKS PASSED' if r.ok else 'FAILED'}")
    return 0 if r.ok else 1


if __name__ == "__main__":
    sys.exit(main())
