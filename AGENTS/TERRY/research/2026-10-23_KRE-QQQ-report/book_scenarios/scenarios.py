"""Price the see-saw book (bank/credit puts + Nasdaq downside) under named KRE/QQQ scenarios.
MODEL, not marks: Black-Scholes European puts, r = 4.0%, no dividends, no skew change,
vol scaled per scenario as stated. Inputs: positions.csv, quotes.csv, px_1y.csv (pull_quotes.py).
Single names move by their 1-year two-factor beta to KRE and QQQ. Writes RESULTS.md + results.json.
Run: python3 -I scenarios.py
"""
import csv, json, math, os, datetime as dt
import statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
R = 0.04
ASOF = None  # set from quotes.csv pull stamp
ASSUMED_IV = {("KRE", "2026-11-27", 70.0): 0.30}  # vendor chain lacks the strike (stops at 67.5, IV 0.309)

def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def bs_put(S, K, T, iv):
    if T <= 0:
        return max(K - S, 0.0)
    d1 = (math.log(S / K) + (R + iv * iv / 2) * T) / (iv * math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    return K * math.exp(-R * T) * ncdf(-d2) - S * ncdf(-d1)

def years(expiry, when):
    exp = dt.datetime.strptime(expiry, "%Y-%m-%d").replace(hour=16)
    return max((exp - when).total_seconds(), 0) / (365 * 86400)

# ---- betas: daily log returns, 1y, two-factor OLS on KRE and QQQ
px = list(csv.DictReader(open(os.path.join(HERE, "px_1y.csv"))))
cols = [c for c in px[0] if c != "Date"]
series = {c: [float(r[c]) for r in px if r[c]] for c in cols}
n = min(len(v) for v in series.values())
rets = {c: [math.log(v[i] / v[i - 1]) for i in range(len(v) - n + 1, len(v))] for c, v in series.items()}

def ols2(y, x1, x2):
    m = lambda a: sum(a) / len(a)
    y0, a0, b0 = [v - m(y) for v in y], [v - m(x1) for v in x1], [v - m(x2) for v in x2]
    s11 = sum(a * a for a in a0); s22 = sum(b * b for b in b0); s12 = sum(a * b for a, b in zip(a0, b0))
    s1y = sum(a * c for a, c in zip(a0, y0)); s2y = sum(b * c for b, c in zip(b0, y0))
    det = s11 * s22 - s12 * s12
    b1 = (s1y * s22 - s2y * s12) / det; b2 = (s2y * s11 - s1y * s12) / det
    res = [c - b1 * a - b2 * b for c, a, b in zip(y0, a0, b0)]
    r2 = 1 - sum(e * e for e in res) / sum(c * c for c in y0)
    return b1, b2, r2

BETA = {"KRE": (1.0, 0.0, 1.0), "QQQ": (0.0, 1.0, 1.0)}
for c in cols:
    if c not in BETA:
        BETA[c] = ols2(rets[c], rets["KRE"], rets["QQQ"])

# ---- book
quotes = list(csv.DictReader(open(os.path.join(HERE, "quotes.csv"))))
ASOF = dt.datetime.strptime(quotes[0]["pulled"], "%Y-%m-%d %H:%M:%S")
book = []
for q in quotes:
    K = float(q["strike"]); key = (q["ticker"], q["expiry"], K)
    if q["iv"]:
        iv, mid, ivsrc = float(q["iv"]), (float(q["bid"]) + float(q["ask"])) / 2, "vendor"
    else:
        iv, mid, ivsrc = ASSUMED_IV[key], None, "ASSUMED"
    S = float(q["spot"])
    if mid is None:
        mid = bs_put(S, K, years(q["expiry"], ASOF), iv)
    book.append(dict(leg=q["leg"], acct=q["account"], tk=q["ticker"], K=K, exp=q["expiry"], qty=int(q["qty"]),
                     S=S, iv=iv, ivsrc=ivsrc, mid=mid, bid=q["bid"], ask=q["ask"], verified=q["verified"]))

def value(line, kre, qqq, m_bank, m_qqq, when):
    b1, b2, _ = BETA[line["tk"]]
    S = line["S"] * math.exp(b1 * math.log(1 + kre) + b2 * math.log(1 + qqq))
    m = m_qqq if line["tk"] == "QQQ" else m_bank
    return bs_put(S, line["K"], years(line["exp"], when), line["iv"] * m) * 100 * line["qty"]

def run(scens, when, include):
    out = []
    lines = [l for l in book if include(l)]
    for name, kre, qqq, mb, mq in scens:
        row = {"scenario": name, "KRE": kre, "QQQ": qqq, "vol_bank": mb, "vol_qqq": mq}
        for leg in ("bank", "nasdaq"):
            ls = [l for l in lines if l["leg"] == leg]
            now = sum(value(l, 0, 0, 1, 1, ASOF) for l in ls)
            fut = sum(value(l, kre, qqq, mb, mq, when) for l in ls)
            row[leg + "_now"] = now; row[leg + "_then"] = fut; row[leg + "_chg"] = fut - now
        row["total_chg"] = row["bank_chg"] + row["nasdaq_chg"]
        out.append(row)
    return out

MON = dt.datetime(2026, 10, 26, 16, 0)
NOV13 = dt.datetime(2026, 11, 13, 16, 0)
# name, KRE move, QQQ move, bank-vol multiplier, QQQ-vol multiplier
S_MON = [("Flat", 0, 0, 1.0, 1.0), ("See-saw continues", .02, -.02, 1.0, 1.05),
         ("Snap-back", -.02, .02, 1.0, .95), ("Both fall", -.03, -.03, 1.15, 1.15), ("Both rally", .02, .02, .9, .9)]
S_NOV = [("Flat", 0, 0, 1.0, 1.0), ("See-saw continues", .05, -.05, 1.0, 1.1),
         ("Snap-back", -.05, .05, 1.05, .85), ("Both fall (Aug-2024 shape)", -.10, -.08, 1.35, 1.35),
         ("Both fall hard", -.15, -.12, 1.6, 1.6), ("Both rally", .05, .05, .85, .8)]
mon = run(S_MON, MON, lambda l: True)
nov = run(S_NOV, NOV13, lambda l: l["exp"] > "2026-10-26")
grid_k = [-.15, -.10, -.05, 0, .05]; grid_q = [-.12, -.08, -.04, 0, .04, .08]
grid = {(k, q): run([("g", k, q, 1, 1)], NOV13, lambda l: l["exp"] > "2026-10-26")[0]["total_chg"]
        for k in grid_k for q in grid_q}

# ---- report
f = lambda x: f"{'+' if x >= 0 else '−'}${abs(x):,.0f}"
pct = lambda x: f"{x * 100:+.0f}%"
L = []
L.append(f"# See-saw book under scenarios — MODEL (quotes pulled {ASOF:%Y-%m-%d %H:%M} ET)\n")
L.append("Black-Scholes European puts, r 4.0%, no dividends, today's vendor implied vol per contract scaled by the stated multiplier. "
         "Changes are model value at the horizon minus model value now (same model both ends, so the vendor-mid vs model gap cancels). "
         "Single names move by 1-year two-factor betas. Not fills; not broker marks.\n")
L.append("## Lines and current screening marks\n")
L.append("| Leg | Acct | Line | Qty | Spot | Bid / Ask | IV | Value at mid |\n|---|---|---|---:|---:|---|---:|---:|")
for l in book:
    ba = f"{l['bid']} / {l['ask']}" if l["bid"] != "" else "no vendor quote"
    L.append(f"| {l['leg']} | {l['acct']}{' (unverified)' if l['verified']=='unverified' else ''} | {l['tk']} {l['exp']} {l['K']:g}P | {l['qty']} | {l['S']:.2f} | {ba} | "
             f"{l['iv']*100:.0f}%{' ASSUMED' if l['ivsrc']=='ASSUMED' else ''} | {f(l['mid']*100*l['qty'])} |")
tb = sum(l["mid"] * 100 * l["qty"] for l in book if l["leg"] == "bank")
tn = sum(l["mid"] * 100 * l["qty"] for l in book if l["leg"] == "nasdaq")
L.append(f"\n**Value at mid now: bank/credit {f(tb)} · Nasdaq {f(tn)} · total {f(tb+tn)}.**\n")
L.append("## Betas used (1 year of daily returns; two-factor on KRE and QQQ)\n")
L.append("| Name | to KRE | to QQQ | R² |\n|---|---:|---:|---:|")
for c in cols:
    if c not in ("KRE", "QQQ"):
        b1, b2, r2 = BETA[c]; L.append(f"| {c} | {b1:.2f} | {b2:.2f} | {r2:.2f} |")
for title, rows in (("By Monday 10/26 close (whole book; the Oct-26 QQQ puts expire that day)", mon),
                    ("By Friday 11/13 close (put-wall time stop; Oct-26 lines excluded — decided Monday)", nov)):
    L.append(f"\n## {title}\n")
    L.append("| Scenario | KRE | QQQ | Vol (bank / QQQ) | Bank/credit puts | Nasdaq downside | **Book** |\n|---|---:|---:|---|---:|---:|---:|")
    for r in rows:
        L.append(f"| {r['scenario']} | {pct(r['KRE'])} | {pct(r['QQQ'])} | ×{r['vol_bank']:.2f} / ×{r['vol_qqq']:.2f} | "
                 f"{f(r['bank_chg'])} | {f(r['nasdaq_chg'])} | **{f(r['total_chg'])}** |")
L.append("\n## Grid at 11/13, vol unchanged (book excluding Oct-26 lines): change in value\n")
L.append("| KRE \\ QQQ | " + " | ".join(pct(q) for q in grid_q) + " |\n|---|" + "---:|" * len(grid_q))
for k in grid_k:
    L.append(f"| {pct(k)} | " + " | ".join(f(grid[(k, q)]) for q in grid_q) + " |")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
json.dump({"asof": str(ASOF), "betas": {c: BETA[c] for c in cols}, "monday": mon, "nov13": nov,
           "grid": {f"{k},{q}": v for (k, q), v in grid.items()}}, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print("\n".join(L))
