"""Q4 timing: when did each relationship change? Rolling 63d series + non-overlapping 21d blocks since 2024-01.
Adds market-structure series (HML-on-SPY beta, SPY–RSP corr, QQQ–RSP corr) and KRE's own factor loadings (M3).
Outputs: out/q4_timeline.csv, out/q4_onsets.csv, out/q4_blocks.csv, out/fig_timeline.png"""
import os
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"
X = pd.read_csv(f"{H}/data/panel.csv", parse_dates=["date"], index_col=0)
R6 = pd.read_csv(f"{OUT}/rolling_63.csv", parse_dates=["date"], index_col=0)
Q3 = pd.read_csv(f"{OUT}/q3_rolling63.csv", parse_dates=["date"], index_col=0)
W = 63
T = pd.DataFrame({
    "HMLp_beta_on_SPY": X.HML_p.rolling(W).cov(X.SPY) / X.SPY.rolling(W).var(),
    "HMLff_beta_on_MKTff": X.HML_ff.rolling(W).cov(X.MKT_ff) / X.MKT_ff.rolling(W).var(),
    "corr_SPY_RSP": R6.corr_SPY_RSP, "corr_QQQ_RSP": X.QQQ.rolling(W).corr(X.RSP),
    "KRE_beta_SPY": R6.KRE_beta_SPY, "KRE_beta_RSP": R6.KRE_beta_RSP, "KBWB_beta_SPY": R6.KBWB_beta_SPY,
    "KRE_corr_IWN": R6.KRE_corr_IWN, "KRE_corr_KBWB": R6.KRE_corr_KBWB,
    "KRE_M3_MKT": Q3["M3 +Δ10y|MKT_s"], "KRE_M3_HML": Q3["M3 +Δ10y|HML_s"], "KRE_M3_dy10": Q3["M3 +Δ10y|dy10"], "KRE_M3_R2": Q3["M3 +Δ10y|r2"],
    "resid_corr_KRE_KBWB_M3": Q3.resid_corr_M3, "IWN_beta_SPY": R6.IWN_beta_SPY, "XLI_beta_SPY": R6.XLI_beta_SPY})
T.loc[:"2026-10-30"].to_csv(f"{OUT}/q4_timeline.csv", float_format="%.4f")
ref = T.loc["2012-02-01":"2024-12-31"]
on = []
for c in T.columns:
    lo, hi = ref[c].quantile(.10), ref[c].quantile(.90)
    for yr in ("2025", "2026"):
        s = T[c].loc[yr]
        for side, m in (("below p10", s < lo), ("above p90", s > hi)):
            b = m.astype(int); run = b.groupby((b != b.shift()).cumsum()).transform("sum") * b
            hit = run[run >= 10]
            on.append(dict(series=c, year=yr, side=side, threshold=lo if side == "below p10" else hi, share_days=m.mean(),
                           first_onset_10d=hit.index.min().date() if len(hit) else None))
ON = pd.DataFrame(on); ON = ON[ON.share_days > 0]; ON.to_csv(f"{OUT}/q4_onsets.csv", index=False, float_format="%.3f")
pd.set_option("display.width", 220); print(ON.round(3).to_string())

# 21-day non-overlapping blocks
END = pd.Timestamp("2026-10-30"); idx = X.index; pe = idx.get_loc(END)
ends = [idx[i] for i in range(pe, idx.get_loc(pd.Timestamp("2024-01-31")), -21)][::-1]
B = []
for e in ends:
    i = idx.get_loc(e); w = X.iloc[i - 20:i + 1]
    B.append(dict(end=e.date(), HMLp_beta_SPY=w.HML_p.cov(w.SPY) / w.SPY.var(), corr_SPY_RSP=w.SPY.corr(w.RSP),
                  KRE_beta_SPY=w.KRE.cov(w.SPY) / w.SPY.var(), KRE_beta_RSP=w.KRE.cov(w.RSP) / w.RSP.var(), KBWB_beta_SPY=w.KBWB.cov(w.SPY) / w.SPY.var(),
                  KRE_corr_KBWB=w.KRE.corr(w.KBWB), KRE_corr_IWN=w.KRE.corr(w.IWN), QQQ_minus_RSP_ret=(1 + w.QQQ).prod() - (1 + w.RSP).prod(),
                  KRE_minus_KBWB_ret=(1 + w.KRE).prod() - (1 + w.KBWB).prod()))
BL = pd.DataFrame(B); BL.to_csv(f"{OUT}/q4_blocks.csv", index=False, float_format="%.3f"); print(BL.round(2).to_string())

# figure
fig, ax = plt.subplots(4, 1, figsize=(13, 12), sharex=True)
s = T.loc["2023-07-01":"2026-10-30"]
def band(a, c):
    a.axhspan(ref[c].quantile(.1), ref[c].quantile(.9), color="gray", alpha=0.12)
ax[0].plot(s.corr_SPY_RSP, label="corr SPY–RSP (63d)", c="k"); band(ax[0], "corr_SPY_RSP")
ax[0].plot(s.HMLp_beta_on_SPY, label="value (IWD−IWF) beta on SPY", c="tab:orange"); band(ax[0], "HMLp_beta_on_SPY")
ax[0].legend(fontsize=8, loc="lower left"); ax[0].set_title("Market structure (gray bands = 10th–90th pct, 2012–2024)")
ax[1].plot(s.KRE_beta_SPY, label="KRE beta on SPY", c="tab:blue"); ax[1].plot(s.KRE_beta_RSP, label="KRE beta on RSP", c="tab:cyan")
ax[1].plot(s.KBWB_beta_SPY, label="KBWB beta on SPY", c="tab:green"); ax[1].plot(s.KRE_M3_MKT, label="KRE market loading in 5-factor model", c="tab:red", ls="--")
band(ax[1], "KRE_beta_SPY"); ax[1].legend(fontsize=8, loc="lower left"); ax[1].set_title("Market sensitivities")
ax[2].plot(s.KRE_corr_KBWB, label="corr KRE–KBWB", c="k"); ax[2].plot(s.resid_corr_KRE_KBWB_M3, label="residual corr after 5 factors", c="tab:purple")
ax[2].plot(s.KRE_corr_IWN, label="corr KRE–IWN", c="tab:olive"); band(ax[2], "KRE_corr_KBWB"); ax[2].legend(fontsize=8, loc="lower left"); ax[2].set_title("Co-movement")
ax[3].plot(s.KRE_M3_HML, label="KRE value (HML) loading", c="tab:orange"); ax[3].plot(s.KRE_M3_dy10 * 10, label="KRE Δ10y loading ×10", c="tab:brown")
ax[3].plot(s.KRE_M3_R2, label="5-factor R²", c="gray"); ax[3].axhline(0, c="k", lw=.5); ax[3].legend(fontsize=8, loc="lower left"); ax[3].set_title("KRE factor loadings (63d)")
for a in ax:
    for d in ("2025-01-01", "2026-06-01", "2026-08-03"): a.axvline(pd.Timestamp(d), c="r", lw=.6, ls=":")
plt.tight_layout(); plt.savefig(f"{OUT}/fig_timeline.png", dpi=110)
