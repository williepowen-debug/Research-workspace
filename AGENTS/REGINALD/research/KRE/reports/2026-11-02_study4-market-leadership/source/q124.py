"""Q1 + Q2 + Q4 rolling sensitivities. Outputs out/q1_benchmarks.csv, out/q2_sectors.csv, out/rolling_63.csv, out/blocks21.csv, out/onsets.csv"""
import os
import numpy as np, pandas as pd

H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"; os.makedirs(OUT, exist_ok=True)
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
END = pd.Timestamp("2026-10-30")
W = 63


def rbeta(y, x, w=W):
    return X[y].rolling(w).cov(X[x]) / X[x].rolling(w).var()


def rcorr(y, x, w=W):
    return X[y].rolling(w).corr(X[x])


def pct(s, v, start, end=None):
    h = s.loc[start:end].dropna()
    return (h <= v).mean(), h.median(), len(h)


# ---- verify brief numbers
b = rbeta("KRE", "SPY"); c = rcorr("KRE", "KBWB")
print("KRE SPY beta", round(b[END], 3), "pct since 2012-02", [round(z, 3) for z in pct(b, b[END], "2012-02-01")], "since 2006-12", [round(z, 3) for z in pct(b, b[END], "2006-12-01")])
print("KRE-KBWB corr", round(c[END], 4), [round(z, 3) for z in pct(c, c[END], "2012-02-01")])
bk = rbeta("KBWB", "SPY"); print("KBWB SPY beta", round(bk[END], 3), [round(z, 3) for z in pct(bk, bk[END], "2012-02-01")])
# partial corr KRE,KBWB | SPY
rks, rbs, rkb = rcorr("KRE", "SPY"), rcorr("KBWB", "SPY"), c
pc = (rkb - rks * rbs) / np.sqrt((1 - rks ** 2) * (1 - rbs ** 2))
print("partial corr|SPY", round(pc[END], 4), [round(z, 3) for z in pct(pc, pc[END], "2012-02-01")])

# ---- Q1 benchmark table
BEN = ["SPY", "RSP", "IWM", "IWN", "QQQ", "XLF", "KBE"]
rows = []
for y in ("KRE", "KBWB"):
    for x in BEN:
        for kind, s in (("corr", rcorr(y, x)), ("beta", rbeta(y, x))):
            p12, m12, n12 = pct(s, s[END], "2012-02-01", "2024-12-31")
            pall, mall, nall = pct(s, s[END], "2012-02-01")
            rows.append(dict(asset=y, bench=x, metric=kind, current=s[END], pct_pre2025=p12, median_pre2025=m12,
                             pct_since2012=pall, median_since2012=mall, value_2025_median=s.loc["2025-01-01":"2025-12-31"].median(),
                             value_2026H1_median=s.loc["2026-01-01":"2026-06-30"].median()))
Q1 = pd.DataFrame(rows); Q1.to_csv(f"{OUT}/q1_benchmarks.csv", index=False, float_format="%.4f")
pd.set_option("display.width", 220)
print(Q1.round(3).to_string())

# leadership metrics
lead = {"corr SPY-RSP": rcorr("SPY", "RSP"), "corr SPY-QQQ": rcorr("SPY", "QQQ"), "corr RSP-QQQ": rcorr("RSP", "QQQ"),
        "beta RSP~SPY": rbeta("RSP", "SPY"), "beta IWN~SPY": rbeta("IWN", "SPY"), "beta IWN~RSP": rbeta("IWN", "RSP"),
        "corr IWN-SPY": rcorr("IWN", "SPY"), "corr HML_ff-MKT_ff": rcorr("HML_ff", "MKT_ff"), "corr HML_p-SPY": rcorr("HML_p", "SPY"),
        "vol CONC (ann.)": X.CONC.rolling(W).std() * np.sqrt(252), "share of SPY var from CONC": None}
v_spy = X.SPY.rolling(W).var(); v_rsp = X.RSP.rolling(W).var()
lead["share of SPY var from CONC"] = 1 - X.SPY.rolling(W).corr(X.RSP) ** 2
L = []
for k, s in lead.items():
    v = s[END] if END in s.index else s.dropna().iloc[-1]
    p, m, n = pct(s, v, "2012-02-01", "2024-12-31")
    L.append(dict(metric=k, current=v, pct_pre2025=p, median_pre2025=m, median_2025=s.loc["2025"].median(), median_2026H1=s.loc["2026-01":"2026-06"].median()))
Ld = pd.DataFrame(L); Ld.to_csv(f"{OUT}/q1_leadership.csv", index=False, float_format="%.4f"); print(Ld.round(3).to_string())

# KRE on RSP + CONC (equal-weight market + concentration)
def roll_ols(y, xs, w=W):
    out = {}
    idx = X.index
    Z = X[[y] + xs].dropna()
    for e in range(w, len(Z) + 1, 1):
        pass
    return None

