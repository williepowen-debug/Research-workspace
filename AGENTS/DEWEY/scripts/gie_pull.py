#!/usr/bin/env python3
"""
GIE AGSI+ / ALSI+ aggregate puller — European gas storage + LNG terminal layer.

Built 2026-08-27 (Will-approved 2026-08-15, "All approved as recommended", on
DAEDALUS's Europe/gas org recommendation built on DEWEY's DR-4 evidence).
Owner / cadence home: BRENT.  Scope: the AGGREGATE layer only (~10 keyless
calls, stable schema).  `entsog_flows.py` is deliberately NOT built — the
rot-prone point-keyed half; a dated revisit trigger is registered separately.

⚠️ THE UA GATE. GIE returns HTTP 403 with no UA and 200 with a browser UA, and
its own error text misnames the cause (it reads as an API-key problem, which it
is not). Keyless works. An API key is OPTIONAL hardening, not a requirement —
pass --key or set GIE_API_KEY. Verified live 2026-08-27: no-UA -> 403 on both
AGSI+ and ALSI+; browser UA -> 200 on both.
  `[[finding_audit_resolution_path_before_reattempt]]`

Usage:
  python3 gie_pull.py storage                 # EU storage: level, YoY, same-date history
  python3 gie_pull.py storage --years 5       # widen the same-date comparison
  python3 gie_pull.py lng                     # ALSI+: send-out, utilisation, YoY
  python3 gie_pull.py refill --target 90      # what pace is needed to reach a target
  python3 gie_pull.py series --dataset agsi --from 2026-06-01 --to 2026-08-27 --csv
  python3 gie_pull.py storage --country de    # a single country instead of the EU aggregate

Exit codes:  0 ok · 1 source UNAVAILABLE after retry · 2 usage

Units (state them when citing — GIE mixes them):
  gasInStorage / workingGasVolume   TWh
  injection / withdrawal / sendOut  GWh/d
  full / trend                      percent
  consumption                       ANNUAL TWh  <-- NOT a daily flow.
    ⚠️ DR-4 (2026-08-12) built a balance treating `consumption` as a daily GWh
    figure. It is an annual total. The error was caught only because the value
    was IDENTICAL across 2024/25/26. This module never uses it in a flow
    calculation and neither should you.
"""

import sys, os, json, csv, argparse, datetime, urllib.request, urllib.error

AGSI = "https://agsi.gie.eu/api"
ALSI = "https://alsi.gie.eu/api"
BROWSER_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

TRANSIENTS = []          # CHECK_STANDARD §7: a cleared transient is still an EVENT


class GieError(Exception):
    """Source unavailable after the §7 retry — loud, never a silent keep-prior."""


def _req(url, key=None):
    h = {"User-Agent": BROWSER_UA, "Accept": "application/json"}
    if key:
        h["x-key"] = key
    return urllib.request.Request(url, headers=h)


def _fetch(url, key=None, timeout=30):
    """CHECK_STANDARD §7: ONE immediate retry on a transient; a clear is logged
    as an event; a persistent failure is UNAVAILABLE and loud (never silent)."""
    last = None
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(_req(url, key), timeout=timeout) as r:
                body = json.loads(r.read())
            if not body.get("data"):
                # ⚠️ AMBIGUOUS, so do NOT name one cause. GIE returns HTTP 200
                # with an EMPTY data[] for BOTH a wrong parameter (e.g.
                # `country=eu` instead of `continent=eu`) AND a UA it dislikes —
                # verified 2026-08-27, both produce an identical clean 200.
                # A 200-with-no-rows is a FAILURE here, never "no data exists".
                raise ValueError(
                    "HTTP 200 but data[] is EMPTY — ambiguous: either the query "
                    "params are wrong (continent=eu vs country=<iso>) or the UA "
                    "was rejected. This is NOT evidence that no data exists.")
            if attempt == 2:
                TRANSIENTS.append(f"{datetime.date.today()} {url} cleared on retry "
                                  f"(first pass: {last})")
            return body
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code == 403:
                raise GieError(
                    f"HTTP 403 for {url}\n"
                    "  This is the UA GATE, not an API-key problem — GIE's own error\n"
                    "  text misnames it. A browser UA keyless returns 200.") from e
            if e.code < 500:
                raise GieError(f"HTTP {e.code} for {url}") from e
        except Exception as e:                              # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
    raise GieError(f"UNAVAILABLE after retry: {url} ({last})")


def _flush_transients():
    for t in TRANSIENTS:
        sys.stderr.write(f"[TRANSIENT] {t}\n")


def _rows(dataset, country=None, frm=None, to=None, size=None, key=None):
    base = AGSI if dataset == "agsi" else ALSI
    q = [f"country={country}"] if country else ["continent=eu"]
    if frm:
        q.append(f"from={frm}")
    if to:
        q.append(f"to={to}")
    if size:
        q.append(f"size={size}")
    return _fetch(f"{base}?{'&'.join(q)}", key)["data"]


def _f(row, *path):
    """Float out of a GIE row; GIE ships numbers as STRINGS. None if absent/'-'."""
    v = row
    for p in path:
        if not isinstance(v, dict):
            return None
        v = v.get(p)
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------- commands

