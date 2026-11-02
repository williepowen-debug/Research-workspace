"""Q3b: (1) decompose the change in univariate SPY beta into loading changes vs factor-structure changes;
(2) decompose the KRE–KBWB correlation into common-factor and residual parts; (3) same M2 R²/OOS check for the predetermined nonbank set.
Reference = pooled daily regression 2012-02-01..2024-12-31; Now = 63 sessions ending 2026-10-30 (spliced factors) and 2026-09-30 (pure French).
Outputs: out/q3b_beta_decomp.csv, out/q3b_corr_decomp.csv, out/q3b_sectors_m2.csv"""
import os
import numpy as np, pandas as pd

H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
for f in ("MKT", "SMB", "HML", "MOM"):
    X[f + "_s"] = X[f + "_ff"].where(X[f + "_ff"].notna(), X[f + "_p"])
FAC = ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10"]
for t in ["KRE", "KBWB", "SPY", "IWN", "XLI", "XLF", "XLU", "IYR", "ITB", "XLB", "IYT", "KIE", "RSP"]:
    X[t + "_x"] = X[t] - X.RF


def ols(d, y, cols):
    A = np.column_stack([np.ones(len(d)), d[cols].values]); b = np.linalg.lstsq(A, d[y].values, rcond=None)[0]
    e = d[y].values - A @ b
    return pd.Series(b[1:], index=cols), e


def window(end, n=63):
    i = X.index.get_loc(pd.Timestamp(end)); return X.iloc[i - n + 1:i + 1]


REF = X.loc["2012-02-01":"2024-12-31"]
periods = {"ref 2012–2024 (pooled)": REF, "now 63d to 10/30 (spliced)": window("2026-10-30"), "now 63d to 9/30 (French)": window("2026-09-30"),
           "2025 (pooled)": X.loc["2025-01-01":"2025-12-31"], "2026 H1 (pooled)": X.loc["2026-01-01":"2026-06-30"]}
rows = []
for asset in ["KRE", "KBWB", "IWN", "XLI", "XLF", "XLU", "IYR", "ITB", "XLB", "IYT", "KIE"]:
    res = {}
    for p, d in periods.items():
        d = d[[asset + "_x", "SPY_x"] + FAC].dropna()
        b, e = ols(d, asset + "_x", FAC)
        vs = d.SPY_x.var()
        fbeta = pd.Series({k: np.cov(d[k], d.SPY_x)[0, 1] / vs for k in FAC})  # beta of each factor on SPY
        ebeta = np.cov(e, d.SPY_x)[0, 1] / vs
        uni = np.cov(d[asset + "_x"], d.SPY_x)[0, 1] / vs
        res[p] = (b, fbeta, ebeta, uni)
    b0, f0, e0, u0 = res["ref 2012–2024 (pooled)"]
    for p in periods:
        b1, f1, e1, u1 = res[p]
        row = dict(asset=asset, period=p, uni_beta_SPY=u1, resid_beta=e1)
        for k in FAC:
            row[f"load_{k}"] = b1[k]; row[f"factorbeta_{k}"] = f1[k]
            row[f"contrib_{k}"] = b1[k] * f1[k]
            row[f"dLoad_{k}"] = (b1[k] - b0[k]) * f1[k]  # change due to asset's own loading
            row[f"dStruct_{k}"] = b0[k] * (f1[k] - f0[k])  # change due to factor's co-movement with SPY
        row["dBeta_total"] = u1 - u0
        row["dBeta_from_loadings"] = sum(row[f"dLoad_{k}"] for k in FAC)
        row["dBeta_from_structure"] = sum(row[f"dStruct_{k}"] for k in FAC)
        row["dBeta_resid"] = e1 - e0
        rows.append(row)
BD = pd.DataFrame(rows); BD.to_csv(f"{OUT}/q3b_beta_decomp.csv", index=False, float_format="%.4f")
pd.set_option("display.width", 250)
cols = ["asset", "period", "uni_beta_SPY", "dBeta_total", "dBeta_from_loadings", "dBeta_from_structure", "dBeta_resid",
        "load_MKT_s", "load_HML_s", "load_SMB_s", "factorbeta_HML_s", "factorbeta_SMB_s", "contrib_HML_s", "dStruct_HML_s", "dStruct_SMB_s"]
print(BD[cols].round(3).to_string())

