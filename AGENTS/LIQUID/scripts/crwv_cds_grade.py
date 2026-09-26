#!/usr/bin/env python3
"""crwv_cds_grade.py — GATE-LIQ-069 leg 2 grading input: CoreWeave single-name CDS prints from the
DTCC Public Price Dissemination SEC-regime cumulative credit files ($0, no login), converted from
upfront on the 500bp fixed coupon to a CONVENTIONAL SPREAD. Born 2026-09-26 (LIQUID, first leg-2 grade).

    python3 crwv_cds_grade.py CACHE_DIR YYYY-MM-DD [YYYY-MM-DD ...]
    (downloads any missing daily ZIP into CACHE_DIR; prints every CoreWeave print per day)

WARNING: NOT the ISDA CDS Standard Model. It approximates it: flat hazard; FLAT discount rate r
(default 4%; the ISDA model uses the USD SOFR swap curve); R = 40% (the conventional-spread
convention); quarterly ACT/360 premium accruing from the previous IMM coupon date; step-in T+1;
accrual-on-default at mid-period; weekly protection-leg integration. Conventional spread = the par
spread on the flat-hazard curve that reprices the clean upfront.
'Other payment amount' (type UFRO) is read as the CLEAN upfront; the 'dirty' column treats it as
cash net of accrued premium and is the clean/dirty half of the error band.
Band measured 2026-09-26: r 3.5-4.5% moves the 9/23-24 prints about +/-5bp; clean-vs-dirty is
+1-2bp there (accrual only since 9/21), +6bp at 7/06, +42bp at 12/17. The structural gap to the full
ISDA model is UNMEASURED; INFERRED bound ~+/-15bp (agreement with the cruder dtcc_cds_probe.py
within ~10bp).
Rows: NEWT, replaced by any CORR/MODI naming it, dropped if CANC/ERRO/TERM names it.
Flags: CAPPED (notional '5,000,000+' — upfront scaled to the capped notional; spreads agree with
uncapped neighbours), NONSTD (non-standardized term indicator), PKG (package), NONIMM (maturity not
on the 20th). Named grading quotes should be unflagged.
"""
import csv, io, math, os, sys, zipfile, subprocess, datetime as dt
D = dt.date
URL = "https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_{d}.zip"


def imm_prev(d):
    c = []
    for y in (d.year - 1, d.year):
        for m in (3, 6, 9, 12):
            x = D(y, m, 20)
            while x.weekday() >= 5:
                x += dt.timedelta(1)
            c.append(x)
    return max(x for x in c if x <= d)


def schedule(acc_start, mat):
    ps, s = [], acc_start
    y = s.year
    nxt = [(y, mm) for mm in (3, 6, 9, 12) if D(y, mm, 20) > s] + [(y + 1, 3)]
    y, m = nxt[0]
    while True:
        e = D(y, m, 20)
        ea = e
        while ea.weekday() >= 5:
            ea += dt.timedelta(1)
        if e >= mat:
            ps.append((s, mat + dt.timedelta(1), mat))
            break
        ps.append((s, ea, ea))
        s = ea
        m += 3
        if m > 12:
            m -= 12
            y += 1
    return ps


def legs(h, c, trade, mat, r, R=0.4):
    step = trade + dt.timedelta(1)
    acc0 = imm_prev(trade)
    t = lambda d: (d - trade).days / 365.0
    df = lambda d: math.exp(-r * t(d))
    sv = lambda d: math.exp(-h * max(0, (d - step).days) / 365.0)
    rpv = 0.0
    for (s, e, pay) in schedule(acc0, mat):
        rpv += (e - s).days / 360.0 * df(pay) * sv(min(pay, mat))
        a = max(s, step)
        if e > a:
            end = min(e, mat)
            mid = a + (end - a) / 2
            rpv += (sv(a) - sv(end)) * ((mid - s).days / 360.0) * df(mid)
    prot, d = 0.0, step
    while d < mat:
        n = min(d + dt.timedelta(7), mat)
        prot += (1 - R) * (sv(d) - sv(n)) * df(d + (n - d) / 2)
        d = n
    accrued_frac = (trade + dt.timedelta(1) - acc0).days / 360.0
    return prot, rpv, accrued_frac


def conv_spread(U, c, trade, mat, r=0.04, dirty=False):
    lo, hi = 1e-5, 3.0
    for _ in range(80):
        h = (lo + hi) / 2
        p, rp, af = legs(h, c, trade, mat, r)
        clean = U + c * af if dirty else U
        if p - c * (rp - af) > clean:
            hi = h
        else:
            lo = h
    p, rp, af = legs(h, c, trade, mat, r)
    return p / (rp - af)


def load(cache, day):
    f = os.path.join(cache, f"sec_{day.replace('-', '_')}.zip")
    if not (os.path.exists(f) and os.path.getsize(f) > 1000):
        subprocess.run(["curl", "-s", "-A", "Mozilla/5.0", "-o", f, URL.format(d=day.replace("-", "_"))], check=False)
    z = zipfile.ZipFile(f)
    return list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8", errors="replace")))


def crwv_rows(rs):
    cw = [x for x in rs if "COREWEAVE" in (x["Underlying Asset Name"] or "").upper()]
    live = {x["Dissemination Identifier"]: x for x in cw if x["Action type"] == "NEWT"}
    dead = set()
    for x in cw:
        o = x["Original Dissemination Identifier"]
        if o in live and x["Action type"] in ("CORR", "MODI"):
            live[o] = dict(x, _corr="CORR")
        if o in live and x["Action type"] in ("CANC", "ERRO", "TERM", "EROR"):
            dead.add(o)
    return [(i, x) for i, x in live.items() if i not in dead]


def main(cache, days):
    os.makedirs(cache, exist_ok=True)
    for day in days:
        try:
            rs = load(cache, day)
        except Exception as e:
            print(f"{day} UNAVAILABLE ({e})")
            continue
        out = crwv_rows(rs)
        print(f"{day}: {len(rs)} SEC credit rows; {len(out)} live CoreWeave prints")
        for i, x in sorted(out, key=lambda p: p[1]["Execution Timestamp"]):
            n = x["Notional amount-Leg 1"]
            flags = []
            if "+" in n: flags.append("CAPPED")
            if x["Non-standardized term indicator"] != "FALSE": flags.append("NONSTD")
            if x["Package indicator"] not in ("FALSE", "false", ""): flags.append("PKG")
            mat = D.fromisoformat(x["Expiration Date"])
            if mat.day != 20: flags.append("NONIMM")
            trade = D.fromisoformat(x["Execution Timestamp"][:10])
            try:
                notl = float(n.replace(",", "").replace("+", ""))
                c = float(x["Fixed rate-Leg 1"])
                U = float(x["Other payment amount"]) / notl
                assert x["Other payment type"] == "UFRO"
            except Exception:
                print(f"  {x['Execution Timestamp'][:16]}Z id {i} mat {mat} — no upfront/coupon, skipped {flags}")
                continue
            s = conv_spread(U, c, trade, mat) * 1e4
            sd = conv_spread(U, c, trade, mat, dirty=True) * 1e4
            print(f"  {x['Execution Timestamp'][:16]}Z id {i} mat {mat} {n:>11} cpn {c*1e4:.0f} "
                  f"upfront {U*100:6.2f}pt -> {s:5.0f}bp (dirty {sd:5.0f}) {','.join(flags)} {x.get('_corr','')}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2:])
