#!/usr/bin/env python3
"""dtcc_cds_probe.py — read single-name CDS prints from the DTCC Public Price Dissemination
(SEC-regime) cumulative credit reports, $0, no login. Born 2026-09-26 (LIQUID, WQ-298 line 4 /
GATE-LIQ-069 leg 2 free-path check).

    python3 dtcc_cds_probe.py COREWEAVE 2026-09-23 2026-09-24 [...]

Source: https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_YYYY_MM_DD.zip
(one file per business day, published ~20:15 ET; history reachable back to at least 2025-12-15).
Index CDS (CDX.NA.HY) is CFTC-regime: same path with cftc/CFTC_.

⚠️ PROBE, NOT A GRADED INSTRUMENT. HY names trade on a fixed coupon (CoreWeave 500bp) with an
UPFRONT (field 'Other payment amount', type UFRO); the par spread printed here is a FLAT-HAZARD
APPROXIMATION (r=4% flat, R=40%, quarterly premium, no accrual-on-default, upfront taken as
disseminated incl. any accrued) — NOT the ISDA Standard Model. Good to tens of bp, not to one.
Notional '5,000,000+' is a disseminated cap, parsed as 5,000,000. Only NEWT rows are read.

BATCH FILTER (2026-10-29, WQ-545): list/batch trades print MANY unrelated names in the same minute at
ONE identical upfront (10/22 13:38Z: 77 names incl. Occidental, Broadcom, Norfolk Southern, all
57,305.63 on 3,000,000). That is a common batch price, not a name's market level. A NEWT row whose
(minute, platform, notional, coupon, upfront) key is shared by >= BATCH_MIN distinct names that day is
labelled BATCH and EXCLUDED from levels by default (`--show-batch` prints it, still labelled).
`--selftest` checks the filter.
⚠️ UPFRONT DIRECTION IS NOT DISSEMINATED (KB-LIQ-150): the conversion assumes buyer-pays. Near the coupon it
can land on the wrong side (NextEra ~134bp converted vs 66bp disseminated, 10/23). Prefer disseminated spreads.
"""
import csv, io, math, sys, zipfile, urllib.request, datetime as dt

URL = "https://pddata.dtcc.com/ppd/api/report/cumulative/{r}/{R}_CUMULATIVE_CREDITS_{d}.zip"

def rpv01(s, T, r=0.04, R=0.4):
    h = s / (1 - R)
    return sum(0.25 * math.exp(-(r + h) * i / 4) for i in range(1, int(round(T * 4)) + 1))

def par_spread(upfront, coupon, T):
    s = coupon + upfront / 3.5
    for _ in range(60):
        s = coupon + upfront / rpv01(s, T)
    return s

def rows(day, regime="sec"):
    u = URL.format(r=regime, R=regime.upper(), d=day.replace("-", "_"))
    b = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
    z = zipfile.ZipFile(io.BytesIO(b))
    return list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8", errors="replace")))

BATCH_MIN = 5

def batch_key(r):
    return (r["Execution Timestamp"][:16], r.get("Platform identifier", ""), r["Notional amount-Leg 1"],
            r["Fixed rate-Leg 1"], r["Other payment amount"])

def batch_keys(rs):
    """Keys shared by >= BATCH_MIN distinct names among NEWT upfront rows: a batch price, not a level."""
    names = {}
    for r in rs:
        if r["Action type"] == "NEWT" and r["Other payment amount"]:
            names.setdefault(batch_key(r), set()).add((r["Underlying Asset Name"] or "").upper())
    return {k for k, v in names.items() if len(v) >= BATCH_MIN}

def main(name, days, show_batch=False):
    for day in days:
        try:
            rs = rows(day)
        except Exception as e:
            print(f"{day} UNAVAILABLE ({e})"); continue
        batch = batch_keys(rs)
        hits = [r for r in rs if name.upper() in (r["Underlying Asset Name"] or "").upper() and r["Action type"] == "NEWT"]
        nb = sum(1 for r in hits if batch_key(r) in batch)
        print(f"{day}: {len(rs)} SEC credit rows; {len(hits)} NEWT for '{name}'; {nb} BATCH"
              f"{' (shown, labelled)' if show_batch else ' (excluded)'}")
        for r in sorted(hits, key=lambda r: r["Execution Timestamp"]):
            is_batch = batch_key(r) in batch
            if is_batch and not show_batch:
                continue
            try:
                notl = float(r["Notional amount-Leg 1"].replace(",", "").replace("+", ""))
            except ValueError:
                continue
            T = (dt.date.fromisoformat(r["Expiration Date"]) - dt.date.fromisoformat(r["Effective Date"])).days / 365.25
            if r["Spread-Leg 1"]:
                lvl = f"spread {float(r['Spread-Leg 1'])*1e4:.0f}bp (disseminated)"
            elif r["Other payment type"] == "UFRO" and r["Other payment amount"] and r["Fixed rate-Leg 1"]:
                up = float(r["Other payment amount"]) / notl; c = float(r["Fixed rate-Leg 1"])
                lvl = f"cpn {c*1e4:.0f} upfront {up*100:.2f}pts ~par {par_spread(up, c, T)*1e4:.0f}bp (approx)"
            else:
                lvl = "no level field"
            tag = "BATCH, not a level | " if is_batch else ""
            print(f"  {r['Execution Timestamp'][:16]}Z exp {r['Expiration Date']} {r['Notional amount-Leg 1']:>11} | {tag}{lvl} | {r['Underlying Asset Name']}")

def selftest():
    def row(nm, ts, up, notl="3,000,000", plat="BILT"):
        return {"Underlying Asset Name": nm, "Action type": "NEWT", "Execution Timestamp": ts,
                "Platform identifier": plat, "Notional amount-Leg 1": notl, "Fixed rate-Leg 1": "0.01",
                "Other payment amount": up}
    lst = [row(f"NAME{i}", "2026-10-22T13:38:04Z", "57305.63") for i in range(5)]
    solo = [row("OCCIDENTAL", "2026-10-22T15:49:00Z", "62400"), row("VISTRA", "2026-10-22T15:49:30Z", "62400")]
    four = [row(f"FOUR{i}", "2026-10-22T14:00:00Z", "100") for i in range(4)]
    dup = [row("SAME", "2026-10-22T16:00:00Z", "5")] * 6
    b = batch_keys(lst + solo + four + dup)
    checks = [
        ("5 names, same minute+upfront -> BATCH", batch_key(lst[0]) in b),
        ("2 names sharing a price -> not batch", batch_key(solo[0]) not in b),
        ("4 names (< BATCH_MIN) -> not batch", batch_key(four[0]) not in b),
        ("one name repeated 6x -> not batch (distinct names counted)", batch_key(dup[0]) not in b),
    ]
    for t, ok in checks:
        print(f"  {'✓' if ok else '✗'} {t}")
    bad = sum(not ok for _, ok in checks)
    print(f"SELFTEST: {'PASS' if not bad else f'FAIL ({bad})'}")
    return 1 if bad else 0

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    show = "--show-batch" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--show-batch"]
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    main(args[0], args[1:], show_batch=show)
