"""Q3: factor models M0..M4 on rolling 21/63/126 windows; exposures vs history; unexplained share; residual corr KRE~KBWB;
volatility-matched comparison; out-of-sample test.
Factor series: French (through 2026-09-30) spliced with ETF proxies for 2026-10-01..10-30 ('_s'); pure-French windows end 9/30.
Outputs: out/q3_exposures.csv, out/q3_unexplained.csv, out/q3_volmatched.csv, out/q3_oos.csv, out/q3_rolling63.csv"""
import os
import numpy as np, pandas as pd
from numpy.lib.stride_tricks import sliding_window_view as swv

H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
for f in ("MKT", "SMB", "HML", "MOM"):
    X[f + "_s"] = X[f + "_ff"].where(X[f + "_ff"].notna(), X[f + "_p"])
X["KRE_x"] = X.KRE - X.RF; X["KBWB_x"] = X.KBWB - X.RF; X["SPY_x"] = X.SPY - X.RF
MODELS = {"M0 SPY": ["SPY_x"], "M1 MKT": ["MKT_s"], "M2 FF3+MOM": ["MKT_s", "SMB_s", "HML_s", "MOM_s"],
          "M3 +Δ10y": ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10"], "M4 +CONC+ΔBaa": ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10", "CONC", "dbaa"],
          "E1 RSP": ["RSP"], "E2 RSP+CONC": ["RSP", "CONC"]}
END = pd.Timestamp("2026-10-30"); END_FF = pd.Timestamp("2026-09-30")
S = X.loc["2006-07-01":"2026-10-30"]


def rolling_fit(y, cols, w):
    """rolling OLS for every window end; returns DataFrame of betas, r2, resid vol, and residual array (for corr)"""
    d = S[[y] + cols].dropna()
    Y = swv(d[y].values, w); Xs = swv(d[cols].values, w, axis=0)  # (n,w) and (n,k,w)
    n = Y.shape[0]; k = len(cols)
    Xm = np.concatenate([np.ones((n, 1, w)), Xs], axis=1).transpose(0, 2, 1)  # n,w,k+1
    XtX = np.einsum("nwi,nwj->nij", Xm, Xm); XtY = np.einsum("nwi,nw->ni", Xm, Y)
    B = np.linalg.solve(XtX, XtY[..., None])[..., 0]
    fit = np.einsum("nwi,ni->nw", Xm, B); E = Y - fit
    r2 = 1 - E.var(axis=1) / Y.var(axis=1)
    idx = d.index[w - 1:]
    out = pd.DataFrame(B[:, 1:], index=idx, columns=cols); out["alpha"] = B[:, 0]; out["r2"] = r2
    out["resid_vol"] = E.std(axis=1) * np.sqrt(252); out["tot_vol"] = Y.std(axis=1) * np.sqrt(252)
    return out, pd.DataFrame(E, index=idx)


rows, un = [], []
store = {}
for w in (21, 63, 126):
    for mname, cols in MODELS.items():
        fk, ek = rolling_fit("KRE_x", cols, w); fb, eb = rolling_fit("KBWB_x", cols, w)
        common = ek.index.intersection(eb.index)
        a, b = ek.loc[common].values, eb.loc[common].values
        a = a - a.mean(1, keepdims=True); b = b - b.mean(1, keepdims=True)
        rc = pd.Series((a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1)), index=common)
        store[(w, mname)] = (fk, rc)
        for endd, lab in ((END, "to 10/30 (spliced)"), (END_FF, "to 9/30 (pure French)")):
            if endd not in fk.index: continue
            hist = fk.loc["2012-02-01":"2024-12-31"]; hrc = rc.loc["2012-02-01":"2024-12-31"]
            for c in cols:
                rows.append(dict(window=w, model=mname, end=lab, factor=c, current=fk.loc[endd, c], hist_median=hist[c].median(),
                                 hist_p10=hist[c].quantile(.1), hist_p90=hist[c].quantile(.9), pct=(hist[c] <= fk.loc[endd, c]).mean()))
            un.append(dict(window=w, model=mname, end=lab, r2=fk.loc[endd, "r2"], r2_hist_median=hist.r2.median(), r2_pct=(hist.r2 <= fk.loc[endd, "r2"]).mean(),
                           resid_vol=fk.loc[endd, "resid_vol"], resid_vol_hist_median=hist.resid_vol.median(), resid_vol_pct=(hist.resid_vol <= fk.loc[endd, "resid_vol"]).mean(),
                           tot_vol=fk.loc[endd, "tot_vol"], resid_corr_KRE_KBWB=rc.get(endd, np.nan), resid_corr_hist_median=hrc.median(),
                           resid_corr_pct=(hrc <= rc.get(endd, np.nan)).mean(), unexplained_share=1 - fk.loc[endd, "r2"]))
E = pd.DataFrame(rows); U = pd.DataFrame(un)
E.to_csv(f"{OUT}/q3_exposures.csv", index=False, float_format="%.4f"); U.to_csv(f"{OUT}/q3_unexplained.csv", index=False, float_format="%.4f")
pd.set_option("display.width", 250); pd.set_option("display.max_rows", 300)
print(E[(E.window == 63)].round(3).to_string())
print(U.round(3).to_string())

# rolling 63 series for timing chart
r63 = pd.DataFrame({f"{m}|{c}": store[(63, m)][0][c] for m in ("M2 FF3+MOM", "M3 +Δ10y") for c in MODELS[m] + ["r2"]})
r63["resid_corr_M3"] = store[(63, "M3 +Δ10y")][1]; r63["resid_corr_M0"] = store[(63, "M0 SPY")][1]; r63["resid_corr_E2"] = store[(63, "E2 RSP+CONC")][1]
r63.to_csv(f"{OUT}/q3_rolling63.csv", float_format="%.4f")

