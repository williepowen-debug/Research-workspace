#!/usr/bin/env python3
"""WAL market tracker — appends dated positioning/market readings to workbook/MARKET_TRACKER.tsv.

Built 2026-10-30 (Will: "we should track metrics like this", after the short-interest question).
Series (long format, one row per reading):
  FINRA consolidated short interest (semi-monthly): short_interest_shares, avg_daily_volume, days_to_cover,
    short_pct_shares_out (shares short / the latest SEC cover-page count dated on or before the settlement).
  SEC XBRL dei:EntityCommonStockSharesOutstanding: shares_outstanding (the denominator, never hard-coded).
  Weekly snapshot (latest completed session, at most one per 7 days unless --snapshot): close_WAL, close_KRE,
    close_WAL-PA, realized_vol_20d, realized_vol_60d, beta_KRE_60d, spot_vs_ev_pct (EV read from THESIS.md).

Dry run by default (prints the rows it would add); --write appends them and restamps the two-clock header.
Run with the repo venv from the repo root:  .venv/bin/python3 AGENTS/WAL/scripts/market_tracker.py [--write]
Scope: WAL single-name figures only. Cohort/KRE judgments are REGINALD's; implied vol is TERRY's.
"""
import argparse
import json
import math
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from boot import FINRA_URL, thesis_ev  # noqa: E402

WAL_DIR = Path(__file__).resolve().parents[1]
TRACKER = WAL_DIR / "workbook" / "MARKET_TRACKER.tsv"
COLS = ["Date", "Metric", "Value", "Unit", "Basis", "Source", "Recorded"]
XBRL_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK0001212545/dei/EntityCommonStockSharesOutstanding.json"
UA = "WAL research williepowen@gmail.com"
FINRA_START = "2025-01-01"
SNAPSHOT_EVERY_DAYS = 7


def read_rows(text):
    """Data rows as dicts; '#' header lines and the column line are skipped."""
    rows = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#") or line.startswith("Date\t"):
            continue
        rows.append(dict(zip(COLS, line.split("\t"))))
    return rows


def dates_for(rows, metric):
    return {r["Date"] for r in rows if r["Metric"] == metric}


def last_date(rows, metric):
    d = dates_for(rows, metric)
    return max(d) if d else None


def denominator(shares, on):
    """Latest (date, count) cover reading dated on or before `on` (ISO strings), else None."""
    prior = [s for s in shares if s[0] <= on]
    return max(prior) if prior else None


def realized_vol(closes, n):
    r = [math.log(b / a) for a, b in zip(closes[-n - 1:-1], closes[-n:])]
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / (len(r) - 1)) * math.sqrt(252)


def beta(y, x, n):
    ry = [math.log(b / a) for a, b in zip(y[-n - 1:-1], y[-n:])]
    rx = [math.log(b / a) for a, b in zip(x[-n - 1:-1], x[-n:])]
    my, mx = sum(ry) / n, sum(rx) / n
    return sum((a - my) * (b - mx) for a, b in zip(ry, rx)) / sum((b - mx) ** 2 for b in rx)


