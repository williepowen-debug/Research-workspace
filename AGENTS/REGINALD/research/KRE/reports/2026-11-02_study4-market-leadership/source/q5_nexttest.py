"""Calibrate the proposed next test: freeze KRE's 5-factor loadings from one 63d window, combine with the NEXT window's factor betas on SPY,
predict KRE's next-window univariate SPY beta. Historical error distribution on non-overlapping windows (anchored 2026-10-30).
Output: out/q5_frozen_loading_test.csv"""
import os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
D = pd.read_csv(f"{OUT}/q4b_rolling_beta_terms.csv", parse_dates=["date"], index_col=0)
FAC = ["MKT_s", "SMB_s", "HML_s", "MOM_s", "dy10"]
idx = D.index; pe = len(idx) - 1
ends = [idx[i] for i in range(pe, 62, -63)][::-1]
rows = []
for a, b in zip(ends[:-1], ends[1:]):
    for asset in ("KRE", "KBWB"):
        pred = sum(D.loc[a, f"{asset}_load_{k}"] * D.loc[b, f"fbeta_{k}"] for k in FAC)
        naive = D.loc[a, f"{asset}_uni"]
        rows.append(dict(asset=asset, from_end=a.date(), to_end=b.date(), realized=D.loc[b, f"{asset}_uni"], pred_frozen=pred, pred_naive=naive))
T = pd.DataFrame(rows); T["err_frozen"] = T.realized - T.pred_frozen; T["err_naive"] = T.realized - T.pred_naive
T.to_csv(f"{OUT}/q5_frozen_loading_test.csv", index=False, float_format="%.4f")
for asset in ("KRE", "KBWB"):
    t = T[T.asset == asset]; h = t[pd.to_datetime(t.to_end) < pd.Timestamp("2025-01-01")]
    print(asset, "n hist", len(h), "frozen-loading err sd %.3f mean %.3f | naive err sd %.3f" % (h.err_frozen.std(), h.err_frozen.mean(), h.err_naive.std()),
          "| p10/p90 frozen err %.2f / %.2f" % (h.err_frozen.quantile(.1), h.err_frozen.quantile(.9)))
    print(t.tail(4).round(3).to_string())
# current loadings to freeze
print(D[[f"KRE_load_{k}" for k in FAC]].iloc[-1].round(3).to_dict())
