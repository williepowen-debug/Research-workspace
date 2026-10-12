"""Save exact common closes for SHADE's two windows; never grade the HY run.

Run from repo root with .venv/bin/python. Supply LIQUID's dated anchor/ref.
The owner grades the canonical letter, including its effective-date restriction.
No intraday substitution, window search, or overwrite of a prior snapshot.
"""
import argparse
from datetime import date, datetime, timedelta
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import yfinance as yf

WRAPPERS = ("ARCC", "FSK", "OBDC", "BIZD")
MANAGERS = ("APO", "ARES")


def summarize(prices, start, end, field):
    returns = {
        ticker: (prices[ticker][end][field] / prices[ticker][start][field] - 1) * 100
        for ticker in WRAPPERS + MANAGERS
    }
    w = sum(returns[t] for t in WRAPPERS) / len(WRAPPERS)
    m = sum(returns[t] for t in MANAGERS) / len(MANAGERS)
    if w < 0 and m < 0:
        pattern = "both_down_wrappers_more" if w < m else "both_down_managers_at_least_as_much"
    elif w < 0 <= m:
        pattern = "wrappers_down_managers_nonnegative"
    else:
        pattern = "wrappers_not_down"
    return {"per_name_pct": returns, "wrappers_pct": w, "managers_pct": m,
            "wrapper_minus_manager_pp": w - m, "cohort_pattern": pattern}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--anchor", required=True, type=date.fromisoformat)
    p.add_argument("--end", required=True, type=date.fromisoformat)
    p.add_argument("--previous-end", required=True, type=date.fromisoformat)
    p.add_argument("--owner-ref", required=True)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    now = datetime.now(ZoneInfo("America/New_York"))
    if args.output.exists():
        p.error("output already exists; preserve prior snapshots")
    if not args.anchor < args.end or not args.previous_end < args.end:
        p.error("both window starts must precede the endpoint")
    if args.end > now.date() or (args.end == now.date() and now.hour < 16):
        p.error("endpoint is not yet a completed regular-session close")
    dates = {str(args.anchor), str(args.previous_end), str(args.end)}
    prices, errors = {}, {}
    for ticker in WRAPPERS + MANAGERS:
        try:
            history = yf.Ticker(ticker).history(
                start=str(min(args.anchor, args.previous_end)),
                end=str(args.end + timedelta(days=1)), auto_adjust=False,
                raise_errors=True,
            )
            rows = {}
            for index, row in history.iterrows():
                d = str(index.date())
                if d in dates:
                    raw, adj = float(row["Close"]), float(row["Adj Close"])
                    if not (raw > 0 and adj > 0):
                        raise ValueError("missing/nonpositive raw or adjusted close")
                    rows[d] = {"raw_close": raw, "adjusted_close": adj,
                               "dividend": float(row["Dividends"])}
            if set(rows) != dates:
                raise ValueError("missing exact date(s): " + ", ".join(sorted(dates - set(rows))))
            prices[ticker] = rows
        except Exception as exc:
            errors[ticker] = str(exc)
    result = {
        "retrieved_at": now.isoformat(timespec="seconds"),
        "completed_at": datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds"),
        "source": "Yahoo Finance via yfinance; vendor vintage served at retrieval",
        "source_urls": {t: f"https://finance.yahoo.com/quote/{t}/history/" for t in WRAPPERS + MANAGERS},
        "owner_anchor_ref": args.owner_ref,
        "primary_window": [str(args.anchor), str(args.end)],
        "since_last_read_window": [str(args.previous_end), str(args.end)],
        "basis": "RAW split-adjusted close; ADJ vendor dividend-adjusted close beside it",
        "prices": prices, "errors": errors,
        "scope": "Close arithmetic only. No HY series/count and no trigger-fire grade.",
    }
    if not errors:
        result["windows"] = {
            label: {basis: summarize(prices, str(start), str(args.end), field)
                    for basis, field in (("RAW", "raw_close"), ("ADJ", "adjusted_close"))}
            for label, start in (("primary", args.anchor), ("since_last_read", args.previous_end))
        }
    with args.output.open("x") as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("retrieved_at", "completed_at", "errors")}))
    if errors:
        raise SystemExit(2)
    print(json.dumps(result["windows"], indent=2))


if __name__ == "__main__":
    main()