def http_json(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_shares():
    d = http_json(XBRL_URL)
    out = []
    for unit in d["units"].values():
        for x in unit:
            out.append((x["end"], int(x["val"]), f"SEC {x['form']} cover acc {x['accn']} (XBRL dei)"))
    return sorted(set(out))


def fetch_finra():
    q = {"limit": 500, "compareFilters": [{"fieldName": "symbolCode", "fieldValue": "WAL", "compareType": "EQUAL"}],
         "dateRangeFilters": [{"fieldName": "settlementDate", "startDate": FINRA_START,
                               "endDate": date.today().isoformat()}]}
    rows = http_json(FINRA_URL, json.dumps(q).encode(), {"Content-Type": "application/json", "Accept": "application/json"})
    return sorted(rows, key=lambda r: r["settlementDate"])


def session_closes():
    """Aligned daily closes for WAL/KRE/WAL-PA over ~6 months, dropping today's bar before 16:15 local (ET box)."""
    import yfinance as yf
    frames = {t: yf.Ticker(t).history(period="6mo")["Close"] for t in ("WAL", "KRE", "WAL-PA")}
    days = sorted(set.intersection(*(set(f.index.date) for f in frames.values())))
    now = datetime.now()
    if days and days[-1] == now.date() and (now.hour, now.minute) < (16, 15):
        days = days[:-1]
    series = {t: [float(f[f.index.date == d].iloc[-1]) for d in days] for t, f in frames.items()}
    return days, series


def build(rows, stamp, force_snapshot, offline=False):
    new = []
    have_shares = dates_for(rows, "shares_outstanding")
    have_si = dates_for(rows, "short_interest_shares")
    shares = fetch_shares()
    for d, v, src in shares:
        if d not in have_shares:
            new.append([d, "shares_outstanding", str(v), "shares", "cover-page count as of this date", src, stamp])
    pairs = [(d, v) for d, v, _ in shares]
    for r in fetch_finra():
        d = r["settlementDate"]
        if d in have_si:
            continue
        src = "FINRA consolidatedShortInterest API" + (f" (revisionFlag {r['revisionFlag']})" if r.get("revisionFlag") else "")
        si = int(r["currentShortPositionQuantity"])
        new.append([d, "short_interest_shares", str(si), "shares", "settlement date", src, stamp])
        new.append([d, "avg_daily_volume", str(r.get("averageDailyVolumeQuantity")), "shares/day", "FINRA period average", src, stamp])
        new.append([d, "days_to_cover", str(r.get("daysToCoverQuantity")), "days", "FINRA: short / average daily volume", src, stamp])
        den = denominator(pairs, d)
        if den:
            new.append([d, "short_pct_shares_out", f"{si / den[1] * 100:.2f}", "%",
                        f"short / {den[1]:,} cover shares as of {den[0]}", src + " + SEC XBRL cover count", stamp])
    days, s = session_closes()
    if days:
        sess = days[-1].isoformat()
        last_snap = last_date(rows, "close_WAL")
        due = force_snapshot or last_snap is None or (days[-1] - date.fromisoformat(last_snap)).days >= SNAPSHOT_EVERY_DAYS
        if due and sess not in dates_for(rows, "close_WAL"):
            ysrc = "yfinance daily bars (vendor, not exchange-certified)"
            ev = thesis_ev((WAL_DIR / "THESIS.md").read_text(encoding="utf-8"))
            w, k, p = s["WAL"], s["KRE"], s["WAL-PA"]
            new += [[sess, "close_WAL", f"{w[-1]:.2f}", "$", "session close", ysrc, stamp],
                    [sess, "close_KRE", f"{k[-1]:.2f}", "$", "session close", ysrc, stamp],
                    [sess, "close_WAL-PA", f"{p[-1]:.2f}", "$", "session close; $25 liquidation preference", ysrc, stamp],
                    [sess, "realized_vol_20d", f"{realized_vol(w, 20) * 100:.1f}", "% annualized", "stdev of 20 daily log returns x sqrt(252)", ysrc, stamp],
                    [sess, "realized_vol_60d", f"{realized_vol(w, 60) * 100:.1f}", "% annualized", "stdev of 60 daily log returns x sqrt(252)", ysrc, stamp],
                    [sess, "beta_KRE_60d", f"{beta(w, k, 60):.2f}", "x", "60 daily log returns, WAL on KRE", ysrc, stamp]]
            if ev:
                new.append([sess, "spot_vs_ev_pct", f"{(w[-1] / ev - 1) * 100:+.2f}", "%", f"close vs EV ${ev:.2f} (THESIS.md at run time)", ysrc + " + THESIS.md", stamp])
    return new


def restamp(text, today):
    note = f"Last real data refresh: {today} (scripts/market_tracker.py --write)"
    return re.sub(r"Last real data refresh: [^|\n]*", note + " ", text, count=1)


def main():
    ap = argparse.ArgumentParser(description="Append new WAL market/positioning readings (dry run unless --write).")
    ap.add_argument("--write", action="store_true", help="append the new rows and restamp the header")
    ap.add_argument("--snapshot", action="store_true", help="add a price snapshot even if the last one is under 7 days old")
    args = ap.parse_args()
    text = TRACKER.read_text(encoding="utf-8")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new = build(read_rows(text), stamp, args.snapshot)
    for r in new:
        print("  + " + " | ".join(r[:5]))
    print(f"{len(new)} new row(s){'' if args.write else ' (dry run — add --write to append)'}")
    if args.write and new:
        body = text if text.endswith("\n") else text + "\n"
        body = restamp(body, date.today().isoformat()) + "\n".join("\t".join(r) for r in sorted(new)) + "\n"
        TRACKER.write_text(body, encoding="utf-8")
        print(f"Wrote {TRACKER.relative_to(WAL_DIR.parents[1])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