# ---- Q2: sectors' SPY and RSP betas
SECT = ["XLU", "IYR", "ITB", "XLI", "XLB", "IYT", "KIE", "IWN", "XLF", "KBWB", "KRE", "QQQ", "XLK"]
rows = []; onset_rows = []
for t in SECT:
    for mk in ("SPY", "RSP"):
        s = rbeta(t, mk); cc = rcorr(t, mk)
        ref = s.loc["2012-02-01":"2024-12-31"].dropna(); p10 = ref.quantile(0.10)
        refc = cc.loc["2012-02-01":"2024-12-31"].dropna(); p10c = refc.quantile(0.10)
        below = s < p10
        # runs >= 10 sessions in 2025-26
        r26 = below.loc["2025-01-01":]
        runs = []; start = None; n = 0
        for d, v in r26.items():
            if v: start = start or d; n += 1
            else:
                if n >= 10: runs.append((start.date(), prev.date(), n))
                start, n = None, 0
            prev = d
        if n >= 10: runs.append((start.date(), prev.date(), n))
        rows.append(dict(etf=t, market=mk, beta_now=s[END], beta_pct_pre2025=(ref <= s[END]).mean(), beta_median_pre2025=ref.median(), p10=p10,
                         beta_min_2025_26=s.loc["2025-01-01":].min(), date_min=s.loc["2025-01-01":].idxmin().date(),
                         share_days_below_p10_2025=(s.loc["2025"] < p10).mean(), share_days_below_p10_2026=(s.loc["2026"] < p10).mean(),
                         corr_now=cc[END], corr_pct_pre2025=(refc <= cc[END]).mean(), corr_median_pre2025=refc.median(),
                         share_days_corr_below_p10_2026=(cc.loc["2026"] < p10c).mean(),
                         runs_below_p10=";".join(f"{a}→{b}({k})" for a, b, k in runs)))
Q2 = pd.DataFrame(rows); Q2.to_csv(f"{OUT}/q2_sectors.csv", index=False, float_format="%.4f")
print(Q2.drop(columns=["runs_below_p10"]).round(3).to_string())
print(Q2[["etf", "market", "runs_below_p10"]].to_string())

# ---- rolling series for Q4 + blocks
RS = pd.DataFrame({"KRE_beta_SPY": rbeta("KRE", "SPY"), "KRE_beta_RSP": rbeta("KRE", "RSP"), "KRE_beta_IWN": rbeta("KRE", "IWN"),
                   "KRE_corr_SPY": rcorr("KRE", "SPY"), "KRE_corr_RSP": rcorr("KRE", "RSP"), "KRE_corr_IWN": rcorr("KRE", "IWN"),
                   "KRE_corr_KBWB": c, "KRE_corr_XLI": rcorr("KRE", "XLI"), "KRE_corr_KBE": rcorr("KRE", "KBE"),
                   "KBWB_beta_SPY": bk, "KBWB_corr_SPY": rcorr("KBWB", "SPY"), "KBWB_corr_RSP": rcorr("KBWB", "RSP"),
                   "corr_SPY_RSP": lead["corr SPY-RSP"], "IWN_beta_SPY": lead["beta IWN~SPY"], "XLI_beta_SPY": rbeta("XLI", "SPY"),
                   "ITB_beta_SPY": rbeta("ITB", "SPY"), "IYR_beta_SPY": rbeta("IYR", "SPY"), "XLU_beta_SPY": rbeta("XLU", "SPY"),
                   "KRE_corr_HMLp": rcorr("KRE", "HML_p"), "partial_KRE_KBWB_SPY": pc})
RS.to_csv(f"{OUT}/rolling_63.csv", float_format="%.4f")
on = []
for col in RS.columns:
    s = RS[col]; ref = s.loc["2012-02-01":"2024-12-31"].dropna(); p10 = ref.quantile(0.10)
    for yr in ("2025", "2026"):
        b_ = (s.loc[yr] < p10).astype(int)
        run = b_.groupby((b_ != b_.shift()).cumsum()).transform("sum") * b_
        hit = run[run >= 10]
        on.append(dict(series=col, year=yr, p10_pre2025=p10, first_onset=hit.index.min().date() if len(hit) else None,
                       share_days_below=(s.loc[yr] < p10).mean()))
ON = pd.DataFrame(on); ON.to_csv(f"{OUT}/onsets.csv", index=False, float_format="%.3f"); print(ON.round(3).to_string())

# non-overlapping 21d blocks since 2024-01 (anchored at END)
pos = X.index.get_loc(END); ends = [X.index[i] for i in range(pos, X.index.get_loc(pd.Timestamp("2024-01-31")), -21)][::-1]
B = []
for e in ends:
    i = X.index.get_loc(e); w = X.iloc[i - 20:i + 1]
    row = dict(end=e.date())
    for y, x in (("KRE", "SPY"), ("KRE", "RSP"), ("KRE", "IWN"), ("KRE", "KBWB"), ("KBWB", "SPY"), ("SPY", "RSP"), ("IWN", "SPY"), ("XLI", "SPY")):
        row[f"corr_{y}_{x}"] = w[y].corr(w[x]); row[f"beta_{y}_{x}"] = w[y].cov(w[x]) / w[x].var()
    row["KRE_vol"] = w.KRE.std() * np.sqrt(252); row["SPY_vol"] = w.SPY.std() * np.sqrt(252)
    B.append(row)
BL = pd.DataFrame(B); BL.to_csv(f"{OUT}/blocks21.csv", index=False, float_format="%.3f")
print(BL[["end", "corr_KRE_SPY", "beta_KRE_SPY", "beta_KRE_RSP", "corr_KRE_IWN", "corr_KRE_KBWB", "beta_KBWB_SPY", "corr_SPY_RSP", "beta_IWN_SPY", "KRE_vol", "SPY_vol"]].round(2).to_string())
