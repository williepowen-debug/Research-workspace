"""Q4b: rolling (63d) decomposition of KRE's and KBWB's univariate SPY beta into factor terms b_k * beta(F_k on SPY) + residual term.
Output: out/q4b_rolling_beta_terms.csv; prints quarterly medians since 2023."""
import os, numpy as np, pandas as pd
from numpy.lib.stride_tricks import sliding_window_view as swv
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
for f in ("MKT", "SMB", "HML", "MOM"):
    X[f + "_s"] = X[f + "_ff"].where(X[f + "_ff"].notna(), X[f + "_p"])
FAC = ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10"]
X["SPY_x"] = X.SPY - X.RF
res = {}
for a in ("KRE", "KBWB"):
    X[a + "_x"] = X[a] - X.RF
    d = X[[a + "_x", "SPY_x"] + FAC].dropna().loc["2012-01-01":"2026-10-30"]
    Y = swv(d[a + "_x"].values, 63); F = swv(d[FAC].values, 63, axis=0); S = swv(d.SPY_x.values, 63); n = Y.shape[0]
    Xm = np.concatenate([np.ones((n, 1, 63)), F], axis=1).transpose(0, 2, 1)
    B = np.linalg.solve(np.einsum("nwi,nwj->nij", Xm, Xm), np.einsum("nwi,nw->ni", Xm, Y)[..., None])[..., 0][:, 1:]
    Sc = S - S.mean(1, keepdims=True); vs = (Sc ** 2).sum(1)
    Fc = F - F.mean(2, keepdims=True); fb = np.einsum("nkw,nw->nk", Fc, Sc) / vs[:, None]
    Yc = Y - Y.mean(1, keepdims=True); uni = (Yc * Sc).sum(1) / vs
    terms = B * fb
    df = pd.DataFrame(terms, columns=[f"{a}_term_{k}" for k in FAC], index=d.index[62:])
    df[f"{a}_uni"] = uni; df[f"{a}_resid_term"] = uni - terms.sum(1)
    for j, k in enumerate(FAC): df[f"{a}_load_{k}"] = B[:, j]
    if a == "KRE":
        for j, k in enumerate(FAC): df[f"fbeta_{k}"] = fb[:, j]
    res[a] = df
D = res["KRE"].join(res["KBWB"]); D.to_csv(f"{OUT}/q4b_rolling_beta_terms.csv", float_format="%.4f")
q = D.loc["2023-01-01":].resample("QE").median()
cols = ["KRE_uni", "KRE_term_MKT_s", "KRE_term_HML_s", "KRE_term_SMB_s", "KRE_term_MOM_s", "KRE_term_dy10", "KRE_load_MKT_s", "KRE_load_HML_s", "fbeta_HML_s", "fbeta_SMB_s", "KBWB_uni", "KBWB_term_MKT_s", "KBWB_term_HML_s", "KBWB_load_MKT_s"]
pd.set_option("display.width", 250); print(q[cols].round(2).to_string())
ref = D.loc["2012-03-01":"2024-12-31"]
print("pre-2025 medians:"); print(ref[cols].median().round(2).to_string())
print("now:"); print(D[cols].iloc[-1].round(2).to_string())
