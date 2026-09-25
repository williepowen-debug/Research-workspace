import csv, io, zipfile, sys, os, statistics, datetime
SP = sys.argv[1]
CODES = {"silver": ("084691", "SILVER - COMMODITY EXCHANGE INC."),
         "platinum": ("076651", "PLATINUM - NEW YORK MERCANTILE EXCHANGE"),
         "palladium": ("075651", "PALLADIUM - NEW YORK MERCANTILE EXCHANGE"),
         "gold": ("088691", "GOLD - COMMODITY EXCHANGE INC.")}
WANT = {"name": "Market and Exchange Names", "date": "As of Date in Form YYYY-MM-DD",
        "code": "CFTC Contract Market Code", "oi": "Open Interest (All)",
        "ncl": "Noncommercial Positions-Long (All)", "ncs": "Noncommercial Positions-Short (All)",
        "ncsp": "Noncommercial Positions-Spreading (All)", "cl": "Commercial Positions-Long (All)",
        "cs": "Commercial Positions-Short (All)", "tl": "Total Reportable Positions-Long (All)",
        "ts": "Total Reportable Positions-Short (All)", "nrl": "Nonreportable Positions-Long (All)",
        "nrs": "Nonreportable Positions-Short (All)"}
data = {m: {} for m in CODES}
fails = {m: [] for m in CODES}; dups = {m: [] for m in CODES}; names = {m: set() for m in CODES}
for y in range(2010, 2027):
    z = zipfile.ZipFile(f"{SP}/hist/deacot{y}.zip")
    txt = z.read(z.namelist()[0]).decode("utf-8", "replace")
    rd = csv.reader(io.StringIO(txt)); hdr = [h.strip() for h in next(rd)]
    idx = {k: hdr.index(v) for k, v in WANT.items()}  # raises if header missing
    for r in rd:
        if len(r) < len(hdr) - 2: continue
        code = r[idx["code"]].strip()
        for m, (c, nm) in CODES.items():
            if code != c: continue
            names[m].add(r[idx["name"]].strip())
            g = lambda k: int(float(r[idx[k]].strip()))
            d = r[idx["date"]].strip()
            v = {k: g(k) for k in WANT if k not in ("name", "date", "code")}
            ok = (v["tl"] + v["nrl"] == v["oi"] and v["ts"] + v["nrs"] == v["oi"]
                  and v["ncl"] + v["ncsp"] + v["cl"] == v["tl"] and v["ncs"] + v["ncsp"] + v["cs"] == v["ts"])
            if not ok: fails[m].append((d, v)); continue
            if d in data[m]:
                dups[m].append(d)
                if data[m][d] != v: fails[m].append((d, "DUP-CONFLICT"))
                continue
            data[m][d] = v
for m in CODES:
    with open(f"{SP}/cot_hist_{m}.tsv", "w", newline="\n") as f:
        f.write("report_date\topen_interest\tnc_long\tnc_short\tnet_nc_long\tnet_over_oi_pct\n")
        for d in sorted(data[m]):
            v = data[m][d]; net = v["ncl"] - v["ncs"]
            f.write(f"{d}\t{v['oi']}\t{v['ncl']}\t{v['ncs']}\t{net}\t{100*net/v['oi']:.4f}\n")
    ds = sorted(data[m]); dts = [datetime.date.fromisoformat(x) for x in ds]
    gaps = [(ds[i-1], ds[i], (dts[i]-dts[i-1]).days) for i in range(1, len(ds)) if (dts[i]-dts[i-1]).days != 7]
    print(m, "n", len(ds), ds[0], ds[-1], "fails", len(fails[m]), fails[m][:3], "dups", len(dups[m]), "names", names[m], "non-7d gaps", gaps)