# ---- volatility-matched comparison (63d): nearest 10% of historical windows in (log KRE vol, log SPY vol)
kv = np.log(S.KRE.rolling(63).std()); sv = np.log(S.SPY.rolling(63).std())
V = pd.DataFrame({"kv": kv, "sv": sv}).loc["2012-02-01":"2024-12-31"].dropna()
cur = np.array([kv[END], sv[END]])
Z = (V - V.mean()) / V.std(); cz = (cur - V.mean().values) / V.std().values
dist = np.sqrt(((Z.values - cz) ** 2).sum(1)); near = V.index[dist <= np.quantile(dist, 0.10)]
from_q124 = pd.read_csv(f"{OUT}/rolling_63.csv", parse_dates=["date"], index_col=0)
vm = []
metrics = {"KRE beta SPY": from_q124.KRE_beta_SPY, "KRE corr SPY": from_q124.KRE_corr_SPY, "KRE corr RSP": from_q124.KRE_corr_RSP,
           "KRE corr IWN": from_q124.KRE_corr_IWN, "KRE–KBWB corr": from_q124.KRE_corr_KBWB, "KRE–KBWB partial|SPY": from_q124.partial_KRE_KBWB_SPY,
           "M3 R²": store[(63, "M3 +Δ10y")][0].r2, "M3 resid corr KRE–KBWB": store[(63, "M3 +Δ10y")][1], "E2 R² (RSP+CONC)": store[(63, "E2 RSP+CONC")][0].r2,
           "corr SPY–RSP": from_q124.corr_SPY_RSP}
for k, s in metrics.items():
    v = s[END]; h = s.reindex(near).dropna(); a = s.loc["2012-02-01":"2024-12-31"].dropna()
    vm.append(dict(metric=k, current=v, pct_all_pre2025=(a <= v).mean(), median_all=a.median(), pct_volmatched=(h <= v).mean(), median_volmatched=h.median(), n_volmatched=len(h)))
VM = pd.DataFrame(vm); VM.to_csv(f"{OUT}/q3_volmatched.csv", index=False, float_format="%.4f")
print("vol-matched: current KRE vol %.1f%%, SPY vol %.1f%%; matched windows %d, KRE vol range %.1f–%.1f%%" % (np.exp(cur[0]) * np.sqrt(252) * 100, np.exp(cur[1]) * np.sqrt(252) * 100, len(near),
      np.exp(V.loc[near].kv.min()) * np.sqrt(252) * 100, np.exp(V.loc[near].kv.max()) * np.sqrt(252) * 100))
print(VM.round(3).to_string())

# ---- out-of-sample: non-overlapping 21d blocks anchored at END; fit prior 126 sessions
idx = S.index; pe = idx.get_loc(END)
ends = [idx[i] for i in range(pe, idx.get_loc(pd.Timestamp("2013-11-01")), -21)][::-1]
O = []
for e in ends:
    i = idx.get_loc(e); test = S.iloc[i - 20:i + 1]; train = S.iloc[i - 21 - 125:i - 20]
    row = dict(end=e)
    for y in ("KRE_x", "KBWB_x"):
        for mname, cols in MODELS.items():
            tr = train[[y] + cols].dropna(); te = test[[y] + cols].dropna()
            if len(tr) < 100 or len(te) < 15: continue
            A = np.column_stack([np.ones(len(tr)), tr[cols].values]); b = np.linalg.lstsq(A, tr[y].values, rcond=None)[0]
            pred = np.column_stack([np.ones(len(te)), te[cols].values]) @ b
            row[f"{y}|{mname}|sse"] = ((te[y].values - pred) ** 2).sum(); row[f"{y}|{mname}|sst"] = ((te[y].values - tr[y].mean()) ** 2).sum()
    O.append(row)
O = pd.DataFrame(O).set_index("end"); O.to_csv(f"{OUT}/q3_oos_blocks.csv", float_format="%.6g")
per = {"2013-11→2019-12": ("2013-11-01", "2019-12-31"), "2020–2022": ("2020-01-01", "2022-12-31"), "2023–2024": ("2023-01-01", "2024-12-31"),
       "2025": ("2025-01-01", "2025-12-31"), "2026 Jan–Jun": ("2026-01-01", "2026-06-30"), "2026 Jul–Oct": ("2026-07-01", "2026-10-30")}
res = []
for y in ("KRE_x", "KBWB_x"):
    for mname in MODELS:
        for p, (a, b) in per.items():
            sub = O.loc[a:b]
            if f"{y}|{mname}|sse" not in sub: continue
            s1, s0 = sub[f"{y}|{mname}|sse"].sum(), sub[f"{y}|{mname}|sst"].sum()
            # block-level median for robustness
            med = (1 - sub[f"{y}|{mname}|sse"] / sub[f"{y}|{mname}|sst"]).median()
            res.append(dict(asset=y[:-2], model=mname, period=p, blocks=int(sub[f"{y}|{mname}|sse"].notna().sum()), oos_r2_pooled=1 - s1 / s0, oos_r2_median_block=med))
RO = pd.DataFrame(res); RO.to_csv(f"{OUT}/q3_oos.csv", index=False, float_format="%.4f")
print(RO.pivot_table(index=["asset", "model"], columns="period", values="oos_r2_pooled").round(3)[list(per)].to_string())
