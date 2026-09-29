"""Offline CATO review probe; no network, owner writes, or market-data claims.

Run from repository root with .venv/bin/python3 and this file's path.
Tests the reviewed implementation, not an alternative implementation.
"""
import contextlib
import io
from pathlib import Path
import runpy
import sys
import types

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
TARGET = ROOT / "AGENTS/LIQUID/scripts/gate069_legs.py"
DATES = ["2026-09-16", "2026-09-17", "2026-09-18", "2026-09-21",
         "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25"]


def probe(missing_ccc=False, missing_equity=False):
    def fred_fetch(sid, limit=30):
        result = []
        for day in DATES:
            if missing_ccc and sid == "BAMLH0A3HYC" and day == "2026-09-24":
                continue
            value = {"BAMLH0A1HYBB": 1.8, "BAMLH0A3HYC": 8.0,
                     "BAMLH0A0HYM2": 2.7}[sid]
            if sid == "BAMLH0A0HYM2":
                value = {"2026-09-24": 2.73, "2026-09-25": 2.76}.get(day, value)
            result.append({"date": day, "value": str(value)})
        return result

    def download(tickers, **kwargs):
        days = [d for d in DATES if not (missing_equity and d == "2026-09-25")]
        # Two consecutive -10% sessions: neither satisfies the -15% daily leg.
        values = [{"2026-09-24": 90.0, "2026-09-25": 81.0}.get(d, 100.0)
                  for d in days]
        return {"Close": pd.DataFrame({t: values for t in tickers},
                                       index=pd.to_datetime(days))}

    fake_fetch = types.ModuleType("fetch")
    fake_fetch.fred_fetch = fred_fetch
    fake_yf = types.ModuleType("yfinance")
    fake_yf.download = download
    old_modules = {k: sys.modules.get(k) for k in ("fetch", "yfinance")}
    old_argv, old_path = sys.argv[:], sys.path[:]
    try:
        sys.modules.update(fetch=fake_fetch, yfinance=fake_yf)
        sys.argv = [str(TARGET)]
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            runpy.run_path(str(TARGET), run_name="__main__")
        return capture.getvalue()
    finally:
        sys.argv, sys.path = old_argv, old_path
        for key, old in old_modules.items():
            if old is None:
                sys.modules.pop(key, None)
            else:
                sys.modules[key] = old


if __name__ == "__main__":
    for label, kwargs, expected in [
        ("complete daily data", {}, "=> L4 🟢 NOT FIRED"),
        ("missing required equity bar", {"missing_equity": True}, "=> L4 🔴 INSTRUMENT-FAULT"),
        ("unrelated CCC missing 9/24", {"missing_ccc": True}, "=> L4 🔴 FIRED"),
    ]:
        output = probe(**kwargs)
        assert expected in output, (label, output)
        print(label)
        for line in output.splitlines():
            if "=> L4" in line or "HY OAS session change" in line or "CRWV " in line:
                print(line)
    print("Counterexample reproduced: CCC gap turns two -10%/+3bp days into -19%/+6bp.")
