#!/usr/bin/env python3
"""Bounded acceptance check for `contract_probe` — fixtures only, NO network.

Exists because an external reviewer showed that `IDENTIFIED` was being returned
with the MATCHED leg 10,000 s stale, and because the prior record claimed the
repair was "TESTED" while no executable test existed. A markdown table recording
that someone ran a check by hand is not a test; this is.

⛔ SCOPE: these are the KNOWN FAILING CASES plus their neighbours, pinned. It is
an acceptance check, not a search for new defects. Run it, do not grow it without
a reason.

    python3 PROME/tools/tests/test_contract_probe_acceptance.py     # rc 0 | 1
"""
import sys
import types
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] /
                       "FORGE" / "tools" / "market-data"))

B = 10_000_000  # fixture epoch; only DIFFERENCES from it are meaningful
STALE = 10_000  # comfortably past contract_probe's STALE_S


def _fake_yf(table):
    class F:
        def __init__(self, sym):
            self.sym = sym

        @property
        def history_metadata(self):
            if self.sym not in table:
                raise Exception("no data")
            px, t = table[self.sym]
            return {"regularMarketPrice": px, "regularMarketTime": t,
                    "instrumentType": "FUTURE", "symbol": self.sym,
                    # Brent's real name: truncated, month cut. Chosen on purpose —
                    # it is the root with no vendor month, i.e. the only one that
                    # DEPENDS on contract_probe, so the cross-check cannot mask a
                    # price-path defect here.
                    "shortName": "Brent Crude Oil Last Day Financ"}
    m = types.ModuleType("yfinance")
    m.Ticker = F
    return m


CASES = [
    # (label, fixture, expected verdict)
    ("matched leg STALE — the reviewer's reproduction",
     {"BZ=F": (106.36, B), "BZX26.NYM": (106.36, B - STALE),
      "BZZ26.NYM": (101.35, B - STALE), "BZF27.NYM": (97.01, B - STALE)},
     "REFUSED-match-on-stale-candidate"),

    # The distinction the fix turns on: a stale NON-matched leg weakens the
    # control set; the match itself was still struck on fresh data.
    ("matched leg FRESH, another leg stale",
     {"BZ=F": (106.36, B), "BZX26.NYM": (106.36, B),
      "BZZ26.NYM": (101.35, B), "BZF27.NYM": (97.01, B - STALE)},
     "IDENTIFIED"),

    ("all legs fresh",
     {"BZ=F": (106.36, B), "BZX26.NYM": (106.36, B),
      "BZZ26.NYM": (101.35, B), "BZF27.NYM": (97.01, B)},
     "IDENTIFIED"),

    # L386's mandatory half: two months quoting the same price cannot distinguish
    # a real resolution from a resolver collapsing months onto one series.
    ("negative control FAILS — duplicate prices",
     {"BZ=F": (106.36, B), "BZX26.NYM": (106.36, B),
      "BZZ26.NYM": (106.36, B), "BZF27.NYM": (97.01, B)},
     "REFUSED-negative-control-failed-duplicate-prices"),

    ("no candidate matches the continuous",
     {"BZ=F": (999.99, B), "BZX26.NYM": (106.36, B),
      "BZZ26.NYM": (101.35, B), "BZF27.NYM": (97.01, B)},
     "REFUSED-no-price-match"),

    ("too few candidates to run a control at all",
     {"BZ=F": (106.36, B), "BZX26.NYM": (106.36, B)},
     "REFUSED-too-few-candidates-for-a-control"),
]


def main():
    failures = []
    for label, table, expected in CASES:
        sys.modules["yfinance"] = _fake_yf(table)
        for mod in ("fetch",):
            sys.modules.pop(mod, None)
        import fetch
        got = fetch.contract_probe("BZ")["verdict"]
        ok = got == expected
        if not ok:
            failures.append((label, expected, got))
        print(f"  {'ok  ' if ok else 'FAIL'} {label:44s} -> {got}")
    print()
    if failures:
        print(f"*** {len(failures)} FAILED ***")
        for label, exp, got in failures:
            print(f"    {label}\n      expected {exp}\n      got      {got}")
        return 1
    print(f"ACCEPTANCE GREEN — {len(CASES)}/{len(CASES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