def cmd_storage(a):
    rows = _rows("agsi", a.country, size=2, key=a.key)
    cur = rows[0]
    day = cur["gasDayStart"]
    full, stock, wgv = _f(cur, "full"), _f(cur, "gasInStorage"), _f(cur, "workingGasVolume")
    inj, wdr = _f(cur, "injection"), _f(cur, "withdrawal")

    label = (a.country or "EU").upper()
    print(f"=== GIE AGSI+ storage — {label} — gas day {day} ===")
    print(f"  full            {full:.2f}%   [percent]")
    print(f"  gasInStorage    {stock:,.1f} TWh of {wgv:,.1f} TWh working volume")
    print(f"  injection       {inj:,.1f} GWh/d      withdrawal {wdr:,.1f} GWh/d")
    print(f"  net             {inj - wdr:+,.1f} GWh/d")

    # Same-DATE comparison across prior years — the measurement DR-4 turned on.
    # Same calendar date, not "same point in the season": the seasonal shape
    # makes any other alignment incomparable.
    print(f"\n  -- same gas day, prior years ({a.years}y) --")
    y0 = int(day[:4])
    hist = []
    for back in range(1, a.years + 1):
        d = f"{y0 - back}{day[4:]}"
        try:
            r = _rows("agsi", a.country, frm=d, to=d, key=a.key)
        except GieError as e:
            print(f"  {d}   UNAVAILABLE ({e})")
            continue
        pv = _f(r[0], "full")
        hist.append((d, pv))
        print(f"  {d}   {pv:6.2f}%   {full - pv:+6.2f}pp vs today")
    if hist:
        lo = min(h[1] for h in hist)
        rank = 1 + sum(1 for h in hist if h[1] < full)
        print(f"\n  >> {full:.2f}% ranks {rank} of {len(hist) + 1} for this date "
              f"(1 = lowest). {a.years}y min was {lo:.2f}%.")
    return 0


def cmd_lng(a):
    rows = _rows("alsi", a.country, size=2, key=a.key)
    cur = rows[0]
    day = cur["gasDayStart"]
    send, dtrs = _f(cur, "sendOut"), _f(cur, "dtrs")
    inv = _f(cur, "inventory", "gwh")
    label = (a.country or "EU").upper()
    print(f"=== GIE ALSI+ LNG terminals — {label} — gas day {day} ===")
    print(f"  sendOut         {send:,.1f} GWh/d")
    print(f"  dtrs (capacity) {dtrs:,.1f} GWh/d")
    if send is not None and dtrs:
        print(f"  utilisation     {send / dtrs * 100:.1f}%   "
              f"({dtrs - send:,.0f} GWh/d of send-out capability IDLE)")
        print("    >> low utilisation with high capacity means the constraint is "
              "CARGOES, not regas.")
    if inv is not None:
        print(f"  inventory       {inv:,.1f} GWh")

    # ⚠️ YoY ON A WINDOW AVERAGE, NOT ON A SINGLE DAY. Send-out is a lumpy
    # cargo-driven flow; a same-day YoY swings tens of percent on arrival timing
    # alone. MEASURED 2026-08-27 on this exact build: the single-day YoY read
    # +0.6% while the 30-day window read -7.9% — an 8.5pp swing, and opposite
    # SIGNS. The point figure would have told the owner "send-out flat YoY".
    # (DR-4's Jun1-Aug11 window measured -20.4%.) A point comparison here can
    # manufacture a "LNG is fine" read out of one well-timed cargo.
    # Identical windows on both sides, and n is printed for each.
    end = datetime.date.fromisoformat(day)
    start = end - datetime.timedelta(days=a.window - 1)

    def _avg(y_off):
        s = start.replace(year=start.year - y_off)
        e = end.replace(year=end.year - y_off)
        rs = _rows("alsi", a.country, frm=s.isoformat(), to=e.isoformat(), key=a.key)
        vals = [v for v in (_f(r, "sendOut") for r in rs) if v is not None]
        return (sum(vals) / len(vals), len(vals)) if vals else (None, 0)

    try:
        cur_avg, n0 = _avg(0)
        pri_avg, n1 = _avg(1)
        print(f"\n  -- sendOut, {a.window}d window ending {day} (identical windows) --")
        print(f"  {start} .. {day}   {cur_avg:,.1f} GWh/d  (n={n0})")
        py = end.replace(year=end.year - 1)
        print(f"  {start.replace(year=start.year-1)} .. {py}   {pri_avg:,.1f} GWh/d  (n={n1})")
        if pri_avg:
            print(f"  >> YoY {(cur_avg - pri_avg) / pri_avg * 100:+.1f}%   "
                  f"(window average — do NOT quote the single-day figure)")
        if n0 != n1:
            print(f"  ⚠️ window lengths differ ({n0} vs {n1} days) — "
                  "the comparison is NOT like-for-like; say so if you cite it.")
    except GieError as e:
        print(f"\n  YoY UNAVAILABLE ({e})")
    return 0


