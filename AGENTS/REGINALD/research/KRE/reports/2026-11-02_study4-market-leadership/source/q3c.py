"""Q3c: (a) does the value factor carry the negative rate sensitivity? (HML_p and KRE on SPY+Δ10y, 63d); (b) KRE cumulative residual (alpha) over the window vs history."""
import os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
Q = pd.read_csv(f"{OUT}/q3_rolling63.csv", parse_dates=["date"], index_col=0)
END = pd.Timestamp("2026-10-30")
def two(y, w=63):
    d = X[[y, "SPY", "dy10"]].dropna(); out = {}
    for e in d.index[w - 1:]:
        pass
from numpy.lib.stride_tricks import sliding_window_view as swv
def rate_beta(y):
    d = X[[y, "SPY", "dy10"]].dropna().loc["2012-01-01":"2026-10-30"]
    Y = swv(d[y].values, 63); F = swv(d[["SPY", "dy10"]].values, 63, axis=0); n = len(Y)
    Xm = np.concatenate([np.ones((n, 1, 63)), F], axis=1).transpose(0, 2, 1)
    B = np.linalg.solve(np.einsum("nwi,nwj->nij", Xm, Xm), np.einsum("nwi,nw->ni", Xm, Y)[..., None])[..., 0]
    return pd.Series(B[:, 2], index=d.index[62:])
rows = []
for y in ("HML_p", "KRE", "KBWB", "IWN", "XLF"):
    s = rate_beta(y); h = s.loc["2012-03-01":"2024-12-31"]
    rows.append(dict(series=y, rate_beta_now=s[END], pct_pre2025=(h <= s[END]).mean(), median_pre2025=h.median(), median_2026=s.loc["2026"].median()))
RB = pd.DataFrame(rows); RB.to_csv(f"{OUT}/q3c_rate_beta_value.csv", index=False, float_format="%.4f"); print(RB.round(3).to_string())
# KRE M3 window alpha (cumulative, 63d) vs history
# (b) 63d cumulative 5-factor alpha vs history
FAC = ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10"]
for f_ in ("MKT", "SMB", "HML", "MOM"):
    X[f_ + "_s"] = X[f_ + "_ff"].where(X[f_ + "_ff"].notna(), X[f_ + "_p"])
out = {}
for a in ("KRE", "KBWB", "IWN", "XLF"):
    d = X[[a, "RF"] + FAC].dropna().loc["2012-01-01":"2026-10-30"]; y = (d[a] - d.RF).values
    Y = swv(y, 63); F = swv(d[FAC].values, 63, axis=0); n = len(Y)
    Xm = np.concatenate([np.ones((n, 1, 63)), F], axis=1).transpose(0, 2, 1)
    B = np.linalg.solve(np.einsum("nwi,nwj->nij", Xm, Xm), np.einsum("nwi,nw->ni", Xm, Y)[..., None])[..., 0]
    s = pd.Series(B[:, 0] * 63, index=d.index[62:]); h = s.loc["2012-03-01":"2024-12-31"]; nov = h.iloc[::63]
    print(a, "63d alpha now %.3f pct %.3f z(non-overlap) %.2f" % (s.iloc[-1], (h <= s.iloc[-1]).mean(), (s.iloc[-1] - nov.mean()) / nov.std()))
    out[a] = s
pd.DataFrame(out).to_csv(f"{OUT}/q3c_alpha63.csv", float_format="%.4f")