# (2) KRE–KBWB correlation decomposition with the same 5-factor model
cr = []
for p, d in periods.items():
    d = d[["KRE_x", "KBWB_x"] + FAC].dropna()
    bk, ek = ols(d, "KRE_x", FAC); bb, eb = ols(d, "KBWB_x", FAC)
    S = d[FAC].cov().values
    common = bk.values @ S @ bb.values; resid = np.cov(ek, eb)[0, 1]
    sk, sb = d.KRE_x.std(), d.KBWB_x.std()
    cr.append(dict(period=p, corr=d.KRE_x.corr(d.KBWB_x), from_common_factors=common / (sk * sb), from_residuals=resid / (sk * sb),
                   resid_corr=np.corrcoef(ek, eb)[0, 1], KRE_R2=1 - ek.var() / d.KRE_x.var(), KBWB_R2=1 - eb.var() / d.KBWB_x.var(),
                   KRE_vol=sk * np.sqrt(252), KBWB_vol=sb * np.sqrt(252), KRE_resid_vol=ek.std() * np.sqrt(252), KBWB_resid_vol=eb.std() * np.sqrt(252),
                   KRE_factor_vol=np.sqrt(bk.values @ S @ bk.values * 252), KBWB_factor_vol=np.sqrt(bb.values @ S @ bb.values * 252)))
CR = pd.DataFrame(cr); CR.to_csv(f"{OUT}/q3b_corr_decomp.csv", index=False, float_format="%.4f"); print(CR.round(3).to_string())

# (3) sectors: M2+Δ10y in-sample R² (63d) now vs pre-2025 rolling distribution; and 2026 Jul–Oct OOS (126d fit, 21d blocks)
from numpy.lib.stride_tricks import sliding_window_view as swv
out = []
idx = X.index; END = pd.Timestamp("2026-10-30"); pe = idx.get_loc(END)
ends = [idx[i] for i in range(pe, idx.get_loc(pd.Timestamp("2013-11-01")), -21)][::-1]
for asset in ["KRE", "KBWB", "IWN", "XLI", "XLF", "XLU", "IYR", "ITB", "XLB", "IYT", "KIE", "RSP"]:
    d = X[[asset + "_x"] + FAC].dropna().loc["2006-07-01":]
    Y = swv(d[asset + "_x"].values, 63); Xs = swv(d[FAC].values, 63, axis=0); n = Y.shape[0]
    Xm = np.concatenate([np.ones((n, 1, 63)), Xs], axis=1).transpose(0, 2, 1)
    B = np.linalg.solve(np.einsum("nwi,nwj->nij", Xm, Xm), np.einsum("nwi,nw->ni", Xm, Y)[..., None])[..., 0]
    E = Y - np.einsum("nwi,ni->nw", Xm, B); r2 = pd.Series(1 - E.var(1) / Y.var(1), index=d.index[62:])
    rv = pd.Series(E.std(1) * np.sqrt(252), index=d.index[62:])
    h = r2.loc["2012-02-01":"2024-12-31"]; hv = rv.loc["2012-02-01":"2024-12-31"]
    # OOS
    sse = {}; sst = {}
    for e in ends:
        i = idx.get_loc(e); te = X.iloc[i - 20:i + 1][[asset + "_x"] + FAC].dropna(); tr = X.iloc[i - 146:i - 20][[asset + "_x"] + FAC].dropna()
        A = np.column_stack([np.ones(len(tr)), tr[FAC].values]); b = np.linalg.lstsq(A, tr[asset + "_x"].values, rcond=None)[0]
        pr = np.column_stack([np.ones(len(te)), te[FAC].values]) @ b
        per = "hist" if e < pd.Timestamp("2025-01-01") else ("2025" if e.year == 2025 else ("2026H1" if e < pd.Timestamp("2026-07-01") else "2026JulOct"))
        sse[per] = sse.get(per, 0) + ((te[asset + "_x"].values - pr) ** 2).sum(); sst[per] = sst.get(per, 0) + ((te[asset + "_x"].values - tr[asset + "_x"].mean()) ** 2).sum()
    out.append(dict(asset=asset, r2_now=r2[END], r2_hist_median=h.median(), r2_pct=(h <= r2[END]).mean(), resid_vol_now=rv[END], resid_vol_hist_median=hv.median(),
                    resid_vol_pct=(hv <= rv[END]).mean(), **{f"oos_{k}": 1 - sse[k] / sst[k] for k in ("hist", "2025", "2026H1", "2026JulOct")}))
SO = pd.DataFrame(out); SO.to_csv(f"{OUT}/q3b_sectors_m2.csv", index=False, float_format="%.4f"); print(SO.round(3).to_string())