def cmd_refill(a):
    """Refill arithmetic: required pace vs achieved pace. DR-4's deliverable.

    ⚠️ Projects to the PHYSICAL peak window, not to a regulatory date — storage
    turns from injection to withdrawal before Dec 1, so projecting to a
    regulatory deadline overstates the achievable level. DR-4 made exactly this
    error and corrected it."""
    rows = _rows("agsi", a.country, size=a.window + 1, key=a.key)
    cur, old = rows[0], rows[-1]
    day = cur["gasDayStart"]
    full, stock, wgv = _f(cur, "full"), _f(cur, "gasInStorage"), _f(cur, "workingGasVolume")
    pace = (stock - _f(old, "gasInStorage")) / a.window     # TWh/day

    target_twh = wgv * a.target / 100.0
    need = target_twh - stock
    end = datetime.date.fromisoformat(a.peak)
    days = (end - datetime.date.fromisoformat(day)).days

    print(f"=== Refill arithmetic — {(a.country or 'EU').upper()} — from gas day {day} ===")
    print(f"  now             {full:.2f}%  ({stock:,.1f} of {wgv:,.1f} TWh)")
    print(f"  achieved pace   {pace:.3f} TWh/d  (trailing {a.window}d)")
    print(f"  target          {a.target:.0f}%  = {target_twh:,.1f} TWh -> need {need:,.1f} TWh")
    print(f"  window          {days} days to {a.peak} (physical peak, NOT a regulatory date)")
    if days <= 0:
        print("  >> window has passed")
        return 0
    req = need / days
    print(f"  REQUIRED pace   {req:.3f} TWh/d")
    if pace > 0:
        print(f"  >> {req / pace:.2f}x the achieved pace"
              f"{'  — OUT OF REACH on current pace' if req > pace else '  — achievable'}")
    proj = stock + pace * days
    print(f"  projection at achieved pace: {proj:,.1f} TWh = {proj / wgv * 100:.1f}%")
    return 0


def cmd_series(a):
    rows = _rows(a.dataset, a.country, frm=getattr(a, "frm"), to=a.to, size=a.size, key=a.key)
    if a.dataset == "agsi":
        cols = ["gasDayStart", "full", "gasInStorage", "workingGasVolume",
                "injection", "withdrawal", "trend"]
        out = [{c: r.get(c) for c in cols} for r in rows]
    else:
        cols = ["gasDayStart", "sendOut", "dtrs", "inventory_gwh", "dtmi_gwh"]
        out = [{"gasDayStart": r.get("gasDayStart"), "sendOut": r.get("sendOut"),
                "dtrs": r.get("dtrs"), "inventory_gwh": _f(r, "inventory", "gwh"),
                "dtmi_gwh": _f(r, "dtmi", "gwh")} for r in rows]
    if a.csv:
        w = csv.DictWriter(sys.stdout, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    elif a.json:
        print(json.dumps(out, indent=1))
    else:
        print(f"=== {a.dataset.upper()} {(a.country or 'EU').upper()} — {len(out)} gas days ===")
        for r in out:
            print("  " + "  ".join(f"{k}={r[k]}" for k in cols))
    return 0


def main():
    ap = argparse.ArgumentParser(description="GIE AGSI+/ALSI+ aggregate puller (BRENT-owned)")
    ap.add_argument("--country", help="ISO code (de, nl, ...); default = EU aggregate")
    ap.add_argument("--key", default=os.environ.get("GIE_API_KEY"),
                    help="optional GIE API key (keyless works; this is hardening)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("storage", help="EU storage level + same-date prior years")
    s.add_argument("--years", type=int, default=5)

    l = sub.add_parser("lng", help="ALSI+ send-out, utilisation, windowed YoY")
    l.add_argument("--window", type=int, default=30,
                   help="days for the send-out YoY average (default 30; a "
                        "single-day YoY on a cargo-driven flow is noise)")

    r = sub.add_parser("refill", help="required vs achieved refill pace")
    r.add_argument("--target", type=float, default=90.0, help="percent full (default 90)")
    r.add_argument("--peak", default=None, help="physical peak date YYYY-MM-DD (default Nov 6)")
    r.add_argument("--window", type=int, default=14, help="trailing days for pace (default 14)")

    q = sub.add_parser("series", help="raw history")
    q.add_argument("--dataset", choices=("agsi", "alsi"), default="agsi")
    q.add_argument("--from", dest="frm")
    q.add_argument("--to")
    q.add_argument("--size", type=int)
    q.add_argument("--csv", action="store_true")
    q.add_argument("--json", action="store_true")

    a = ap.parse_args()
    if a.cmd == "refill" and not a.peak:
        a.peak = f"{datetime.date.today().year}-11-06"

    try:
        rc = {"storage": cmd_storage, "lng": cmd_lng,
              "refill": cmd_refill, "series": cmd_series}[a.cmd](a)
    except GieError as e:
        _flush_transients()
        sys.stderr.write(f"GIE UNAVAILABLE: {e}\n"
                         "  This is a SOURCE failure, not a reading. Do not record a "
                         "level, and do not keep the prior value silently.\n")
        return 1
    _flush_transients()
    return rc


if __name__ == "__main__":
    sys.exit(main() or 0)
