"""One-time scan, Q2 -> Q3 2026, accruing 30-89 day late loans by class (FFIEC Call Report RC-N). Not a registered instrument.
Universe: the 138 live banks on the borrowing short list + PFBC as the positive control.
LEAD RULE, written before any result was seen (2026-11-05 ~11:48 ET): a class leads if
  30-89 up >= $25M AND up >= 50% AND 9/30 30-89 >= 2.0% of that class's loans at 9/30.
Probable acquirers (assets >= +20%) are listed apart. A class with no book figure cannot lead.
Tie-out: class sum must equal the reported total 30-89 within 1%, else the bank is reported as UNTIED.
Usage (repo root): .venv/bin/python3 AGENTS/REGINALD/domain/sources/2026-11-05_late-loan-scan/scan.py OUTDIR"""
import csv, os, sys, json
sys.path.insert(0, "AGENTS/REGINALD/scripts")
import mi3_cohort_screen as m, borrowing_screen as bs, borrowing_shortlist_ffiec as sl
out = sys.argv[1]
R = list(csv.DictReader(open(sl.DRY), delimiter="\t")); F = lambda r, k: float(r[k])
by = {int(r["rssd"]): r for r in R if r["rssd"] not in ("", "None")}
small = [r for r in R if r["small"] == "True" and r["merger"] == "False"]
flagged = [r for r in small if F(r,"dbor") >= bs.FLAG_MIN_K and (F(r,"bor_p")==0 or F(r,"dbor")/F(r,"bor_p") >= bs.FLAG_MIN_PCT) and F(r,"ddep") < 0]
top20 = sorted((r for r in small if F(r,"dbor") > 0), key=lambda r: -F(r,"dbor"))[:20]
big100 = sorted(small, key=lambda r: -F(r,"asset"))[:100]
ids = set(bs.COHORT_RSSD) | {int(r["rssd"]) for r in flagged + top20 + big100}
ids |= {1918344}
ids.discard(761806)
CLS = {  # class: (30-89 codes, nonaccrual codes, book codes)
 "construction": (["F172","F173"], ["F176","F177"], ["F158","F159"]),
 "1-4 family": (["5398","C236","C238"], ["5400","C229","C230"], ["1797","5367","5368"]),
 "multifamily": (["3499"], ["3501"], ["1460"]),
 "owner CRE": (["F178"], ["F182"], ["F160"]),
 "non-owner CRE": (["F179"], ["F183"], ["F161"]),
 "C&I": (["1606"], ["1608"], ["1763","1764"]),
}
def val(d, c):
    for p in ("RCON", "RCFD"):
        if p + c in d: return d[p + c]
    return None
def tot(d, cs):
    v = [val(d, c) for c in cs]
    return None if all(x is None for x in v) else sum(x or 0 for x in v)
u, t = m.creds()
rows, leads, untied, missing = [], [], [], []
name = lambda rs: (by[rs]["name"] if rs in by else "PREFERRED BANK")
for rs in sorted(ids):
    a = m.facsimile(u, t, rs, "6/30/2026"); b = m.facsimile(u, t, rs, "9/30/2026")
    if a is None or b is None: missing.append(name(rs)); continue
    p, c = m.parse(a), m.parse(b)
    tp, tc = val(p, "1406"), val(c, "1406")
    ap, ac = val(p, "2170"), val(c, "2170")
    lp, lc = val(p, "2122"), val(c, "2122")
    s = sum((tot(c, v[0]) or 0) for v in CLS.values())
    tied = tc is not None and (tc == 0 and s == 0 or tc and abs(s - tc) / tc <= 0.01)
    if not tied: untied.append((name(rs), tc, s))
    acq = bool(ap and ac / ap - 1 >= 0.20)
    row = dict(rssd=rs, name=name(rs), state=by[rs]["state"] if rs in by else "CALIFORNIA", assets_m=round((ac or 0)/1e3), loans_m=round((lc or 0)/1e3),
               t3089_p=tp, t3089_c=tc, na_p=val(p,"1403"), na_c=val(c,"1403"), acq=acq, tied=bool(tied))
    rows.append(row)
    for k, (q, n, bk) in CLS.items():
        qp, qc, np_, nc, bv = tot(p,q), tot(c,q), tot(p,n), tot(c,n), tot(c,bk)
        if None in (qp, qc) or not bv: continue
        d = qc - qp
        if d >= 25000 and (qp == 0 or d / qp >= 0.5) and qc / bv >= 0.02:
            leads.append(dict(name=row["name"], rssd=rs, cls=k, p=qp, c=qc, pct_book=round(qc/bv*100,1), book_m=round(bv/1e3), na_p=np_, na_c=nc, assets_m=row["assets_m"], acq=acq, tied=bool(tied)))
json.dump(dict(rows=rows, leads=leads, untied=untied, missing=missing), open(os.path.join(out, "scan_raw.json"), "w"), indent=0)
leads.sort(key=lambda x: -(x["c"] - x["p"]))
print(f"banks scanned {len(rows)}, missing {missing}, untied {len(untied)}")
print("sum 30-89 6/30 $M", round(sum(r['t3089_p'] or 0 for r in rows)/1e3), "9/30", round(sum(r['t3089_c'] or 0 for r in rows)/1e3))
for x in leads:
    print(f"{x['name'][:34]:34} {x['cls']:14} 30-89 {x['p']/1e3:8.1f} -> {x['c']/1e3:8.1f}  {x['pct_book']:5.1f}% of ${x['book_m']:,}M  NA {(x['na_p'] or 0)/1e3:7.1f}->{(x['na_c'] or 0)/1e3:7.1f} assets ${x['assets_m']:,}M{' ACQ' if x['acq'] else ''}{'' if x['tied'] else ' UNTIED'}")
print("UNTIED:", [(n, a, b) for n, a, b in untied][:12])
