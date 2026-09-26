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

def main(name, days):
    for day in days:
        try:
            rs = rows(day)
        except Exception as e:
            print(f"{day} UNAVAILABLE ({e})"); continue
        hits = [r for r in rs if name.upper() in (r["Underlying Asset Name"] or "").upper() and r["Action type"] == "NEWT"]
        print(f"{day}: {len(rs)} SEC credit rows; {len(hits)} NEWT for '{name}'")
        for r in sorted(hits, key=lambda r: r["Execution Timestamp"]):
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
            print(f"  {r['Execution Timestamp'][:16]}Z exp {r['Expiration Date']} {r['Notional amount-Leg 1']:>11} | {lvl} | {r['Underlying Asset Name']}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    main(sys.argv[1], sys.argv[2:])
