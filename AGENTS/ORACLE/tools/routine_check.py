#!/usr/bin/env python3
"""ORACLE routine ran-check (WQ-527 C, DOCKET L847) — run at boot.

For each US weekday (ET) from the routine's install date through today, says plainly whether a
read exists (any ODDS_LOG row stamped on that ET date, routine or live session) and whether the
routine itself ran (a ROUTINE_RUNS.tsv row). A weekday with no read prints `NOT READ` — the usual
cause is a machine switch or a powered-off/idle box (cron runs only while WSL is up).

rc 0 = every weekday read · rc 1 = at least one weekday NOT READ · rc 2 = cannot evaluate.
Market holidays are listed like any weekday; O3 treats a holiday pull as context, not a read.
"""
import csv, datetime as dt, os, socket, sys
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
HERE = os.path.dirname(os.path.abspath(__file__))
WB = os.path.join(HERE, "..", "workbook")
ODDS = os.path.join(WB, "ODDS_LOG.tsv")
RUNS = os.path.join(WB, "ROUTINE_RUNS.tsv")
INSTALLED = dt.date(2026, 10, 29)  # first weekday the routine could run


def et_date(stamp):
    t = dt.datetime.strptime(stamp, "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
    return t.astimezone(ET).date()


def main():
    if not os.path.exists(ODDS):
        print("ROUTINE-CHECK CANNOT-EVALUATE: no ODDS_LOG"); return 2
    read_days = set()
    with open(ODDS) as fh:
        for line in fh:
            if line[:2] == "20":
                read_days.add(et_date(line.split("\t", 1)[0]))
    runs = {}
    if os.path.exists(RUNS):
        with open(RUNS, newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                runs[dt.date.fromisoformat(r["et_date"])] = r
    today = dt.datetime.now(ET).date()
    day, missed = INSTALLED, []
    print(f"ORACLE routine ran-check — today {today} ET, this box {socket.gethostname()}")
    while day <= today:
        if day.weekday() < 5:
            r = runs.get(day)
            src = f"routine {r['status']} on {r['host']}" if r else "live session (no routine row)"
            if day in read_days:
                print(f"  {day} {day:%a}  READ      {src}")
            elif day == today:
                print(f"  {day} {day:%a}  PENDING   no read yet today")
            else:
                print(f"  {day} {day:%a}  NOT READ  routine did not run and no session pulled")
                missed.append(day)
        day += dt.timedelta(days=1)
    if missed:
        print(f"ROUTINE-CHECK MISSED {len(missed)}: " + ", ".join(map(str, missed))
              + " — check the box was on and `crontab -l` holds the ORACLE line (SCHEDULED_RUNS.md)")
        return 1
    print("ROUTINE-CHECK OK"); return 0


# ---------------------------------------------------------------------------------------------
# Band-touch scan (added 2026-11-26, PROME prome-80 ask; extends this boot check, adds no job,
# changes no ruling: the routine still pulls and never grades, WQ-527 C). READ-ONLY: it prints
# what a grader would look at since the last graded read; ORACLE still grades and records.
# Letters are the VX.tsv rows; if a row's letter changes, change it here in the same edit.
#   VX-ORC-04  WTI $110 month leg, read >= 40.0 (Alert arming) / >= 60.0 (Critical arming)
#   VX-ORC-06  AI bubble burst, read > 30 (Watch) / > 40 (Alert)
#   VX-ORC-12  Dec FOMC +25 leg, read < 50.0 (de-alert leg; Alert is the held state)
#   VX-ORC-07  any tracked market, two log rows <= 48h apart, |move| > 10 (Alert) / > 20 (Critical)
# A read = the first ODDS_LOG row of an ET business day (NYSE calendar), both legs liq >= $5K.
# 48h pairs: overlapping pairs on one slug collapse to the largest (episodes, not sub-pairs).
# ---------------------------------------------------------------------------------------------
VX = os.path.join(WB, "VX.tsv")
LIQ_MIN = 5000.0
NYSE_CLOSED = {dt.date(2026, m, d) for m, d in
               [(1, 1), (1, 19), (2, 16), (4, 3), (5, 25), (6, 19), (7, 3), (9, 7), (11, 26), (12, 25)]}
READ_BANDS = [  # (row, slug test, [(test, label)])
    ("VX-ORC-04", lambda s: s.startswith("will-wti-reach-110-in-"),
     [(lambda p: p >= 60.0, "Critical-arming read >= 60.0"), (lambda p: p >= 40.0, "Alert-arming read >= 40.0")]),
    ("VX-ORC-06", lambda s: s == "ai-industry-downturn-by-december-31-2026-857",
     [(lambda p: p > 40.0, "Alert read > 40"), (lambda p: p > 30.0, "Watch read > 30")]),
    ("VX-ORC-12", lambda s: s.startswith("will-the-fed-increase-interest-rates-by-25-bps-after-the-december-2026"),
     [(lambda p: p < 50.0, "de-alert leg read < 50.0")]),
]
GRADED_ROWS = ("VX-ORC-04", "VX-ORC-06", "VX-ORC-07", "VX-ORC-12")


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def last_graded_date():
    """Oldest `Updated` date among the graded rows = the earliest point not yet graded by ORACLE."""
    dates = []
    with open(VX, newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["ID"] in GRADED_ROWS:
                dates.append(dt.date.fromisoformat(r["Updated"][:10]))
    return min(dates) if dates else None


def band_scan(since):
    rows = []
    with open(ODDS, newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            p, liq = _f(r["yes_prob"]), _f(r["liquidity"])
            if p is None:
                continue
            t = dt.datetime.strptime(r["ts"], "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
            rows.append((t, r["slug"], r["label"], p * 100, liq))
    start = dt.datetime.combine(since, dt.time(), ET)
    touches = []
    # Read bands: first row per slug per ET business day.
    seen = set()
    for t, slug, label, p, liq in sorted(rows):
        d = t.astimezone(ET).date()
        if (slug, d) in seen:
            continue
        seen.add((slug, d))
        if t < start or d.weekday() >= 5 or d in NYSE_CLOSED:
            continue
        for row, test, bands in READ_BANDS:
            if test(slug):
                for hit, name in bands:
                    if hit(p):
                        thin = "" if (liq or 0) >= LIQ_MIN else f" ⚠️ THIN liq ${liq or 0:,.0f}: not a qualified read"
                        touches.append((t, f"{row}  {d} read {p:.2f} ({slug[:48]}) — {name}{thin}"))
                        break
    # 48h pairs (VX-ORC-07), both legs liq >= $5K, end inside the window.
    by = {}
    for t, slug, label, p, liq in rows:
        if liq is not None and liq >= LIQ_MIN:
            by.setdefault(slug, []).append((t, p, liq, label))
    for slug, L in by.items():
        L.sort()
        cands = []
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                if L[j][0] - L[i][0] > dt.timedelta(hours=48):
                    break
                mv = L[j][1] - L[i][1]
                if abs(mv) > 10.0 and L[j][0] >= start:
                    cands.append((abs(mv), L[i], L[j], mv))
        kept = []
        for c in sorted(cands, key=lambda c: -c[0]):
            if all(not (c[1][0] < k[2][0] and k[1][0] < c[2][0]) for k in kept):
                kept.append(c)
        for _, a, b, mv in kept:
            band = "Critical >20" if abs(mv) > 20 else "Alert >10"
            touches.append((b[0], f"VX-ORC-07  {a[0]:%m-%dT%H:%MZ} -> {b[0]:%m-%dT%H:%MZ}  {mv:+.1f}pp  "
                                  f"{a[1]:.1f} -> {b[1]:.1f}  min liq ${min(a[2], b[2]):,.0f}  {a[3][:40]} — {band}"))
    return sorted(touches)


def bands_main(argv):
    since = None
    if "--since" in argv:
        since = dt.date.fromisoformat(argv[argv.index("--since") + 1])
    elif os.path.exists(VX):
        since = last_graded_date()
    if since is None:
        print("BAND-SCAN CANNOT-EVALUATE: no --since and no VX.tsv Updated dates"); return
    touches = band_scan(since)
    print(f"\nORACLE band-touch scan (read-only) — since {since} ET (oldest Updated on "
          f"{', '.join(GRADED_ROWS)}{'; --since given' if '--since' in argv else ''})")
    for _, line in touches:
        print("  " + line)
    if touches:
        print(f"BAND-SCAN {len(touches)} TOUCH(ES) since {since}: grade each on its VX row, route per the "
              "signal table (48h >10pp -> PROME triage), then bump the row's Updated.")
    else:
        print(f"BAND-SCAN 0 touches since {since}.")


if __name__ == "__main__":
    rc = main()
    if "--no-bands" not in sys.argv:
        try:
            bands_main(sys.argv)
        except Exception as e:  # the ran-check's rc must not depend on the scan
            print(f"BAND-SCAN ERROR {type(e).__name__}: {e} — the ran-check result above stands")
    sys.exit(rc)
